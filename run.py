import json

def list_to_json_with_zero_based_numbers(list_of_strings):
    # Creating a dictionary where each string is assigned a number as the key, starting from 0
    numbered_dict = {str(i): string for i, string in enumerate(list_of_strings)}
    return numbered_dict

# Example usage
example_list = ['Fall-Detected', 'Gloves', 'Goggles', 'Hardhat', 'Ladder', 'Mask', 'NO-Gloves', 'NO-Goggles', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest']


result = list_to_json_with_zero_based_numbers(example_list)
print(json.dumps(result))

