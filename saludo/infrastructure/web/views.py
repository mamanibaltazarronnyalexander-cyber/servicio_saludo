import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from saludo.application.services.saludar_service import SaludarService

saludar_use_case = SaludarService()


@csrf_exempt
@require_POST
def saludar_view(request):
    try:
        body = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)

    nombre = body.get("nombre")
    if not isinstance(nombre, str):
        return JsonResponse({"error": "El campo 'nombre' es obligatorio"}, status=400)

    try:
        mensaje = saludar_use_case.ejecutar(nombre)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"mensaje": mensaje})
