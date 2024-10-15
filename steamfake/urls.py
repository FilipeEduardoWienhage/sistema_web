from django.urls import path

from steamfake import views


urlpatterns = [
    path("categoria", views.categoria_index, name="categorias"),
    path('categoria/cadastro', views.categoria_cadastro),
    path('categoria/cadastrar', views.categoria_cadastrar),
    path('categoria/apagar/<int:id>', views.categoria_apagar),
]