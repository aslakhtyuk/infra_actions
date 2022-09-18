from django.urls import include, path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', include(views.index, name='index')),
    path('second/', include(views.second_page, name='second_page')),

]
