from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import kks_description, data_input_table,app_daily_stats

class kks_description_serilaizer(serializers.ModelSerializer):
    class Meta:
        model = kks_description
        fields = ('kks', 'category','location','area','description','process_parameter','unit',
                    'local_only','daily_reading','standby_readings','min_value','max_value')

class data_input_table_serilaizer(serializers.ModelSerializer):
    
    kks_code = serializers.SlugRelatedField(queryset=kks_description.objects.all(),slug_field='kks')
    kks_description = serializers.SlugRelatedField(queryset=kks_description.objects.all(),slug_field='description')
    
    class Meta:
        model = data_input_table
        fields = ('kks_code','kks_description','date','value','inactive','remarks')
    
    def create(self,request):
        return print(request.body)
        
class app_daily_stats_serilaizer(serializers.ModelSerializer):
    class Meta:
        model = app_daily_stats
        fields = ('date', 'shift','max_value_breached','min_value_breached','kks_inactive_count',
                   'kks_reading_percentage')
        read_only_fields = ('id','date', 'shift','max_value_breached',
                            'min_value_breached','kks_inactive_count','kks_reading_percentage')