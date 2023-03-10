from django.shortcuts import render, redirect
from .models import *
from .forms import ProductCardForm, UpdateQty, UpdateShoeSize, UpdateClothSize, AddShippingAddress, CompleteOrder
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#import flash messages
from django.contrib import messages


# Create your views here.

def header(request):
    return render(request, 'products/header.html')

def products(request):
    products = ProductCard.objects.all()

    return render(request, 'products/products.html', {'products':products,})

    # #setting the Paginator
    # page = request.GET.get('page')
    # results = 3
    # paginator = Paginator(products, results)

    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     products = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     products = paginator.page(page)

    # leftIndex = (int(page)-4)

    # if leftIndex<1:
    #     leftIndex = 1
    # rightIndex = (int(page)+5)

    # if rightIndex > paginator.num_pages:
    #     rightINdex = paginator.num_pages +1
    
    # custom_range = range(leftIndex,rightIndex)

    # return render(request, 'products/products.html', {'products':products, 'paginator':paginator, 'custom_range':custom_range})


def product_card(request, pk):
    productObj = ProductCard.objects.get(id=pk)
    
    return render(request, 'products/product_card.html', {'productObj':productObj})


# @login_required(login_url='login')
# def create_card(request):
#     form = ProductCardForm()

#     if request.method == 'POST':
#         form = ProductCardForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()   
#             return redirect('products')
    
#     return render(request,'products/product_form.html', {'form':form})


# @login_required(login_url='login')
# def update_card(request, pk):

#     productObj = ProductCard.objects.get(id=pk)
#     form = ProductCardForm(instance=productObj)

#     if request.method == 'POST':
#         form = ProductCardForm(request.POST,request.FILES, instance=productObj)
#         if form.is_valid:
#             form.save()
#             return redirect('product-card', pk=productObj.id) 

#     return render(request, 'products/update_form.html', {'form':form,'productObj':productObj})


# @login_required(login_url='login')
# def delete_card(request, pk):
#     productObj = ProductCard.objects.get(id=pk)
#     page = 'delete_card'
#     if request.method == 'POST':
#         productObj.delete()
#         return redirect('products')
#     return render(request, 'products/delete_form.html', {'productObj':productObj, 'page':page})


#checking if size existing before clicking 'Checkout'
"""
def check_size(request, pk):
    customer = request.user.profile

    order = Order.objects.filter(customer=customer, compleated=False).first()
    orderItems = order.order_items.all()

    return OrderItem.objects.filter().exist()
"""

@login_required(login_url='login')
def order(request):
    customer = request.user.profile

    order , created = Order.objects.get_or_create(customer=customer, compleated=False)
    orderItems = order.order_items.all()
    
    return render(request, 'products/order.html', {'orderItems':orderItems, 'order':order,})


@login_required(login_url='login')
def add_orderItem(request, pk):
    productObj = ProductCard.objects.get(id=pk)
    customer = request.user.profile
    
    if request.method == 'POST':
        #print(request.POST)
        order , created = Order.objects.get_or_create(customer=customer, compleated=False)
        # OrderItem.objects.create(product = productObj, order=order)
        # return redirect('products')
        orderItems = order.order_items.all()
        
        if order.compleated != True:  
            #if we add same product twice 
            addedProduct = OrderItem.objects.filter(product=productObj, order=order).first()
             
            OrderItem.objects.create(product=productObj, order=order)     
            return redirect('products')
        
    return render(request, 'products/products.html', {})


@login_required(login_url='login')
def update_orderItem(request,pk):
    orderItem = OrderItem.objects.get(id=pk)

    form_q = UpdateQty(instance=orderItem)
    form_s = UpdateShoeSize(instance=orderItem)
    form_c = UpdateClothSize(instance=orderItem)

    if request.method == 'POST':
        form_q = UpdateQty(request.POST, instance=orderItem)
        form_s = UpdateShoeSize(request.POST, instance=orderItem)
        form_c = UpdateClothSize(request.POST, instance=orderItem)

        if form_q.is_valid() and form_s.is_valid() and form_c.is_valid():
            form_q.save()
            form_s.save()
            form_c.save()
            return redirect('order')
   
    return render(request, 'products/update_orderItem.html',{'orderItem':orderItem, 'form_q':form_q, 'form_s':form_s, 'form_c':form_c})

@login_required(login_url='login')
def delete_orderItem(request, pk):
    

    orderItem = OrderItem.objects.get(id=pk)
    page = 'delete_order'
    if request.method == 'POST':
        orderItem.delete()
        return redirect('order')
    return render(request, 'products/delete_form.html', {'orderItem':orderItem, 'page':page})

@login_required(login_url='login')
def chekout(request, pk):
    customer = request.user.profile
    shippingAddress = ShippingAddress.objects.filter(customer=customer).first()
    order = Order.objects.get(id=pk)
    form = CompleteOrder(instance=order)

    if request.method == 'POST':
        form = CompleteOrder(request.POST, instance=order)
        if form.is_valid():
            order_compleate = form.save(commit=False)
            order_compleate.compleated = True
            form.save()
        return redirect('products')

    return render(request,'products/checkout.html', {'shippingAddress':shippingAddress, 'order':order, 'customer':customer})


@login_required(login_url='login')
def add_ShippingAddress(request):
    customer = request.user.profile
    order = Order.objects.filter(customer=customer, compleated=False).first()
    form = AddShippingAddress()
    
    if request.method == 'POST':
        form = AddShippingAddress(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.customer = customer
            address.save()
            return redirect('checkout', pk=order.id)
    
    return render (request, 'products/add_shippingaddress.html', {'form':form})

@login_required(login_url='login')
def update_ShippingAddress(request, pk):
    shippingAddress = ShippingAddress.objects.get(id=pk)
    customer = request.user.profile
    order = Order.objects.filter(customer=customer, compleated=False).first()
    form = AddShippingAddress(instance=shippingAddress)

    if request.method == 'POST':
        form = AddShippingAddress(request.POST, instance=shippingAddress)
        if form.is_valid():
            form.save()
            return redirect('checkout' , pk=order.id)
    
    return render(request, 'products/update-shippingaddress.html', {'form':form})