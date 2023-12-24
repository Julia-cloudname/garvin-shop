from django.urls import path
from . import views
from .views import view_history

urlpatterns = [
    path('', views.view_history, name='view_history'),
    path('history/remove/<int:product_id>/', views.remove_from_history, name='remove_from_history'),
]