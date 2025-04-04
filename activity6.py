# Program to merge two dictionaries

def merge_dictionaries():
    # Get the first dictionary from the user
    print("Enter the first dictionary:")
    dict1 = input("Enter dictionary in key:value format, separated by commas (e.g., key1:value1,key2:value2): ")
    dict1 = dict(map(str.strip, item.split(":")) for item in dict1.split(","))
    
    # Get the second dictionary from the user
    print("\nEnter the second dictionary:")
    dict2 = input("Enter dictionary in key:value format, separated by commas (e.g., key1:value1,key2:value2): ")
    dict2 = dict(map(str.strip, item.split(":")) for item in dict2.split(","))
    
    # Merge the two dictionaries
    merged_dict = {**dict1, **dict2}
    
    # Display the merged dictionary
    print("\nMerged Dictionary:")
    print(merged_dict)

# Call the function to execute
merge_dictionaries()

