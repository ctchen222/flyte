# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/event/cloudevents.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.event import event_pb2 as flyteidl_dot_event_dot_event__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2
from flyteidl.core import interface_pb2 as flyteidl_dot_core_dot_interface__pb2
from flyteidl.core import artifact_id_pb2 as flyteidl_dot_core_dot_artifact__id__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n flyteidl/event/cloudevents.proto\x12\x0e\x66lyteidl.event\x1a\x1a\x66lyteidl/event/event.proto\x1a\x1c\x66lyteidl/core/literals.proto\x1a\x1d\x66lyteidl/core/interface.proto\x1a\x1f\x66lyteidl/core/artifact_id.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb2\x04\n\x1b\x43loudEventWorkflowExecution\x12\x43\n\traw_event\x18\x01 \x01(\x0b\x32&.flyteidl.event.WorkflowExecutionEventR\x08rawEvent\x12H\n\x10output_interface\x18\x02 \x01(\x0b\x32\x1d.flyteidl.core.TypedInterfaceR\x0foutputInterface\x12<\n\x0c\x61rtifact_ids\x18\x03 \x03(\x0b\x32\x19.flyteidl.core.ArtifactIDR\x0b\x61rtifactIds\x12[\n\x13reference_execution\x18\x04 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifierR\x12referenceExecution\x12\x1c\n\tprincipal\x18\x05 \x01(\tR\tprincipal\x12?\n\x0elaunch_plan_id\x18\x06 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\x0claunchPlanId\x12O\n\x06labels\x18\x07 \x03(\x0b\x32\x37.flyteidl.event.CloudEventWorkflowExecution.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x93\x04\n\x17\x43loudEventNodeExecution\x12?\n\traw_event\x18\x01 \x01(\x0b\x32\".flyteidl.event.NodeExecutionEventR\x08rawEvent\x12H\n\x0ctask_exec_id\x18\x02 \x01(\x0b\x32&.flyteidl.core.TaskExecutionIdentifierR\ntaskExecId\x12H\n\x10output_interface\x18\x03 \x01(\x0b\x32\x1d.flyteidl.core.TypedInterfaceR\x0foutputInterface\x12<\n\x0c\x61rtifact_ids\x18\x04 \x03(\x0b\x32\x19.flyteidl.core.ArtifactIDR\x0b\x61rtifactIds\x12\x1c\n\tprincipal\x18\x05 \x01(\tR\tprincipal\x12?\n\x0elaunch_plan_id\x18\x06 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\x0claunchPlanId\x12K\n\x06labels\x18\x07 \x03(\x0b\x32\x33.flyteidl.event.CloudEventNodeExecution.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xe2\x01\n\x17\x43loudEventTaskExecution\x12?\n\traw_event\x18\x01 \x01(\x0b\x32\".flyteidl.event.TaskExecutionEventR\x08rawEvent\x12K\n\x06labels\x18\x02 \x03(\x0b\x32\x33.flyteidl.event.CloudEventTaskExecution.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xef\x02\n\x18\x43loudEventExecutionStart\x12M\n\x0c\x65xecution_id\x18\x01 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifierR\x0b\x65xecutionId\x12?\n\x0elaunch_plan_id\x18\x02 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\x0claunchPlanId\x12:\n\x0bworkflow_id\x18\x03 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\nworkflowId\x12<\n\x0c\x61rtifact_ids\x18\x04 \x03(\x0b\x32\x19.flyteidl.core.ArtifactIDR\x0b\x61rtifactIds\x12+\n\x11\x61rtifact_trackers\x18\x05 \x03(\tR\x10\x61rtifactTrackers\x12\x1c\n\tprincipal\x18\x06 \x01(\tR\tprincipalB\xbc\x01\n\x12\x63om.flyteidl.eventB\x10\x43loudeventsProtoP\x01Z;github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/event\xa2\x02\x03\x46\x45X\xaa\x02\x0e\x46lyteidl.Event\xca\x02\x0e\x46lyteidl\\Event\xe2\x02\x1a\x46lyteidl\\Event\\GPBMetadata\xea\x02\x0f\x46lyteidl::Eventb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.event.cloudevents_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.flyteidl.eventB\020CloudeventsProtoP\001Z;github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/event\242\002\003FEX\252\002\016Flyteidl.Event\312\002\016Flyteidl\\Event\342\002\032Flyteidl\\Event\\GPBMetadata\352\002\017Flyteidl::Event'
  _CLOUDEVENTWORKFLOWEXECUTION_LABELSENTRY._options = None
  _CLOUDEVENTWORKFLOWEXECUTION_LABELSENTRY._serialized_options = b'8\001'
  _CLOUDEVENTNODEEXECUTION_LABELSENTRY._options = None
  _CLOUDEVENTNODEEXECUTION_LABELSENTRY._serialized_options = b'8\001'
  _CLOUDEVENTTASKEXECUTION_LABELSENTRY._options = None
  _CLOUDEVENTTASKEXECUTION_LABELSENTRY._serialized_options = b'8\001'
  _globals['_CLOUDEVENTWORKFLOWEXECUTION']._serialized_start=240
  _globals['_CLOUDEVENTWORKFLOWEXECUTION']._serialized_end=802
  _globals['_CLOUDEVENTWORKFLOWEXECUTION_LABELSENTRY']._serialized_start=745
  _globals['_CLOUDEVENTWORKFLOWEXECUTION_LABELSENTRY']._serialized_end=802
  _globals['_CLOUDEVENTNODEEXECUTION']._serialized_start=805
  _globals['_CLOUDEVENTNODEEXECUTION']._serialized_end=1336
  _globals['_CLOUDEVENTNODEEXECUTION_LABELSENTRY']._serialized_start=745
  _globals['_CLOUDEVENTNODEEXECUTION_LABELSENTRY']._serialized_end=802
  _globals['_CLOUDEVENTTASKEXECUTION']._serialized_start=1339
  _globals['_CLOUDEVENTTASKEXECUTION']._serialized_end=1565
  _globals['_CLOUDEVENTTASKEXECUTION_LABELSENTRY']._serialized_start=745
  _globals['_CLOUDEVENTTASKEXECUTION_LABELSENTRY']._serialized_end=802
  _globals['_CLOUDEVENTEXECUTIONSTART']._serialized_start=1568
  _globals['_CLOUDEVENTEXECUTIONSTART']._serialized_end=1935
# @@protoc_insertion_point(module_scope)
