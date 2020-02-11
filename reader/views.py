from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class ReaderList(LoginRequiredMixin, ListView):     # 讀者列表
    model = Reader
    ordering = ['realname']     # 依姓名排序
    paginate_by = 1

class ReaderView(LoginRequiredMixin, DetailView):   # 檢視讀者
    model = Reader

class ReaderAdd(LoginRequiredMixin, CreateView):    # 新增讀者
    model = Reader
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('reader_list')

class ReaderEdit(LoginRequiredMixin, UpdateView):   # 編輯讀者
    model = Reader
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('reader_list')

class ReaderDelete(LoginRequiredMixin, DeleteView): # 刪除讀者
    model = Reader
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('reader_list')