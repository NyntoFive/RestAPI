from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/photos')


class CKKItem(models.Model):
    name= models.CharField(max_length=150)
    sku = models.CharField(max_length=50)
    crawled_date= models.DateTimeField(blank=True,null=True)
    description=models.TextField()
    desc_text=models.TextField()
    price= models.DecimalField(max_digits=8,decimal_places=2)
    metaKeywords=models.TextField()
    breadcrumbs=models.TextField()
    main_image = models.ImageField(storage=fs, blank=True,null=True)
    images = models.TextField()
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    url = models.URLField(blank=True)

# name=d['name']
# sku=d['sku']
# crawl_date=d['crawl_date']
# date_str=d['date_str']
# description=d['description']
# desc_text=d['desc_text']
# price=d['price']
# metaKeywords=d['metaKeywords']
# breadcrumbs=d['breadcrumbs']
# image=d['image']
# images=d['images']
# category=d['category']
# subcategory=d['subcategory']