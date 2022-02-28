from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status as Status
from core.api.serializers import *
from core.models import *

#____________________Others_________________


class ProductsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class CustomIsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True     
        return False


#_______________________VIEW____________________________



#______________________Products_________________________

class ProductsApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (AllowAny,)
    pagination_class  = ProductsPagination


class ProductsDetailApiView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Products.objects.get(id=pk)
            serializer = ProductsSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данного товара по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class ProductsDeleteApiView(RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    permission_classes = (CustomIsAdminUser,)
    serializer_class = ProductsCRUDSerializer


class ProductsCreateApiView(CreateAPIView):
    serializer_class = ProductsCRUDSerializer
    permission_classes = (CustomIsAdminUser,)


class ProductsUpdateApiView(RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCRUDSerializer
    permission_classes = (CustomIsAdminUser,)


#_________________________________________CATEGORY___________________________________________________________


class CategoriesApiView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (AllowAny,)



class CategoriesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Categories.objects.get(id=pk)
            serializer = CategoriesSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данной категории по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class CategoriesDeleteApiView(RetrieveDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (CustomIsAdminUser,)



class CategoriesCreateApiView(CreateAPIView):
    serializer_class = CategoriesSerializer
    permission_classes = (CustomIsAdminUser,)


class CategoriesUpdateApiView(RetrieveUpdateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________AttributesTitles__________________



class AttributesTitlesApiView(ListAPIView):

    queryset = AttributesTitles.objects.all()
    serializer_class = AttributesTitlesSerializer
    permission_classes = (CustomIsAdminUser,)


class AttributesTitlesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = AttributesTitles.objects.get(id=pk)
            serializer = AttributesTitlesSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данной имя атрибута по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class AttributesTitlesDeleteApiView(RetrieveDestroyAPIView):
    queryset = AttributesTitles.objects.all()
    serializer_class = AttributesTitlesSerializer
    permission_classes = (CustomIsAdminUser,)



class AttributesTitlesCreateApiView(CreateAPIView):
    serializer_class = AttributesTitlesSerializer
    permission_classes = (CustomIsAdminUser,)


class AttributesTitlesUpdateApiView(RetrieveUpdateAPIView):
    queryset = AttributesTitles.objects.all()
    serializer_class = AttributesTitlesSerializer
    permission_classes = (CustomIsAdminUser,)



#___________________Attributes__________________


class AttributesFilterApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        try:
            attributes_id = request.data['attributes']
            attributes = Attributes.objects.filter(id__in=attributes_id)
            serializer = AttributesSerializers(attributes, many=True)
            return Response(serializer.data)
        except KeyError:
            return Response({'detail': 'Введите данные корректно! JSON должен один или более количеств id с ключом attributes'})        
        
    
    def post(self, request):
        
        attributes_id = request.data['attributes']
        attributes = Attributes.objects.filter(id__in=attributes_id)
        serializer = AttributesSerializers(attributes, many=True)
        return Response(serializer.data)


class AttributesApiView(ListAPIView):

    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializers
    permission_classes = (CustomIsAdminUser,)


class AttributesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Attributes.objects.get(id=pk)
            serializer = AttributesSerializers(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данной имя атрибута по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class AttributesDeleteApiView(RetrieveDestroyAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializers
    permission_classes = (CustomIsAdminUser,)



class AttributesCreateApiView(CreateAPIView):
    serializer_class = AttributesSerializers
    permission_classes = (CustomIsAdminUser,)


class AttributesUpdateApiView(RetrieveUpdateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializers
    permission_classes = (CustomIsAdminUser,)


#___________________Pages__________________



class PagesApiView(ListAPIView):

    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (CustomIsAdminUser,)


class PagesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Pages.objects.get(id=pk)
            serializer = PagesSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данной страница по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class PagesDeleteApiView(RetrieveDestroyAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (CustomIsAdminUser,)



class PagesCreateApiView(CreateAPIView):
    serializer_class = PagesSerializer
    permission_classes = (CustomIsAdminUser,)


class PagesUpdateApiView(RetrieveUpdateAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (CustomIsAdminUser,)



#___________________Posts__________________



class PostsApiView(ListAPIView):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (CustomIsAdminUser,)


class PostsDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Posts.objects.get(id=pk)
            serializer = PostsSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данного поста по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class PostsDeleteApiView(RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (CustomIsAdminUser,)



class PostsCreateApiView(CreateAPIView):
    serializer_class = PostsSerializer
    permission_classes = (CustomIsAdminUser,)


class PostsUpdateApiView(RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (CustomIsAdminUser,)



#___________________Discounts__________________



class DiscountsApiView(ListAPIView):

    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
    permission_classes = (CustomIsAdminUser,)


class DiscountsDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Discounts.objects.get(id=pk)
            serializer = DiscountsSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данной свойство скидки по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class DiscountsDeleteApiView(RetrieveDestroyAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
    permission_classes = (CustomIsAdminUser,)



class DiscountsCreateApiView(CreateAPIView):
    serializer_class = DiscountsSerializer
    permission_classes = (CustomIsAdminUser,)


class DiscountsUpdateApiView(RetrieveUpdateAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________Taxes__________________


class TaxesApiView(ListAPIView):

    queryset = Taxes.objects.all()
    serializer_class = TaxesSerializer
    permission_classes = (CustomIsAdminUser,)


class TaxesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Taxes.objects.get(id=pk)
            serializer = TaxesSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данной налоговой системы по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class TaxesDeleteApiView(RetrieveDestroyAPIView):
    queryset = Taxes.objects.all()
    serializer_class = TaxesSerializer
    permission_classes = (CustomIsAdminUser,)



class TaxesCreateApiView(CreateAPIView):
    serializer_class = TaxesSerializer
    permission_classes = (CustomIsAdminUser,)


class TaxesUpdateApiView(RetrieveUpdateAPIView):
    queryset = Taxes.objects.all()
    serializer_class = TaxesSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________ProductsImages__________________


class ProductsImagesApiView(ListAPIView):

    queryset = ProductsImages.objects.all()
    serializer_class = ProductsImagesSerializer
    permission_classes = (CustomIsAdminUser,)


class ProductsImagesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = ProductsImages.objects.get(id=pk)
            serializer = ProductsImagesSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная картина по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class ProductsImagesDeleteApiView(RetrieveDestroyAPIView):
    queryset = ProductsImages.objects.all()
    serializer_class = TaxesSerializer
    permission_classes = (CustomIsAdminUser,)



class ProductsImagesCreateApiView(CreateAPIView):
    serializer_class = ProductsImagesSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________Countries__________________


class CountriesApiView(ListAPIView):

    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = (CustomIsAdminUser,)


class CountriesDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Countries.objects.get(id=pk)
            serializer = CountriesSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная страна по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class CountriesDeleteApiView(RetrieveDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = (CustomIsAdminUser,)



class CountriesCreateApiView(CreateAPIView):
    serializer_class = CountriesSerializer
    permission_classes = (CustomIsAdminUser,)


class CountriesUpdateApiView(RetrieveUpdateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = (CustomIsAdminUser,)




#___________________MakerOfProducts__________________


class MakerOfProductsApiView(ListAPIView):

    queryset = MakerOfProducts.objects.all()
    serializer_class = MakerOfProductsSerializer
    permission_classes = (CustomIsAdminUser,)


class MakerOfProductsDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = MakerOfProducts.objects.get(id=pk)
            serializer = MakerOfProductsSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная страна по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class MakerOfProductsDeleteApiView(RetrieveDestroyAPIView):
    queryset = MakerOfProducts.objects.all()
    serializer_class = MakerOfProductsSerializer
    permission_classes = (CustomIsAdminUser,)



class MakerOfProductsCreateApiView(CreateAPIView):
    serializer_class = MakerOfProductsSerializer
    permission_classes = (CustomIsAdminUser,)


class MakerOfProductsUpdateApiView(RetrieveUpdateAPIView):
    queryset = MakerOfProducts.objects.all()
    serializer_class = MakerOfProductsSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________DeliveriesType__________________


class DeliveriesTypeApiView(ListAPIView):

    queryset = DeliveriesType.objects.all()
    serializer_class = DeliveriesTypeSerializer
    permission_classes = (CustomIsAdminUser,)


class DeliveriesTypeDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = DeliveriesType.objects.get(id=pk)
            serializer = DeliveriesTypeSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная страна по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class DeliveriesTypeDeleteApiView(RetrieveDestroyAPIView):
    queryset = DeliveriesType.objects.all()
    serializer_class = DeliveriesTypeSerializer
    permission_classes = (CustomIsAdminUser,)



class DeliveriesTypeCreateApiView(CreateAPIView):
    serializer_class = DeliveriesTypeSerializer
    permission_classes = (CustomIsAdminUser,)


class DeliveriesTypeUpdateApiView(RetrieveUpdateAPIView):
    queryset = DeliveriesType.objects.all()
    serializer_class = DeliveriesTypeSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________DeliveriesStatus__________________


class DeliveriesStatusApiView(ListAPIView):

    queryset = DeliveriesStatus.objects.all()
    serializer_class = DeliveriesStatusSerializer
    permission_classes = (CustomIsAdminUser,)


class DeliveriesStatusDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = DeliveriesStatus.objects.get(id=pk)
            serializer = DeliveriesStatusSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная страна по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class DeliveriesStatusDeleteApiView(RetrieveDestroyAPIView):
    queryset = DeliveriesStatus.objects.all()
    serializer_class = DeliveriesStatusSerializer
    permission_classes = (CustomIsAdminUser,)



class DeliveriesStatusCreateApiView(CreateAPIView):
    serializer_class = DeliveriesStatusSerializer
    permission_classes = (CustomIsAdminUser,)


class DeliveriesStatusUpdateApiView(RetrieveUpdateAPIView):
    queryset = DeliveriesStatus.objects.all()
    serializer_class = DeliveriesStatusSerializer
    permission_classes = (CustomIsAdminUser,)


#___________________Orders__________________


class OrdersApiView(ListAPIView):

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (CustomIsAdminUser,)


class OrdersDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = Orders.objects.get(id=pk)
            serializer = OrdersSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная страна по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class OrdersDeleteApiView(RetrieveDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (CustomIsAdminUser,)



class OrdersCreateApiView(CreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = (CustomIsAdminUser,)


class OrdersUpdateApiView(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (CustomIsAdminUser,)



#___________________OrdersDetails__________________


class OrdersDetailsApiView(ListAPIView):

    queryset = OrdersDetails.objects.all()
    serializer_class = OrdersDetailsSerializer
    permission_classes = (CustomIsAdminUser,)


class OrdersDetailsDetailApiView(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            queryset = OrdersDetails.objects.get(id=pk)
            serializer = OrdersDetailsSerializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': f'Данная страна по id {pk} не существует'}, status=Status.HTTP_404_NOT_FOUND)


class OrdersDetailsDeleteApiView(RetrieveDestroyAPIView):
    queryset = OrdersDetails.objects.all()
    serializer_class = OrdersDetailsSerializer
    permission_classes = (CustomIsAdminUser,)



class OrdersDetailsCreateApiView(CreateAPIView):
    serializer_class = OrdersDetailsSerializer
    permission_classes = (CustomIsAdminUser,)


class OrdersDetailsUpdateApiView(RetrieveUpdateAPIView):
    queryset = OrdersDetails.objects.all()
    serializer_class = OrdersDetailsSerializer
    permission_classes = (CustomIsAdminUser,)


class OrdersDetailsUpdateApiView(RetrieveUpdateAPIView):
    queryset = OrdersDetails.objects.all()
    serializer_class = OrdersDetailsSerializer
    permission_classes = (CustomIsAdminUser,)

