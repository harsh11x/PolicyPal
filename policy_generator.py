import os
import json

class PolicyGenerator:
    def __init__(self, templates_path, config_path=None):
        # Store the absolute path for better flexibility
        self.templates_path = os.path.abspath(templates_path)
        
        # Load config for defaults
        if config_path:
            self.config = self.load_config(config_path)
        else:
            self.config = {"default_industry": "General", "default_country": "Global"}

    def load_config(self, config_path):
        # Read the JSON config file for defaults
        config_file_path = os.path.abspath(config_path)
        if not os.path.exists(config_file_path):
            raise FileNotFoundError(f"Config file not found: {config_file_path}")
        
        with open(config_file_path, 'r') as config_file:
            return json.load(config_file)

    def generate_policy(self, company_name, effective_date, industry=None, country=None, policy_name=None):
        # Determine the path to the policy template file based on the policy name
        if policy_name:
            template_file_path = os.path.join(self.templates_path, policy_name)
        else:
            template_file_path = os.path.join(self.templates_path, "basic_policy.txt")

        # Check if the file exists
        if not os.path.exists(template_file_path):
            raise FileNotFoundError(f"Template file not found: {template_file_path}")

        # Read the template file
        with open(template_file_path, 'r') as template_file:
            template = template_file.read()

        # Use defaults from config or provided values
        industry = industry if industry else self.config.get("default_industry", "General")
        country = country if country else self.config.get("default_country", "Global")

        # Format the template with provided details
        return template.format(
            company_name=company_name, 
            effective_date=effective_date,
            industry=industry, 
            country=country
        )

# Example usage:
if __name__ == "__main__":
    # Assuming templates are located in a 'templates' folder and config in 'config.json'
    generator = PolicyGenerator(templates_path="templates", config_path="config.json")
    
    # Generate a policy for a specific company, industry, and country
    policy_name = "basic_policy.txt"  # Replace with the desired policy template name
    policy = generator.generate_policy(
        company_name="ABC Corp", 
        effective_date="2024-10-13",
        policy_name=policy_name
    )
    
    print(policy)