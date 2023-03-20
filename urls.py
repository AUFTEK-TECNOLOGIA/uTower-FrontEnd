from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=forms.AuthenticationForm), name='login'),
]