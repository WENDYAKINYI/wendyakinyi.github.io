# Import built--in packages
import numpy as np

# Import installed packages
import tkinter as tk
import ttkbootstrap as ttk


### -----------------------------------------###
from debt_repayment.tools.helper_functions import calculate_payments, calculate_total_paid, calculate_total_interest
from debt_repayment.amortization_table.table import AmortizationTable
### -----------------------------------------###
# ####-------------------------------------------------------------------####
# #### You will need to write your own functions/class in the appropriate
# #### location and import them here using a combination of relative and
# #### absolute imports. Unless specified in the homework, you're free to
# #### May the odds be ever in your favor :)

# def calculate_payments(amount, int_rate, duration):
#     pass

# def calculate_total_paid(amount, int_rate, duration):
#     pass

# def calculate_total_interest(amount, int_rate, duration):
#     pass

# # class AmortizationTable:
#     pass
# ####-------------------------------------------------------------------####
### -----------------------------------------###
### -----ADD YOUR IMPORT STATEMENTS HERE-----###
### -----------------------------------------###


# Global variables:
TEXTSIZE = 12


class DebtAPP(tk.Tk):
    """
    This creates the primary window that contains the user interface. It is considered
    the "parent" window for all other elements in the application. Creates the title
    for the window, sets the starting size of the window and a minimum window size.
    It also instantiates a "top window" (which is a Frame, it's a baby version of a window) 
    which contains the top half of the application and a "middle window" (which is another Frame) 
    containing the lower portion of the application.

    Attributes:
    --------------------------------------------------------
        cls (AmortizationTable): class that we use to create the amortization table

    Methods:
    --------------------------------------------------------
        __init__: instantiates the primary application window and the top and bottom
        frames (parts) of the application
    """

    def __init__(self, cls):
        global data
        global a_table
        a_table = cls

        # main setup
        super().__init__()
        self.title('Loan Repayment Calculator')
        self.geometry('1000x600')
        self.minsize(width=800, height=600)

        # Top Window:
        self.top_window = TopWindow(self)
        # Widgets
        # input fields (loan amount etc)
        self.input_field = InputField(self.top_window)
        # output fields (monthly payments etc)
        self.payment_output = Payment(self.top_window)

        # Middle Window:
        self.mid_window = MiddleWindow(self)
        # Widgets
        # input fields (lump sum payment etc)
        self.input_field = ExtraInputField(self.mid_window)
        # output fields (updated total repaid amount etc)
        self.payment_output = UpdatedPayment(self.mid_window)

        # Run
        self.mainloop()


class TopWindow(ttk.Frame):
    """
    This creates the top portion of the application, input/output fields for the 
    loan type, loan amount, interest rate, duration

    Attributes:
    --------------------------------------------------------
        parent: parent window, i.e. this "smaller" window needs to be placed inside 
        a larger window, which in this case is the DebAPP primary window.

    Methods:
    --------------------------------------------------------
        __init__: creates label at the top of the application and creates input 
        field for the loan type.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(pady=10, expand=True)

        ttk.Label(master=self,
                  text="Adjust the calculator to see the results update:",
                  font=f"Calibri 18").pack()

        global LOAN_TYPE_VAR
        self.loan_type = ttk.Label(
            master=self, text="Loan Type:", font=f"Calibri {TEXTSIZE}")
        LOAN_TYPE_VAR = tk.StringVar()
        self.loan_type_entry = ttk.Entry(
            master=self, textvariable=LOAN_TYPE_VAR)
        self.loan_type.pack()
        self.loan_type_entry.pack()


class InputField(ttk.Frame):
    """
    This creates input fields at the top of the application, i.e. loan amount,
    interest rate, duration of the loan. 
    Is anyone reading this code?... asking for a friend.

    Attributes:
    --------------------------------------------------------
        parent: parent window, i.e. this "smaller" input window needs to be placed inside 
        a larger window, which in this case is the TopWindow.

    Methods:
    --------------------------------------------------------
        __init__: calls for the creation of the widgets (which are the input fields) 
        and creates the layout (places the widgets)

        create_widgets: creates the variables and labels needed to show the text asking
        the user to provide the necessary input and input boxes where the user types
        in the values

        create_layout: creates the variables and labels needed to show the show the
        output of the calculations to the user.
    """

    def __init__(self, parent):

        # Layout setup
        super().__init__(parent)
        self.pack(side='left', expand=True, fill='both', pady=10)

        # Widgets
        self.create_widgets()
        # Place widgets
        self.create_layout()

    def create_widgets(self):
        """
        Creates the widgets, i.e. input fields, button and text prompts for the user

        Args:
            None

        Returns:
            None
        """
        # Loan balance input, how much did you borrow :
        self.loan_label = ttk.Label(
            master=self, text="Loan Balance:", font=f"Calibri {TEXTSIZE}")
        self.loan_sign = ttk.Label(
            master=self, text="$", background='light grey', font=f"Calibri {TEXTSIZE}")
        global LOAN_BALANCE
        LOAN_BALANCE = tk.DoubleVar(master=self)
        self.loan_entry = ttk.Entry(master=self, textvariable=LOAN_BALANCE)

        # Interest rate input for the loan:
        self.interest_label = ttk.Label(
            master=self, text="Interest Rate:", font=f"Calibri {TEXTSIZE}")
        self.interest_sign = ttk.Label(
            master=self, background='light grey', text="%", font=f"Calibri {TEXTSIZE}")
        global INTEREST_PERCENTAGE
        # I need good book recommendations. Any suggestions ?
        INTEREST_PERCENTAGE = tk.DoubleVar(master=self)
        self.interest_entry = ttk.Entry(
            master=self, textvariable=INTEREST_PERCENTAGE)

        # Remaining time on the loan input, i.e. number of months:
        self.time_label = ttk.Label(
            master=self, text="Remaining Time:", font=f"Calibri {TEXTSIZE}")
        self.time_sign = ttk.Label(
            master=self, text="months", background='light grey', font=f"Calibri {TEXTSIZE}")
        global TIME_REMAINING
        TIME_REMAINING = tk.IntVar(master=self)
        self.time_entry = ttk.Entry(master=self, textvariable=TIME_REMAINING)

        # Creates the payment button and calls all the necessary functions to compute the
        # monthly payments, total repaid (including interest) and total interest paid.
        self.payment_button = ttk.Button(master=self, text="Calculate Payments",
                                         command=lambda: [self.set_payment_var(LOAN_BALANCE.get(),
                                                                               INTEREST_PERCENTAGE.get(),
                                                                               TIME_REMAINING.get()),
                                                          self.set_total_paid_var(LOAN_BALANCE.get(),
                                                                                  INTEREST_PERCENTAGE.get(),
                                                                                  TIME_REMAINING.get()),
                                                          self.set_total_interest_var(LOAN_BALANCE.get(),
                                                                                      INTEREST_PERCENTAGE.get(),
                                                                                      TIME_REMAINING.get())])
        return

    def set_payment_var(self, amount, int_rate, duration):
        """
        Updates the variable MONTHLY_PAYMENT by making a call to the calculate_payments
        defined by students and imported into this module.

        Args:
            amount (float): total loan amount
            int_rate (float): interest rate for the loan
            duration (int): duration of the loan in months

        Returns:
            None
        """
        MONTHLY_PAYMENT.set(
            round(calculate_payments(amount, int_rate, duration), 2))
        return

    def set_total_paid_var(self, amount, int_rate, duration):
        """
        Updates the variable TOTAL_REPAID by making a call to the calculate_total_paid
        defined by students and imported into this module.

        Args:
            amount (float): total loan amount
            int_rate (float): interest rate for the loan
            duration (int): duration of the loan in months

        Returns:
            None
        """
        TOTAL_REPAID.set(
            round(calculate_total_paid(amount, int_rate, duration), 2))
        return

    def set_total_interest_var(self, amount, int_rate, duration):
        """
        Updates the variable TOTAL_INTEREST by making a call to the calculate_total_paid
        defined by students and imported into this module. Also give you a recommendation
        for a couple of funny videos from "Golden Moustache".

        Args:
            amount (float): total loan amount
            int_rate (float): interest rate for the loan
            duration (int): duration of the loan in months

        Returns:
            None
        """
        TOTAL_INTEREST.set(
            round(calculate_total_interest(amount, int_rate, duration), 2))
        return
        # Worth a watch.
        # https://www.youtube.com/watch?v=bGOwX0A_WKM
        # This one too, just need to auto-translate in the settings of the video
        # https://www.youtube.com/watch?v=GfJkh6xEld8
        # If you're coming across these "easter eggs". Keep them to yourself, I'm curious
        # how many people will actually see them.

    def create_layout(self):
        """
        Creates the layout for all the input fields defined in the create_widgets

        Args:
            None

        Returns:
            None
        """
        # Define the grid layout (number of rows and columns)
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # Place widgets
        # place loan input field
        self.loan_label.grid(row=0, column=0, pady=10)
        self.loan_sign.grid(row=0, column=1, sticky='e', pady=10)
        self.loan_entry.grid(row=0, column=2, sticky='w', pady=10)

        # place interest rate input field
        self.interest_label.grid(row=1, column=0, pady=10)
        self.interest_sign.grid(row=1, column=1, sticky='e', pady=10)
        self.interest_entry.grid(row=1, column=2, sticky='w', pady=10)

        # place remaining time on loan input field
        self.time_label.grid(row=2, column=0, pady=10)
        self.time_sign.grid(row=2, column=1, sticky='w', pady=10)
        self.time_entry.grid(row=2, column=2, sticky='e', pady=10)
        self.payment_button.grid(
            row=3, columnspan=3, sticky='nsew', pady=10, padx=10)

        return


class Payment(ttk.Frame):
    """
    This creates the labels for the output of the calculations done by 
    the student's wonderful code, or is it wonderful ? Time will tell

    Attributes:
    --------------------------------------------------------
        parent: parent window, i.e. this "smaller" output window needs to be placed inside 
        a larger window, which in this case is the TopWindow.

    Methods:
    --------------------------------------------------------
        __init__: calls for the creation of the widgets (which is the text) 
        and creates the layout (places the widgets). Nails, Hair, Hips, Heels

        create_widgets: creates the variables and labels needed to show the text asking
        the user to provide the necessary input and input boxes where the user types
        in the values

        create_layout: creates the variables and labels needed to show the show the
        output of the calculations to the user.
    """

    def __init__(self, parent):

        # Layout setup
        super().__init__(parent)
        self.pack(side='left', expand=True, fill='both', pady=10)

        # Widgets
        self.create_widgets()
        # Place widgets
        self.create_layout()

    def create_widgets(self):
        """
        Creates the widgets, i.e. output fields, button and text prompts for the user

        Args:
            None

        Returns:
            None
        """
        global MONTHLY_PAYMENT
        MONTHLY_PAYMENT = tk.DoubleVar(self, value=np.nan)
        self.monthly_payment_label = ttk.Label(master=self,
                                               text=f"Your estimated monthly payment is: $",
                                               font=f"Calibri {TEXTSIZE}")
        self.monthly_payment_value = ttk.Label(master=self,
                                               textvariable=MONTHLY_PAYMENT,
                                               font=f"Calibri {TEXTSIZE}")

        global TOTAL_REPAID
        TOTAL_REPAID = tk.DoubleVar(self, value=np.nan)
        self.total_repaid = ttk.Label(master=self,
                                      text="Total amount to be repaid (with interest): $",
                                      font=f"Calibri {TEXTSIZE}")
        self.total_repaid_value = ttk.Label(master=self,
                                            textvariable=TOTAL_REPAID,
                                            font=f"Calibri {TEXTSIZE}")

        global TOTAL_INTEREST
        TOTAL_INTEREST = tk.DoubleVar(self, value=np.nan)
        self.total_interest = ttk.Label(master=self,
                                        text="Total interest to be repaid: $",
                                        font=f"Calibri {TEXTSIZE}")
        self.total_interest_value = ttk.Label(master=self,
                                              textvariable=TOTAL_INTEREST,
                                              font=f"Calibri {TEXTSIZE}")

        # create the "Create Amortization Table" button. Makes a call to the AmortizationTable
        # class that was passed in when the DebtAPP was called in dashboard.py
        # You should also watch "Snow Society" on Netflix, it's in Spanish but it's got subtitles
        # and is dubbed and it's an amazing movie. You may decide to never get on a plane again though
        self.amortization_button = ttk.Button(master=self,
                                              text="Generate Amortization Table",
                                              command=lambda: [globals().update(data=a_table(LOAN_TYPE_VAR.get(),
                                                                                             LOAN_BALANCE.get(), INTEREST_PERCENTAGE.get(), TIME_REMAINING.get(),
                                                                                             MONTHLY_PAYMENT.get()))]
                                              )

        return

    def create_layout(self):
        """
        Creates the layout for all the output fields defined in the create_widgets

        Args:
            None

        Returns:
            None
        """
        # grid layout
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # place widgets
        # place the monthly payment amount
        self.monthly_payment_label.grid(row=0, column=0, pady=10, sticky='e')
        self.monthly_payment_value.grid(row=0, column=1, pady=10, sticky='w')

        # place the total repaid amount
        self.total_repaid.grid(row=1, column=0, pady=10, sticky='e')
        self.total_repaid_value.grid(row=1, column=1, pady=10, sticky='w')

        # place the total interest paid
        self.total_interest.grid(row=2, column=0, sticky='e', pady=10)
        self.total_interest_value.grid(row=2, column=1, sticky='w', pady=10)

        # place the creation of the amortization table button
        self.amortization_button.grid(
            row=3, columnspan=2, sticky='nsew', padx=10, pady=10)


class MiddleWindow(ttk.Frame):
    """
    This creates the primary window that contains the user interface. It is considered
    the "parent" window for all other elements in the application.

    Attributes:
    --------------------------------------------------------

    Methods:
    --------------------------------------------------------
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(pady=10, expand=True)

        ttk.Label(master=self,
                  text="Pay off your balance faster and pay less interest",
                  font=f"Calibri 18").pack()


class ExtraInputField(ttk.Frame):
    """
    This creates input fields at the bottom of the application, i.e. lump sum 
    payment and extra payments per month.
    How come we can feel something that touches the tip of our finger, but not the atom
    that is right next to the "last" atom on the tip of our finger ?

    Attributes:
    --------------------------------------------------------
        parent: parent window, i.e. this "smaller" input window needs to be placed inside 
        a larger window, which in this case is the MiddleWindow.

    Methods:
    --------------------------------------------------------
        __init__: calls for the creation of the widgets (which are the input fields) 
        and creates the layout (places the widgets)

        create_widgets: creates the variables and labels needed to show the text asking
        the user to provide the necessary input and input boxes where the user types
        in the values

        create_layout: creates the variables and labels needed to show the show the
        output of the calculations to the user.
    """

    def __init__(self, parent):

        # Layout setup
        super().__init__(parent)
        self.pack(side='left', pady=10)

        # Widgets
        self.create_widgets()
        # Place widgets
        self.create_layout()

    def create_widgets(self):
        """
        Creates the widgets, i.e. input fields, button and text prompts for the user

        Args:
            None

        Returns:
            None
        """
        self.lump_label = ttk.Label(master=self, text="What if you made a single lump-sum payment of $",
                                    font=f"Calibri {TEXTSIZE}")
        global LUMP_AMOUNT
        LUMP_AMOUNT = tk.DoubleVar(master=self)
        self.lump_entry = ttk.Entry(master=self, textvariable=LUMP_AMOUNT)
        self.lump_sign = ttk.Label(
            master=self, text="?", font=f"Calibri {TEXTSIZE}")

        self.extra_label = ttk.Label(
            master=self, text="What if you paid an additional $", font=f"Calibri {TEXTSIZE}")
        # Reading this source code may cause blindness... read at your own risk.
        global EXTRA_AMOUNT
        EXTRA_AMOUNT = tk.DoubleVar(master=self)
        self.extra_entry = ttk.Entry(master=self, textvariable=EXTRA_AMOUNT)
        self.extra_sign = ttk.Label(
            master=self, text="per month?", font=f"Calibri {TEXTSIZE}")

        return

    def create_layout(self):
        """
        Creates the layout for all the input fields defined in the create_widgets

        Args:
            None

        Returns:
            None
        """
        # grid layout
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # place widgets
        # place lump sum payment input field
        self.lump_label.grid(row=0, column=0, sticky='e', pady=10)
        self.lump_entry.grid(row=0, column=1, sticky='e', pady=10)
        self.lump_sign.grid(row=0, column=2, sticky='w', pady=10)

        # place extra monthly payment
        self.extra_label.grid(row=1, column=0, sticky='e', pady=10)
        self.extra_entry.grid(row=1, column=1, sticky='e', pady=10)
        self.extra_sign.grid(row=1, column=2, sticky='w', pady=10)

        return


class UpdatedPayment(ttk.Frame):
    """
    This creates the primary window that contains the user interface. It is considered
    the "parent" window for all other elements in the application.

    Attributes:
    --------------------------------------------------------

    Methods:
    --------------------------------------------------------
    """

    def __init__(self, parent):

        # Layout setup
        super().__init__(parent)
        self.pack(side='left', pady=10, fill='both', expand=True)

        # Widgets
        self.create_widgets()
        # Place widgets
        self.create_layout()

    def create_widgets(self):
        """
        Creates the widgets, i.e. output fields, button and text prompts for the user

        Args:
            None

        Returns:
            None
        """
        self.total_repaid = ttk.DoubleVar(master=self)
        self.total_repaid_var = ttk.Label(master=self,
                                          textvariable=self.total_repaid,
                                          font=f"Calibri {TEXTSIZE}")
        self.total_repaid_label = ttk.Label(master=self,
                                            text="Total amount to be repaid (with interest): $",
                                            font=f"Calibri {TEXTSIZE}")

        self.total_interest = ttk.DoubleVar(master=self)
        self.total_interest_var = ttk.Label(master=self,
                                            textvariable=self.total_interest,
                                            font=f"Calibri {TEXTSIZE}")
        self.total_interest_label = ttk.Label(master=self,
                                              text="Total interest to be repaid: $",
                                              font=f"Calibri {TEXTSIZE}")

        self.amount_saved = ttk.DoubleVar(master=self)
        self.amount_saved_var = ttk.Label(master=self,
                                          textvariable=self.amount_saved,
                                          font=f"Calibri {TEXTSIZE}")
        self.total_interest_saved = ttk.Label(master=self,
                                              text="You will have saved $",
                                              font=f"Calibri {TEXTSIZE}")

        self.min_payment = ttk.DoubleVar(master=self)
        self.min_payment_var = ttk.Label(master=self,
                                         textvariable=self.total_interest,
                                         font=f"Calibri {TEXTSIZE}")
        self.min_payment_label = ttk.Label(master=self, text="Minimum Monthly Payment:", background='light blue',
                                           font=f"Calibri {TEXTSIZE}")

        self.total_payment_label = ttk.Label(
            master=self, text="You could be paid off in ", font=f"Calibri {TEXTSIZE}")

        # Update payments button:
        self.update_payments_button = ttk.Button(master=self,
                                                 text="Update payments",
                                                 command=lambda: [data.update_payments(
                                                     LUMP_AMOUNT.get(), EXTRA_AMOUNT.get()),
                                                     self.total_repaid.set(
                                                         round(data.amortization_df['Payment amount'].sum(), 2)),
                                                     self.amount_saved.set(
                                                         round(TOTAL_REPAID.get()-self.total_repaid.get(), 2)),
                                                     self.total_interest.set(round(self.total_repaid.get()-data.loan_balance, 2))])

        # Halfway button
        self.halfway_var = ttk.StringVar(master=self)
        self.halfway_label = ttk.Label(master=self,
                                       textvariable=self.halfway_var,
                                       font=f"Calibri {TEXTSIZE}")
        self.halfway_button = ttk.Button(master=self,
                                         text="Halfway",
                                         command=lambda: [self.halfway_var.set(f"Halfway: {data.halfway()} month(s)")])

        # Principal button
        self.principal_var = ttk.StringVar(master=self)
        self.principal_label = ttk.Label(master=self,
                                         textvariable=self.principal_var,
                                         font=f"Calibri {TEXTSIZE}")
        self.principal_button = ttk.Button(master=self,
                                           text="Principal",
                                           command=lambda: [self.principal_var.set(f"More principal: {data.more_principal()}")])

    def create_layout(self):
        """
        Creates the layout for all the output fields defined in the create_widgets

        Args:
            None

        Returns:
            None
        """
        # grid layout
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        # If you like short series, watch "Le Visiteur du Futur" (The Visitor from the Future).
        # It's short sketches, a couple of minutes each that get progressively longer, that are
        # pretty funny (at least to me). It's worth watching just for Season 3 Episode 8 alone (don't
        # just jump to the episode directly as it won't hit the same if you don't watch the whole series).
        # https://www.youtube.com/@watchthevisitor/playlists
        # If you do watch it, yes I'm aware that Dr. Henry Castafolte and I look eeriely alike.

        # place widgets
        self.total_repaid_label.grid(row=0, column=0, pady=10, sticky='e')
        self.total_repaid_var.grid(row=0, column=1, pady=10, sticky='w')
        self.total_interest_label.grid(row=1, column=0, pady=10, sticky='e')
        self.total_interest_var.grid(row=1, column=1, pady=10, sticky='w')
        self.total_interest_saved.grid(row=2, column=0, sticky='e', pady=10)
        self.amount_saved_var.grid(row=2, column=1, sticky='w', pady=10)
        # Buttons:
        self.update_payments_button.grid(
            row=3, column=0, sticky='nsew', padx=10, pady=10)
        self.halfway_button.grid(
            row=3, column=1, sticky='nsew', padx=10, pady=10)
        self.principal_button.grid(
            row=3, column=2, sticky='nsew', padx=10, pady=10)
        # If you're this far in the code, stop and think about what you're doing
        # Output:
        self.halfway_label.grid(
            row=4, column=1, sticky='nsew', padx=10, pady=10)
        self.principal_label.grid(
            row=4, column=2, sticky='nsew', padx=10, pady=10)


if __name__ == "__main__":
    DebtAPP(AmortizationTable)
