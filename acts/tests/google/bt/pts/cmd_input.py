#/usr/bin/env python3.4
#
# Copyright (C) 2016 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""
Python script for wrappers to various libraries.
"""

from gattc_lib import GattClientLib

import cmd
"""Various Global Strings"""
CMD_LOG = "CMD {} result: {}"
FAILURE = "CMD {} threw exception: {}"


class CmdInput(cmd.Cmd):
    """Simple command processor for Bluetooth PTS Testing"""
    gattc_lib = None

    def setup_vars(self, android_devices, mac_addr, log):
        self.pri_dut = android_devices[0]
        if len(android_devices) > 1:
            self.sec_dut = android_devices[1]
            self.ter_dut = android_devices[2]
        self.mac_addr = mac_addr
        self.log = log

        # Initialize libraries
        self.gattc_lib = GattClientLib(log, mac_addr, self.pri_dut)

    def emptyline(self):
        pass

    def do_EOF(self, line):
        "End Script"
        return True

    """Begin GATT Client wrappers"""

    def do_gattc_connect_over_le(self, line):
        """Perform GATT connection over LE"""
        cmd = "Gatt connect over LE"
        try:
            autoconnect = False
            if line:
                autoconnect = bool(line)
            self.gattc_lib.connect_over_le(autoconnect)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_connect_over_bredr(self, line):
        """Perform GATT connection over BREDR"""
        cmd = "Gatt connect over BR/EDR"
        try:
            self.gattc_lib.connect_over_bredr()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_disconnect(self, line):
        """Perform GATT disconnect"""
        cmd = "Gatt Disconnect"
        try:
            self.gattc_lib.disconnect()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_char_by_uuid(self, line):
        """GATT client read Characteristic by UUID."""
        cmd = "GATT client read Characteristic by UUID."
        try:
            self.gattc_lib.read_char_by_uuid(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_request_mtu(self, line):
        """Request MTU Change of input value"""
        cmd = "Request MTU Value"
        try:
            self.gattc_lib.request_mtu(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_list_all_uuids(self, line):
        """From the GATT Client, discover services and list all services,
        chars and descriptors
        """
        cmd = "Discovery Services and list all UUIDS"
        try:
            self.gattc_lib.list_all_uuids()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_discover_services(self, line):
        """GATT Client discover services of GATT Server"""
        cmd = "Discovery Services of GATT Server"
        try:
            self.gattc_lib.discover_services()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_refresh(self, line):
        """Perform Gatt Client Refresh"""
        cmd = "GATT Client Refresh"
        try:
            self.gattc_lib.refresh()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_char_by_instance_id(self, line):
        """From the GATT Client, discover services and list all services,
        chars and descriptors
        """
        cmd = "GATT Client Read By Instance ID"
        try:
            self.gattc_lib.read_char_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_char_by_instance_id(self, line):
        """GATT Client Write to Characteristic by instance ID"""
        cmd = "GATT Client write to Characteristic by instance ID"
        try:
            self.gattc_lib.write_char_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_mod_write_char_by_instance_id(self, line):
        """GATT Client Write to Char that doesn't have write permission"""
        cmd = "GATT Client Write to Char that doesn't have write permission"
        try:
            self.gattc_lib.mod_write_char_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_invalid_char_by_instance_id(self, line):
        """GATT Client Write to Char that doesn't exists"""
        try:
            self.gattc_lib.write_invalid_char_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_mod_read_char_by_instance_id(self, line):
        """GATT Client Read Char that doesn't have write permission"""
        cmd = "GATT Client Read Char that doesn't have write permission"
        try:
            self.gattc_lib.mod_read_char_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_invalid_char_by_instance_id(self, line):
        """GATT Client Read Char that doesn't exists"""
        cmd = "GATT Client Read Char that doesn't exists"
        try:
            self.gattc_lib.read_invalid_char_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_mod_write_desc_by_instance_id(self, line):
        """GATT Client Write to Desc that doesn't have write permission"""
        cmd = "GATT Client Write to Desc that doesn't have write permission"
        try:
            self.gattc_lib.mod_write_desc_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_invalid_desc_by_instance_id(self, line):
        """GATT Client Write to Desc that doesn't exists"""
        cmd = "GATT Client Write to Desc that doesn't exists"
        try:
            self.gattc_lib.write_invalid_desc_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_mod_read_desc_by_instance_id(self, line):
        """GATT Client Read Desc that doesn't have write permission"""
        cmd = "GATT Client Read Desc that doesn't have write permission"
        try:
            self.gattc_lib.mod_read_desc_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_invalid_desc_by_instance_id(self, line):
        """GATT Client Read Desc that doesn't exists"""
        cmd = "GATT Client Read Desc that doesn't exists"
        try:
            self.gattc_lib.read_invalid_desc_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_mod_read_char_by_uuid_and_instance_id(self, line):
        """GATT Client Read Char that doesn't have write permission"""
        cmd = "GATT Client Read Char that doesn't have write permission"
        try:
            self.gattc_lib.mod_read_char_by_uuid_and_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_invalid_char_by_uuid(self, line):
        """GATT Client Read Char that doesn't exist"""
        cmd = "GATT Client Read Char that doesn't exist"
        try:
            self.gattc_lib.read_invalid_char_by_uuid(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_desc_by_instance_id(self, line):
        """GATT Client Write to Descriptor by instance ID"""
        cmd = "GATT Client Write to Descriptor by instance ID"
        try:
            self.gattc_lib.write_desc_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_enable_notification_desc_by_instance_id(self, line):
        """GATT Client Enable Notification on Descriptor by instance ID"""
        cmd = "GATT Client Enable Notification on Descriptor by instance ID"
        try:
            self.gattc_lib.enable_notification_desc_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_char_enable_all_notifications(self, line):
        """GATT Client enable all notifications"""
        cmd = "GATT Client enable all notifications"
        try:
            self.gattc_lib.char_enable_all_notifications()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_char_by_invalid_instance_id(self, line):
        """GATT Client read char by non-existant instance id"""
        cmd = "GATT Client read char by non-existant instance id"
        try:
            self.gattc_lib.read_char_by_invalid_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_begin_reliable_write(self, line):
        """Begin a reliable write on the Bluetooth Gatt Client"""
        cmd = "GATT Client Begin Reliable Write"
        try:
            self.gattc_lib.begin_reliable_write()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_abort_reliable_write(self, line):
        """Abort a reliable write on the Bluetooth Gatt Client"""
        cmd = "GATT Client Abort Reliable Write"
        try:
            self.gattc_lib.abort_reliable_write()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_execute_reliable_write(self, line):
        """Execute a reliable write on the Bluetooth Gatt Client"""
        cmd = "GATT Client Execute Reliable Write"
        try:
            self.gattc_lib.execute_reliable_write()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_read_all_char(self, line):
        """GATT Client read all Characteristic values"""
        cmd = "GATT Client read all Characteristic values"
        try:
            self.gattc_lib.read_all_char()
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_all_char(self, line):
        """Write to every Characteristic on the GATT server"""
        cmd = "GATT Client Write All Characteristics"
        try:
            self.gattc_lib.write_all_char(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_all_desc(self, line):
        """ Write to every Descriptor on the GATT server """
        cmd = "GATT Client Write All Descriptors"
        try:
            self.gattc_lib.write_all_desc(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_write_desc_notification_by_instance_id(self, line):
        """Write 0x00 or 0x02 to notification descriptor [instance_id]"""
        cmd = "Write 0x00 0x02 to notification descriptor"
        try:
            self.gattc_lib.write_desc_notification_by_instance_id(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    def do_gattc_discover_service_by_uuid(self, line):
        """Discover service by uuid"""
        cmd = "Discover service by uuid"
        try:
            self.gattc_lib.discover_service_by_uuid(line)
        except Exception as err:
            self.log.info(FAILURE.format(cmd, err))

    """End GATT Client wrappers"""
