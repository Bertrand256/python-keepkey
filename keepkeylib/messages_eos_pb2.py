# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages-eos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12messages-eos.proto\"[\n\x0f\x45osGetPublicKey\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x14\n\x0cshow_display\x18\x02 \x01(\x08\x12\x1f\n\x04kind\x18\x03 \x01(\x0e\x32\x11.EosPublicKeyKind\">\n\x0c\x45osPublicKey\x12\x16\n\x0ewif_public_key\x18\x01 \x01(\t\x12\x16\n\x0eraw_public_key\x18\x02 \x01(\x0c\"c\n\tEosSignTx\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x10\n\x08\x63hain_id\x18\x02 \x01(\x0c\x12\x1c\n\x06header\x18\x03 \x01(\x0b\x32\x0c.EosTxHeader\x12\x13\n\x0bnum_actions\x18\x04 \x01(\r\"\x9c\x01\n\x0b\x45osTxHeader\x12\x12\n\nexpiration\x18\x01 \x02(\r\x12\x15\n\rref_block_num\x18\x02 \x02(\r\x12\x18\n\x10ref_block_prefix\x18\x03 \x02(\r\x12\x1b\n\x13max_net_usage_words\x18\x04 \x02(\r\x12\x18\n\x10max_cpu_usage_ms\x18\x05 \x02(\r\x12\x11\n\tdelay_sec\x18\x06 \x02(\r\"\x14\n\x12\x45osTxActionRequest\"\xe6\x04\n\x0e\x45osTxActionAck\x12 \n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x10.EosActionCommon\x12$\n\x08transfer\x18\x02 \x01(\x0b\x32\x12.EosActionTransfer\x12$\n\x08\x64\x65legate\x18\x03 \x01(\x0b\x32\x12.EosActionDelegate\x12(\n\nundelegate\x18\x04 \x01(\x0b\x32\x14.EosActionUndelegate\x12 \n\x06refund\x18\x05 \x01(\x0b\x32\x10.EosActionRefund\x12!\n\x07\x62uy_ram\x18\x06 \x01(\x0b\x32\x10.EosActionBuyRam\x12,\n\rbuy_ram_bytes\x18\x07 \x01(\x0b\x32\x15.EosActionBuyRamBytes\x12#\n\x08sell_ram\x18\x08 \x01(\x0b\x32\x11.EosActionSellRam\x12-\n\rvote_producer\x18\t \x01(\x0b\x32\x16.EosActionVoteProducer\x12)\n\x0bupdate_auth\x18\n \x01(\x0b\x32\x14.EosActionUpdateAuth\x12)\n\x0b\x64\x65lete_auth\x18\x0b \x01(\x0b\x32\x14.EosActionDeleteAuth\x12%\n\tlink_auth\x18\x0c \x01(\x0b\x32\x12.EosActionLinkAuth\x12)\n\x0bunlink_auth\x18\r \x01(\x0b\x32\x14.EosActionUnlinkAuth\x12)\n\x0bnew_account\x18\x0e \x01(\x0b\x32\x14.EosActionNewAccount\x12\"\n\x07unknown\x18\x0f \x01(\x0b\x32\x11.EosActionUnknown\"2\n\x08\x45osAsset\x12\x12\n\x06\x61mount\x18\x01 \x01(\x12\x42\x02\x30\x01\x12\x12\n\x06symbol\x18\x02 \x01(\x04\x42\x02\x30\x01\"?\n\x12\x45osPermissionLevel\x12\x11\n\x05\x61\x63tor\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x16\n\npermission\x18\x02 \x01(\x04\x42\x02\x30\x01\"S\n\x13\x45osAuthorizationKey\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0e\n\x06weight\x18\x03 \x01(\r\x12\x11\n\taddress_n\x18\x04 \x03(\r\"O\n\x17\x45osAuthorizationAccount\x12$\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x13.EosPermissionLevel\x12\x0e\n\x06weight\x18\x02 \x01(\r\"8\n\x14\x45osAuthorizationWait\x12\x10\n\x08wait_sec\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\r\"\x9b\x01\n\x10\x45osAuthorization\x12\x11\n\tthreshold\x18\x01 \x01(\r\x12\"\n\x04keys\x18\x02 \x03(\x0b\x32\x14.EosAuthorizationKey\x12*\n\x08\x61\x63\x63ounts\x18\x03 \x03(\x0b\x32\x18.EosAuthorizationAccount\x12$\n\x05waits\x18\x04 \x03(\x0b\x32\x15.EosAuthorizationWait\"d\n\x0f\x45osActionCommon\x12\x13\n\x07\x61\x63\x63ount\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x04name\x18\x02 \x01(\x04\x42\x02\x30\x01\x12*\n\rauthorization\x18\x03 \x03(\x0b\x32\x13.EosPermissionLevel\"h\n\x11\x45osActionTransfer\x12\x12\n\x06sender\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x14\n\x08receiver\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x1b\n\x08quantity\x18\x03 \x01(\x0b\x32\t.EosAsset\x12\x0c\n\x04memo\x18\x04 \x01(\t\"\x91\x01\n\x11\x45osActionDelegate\x12\x12\n\x06sender\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x14\n\x08receiver\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x1f\n\x0cnet_quantity\x18\x03 \x01(\x0b\x32\t.EosAsset\x12\x1f\n\x0c\x63pu_quantity\x18\x04 \x01(\x0b\x32\t.EosAsset\x12\x10\n\x08transfer\x18\x05 \x01(\x08\"\x81\x01\n\x13\x45osActionUndelegate\x12\x12\n\x06sender\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x14\n\x08receiver\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x1f\n\x0cnet_quantity\x18\x03 \x01(\x0b\x32\t.EosAsset\x12\x1f\n\x0c\x63pu_quantity\x18\x04 \x01(\x0b\x32\t.EosAsset\"$\n\x0f\x45osActionRefund\x12\x11\n\x05owner\x18\x01 \x01(\x04\x42\x02\x30\x01\"W\n\x0f\x45osActionBuyRam\x12\x11\n\x05payer\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x14\n\x08receiver\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x1b\n\x08quantity\x18\x03 \x01(\x0b\x32\t.EosAsset\"N\n\x14\x45osActionBuyRamBytes\x12\x11\n\x05payer\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x14\n\x08receiver\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\r\n\x05\x62ytes\x18\x03 \x01(\r\":\n\x10\x45osActionSellRam\x12\x13\n\x07\x61\x63\x63ount\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x11\n\x05\x62ytes\x18\x02 \x01(\x12\x42\x02\x30\x01\"T\n\x15\x45osActionVoteProducer\x12\x11\n\x05voter\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x11\n\x05proxy\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x15\n\tproducers\x18\x03 \x03(\x04\x42\x02\x30\x01\"w\n\x13\x45osActionUpdateAuth\x12\x13\n\x07\x61\x63\x63ount\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x16\n\npermission\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x12\n\x06parent\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\x1f\n\x04\x61uth\x18\x04 \x01(\x0b\x32\x11.EosAuthorization\"B\n\x13\x45osActionDeleteAuth\x12\x13\n\x07\x61\x63\x63ount\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x16\n\npermission\x18\x02 \x01(\x04\x42\x02\x30\x01\"e\n\x11\x45osActionLinkAuth\x12\x13\n\x07\x61\x63\x63ount\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x04\x63ode\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x04type\x18\x03 \x01(\x04\x42\x02\x30\x01\x12\x17\n\x0brequirement\x18\x04 \x01(\x04\x42\x02\x30\x01\"N\n\x13\x45osActionUnlinkAuth\x12\x13\n\x07\x61\x63\x63ount\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x04\x63ode\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x04type\x18\x03 \x01(\x04\x42\x02\x30\x01\"\x81\x01\n\x13\x45osActionNewAccount\x12\x13\n\x07\x63reator\x18\x01 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x04name\x18\x02 \x01(\x04\x42\x02\x30\x01\x12 \n\x05owner\x18\x03 \x01(\x0b\x32\x11.EosAuthorization\x12!\n\x06\x61\x63tive\x18\x04 \x01(\x0b\x32\x11.EosAuthorization\"9\n\x10\x45osActionUnknown\x12\x11\n\tdata_size\x18\x01 \x01(\r\x12\x12\n\ndata_chunk\x18\x02 \x01(\x0c\"Z\n\x0b\x45osSignedTx\x12\x13\n\x0bsignature_v\x18\x01 \x01(\r\x12\x13\n\x0bsignature_r\x18\x02 \x01(\x0c\x12\x13\n\x0bsignature_s\x18\x03 \x01(\x0c\x12\x0c\n\x04hash\x18\x04 \x01(\x0c*3\n\x10\x45osPublicKeyKind\x12\x07\n\x03\x45OS\x10\x00\x12\n\n\x06\x45OS_K1\x10\x01\x12\n\n\x06\x45OS_R1\x10\x02\x42\x38\n#com.shapeshift.keepkey.lib.protobufB\x11KeepKeyMessageEos')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_eos_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.shapeshift.keepkey.lib.protobufB\021KeepKeyMessageEos'
  _EOSASSET.fields_by_name['amount']._options = None
  _EOSASSET.fields_by_name['amount']._serialized_options = b'0\001'
  _EOSASSET.fields_by_name['symbol']._options = None
  _EOSASSET.fields_by_name['symbol']._serialized_options = b'0\001'
  _EOSPERMISSIONLEVEL.fields_by_name['actor']._options = None
  _EOSPERMISSIONLEVEL.fields_by_name['actor']._serialized_options = b'0\001'
  _EOSPERMISSIONLEVEL.fields_by_name['permission']._options = None
  _EOSPERMISSIONLEVEL.fields_by_name['permission']._serialized_options = b'0\001'
  _EOSACTIONCOMMON.fields_by_name['account']._options = None
  _EOSACTIONCOMMON.fields_by_name['account']._serialized_options = b'0\001'
  _EOSACTIONCOMMON.fields_by_name['name']._options = None
  _EOSACTIONCOMMON.fields_by_name['name']._serialized_options = b'0\001'
  _EOSACTIONTRANSFER.fields_by_name['sender']._options = None
  _EOSACTIONTRANSFER.fields_by_name['sender']._serialized_options = b'0\001'
  _EOSACTIONTRANSFER.fields_by_name['receiver']._options = None
  _EOSACTIONTRANSFER.fields_by_name['receiver']._serialized_options = b'0\001'
  _EOSACTIONDELEGATE.fields_by_name['sender']._options = None
  _EOSACTIONDELEGATE.fields_by_name['sender']._serialized_options = b'0\001'
  _EOSACTIONDELEGATE.fields_by_name['receiver']._options = None
  _EOSACTIONDELEGATE.fields_by_name['receiver']._serialized_options = b'0\001'
  _EOSACTIONUNDELEGATE.fields_by_name['sender']._options = None
  _EOSACTIONUNDELEGATE.fields_by_name['sender']._serialized_options = b'0\001'
  _EOSACTIONUNDELEGATE.fields_by_name['receiver']._options = None
  _EOSACTIONUNDELEGATE.fields_by_name['receiver']._serialized_options = b'0\001'
  _EOSACTIONREFUND.fields_by_name['owner']._options = None
  _EOSACTIONREFUND.fields_by_name['owner']._serialized_options = b'0\001'
  _EOSACTIONBUYRAM.fields_by_name['payer']._options = None
  _EOSACTIONBUYRAM.fields_by_name['payer']._serialized_options = b'0\001'
  _EOSACTIONBUYRAM.fields_by_name['receiver']._options = None
  _EOSACTIONBUYRAM.fields_by_name['receiver']._serialized_options = b'0\001'
  _EOSACTIONBUYRAMBYTES.fields_by_name['payer']._options = None
  _EOSACTIONBUYRAMBYTES.fields_by_name['payer']._serialized_options = b'0\001'
  _EOSACTIONBUYRAMBYTES.fields_by_name['receiver']._options = None
  _EOSACTIONBUYRAMBYTES.fields_by_name['receiver']._serialized_options = b'0\001'
  _EOSACTIONSELLRAM.fields_by_name['account']._options = None
  _EOSACTIONSELLRAM.fields_by_name['account']._serialized_options = b'0\001'
  _EOSACTIONSELLRAM.fields_by_name['bytes']._options = None
  _EOSACTIONSELLRAM.fields_by_name['bytes']._serialized_options = b'0\001'
  _EOSACTIONVOTEPRODUCER.fields_by_name['voter']._options = None
  _EOSACTIONVOTEPRODUCER.fields_by_name['voter']._serialized_options = b'0\001'
  _EOSACTIONVOTEPRODUCER.fields_by_name['proxy']._options = None
  _EOSACTIONVOTEPRODUCER.fields_by_name['proxy']._serialized_options = b'0\001'
  _EOSACTIONVOTEPRODUCER.fields_by_name['producers']._options = None
  _EOSACTIONVOTEPRODUCER.fields_by_name['producers']._serialized_options = b'0\001'
  _EOSACTIONUPDATEAUTH.fields_by_name['account']._options = None
  _EOSACTIONUPDATEAUTH.fields_by_name['account']._serialized_options = b'0\001'
  _EOSACTIONUPDATEAUTH.fields_by_name['permission']._options = None
  _EOSACTIONUPDATEAUTH.fields_by_name['permission']._serialized_options = b'0\001'
  _EOSACTIONUPDATEAUTH.fields_by_name['parent']._options = None
  _EOSACTIONUPDATEAUTH.fields_by_name['parent']._serialized_options = b'0\001'
  _EOSACTIONDELETEAUTH.fields_by_name['account']._options = None
  _EOSACTIONDELETEAUTH.fields_by_name['account']._serialized_options = b'0\001'
  _EOSACTIONDELETEAUTH.fields_by_name['permission']._options = None
  _EOSACTIONDELETEAUTH.fields_by_name['permission']._serialized_options = b'0\001'
  _EOSACTIONLINKAUTH.fields_by_name['account']._options = None
  _EOSACTIONLINKAUTH.fields_by_name['account']._serialized_options = b'0\001'
  _EOSACTIONLINKAUTH.fields_by_name['code']._options = None
  _EOSACTIONLINKAUTH.fields_by_name['code']._serialized_options = b'0\001'
  _EOSACTIONLINKAUTH.fields_by_name['type']._options = None
  _EOSACTIONLINKAUTH.fields_by_name['type']._serialized_options = b'0\001'
  _EOSACTIONLINKAUTH.fields_by_name['requirement']._options = None
  _EOSACTIONLINKAUTH.fields_by_name['requirement']._serialized_options = b'0\001'
  _EOSACTIONUNLINKAUTH.fields_by_name['account']._options = None
  _EOSACTIONUNLINKAUTH.fields_by_name['account']._serialized_options = b'0\001'
  _EOSACTIONUNLINKAUTH.fields_by_name['code']._options = None
  _EOSACTIONUNLINKAUTH.fields_by_name['code']._serialized_options = b'0\001'
  _EOSACTIONUNLINKAUTH.fields_by_name['type']._options = None
  _EOSACTIONUNLINKAUTH.fields_by_name['type']._serialized_options = b'0\001'
  _EOSACTIONNEWACCOUNT.fields_by_name['creator']._options = None
  _EOSACTIONNEWACCOUNT.fields_by_name['creator']._serialized_options = b'0\001'
  _EOSACTIONNEWACCOUNT.fields_by_name['name']._options = None
  _EOSACTIONNEWACCOUNT.fields_by_name['name']._serialized_options = b'0\001'
  _EOSPUBLICKEYKIND._serialized_start=3073
  _EOSPUBLICKEYKIND._serialized_end=3124
  _EOSGETPUBLICKEY._serialized_start=22
  _EOSGETPUBLICKEY._serialized_end=113
  _EOSPUBLICKEY._serialized_start=115
  _EOSPUBLICKEY._serialized_end=177
  _EOSSIGNTX._serialized_start=179
  _EOSSIGNTX._serialized_end=278
  _EOSTXHEADER._serialized_start=281
  _EOSTXHEADER._serialized_end=437
  _EOSTXACTIONREQUEST._serialized_start=439
  _EOSTXACTIONREQUEST._serialized_end=459
  _EOSTXACTIONACK._serialized_start=462
  _EOSTXACTIONACK._serialized_end=1076
  _EOSASSET._serialized_start=1078
  _EOSASSET._serialized_end=1128
  _EOSPERMISSIONLEVEL._serialized_start=1130
  _EOSPERMISSIONLEVEL._serialized_end=1193
  _EOSAUTHORIZATIONKEY._serialized_start=1195
  _EOSAUTHORIZATIONKEY._serialized_end=1278
  _EOSAUTHORIZATIONACCOUNT._serialized_start=1280
  _EOSAUTHORIZATIONACCOUNT._serialized_end=1359
  _EOSAUTHORIZATIONWAIT._serialized_start=1361
  _EOSAUTHORIZATIONWAIT._serialized_end=1417
  _EOSAUTHORIZATION._serialized_start=1420
  _EOSAUTHORIZATION._serialized_end=1575
  _EOSACTIONCOMMON._serialized_start=1577
  _EOSACTIONCOMMON._serialized_end=1677
  _EOSACTIONTRANSFER._serialized_start=1679
  _EOSACTIONTRANSFER._serialized_end=1783
  _EOSACTIONDELEGATE._serialized_start=1786
  _EOSACTIONDELEGATE._serialized_end=1931
  _EOSACTIONUNDELEGATE._serialized_start=1934
  _EOSACTIONUNDELEGATE._serialized_end=2063
  _EOSACTIONREFUND._serialized_start=2065
  _EOSACTIONREFUND._serialized_end=2101
  _EOSACTIONBUYRAM._serialized_start=2103
  _EOSACTIONBUYRAM._serialized_end=2190
  _EOSACTIONBUYRAMBYTES._serialized_start=2192
  _EOSACTIONBUYRAMBYTES._serialized_end=2270
  _EOSACTIONSELLRAM._serialized_start=2272
  _EOSACTIONSELLRAM._serialized_end=2330
  _EOSACTIONVOTEPRODUCER._serialized_start=2332
  _EOSACTIONVOTEPRODUCER._serialized_end=2416
  _EOSACTIONUPDATEAUTH._serialized_start=2418
  _EOSACTIONUPDATEAUTH._serialized_end=2537
  _EOSACTIONDELETEAUTH._serialized_start=2539
  _EOSACTIONDELETEAUTH._serialized_end=2605
  _EOSACTIONLINKAUTH._serialized_start=2607
  _EOSACTIONLINKAUTH._serialized_end=2708
  _EOSACTIONUNLINKAUTH._serialized_start=2710
  _EOSACTIONUNLINKAUTH._serialized_end=2788
  _EOSACTIONNEWACCOUNT._serialized_start=2791
  _EOSACTIONNEWACCOUNT._serialized_end=2920
  _EOSACTIONUNKNOWN._serialized_start=2922
  _EOSACTIONUNKNOWN._serialized_end=2979
  _EOSSIGNEDTX._serialized_start=2981
  _EOSSIGNEDTX._serialized_end=3071
# @@protoc_insertion_point(module_scope)
