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
            
            for row in reader:
                    row_id = int(row['id'])  # Assuming 'id' is the column name for IDs. Adjust if different.
                    if row_id in values:
                        row[column_name] = values[row_id]
                    writer.writerow(row)


values = {
    1: 'The student has good grades',
    2: 'The teacher is the heart of reform',
    3: 'Why are these caravans here?',
    4: 'We must protect it',
    5: 'Singing united everyone',
    6: 'Girls wearing masks are dancing',
    7: 'Dancing is necessary here',
    8: 'Healthy food is what sustains life',
    9: 'We must strive to survive',
    10: 'There is life for those who seek it',
    11: 'They rebelled for freedom',
    12: 'The bird lives in the nest',
    13: 'We live now, we die later',
    14: 'Emigration is difficult',
    15: 'Live in a foreign land without your homeland',
    16: 'People see you as a stranger to them',
    17: 'Beauty begins from within',
    18: 'They will harm you even if you have nothing',
    19: 'She told you she\'d come at night',
    20: 'She closed it in her mouth so it wouldn\'t be seen'
}


insert_text_to_column('75_id.csv', 'eng', values, '75_id_text.csv')
