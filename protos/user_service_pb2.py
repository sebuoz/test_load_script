# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protos.user_pb2 as user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x02pb\x1a\nuser.proto\"\x1a\n\x0cGetMeRequest\x12\n\n\x02Id\x18\x01 \x01(\t2<\n\x0bUserService\x12-\n\x05GetMe\x12\x10.pb.GetMeRequest\x1a\x10.pb.UserResponse\"\x00\x42\x14Z\x12\x63yrex/vacancies/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022cyrex/vacancies/pb'
  _globals['_GETMEREQUEST']._serialized_start=38
  _globals['_GETMEREQUEST']._serialized_end=64
  _globals['_USERSERVICE']._serialized_start=66
  _globals['_USERSERVICE']._serialized_end=126
# @@protoc_insertion_point(module_scope)
