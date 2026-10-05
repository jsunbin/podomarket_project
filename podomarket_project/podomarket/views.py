from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from allauth.account.views import PasswordChangeView
from .models import Post
from .forms import PostForm


class IndexView(ListView):
    model = Post
    template_name = 'podomarket/index.html'
    context_object_name = 'posts'
    paginate_by = 8
    ordering = ['-dt_updated']


class PostDetailView(DetailView):
    model = Post
    template_name = 'podomarket/post_detail.html'
    pk_url_kwarg = 'post_id'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "podomarket/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

    def get_success_url(self) -> str:
        return reverse('post_detail', kwargs={'post_id': self.object.id})


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')