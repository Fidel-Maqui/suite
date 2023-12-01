from django_unicorn.components import UnicornView


class SearchbynameView(UnicornView):
    something_safe = ""

    class Meta:
        safe = ("something_safe", )