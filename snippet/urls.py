from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('snippets/', views.GenericSnippetList.as_view()),
    path('snippets/<int:pk>/', views.GenericSnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
