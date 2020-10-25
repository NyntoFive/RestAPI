from django.shortcuts import get_object_or_404
from products.models import CKKItem
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
from products.serializers import CKKItemSerializer

class CKKItemListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ckk_list.html'

    def get(self, request):
        queryset = CKKItem.objects.all()
        return Response({'products': queryset})

class CKKItemDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ckk_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(CKKItem, pk=pk)
        serializer = CKKItemSerializer(product)
        return Response({'serializer': serializer, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(CKKItem, pk=pk)
        serializer = CKKItemSerializer(product, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'product': product})
        serializer.save()
        return redirect('ckk_list')