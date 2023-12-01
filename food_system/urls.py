from django.urls import path
from . import views as food_views

urlpatterns = [
    path('', food_views.home),
    path('business/',food_views.business),
    path('business/<int:id_business>/', food_views.product, name='business_detail'),
    path('profile', food_views.profile),
    path('request', food_views.orders),
    path('my_request', food_views.my_request),
    path('available_orders', food_views.available_orders),
    path('about_us/', food_views.about_us),
    path('not_found/', food_views.not_found),
]