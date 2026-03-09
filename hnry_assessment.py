
TAX_BRACKETS = [
    {"threshold": 15600.00, "percentage": 10.5},
    {"threshold": 53500.00, "percentage": 17.5},
    {"threshold": 78100.00, "percentage": 30},
    {"threshold": 180000.00, "percentage": 33},
    {"threshold": float("inf"), "percentage": 39}
]
TEST_CASES = [
{"income": 10000.00, "to_pay": 1050.00},
{"income": 35000.00, "to_pay": 5033.00},
{"income": 59000.00, "to_pay": 9920.50},
{"income": 100000.00, "to_pay": 22877.50},
{"income": 220000.00, "to_pay": 64877.50},
]

def calculate_tax(income):
    total_tax = 0
    tax_bracket_index = 0
    low_threshold = 0
    for tax_bracket in TAX_BRACKETS:
        # if income is greater than current bracket, pay max amount for that bracket
        if income > tax_bracket['threshold']:
            total_tax += (min(income, tax_bracket['threshold']) - low_threshold) * (tax_bracket['percentage'] / 100)
            tax_bracket_index += 1
            # set threshold as low threshold for next bracket
            low_threshold = tax_bracket['threshold']
        else:
            incomeToTax = income
            incomeToTax = income - low_threshold
            total_tax += incomeToTax  * (tax_bracket['percentage'] / 100)
            break
    
    return total_tax

def evalulate_tax_calculation():
    for test_case in TEST_CASES:
        answer = calculate_tax(test_case['income'])
        if answer == test_case["to_pay"]:
            print("Income:" + str(test_case["income"]) + ",  to pay: " + str(test_case["to_pay"])  + " Awnser: " + str(answer) + " SUCCESS")
        else:
            print("Income:" + str(test_case["income"]) + ",  to pay: " + str(test_case["to_pay"])  + " Awnser: " + str(answer) + " FAILED")


if __name__ == "__main__":
    evalulate_tax_calculation()
