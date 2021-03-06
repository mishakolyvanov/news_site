from django.db import transaction
from django.http import Http404
from django.shortcuts import render, redirect
from NewsApp.models import News
from .forms import NewsForm


def index(request):
    all_news_list = News.objects.order_by('-pub_date')
    return render(request, 'list.html', {'all_news_list': all_news_list, 'header': 'All News'})


def tag_list(request, tag):
    all_news_list = News.objects.filter(tags__name=tag).order_by('-pub_date')
    return render(request, 'list.html', {'all_news_list': all_news_list, 'header': tag})


def detail(request, news_id):
    try:
        with transaction.atomic():
            a = News.objects.select_for_update().get(id=news_id)
            a.views_count += 1
            a.save()
    except News.DoesNotExist:
        raise Http404("Статья не найдена!")
    return render(request, 'detail.html', {'news': a})


def stat(request):
    stat_news_list = News.objects.order_by('-views_count')
    return render(request, 'stat.html', {'stat_news_list': stat_news_list})


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('NewsApp:index')
        else:
            error = f'Ошибка в форме: {form.errors}'

    form = NewsForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', data)
