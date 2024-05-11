import json
import parte1_pb2 as pb

# Cargar los datos JSON
with open('sample_request_data.json', 'r') as file:
    data = json.load(file)

# Lista para almacenar mensajes serializados
serialized_messages = []

# Iterar sobre cada entrada de datos y crear un mensaje gRPC
for index in range(len(data['taxi_id'])):
    # Crear una nueva instancia del mensaje TaxiDetails
    request = pb.TaxiDetails(
        taxi_id=data['taxi_id'][str(index)],
        conductor_id=data['conductor_id'][str(index)],
        pasajero_id=data['pasajero_id'][str(index)].split(', '),  # Dividir la cadena en lista
        costo_estimado=data['costo_estimado'][str(index)]
    )
    
    # Serializar el mensaje a formato binario
    serialized_message = request.SerializeToString()
    serialized_messages.append(serialized_message)

# Guardar los mensajes en formato binario en un archivo
with open('output_p1b.bin', 'wb') as bin_file:
    for message in serialized_messages:
        bin_file.write(message)

# Imprimir los primeros 10 mensajes convertidos para verificar
for message in serialized_messages[:10]:
    print(message)
