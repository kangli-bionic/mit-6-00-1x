"""
@project_name: Bisection Search - Minimum Payment

@file_name: bisection-search-minimum-payment.py

@description: Calculates the minimum fixed monthly payment needed
    in order to pay off a credit card balance within 12 months.

@author: Phi Luu
@created: June 09, 2017
@updated: June 09, 2017
"""

monthlyInterestRate = annualInterestRate / 12.0


def getBalance(balance, monthlyPay, months):
    """Calculates the credit card balance after a number of months
    if a person pays a fixed amount of money each month.

    Args:
        balance: The balance of the credit card for this month
        monthlyPay: The fixed amount of money the person pays each month
        months: The number of months needed to calculate upto

    Returns: The remaining balance after a specified number of months
    """

    for month in range(months):
        monthlyUnpaid = balance - monthlyPay
        # this is the updated (remaining) balance of the current month
        # which will be used for next month
        balance = monthlyUnpaid + monthlyInterestRate * monthlyUnpaid
    return balance


def getMinMonthlyPay(balance, months, lowerBound, upperBound):
    """Calculates the minimum fixed monthly payment needed in order to
    pay off a credit card balance within a specified number of months.

    Args:
        balance: The balance of the credit card for this month
        months: The number of months needed to calculate upto
        lowerBound: The constantly updated lower bound of the minimum payment
        upperBound: The constantly updated upper bound of the minimum payment

    Returns: The minimum fixed monthly payment needed
    """

    monthlyPay = (lowerBound + upperBound) / 2
    currentBalance = getBalance(balance, monthlyPay, months)

    if abs(currentBalance) <= epsilon:  # within tolerance. Approved
        return monthlyPay
    elif currentBalance > epsilon:  # too low. Move to higher interval
        return getMinMonthlyPay(balance, months, monthlyPay, upperBound)
    else:  # too high. Move to lower interval
        return getMinMonthlyPay(balance, months, lowerBound, monthlyPay)


months = 12
# lower bound for the minimum monthly payment is the payment
# as if there were no interest rate
lowerMonthlyPay = balance / months
# upper bound for the minimum monthly payment is the one-time payment at
# the end of the final month (no money was paid for the previous months)
upperMonthlyPay = (balance * (1.0 + monthlyInterestRate)**months) / months
# set a tolerance on the final balance to accept or deny the given payment
epsilon = 0.005
print("Lowest Payment: " + str(
    round(
        getMinMonthlyPay(balance, months, lowerMonthlyPay, upperMonthlyPay),
        2)))
