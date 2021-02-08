from django.db import models

class Item(models.Model):
	name = models.CharField(max_length = 50)
	price = models.IntegerField(default = 0)
	desc = models.CharField(max_length = 200, default = '')
	image = models.ImageField(upload_to = 'static/images')


	@staticmethod
	def get_all_items():
		return Item.objects.all()

	def get_all_by_id(id):
		return Item.objects.filter(id__in = id )


class Customer(models.Model):
	name = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 15)
	email = models.EmailField()
	password = models.CharField(max_length = 500)

	def lodge(self):
		self.save()

	@staticmethod
	def get_cust_by_email(email):
		try:
			return Customer.objects.get(email = email)
		except:
			return False