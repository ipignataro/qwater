import csv
import sys

# Function to convert .map to .csv
def convert_map_to_csv(map_file, csv_file):
    with open(map_file, 'r') as map_file:
        # Read lines from .map file
        map_lines = map_file.readlines()
        
        # Assuming .map file format, parse the data accordingly
        # For example, splitting by whitespace or specific characters
        # This is a placeholder, actual parsing depends on your .map file structure
        parsed_data = [line.strip().split() for line in map_lines]

    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write parsed data to .csv file
        csv_writer.writerows(parsed_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input.map output.csv")
        sys.exit(1)
    
    input_map_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    # Example usage
    convert_map_to_csv(input_map_file, output_csv_file)