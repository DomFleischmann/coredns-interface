#!/usr/bin/python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class CoreDNSProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:coredns}-relation-joined')
    def joined(self):
        self.set_state('{relation_name}.joined')

    @hook('{provides:coredns}-relation-changed')
    def changed(self):
        self.set_state('{relation_name}.ready')

    @hook('{provides:coredns}-relation-{broken,departed}')
    def broken_departed(self):
        self.remove_state('{relation_name}.ready')
        self.remove_state('{relation_name}.joined')

    @hook('{provides:coredns}-relation-broken')
    def broken(self):
        self.set_state('{relation_name}.removed')

    def send_ip(self, host):
        conv = self.conversation()
        conv.set_remote('host', host)

