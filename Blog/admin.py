from django.contrib import admin
from .models import Post, Newsletter

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'estado','creado')
    list_filter = ("estado",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'url': ('titulo',)}

admin.site.register(Newsletter)
admin.site.register(Post, PostAdmin)