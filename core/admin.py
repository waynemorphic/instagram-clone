from django.contrib import admin
from core.models import Image_Model, Profile_Model, User_Model
# Register your models here.



# class ImageAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['image_name']}),
#         ('user', {'fields': ['user']}),
#         ('image caption', {'fields': ['image_caption']}),
#     ]
    
admin.site.register(Image_Model)
admin.site.register(Profile_Model)
admin.site.register(User_Model)
