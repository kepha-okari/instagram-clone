from django.contrib import admin
from .models import Comment,Image,Tag,Profile

# Register your models here.
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Profile)
