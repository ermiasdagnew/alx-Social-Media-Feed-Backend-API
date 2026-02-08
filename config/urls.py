from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Server is running!")

urlpatterns = [
    path('', home),                     # Home page
    path('admin/', admin.site.urls),    # Admin
    path('api/', include('feed.urls'))  # Include your feed app API
]
