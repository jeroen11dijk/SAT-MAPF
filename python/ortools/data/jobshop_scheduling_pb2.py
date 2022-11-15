# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/data/jobshop_scheduling.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ortools/data/jobshop_scheduling.proto',
  package='operations_research.data.jssp',
  syntax='proto3',
  serialized_options=b'\n\034com.google.ortools.data.jsspP\001\252\002\030Google.OrTools.Data.Jssp',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%ortools/data/jobshop_scheduling.proto\x12\x1doperations_research.data.jssp\x1a\x1egoogle/protobuf/wrappers.proto\"7\n\x04Task\x12\x0f\n\x07machine\x18\x01 \x03(\x05\x12\x10\n\x08\x64uration\x18\x02 \x03(\x03\x12\x0c\n\x04\x63ost\x18\x03 \x03(\x03\"\xa7\x02\n\x03Job\x12\x32\n\x05tasks\x18\x01 \x03(\x0b\x32#.operations_research.data.jssp.Task\x12\x33\n\x0e\x65\x61rliest_start\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x16\n\x0e\x65\x61rly_due_date\x18\x03 \x01(\x03\x12\x15\n\rlate_due_date\x18\x04 \x01(\x03\x12$\n\x1c\x65\x61rliness_cost_per_time_unit\x18\x05 \x01(\x03\x12#\n\x1blateness_cost_per_time_unit\x18\x06 \x01(\x03\x12/\n\nlatest_end\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x0c\n\x04name\x18\x10 \x01(\t\"/\n\x14TransitionTimeMatrix\x12\x17\n\x0ftransition_time\x18\x01 \x03(\x03\"l\n\x07Machine\x12S\n\x16transition_time_matrix\x18\x01 \x01(\x0b\x32\x33.operations_research.data.jssp.TransitionTimeMatrix\x12\x0c\n\x04name\x18\x10 \x01(\t\"U\n\rJobPrecedence\x12\x17\n\x0f\x66irst_job_index\x18\x01 \x01(\x05\x12\x18\n\x10second_job_index\x18\x02 \x01(\x05\x12\x11\n\tmin_delay\x18\x03 \x01(\x03\"\xb8\x02\n\x10JsspInputProblem\x12\x30\n\x04jobs\x18\x01 \x03(\x0b\x32\".operations_research.data.jssp.Job\x12\x38\n\x08machines\x18\x02 \x03(\x0b\x32&.operations_research.data.jssp.Machine\x12\x41\n\x0bprecedences\x18\x03 \x03(\x0b\x32,.operations_research.data.jssp.JobPrecedence\x12#\n\x1bmakespan_cost_per_time_unit\x18\x04 \x01(\x03\x12\x34\n\x0escaling_factor\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x0c\n\x04seed\x18\x18 \x01(\x05\x12\x0c\n\x04name\x18\x10 \x01(\t\"=\n\x0c\x41ssignedTask\x12\x19\n\x11\x61lternative_index\x18\x01 \x01(\x05\x12\x12\n\nstart_time\x18\x02 \x01(\x03\"{\n\x0b\x41ssignedJob\x12:\n\x05tasks\x18\x01 \x03(\x0b\x32+.operations_research.data.jssp.AssignedTask\x12\x15\n\rdue_date_cost\x18\x02 \x01(\x03\x12\x19\n\x11sum_of_task_costs\x18\x03 \x01(\x03\"y\n\x12JsspOutputSolution\x12\x38\n\x04jobs\x18\x01 \x03(\x0b\x32*.operations_research.data.jssp.AssignedJob\x12\x15\n\rmakespan_cost\x18\x02 \x01(\x03\x12\x12\n\ntotal_cost\x18\x03 \x01(\x03\x42;\n\x1c\x63om.google.ortools.data.jsspP\x01\xaa\x02\x18Google.OrTools.Data.Jsspb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='operations_research.data.jssp.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine', full_name='operations_research.data.jssp.Task.machine', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='operations_research.data.jssp.Task.duration', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost', full_name='operations_research.data.jssp.Task.cost', index=2,
      number=3, type=3, cpp_type=2, label=3,
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
  serialized_start=104,
  serialized_end=159,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='operations_research.data.jssp.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='operations_research.data.jssp.Job.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='earliest_start', full_name='operations_research.data.jssp.Job.earliest_start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='early_due_date', full_name='operations_research.data.jssp.Job.early_due_date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='late_due_date', full_name='operations_research.data.jssp.Job.late_due_date', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='earliness_cost_per_time_unit', full_name='operations_research.data.jssp.Job.earliness_cost_per_time_unit', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lateness_cost_per_time_unit', full_name='operations_research.data.jssp.Job.lateness_cost_per_time_unit', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_end', full_name='operations_research.data.jssp.Job.latest_end', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='operations_research.data.jssp.Job.name', index=7,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=162,
  serialized_end=457,
)


_TRANSITIONTIMEMATRIX = _descriptor.Descriptor(
  name='TransitionTimeMatrix',
  full_name='operations_research.data.jssp.TransitionTimeMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transition_time', full_name='operations_research.data.jssp.TransitionTimeMatrix.transition_time', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  serialized_start=459,
  serialized_end=506,
)


_MACHINE = _descriptor.Descriptor(
  name='Machine',
  full_name='operations_research.data.jssp.Machine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transition_time_matrix', full_name='operations_research.data.jssp.Machine.transition_time_matrix', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='operations_research.data.jssp.Machine.name', index=1,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=508,
  serialized_end=616,
)


_JOBPRECEDENCE = _descriptor.Descriptor(
  name='JobPrecedence',
  full_name='operations_research.data.jssp.JobPrecedence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_job_index', full_name='operations_research.data.jssp.JobPrecedence.first_job_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second_job_index', full_name='operations_research.data.jssp.JobPrecedence.second_job_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_delay', full_name='operations_research.data.jssp.JobPrecedence.min_delay', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=618,
  serialized_end=703,
)


_JSSPINPUTPROBLEM = _descriptor.Descriptor(
  name='JsspInputProblem',
  full_name='operations_research.data.jssp.JsspInputProblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='operations_research.data.jssp.JsspInputProblem.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='machines', full_name='operations_research.data.jssp.JsspInputProblem.machines', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='precedences', full_name='operations_research.data.jssp.JsspInputProblem.precedences', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='makespan_cost_per_time_unit', full_name='operations_research.data.jssp.JsspInputProblem.makespan_cost_per_time_unit', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scaling_factor', full_name='operations_research.data.jssp.JsspInputProblem.scaling_factor', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seed', full_name='operations_research.data.jssp.JsspInputProblem.seed', index=5,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='operations_research.data.jssp.JsspInputProblem.name', index=6,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=706,
  serialized_end=1018,
)


_ASSIGNEDTASK = _descriptor.Descriptor(
  name='AssignedTask',
  full_name='operations_research.data.jssp.AssignedTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alternative_index', full_name='operations_research.data.jssp.AssignedTask.alternative_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='operations_research.data.jssp.AssignedTask.start_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1020,
  serialized_end=1081,
)


_ASSIGNEDJOB = _descriptor.Descriptor(
  name='AssignedJob',
  full_name='operations_research.data.jssp.AssignedJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='operations_research.data.jssp.AssignedJob.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='due_date_cost', full_name='operations_research.data.jssp.AssignedJob.due_date_cost', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sum_of_task_costs', full_name='operations_research.data.jssp.AssignedJob.sum_of_task_costs', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=1083,
  serialized_end=1206,
)


_JSSPOUTPUTSOLUTION = _descriptor.Descriptor(
  name='JsspOutputSolution',
  full_name='operations_research.data.jssp.JsspOutputSolution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='operations_research.data.jssp.JsspOutputSolution.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='makespan_cost', full_name='operations_research.data.jssp.JsspOutputSolution.makespan_cost', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_cost', full_name='operations_research.data.jssp.JsspOutputSolution.total_cost', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=1208,
  serialized_end=1329,
)

_JOB.fields_by_name['tasks'].message_type = _TASK
_JOB.fields_by_name['earliest_start'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_JOB.fields_by_name['latest_end'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MACHINE.fields_by_name['transition_time_matrix'].message_type = _TRANSITIONTIMEMATRIX
_JSSPINPUTPROBLEM.fields_by_name['jobs'].message_type = _JOB
_JSSPINPUTPROBLEM.fields_by_name['machines'].message_type = _MACHINE
_JSSPINPUTPROBLEM.fields_by_name['precedences'].message_type = _JOBPRECEDENCE
_JSSPINPUTPROBLEM.fields_by_name['scaling_factor'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_ASSIGNEDJOB.fields_by_name['tasks'].message_type = _ASSIGNEDTASK
_JSSPOUTPUTSOLUTION.fields_by_name['jobs'].message_type = _ASSIGNEDJOB
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['TransitionTimeMatrix'] = _TRANSITIONTIMEMATRIX
DESCRIPTOR.message_types_by_name['Machine'] = _MACHINE
DESCRIPTOR.message_types_by_name['JobPrecedence'] = _JOBPRECEDENCE
DESCRIPTOR.message_types_by_name['JsspInputProblem'] = _JSSPINPUTPROBLEM
DESCRIPTOR.message_types_by_name['AssignedTask'] = _ASSIGNEDTASK
DESCRIPTOR.message_types_by_name['AssignedJob'] = _ASSIGNEDJOB
DESCRIPTOR.message_types_by_name['JsspOutputSolution'] = _JSSPOUTPUTSOLUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.Task)
  })
_sym_db.RegisterMessage(Task)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.Job)
  })
_sym_db.RegisterMessage(Job)

TransitionTimeMatrix = _reflection.GeneratedProtocolMessageType('TransitionTimeMatrix', (_message.Message,), {
  'DESCRIPTOR' : _TRANSITIONTIMEMATRIX,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.TransitionTimeMatrix)
  })
_sym_db.RegisterMessage(TransitionTimeMatrix)

Machine = _reflection.GeneratedProtocolMessageType('Machine', (_message.Message,), {
  'DESCRIPTOR' : _MACHINE,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.Machine)
  })
_sym_db.RegisterMessage(Machine)

JobPrecedence = _reflection.GeneratedProtocolMessageType('JobPrecedence', (_message.Message,), {
  'DESCRIPTOR' : _JOBPRECEDENCE,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.JobPrecedence)
  })
_sym_db.RegisterMessage(JobPrecedence)

JsspInputProblem = _reflection.GeneratedProtocolMessageType('JsspInputProblem', (_message.Message,), {
  'DESCRIPTOR' : _JSSPINPUTPROBLEM,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.JsspInputProblem)
  })
_sym_db.RegisterMessage(JsspInputProblem)

AssignedTask = _reflection.GeneratedProtocolMessageType('AssignedTask', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNEDTASK,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.AssignedTask)
  })
_sym_db.RegisterMessage(AssignedTask)

AssignedJob = _reflection.GeneratedProtocolMessageType('AssignedJob', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNEDJOB,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.AssignedJob)
  })
_sym_db.RegisterMessage(AssignedJob)

JsspOutputSolution = _reflection.GeneratedProtocolMessageType('JsspOutputSolution', (_message.Message,), {
  'DESCRIPTOR' : _JSSPOUTPUTSOLUTION,
  '__module__' : 'ortools.data.jobshop_scheduling_pb2'
  # @@protoc_insertion_point(class_scope:operations_research.data.jssp.JsspOutputSolution)
  })
_sym_db.RegisterMessage(JsspOutputSolution)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
