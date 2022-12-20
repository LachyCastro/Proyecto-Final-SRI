from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from logic.proc_query import get_query_input
from django.core.paginator import Paginator
from logic.main import vectorial_model, boolean_model, extended_boolean_model
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


# Vistas de los recursos en PDF###################################
class DocumentList(ListView):

    def get(self, request: HttpRequest) -> HttpResponse:
        # para saber luego q modelo aplicar
        type_query = request.GET["choices-single-defaul"]
        query = request.GET["search"]  # Consulta desde la web
        resource = []
        #try:
        if (type_query == "Vectorial"):
            #process_query = get_query_input(query)
            resource = vectorial_model(query)
            print(resource, 'resourseeeeeeeeeeeeeeeeeeee')
        elif (type_query == "Boolean"):
            resource = boolean_model(query)
        elif (type_query == "Extended Boolean"):
            resource = extended_boolean_model(query, False)
        # except Exception as ex:
        #     if ex.args[0] == "unmatched ')'":
        #         messages.error(request, "Wrong parentheses")
        #     else:
        #         messages.error(request, "Invalid query")
        #     return redirect("index")

        return render(request, 'documents.html', {'document_list': resource})
