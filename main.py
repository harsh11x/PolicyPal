import os
from compliance_checker import ComplianceChecker
from policy_generator import PolicyGenerator
from colorama import Fore

def print_title():
    # Create a star pattern for the title "CRAWLER"
    star_title = [
        "  ***********           ***********       **             ***************   *************   **       **   ***********          ****          ** ",
        "  *************       ***************     **             ***************   *************    **     **    *************       **  **         ** ",
        "  **          **     **             **    **                   ***         **                **   **     **          **     **    **        ** ",
        "  **           **   **               **   **                   ***         **                 ** **      **           **   **      **       ** ",
        "  **************    **               **   **                   ***         **                  ***       **************   ************      ** ",
        "  ***********        **             **    **                   ***         **                  ***       ***********     **          **     ** ",
        "  **                  ***************     ************   ***************   *************       ***       **             **            **    ************ ",
        "  **                    ***********       ************   ***************   *************       ***       **            **              **   ************ ",
    ]
    
    # Print the star title
    for line in star_title:
        print(Fore.WHITE + line)
    
    print(Fore.CYAN + "Made by: Harsh Dev\n")

def main():
    print_title()

    # Policy options
    policy_options = [
        "acceptable_use_policy.txt",
        "basic_policy.txt",
        "compliance_policy.txt",
        "cookie_policy.txt",
        "data_protection_policy.txt",
        "privacy_policy.txt",
        "refund_policy.txt",
        "security_policy.txt",
        "shipping_policy.txt",
        "social_media_policy.txt",
        "terms_of_service.txt",
    ]

    # Display policy options
    print(Fore.GREEN + "Select a policy to generate:")
    for index, policy in enumerate(policy_options, start=1):
        print(Fore.RED + f"{index}. {policy}")

    # Get user choice
    choice = int(input("Enter the number of the policy you want to generate: ")) - 1
    selected_policy = policy_options[choice]

    # Collecting user inputs for company details
    company_name = input("Enter your company name: ")
    effective_date = input("Enter the effective date (YYYY-MM-DD): ")
    industry = input("Enter the industry (e.g., finance, healthcare, ecommerce): ")
    country = input("Enter the country (e.g., us, eu): ")

    # Load or generate policy text
    generator = PolicyGenerator('templates')
    
    try:
        # Modify the generate_policy method in PolicyGenerator to accept industry and country
        policy_text = generator.generate_policy(company_name, effective_date, industry, country, selected_policy)
        print("Generated Policy:\n", policy_text)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    # Optional: Adding custom clauses to the policy
    custom_clauses = input("Do you want to add custom clauses to the policy? (yes/no): ")
    if custom_clauses.lower() == 'yes':
        additional_text = input("Enter additional clauses: ")
        policy_text += f"\n\nAdditional Clauses:\n{additional_text}"

    # Initialize the compliance checker
    checker = ComplianceChecker(policy_text)

    # Check for GDPR and CCPA compliance
    missing_gdpr_keywords = checker.check_gdpr()
    missing_ccpa_keywords = checker.check_ccpa()

    # Output compliance results
    if missing_gdpr_keywords:
        print("\nMissing keywords for GDPR compliance:", missing_gdpr_keywords)
    else:
        print("\nYour policy is GDPR compliant!")

    if missing_ccpa_keywords:
        print("\nMissing keywords for CCPA compliance:", missing_ccpa_keywords)
    else:
        print("\nYour policy is CCPA compliant!")

    # Create the "You_Policy" directory on the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "You_Policy")
    os.makedirs(desktop_path, exist_ok=True)

    # Save the final generated policy to a file
    save_policy = input("Do you want to save this policy to a file? (yes/no): ")
    if save_policy.lower() == 'yes':
        file_name = os.path.join(desktop_path, f"{selected_policy}")
        with open(file_name, 'w') as policy_file:
            policy_file.write(policy_text)
        print(f"Policy saved as {file_name}")

if __name__ == "__main__":
    main()