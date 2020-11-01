from django.urls import path
from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('ayuda/', views.ayuda, name='necesitoayuda'),
            path('amistadestoxicas/', views.amistadestoxicas, name='necesitoayuda2'),
            path('diferencias/', views.diferencias, name='necesitoayuda3'),
            path('suicidio/', views.suicidio, name='necesitoayuda4'),
            path('acososexual/', views.acososexual, name='necesitoayuda5'),
            path('redesSociales/', views.redesSociales, name='necesitoayuda6'),
            path('paginasAyuda/', views.paginasAyuda, name='necesitoayuda7'),
            path('entrada/', views.EntradaListView.as_view(), name='entradas'),
            path('contacto/', views.contacto, name='contacto'),
            path('entrada/<str:pk>', views.EntradaDetailView.as_view(), name='entrada-detail'),
]

urlpatterns += [
    path('entrada/create/', views.entrada_new,name='entrada_create'),
    path('entrada/<str:pk>/update/', views.entrada_edit, name='entrada_update'),
    path('entrada/<str:pk>/delete/', views.EntradaDelete.as_view(), name='entrada_delete'),
]