from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.brands),
    path('new/', views.new_brand),
    path('<str:id>/', views.brand_detail),
    path('<str:id>/edit', views.brand_edit),
    path('<str:brand_id>/cars', views.cars),
    path('<str:brand_id>/cars/new', views.new_car),
    path('<str:brand_id>/cars/<str:car_id>', views.car_detail),
    path('<str:brand_id>/cars/<str:car_id>/edit', views.car_edit),

]