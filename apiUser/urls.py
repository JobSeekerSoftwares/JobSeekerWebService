from django.conf.urls import url
from django.urls import path
from apiUser import views

urlpatterns = [
    url(r'^snipp/$', views.empregadores_list),
    url(r'^procurar/(?P<curriculo>\w{0,50})$', views.job_search),
    url(r'^procurando/$', views.job_search2),
    url(r'^meusEmpregos/$', views.meus_empregos),
    url(r'^pessoa/$', views.person_search),
    path('singup/trabalhador/', views.UserTrabalhadorCreate.as_view(), name='accountrabalhador-create'),
    path('singup/empregador/', views.UserEmpregadorCreate.as_view(), name='accounempregador-create')
]
