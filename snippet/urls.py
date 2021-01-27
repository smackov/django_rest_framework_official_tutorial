from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.GenericSnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.GenericSnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlighted/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
