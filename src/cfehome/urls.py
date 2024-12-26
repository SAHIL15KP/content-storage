
from django.contrib import admin
from django.urls import path, include

from landing import views as landing_views
from projects import views as projects_views

urlpatterns = [
    path("",    landing_views.home_page_view, name='home'),
    path("items/", include('items.urls')),
    path("projects/", include('projects.urls')),
    path("about/",    landing_views.about_page_view, name='about'),
    path("activate/project/<slug:handle>/", 
          projects_views.activate_project_view, name='activate_project'),
    path("deactivate/project/", 
           projects_views.deactivate_project_view, name='deactivate_project'),
    path("admin/", admin.site.urls),
]
