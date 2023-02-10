from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from django.views import View

from .models import Category, Product, Subcategory


# Create your views here.


def index(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(available=True)

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
    }
    return render(request, 'shop/home/home.html', context)


def product_list(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/product/list.html',
                  {'categories': categories,
                   'subcategories': subcategories,
                   'products': products})


# View for product list in site
def product_list_category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    subcategory = None
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(available=True)
    # print(products.filter(category=1))
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'subcategory': subcategory,
                   'subcategories': subcategories,
                   'products': products})


def product_list_subcategory(request, category_slug=None, subcategory_slug=None):
    category = None
    categories = Category.objects.all()
    subcategory = None
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(available=True)
    # print(products.filter(category=1))
    if category_slug and subcategory_slug:
        # print(category_slug)
        # print(category.id)
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        print(subcategory)
        products = products.filter(subcategory=subcategory)
        print(products)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'subcategory': subcategory,
                   'subcategories': subcategories,
                   'products': products})


# View for single product
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    # Add to cart button
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
