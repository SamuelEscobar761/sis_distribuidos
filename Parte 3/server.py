# server.py
from concurrent.futures import ThreadPoolExecutor
import grpc
from grpc_reflection.v1alpha import reflection
import uuid
import logging as log
import parte2_pb2 as pb
import parte2_pb2_grpc as rpc
import config
import validation

log.basicConfig(level=log.INFO)

def gen_id():
    """ Genera un UUID hexadecimal único para cada viaje. """
    return uuid.uuid4().hex

class Viaje(rpc.ViajeServiceServicer):
    def Start(self, request, context):
        """ Maneja las solicitudes de inicio de viaje, realizando validaciones y procesando la lógica del negocio. """
        error = validation.validate_request(request)
        if error:
            log.error(f"Error en la validación de la solicitud: {error}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(error)
            return pb.StartResponse()
        log.info(f'Recepción de solicitud de viaje: {request}')
        id_viaje = gen_id()
        costo_base = 3
        if request.tipoViaje == pb.TipoViaje.POOL:
            costo_viaje = costo_base / len(request.pasajero_id) if request.pasajero_id else costo_base
        elif request.tipoViaje == pb.TipoViaje.PREMIUM:
            costo_viaje = costo_base * 1.25
        else:
            costo_viaje = costo_base

        respuesta = pb.StartResponse(viaje_id=id_viaje, costo_cliente=costo_viaje)
        log.info(f'Viaje iniciado con ID: {id_viaje} y costo: {costo_viaje}')
        return respuesta

if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    rpc.add_ViajeServiceServicer_to_server(Viaje(), server)
    service_names = (
        pb.DESCRIPTOR.services_by_name['ViajeService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)
    server.add_insecure_port(f'{config.host}:{config.port}')
    server.start()
    log.info(f'El servidor está listo y escuchando en {config.host}:{config.port}')
    server.wait_for_termination()
