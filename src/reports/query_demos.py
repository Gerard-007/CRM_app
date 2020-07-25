from .models import Customer, Order, Product

customers = Customer.objects.all()

#Returns first customer in table
firstCustomer = Customer.objects.first()

#Returns last customer in table
lastCustomer = Customer.objects.last()

#Return single customer by name
customer_by_name = Customer.objects.get(name="Peter Piper")

#Return single customer by name
customer_id = Customer.objects.get(id=4)

#Return all orders related to customer(firstCustomer variable set above)
firstCustomer.order_set.all()

#Return orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#Return products from products table with value of "out door" in cate
products = Product.objects.filter(category="soft drinks")

#Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

#Return all products with tag of "sports": (Query many to many fields)
productsFiltered = Product.objects.filter(tags__name="promo")

#Return the total count for number of time a Maltina was ordered
maltOrder = firstCustomer.order_set.filter(product__name="maltina").count()

# Return total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
    #Returns: allOrders: {'Maltina':2, 'Star':1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Return all child models related to parent
parent.childmodel_set.all()