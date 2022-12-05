from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from logic.proc_query import get_query_input
from django.core.paginator import Paginator
from logic.main import vectorial_model, boolean_model

def index(request):
    return render(request, 'index.html')

# def get_query(request):

#     type_query = request.GET["choices-single-defaul"] #para saber luego q modelo aplicar
#     query = request.GET["search"] #Consulta
#     process_query = get_query_input(query)
#     return HttpResponse(type_query)

class DocumentList(ListView): #Vistas de los recursos en PDF###################################
    
    def get(self, request : HttpRequest) -> HttpResponse:
        type_query = request.GET["choices-single-defaul"] #para saber luego q modelo aplicar
        query = request.GET["search"] #Consulta desde la web
        resource = []
        if(type_query == "Vectorial"):
            process_query = get_query_input(query)
            resource = vectorial_model(process_query)
        elif(type_query == "Boolean"):
            resource = boolean_model(query)
            
        paginator = Paginator(resource, 12)
        page = request.GET.get('page')
        resources = paginator.get_page(page)


        return render(request,'documents.html', {'document_list': resources})