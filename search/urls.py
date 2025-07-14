from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload'),
    path('', views.search, name='search'),
    path('chat/', views.semantic_search, name='doc_search'),
]
