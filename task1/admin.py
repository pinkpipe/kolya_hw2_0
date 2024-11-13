from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', 'size', 'age_limited')
    fieldsets = (
        ('Description', {
            'fields':
                ('title', 'description')
        }),
        ('More', {
            'fields':
                ('cost', 'size', 'age_limited')
        })
    )
