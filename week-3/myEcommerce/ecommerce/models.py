from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Cart(models.Model):
    # ลบ Cart ให้หมดก่อนค่อยลบ Customer
    customer = models.ForeignKey("ecommerce.Customer", on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)
    expired_in = models.IntegerField(default=60)

class CartItem(models.Model):
    # ลบ Cart ออกได้เลยถ้าไม่เอาแล้ว
    cart = models.ForeignKey("ecommerce.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("ecommerce.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "Name of Product: " + self.name + "\nprice: " + self.price
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    product = models.ManyToManyField("ecommerce.Product")

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey("ecommerce.Customer", on_delete=models.PROTECT)
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    remark = models.TextField(null=True)

class OrderItem(models.Model):
    order = models.ForeignKey("ecommerce.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("ecommerce.Product", on_delete=models.PROTECT)
    amount = models.IntegerField(default=1)

class Payment(models.Model):
    order = models.ForeignKey("ecommerce.Order", on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now=False, auto_now_add=True)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PaymentItem(models.Model):
    payment = models.ForeignKey("ecommerce.Payment", on_delete=models.CASCADE)
    order_item = models.OneToOneField("ecommerce.OrderItem", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class PaymentMethod(models.Model):
    QR_METHOD = "QR"
    CREDIT_METHOD = "CREDIT"
    PAYMENT_METHOD = {
        QR_METHOD: "Qr",
        CREDIT_METHOD: "Credit",
    }
    payment = models.ForeignKey("ecommerce.Payment", on_delete=models.PROTECT)
    method = models.CharField(choices=PAYMENT_METHOD)
    price = models.DecimalField(max_digits=10, decimal_places=2)