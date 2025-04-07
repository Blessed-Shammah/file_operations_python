def process_file(input_filename):
    try:
        # Read the input file
        with open(input_filename, 'r') as file:
            content = file.readlines()
            
        # Process the content (example: capitalize each line)
        modified_content = [line.upper() for line in content]
        
        # Create output filename by adding '_modified' before the extension
        output_filename = input_filename.rsplit('.', 1)[0] + '_modified.' + input_filename.rsplit('.', 1)[1]
        
        # Write to new file
        with open(output_filename, 'w') as file:
            file.writelines(modified_content)
            
        return f"Success! Modified content written to {output_filename}"
            
    except FileNotFoundError:
        return f"Error: File '{input_filename}' not found"
    except PermissionError:
        return f"Error: Permission denied to access '{input_filename}'"
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Interactive part
def main():
    filename = input("Enter the filename to process: ")
    result = process_file(filename)
    print(result)

# Allow running as script or using functions separately
if __name__ == "__main__":
    main()
