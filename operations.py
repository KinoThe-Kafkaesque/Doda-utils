import csv


def add_id_to_csv(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = ['id'] + reader.fieldnames  # Add 'id' to the beginning

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for i, row in enumerate(reader, start=1):
                row['id'] = i
                writer.writerow(row)


# Example usage
add_id_to_csv('your_input_file.csv', 'output_file_with_id.csv')
