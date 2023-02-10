from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_list, name='product_list'),
    path('product/<slug:category_slug>/', views.product_list_category, name='product_list_by_category'),
    path('product/<slug:category_slug>/<slug:subcategory_slug>/', views.product_list_subcategory, name='product_list_by_subcategory'),
    path('product/detail/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]