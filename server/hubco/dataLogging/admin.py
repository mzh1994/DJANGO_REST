from django.contrib import admin
from .models import data_input_table, kks_description,app_daily_stats

# Register your models here.

admin.site.register(data_input_table)
admin.site.register(kks_description)
admin.site.register(app_daily_stats)

