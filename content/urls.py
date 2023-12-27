from django.urls import path
from .views import ProductListView, ProductDetailView, VideoDetailView
from content import views

app_name = "content"

urlpatterns = [
    
    path('summary/', views.ProductView.as_view(), name='summary'),
    path('remove-from-product/<pk>/',
         views.RemoveFromProductView.as_view(), name='remove-from-product'),
    path('product-chart/', views.product_chart, name='product-chart'),
    path("", ProductListView.as_view(), name='product-list'),
    path("<slug>/", ProductDetailView.as_view(), name='product-detail'),
    path("<slug>/<video_slug>/", VideoDetailView.as_view(), name='video-detail'),
    

    
    
]