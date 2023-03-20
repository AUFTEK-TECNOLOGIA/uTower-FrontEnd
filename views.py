from django.contrib.auth.views import LoginView
from .forms import MaterialLoginForm

class MaterialLoginView(LoginView):
    form_class = MaterialLoginForm
    template_name = 'login.html'
