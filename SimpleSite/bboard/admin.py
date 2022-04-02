from django.contrib import admin
from  .models import Bb, Categories


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Categories)
