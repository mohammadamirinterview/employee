from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token
from restapp import views

urlpatterns = [
    path('', views.redirect_view),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('api/employees/', views.EmployeeList.as_view()),
    path('api/employees/<int:pk>', views.EmployeeListById.as_view()),
    path('docs/', include_docs_urls(title='restapp')),
    path('', include('django_prometheus.urls')),
]
