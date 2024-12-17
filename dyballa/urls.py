from django.urls import path
from.import views
urlpatterns=[
    path("",views.dyballa,name="dyballa"),
    path('submit/',views.submit,name="submit")
]