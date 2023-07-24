from django.urls import path
from .views import add_bio_data

urlpatterns = [
    path('', add_bio_data, name='add_bio_data'),
]