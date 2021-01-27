from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', views.GenericSnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.GenericSnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlighted/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

"""Registering the viewsets with the router is similar to providing a urlpattern. 
We include two arguments - the URL prefix for the views, and the viewset itself.
The DefaultRouter class we're using also automatically creates the API root view 
for us, so we can now delete the api_root method from our views module."""

from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
