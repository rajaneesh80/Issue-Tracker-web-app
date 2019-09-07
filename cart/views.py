from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

##############################################################

@login_required
def view_cart(request):
    """A view cart """
    return render(request, 'cart/cart.html')

##############################################################

def add_to_cart(request, id):
    """"Add a product to the cart"""
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    messages.success(request, 'Feature added to cart!')
    request.session['cart'] = cart
    return redirect(reverse('issues'))

##############################################################

def adjust_cart(request, id):
	"""Add a quantity to cart"""
	quantity=int(request.POST.get('quantity'))
	cart = request.session.get('cart', {})
	cart[id] = cart.get(id, quantity)
	request.session['cart'] = cart
	return redirect(reverse('issues'))




##############################################################