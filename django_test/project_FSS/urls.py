from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('project_FSS/', views.index, name='all-project_FSS'), # notre_domaine.com/fssbook
    path('project_FSS/<slug:fssbook_slug>', views.fssbook_details, name='fssbook_details')
]