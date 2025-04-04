# List operations program: Sorting, Reversing, Inserting, Deleting, and Finding

def list_operations():
    # Initialize an empty list
    my_list = []

    while True:
        print("\nList Operations Menu:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Sort the list")
        print("5. Reverse the list")
        print("6. Display the list")
        print("7. Exit")

        # Get user choice
        choice = input("Please choose an operation (1-7): ")

        if choice == '1':
            # Insert an element
            element = input("Enter the element to insert: ")
            my_list.append(element)
            print(f"'{element}' has been inserted into the list.")

        elif choice == '2':
            # Delete an element
            element = input("Enter the element to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"'{element}' has been deleted from the list.")
            else:
                print(f"'{element}' not found in the list.")

        elif choice == '3':
            # Find an element
            element = input("Enter the element to find: ")
            if element in my_list:
                print(f"'{element}' is in the list.")
            else:
                print(f"'{element}' is not in the list.")

        elif choice == '4':
            # Sort the list
            my_list.sort()
            print("The list has been sorted.")
        
        elif choice == '5':
            # Reverse the list
            my_list.reverse()
            print("The list has been reversed.")
        
        elif choice == '6':
            # Display the list
            print("Current List:", my_list)
        
        elif choice == '7':
            # Exit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please choose a valid operation (1-7).")

# Call the function to execute the program
list_operations()

