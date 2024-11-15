from django.contrib import admin
from .models import Mehmonhonlar

class MehmonhonlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_time', 'address', 'star_rating')
    search_fields = ('title', 'address')
    list_filter = ('star_rating',)

admin.site.register(Mehmonhonlar, MehmonhonlarAdmin)
