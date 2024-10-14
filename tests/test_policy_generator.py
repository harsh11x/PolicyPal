import unittest
from policy_generator import PolicyGenerator

class TestPolicyGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PolicyGenerator(templates_path="../templates")

    def test_generate_policy(self):
        policy = self.generator.generate_policy("TestCorp", "2024-01-01", "finance", "us")
        self.assertIn("TestCorp", policy)
        self.assertIn("2024-01-01", policy)

if __name__ == "__main__":
    unittest.main()
