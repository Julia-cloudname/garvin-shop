from django.urls import path
from . import views
from .views import history

urlpatterns = [
    path('', views.history, name='history'),
    # path('history/remove/<int:product_id>/', views.remove_from_history, name='remove_from_history'),
]