
from django.db import models
from PIL import Image

from users.models import Profile 
# Create your models here.


class ProductCard(models.Model):
    product_image = models.ImageField(null=True, blank=True, upload_to="product_images/", default="default-product.png")
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    is_shoe = models.BooleanField(default=True)
    is_cloth = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(ProductCard,self).save(*args, **kwargs)

        img = Image.open(self.product_image.path)

        if img.height > 300 or img.width > 350:
            output_size = (315,350)
            img = img.resize(output_size)
            img.save(self.product_image.path)

    class Meta:
        ordering = ['created']


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    compleated = models.BooleanField(default=False)

    def __str__(self):
        return f'Order# {str(self.id)}'
    
    @property
    def get_price_total(self):
        orderitems = self.order_items.all()
        total_orderitem = sum([item.get_total for item in orderitems])
        return total_orderitem

    @property
    def get_qty_total(self):
        orderitems = self.order_items.all()
        total_qty = sum([item.quantity for item in orderitems])
        return total_qty
    

class OrderItem(models.Model):
    product = models.ForeignKey(ProductCard, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name="order_items", blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    shoe_size = models.ManyToManyField('ShoeSize', blank=True, null=True)
    cloth_size = models.ManyToManyField('ClothSize', blank=True, null=True)
    
    def __str__(self):
        return f'{self.product} - {self.order}'


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class ShoeSize(models.Model):
    shoe_size = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.shoe_size)


class ClothSize(models.Model):
    cloth_size = models.CharField(max_length = 50, null=True, blank=True)

    def __str__(self):
        return str(self.cloth_size)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)

    def __str__(self):
        return f"{str(self.customer)}'s Shipping Address" 