from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from logic.main import vectorial_model, boolean_model, extended_boolean_model


def index(request):
    return render(request, 'index.html')


# Vistas de los recursos en PDF###################################
class DocumentList(ListView):

    def get(self, request: HttpRequest) -> HttpResponse:
        # para saber luego q modelo aplicar
        type_query = request.GET["choices-single-defaul"]
        query = request.GET["search"]  # Consulta desde la web
        resource = []
        if (type_query == "Vectorial"):
            resource = vectorial_model(query)
        elif (type_query == "Boolean"):
            resource = boolean_model(query)
        elif (type_query == "Extended Boolean"):
            resource = extended_boolean_model(query, False)
        return render(request, 'documents.html', {'document_list': resource})
