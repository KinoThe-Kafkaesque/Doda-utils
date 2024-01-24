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


# add_id_to_csv('75.csv', '75_id.csv')


def insert_text_to_column(input_file, column_name, values_array, output_file):
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()


values = [{
    'id': 1,
    'text': 'Hello'
}, {
    'id': 2,
    'text: 'World'
}]

insert_text_to_column('75_id.csv', 'eng', values, '75_id_text.csv')
