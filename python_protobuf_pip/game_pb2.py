# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='tutorial',
  serialized_pb=_b('\n\ngame.proto\x12\x08tutorial\"\xb3\x01\n\x04Game\x12\x15\n\rplayer_one_id\x18\x01 \x02(\x05\x12\x31\n\x14player_one_character\x18\x02 \x02(\x0e\x32\x13.tutorial.Character\x12\x15\n\rplayer_two_id\x18\x03 \x02(\x05\x12\x31\n\x14player_two_character\x18\x04 \x02(\x0e\x32\x13.tutorial.Character\x12\x17\n\x0fplayer_one_wins\x18\x05 \x02(\x08*\xa1\x01\n\tCharacter\x12\t\n\x05LUIGI\x10\x00\x12\t\n\x05MARIO\x10\x01\x12\x0f\n\x0b\x44ONKEY_KONG\x10\x02\x12\x08\n\x04LINK\x10\x03\x12\t\n\x05SAMUS\x10\x04\x12\x12\n\x0e\x43\x41PTAIN_FALCON\x10\x05\x12\x08\n\x04NESS\x10\x06\x12\t\n\x05YOSHI\x10\x07\x12\t\n\x05KIRBY\x10\x08\x12\x07\n\x03\x46OX\x10\t\x12\x0b\n\x07PIKACHU\x10\n\x12\x0e\n\nJIGGLYPUFF\x10\x0b')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CHARACTER = _descriptor.EnumDescriptor(
  name='Character',
  full_name='tutorial.Character',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LUIGI', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARIO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONKEY_KONG', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAMUS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAPTAIN_FALCON', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NESS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOSHI', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIRBY', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOX', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIKACHU', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JIGGLYPUFF', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=207,
  serialized_end=368,
)
_sym_db.RegisterEnumDescriptor(_CHARACTER)

Character = enum_type_wrapper.EnumTypeWrapper(_CHARACTER)
LUIGI = 0
MARIO = 1
DONKEY_KONG = 2
LINK = 3
SAMUS = 4
CAPTAIN_FALCON = 5
NESS = 6
YOSHI = 7
KIRBY = 8
FOX = 9
PIKACHU = 10
JIGGLYPUFF = 11



_GAME = _descriptor.Descriptor(
  name='Game',
  full_name='tutorial.Game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_one_id', full_name='tutorial.Game.player_one_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_one_character', full_name='tutorial.Game.player_one_character', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_two_id', full_name='tutorial.Game.player_two_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_two_character', full_name='tutorial.Game.player_two_character', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_one_wins', full_name='tutorial.Game.player_one_wins', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=204,
)

_GAME.fields_by_name['player_one_character'].enum_type = _CHARACTER
_GAME.fields_by_name['player_two_character'].enum_type = _CHARACTER
DESCRIPTOR.message_types_by_name['Game'] = _GAME
DESCRIPTOR.enum_types_by_name['Character'] = _CHARACTER

Game = _reflection.GeneratedProtocolMessageType('Game', (_message.Message,), dict(
  DESCRIPTOR = _GAME,
  __module__ = 'game_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Game)
  ))
_sym_db.RegisterMessage(Game)


# @@protoc_insertion_point(module_scope)
