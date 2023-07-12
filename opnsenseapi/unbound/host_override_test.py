import json
import unittest

from opnsenseapi.ifaces.opnsense import _OpnSense
from opnsenseapi.unbound.host_override import HostOverride, Host


class HostOverrideTest(unittest.TestCase):
    def test_host_to_json(self):
        class MockValidator(_OpnSense):
            pass
        mocker = MockValidator
        ho = HostOverride(mocker)
        test = json.dumps({
            "host": {
                "enabled": "1",
                "hostname": "hostname",
                "domain": "domain",
                "rr": "A",
                "mxprio": "",
                "mx": "",
                "server": "10.10.10.10",
                "description": "descr"
            }
        }, indent=2)
        h = ho.create_host_from_json(test)

        self.assertEqual(True, True)  # add assertion here

    def test_json_to_host(self):
        class MockValidator(_OpnSense):
            pass
        mocker = MockValidator
        ho = HostOverride(mocker)
        test = Host(id="abc",
                    enabled=True,
                    hostname="hostname",
                    domain="domain",
                    rr="A",
                    server="10.10.10.10",
                    description="descr")
        expected = json.dumps({
            "host": {
                "enabled": "1",
                "hostname": "hostname",
                "domain": "domain",
                "rr": "A",
                "mxprio": "",
                "mx": "",
                "server": "10.10.10.10",
                "description": "descr"
            }
        })
        result = ho.create_json_from_host(test)
        self.assertEqual(sorted(json.loads(result)), sorted(json.loads(expected)))  # add assertion here


if __name__ == '__main__':
    unittest.main()