from django.shortcuts import render, redirect
from .models import CHMED,WestMED
from MedLang_Chat.utils.Paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html')

# def login(request):
#     pass
#     return render(request, 'login/login.html')

def chdrugdb(request):
    # search
    data_dict = {}
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict["med_name__contains"] = search_data
    
    med_data = CHMED.objects.filter(**data_dict).order_by("id")

    page_object = Paginator(request, med_data,page_size=10,page_param="page")
    page_medata = page_object.page_queryset
    page_object.html()
    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "page_data": page_medata,
        "search_data": search_data,
        "page_string": page_string,
        "head_page":head_page,
        "end_page": end_page
    }

    return render(request, "DrugInfo/chdrugdb.html", context)

def westdrugdb(request):
    data_dict = {}
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict["med_name__contains"] = search_data
    med_data = WestMED.objects.filter(**data_dict).order_by("id")

    page_object = Paginator(request, med_data,page_size=10,page_param="page")
    page_medata = page_object.page_queryset
    page_object.html()
    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "page_data": page_medata,
        "search_data": search_data,
        "page_string": page_string,
        "head_page":head_page,
        "end_page": end_page
    }
    return render(request, "DrugInfo/westdrugdb.html", context)

def chat(request):
    pass
    return render(request, 'chat.html')

def error(request):
    pass
    return render(request, 'error.html')

def issue(request):
    pass
    return render(request,'issue.html')
