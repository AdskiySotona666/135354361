# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"5\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x10RegisterResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"1\n\rLoginResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2~\n\x0b\x41uthService\x12;\n\x08Register\x12\x15.auth.RegisterRequest\x1a\x16.auth.RegisterResponse\"\x00\x12\x32\n\x05Login\x12\x12.auth.LoginRequest\x1a\x13.auth.LoginResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=20
  _globals['_REGISTERREQUEST']._serialized_end=73
  _globals['_REGISTERRESPONSE']._serialized_start=75
  _globals['_REGISTERRESPONSE']._serialized_end=127
  _globals['_LOGINREQUEST']._serialized_start=129
  _globals['_LOGINREQUEST']._serialized_end=179
  _globals['_LOGINRESPONSE']._serialized_start=181
  _globals['_LOGINRESPONSE']._serialized_end=230
  _globals['_AUTHSERVICE']._serialized_start=232
  _globals['_AUTHSERVICE']._serialized_end=358
# @@protoc_insertion_point(module_scope)
