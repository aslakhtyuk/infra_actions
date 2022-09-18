from django.urls import include, path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', include(views.index, namespace='index')),
    path('second/', include(views.second_page, namespace='second_page')),

]
