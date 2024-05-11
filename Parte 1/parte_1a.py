# Documentar y agregar comentarios al codigo

# Importar las bibliotecas necesarias para enviar el client stub
# Completar
import parte1_pb2 as pb

# Completar las elipsis (...)
solicitud_1 = pb.TaxiDetails(
    taxi_id=12345,
    conductor_id='Sist_dist',
    pasajero_id=['56825', '56835', '56845'],
    costo_estimado=10
)

# Imprimir el mensaje de solicitud:
print("Formato de solicitud:\n",solicitud_1)