def read_and_write_file():
    # Step 1: Ask the user for the input filename
    input_filename = input("Enter the name of the file to read (e.g., input.txt): ")

    # Step 2: Define the output filename (e.g., append '_modified' to the original name)
    output_filename = input_filename.split('.')[0] + '_modified.txt'

    try:
        # Step 3: Open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Step 4: Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()  # Simple modification: convert to uppercase

        # Step 5: Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Success! The modified content has been written to {output_filename}.")

    except FileNotFoundError:
        # Handle the case where the input file doesn't exist
        print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again.")
    except PermissionError:
        # Handle permission issues (e.g., no read/write access)
        print("Error: Permission denied. Please check if you have the necessary permissions to read/write files.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_file()