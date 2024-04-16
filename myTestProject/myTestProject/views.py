from django.http import HttpResponse
from django.http import JsonResponse
def home_page(request):
    return HttpResponse("This is Home")

def contact_page(request):
     return HttpResponse("This is Contact")

def json_responce(request):
     data={
          'name':"Kishor",
          'sirname':"Jadhav",
          'contactNo':"9322455007"

     }
     return JsonResponse(data)