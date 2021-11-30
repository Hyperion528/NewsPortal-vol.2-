from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post, Category

from django.views import View
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.shortcuts import render

from .filters import PostFilter
from .forms import PostForm
 
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
 
#from .models import Appointment

class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = ['-date_create']
    paginate_by = 1 # поставим постраничный вывод в один элемент
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
 
        # context['categories'] = Category.objects.all()
        
        return context
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса 
 
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
 
        return super().get(request, *args, **kwargs)
    


class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post_detail.html'  # название шаблона будет product.html
    # context_object_name = 'post'  # название объекта. в нём будет
    # queryset = Post.objects.all()



class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'post_add.html'
    form_class = PostForm
    permission_required = 'news.add_post'


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'post_add.html'
    form_class = PostForm
    permission_required = 'news.change_post'
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
 
 
# дженерик для удаления товара
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
    permission_required = 'news.delete_post'


# class AppointmentView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'make_appointment.html', {})
 
#     def post(self, request, *args, **kwargs):
#         appointment = Appointment(
#             date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
#             client_name=request.POST['client_name'],
#             message=request.POST['message'],
#         )
#         appointment.save()
 
#         return redirect('appointments:make_appointment')