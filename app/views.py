from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Usuario
from .forms import UsuarioForm
from .tasks import enviar_email_boas_vindas

#Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home_template.html'

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'user/listar_template.html'
    context_object_name = 'usuarios'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'user/detail_template.html'
    context_object_name = 'usuario'
    pk_url_kwarg = 'usuario_id'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'user/criar_template.html'
    success_url = reverse_lazy('listar_usuarios')

    def form_valid(self, form):
        response = super().form_valid(form)
        enviar_email_boas_vindas.delay(self.object.nome, self.object.email)
        return super().form_valid(form)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'user/forms_template.html'
    context_object_name = 'usuario'
    pk_url_kwarg = 'usuario_id'

    def get_success_url(self):
        return reverse_lazy('detalhes_usuario', kwargs={'usuario_id': self.object.id})

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'user/delete_template.html'
    context_object_name = 'usuario'
    pk_url_kwarg = 'usuario_id'
    success_url = reverse_lazy('listar_usuarios')

