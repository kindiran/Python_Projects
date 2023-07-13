import datetime
import logging

logging.basicConfig(filename="C:\\workdir\\loan\\log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

def cus_details(master_loan_rules,cus_name,credit_score,loan_amt):

    logging.debug("Load Application is received")
    LoanApplicationStatus = "Denied"
    InterestRate = -1
    DurationInMonths = -1
    customername = cus_name

    for rule in master_loan_rules:
       logging.debug("Processing rule {rule}")  
       if credit_score >= rule["min_cs"] and credit_score <= rule["max_cs"] and loan_amt >= rule["min_loan_amt"] and loan_amt <= rule["max_loan_amt"]:
          LoanApplicationStatus = "Approved"
          InterestRate = rule["interest"]
          DurationInMonths = rule["duration"]
    logging.info(f"Loan Application is processed with result {LoanApplicationStatus}")   
    #if LoanApplicationStatus == "Approved":
        #return {"LoanApplicationStatus: ":"Approved",
       # "InterestRate": rule["interest"],
        #"DurationInMonths": rule["duration"]}
     
    #elif LoanApplicationStatus == "Denied":
     #  return {"LoanApplicationStatus: ":"Denied","message":"sorry,you are not eligible for the loan"}
    
    logging.debug(f"Generating statement begins")  
    write_result(customername,LoanApplicationStatus,loan_amt,InterestRate,DurationInMonths)
    logging.debug(f"Generating statement ends")    


def loan_result(master_loan_rules,cus_name,credit_score,loan_amt):
    
    LoanApplicationStatus = "Denied"
    InterestRate = -1
    DurationInMonths = -1
    customername = cus_name

    f = open("C:\\workdir\\loan\\file_output\\loan-output.txt", "w")
    f.write(f"Dear {customername},")    

    for rule in master_loan_rules:
    
       if credit_score >= rule["min_cs"] and credit_score <= rule["max_cs"] and loan_amt >= rule["min_loan_amt"] and loan_amt <= rule["max_loan_amt"]:
          LoanApplicationStatus = "Approved"
          InterestRate = rule["interest"]
          DurationInMonths = rule["duration"]
        
    if LoanApplicationStatus == "Approved":
        f.write("\n Congratulations!.\n We are happy to inform you that your loan is approved.\n")
        f.write(f' Approved Amount : {loan_amt} with interest rate : {rule["interest"]} and for duration: {rule["duration"]}.')
     
    elif LoanApplicationStatus == "Denied":
       f.write("Sorry! We caould not approve your loan at this point of time.")
     
    f.close() 
   
def write_result(customername,LoanApplicationStatus,loan_amt,InterestRate,DurationInMonths):

    f = open("C:\\workdir\\loan\\file_output\\loan-output.txt", "w")
    f.write(f'                                 {datetime.datetime.today().strftime("%Y%m%d %H:%M:%S")} \n')
    f.write(f"Dear {customername},")    

    if LoanApplicationStatus == "Approved":
        f.write("\n Congratulations!.\n We are happy to inform you that your loan is approved.\n")
        f.write(f' Approved Amount : {loan_amt} with interest rate : {InterestRate} and for duration: {DurationInMonths}.')
     
    elif LoanApplicationStatus == "Denied":
       f.write("Sorry! We caould not approve your loan at this point of time.")
     
    f.close() 
