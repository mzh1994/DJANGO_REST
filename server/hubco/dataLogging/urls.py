from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'get_input_data', views.input_data_ViewSet,basename='input_data')
router.register(r'get_report_data', views.app_daily_stats_ViewSet)
router.register(r'get_kks_data', views.kks_description_ViewSet)

urlpatterns = [    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_api'))
]