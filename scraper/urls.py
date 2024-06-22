from django.urls import path
from .views import SearchDetailView


urlpatterns = [
    path('api/my_view/', SearchDetailView.as_view(), name='my_model-list-create'),
]
