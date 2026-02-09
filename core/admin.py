from django.contrib import admin
from .models import Ad
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display=('title','price','phone','created_at','image')
    search_fields=('title',)

# Register your models here.
