from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.
class Newsletter(models.Model):
    email= models.EmailField()
    
    def __str__(self):
        return f"E-Mail: {self.email}"
 
   
STATUS =(
    (0,"Borrador"),
    (1,"Publicado")
)

class Post(models.Model):
    
    titulo = models.CharField(max_length=200, unique=True)
    subtitulo = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200, unique=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    actualizado = models.DateTimeField(auto_now= True)
    contenido = RichTextUploadingField() 
    creado = models.DateField(auto_now_add=True)
    estado = models.IntegerField(choices=STATUS, default=0)
    
    class meta:
        
        orden = ['-creado']
        
    def __str__(self):
        return self.titulo
