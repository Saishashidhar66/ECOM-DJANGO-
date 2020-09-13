from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Category,Contact
from django.http import request
from django.core.mail import send_mail
from.forms import ProductForm
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'index.html', context)

def google(request):
    return HttpResponse("hello")
def product(request,id):
    product = Product.objects.get(id = id)
    context = {'product':product}
    return render(request, 'product.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email, message = message)
        contact.save()
        send_mail(
            f"Message from {name}",
            "message",
            "saishashidhar66@gmail.com",
            ['saishashidhar66@gmail.com'],
            fail_silently=False )
        send_mail(
            f"Hlooo {name}",
            f"Thank You For Reaching Us about {message}\n Please Wait until Our Executive contact You \n Thank You for your Patiance   -Team ECOM",
            "saishashidhar66@gmail.com",
            [email],
            fail_silently=False )
    return render(request, 'contact.html')
def allcat(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request, 'allcat.html', context)
def catprod(request,id):
    category = Category.objects.get(id = id)
    cat_prod = category.product_set.all()
    context = {'cat_prod':cat_prod, 'category':category}
    return render(request, 'catprod.html', context)
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'createprod.html',context)
def updateProduct(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'updateprod.html',context)
def deleteProduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')
    