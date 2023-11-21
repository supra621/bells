from django.contrib import admin
from django.urls import include, path

import core.views

from . import views

urlpatterns = [
    path('', views.test_view),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('core/', core.views.test_app_view),
]
