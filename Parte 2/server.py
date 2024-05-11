from concurrent.futures import ThreadPoolExecutor
import grpc
import uuid
from grpc_reflection.v1alpha import reflection
import logging as log
import parte2_pb2 as pb
import parte2_pb2_grpc as rpc

# Configurando el logging
log.basicConfig(level=log.INFO)

def gen_id():
    # Generar un identificador único en formato hex
    return uuid.uuid4().hex

class Viaje(rpc.ViajeService):
    def Start(self, request, context):
        log.info('Recepción de solicitud de viaje: %s', request)

        # Generar un nuevo ID para el viaje
        id_viaje = gen_id()

        # Calcular el costo base del viaje
        costo_base = 3  # costo nominal asumido

        # Calcular el costo final del viaje según el tipo
        if request.tipo_viaje == pb.TipoViaje.POOL:
            costo_viaje = costo_base / len(request.pasajero_id)
        elif request.tipo_viaje == pb.TipoViaje.PREMIUM:
            costo_viaje = costo_base * 1.25
        else:
            costo_viaje = costo_base

        # Crear la respuesta según la estructura definida en .proto
        respuesta = pb.StartResponse(viaje_id=id_viaje, costo_cliente=costo_viaje)
        return respuesta

if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rpc.add_ViajeServiceServicer_to_server(Viaje(), server)

    # Configuración para la reflexión del servidor (para explorar servicios)
    services_names = (
        pb.DESCRIPTOR.services_by_name['ViajeService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(services_names, server)

    # Dirección y puerto del servidor
    addr = f'[::]:8456'
    server.add_insecure_port(addr)
    server.start()

    log.info('El servidor está listo y escuchando en el puerto %s', addr)
    server.wait_for_termination()
