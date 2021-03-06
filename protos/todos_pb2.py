# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/todos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/todos.proto',
  package='todos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12protos/todos.proto\x12\x05todos\x1a\x1fgoogle/protobuf/timestamp.proto\"|\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12,\n\x08\x64ue_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x08priority\x18\x04 \x01(\x0e\x32\x13.todos.TodoPriority\"#\n\x05Todos\x12\x1a\n\x05todos\x18\x01 \x03(\x0b\x32\x0b.todos.Todo*-\n\x0cTodoPriority\x12\x08\n\x04HIGH\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\x07\n\x03LOW\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_TODOPRIORITY = _descriptor.EnumDescriptor(
  name='TodoPriority',
  full_name='todos.TodoPriority',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=225,
  serialized_end=270,
)
_sym_db.RegisterEnumDescriptor(_TODOPRIORITY)

TodoPriority = enum_type_wrapper.EnumTypeWrapper(_TODOPRIORITY)
HIGH = 0
MEDIUM = 1
LOW = 2



_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='todos.Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todos.Todo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='todos.Todo.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='due_date', full_name='todos.Todo.due_date', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priority', full_name='todos.Todo.priority', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=186,
)


_TODOS = _descriptor.Descriptor(
  name='Todos',
  full_name='todos.Todos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='todos', full_name='todos.Todos.todos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=223,
)

_TODO.fields_by_name['due_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TODO.fields_by_name['priority'].enum_type = _TODOPRIORITY
_TODOS.fields_by_name['todos'].message_type = _TODO
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['Todos'] = _TODOS
DESCRIPTOR.enum_types_by_name['TodoPriority'] = _TODOPRIORITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), {
  'DESCRIPTOR' : _TODO,
  '__module__' : 'protos.todos_pb2'
  # @@protoc_insertion_point(class_scope:todos.Todo)
  })
_sym_db.RegisterMessage(Todo)

Todos = _reflection.GeneratedProtocolMessageType('Todos', (_message.Message,), {
  'DESCRIPTOR' : _TODOS,
  '__module__' : 'protos.todos_pb2'
  # @@protoc_insertion_point(class_scope:todos.Todos)
  })
_sym_db.RegisterMessage(Todos)


# @@protoc_insertion_point(module_scope)
