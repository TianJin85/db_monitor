from django.urls import path

from role import views

app_name = "role"

urlpatterns = [
    path('api/role', views.ApiRoleList.as_view()),
    path('api/role/<int:pk>', views.ApiRoleDetail.as_view()),
    path('api/role/page=<int:pk>', views.PageInfo),
]
