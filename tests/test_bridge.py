import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'quilt-quantum-audio'))
import unittest

from quilt_quantum_canary_bridge import bridge_canary, try_normalize, try_partial_hash


class TestBridge(unittest.TestCase):

    def test_normalize(self):
        h = try_normalize("QPAM")
        self.assertIsInstance(h, int)

    def test_partial(self):
        h = try_partial_hash("QPAM", 4)
        self.assertIsInstance(h, int)

    def test_all_schemes(self):
        result = bridge_canary()
        self.assertIn("QPAM", result["bridges"])
        self.assertIn("MQSM", result["bridges"])


if __name__ == "__main__":
    unittest.main()
