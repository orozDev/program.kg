from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from core.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'phone_number', 'status',)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'phone_number', 'status', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ProductsSerializer(serializers.ModelSerializer):

    category_id = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    maker = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    images = serializers.StringRelatedField(many=True)
   

    class Meta:
        model = Products
        fields = (
            'id',
            'created_at',
            'updated_at',
            'name',
            'maker',
            'main_image', 
            'images',
            'category_id',
            'short_description',
            'description',
            'attributes',
            'sale_price',
        )


class ProductsCRUDSerializer(serializers.ModelSerializer):
    markup_type = serializers.SlugRelatedField(many=False, read_only=True, slug_field='slug')
    class Meta: 
        model = Products
        fields = (
            'name',
            'short_description',
            'description',
            'category_id',
            'attributes',
            'cost_price',
            'main_image',
            'images',
            'maker',
            'markup',
            'markup_type',
        )


class AttributesSerializers(serializers.ModelSerializer):

    attribute_title_id = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Attributes
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Categories
        fields = '__all__'



class PagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Posts
        fields = '__all__'


class DiscountsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Discounts
        fields = '__all__'


class TaxesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Taxes
        fields = '__all__'


class AttributesTitlesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AttributesTitles
        fields = '__all__'

class ProductsImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductsImages
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Countries
        fields = '__all__'


class MakerOfProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MakerOfProducts
        fields = '__all__'


class DeliveriesTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeliveriesType
        fields = '__all__'



class DeliveriesStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeliveriesStatus
        fields = '__all__'



class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = '__all__'



class OrdersDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrdersDetails
        fields = '__all__'
