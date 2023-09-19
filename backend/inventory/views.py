from rest_framework import viewsets
from rest_framework import permissions
from .models import Item, Restaurant, Seller, ItemHistory, Todo
from .serializers import ItemSerializer, RestaurantSerializer, SellerSerializer, ItemHistorySerializer, TodoSerializer
from .paginations import StandardResultsSetPagination
from django_api.constants import DEFAULT_FILTERS, DEFAULT_HTTP_METHODS

class CustomModelViewSet(viewsets.ModelViewSet):
    http_method_names = DEFAULT_HTTP_METHODS
    filter_backends = DEFAULT_FILTERS
    pagination_class = StandardResultsSetPagination


class RestaurantViewSet(CustomModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['restaurant_name']


class ItemViewSet(CustomModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['item_id', 'restaurant_id', 'seller_id']
    search_fields = ['item_name']
    

class SellerViewSet(CustomModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['seller_name']
    

class ItemHistoryViewSet(CustomModelViewSet):
    queryset = ItemHistory.objects.all()
    serializer_class = ItemHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['item_id', 'updated_on']


class TodoViewSet(CustomModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['status']
    search_fields = ['title', 'description']
    