{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9720cfd4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2050568560.py, line 12)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\admin\\AppData\\Local\\Temp\\ipykernel_16372\\2050568560.py\"\u001b[1;36m, line \u001b[1;32m12\u001b[0m\n\u001b[1;33m    except ValueError:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import LoanApproval\n",
    "import RateTenure\n",
    "import EMI\n",
    "\n",
    "def displayLoanDetails():\n",
    "    print(loanAmt)\n",
    "\n",
    "try:\n",
    "    loanAmt = float(input(\"Please enter the loan amount you would like to apply for:\\n \"))\n",
    "    collValue = float(input(\"Please enter the collateral value:\\n \"))\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"Please enter only numerical value as limit\")\n",
    "\n",
    "status, message = loanApproved(loanAmt, collValue)\n",
    "print(message)\n",
    "\n",
    "if status:\n",
    "    \n",
    "    print(\"Processing your loan application.\")\n",
    "    intRate, tenure = computerRateTenure(loanAmt, collValue)\n",
    "    emi = computeEMI(loanAmt, intRate, tenure)\n",
    "    displayLoanDetails()\n",
    "    \n",
    "    \n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e724d1c0",
   "metadata": {},
   "outputs": [],
   "source": []
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
