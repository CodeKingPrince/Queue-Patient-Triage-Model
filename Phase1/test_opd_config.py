from main1 import validate_opd_config

result = validate_opd_config()

print("\nOPD CONFIGURATION TEST")
print("=" * 45)

print("Configuration valid:", result["valid"])

print(
    "Configured departments:",
    result["configured_count"]
)

print(
    "Missing departments:",
    result["missing_departments"]
)

print(
    "Invalid configurations:",
    result["invalid_configs"]
)

if result["valid"]:

    print("\nAll OPD configurations passed validation.")

else:


    

    print("\nPlease correct the configuration errors.")