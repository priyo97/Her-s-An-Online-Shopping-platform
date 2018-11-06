from django.db import models


class Category1(models.Model):

	c_name = models.CharField(max_length=50)

	def __str__(self):

		return f"{self.c_name}"

class Category2(models.Model):

	c_name = models.CharField(max_length=50)

	def __str__(self):

		return f"{self.c_name}"


class Product(models.Model):

	p_name = models.CharField(max_length=100)
	p_brand = models.CharField(max_length=100)

	price = models.DecimalField(max_digits=7, decimal_places=2)
	d_price = models.DecimalField(max_digits=7, decimal_places=2)

	category1 = models.ForeignKey(Category1,on_delete=models.CASCADE)
	category2 = models.ForeignKey(Category2,on_delete=models.CASCADE)

	url = models.URLField()

	def __str__(self):
		return f"{self.p_name}|{self.category1}|{self.category2}"


class Customer(models.Model):

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	
	email = models.EmailField(max_length=30)
	address = models.TextField()
	
	phone_number = models.CharField(max_length=10)
	date_added = models.DateField(auto_now_add=True)

	purchases = models.ManyToManyField(Product,through="CustomerProduct")
	
	def __str__(self):

		return f"{self.first_name} {self.last_name}"



class CustomerProduct(models.Model):

	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	no_of_items = models.IntegerField()
	total_amount = models.DecimalField(max_digits=7, decimal_places=2)
	purchase_date = models.DateField(auto_now_add=True)
