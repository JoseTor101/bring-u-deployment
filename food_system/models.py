from django.db import models
from accounts.models import UserProfile
from django.utils import timezone

class Business(models.Model):
    id_business = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads_restaurants/', default='page_media/food.png')
    opening_time = models.TimeField(default="07:00:00")
    closing_time = models.TimeField(default="18:00:00")

    def __str__(self):
        return self.name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    fk_id_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    price = models.IntegerField()


def upload_to(instance, filename):
    return f'{filename}'
    
class Request(models.Model):
    id_request = models.AutoField(primary_key=True)
    fk_id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fk_id_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    status = models.CharField(max_length=30, default="Sin tomar")
    delivery_location = models.CharField(max_length=250)
    desc_delivery = models.CharField(max_length=1000, null=True)
    pick_up_location = models.CharField(max_length=250, default="Pick-up location")
    desc_pick_up_location = models.CharField(max_length=1000, null=True)
    file= models.FileField(upload_to='orders_media/', null=True)
    business_name = models.CharField(max_length=70, null=True)

    def delete(self, *args, **kwargs):
        history_entry = HistoryRequest.objects.create(
            fk_id_user=self.fk_id_user,
            fk_id_product=self.fk_id_product,
            name=self.name,
            desc=self.desc,
            price=self.price,
            status="Cancelado",
            delivery_location=self.delivery_location,
            desc_delivery=self.desc_delivery,
            pick_up_location=self.pick_up_location,
            desc_pick_up_location=self.desc_pick_up_location
        )
        super().delete(*args, **kwargs)

class Delivery(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    fk_id_request = models.ForeignKey(Request, on_delete=models.CASCADE)
    fk_id_client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_deliveries', default=None)
    fk_id_delivery_man = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='delivery_man_deliveries')
    time = models.TimeField(auto_now=True)
    finished = models.BooleanField(default=False)

    def order_finished(self, *args, **kwargs):
        history_entry = HistoryDelivery.objects.create(
            fk_id_client=self.fk_id_client,
            fk_id_delivery_man=self.fk_id_delivery_man,
            name=self.fk_id_request.name,
            desc=self.fk_id_request.desc,
            price=self.fk_id_request.price,
            status="Finalizado"
        )

class HistoryRequest(models.Model):
    id_history_request = models.AutoField(primary_key=True)
    fk_id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fk_id_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    status = models.CharField(max_length=30, default="Sin tomar")
    delivery_location = models.CharField(max_length=250)
    desc_delivery = models.CharField(max_length=1000, null=True)
    pick_up_location = models.CharField(max_length=250, default="Pick-up location")
    desc_pick_up_location = models.CharField(max_length=1000, null=True)
    business_name = models.CharField(max_length=70, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

class HistoryDelivery(models.Model):
    id_history_delivery = models.AutoField(primary_key=True)
    fk_id_client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_deliveries_history', default=None)
    fk_id_delivery_man = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='delivery_man_deliveries_history')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    status = models.CharField(max_length=30)
    time = models.TimeField(auto_now=True)
