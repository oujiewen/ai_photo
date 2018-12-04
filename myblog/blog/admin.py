from django.contrib import admin

from models import Guest
from models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display=['name','status','start_time','id']
    search_fields=['name','id']
    list_filter=['status']


class GusetAdmin(admin.ModelAdmin):
    list_display = ['event','realname', 'phone', 'email', 'sign','create_time']
    search_fields = ['realname', 'sign']
    list_filter = ['sign']


admin.site.register(Guest,GusetAdmin)
admin.site.register(Event,EventAdmin)
