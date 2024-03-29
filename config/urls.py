from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from content import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path('admin/', admin.site.urls),

    # ckeditor 
    path('_ckeditor/', include('ckeditor_uploader.urls')),

    
    # Content
    path("products/", include("content.urls", namespace="content")),

    # User management
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("payments/", include("payment.urls")),
    path("", include("core.urls")),
    
    # tailwind things
    path("__reload__/", include("django_browser_reload.urls")),
    # Your stuff: custom urls includes go here
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]
urlpatterns += (
re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
)
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
        
        
urlpatterns +=  staticfiles_urlpatterns()