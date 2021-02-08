from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item, Customer
import pyautogui as pag
from django.views import View

# Create your views here.



def checkout(request):
	price = request.POST.get('product')
	print(price)
	return render(request, 'checkout.html', {'price' : price})



def signout(request):
	request.session.clear()
	return redirect('signin')

class Index(View):
	def get(self, request):
		prds = Item.get_all_items();

		#print(request.session.get('cust_email'))
		return render(request, 'index.html', {'prds' : prds})

	def post(self, request):
		prod = request.POST.get('product')
		cart = request.session.get('cart')
		if cart:
			count = cart.get(prod)
			if count:
				cart[prod] = count+1
			else:
				cart[prod] = 1
		else:
			cart = {}
			cart[prod] = 1

		request.session['cart'] = cart
		#print(cart)
		return redirect('home')

class Signup(View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):
		formdata = request.POST
		name = formdata.get('name')
		phone = formdata.get('phone')
		email = formdata.get('email')
		password = formdata.get('password')
		#print(name,phone,email,password)
		cust = Customer(name = name ,phone = phone, email = email, password = password)
		cust.lodge()
		pag.alert(text="Account Created, Kindly keep your credential safe", title="Alert")		
		return redirect('home')


class Signin(View):
	def get(self, request):
		return render(request, 'signin.html')

	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		cust = Customer.get_cust_by_email(email)
		if cust and password == cust.password:
			request.session['cust_id'] = cust.id
			request.session['cust_email'] = cust.email
			return redirect('home')
		else:
			pag.alert(text="Email/Password is not correct", title="Alert")

		return render(request, 'signin.html')


	

class Cart(View):
	def get(self , request):
		ids = list(request.session.get('cart').keys())
		prods = Item.get_all_by_id(ids)
		#print(prods)
		return render(request , 'cart.html' , {'prods' : prods})

