from django.urls import path
from .views import ImageUpload

urlpatterns = [
    path('', ImageUpload.as_view()),
]
