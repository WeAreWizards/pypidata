# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raw_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='raw_data.proto',
  package='',
  serialized_pb='\n\x0eraw_data.proto\"d\n\x07RawData\x12\x1b\n\x13retrieved_timestamp\x18\x01 \x01(\x04\x12\x10\n\x08url_used\x18\x02 \x01(\x0c\x12\x14\n\x0cpackage_name\x18\x03 \x01(\x0c\x12\x14\n\x0cpackage_json\x18\x04 \x01(\x0c')




_RAWDATA = _descriptor.Descriptor(
  name='RawData',
  full_name='RawData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retrieved_timestamp', full_name='RawData.retrieved_timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url_used', full_name='RawData.url_used', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='package_name', full_name='RawData.package_name', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='package_json', full_name='RawData.package_json', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=18,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['RawData'] = _RAWDATA

class RawData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RAWDATA

  # @@protoc_insertion_point(class_scope:RawData)


# @@protoc_insertion_point(module_scope)