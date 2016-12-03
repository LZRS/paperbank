from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from .models import Paper, Tag
from .utils import get_page, get_main_page_context_dict


# Create your views here.
def landing(request):
    """
    This renders the first page that the user sees when
    visiting the application.
    Just rendering the page.
    """
    return render(request, 'landing_page.html')


def main(request):
    """
    This is the main page 
    It just lists the papers current in the database,
  
    TODO: Update to use list django generic views
    """
    context_dict = {}
    papers = Paper.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)

    context_dict['papers_page'] = get_page(papers, page)
    context_dict.update(get_main_page_context_dict())
    return render(request, 'main_page.html', context_dict)


def search(request):
    """
    Searches through the papers and find
    the most appropriate 

    TODO: Update to use django generic views
    """
    context_dict = {}
    question = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    results = Paper.objects.filter(name__icontains=question).order_by('-created_date')
    context_dict['papers_page'] = get_page(results, page)
    context_dict.update(get_main_page_context_dict())
    return render(request, 'main_page.html', context_dict)

def filter_by_tag(request, tag_name):
    """
    This filters through the papers basing
    on the given tag 
  
    TODO: Update to use django generic views
    """
    context_dict = {}
    tag = Tag.objects.filter(name=tag_name)
    page = request.GET.get('page', 1)

    if not tag:
        return redirect(reverse('main_page'))

    results = Paper.objects.filter(tags=tag).order_by('-created_date')
    context_dict['papers_page'] = get_page(results, page)
    context_dict.update(get_main_page_context_dict())
    return render(request, 'main_page.html', context_dict)
