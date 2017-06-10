"""
@project_name: Minimum Payment

@file_name: minimum-payment.py

@description: Calculates the minimum fixed monthly payment needed
    in order to pay off a credit card balance within 12 months.

@author: Phi Luu
@created: June 09, 2017
@updated: June 09, 2017
"""


def getMinMonthlyPay(balance, annualInterestRate, months):
    """Calculates the minimum fixed monthly payment needed in order to
    pay off a credit card balance within a specified number of months.

    Args:
        balance: The balance of the credit card for this month
        annualInterestRate: The annual interest rate of the bank
        months: The number of months needed to calculate upto

    Returns: The minimum fixed monthly payment needed

    Assumptions: The monthly payment must be a multiple of $10.
    """

    monthlyInterestRate = annualInterestRate / 12.0
    minMonthlyPay = 10  # start with $10
    tempBalance = balance  # balance for each case of minMonthlyPay

    # continue increasing the monthly payment
    # until the balance at the end of the specified number of months
    # getting paid off
    while True:
        for month in range(months):
            monthlyUnpaid = tempBalance - minMonthlyPay
            # this is the updated (remaining) balance of the month
            # which will be used for next month
            tempBalance = monthlyUnpaid + monthlyInterestRate * monthlyUnpaid

        # this version of tempBalance is at the end of
        # the specified number of months
        if tempBalance <= 0:
            break
        # reset balance and add $10 more to the monthly payment
        tempBalance = balance
        minMonthlyPay += 10
    return minMonthlyPay


print("Lowest Payment: " +
      str(getMinMonthlyPay(balance, annualInterestRate, 12)))
