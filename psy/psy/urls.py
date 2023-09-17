from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('psychologist_app.urls')),
    path('', include('review_app.urls')),
    path('', include('client_app.urls')),
    path('', include('blog.urls')),
    path('', include('telegram_bot_app.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns