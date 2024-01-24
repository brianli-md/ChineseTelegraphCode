import os
import json

file_names = ["tw", "cn"]  # List of file names to process

for file_name in file_names:
    file_path = f"./{file_name}"  # Path to the file in the current directory
    output_dir = "./build"  # Output directory path
    output_file_path = f"{output_dir}/{file_name}.json"  # Output file path within the "build" directory

    # Check if the "build" directory exists and create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    result = []  # Array to store the converted lines

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            line_array = line.split()  # Split the line at spaces
            result.append(line_array)  # Append the converted line to the result array

    # Create a dictionary to store the lines in the desired format
    chinese_code_json = {}
    for line_array in result:
        chinese_code_json[line_array[1]] = line_array[0]

    # Save the JSON data to a file within the "build" directory
    with open(output_file_path, 'w') as output_file:
        json.dump(chinese_code_json, output_file, ensure_ascii=False)

    print(f"JSON data saved to {output_file_path}")
