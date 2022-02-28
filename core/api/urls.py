from django.urls import path, include
from core.api.views import *
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('swagger/', get_swagger_view(title='Pastebin API')),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
    
    path('products/', ProductsApiView.as_view()),
    path('products/<int:pk>/', ProductsDetailApiView.as_view()),
    path('products/<int:pk>/delete/', ProductsDeleteApiView.as_view()),
    path('products/create/', ProductsCreateApiView.as_view()),
    path('products/<int:pk>/update/', ProductsUpdateApiView.as_view()),
    
    path('categories/', CategoriesApiView.as_view()),
    path('categories/<int:pk>/', CategoriesDetailApiView.as_view()),
    path('categories/<int:pk>/delete/', CategoriesDeleteApiView.as_view()),
    path('categories/create/', CategoriesCreateApiView.as_view()),
    path('categories/<int:pk>/update/', CategoriesUpdateApiView.as_view()),

    path('attributes_titles/', AttributesTitlesApiView.as_view()),
    path('attributes_titles/<int:pk>/', AttributesTitlesDetailApiView.as_view()),
    path('attributes_titles/<int:pk>/delete/', AttributesTitlesDeleteApiView.as_view()),
    path('attributes_titles/create/', AttributesTitlesCreateApiView.as_view()),
    path('attributes_titles/<int:pk>/update/', AttributesTitlesUpdateApiView.as_view()),

    path('pages/', PagesApiView.as_view()),
    path('pages/<int:pk>/', PagesDetailApiView.as_view()),
    path('pages/<int:pk>/delete/', PagesDeleteApiView.as_view()),
    path('pages/create/', PagesCreateApiView.as_view()),
    path('pages/<int:pk>/update/', PagesUpdateApiView.as_view()),

    path('posts/', PostsApiView.as_view()),
    path('posts/<int:pk>/', PostsDetailApiView.as_view()),
    path('posts/<int:pk>/delete/', PostsDeleteApiView.as_view()),
    path('posts/create/', PostsCreateApiView.as_view()),
    path('posts/<int:pk>/update/', PostsUpdateApiView.as_view()),

    path('discounts/', DiscountsApiView.as_view()),
    path('discounts/<int:pk>/', DiscountsDetailApiView.as_view()),
    path('discounts/<int:pk>/delete/', DiscountsDeleteApiView.as_view()),
    path('discounts/create/', DiscountsCreateApiView.as_view()),
    path('discounts/<int:pk>/update/', DiscountsUpdateApiView.as_view()),

    path('taxes/', TaxesApiView.as_view()),
    path('taxes/<int:pk>/', TaxesDetailApiView.as_view()),
    path('taxes/<int:pk>/delete/', TaxesDeleteApiView.as_view()),
    path('taxes/create/', TaxesCreateApiView.as_view()),
    path('taxes/<int:pk>/update/', TaxesUpdateApiView.as_view()),

    path('products_images/', ProductsImagesApiView.as_view()),
    path('products_images/<int:pk>/', ProductsImagesDetailApiView.as_view()),
    path('products_images/<int:pk>/delete/', ProductsImagesDeleteApiView.as_view()),
    path('products_images/create/', ProductsImagesCreateApiView.as_view()),

    path('сountries/', CountriesApiView.as_view()),
    path('сountries/<int:pk>/', CountriesDetailApiView.as_view()),
    path('сountries/<int:pk>/delete/', CountriesDeleteApiView.as_view()),
    path('сountries/create/', CountriesCreateApiView.as_view()),
    path('сountries/<int:pk>/update/', CountriesUpdateApiView.as_view()),

    path('сountries/', CountriesApiView.as_view()),
    path('сountries/<int:pk>/', CountriesDetailApiView.as_view()),
    path('сountries/<int:pk>/delete/', CountriesDeleteApiView.as_view()),
    path('сountries/create/', CountriesCreateApiView.as_view()),
    path('сountries/<int:pk>/update/', CountriesUpdateApiView.as_view()),
 
    path('maker_of_products/', MakerOfProductsApiView.as_view()),
    path('maker_of_products/<int:pk>/', MakerOfProductsDetailApiView.as_view()),
    path('maker_of_products/<int:pk>/delete/', MakerOfProductsDeleteApiView.as_view()),
    path('maker_of_products/create/', MakerOfProductsCreateApiView.as_view()),
    path('maker_of_products/<int:pk>/update/', MakerOfProductsUpdateApiView.as_view()),
 
    path('deliveries_type/', DeliveriesTypeApiView.as_view()),
    path('deliveries_type/<int:pk>/', DeliveriesTypeDetailApiView.as_view()),
    path('deliveries_type/<int:pk>/delete/', DeliveriesTypeDeleteApiView.as_view()),
    path('deliveries_type/create/', DeliveriesTypeCreateApiView.as_view()),
    path('deliveries_type/<int:pk>/update/', DeliveriesTypeUpdateApiView.as_view()),
 
    path('deliveriess_status/', DeliveriesStatusApiView.as_view()),
    path('deliveriess_status/<int:pk>/', DeliveriesStatusDetailApiView.as_view()),
    path('deliveriess_status/<int:pk>/delete/', DeliveriesStatusDeleteApiView.as_view()),
    path('deliveriess_status/create/', DeliveriesStatusCreateApiView.as_view()),
    path('deliveriess_status/<int:pk>/update/', DeliveriesStatusUpdateApiView.as_view()),
 
    path('orders/', OrdersApiView.as_view()),
    path('orders/<int:pk>/', OrdersDetailApiView.as_view()),
    path('orders/<int:pk>/delete/', OrdersDeleteApiView.as_view()),
    path('orders/create/', OrdersCreateApiView.as_view()),
    path('orders/<int:pk>/update/', OrdersUpdateApiView.as_view()),

    path('orders_details/', OrdersDetailsApiView.as_view()),
    path('orders_details/<int:pk>/', OrdersDetailsDetailApiView.as_view()),
    path('orders_details/<int:pk>/delete/', OrdersDetailsDeleteApiView.as_view()),
    path('orders_details/create/', OrdersDetailsCreateApiView.as_view()),
    path('orders_details/<int:pk>/update/', OrdersDetailsUpdateApiView.as_view()),
   
    path('attributes/filter/', AttributesFilterApiView.as_view()),
    path('attributes/', AttributesApiView.as_view()),
    path('attributes/<int:pk>/', AttributesDetailApiView.as_view()),
    path('attributes/<int:pk>/delete/', AttributesDeleteApiView.as_view()),
    path('attributes/create/', AttributesCreateApiView.as_view()),
    path('attributes/<int:pk>/update/', AttributesUpdateApiView.as_view()),
]
