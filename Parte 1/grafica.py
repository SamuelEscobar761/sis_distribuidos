import json
import matplotlib.pyplot as plt

# Cargar los datos del archivo JSON
with open('sample_request_data.json', 'r') as file:
    data = json.load(file)

# Preparar los datos para la gráfica
taxi_ids = [data['taxi_id'][str(i)] for i in range(len(data['taxi_id']))]
costos_estimados = [data['costo_estimado'][str(i)] for i in range(len(data['costo_estimado']))]

# Crear la gráfica
plt.figure(figsize=(10, 5))  # Ajusta el tamaño de la gráfica según necesites
plt.scatter(taxi_ids, costos_estimados, color='blue')  # Puntos azules para cada par de datos
plt.title('Costo Estimado vs. ID del Taxi')
plt.xlabel('ID del Taxi')
plt.ylabel('Costo Estimado ($)')

# Guardar la gráfica en un archivo de imagen
plt.savefig('costo_estimado_vs_taxi_id.png')

# Mostrar la gráfica
plt.show()
