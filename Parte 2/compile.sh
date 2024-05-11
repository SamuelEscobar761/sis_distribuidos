#!/bin/bash

# Directorio actual
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Compilación de archivos .proto con grpc_tools.protoc
python3 -m grpc_tools.protoc -I"$DIR" --python_out="$DIR" --grpc_python_out="$DIR" "$DIR/parte2.proto"
