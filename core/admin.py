from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rest_framework.authtoken.models import Token
from django import forms
from .models import *


admin.site.site_header = 'Администрация'


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('id', 'username', 'name', 'phone_number', 'email')
    ordering = ('-created_at',)
    list_display = ('username', 'name', 'phone_number', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'name', 'email', 'phone_number', 'status', 'is_superuser', 'password', 'created_at', 'updated_at',)},
         ),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'name', 'email', 'phone_number', 'status', 'password1', 'password2', 'is_superuser',)}
         ),
    )
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, UserAdminConfig)

class PagesAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Pages
        fields = '__all__'

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'published',) 
    list_display_links = ('id', 'title',)
    list_filter = ['user_id']
    search_fields = ('title', 'user_id',)
    readonly_fields = ('created_at', 'updated_at')
    form = PagesAdminForm


class PostsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'published',)
    list_display_links = ('id', 'title',)
    list_filter = ['user_id',]
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'user_id',)
    form = PostsAdminForm


@admin.register(ProductsImages)
class ProductsImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_img', 'get_img_url']
    list_display_links = ('id', 'get_img',)
    readonly_fields = ('get_img_url', 'get_img', 'created_at', 'updated_at')
    fields = ('image', 'get_img', 'get_img_url')

    def get_img_url(self, obj):
        return f'{obj.image.url}'
    
    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width: 15rem;">')


    
    get_img.short_description = 'Картина'
    get_img_url.short_description = 'Ссылка картины'


@admin.register(Discounts)
class DiscountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rate','rate_type',)
    list_display_links = ('id', 'name',)
    list_filter = ['rate_type']
    search_fields = ['name']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Taxes)
class TaxesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rate','rate_type',)
    list_display_links = ('id', 'name',)
    list_filter = ['rate_type']
    search_fields = ['name']
    readonly_fields = ('created_at', 'updated_at')


class CategoriesAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание  о категории', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Categories
        fields = '__all__'



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_id',)
    list_display_links = ('id', 'name',)
    list_filter = ['parent_id']
    search_fields = ['name']
    readonly_fields = ('created_at', 'updated_at')
    form = CategoriesAdminForm


@admin.register(AttributesTitles)
class AttributesTitlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title',)
    search_fields = ['title']
    readonly_fields = ('created_at', 'updated_at')


class AttributesAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Attributes
        fields = '__all__'


@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute_title_id', 'value')
    list_display_links = ('id', 'attribute_title_id',)
    list_filter = ['attribute_title_id']
    search_fields = ['value']
    readonly_fields = ('created_at', 'updated_at')
    form = AttributesAdminForm


class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание товара', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Products
        fields = '__all__'


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'maker', 
        'category_id',
        'cost_price', 
        'markup', 
        'markup_type', 
        'sale_price_no_taxes', 
        'sale_price',
        'get_img'
     )
    list_display_links = ('id', 'name')
    list_filter = ['category_id','markup_type',]
    search_fields = ['name',]

    readonly_fields = ('get_img', 'created_at', 'updated_at', 'get_imgs', 'get_logo_compony','detailAttr')
    fields = (
        'created_at',
        'updated_at',
        'name',
        'get_logo_compony',
        'maker',
        'main_image', 
        'images',
        'category_id',
        'short_description',
        'description',
        'attributes',
        'detailAttr',
        'cost_price', 
        'markup', 
        'markup_type', 
        'sale_price_no_taxes', 
        'sale_price',
        'get_img',
        'get_imgs',
        
    )
    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.main_image.image.url}" style="width: 15rem;">')

    def get_logo_compony(self, obj):
        return mark_safe(f'<img src="{obj.maker.logo.url}" style="width: 4rem;">')

    def get_imgs(self, obj):
        temp = ''
        for image in obj.images.all():
            temp = temp + f'<div style="margin-bottom: 10px"><img src="{image}" style="width: 15rem;"></div>'
        return mark_safe(temp)
    
    def detailAttr(self, obj):
        temp = ''
        for attr in obj.attributes.all():
            temp = temp + f'<p>{attr.attribute_title_id}: {attr.value}</p>'

        return mark_safe(temp)

    detailAttr.short_description = 'Атрибуты'
    get_img.short_description = 'Главная картина'
    get_imgs.short_description = 'Картины'
    get_logo_compony.short_description = 'Логотип производителя'

    form = ProductsAdminForm


class ProductsDiscountsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание скидки', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = ProductsDiscounts
        fields = '__all__'


@admin.register(ProductsDiscounts)
class ProductsDiscountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'discount_id', 'start_date', 'end_date', )
    list_display_links = ('id', 'product_id',)
    list_filter = ['product_id', 'start_date',]
    search_fields = ('product_id', 'discount_id')
    readonly_fields = ('created_at', 'updated_at')
    form = ProductsDiscountsAdminForm



@admin.register(DeliveriesType)
class DeliveriesTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title',)
    search_fields = ['title']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(DeliveriesStatus)
class DeliveriesStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title',)
    search_fields = ['title']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'full_name',
        'phone_1',
        'phone_2',
        'address',
        'delivery_type',
        'status',
        'total_price',
        'total_price_discount',
    )
    list_display_links = ('id', 'full_name',)
    list_filter = ['delivery_type', 'status',]
    search_fields = (
        'full_name',
        'phone_1',
        'phone_2',
        'address',
        )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(OrdersDetails)
class OrdersDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'order_id',
        'product_id',
        'discount_sum',
        'sale_price',
        'quantity',
        'total_price',
        'total_price_discount',
    )
    list_display_links = ('id', 'order_id',)
    list_filter = ['product_id']
    search_fields = []


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title',)
    search_fields = ['title']    


@admin.register(RateTypes)
class RateTypesAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'slug')
    list_display_links = ('id', 'title',)
    list_filter = []
    search_fields = ['title', 'slug']
    fields = ('title', 'slug', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at')
    

class MakerOfProductsAdminForm(forms.ModelForm):
    
    description = forms.CharField(label='Описание компании', widget=CKEditorUploadingWidget())

    class Meta:
        model = MakerOfProducts
        fields = '__all__'


@admin.register(MakerOfProducts)
class MakerOfProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'country','get_img')
    list_display_links = ('id', 'title',)
    search_fields = ['title',]

    fields = ('title', 'description', 'country','logo','get_img', 'created_at', 'updated_at')
    readonly_fields = ['get_img', 'created_at', 'updated_at']
    
    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="width: 5rem;">')

    get_img.short_description = 'Логотип'

    form = MakerOfProductsAdminForm
    

@admin.register(UsersStatus)
class UserStatusAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title',)

# Register your models here.
