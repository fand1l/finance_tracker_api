from django.urls import path, include

urlpatterns = [
    path('finance/', include('finance.urls')),
    path('users/', include('users.urls')),
]