import csv

def write_to_csv(data):
    file_name = "data/Dataset.csv"
    header = ["ID", "Name", "Age"]  # Modify as needed
    
    try:
        with open(file_name, "r") as file:
            existing_data = file.readlines()
        file_exists = len(existing_data) > 0
    except FileNotFoundError:
        file_exists = False
    
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)

# Uncomment the lines below to insert data
write_to_csv([1, "Alice", 25])
# write_to_csv([2, "Bob", 30])
# write_to_csv([3, "Charlie", 22])
