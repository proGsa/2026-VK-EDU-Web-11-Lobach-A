from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest

def paginate(objects_list, request: HttpRequest, per_page: int = 20):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page', 1)
    
    try:
        page = paginator.page(page_number)
    except (PageNotAnInteger, ValueError):
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    return page