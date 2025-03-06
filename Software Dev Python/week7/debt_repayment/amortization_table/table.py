import pandas as pd
import os
from datetime import datetime, timedelta
from debt_repayment.tools.my_logger import custom_logger


class AmortizationTable:
    """
    A class to represent an amortization table for a loan.

    Attributes:
    - loan_type (str) - The type of loan (e.g., 'home', 'car').
    - loan_balance (float) - The initial balance of the loan.
    - interest_rate (float) - The annual interest rate of the loan as a percentage.
    - num_months (int) - The number of months over which the loan will be repaid.
    - monthly_payment (float) - The amount to be paid each month.
    - amortization_df : DataFrame - A pandas DataFrame representing the amortization table.

    Methods:
    - create_table(): Generates the amortization table and saves it to a CSV file.
    - save_table(dataframe): Saves the given DataFrame to a CSV file in a specified directory.
    - more_principal(): Finds the first month where the principal paid exceeds the interest paid.
    - halfway(): Determines the month by which half of the initial loan balance has been paid off.
    - update_payments(lump_sum=0.0, extra_payment=0.0): Updates the loan balance and monthly payment 
      with optional lump sum and/or extra monthly payments and regenerates the amortization table.
    """

    def __init__(self, loan_type, loan_balance, interest_rate, num_months, monthly_payment):
        """
        Constructs all the necessary attributes for the AmortizationTable object.

        Parameters:
        - loan_type (str) - The type of loan (e.g., 'home', 'car').
        - loan_balance (float) - The initial balance of the loan.
        - interest_rate (float) - The annual interest rate of the loan as a percentage.
        - num_months (int) - The number of months over which the loan will be repaid.
        - monthly_payment (float) - The amount to be paid each month.
        """
        self.logger = custom_logger('AmortizationTable')
        self.logger.debug('Instantiating AmortizedTable Class')
        self.loan_type = loan_type
        self.loan_balance = loan_balance
        self.interest_rate = interest_rate
        self.num_months = num_months
        self.monthly_payment = monthly_payment
        self.amortization_df = pd.DataFrame()
        self.create_table()

    def create_table(self):
        """
        Generates the amortization table based on the initial loan details entered and saves it to a CSV file.
        """
        self.logger.info('Creating the amortized table')
        remaining_balance = self.loan_balance
        # To check for zero interest rate to avoid division by zero
        if self.interest_rate == 0:
            self.logger.error('Interest rate should be greater than zero.')
            return

        monthly_interest_rate = self.interest_rate / 12 / 100
        records = []

        for month in range(1, self.num_months + 1):
            interest_paid = remaining_balance * monthly_interest_rate
            principal_paid = self.monthly_payment - interest_paid
            remaining_balance -= principal_paid

            # To ensure remaining balance never goes negative
            if remaining_balance < 0:
                principal_paid += remaining_balance
                remaining_balance = 0.0

            records.append({
                "Pmt #": month,
                "Due date": (datetime.now() + timedelta(days=30*month)).strftime('%Y-%m-%d'),
                "Payment amount": self.monthly_payment,
                "Principal paid": principal_paid,
                "Interest paid": interest_paid,
                "Remaining balance": remaining_balance
            })

            if remaining_balance <= 0:
                break

        self.amortization_df = pd.DataFrame(records)
        self.save_table(self.amortization_df)

    def save_table(self, dataframe):
        """
        Saves the amortization table DataFrame to a CSV file in a specified directory.

        Parameters:
        - dataframe : DataFrame - The amortization table DataFrame to be saved.
        """
        directory = "debt_repayment/files/tables/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"{self.loan_type}.{
            self.loan_balance}.{self.monthly_payment}.csv"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            file.write(f"Loan type: {self.loan_type}, Balance: {self.loan_balance}, Monthly payment: {
                       self.monthly_payment}, Interest: {self.interest_rate}\n")
        dataframe.to_csv(filepath, mode='a', index=False)

    def more_principal(self):
        """
        Finds the first month where the principal paid exceeds the interest paid.

        Returns:
        - int or None - The month number where principal exceeds interest or None if it never does.
        """
        # The month where more is paid towards principal than interest
        for index, row in self.amortization_df.iterrows():
            if row["Principal paid"] > row["Interest paid"]:
                return index + 1
        return None  # In case the entire loan term pays more interest than principal

    def halfway(self):
        """
        Determines the month by which half of the initial loan balance has been paid off.

        Returns:
        - int or None - The month number by which half of the loan balance is paid or None if the loan ends before this occurs.
        """
        total_principal_paid = 0
        half_loan_balance = self.loan_balance / 2

        for index, row in self.amortization_df.iterrows():
            total_principal_paid += row["Principal paid"]
            if total_principal_paid >= half_loan_balance:
                return index + 1
        return None  # In case the loan term ends before paying off half the loan

    def update_payments(self, lump_sum=0.0, extra_payment=0.0):
        """
        Updates the loan balance and monthly payment with optional lump sum and/or extra monthly payments. 
        Regenerates the amortization table with updated details.

        Parameters:
        - lump_sum (float) - The amount of the lump sum payment to be applied to the loan balance (default is 0.0).
        - extra_payment (float) - The amount of extra payment to be added to the monthly payment (default is 0.0).
        """
        if lump_sum == 0.0 and extra_payment == 0.0:
            self.logger.error(
                'Unable to update loan and payments due to missing values.')
            return

        # Update log
        if lump_sum != 0.0:
            self.logger.info(f'Applying lump sum payment: {
                             lump_sum}, Current loan balance before payment: {self.loan_balance}')

        # Interest adjustment if lump sum payment equals loan balance
        if lump_sum == self.loan_balance:
            self.interest_to_be_paid = 0.0

        if extra_payment != 0.0:
            self.logger.info(f'Applying extra monthly payment: {
                             extra_payment}, Current monthly payment before update: {self.monthly_payment}')

        # Apply the updates
        if lump_sum != 0.0:
            self.loan_balance -= lump_sum

        if extra_payment != 0.0:
            self.monthly_payment += extra_payment

        # updated log state
        self.logger.info(f'Updated loan repayment details: monthly_payment={
                         self.monthly_payment}, loan_balance={self.loan_balance}')

        # amortization table with updated details
        self.create_table()
