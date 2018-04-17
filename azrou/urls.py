from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from core.views import HomeView
from core.views import GallerieView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^gallerie/(?P<id>\d+)$', GallerieView.as_view(), name='galleriename'),
    url(r"^blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),

]


if settings.DEBUG:
    import debug_toolbar  # NOQA

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
