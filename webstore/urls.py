from django.urls import path, include, re_path
from webstore.views import HomeView, CategoryViews, BrandView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path("category/", CategoryViews.as_view(), name='category-views'),
    path('brand/', BrandView.as_view, name='brand-views'),
    
]

