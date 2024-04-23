from django.urls import path
from . import views

urlpatterns = [
    # path('load_image', views.GalleryView.as_view()),
    path('load_image', views.CreateGalleryView.as_view()),
    path('list_image', views.ListGalleryView.as_view()),
]
