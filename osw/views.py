from django.shortcuts import render,redirect
from .forms import Login,Register,Problem
from .models import Customer,Product

def index(request):

	if "username" in request.session:
		context = {'sign':"Sign Out","value":r"/logout"}
	else:
		context = {'sign':"Sign In","value":r"/login"}

	return render(request,'osw/index.html',context)


def logout(request):

	if request.session["username"] in  user_cart:
		del user_cart[request.session["username"]]

	del request.session["username"]

	return redirect("index")
	
def login(request):

	if request.method == "POST":

		try:
			user = Customer.objects.filter(username__exact=request.POST["username"]).get()
		except:
			return redirect('login')

		if user.password == request.POST["password"]:

			request.session["username"] = request.POST["username"]

			user_cart[request.session["username"]] = []

			return redirect('index')
		else:
			return redirect('login')
	else:

		f = Login()
		context = {"f":f}
		return render(request,"osw/login.html",context)



def register(request):

	if request.method == "POST":
		form = Register(request.POST)

		if form.is_valid():
			new_user = Customer(first_name=request.POST["first_name"]
							,last_name=request.POST["last_name"]
							,username=request.POST["username"]
							,password=request.POST["password"]
							,email=request.POST["email"]
							,phone_number=request.POST["phone_number"]
							,address=request.POST["address"])
			new_user.save()

			
			request.session["username"] = request.POST["username"]

			user_cart[request.session["username"]] = []

			return redirect('index')
	else:

		f = Register()
		context = {"f":f}
		return render(request,"osw/register.html",context)	


def main(request):

	if "username" in request.session:

		# print(request.session["username"])
	
		c = request.GET["c2"]
		items = Product.objects.filter(category2=int(c))
		
		context = {"items":items}

		return render(request,"osw/main.html",context)

	else:

		return redirect('login')


user_cart = {}

def cart(request):

	if request.POST:
		# print(request.session["username"])
		# print(request.POST.getlist('items'))

		user = request.session["username"]


		for item in request.POST.getlist('items'):
			p = Product.objects.get( id=int(item) )
			print(item,p)

			user_cart[user].append(p)

		print("user:"+user+" ",user_cart[user])

	return redirect("index")


def payment(request):

	if "username" in request.session:

		products = user_cart[request.session["username"]]

		total_amount = 0

		for p in products:

			total_amount += p.d_price

		context = {"items":products,"no_products":len(products),"total_amount":total_amount}

		return render(request,"osw/payment.html",context)
	else:
		return redirect("login")





def problem(request):

	f = Problem()
	context = {"f":f}

	return render(request,"osw/problem.html",context)
