from django.urls import path

from .views import (
    CustomLoginView, users_list, users_add,
    user_detail, user_update, user_delete
)

app_name = 'account'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('users/list/', users_list, name='users_list'),
    path('users/add/', users_add, name='add_user'),
    path('users/detail/<int:id>/', user_detail, name='user_detail'),
    path('users/update/<int:id>/', user_update, name='user_update'),
    path('users/delete/<int:id>/', user_delete, name='user_delete'),
]