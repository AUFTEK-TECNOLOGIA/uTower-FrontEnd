from django.urls import path
from .views import MaterialLoginView

urlpatterns = [
    path('login/', MaterialLoginView.as_view(), name='login'),
    # outras rotas aqui
]
