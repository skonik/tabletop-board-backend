from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tables import views

urlpatterns = [
    path('', views.TablesList.as_view(), name='tables-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
