# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='node.proto',
  package='iohk.chain.node',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nnode.proto\x12\x0fiohk.chain.node\"\x12\n\x10HandshakeRequest\"4\n\x11HandshakeResponse\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0e\n\x06\x62lock0\x18\x02 \x01(\x0c\"\x0c\n\nTipRequest\"#\n\x0bTipResponse\x12\x14\n\x0c\x62lock_header\x18\x01 \x01(\x0c\"\x17\n\x08\x42lockIds\x12\x0b\n\x03ids\x18\x01 \x03(\x0c\"\x1a\n\x0b\x46ragmentIds\x12\x0b\n\x03ids\x18\x01 \x03(\x0c\"\x1d\n\x0cPeersRequest\x12\r\n\x05limit\x18\x01 \x01(\r\"5\n\rPeersResponse\x12$\n\x05peers\x18\x01 \x03(\x0b\x32\x15.iohk.chain.node.Peer\"\\\n\x04Peer\x12%\n\x02v4\x18\x01 \x01(\x0b\x32\x17.iohk.chain.node.PeerV4H\x00\x12%\n\x02v6\x18\x02 \x01(\x0b\x32\x17.iohk.chain.node.PeerV6H\x00\x42\x06\n\x04peer\"\"\n\x06PeerV4\x12\n\n\x02ip\x18\x01 \x01(\x07\x12\x0c\n\x04port\x18\x02 \x01(\x07\"7\n\x06PeerV6\x12\x0f\n\x07ip_high\x18\x01 \x01(\x06\x12\x0e\n\x06ip_low\x18\x02 \x01(\x06\x12\x0c\n\x04port\x18\x03 \x01(\x07\".\n\x12PullHeadersRequest\x12\x0c\n\x04\x66rom\x18\x01 \x03(\x0c\x12\n\n\x02to\x18\x02 \x01(\x0c\"&\n\x16PullBlocksToTipRequest\x12\x0c\n\x04\x66rom\x18\x01 \x03(\x0c\"\x15\n\x13PushHeadersResponse\"\x16\n\x14UploadBlocksResponse\"\x18\n\x05\x42lock\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x19\n\x06Header\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x1b\n\x08\x46ragment\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x17\n\x06Gossip\x12\r\n\x05nodes\x18\x02 \x03(\x0c\"\xa7\x01\n\nBlockEvent\x12+\n\x08\x61nnounce\x18\x01 \x01(\x0b\x32\x17.iohk.chain.node.HeaderH\x00\x12,\n\x07solicit\x18\x02 \x01(\x0b\x32\x19.iohk.chain.node.BlockIdsH\x00\x12\x36\n\x07missing\x18\x03 \x01(\x0b\x32#.iohk.chain.node.PullHeadersRequestH\x00\x42\x06\n\x04item2\xfc\x07\n\x04Node\x12R\n\tHandshake\x12!.iohk.chain.node.HandshakeRequest\x1a\".iohk.chain.node.HandshakeResponse\x12@\n\x03Tip\x12\x1b.iohk.chain.node.TipRequest\x1a\x1c.iohk.chain.node.TipResponse\x12\x46\n\x05Peers\x12\x1d.iohk.chain.node.PeersRequest\x1a\x1e.iohk.chain.node.PeersResponse\x12\x45\n\tGetBlocks\x12\x19.iohk.chain.node.BlockIds\x1a\x16.iohk.chain.node.Block\"\x03\x90\x02\x01\x30\x01\x12G\n\nGetHeaders\x12\x19.iohk.chain.node.BlockIds\x1a\x17.iohk.chain.node.Header\"\x03\x90\x02\x01\x30\x01\x12N\n\x0cGetFragments\x12\x1c.iohk.chain.node.FragmentIds\x1a\x19.iohk.chain.node.Fragment\"\x03\x90\x02\x01\x30\x01\x12R\n\x0bPullHeaders\x12#.iohk.chain.node.PullHeadersRequest\x1a\x17.iohk.chain.node.Header\"\x03\x90\x02\x01\x30\x01\x12T\n\x0fPullBlocksToTip\x12\'.iohk.chain.node.PullBlocksToTipRequest\x1a\x16.iohk.chain.node.Block0\x01\x12N\n\x0bPushHeaders\x12\x17.iohk.chain.node.Header\x1a$.iohk.chain.node.PushHeadersResponse(\x01\x12O\n\x0cUploadBlocks\x12\x16.iohk.chain.node.Block\x1a%.iohk.chain.node.UploadBlocksResponse(\x01\x12M\n\x11\x42lockSubscription\x12\x17.iohk.chain.node.Header\x1a\x1b.iohk.chain.node.BlockEvent(\x01\x30\x01\x12P\n\x14\x46ragmentSubscription\x12\x19.iohk.chain.node.Fragment\x1a\x19.iohk.chain.node.Fragment(\x01\x30\x01\x12J\n\x12GossipSubscription\x12\x17.iohk.chain.node.Gossip\x1a\x17.iohk.chain.node.Gossip(\x01\x30\x01\x62\x06proto3'
)




_HANDSHAKEREQUEST = _descriptor.Descriptor(
  name='HandshakeRequest',
  full_name='iohk.chain.node.HandshakeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=31,
  serialized_end=49,
)


_HANDSHAKERESPONSE = _descriptor.Descriptor(
  name='HandshakeResponse',
  full_name='iohk.chain.node.HandshakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='iohk.chain.node.HandshakeResponse.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block0', full_name='iohk.chain.node.HandshakeResponse.block0', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=51,
  serialized_end=103,
)


_TIPREQUEST = _descriptor.Descriptor(
  name='TipRequest',
  full_name='iohk.chain.node.TipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=105,
  serialized_end=117,
)


_TIPRESPONSE = _descriptor.Descriptor(
  name='TipResponse',
  full_name='iohk.chain.node.TipResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_header', full_name='iohk.chain.node.TipResponse.block_header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=119,
  serialized_end=154,
)


_BLOCKIDS = _descriptor.Descriptor(
  name='BlockIds',
  full_name='iohk.chain.node.BlockIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='iohk.chain.node.BlockIds.ids', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=156,
  serialized_end=179,
)


_FRAGMENTIDS = _descriptor.Descriptor(
  name='FragmentIds',
  full_name='iohk.chain.node.FragmentIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='iohk.chain.node.FragmentIds.ids', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=181,
  serialized_end=207,
)


_PEERSREQUEST = _descriptor.Descriptor(
  name='PeersRequest',
  full_name='iohk.chain.node.PeersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='iohk.chain.node.PeersRequest.limit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=209,
  serialized_end=238,
)


_PEERSRESPONSE = _descriptor.Descriptor(
  name='PeersResponse',
  full_name='iohk.chain.node.PeersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='iohk.chain.node.PeersResponse.peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=240,
  serialized_end=293,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='iohk.chain.node.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v4', full_name='iohk.chain.node.Peer.v4', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v6', full_name='iohk.chain.node.Peer.v6', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='peer', full_name='iohk.chain.node.Peer.peer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=295,
  serialized_end=387,
)


_PEERV4 = _descriptor.Descriptor(
  name='PeerV4',
  full_name='iohk.chain.node.PeerV4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='iohk.chain.node.PeerV4.ip', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='iohk.chain.node.PeerV4.port', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=389,
  serialized_end=423,
)


_PEERV6 = _descriptor.Descriptor(
  name='PeerV6',
  full_name='iohk.chain.node.PeerV6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_high', full_name='iohk.chain.node.PeerV6.ip_high', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_low', full_name='iohk.chain.node.PeerV6.ip_low', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='iohk.chain.node.PeerV6.port', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=425,
  serialized_end=480,
)


_PULLHEADERSREQUEST = _descriptor.Descriptor(
  name='PullHeadersRequest',
  full_name='iohk.chain.node.PullHeadersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='iohk.chain.node.PullHeadersRequest.from', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='iohk.chain.node.PullHeadersRequest.to', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=482,
  serialized_end=528,
)


_PULLBLOCKSTOTIPREQUEST = _descriptor.Descriptor(
  name='PullBlocksToTipRequest',
  full_name='iohk.chain.node.PullBlocksToTipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='iohk.chain.node.PullBlocksToTipRequest.from', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=530,
  serialized_end=568,
)


_PUSHHEADERSRESPONSE = _descriptor.Descriptor(
  name='PushHeadersResponse',
  full_name='iohk.chain.node.PushHeadersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=570,
  serialized_end=591,
)


_UPLOADBLOCKSRESPONSE = _descriptor.Descriptor(
  name='UploadBlocksResponse',
  full_name='iohk.chain.node.UploadBlocksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=593,
  serialized_end=615,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='iohk.chain.node.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='iohk.chain.node.Block.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=617,
  serialized_end=641,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='iohk.chain.node.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='iohk.chain.node.Header.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=643,
  serialized_end=668,
)


_FRAGMENT = _descriptor.Descriptor(
  name='Fragment',
  full_name='iohk.chain.node.Fragment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='iohk.chain.node.Fragment.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=670,
  serialized_end=697,
)


_GOSSIP = _descriptor.Descriptor(
  name='Gossip',
  full_name='iohk.chain.node.Gossip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='iohk.chain.node.Gossip.nodes', index=0,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=699,
  serialized_end=722,
)


_BLOCKEVENT = _descriptor.Descriptor(
  name='BlockEvent',
  full_name='iohk.chain.node.BlockEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='announce', full_name='iohk.chain.node.BlockEvent.announce', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solicit', full_name='iohk.chain.node.BlockEvent.solicit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing', full_name='iohk.chain.node.BlockEvent.missing', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='item', full_name='iohk.chain.node.BlockEvent.item',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=725,
  serialized_end=892,
)

_PEERSRESPONSE.fields_by_name['peers'].message_type = _PEER
_PEER.fields_by_name['v4'].message_type = _PEERV4
_PEER.fields_by_name['v6'].message_type = _PEERV6
_PEER.oneofs_by_name['peer'].fields.append(
  _PEER.fields_by_name['v4'])
_PEER.fields_by_name['v4'].containing_oneof = _PEER.oneofs_by_name['peer']
_PEER.oneofs_by_name['peer'].fields.append(
  _PEER.fields_by_name['v6'])
_PEER.fields_by_name['v6'].containing_oneof = _PEER.oneofs_by_name['peer']
_BLOCKEVENT.fields_by_name['announce'].message_type = _HEADER
_BLOCKEVENT.fields_by_name['solicit'].message_type = _BLOCKIDS
_BLOCKEVENT.fields_by_name['missing'].message_type = _PULLHEADERSREQUEST
_BLOCKEVENT.oneofs_by_name['item'].fields.append(
  _BLOCKEVENT.fields_by_name['announce'])
_BLOCKEVENT.fields_by_name['announce'].containing_oneof = _BLOCKEVENT.oneofs_by_name['item']
_BLOCKEVENT.oneofs_by_name['item'].fields.append(
  _BLOCKEVENT.fields_by_name['solicit'])
_BLOCKEVENT.fields_by_name['solicit'].containing_oneof = _BLOCKEVENT.oneofs_by_name['item']
_BLOCKEVENT.oneofs_by_name['item'].fields.append(
  _BLOCKEVENT.fields_by_name['missing'])
_BLOCKEVENT.fields_by_name['missing'].containing_oneof = _BLOCKEVENT.oneofs_by_name['item']
DESCRIPTOR.message_types_by_name['HandshakeRequest'] = _HANDSHAKEREQUEST
DESCRIPTOR.message_types_by_name['HandshakeResponse'] = _HANDSHAKERESPONSE
DESCRIPTOR.message_types_by_name['TipRequest'] = _TIPREQUEST
DESCRIPTOR.message_types_by_name['TipResponse'] = _TIPRESPONSE
DESCRIPTOR.message_types_by_name['BlockIds'] = _BLOCKIDS
DESCRIPTOR.message_types_by_name['FragmentIds'] = _FRAGMENTIDS
DESCRIPTOR.message_types_by_name['PeersRequest'] = _PEERSREQUEST
DESCRIPTOR.message_types_by_name['PeersResponse'] = _PEERSRESPONSE
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
DESCRIPTOR.message_types_by_name['PeerV4'] = _PEERV4
DESCRIPTOR.message_types_by_name['PeerV6'] = _PEERV6
DESCRIPTOR.message_types_by_name['PullHeadersRequest'] = _PULLHEADERSREQUEST
DESCRIPTOR.message_types_by_name['PullBlocksToTipRequest'] = _PULLBLOCKSTOTIPREQUEST
DESCRIPTOR.message_types_by_name['PushHeadersResponse'] = _PUSHHEADERSRESPONSE
DESCRIPTOR.message_types_by_name['UploadBlocksResponse'] = _UPLOADBLOCKSRESPONSE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Fragment'] = _FRAGMENT
DESCRIPTOR.message_types_by_name['Gossip'] = _GOSSIP
DESCRIPTOR.message_types_by_name['BlockEvent'] = _BLOCKEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandshakeRequest = _reflection.GeneratedProtocolMessageType('HandshakeRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKEREQUEST,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.HandshakeRequest)
  })
_sym_db.RegisterMessage(HandshakeRequest)

HandshakeResponse = _reflection.GeneratedProtocolMessageType('HandshakeResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKERESPONSE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.HandshakeResponse)
  })
_sym_db.RegisterMessage(HandshakeResponse)

TipRequest = _reflection.GeneratedProtocolMessageType('TipRequest', (_message.Message,), {
  'DESCRIPTOR' : _TIPREQUEST,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.TipRequest)
  })
_sym_db.RegisterMessage(TipRequest)

TipResponse = _reflection.GeneratedProtocolMessageType('TipResponse', (_message.Message,), {
  'DESCRIPTOR' : _TIPRESPONSE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.TipResponse)
  })
_sym_db.RegisterMessage(TipResponse)

BlockIds = _reflection.GeneratedProtocolMessageType('BlockIds', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKIDS,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.BlockIds)
  })
_sym_db.RegisterMessage(BlockIds)

FragmentIds = _reflection.GeneratedProtocolMessageType('FragmentIds', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENTIDS,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.FragmentIds)
  })
_sym_db.RegisterMessage(FragmentIds)

PeersRequest = _reflection.GeneratedProtocolMessageType('PeersRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEERSREQUEST,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PeersRequest)
  })
_sym_db.RegisterMessage(PeersRequest)

PeersResponse = _reflection.GeneratedProtocolMessageType('PeersResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERSRESPONSE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PeersResponse)
  })
_sym_db.RegisterMessage(PeersResponse)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {
  'DESCRIPTOR' : _PEER,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.Peer)
  })
_sym_db.RegisterMessage(Peer)

PeerV4 = _reflection.GeneratedProtocolMessageType('PeerV4', (_message.Message,), {
  'DESCRIPTOR' : _PEERV4,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PeerV4)
  })
_sym_db.RegisterMessage(PeerV4)

PeerV6 = _reflection.GeneratedProtocolMessageType('PeerV6', (_message.Message,), {
  'DESCRIPTOR' : _PEERV6,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PeerV6)
  })
_sym_db.RegisterMessage(PeerV6)

PullHeadersRequest = _reflection.GeneratedProtocolMessageType('PullHeadersRequest', (_message.Message,), {
  'DESCRIPTOR' : _PULLHEADERSREQUEST,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PullHeadersRequest)
  })
_sym_db.RegisterMessage(PullHeadersRequest)

PullBlocksToTipRequest = _reflection.GeneratedProtocolMessageType('PullBlocksToTipRequest', (_message.Message,), {
  'DESCRIPTOR' : _PULLBLOCKSTOTIPREQUEST,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PullBlocksToTipRequest)
  })
_sym_db.RegisterMessage(PullBlocksToTipRequest)

PushHeadersResponse = _reflection.GeneratedProtocolMessageType('PushHeadersResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUSHHEADERSRESPONSE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.PushHeadersResponse)
  })
_sym_db.RegisterMessage(PushHeadersResponse)

UploadBlocksResponse = _reflection.GeneratedProtocolMessageType('UploadBlocksResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADBLOCKSRESPONSE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.UploadBlocksResponse)
  })
_sym_db.RegisterMessage(UploadBlocksResponse)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.Block)
  })
_sym_db.RegisterMessage(Block)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.Header)
  })
_sym_db.RegisterMessage(Header)

Fragment = _reflection.GeneratedProtocolMessageType('Fragment', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENT,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.Fragment)
  })
_sym_db.RegisterMessage(Fragment)

Gossip = _reflection.GeneratedProtocolMessageType('Gossip', (_message.Message,), {
  'DESCRIPTOR' : _GOSSIP,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.Gossip)
  })
_sym_db.RegisterMessage(Gossip)

BlockEvent = _reflection.GeneratedProtocolMessageType('BlockEvent', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKEVENT,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:iohk.chain.node.BlockEvent)
  })
_sym_db.RegisterMessage(BlockEvent)



_NODE = _descriptor.ServiceDescriptor(
  name='Node',
  full_name='iohk.chain.node.Node',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=895,
  serialized_end=1915,
  methods=[
  _descriptor.MethodDescriptor(
    name='Handshake',
    full_name='iohk.chain.node.Node.Handshake',
    index=0,
    containing_service=None,
    input_type=_HANDSHAKEREQUEST,
    output_type=_HANDSHAKERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Tip',
    full_name='iohk.chain.node.Node.Tip',
    index=1,
    containing_service=None,
    input_type=_TIPREQUEST,
    output_type=_TIPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Peers',
    full_name='iohk.chain.node.Node.Peers',
    index=2,
    containing_service=None,
    input_type=_PEERSREQUEST,
    output_type=_PEERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlocks',
    full_name='iohk.chain.node.Node.GetBlocks',
    index=3,
    containing_service=None,
    input_type=_BLOCKIDS,
    output_type=_BLOCK,
    serialized_options=b'\220\002\001',
  ),
  _descriptor.MethodDescriptor(
    name='GetHeaders',
    full_name='iohk.chain.node.Node.GetHeaders',
    index=4,
    containing_service=None,
    input_type=_BLOCKIDS,
    output_type=_HEADER,
    serialized_options=b'\220\002\001',
  ),
  _descriptor.MethodDescriptor(
    name='GetFragments',
    full_name='iohk.chain.node.Node.GetFragments',
    index=5,
    containing_service=None,
    input_type=_FRAGMENTIDS,
    output_type=_FRAGMENT,
    serialized_options=b'\220\002\001',
  ),
  _descriptor.MethodDescriptor(
    name='PullHeaders',
    full_name='iohk.chain.node.Node.PullHeaders',
    index=6,
    containing_service=None,
    input_type=_PULLHEADERSREQUEST,
    output_type=_HEADER,
    serialized_options=b'\220\002\001',
  ),
  _descriptor.MethodDescriptor(
    name='PullBlocksToTip',
    full_name='iohk.chain.node.Node.PullBlocksToTip',
    index=7,
    containing_service=None,
    input_type=_PULLBLOCKSTOTIPREQUEST,
    output_type=_BLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PushHeaders',
    full_name='iohk.chain.node.Node.PushHeaders',
    index=8,
    containing_service=None,
    input_type=_HEADER,
    output_type=_PUSHHEADERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadBlocks',
    full_name='iohk.chain.node.Node.UploadBlocks',
    index=9,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_UPLOADBLOCKSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BlockSubscription',
    full_name='iohk.chain.node.Node.BlockSubscription',
    index=10,
    containing_service=None,
    input_type=_HEADER,
    output_type=_BLOCKEVENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FragmentSubscription',
    full_name='iohk.chain.node.Node.FragmentSubscription',
    index=11,
    containing_service=None,
    input_type=_FRAGMENT,
    output_type=_FRAGMENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GossipSubscription',
    full_name='iohk.chain.node.Node.GossipSubscription',
    index=12,
    containing_service=None,
    input_type=_GOSSIP,
    output_type=_GOSSIP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NODE)

DESCRIPTOR.services_by_name['Node'] = _NODE

# @@protoc_insertion_point(module_scope)
