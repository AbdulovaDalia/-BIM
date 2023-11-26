import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def convert_csv_to_json(input_filename: str, output_filename: str) -> None:
    data = []
    with open(input_filename, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(output_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def task() -> None:
    convert_csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
