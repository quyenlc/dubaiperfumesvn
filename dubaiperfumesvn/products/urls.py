from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "products"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
]
