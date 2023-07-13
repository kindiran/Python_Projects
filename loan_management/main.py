import engine as le
import data as md

customername = "AAA"
customercreditscore = 299
loanamount = 29999


res = le.cus_details(master_loan_rules = md.master_loan_rules,cus_name = customername,credit_score = customercreditscore,loan_amt= loanamount)
print(res)

#le.loan_result(master_loan_rules = md.master_loan_rules,cus_name = customername,credit_score = customercreditscore,loan_amt= loanamount)

