# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parte2.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cparte2.proto\x1a\x1fgoogle/protobuf/timestamp.proto\".\n\tUbicacion\x12\x0f\n\x07latitud\x18\x01 \x01(\x01\x12\x10\n\x08longitud\x18\x02 \x01(\x01\"\xb5\x01\n\x0cStartRequest\x12\x0f\n\x07taxi_id\x18\x01 \x01(\x03\x12\x14\n\x0c\x63onductor_id\x18\x02 \x01(\t\x12\x13\n\x0bpasajero_id\x18\x03 \x03(\t\x12\x1e\n\ntipo_viaje\x18\x04 \x01(\x0e\x32\n.TipoViaje\x12\x1d\n\tubicacion\x18\x05 \x01(\x0b\x32\n.Ubicacion\x12*\n\x06tiempo\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\rStartResponse\x12\x10\n\x08viaje_id\x18\x01 \x01(\t\x12\x15\n\rcosto_cliente\x18\x02 \x01(\x01*/\n\tTipoViaje\x12\x0b\n\x07REGULAR\x10\x00\x12\x08\n\x04POOL\x10\x01\x12\x0b\n\x07PREMIUM\x10\x02\x32\x38\n\x0cViajeService\x12(\n\x05Start\x12\r.StartRequest\x1a\x0e.StartResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'parte2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TIPOVIAJE']._serialized_start=339
  _globals['_TIPOVIAJE']._serialized_end=386
  _globals['_UBICACION']._serialized_start=49
  _globals['_UBICACION']._serialized_end=95
  _globals['_STARTREQUEST']._serialized_start=98
  _globals['_STARTREQUEST']._serialized_end=279
  _globals['_STARTRESPONSE']._serialized_start=281
  _globals['_STARTRESPONSE']._serialized_end=337
  _globals['_VIAJESERVICE']._serialized_start=388
  _globals['_VIAJESERVICE']._serialized_end=444
# @@protoc_insertion_point(module_scope)
