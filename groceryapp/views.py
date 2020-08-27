from django.shortcuts import render
from django.http import HttpResponse
from groceryapp.models import User,Category,Item,Order,Orderdone

def login(request):
	count = request.session.get('page_count',0)
	request.session['page_count'] = count+1
	return render(request,'login.html')

def registeraction(request):
	username = request.GET.get('Username')
	password = request.GET.get('Password')
	email = request.GET.get('Email')
	address = request.GET.get('Address')
	phoneno = request.GET.get('Phone')
	pincode = request.GET.get('Pincode')

	u = User(username=username,password=password,email=email,address=address,mobileno=phoneno,pincode=pincode)
	u.save()
	print(u)
	return render(request,'login.html')

def loginaction(request):
	username = request.GET.get('Username')
	password = request.GET.get('Password')

	l = User.objects.all()
	print(l)

	for i in l:
		if username == i.username and password == i.password:
			k = i.id
			print(k)
			contex = {
				'Userid':k
			}
			request.session['k'] = k
			return render(request,'index.html',contex)
	else:
		return render(request,'login.html')


	# for i in l:
	# 	if username == i.username and password == i.password:
	# 		request.session['username'] = username
	# 		return render(request,'index.html')
	# 	return render(request,'login.html')

	# username = request.GET.get('Username')
	# password = request.GET.get('Password')
	# print(username)
	# print(password)

	# users = User.objects.all()

	# users = auth.authenticate(username = username, password = password)

	# if users is not None:
 #        	auth.login(request,users)
 #        	return render(request,'index.html')
 #    else:
 #        	return render(request,'login.html')

	# for i in users:
	# 	if username==i.username and password==i.password:
	# 		request.session['username'] = username
	# 		return render(request,'index.html')
	# 	return render(request,'login.html')

	# l = User.objects.all()
	# print(l)
	# for i in l:
	# 	if username == i.username and password == i.password:
	# 		request.session['username'] = username
	# 		print(username)
	# 		return render(request,'index.html')
	# 	return render(request,'login.html')

def index(request):
	return render(request,'index.html')

def item(request):
	id = request.GET.get('id')

	i = Category.objects.all()
	contex = {
		'Data':i,'Userid':id
	}
	return render(request,'item.html',contex)

def cart(request):
	id = request.GET.get('id')
	# uid = request.GET.get('uid')

	x = Category.objects.get(id=id)
	k = Item.objects.filter(category=x)

	contex = {
		'Data': k
	}
	print(k)
	return render(request,'cart.html',contex)

def checkout(request):
	id = request.GET.get('did')
	print(id)
	r =2
	# s = Order.objects.all(id=id)
	# x = Category.objects.get(id=id)
	# n = request.GET.get('name')
	# p = request.GET.get('price')

	obj = Order.objects.all()

	name = request.GET.get('item_name_1')
	name1 = request.GET.get('item_name_2')
	name2 = request.GET.get('item_name_3')
	price = request.GET.get('amount_1')
	price1 = request.GET.get('amount_2')
	price2 = request.GET.get('amount_3')

	print(name)
	print(price)
	print(name1)
	print(price1)
	print(name2)
	print(price2)

	o = Order(name=name,price=price,user=r)
	o.save()
	print(o)

	o1 = Order(name=name1,price=price1,user=r)
	o1.save()
	print(o1)

	o2 = Order(name=name2,price=price2,user=r)
	o2.save()
	print(o2)

	
	contex = {
		'Data': obj
	}
	return render(request,'checkout.html',contex)

def checkout1(request):
	id = request.GET.get('id')
	print(id)
	# sname = request.GET.get('sessionname')

	obj = Order.objects.filter(user=id)
	# total = Order.objects.all().aggregate(sum('price'))
	# print(total)
	contex = {
		'Data': obj
	}
	return render(request,'checkout.html',contex)

def delateaction(request):
	id = request.GET.get('id')
	item = Order.objects.get(id=id)
	item.delete()

	obj = Order.objects.all()
	# total = Order.objects.all().aggregate(sum('price'))
	# print(total)
	contex = {
		'Data': obj
	}
	return render(request,'checkout.html',contex)


def indexaction(request):
	# iname = request.GET.get('item_name')
	# iprice = request.GET.get('item_price')
	# name = request.GET.get('name')
	# mobile = request.GET.get('mobile')
	# houseno = request.GET.get('houseno')
	# street = request.GET.get('street')

	# print(iname)
	# print(iprice)
	# print(name)
	# print(mobile)
	# print(houseno)
	# print(street)

	# o = Orderdone(item_name=iname,item_price=iprice,name=name,mobile=mobile,houseNo=houseno,street=street)
	# o.save()

	# print(o)

	# contex={
	# 	'Data' : o
	# }

	username = request.session.get('username')
	if not username:
		return render(request,'login.html')
	request.session['username'] = username
	return render(request,'index.html')


	# bool user

	# user = request.session['username']
	# if user is True:
	# 	return render(request,'index.html')
	# if user is False:
	# 	return render(request,'login.html')


def logout(request):
	del request.session['k']
	return render(request,'login.html')

def about(request):
	return render(request,'about.html')


def services(request):
	return render(request,'services.html')



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Back-end code
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def indexcategory(request):
	return render(request,'indexcategory.html')

def addcate(request):
	name=request.GET.get('name')
	des=request.GET.get('des')

	c = Category(name=name,des=des)
	c.save()
	print(c) 
	return render(request,'indexcategory.html')

def displaycategory(request):
	id = request.GET.get('id')
	x = Category.objects.get(id=id)
	print(x)
	return render(request,'displaycategory.html',{'Data':x})


def addproduct(request):

	# id = request.GET.get('id')
	# x = Category.objects.get(id=id)
	# print(x)

	id = request.GET.get('did')
	print(id)
	c = Category.objects.get(id=id)

	name = request.GET.get('name')
	price = request.GET.get('price')
	weightunit = request.GET.get('weightunit')
	weight = request.GET.get('weight')
	desription = request.GET.get('desription')

	p = Item(id=None,name=name,price=price,description=desription,weightunit=weightunit,weight=weight,category=c)
	p.save()
	print(p)

	obj = Category.objects.all()
	contex = {
		'Data':obj
	}
	return render(request,'displaycategory.html',contex)

# Create your views here.
