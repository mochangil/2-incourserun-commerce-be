from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}


class ReviewPagination(PageNumberPagination):
    page_size = 5
    # get 요청으로 page, page_size 수정가능
    # page_size_query_param = 'page_size'
    # page_query_param = 'page'

