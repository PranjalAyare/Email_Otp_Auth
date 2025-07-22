from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("🎉 Email OTP Auth API is running!")

urlpatterns = [
    path('', home),  # Root route
    path('admin/', admin.site.urls),
    path('api/', include('authapp.urls')),
]
