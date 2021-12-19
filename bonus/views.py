from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import render

from django.http import HttpResponse

from .models import Msg, User


def index(request):
    userList = User.objects.all()

    return render(
        request,
        'bonus/index.html',
        context={'user_list': userList})


def addSuggest(request):
    userList = User.objects.all()

    return render(
        request,
        'bonus/addSuggest.html',
        context={'user_list': userList})


class MsgListView(ListView):
    model = Msg
    template_name = 'bonus/msg_list.html'     # 預設檔名，可略
    context_object_name = 'msg_list'          # 預設為 msg_list, 可略

    def get_queryset(self):
        return Msg.objects.order_by('-date')  # 排序與數量

class MsgDetailView(DetailView):
    model = Msg
    template_name = 'bonus/msg_detail.html'   # 預設檔名，可略
