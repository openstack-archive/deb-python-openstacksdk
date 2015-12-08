# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.tests.functional import base


class TestCapability(base.BaseFunctionalTest):

    def test_list(self):
        ids = [o.id for o in self.conn.telemetry.capabilities()]
        self.assertIn('resources:query:simple', ids)
        self.assertIn('events:query:simple', ids)
        self.assertIn('meters:query:simple', ids)
        self.assertIn('statistics:query:simple', ids)
        self.assertIn('alarms:query:simple', ids)
        self.assertIn('samples:query:simple', ids)
