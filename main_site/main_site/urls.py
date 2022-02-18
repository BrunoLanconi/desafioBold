from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # allauth url
    path('accounts/', include('allauth.urls')),
    # Including all content of pages folder on our 'requisition dispatcher'
    path("", include("pages.urls", namespace="pages")),
]
