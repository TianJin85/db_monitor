from django.urls import path
from monitoring import views

app_name = "monitoring"

urlpatterns = [

    path('api/monitoring-log', views.ApiMonitoringLog.as_view()),
    path('api/monitoring-config', views.ApiMonitoringConfig.as_view()),
    path('api/monitoring-config/<int:pk>', views.ApiMonitoringConfigDetail.as_view()),
    path('api/monitoring-info', views.ApiMonitoringInfo.as_view()),
    path('api/monitoring-run', views.ApiMonitoringRun.as_view()),
    path('api/monitoring-run/<int:pk>', views.ApiMonitoringRunDetail.as_view()),

]
