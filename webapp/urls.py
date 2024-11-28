from django.urls import path
from webapp import views
urlpatterns=[
    path('homePage/',views.homePage,name="homePage"),
    path('product_page/',views.product_page,name="product_page"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('single_products/<int:pro_id>/',views.single_products,name="single_products"),
    path('product_filter/<cate_name>',views.product_filter,name="product_filter"),
    path('signup/',views.signup,name="signup"),
    path('',views.signin,name="signin"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('signin_page/',views.signin_page,name="signin_page"),
    path('logout_page/',views.logout_page,name="logout_page"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart/',views.cart,name="cart"),
    path('delete_cart/<int:p_id>/', views.delete_cart, name="delete_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('save_order/', views.save_order, name="save_order"),
    path('payment/', views.payment, name="payment"),




]