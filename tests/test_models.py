import unittest
from models.traffic_flow_model import build_traffic_flow_model

class TestTrafficFlowModel(unittest.TestCase):
    def test_model_initialization(self):
        model = build_traffic_flow_model((None, 100, 1))
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
