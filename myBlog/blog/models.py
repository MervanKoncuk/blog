from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    content = RichTextField(max_length=1000, verbose_name="Blog İçerik")
    image = models.ImageField(upload_to='kisiresmi/',blank = True,null = True,verbose_name="kisi Resmi Ekleyin")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi ")
    
