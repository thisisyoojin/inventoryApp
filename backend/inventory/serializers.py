from rest_framework import serializers
from inventory.models import Item, Restaurant, Seller, ItemHistory, Todo

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

    restaurant_name = serializers.CharField(max_length=30)
    


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    item_name = serializers.CharField(max_length=30)
    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    seller_id = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    current_count = serializers.IntegerField()



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

    seller_name = serializers.CharField()


class ItemHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemHistory
        fields = "__all__"

    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    count = serializers.IntegerField()

    def get_queryset(self):
        """
        This view should return a list of all the history for the item
        """
        item_id = self.kwargs['item_id']
        updated_on = self.kwargs['updated_on']
        return ItemHistory.objects.filter(item_id=item_id, updated_on=updated_on)
    

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()


    