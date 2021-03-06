from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .endpoints import DocumentsAPIEndpoint, ImagesAPIEndpoint, PagesAPIEndpoint
from .router import WagtailAPIRouter

v2 = WagtailAPIRouter('wagtailapi_v2')
v2.register_endpoint('pages', PagesAPIEndpoint)
v2.register_endpoint('images', ImagesAPIEndpoint)
v2.register_endpoint('documents', DocumentsAPIEndpoint)

urlpatterns = [
    url(r'^v2beta/', v2.urls),
]
