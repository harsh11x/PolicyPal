import re

class ComplianceChecker:
    def __init__(self, policy_text):
        self.policy_text = policy_text

    def check_gdpr(self):
        # Example check for GDPR compliance
        required_keywords = ['data subject', 'processing', 'consent', 'rights']
        missing_keywords = [kw for kw in required_keywords if kw not in self.policy_text.lower()]
        return missing_keywords

    def check_ccpa(self):
        # Example check for CCPA compliance
        required_keywords = ['consumer', 'sale of personal information', 'opt-out']
        missing_keywords = [kw for kw in required_keywords if kw not in self.policy_text.lower()]
        return missing_keywords