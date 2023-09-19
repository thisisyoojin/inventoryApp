from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

DEFAULT_FILTERS = [DjangoFilterBackend, filters.SearchFilter]
DEFAULT_HTTP_METHODS = ["get", "post", "list", "put", "delete"]