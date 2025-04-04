# Program to merge two dictionaries with addition of values for overlapping keys

def merge_dictionaries():
    # Get the first dictionary from the user
    print("Enter the first dictionary:")
    dict1 = input("Enter dictionary in key:value format, separated by commas (e.g., key1:value1,key2:value2): ")
    dict1 = dict(map(str.strip, item.split(":")) for item in dict1.split(","))
    
    # Convert string values to integers for numerical operations
    dict1 = {key: int(value) for key, value in dict1.items()}
    
    # Get the second dictionary from the user
    print("\nEnter the second dictionary:")
    dict2 = input("Enter dictionary in key:value format, separated by commas (e.g., key1:value1,key2:value2): ")
    dict2 = dict(map(str.strip, item.split(":")) for item in dict2.split(","))
    
    # Convert string values to integers for numerical operations
    dict2 = {key: int(value) for key, value in dict2.items()}
    
    # Merge the two dictionaries
    merged_dict = dict1.copy()  # Start with the first dictionary

    for key, value in dict2.items():
        if key in merged_dict:
            # If the key exists in both dictionaries, add the values
            merged_dict[key] += value
        else:
            # If the key doesn't exist in the merged dictionary, add the key-value pair
            merged_dict[key] = value
    
    # Display the merged dictionary
    print("\nMerged Dictionary with added values for overlapping keys:")
    print(merged_dict)

# Call the function to execute
merge_dictionaries()

