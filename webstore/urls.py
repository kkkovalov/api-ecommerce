from django.urls import path, include
from webstore.views import HomeView, CategoryViews


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/', CategoryViews.as_view(), name='category-views'),
]

