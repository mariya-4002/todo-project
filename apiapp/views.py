from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "API working successfully!"})
