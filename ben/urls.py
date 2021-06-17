from os import name
from django.urls import path
from . import views
urlpatterns =[
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('reviews-create/', views.ReviewCreateView.as_view(), name="reviews-create"),
    path('review-list/', views.ReviewsListView.as_view(), name="reviews-list"),
    path('review-list-home/', views.ReviewsListHomeView.as_view(), name="reviews-list-home")

]