from django.contrib import admin
from.models import Argentina
# Register your models here
class ArgentinaAdmin(admin.ModelAdmin):
    list_display=("name","age","height","weight")
admin.site.register(Argentina,ArgentinaAdmin)