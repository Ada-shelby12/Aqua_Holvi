import csv
import os

def create_csv(filename):
    """Creates a CSV file with a header."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Age'])

def insert_values(filename):
    """Inserts values into the CSV file."""
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        while True:
            id = input("Enter ID (or 'q' to quit): ")
            if id == 'q':
                break
            name = input("Enter Name: ")
            age = input("Enter Age (integer): ")
            try:
                age = int(age)
                writer.writerow([id, name, age])
            except ValueError:
                print("Invalid age input. Please enter an integer.")

def read_csv(filename):
    """Reads and displays values from the CSV file."""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            id, name, age = row
            print(f"ID: {id}, Name: {name}, Age: {age}")

def update_csv(filename):
    """Updates values in the CSV file."""
    temp_filename = 'temp.csv'
    with open(filename, 'r') as file, open(temp_filename, 'w', newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)
        writer.writerow(next(reader))  # Write header

        for row in reader:
            id, name, age = row
            print(f"Row: {row}")
            update = input("Update this row? (y/n): ")
            if update.lower() == 'y':
                name = input("Enter new name: ")
                age = input("Enter new age (integer): ")
                try:
                    age = int(age)
                    writer.writerow([id, name, age])
                except ValueError:
                    print("Invalid age input. Please enter an integer.")
            else:
                writer.writerow(row)

    os.remove(filename)
    os.rename(temp_filename, filename)

def delete_rows(filename):
    """Deletes rows from the CSV file."""
    temp_filename = 'temp.csv'
    with open(filename, 'r') as file, open(temp_filename, 'w', newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)
        writer.writerow(next(reader))  # Write header

        for row in reader:
            print(f"Row: {row}")
            delete = input("Delete this row? (y/n): ")
            if delete.lower() != 'y':
                writer.writerow(row)

    os.remove(filename)
    os.rename(temp_filename, filename)

if __name__ == "__main__":
    filename = 'data.csv'

    create_csv(filename)
    insert_values(filename)
    read_csv(filename)
    update_csv(filename)
    delete_rows(filename)