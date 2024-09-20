from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from .serializers import UsersSerializer, ContactsSerializer, TasksSerializer
from join_app.models import Users, Contacts, Tasks


class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CreateListUpdateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    pass


class ContactsView(CreateListUpdateDestroyViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class TasksView(CreateListUpdateDestroyViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer




# class MarketSingelView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer



# class SellersView(generics.ListCreateAPIView):
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer

 
        

        

# class SellerOfMarketList(generics.ListCreateAPIView):
#     serializer_class = SellerListSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         market = Market.objects.get(pk=pk)
#         return market.sellers.all()
    
#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         market = Market.objects.get(pk=pk)
#         serializer.save(markets=[market])


# class ProductViewSetOld(viewsets.ViewSet):
#     queryset = Product.objects.all()

#     def list(self, request):
#         serializer = ProductSerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         product = get_object_or_404(self.queryset, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def destroy(self, request, pk=None):
#         product = get_object_or_404(self.queryset, pk=pk)
#         product.delete()
#         return Response({"success": True})
    
# class ProductViewSetOlder(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ListRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     pass


# class ProductViewSet(ListRetrieveViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

