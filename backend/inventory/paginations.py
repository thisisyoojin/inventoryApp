from rest_framework.pagination import LimitOffsetPagination

class StandardResultsSetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 500
    limit_query_param = "query_limit"
    offset_query_param = "query_offset"
    