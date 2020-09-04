from django.shortcuts import render, get_object_or_404, redirect
import itertools
# Create your views here.

from django.http import HttpResponse, Http404
from django.views import View
from django.conf import settings
import json
import os
from datetime import datetime
from django.views.generic.base import TemplateView

# class MainPageView(View):
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_JSON_PATH = os.path.join(os.path.dirname(BASE_DIR), 'news.json')

with open(NEWS_JSON_PATH, "r") as f:
    data = json.load(f)


def index(request):
    return redirect('/news/')
    # return HttpResponse("Coming soon")
#settings.NEWS_JSON_PATH["link"]


def news_list_view(request, *args, **kwargs):

    def sort_news(data_raw):
        sorted_news = sorted(data_raw, key=lambda i: i['created'], reverse=True)
        groupped_news = itertools.groupby(sorted_news, lambda i: i['created'][:10])
        data_sorted = list()

        for idx, row in enumerate(groupped_news):
            data_sorted.append(dict())
            data_sorted[idx]["date"] = row[0]
            data_sorted[idx]["lis"] = list()
            for inner in row[1]:
                data_sorted[idx]["lis"].append(inner)
        return data_sorted
    '''function starts here'''
    # if request.method == 'GET':
    if request.GET.get('q'):
        result_search = list()
        for entry in data:
            if request.GET.get('q') in entry['title']:
                result_search.append(entry)
        data_sorted = sort_news(result_search)
    else:
        data_sorted = sort_news(data)

    context = {
        'data_sort': data_sorted,
        'dicts': data,
    }

    return render(request, 'news/index.html', context)


def create_news_view(request, *args, **kwargs):

    print("in create_news_view")
    if request.method == 'POST':
        print("we are in POST")
        title = request.POST.get('title')
        text = request.POST.get('text')
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        link = 0
        for entry in data:
            new = entry['link']
            if new >= link:
                link = new+1
        data.append({'created': dt_string, 'title': title, 'text': text, 'link': link})
        print("check", data)
        return redirect('/news/')

    context = {

    }
    return render(request, "news/create.html", context)


# def news_view(request, *args, **kwargs):
#     with open(NEWS_JSON_PATH, "r") as f:
#         data = json.load(f)
#
#     return render(request, 'news/news.html', {'dicts': data})


def news_detail_view(request, link, *args, **kwargs):

    with open(NEWS_JSON_PATH, "r") as f:
        data = json.load(f)
        for dic in data:
            if dic["link"] == int(link):
                data = dic


    context = {
        'dict': data,
    }
    return render(request, 'news/news.html', context)



# class MainPageView(View):
#     def get(self, request, *args, **kwargs):
#         with open(NEWS_JSON_PATH, "r") as f:
#             data = json.load(f)
#         return render(request, 'news/index.html', context={'dicts': data})


# class NewsView(View):
#     def get(self, request, *args, **kwargs):
#         with open(NEWS_JSON_PATH, "r") as f:
#             data = json.load(f)
#
#         return render(request, 'news/news.html', {'dicts': data})


# class NewsArticleView(View):
#     def get(self, request, link, *args, **kwargs):
#
#         with open(NEWS_JSON_PATH, "r") as f:
#             data = json.load(f)
#             for dic in data:
#                 if dic["link"] == int(link):
#                     data = dic
#
#
#         return render(request, 'news/news.html', context={'dict': data})
#
#
