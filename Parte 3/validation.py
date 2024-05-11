# validation.py
import re
from parte2_pb2_grpc import TipoViaje

def validate_request(request):
    if not request.taxi_id > 0:
        return "taxi_id debe ser positivo"
    if request.conductor_id == "":
        return "conductor_id es requerido"
    if not request.pasajero_id:
        return "al menos un pasajero_id es requerido"
    if request.tipoViaje not in (TipoViaje.REGULAR, TipoViaje.POOL, TipoViaje.PREMIUM):
        return "tipoViaje no válido"
    if not (-90 <= request.ubicacion.lat <= 90 and -180 <= request.ubicacion.lng <= 180):
        return "ubicacion no válida"
    try:
        # Intenta convertir el string de tiempo a objeto datetime para verificar su validez
        import dateutil.parser
        dateutil.parser.parse(request.tiempo)
    except ValueError:
        return "tiempo no válido"
    return None  # No error
