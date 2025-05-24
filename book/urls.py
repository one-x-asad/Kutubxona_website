from django.urls import path
from .views import home,con, Book,Category

urlpatterns=[
    path('',home,name="saxifa"),
    path("contact/",con,name="con"),
    path("add_book/",Book,name="addd"),
    path("add_cat/",Category,name="Cat"),
]