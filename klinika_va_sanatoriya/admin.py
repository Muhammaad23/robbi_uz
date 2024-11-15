from django.contrib import admin
from .models import Kilinika_sanatoriya

class KilinikaAdmin(admin.ModelAdmin):
    list_display = ['title', 'tier', 'address']
    list_filter = ['tier']
    search_fields = ['title', 'address']

admin.site.register(Kilinika_sanatoriya, KilinikaAdmin)
