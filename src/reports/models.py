from django.db import models
from django.urls import reverse
import random
# Create your models here.

def product_size_price_calculator(price, quantity):
    total_price = float(price)*float(quantity)
    return total_price


def id_generator(id, name):
    random_id = '{}-{}'.format(name[0:4], id)+str(random.randint(0000, 9999))
    return random_id

def random_generator():
    random_id = f'{random.randint(0000, 9999)}'
    return random_id


class Customer(models.Model):
    """Model definition for Customer."""
    customer_id = models.CharField(null=True, blank=True, max_length=50)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        """Meta definition for Customer."""
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Unicode representation of Customer."""
        return self.name

    @property
    def customer_id_gen(self):
        if self.name:
            self.customer_id=random_generator()
            return self.customer_id

    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})



class Tag(models.Model):
    """Model definition for Tag."""
    name = models.CharField(max_length=200, null=True)

    class Meta:
        """Meta definition for Tag."""
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name




class Product(models.Model):
    """Model definition for Product."""
    CATEGORY = (
        ('Non-Alcoholic', 'Non-Alcholic'),
        ('Alcoholic', 'Alcholic'),
    )
    # product_id = models.C(primary_key=True, editable=False)
    product_id = models.CharField(null=True, blank=True, max_length=50)
    name = models.CharField(max_length=200, null=True)
    production_plant = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    carton_size = models.IntegerField(blank=True, null=True)
    pallet_size = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    expire_date = models.DateTimeField(auto_now_add=False, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    @property
    def carton_prize(self):
        if self.carton_size:
            return product_size_price_calculator(self.price, self.carton_size)
        return "0"
    
    @property
    def pallet_prize(self):
        if self.pallet_size:
            return product_size_price_calculator(self.price, self.pallet_size)
        return "0"






class Order(models.Model):
    """Model definition for Order."""
    STATUS = (
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # order_id = models.AutoField(primary_key=True, editable=False)
    order_id = models.CharField(null=True, blank=True, max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    remark = models.CharField(max_length=500, null=True)
    

    class Meta:
        """Meta definition for Order."""
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    @property
    def order_id_gen(self):
        if self.quantity:
            self.order_id=random_generator()
            return self.order_id

    def __str__(self):
        """Unicode representation of Order."""
        return "{}-{}".format(self.order_id, self.customer.name)

    def get_absolute_url(self):
        # return reverse('reports:home', kwargs={'pk': self.pk})
        return reverse('home', kwargs={'pk': self.pk})

    @property
    def status_choice(self):
        if self.status == "Pending":
            return 'warning'
        elif self.status == "Canceled":
            return 'danger'
        elif self.status == "Out for delivery":
            return 'info'
        elif self.status == "Delivered":
            return 'success'
            


# # class ProductionPlant(models.Model):
#     """Model definition for ProductionPlant."""
#     plant_id = models.AutoField(primary_key=True, editable=False, max_length=10)
#     plant_location = models.CharField()

#     class Meta:
#         """Meta definition for ProductionPlant."""

#         verbose_name = 'ProductionPlant'
#         verbose_name_plural = 'ProductionPlants'

#     def __str__(self):
#         """Unicode representation of ProductionPlant."""
#         pass
