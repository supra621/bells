import gremlin.views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import core.views
import gremlin.views

from . import views

urlpatterns = [
    path('', views.test_view),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('core/', core.views.test_app_view),
    path('gremlin/', gremlin.views.test_graph),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
