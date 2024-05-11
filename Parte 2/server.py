from concurrent.futures import ThreadPoolExecutor
import grpc
import uuid
from grpc_reflection.v1alpha import reflection
import logging as log
import parte2_pb2 as pb
import parte2_pb2_grpc as rpc
import config  # Importar el archivo de configuración

log.basicConfig(level=log.INFO)

def gen_id():
    return uuid.uuid4().hex

class Viaje(rpc.ViajeService):
    def Start(self, request, context):
        log.info('Recepción de solicitud de viaje: %s', request)
        id_viaje = gen_id()
        costo_base = 3
        if request.tipo_viaje == pb.TipoViaje.POOL:
            costo_viaje = costo_base / len(request.pasajero_id)
        elif request.tipo_viaje == pb.TipoViaje.PREMIUM:
            costo_viaje = costo_base * 1.25
        else:
            costo_viaje = costo_base
        respuesta = pb.StartResponse(viaje_id=id_viaje, costo_cliente=costo_viaje)
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
    log.info('El servidor está listo y escuchando en %s:%s', config.host, config.port)
    server.wait_for_termination()
