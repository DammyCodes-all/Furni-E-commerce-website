from django.contrib import admin
from .models import furnitures,team,Cart,ContactRequest

# Register your models here.
admin.site.register(furnitures)
admin.site.register(team)
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'timestamp')
    search_fields = ('email', 'firstname')