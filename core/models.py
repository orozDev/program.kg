from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Дата создания и Дата обновления используется как миксин (наследование) для всех таблиц
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


#Тип как процент или наличная сумма
class RateTypes(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name='Slug название')

    def __str__(self):
        return self.title


# Программный менеджер для регистрации пользователя через shell 
class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, username, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, name, password, **other_fields)

    def create_user(self, username, name, password, **other_fields):

        user = self.model(username=username,
                          name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


#Таблица названии статусов пользователя
class UsersStatus(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователей'
        ordering = ['-updated_at']
        
    title = models.CharField(max_length=100, verbose_name='Наименование статуа')
    slug = models.SlugField(verbose_name='Slug название', default=None)

    def __str__(self):
        return self.title



# Таблица пользователя 
class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
        ordering = ['-updated_at']

    username = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    name = models.CharField(max_length=150, blank=True, verbose_name='Полное имя')
    email = models.EmailField(verbose_name='Элетронная почта')
    status = models.ManyToManyField('UsersStatus', verbose_name='Статус(ы) пользователя')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True)

    is_staff = models.BooleanField(default=True, verbose_name='Подтверждение')
    is_active = models.BooleanField(default=True,)
    is_superuser = models.BooleanField(default=False, verbose_name='Статус администратора')
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'phone_number', 'status']

    def __str__(self):
        return f'{self.username}'



# Страницы для контента
class Pages(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    content = models.TextField(verbose_name='Контент страницы')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    published = models.BooleanField(verbose_name='Статус видимости', default=False)

    def __str__(self):
        return self.title


# Таблица: Посты & Новости & Объявления
class Posts(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    content = models.TextField(verbose_name='Контент поста')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    published = models.BooleanField(verbose_name='Статус видимости', default=False)

    def __str__(self):
        return self.title


# Таблица свойство скидки: название, значение, тип значении
class Discounts(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        ordering = ['-updated_at']
    
    name = models.CharField(max_length=255, verbose_name='Название скидки')
    rate = models.DecimalField(verbose_name='Цифра в скидках', max_digits=20, decimal_places=2)
    rate_type = models.ForeignKey('RateTypes', on_delete=models.CASCADE, null=True, verbose_name='Тип значение скидки')
    
    def __str__(self):
        return self.name


# Таблица налогов (НДС)   
class Taxes(TimeStampMixin):

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'
        ordering = ['-updated_at']

    name = models.CharField(max_length=255, verbose_name='Название налога')
    rate = models.DecimalField(verbose_name='Значение налога', max_digits=20, decimal_places=2)
    rate_type = models.ForeignKey('RateTypes', on_delete=models.CASCADE, null=True, verbose_name='Тип значение налога')
    
    def __str__(self):
        return self.name


# Таблица категории товаров
class Categories(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-updated_at']

    name = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание о категории')
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, verbose_name='Родительская категория', blank=True)


    def __str__(self):
        return self.name
    

# Таблица название атрибутов
class AttributesTitles(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Название атрибута'
        verbose_name_plural = 'Название атрибутов'
        ordering = ['-updated_at']
    
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title


# Таблица атрибутов товара  
class Attributes(TimeStampMixin):
    
    class Meta:
        
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'
        ordering = ['-updated_at']

    attribute_title_id = models.ForeignKey('AttributesTitles', on_delete=models.CASCADE, null=True, verbose_name='Название аттрибута')
    value = models.CharField(max_length=255, verbose_name='Значение')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.attribute_title_id.title}: {self.value}'

# Картинки для товара
class ProductsImages(TimeStampMixin):

    class Meta:
        verbose_name = 'Картина товара'
        verbose_name_plural = 'Картины товаров'
        ordering = ['-updated_at']

    image = models.ImageField(upload_to='products/images/', verbose_name='Картина')

    def __str__(self):
        return f'http://127.0.0.1:8000{self.image.url}'

#Таблица стран
class Countries(TimeStampMixin):

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Название страны')

    def __str__(self):
        return self.title


# Таблица производителей
class MakerOfProducts(TimeStampMixin):

    class Meta:
        verbose_name = 'Призводитель'
        verbose_name_plural = 'Призводители'
        ordering = ['-updated_at']

    logo = models.ImageField(upload_to='makers/images/', verbose_name='Логотип')
    country = models.ForeignKey('Countries', on_delete=models.CASCADE, null=True, verbose_name='Страна')
    title = models.CharField(max_length=255, verbose_name='Название компании производителей')
    description = models.TextField(verbose_name='Описание компании')

    def __str__(self) -> str:
        return self.title


# Перечень товаров
class Products(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-updated_at']

    name = models.CharField(max_length=255, verbose_name='Имя товара')
    short_description = models.TextField(verbose_name='краткое описание товара')
    description = models.TextField(verbose_name='Описание товара')
    category_id = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True, verbose_name='Категория')
    attributes = models.ManyToManyField('Attributes', verbose_name='Атрибуты')
    cost_price = models.DecimalField(verbose_name='Себестоимость', max_digits=20, decimal_places=2)
    main_image = models.ForeignKey('ProductsImages', on_delete=models.SET_NULL, null=True, verbose_name='Главная картина')
    images = models.ManyToManyField('ProductsImages', verbose_name='Картины товаров', related_name='productsImages')
    maker = models.ForeignKey('MakerOfProducts', on_delete=models.CASCADE, null=True, verbose_name='Производитель')
    markup = models.DecimalField(verbose_name='Надбавка', max_digits=20, decimal_places=2)
    markup_type = models.ForeignKey('RateTypes', on_delete=models.CASCADE, null=True, verbose_name='Тип надбавки')
    sale_price_no_taxes = models.DecimalField(verbose_name='Продажная цена без НДС', max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(verbose_name='Вычисление с учетом налога', max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name


# Товары со скидками 
class ProductsDiscounts(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Товар со скидкой'
        verbose_name_plural = 'Товары со скидками'
        ordering = ['-updated_at']

    product_id = models.ForeignKey('Products', on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    discount_id = models.ForeignKey('Discounts', on_delete=models.CASCADE, null=True, verbose_name='свойство cкидка')
    description = models.TextField(verbose_name='Описание скидки')
    start_date = models.DateField(default=timezone.now, verbose_name='Начало скидки')
    end_date = models.DateField(default=timezone.now, verbose_name='Конец скидки')

    def __str__(self) :
        return f'{self.product_id.name} - {self.discount_id.name}'


# Таблица наименование способов доставки: самовывоз, курьерская доставка, платная доставка.
class DeliveriesType(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Наименование доставки'
        verbose_name_plural = 'Наименовании доставок'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self) :
        return self.title


# таблица наименование статусов доставки товара: новый заказ, подтвержденный заказ, отмененный заказ, выполненный заказ
class DeliveriesStatus(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Статус доставки'
        verbose_name_plural = 'Статусы доставок'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self) :
        return self.title

# Таблица заказов
class Orders(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-updated_at']

    full_name = models.CharField(max_length=400, verbose_name='ФИО')
    phone_1 = models.CharField(max_length=15, verbose_name='Первый номер телефона')
    phone_2 = models.CharField(max_length=15, verbose_name='Второй номер телефона', null=True, blank=True)
    address = models.CharField(max_length=400, verbose_name='Адрес')
    information = models.TextField(verbose_name='Дополнительная информация')
    delivery_type = models.ForeignKey('DeliveriesType', on_delete=models.CASCADE, null=True, verbose_name='Способ доставки')
    status = models.ForeignKey('DeliveriesStatus', on_delete=models.CASCADE, null=True, verbose_name='Статус доставки')
    total_price = models.DecimalField(verbose_name='Общая сумма заказа без скидок', max_digits=20, decimal_places=2)
    total_price_discount = models.DecimalField(verbose_name='Общая сумма заказа с учетом скидок', max_digits=20, decimal_places=2)

    def __str__(self) :
        return f'{self.full_name} - {self.status.title}'


# Список заказных товаров
class OrdersDetails(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Список заказа'
        verbose_name_plural = 'Списки заказов'
        ordering = ['-updated_at']

    order_id = models.ForeignKey('Orders', on_delete=models.CASCADE, null=True, verbose_name='Заказ')
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE, null=True, verbose_name='Товар')
    discount_sum = models.PositiveIntegerField(verbose_name='сумма скидки в цифрах')
    sale_price = models.DecimalField(verbose_name='цена товара', max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    total_price = models.DecimalField(verbose_name='Общая сумма без учета скидки', max_digits=20, decimal_places=2)
    total_price_discount = models.DecimalField(verbose_name=' сумма с учетом скидок', max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.order_id}'

# Create your models here.
