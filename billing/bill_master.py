import csv

def csv_to_dict():
    result_dict = {}

    with open("C:\\Users\Raja\\Python_Projects\\billing\\products.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row["product_id"]
            value = row
            result_dict[key] = value

    return result_dict






    

