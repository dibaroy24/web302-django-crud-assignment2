from django.urls import path
from .views import WWESuperstarList, WWESuperstarDetail, WWESuperstarCreate, WWESuperstarUpdate, WWESuperstarDelete

urlpatterns = [
    path('', WWESuperstarList.as_view(), name='home'),
    path('<int:pk>', WWESuperstarDetail.as_view(), name='detail'),
    path('add', WWESuperstarCreate.as_view(), name='add'),
    path('edit/<int:pk>', WWESuperstarUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', WWESuperstarDelete.as_view(), name='delete')
]
