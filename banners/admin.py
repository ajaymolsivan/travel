from django.contrib import admin
from .models import Banner
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'content',]


admin.site.register(Banner, BannerAdmin)
