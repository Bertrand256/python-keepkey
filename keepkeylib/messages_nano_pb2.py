# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages-nano.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13messages-nano.proto\"R\n\x0eNanoGetAddress\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x17\n\tcoin_name\x18\x02 \x01(\t:\x04Nano\x12\x14\n\x0cshow_display\x18\x03 \x01(\x08\"\x1e\n\x0bNanoAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\xb6\x02\n\nNanoSignTx\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x17\n\tcoin_name\x18\x02 \x01(\t:\x04Nano\x12-\n\x0cparent_block\x18\x03 \x01(\x0b\x32\x17.NanoSignTx.ParentBlock\x12\x11\n\tlink_hash\x18\x04 \x01(\x0c\x12\x16\n\x0elink_recipient\x18\x05 \x01(\t\x12\x18\n\x10link_recipient_n\x18\x06 \x03(\r\x12\x16\n\x0erepresentative\x18\x07 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x08 \x01(\x0c\x1aY\n\x0bParentBlock\x12\x13\n\x0bparent_hash\x18\x01 \x01(\x0c\x12\x0c\n\x04link\x18\x02 \x01(\x0c\x12\x16\n\x0erepresentative\x18\x04 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x05 \x01(\x0cJ\x04\x08\t\x10\n\"5\n\x0cNanoSignedTx\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x12\n\nblock_hash\x18\x02 \x01(\x0c\x42\x30\n\x1a\x63om.keepkey.deviceprotocolB\x12KeepKeyMessageNano')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_nano_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.keepkey.deviceprotocolB\022KeepKeyMessageNano'
  _NANOGETADDRESS._serialized_start=23
  _NANOGETADDRESS._serialized_end=105
  _NANOADDRESS._serialized_start=107
  _NANOADDRESS._serialized_end=137
  _NANOSIGNTX._serialized_start=140
  _NANOSIGNTX._serialized_end=450
  _NANOSIGNTX_PARENTBLOCK._serialized_start=355
  _NANOSIGNTX_PARENTBLOCK._serialized_end=444
  _NANOSIGNEDTX._serialized_start=452
  _NANOSIGNEDTX._serialized_end=505
# @@protoc_insertion_point(module_scope)
