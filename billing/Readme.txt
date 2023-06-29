Billing Project:

Bill Master:
  Reads the product master csv and load it into a dictionary


Bill Generator:
  Generates bills continuously in JSON format with random data. 

Bill Processor:
  Process the bills generated the Bill Generator. Read through all the bills, get the product Id and find the price for the product using the product master file and calculate the line amount for each product and update the JSON.  Also, calculates the total amount for the bill and udpate the JSON and finally dumps the JSON output into a file in the processed folder and delete the input file.

Input Bill:

{
    "BillID": "20230628203918",
    "BillDate": "02/19/2008 22:44:19",
    "StoreID": 2,
    "BillDetails": [{
            "ProductID": 23,
            "Quantity": 10
        }, {
            "ProductID": 18,
            "Quantity": 8
        }, {
            "ProductID": 5,
            "Quantity": 16
        }, {
            "ProductID": 22,
            "Quantity": 15
        }, {
            "ProductID": 17,
            "Quantity": 1
        }, {
            "ProductID": 1,
            "Quantity": 11
        }, {
            "ProductID": 6,
            "Quantity": 6
        }
    ]
}

Ouput Bill:

{
    "BillID": "20230628203918",
    "BillDate": "02/19/2008 22:44:19",
    "StoreID": 2,
    "BillDetails": [{
            "ProductID": 23,
            "Quantity": 10,
            "line_total": 30.0
        }, {
            "ProductID": 18,
            "Quantity": 8,
            "line_total": 16.0
        }, {
            "ProductID": 5,
            "Quantity": 16,
            "line_total": 64.0
        }, {
            "ProductID": 22,
            "Quantity": 15,
            "line_total": 60.0
        }, {
            "ProductID": 17,
            "Quantity": 1,
            "line_total": 1.0
        }, {
            "ProductID": 1,
            "Quantity": 11,
            "line_total": 27.5
        }, {
            "ProductID": 6,
            "Quantity": 6,
            "line_total": 30.0
        }
    ],
    "BillTotal": 228.5
}


