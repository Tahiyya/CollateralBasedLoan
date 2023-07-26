{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8a6dae9e",
   "metadata": {},
   "source": [
    "# EMI Computation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a7b9f4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python program to calculate EMI\n",
    "\n",
    "# Import the math module to use the power function\n",
    "import math\n",
    "\n",
    "# Calculate the monthly interest rate and number of months\n",
    "def computeEMI(loanAmt, intRate, tenure):\n",
    "    monIntRate = ( intRate / 100 ) / 2\n",
    "    numMonths = tenure\n",
    "\n",
    "    # Calculate the EMI using the formula\n",
    "    emi = (loanAmt * monIntRate * math.pow(1 + monIntRate, numMonths)) / (math.pow(1 + monIntRate, numMonths) - 1)\n",
    "    return round(emi, 2)\n"
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
