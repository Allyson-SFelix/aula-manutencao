from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Olá, Djanguinho!",
        "status": "ok"
        })