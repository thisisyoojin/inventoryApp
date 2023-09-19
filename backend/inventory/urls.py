from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet,basename="item")
router.register(r'itemhistory', views.ItemHistoryViewSet,basename="itemhistory")
router.register(r'seller', views.SellerViewSet,basename="seller")
router.register(r'restaurants', views.RestaurantViewSet,basename="restaurant")
router.register(r'todos', views.TodoViewSet,basename="todo")


urlpatterns = [
    path('', include(router.urls))
]