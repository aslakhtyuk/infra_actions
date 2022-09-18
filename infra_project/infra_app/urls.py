from django.urls import includes, path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', includes(views.index, name='index')),
    path('second/', includes(views.second_page, name='second_page')),

]
