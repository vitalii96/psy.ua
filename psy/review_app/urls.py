from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('reviews/', reviews, name='reviews'),
    path('reviews/add/', AddReview.as_view(), name='reviews_add'),
    path('reviews/add/', add_review, name='add_review'),


]