from django.urls import path
from ecommerceapp import views
from .views import ProductDetailView

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('profile',views.profile,name="profile"),
    path('checkout/', views.checkout, name="Checkout"),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),

]
