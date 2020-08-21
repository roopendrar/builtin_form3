from django.urls import path
from app12 import views
app_name="app12"


urlpatterns = [
    path('builtin/',views.builtin,name="builtin"),

]
