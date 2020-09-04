import django_filters.rest_framework

class SearchBackend(django_filters.rest_framework.DjangoFilterBackend):
    """Enable Search on Video title & description
    """
    def filter_queryset(self, request, queryset, view):

        if 'q_key' and 'q_value' in request.query_params:
            try:
                search_field = request.query_params['q_key'] + "__icontains"
                f = {
                    search_field: request.query_params.get('q_value')
                }
                queryset = queryset.filter(**f)
            except ValidationError as e:
                pass
        return queryset
