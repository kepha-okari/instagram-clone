from django.contrib import admin
from .models import Comments,Image,Tag,Profile

# Register your models here.
admin.site.register(Comments)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Profile)
