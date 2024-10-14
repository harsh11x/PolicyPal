import unittest
from src.compliance_checker import ComplianceChecker

class TestComplianceChecker(unittest.TestCase):
    def test_gdpr_check(self):
        checker = ComplianceChecker("This policy mentions data subject and processing.")
        missing_keywords = checker.check_gdpr()
        self.assertEqual(missing_keywords, ['consent', 'rights'])

    def test_ccpa_check(self):
        checker = ComplianceChecker("This policy informs consumers about their rights.")
        missing_keywords = checker.check_ccpa()
        self.assertEqual(missing_keywords, ['sale of personal information', 'opt-out'])

if __name__ == '__main__':
    unittest.main()
