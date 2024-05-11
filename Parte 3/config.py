from os import environ

# Asumiendo que el codigo_upb es proporcionado y representa un valor numérico
codigo_upb = 56825  # Este debería ser reemplazado por el código real

# Calcular el puerto usando el código UPB
puerto_server = 2024 + codigo_upb % 10
port = int(environ.get('PORT', puerto_server))
host = environ.get('HOST', 'localhost')
