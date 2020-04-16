from django.urls import path
from .views import *

urlpatterns = [
    path('', AnecdotesList.as_view(), name='anecdotes_list_url'),
    path('create/', AnecdoteCreate.as_view(), name='anecdote_create_url'),
    path('<int:id>/', AnecdoteDetails.as_view(), name='anecdote_detail_url'),
    path('<int:id>/update/', AnecdoteUpdate.as_view(), name='anecdote_update_url'),
    path('<int:id>/delete/', AnecdoteDelete.as_view(), name='anecdote_delete_url'),
    path('tags/', TagsList.as_view(), name='tags_list_url'),
    path('tag/<int:id>/', TagDetails.as_view(), name='tag_detail_url'),
    path('tags/<int:id>/', TagDetails.as_view(), name='tag_detail_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<int:id>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<int:id>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<int:id>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('tag/<int:id>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('users/', UsersList.as_view(), name='users_list_url'),
    path('check/', AnecdotesCheckDups.as_view(), name='check_dup_url'),
]
