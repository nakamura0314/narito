from django.shortcuts import render, redirect
from .forms import DayCreateForm
from .models import Day


def index(request):
    context = {
        'day_list': Day.objects.all(),
    }
    return render(request, 'diary/day_list.html', context)


def add(request):
    # 送信内容を基にフォームを作る。POSTじゃなければ、空のフォーム
    form = DayCreateForm(request.POST or None)

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)
