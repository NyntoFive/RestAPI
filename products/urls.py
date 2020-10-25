from django.urls import path
from .views import CKKItemListView, CKKItemDetailView
from products.serializers import CKKItemSerializer

urlpatterns = [
    path('',CKKItemListView.as_view(), name="ckk_list"),
    path('<int:pk>/',CKKItemDetailView.as_view(), name="ckk_detail"),
]