from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view
from cars.views import create_cars_view
from user.views import register_view
from user.views import login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
path('register/', register_view, name='register'),
    path('cars/', cars_view, name = 'cars_list'),
    path('create_car/', create_cars_view, name = 'create_car')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)