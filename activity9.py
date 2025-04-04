import os
import shutil

# Create sample files and folders (for demo purpose)
os.makedirs('demo_folder', exist_ok=True)
with open('demo_folder/sample.txt', 'w') as f:
    f.write("This is a demo file.")

# Access: List files in the folder
print("Files in 'demo_folder':")
print(os.listdir('demo_folder'))

# Rename the file
os.rename('demo_folder/sample.txt', 'demo_folder/renamed.txt')
print("\nFile renamed to 'renamed.txt'")

# Copy the file
shutil.copy('demo_folder/renamed.txt', 'demo_folder/copied.txt')
print("File copied to 'copied.txt'")

# Move the copied file to a new folder
os.makedirs('moved_folder', exist_ok=True)
shutil.move('demo_folder/copied.txt', 'moved_folder/copied.txt')
print("Copied file moved to 'moved_folder'")

