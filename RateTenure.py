{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3840ce83",
   "metadata": {},
   "source": [
    "# Rate and Tenure Calculation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f170364",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python program to determine rate and tenure based on principal and collateral amount\n",
    "\n",
    "# Define the maximum loan amount and the minimum collateral value required for loan approval\n",
    "MAX_LOAN_AMOUNT = 100000\n",
    "\n",
    "# Define the minimum and maximum interest rates for the loan\n",
    "MIN_INTEREST_RATE = 5\n",
    "MAX_INTEREST_RATE = 10\n",
    "\n",
    "# Define the minimum and maximum loan periods in months\n",
    "MIN_LOAN_PERIOD = 12\n",
    "MAX_LOAN_PERIOD = 60\n",
    "\n",
    "def computerRateTenure(principal, collateral):\n",
    "    # Calculate the loan-to-collateral ratio\n",
    "    ratio = principal / collateral\n",
    "\n",
    "\n",
    "    # Calculate the interest rate based on the loan-to-collateral ratio\n",
    "    intRate = (ratio * (MAX_INTEREST_RATE - MIN_INTEREST_RATE)) + MIN_INTEREST_RATE\n",
    "\n",
    "    # Calculate the loan period based on the loan amount\n",
    "    tenure = int((loanAmt / MAX_LOAN_AMOUNT) * (MAX_LOAN_PERIOD - MIN_LOAN_PERIOD)) + MIN_LOAN_PERIOD\n",
    "\n",
    "    # Print the interest rate and loan period\n",
    "    return round(intRate, 2), tenure"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
