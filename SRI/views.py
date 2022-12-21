from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from logic.main import vectorial_model, boolean_model, extended_boolean_model,charge_corpus
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
        if "corpus" in request.GET:
           
            charge_corpus()
            messages.error(request,"charge corpus done!")
            return redirect("index")
        try:
            if (type_query == "Vectorial"):
                resource = vectorial_model(query)
            elif (type_query == "Boolean"):
                resource = boolean_model(query)
            elif (type_query == "Extended Boolean"):
                resource = extended_boolean_model(query, False)
        except Exception as ex:
            print(ex.args[0])
            if ex.args[0] == "unmatched ')'":
                messages.error(request, "Wrong parentheses")
            else:
                messages.error(request, "Invalid query")
            return redirect("index")
        return render(request, 'documents.html', {'document_list': resource})
