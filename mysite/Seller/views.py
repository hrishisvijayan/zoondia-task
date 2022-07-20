from django.shortcuts import redirect, render
from .models import Cart, Seller, Product
from . forms import ProductForm

# Create your views here.


def home(request):
    product = Product.objects.all()
    return render(request,'home.html',{'product': product})


def signup(request):
    if request.method == 'POST':
        print('request is here')
        name = request.POST.get('name') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password  == confirm:
            Seller.objects.create(name=name,email=email,password=password)
            return render(request,'home.html')
        else:
            error = 'input credential are not valid'
            return render(request,'seller-signup.html',{ 'error' : error })
        
    return render(request,'seller-signup.html')

def create_product(request):
    form = ProductForm(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        print(request.POST,request.FILES)
        print('i am here')
        if form.is_valid():
            form.save()
            print('this is form',form)
        else:
            print('an error is here')
    return render(request,'addproduct.html',{'form':form})
 

def view_products(request):
    product = Product.objects.all()
    return render(request,'viewproducts.html',{'product': product})

def edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        name= request.POST.get('name')
        price= request.POST.get('price')
        quantity= request.POST.get('quantity')
        status= request.POST.get('status')
        Product.objects.filter(id=id).update(name=name,price=price,quantity=quantity,status=status)
        return redirect('viewproducts')
    return render(request,'editproduct.html',{'product':product})

def addcart(request,id):
    product = Product.objects.get(id=id)
    if not request.session.session_key:
        request.session.create()
    session = request.session.session_key
    if Cart.objects.filter(product=product,session_id=session).exists():
        cart=Cart.objects.get(product=product,session_id=session)
        cart.quantity+=1
        cart.save()
    else:
        Cart.objects.create(product=product,session_id=session)
    return redirect('home')

def cartpage(request):
    cart = Cart.objects.filter(session_id=request.session.session_key)
    return render(request,'cart.html',{ 'cart' : cart })