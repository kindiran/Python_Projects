import json
import os
import time

from bill_master import csv_to_dict

l_bills_dir_path = "C:\\workdir\\Python_Projects\\billing\\input\\"
l_processed_bill_dir_path = "C:\\workdir\\Python_Projects\\billing\\processed\\"

def get_bill_details(file_name):
    with open(l_bills_dir_path+file_name,"r") as f:
        data_dict = json.load(f)
        return data_dict

def write_bill_details(data, filename):
    with open(l_processed_bill_dir_path+filename,"w") as f:
        data_dict = json.dump(data,f)

def delete_file(filename):
    try:
        os.remove(l_bills_dir_path+filename)
        print(f"The file '{filename}' has been deleted.")
    except OSError as e:
        print(f"Error occurred while deleting the file: {e}")
    finally:
        pass

def process_bill(file_name):
    bill = get_bill_details(file_name)
    bill_item_list = bill["BillDetails"]
    sum = 0
    for item in bill_item_list:
        pid = item["ProductID"] 
        qnty =  item["Quantity"] 
        price = master[str(pid)]["unit_price"]
        total = float(qnty) * float(price)
        sum = sum + total
        print(f"Cost for Product : {pid} - {qnty} - {price} - {total}")
        item.update({"line_total": total})
        print (f"Total Bill : {sum}")
    bill.update({"BillTotal": sum})
    write_bill_details(bill,file_name)
    delete_file(file_name)

#Processing bills
master = csv_to_dict()
while True:
    for file_name in os.listdir(l_bills_dir_path):
        file_path = os.path.join(l_bills_dir_path, file_name)
        if os.path.isfile(file_path):
            print(f'processing bill : {file_name} begins...')
            process_bill(file_name)
            print(f'processing bill : {file_name} end...')
    time.sleep(2)


