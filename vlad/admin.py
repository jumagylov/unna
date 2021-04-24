from django.contrib import admin
from .models import VladModels
# Register your models here.


class VladMainModelsAdmin(admin.ModelAdmin):
    list_display = ('from_whom', 'user_exel_file', 'add_time')
    list_display_links = ('from_whom', 'user_exel_file')
    list_filter = ('add_time',)


admin.site.register(VladModels, VladMainModelsAdmin)
