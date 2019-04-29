from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Orcamento_adesivo, Orcamento_filme
from .forms import OcadesivoForm, OcfilmeForm



# Views

@method_decorator(login_required, name='dispatch')
class Cadastro(TemplateView):

    template_name = 'moduloof/cadastro.html'


@method_decorator(login_required, name='dispatch')
class Novo_ocadesivo(CreateView):

    model = Orcamento_adesivo
    template_name = 'moduloof/orcadesivo.html'
    fields = '__all__'
    success_url = reverse_lazy('url_ladesivo')


@method_decorator(login_required, name='dispatch')
class Dupocadesivo(UpdateView):

    model = Orcamento_adesivo
    template_name = 'moduloof/duporcadesivo.html'
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class Delocadesivo(DeleteView):

    model = Orcamento_adesivo
    template_name = 'moduloof/delete_confirm.html'

    def get_success_url(self):
        return reverse_lazy('url_ladesivo')


@method_decorator(login_required, name='dispatch')
class Locadesivo(ListView):

    model = Orcamento_adesivo
    template_name = 'moduloof/lorcadesivo.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OcadesivoForm()
        return context


@method_decorator(login_required, name='dispatch')
class Cons_ocadesivo(UpdateView):

    model = Orcamento_adesivo
    template_name = 'moduloof/orcadesivo.html'
    fields = '__all__'

    def get_success_url(self):
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        companyid = self.kwargs['pk']
        return reverse_lazy('url_cons_ocadesivo', kwargs={'pk': companyid})


@method_decorator(login_required, name='dispatch')
class Novo_ocfilme(CreateView):

    model = Orcamento_filme
    template_name = 'moduloof/orcfilme.html'
    fields = '__all__'
    success_url = reverse_lazy('url_lfilme')


@method_decorator(login_required, name='dispatch')
class Delocfilme(DeleteView):

    model = Orcamento_filme
    template_name = 'moduloof/delete_confirm.html'

    def get_success_url(self):
        return reverse_lazy('url_lfilme')


@method_decorator(login_required, name='dispatch')
class Dupocfilme(UpdateView):

    model = Orcamento_filme
    template_name = 'moduloof/duporcfilme.html'
    fields = '__all__'


"""
@login_required
def duporcfilme(request, pk):
    data = {}
    cons = Orcamento_filme.objects.get(pk=pk)
    if request.method == 'POST':
        form = OcfilmeForm(request.POST or None)

        if form.is_valid():
            form.save()
            cons = Orcamento_filme.objects.all().order_by("-id")[0]
            return redirect('url_cons_ocfilme', cons.id)

        data['form'] = form
        return render(request, 'moduloof/orcfilme.html', data)


    else:

        form = OcfilmeForm(request.POST or None, instance=cons)
        data['form'] = form

    return render(request, 'moduloof/duporcfilme.html', data)
"""


@method_decorator(login_required, name='dispatch')
class Locfilme(ListView):

    model = Orcamento_filme
    template_name = 'moduloof/lorcfilme.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OcfilmeForm()
        return context


@method_decorator(login_required, name='dispatch')
class Cons_ocfilme(UpdateView):

    model = Orcamento_filme
    template_name = 'moduloof/orcfilme.html'
    fields = '__all__'

    def get_success_url(self):
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        companyid = self.kwargs['pk']
        return reverse_lazy('url_cons_ocfilme', kwargs={'pk': companyid})
