from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categorias
from .forms import FormArticulo, EditarArticulo
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-fechapost']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorias.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context



class ArticuloDetalleVista(DetailView):
    model = Post
    template_name = 'articulo_detalles.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorias.objects.all()
        context = super(ArticuloDetalleVista, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
class Agregar_Post(CreateView):
    model = Post
    form_class = FormArticulo
    template_name = 'agregar_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorias.objects.all()
        context = super(Agregar_Post, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
class UpdatePost(UpdateView):
    model = Post
    form_class = EditarArticulo
    template_name = 'editar_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorias.objects.all()
        context = super(UpdatePost, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
class EliminarPost(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorias.objects.all()
        context = super(EliminarPost, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
class Agregar_Categoria(CreateView):
    model = Categorias
    fields = '__all__'

def CategoriasView(request, cat):
    categorias_post = Post.objects.filter(categorias = cat)
    return render(request, 'categorias.html', {'cat':cat.title(), 'categorias_post':categorias_post})

