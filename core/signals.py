from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save, post_save
from .models import Products, ProductsImages, Taxes, RateTypes, User

@receiver(pre_delete, sender=Products)
def pre_delete_products(instance, **kwargs):
    temp = instance.main_image.id

    instance.main_image = None
    instance.save()

    ProductsImages.objects.get(id=temp).delete()

    instance.attributes.all().delete()
    instance.images.all().delete()

@receiver(pre_save, sender=Products)
def post_save_products(instance, **kwargs):
    markup_type = RateTypes.objects.get(id=instance.markup_type.id)
    if markup_type.slug == 'percent':
        instance.sale_price_no_taxes = instance.cost_price + (instance.cost_price * instance.markup)
    
    else:
        instance.sale_price_no_taxes = instance.cost_price + instance.markup

    tax = Taxes.objects.first()

    if tax.rate_type.slug == 'percent':
        instance.sale_price = instance.sale_price_no_taxes + (instance.cost_price * tax.rate)

    else:
         instance.sale_price = instance.sale_price_no_taxes + tax.rate
    
    return instance


# @receiver(pre_save, sender=User)
# def pre_save_user(instance, **kwargs):
#     # if instance.status.filter(slug='admin').exists():
#     #     instance.is_superuser = True

#     return instance  
