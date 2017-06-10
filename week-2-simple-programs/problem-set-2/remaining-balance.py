"""
@project_name: Remaining Balance

@file_name: remaining-balance.py

@description: Calculate the credit card balance after one year
    if a person only pays the minimum monthly payment required
    by the credit card company each month.

@author: Phi Luu
@created: June 09, 2017
@updated: June 09, 2017
"""


def getBalanceMinPay(balance, annualInterestRate, monthlyPaymentRate, months):
    """Calculates the credit card balance after a number of months
    if a person only pays the minimum monthly payment required
    by the credit card company each month.

    Args:
        balance: The balance of the credit card for this month
        annualInterestRate: The annual interest rate of the bank
        monthlyPaymentRate: The minumum monthly payment required
        months: The number of months needed to calculate upto

    Returns: The credit card balance after a number of months, in two decimal
    places
    """

    monthlyInterestRate = annualInterestRate / 12.0

    # this is the calculation of the remaining balance of this month
    # which will be used for next month
    for month in range(months):
        minMonthlyPay = monthlyPaymentRate * balance
        monthlyUnpaid = balance - minMonthlyPay
        # this is the updated (remaining) balance of the month
        # which will be used for next month
        balance = monthlyUnpaid + monthlyInterestRate * monthlyUnpaid
    return round(balance, 2)


print(getBalanceMinPay(balance, annualInterestRate, monthlyPaymentRate, 12))
