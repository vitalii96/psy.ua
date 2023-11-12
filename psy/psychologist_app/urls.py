from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', ContactInformation.as_view(), name='contact'),
    path('education/', Education.as_view(), name='education'),
    # path('base/', Base.as_view(), name='base'),
    # path('test/', test, name='test'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)