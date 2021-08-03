from django.db import models

# Create your models here.

class kks_description(models.Model):
    kks = models.CharField(max_length=50,db_column='kks',primary_key=True)
    category = models.CharField(max_length=50,db_column='category',null=True)
    location = models.CharField(max_length=50, db_column='location',null=True)
    area = models.CharField(max_length=200,db_column='area',null=True)
    description = models.CharField(max_length=200,db_column='description',null=True)
    process_parameter = models.CharField(max_length=200,db_column='process_parameter',null=True)
    unit = models.CharField(max_length=200,db_column='unit',null=True)
    local_only= models.CharField(max_length=200,db_column='local_only',null=True)
    daily_reading = models.CharField(max_length=200,db_column='daily_reading',null=True)
    standby_readings = models.CharField(max_length=200,db_column='standby_readings',null=True)
    min_value = models.FloatField(db_column='min_value',null=True)
    max_value = models.FloatField(db_column='max_value',null=True)

    class Meta:
        db_table = 'kks_description'

class data_input_table(models.Model):
    kks_code = models.ForeignKey(kks_description,on_delete=models.CASCADE,db_column='kks_code',
                                                                          related_name='kks_code',
                                                                          blank=True,
                                                                          null=True,
                                                                          to_field = 'kks') 
    kks_description = models.ForeignKey(kks_description,null=True,blank=True,
                                                        on_delete=models.CASCADE,
                                                        db_column='kks_description',
                                                        related_name='kks_description',
                                                        to_field = 'kks')
    date = models.CharField(max_length=50,db_column='date')
    value = models.FloatField(db_column='value',null=True)
    inactive = models.CharField(max_length=10,db_column='inactive',null=True)
    remarks = models.CharField(max_length=200,db_column='remarks',null=True)

    class Meta:
        db_table = 'data_input_table'
        unique_together = (("kks_code", "date"))
    
    def __str__(self):
        return f'{self.kks_code.kks,self.kks_description.description,self.date,self.value,self.inactive}'

class app_daily_stats(models.Model):
    date = models.CharField(max_length=20,db_column='date',null=True)
    shift = models.CharField(max_length=20,db_column='shift',null=True)
    max_value_breached = models.IntegerField(db_column='max_value_breached',null=True)
    min_value_breached = models.IntegerField(db_column='min_value_breached',null=True)
    kks_inactive_count = models.IntegerField(db_column='kks_inactive_count',null=True)
    kks_reading_percentage = models.FloatField(max_length=200,db_column='kks_reading_percentage',null=True)

    class Meta:
        db_table = 'app_daily_stats'
    
    def __str__(self):
        return f'{self.date,self.shift,self.max_value_breached,self.min_value_breached,self.kks_inactive_count,self.kks_reading_percentage}'
