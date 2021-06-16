from django.urls import path
from .views import ImageUpload, ImageUploadtemplate

urlpatterns = [
    path('', ImageUploadtemplate.as_view()),
    path('image-upload', ImageUpload.as_view()),
]
