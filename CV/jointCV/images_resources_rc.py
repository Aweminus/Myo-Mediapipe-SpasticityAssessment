# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xb3\
\x00\
\x00\x09\x27\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\xbf\xc0\xc0\xc0\x92\xca\xc1\x0c\
\x14\xb9\xc6\xb9\x46\x00\x48\x31\x16\x07\xb9\x3b\x31\xac\x3b\x27\
\xf3\x12\xc8\x61\x49\x77\xf4\x75\x64\x60\xd8\xd8\xcf\xfd\x27\x91\
\x15\xc8\x67\x0b\xf0\x09\x71\x55\x53\x53\x03\x32\xf7\x7b\x95\x2e\
\x02\x52\x4c\x25\x41\x7e\xc1\xff\x19\x9e\x6e\x37\xf0\x02\xf2\x38\
\x0b\x3c\x22\x8b\x19\x18\xc4\x05\x41\x98\xf1\x94\xda\x67\x7b\x06\
\x06\x8e\x39\x9e\x2e\x8e\x21\x15\x71\x6f\x0f\x1a\x32\x02\x95\x1c\
\x5a\xf0\xd5\x3f\x97\xd3\x5f\x81\x61\x14\x8c\x82\x51\x30\x0a\x46\
\xc1\x28\x18\x05\xa3\x60\x20\x40\x5c\x56\x74\x31\x03\xa3\x48\xf8\
\x31\x50\x63\x87\xc1\xd3\xd5\xcf\x65\x9d\x53\x42\x13\x00\x8c\xb8\
\x28\x70\
"

qt_resource_name = b"\
\x00\x14\
\x04\x85\xaa\x27\
\x00\x6c\
\x00\x6f\x00\x67\x00\x69\x00\x6e\x00\x5f\x00\x62\x00\x61\x00\x63\x00\x6b\x00\x67\x00\x72\x00\x6f\x00\x75\x00\x6e\x00\x64\x00\x2e\
\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x7a\x69\x35\x47\x78\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()