from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import render

from .models import Msg, User

def index(request):
    msgList = Msg.objects.all().order_by('-date')[:4] # 排序與數量
    print (str(msgList))
    return render(
        request,
        'bonus/index.html',
        context={'msg_list': msgList})

class MsgListView(ListView):
    model = Msg
    template_name = 'bonus/msg_list.html'     # 預設檔名，可略
    context_object_name = 'msg_list'          # 預設為 msg_list, 可略

    def get_queryset(self):
        return Msg.objects.order_by('-date')  # 排序與數量

class MsgDetailView(DetailView):
    model = Msg
    template_name = 'bonus/msg_detail.html'   # 預設檔名，可略
