from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.BigAutoField(primary_key=True, auto_created=True)
    restaurant_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.restaurant_name}"


class Seller(models.Model):
    seller_id = models.BigAutoField(primary_key=True, auto_created=True)
    seller_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.seller_name}"


class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True, auto_created=True)
    item_name = models.CharField(max_length=30)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    created_on = models.DateField(auto_now_add=True)
    current_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item_name}"
    

class ItemHistory(models.Model):
    
    class Meta:
        unique_together = (('updated_on', 'item_id'),)
    
    updated_on = models.DateField(auto_now=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"${self.updated_on}: {self.item_id} - {self.count}"
    

class Todo(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
