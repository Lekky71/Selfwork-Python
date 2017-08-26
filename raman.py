class CashBook:
    date = ''
    particulars = ''
    folio = ''
    cash = 0
    bank = 0

    def __init__(self, date, particulars, folio, cash, bank):
        self.date = date
        self.particulars = particulars
        self.folio = folio
        self.cash = cash
        self.bank = bank

    def getCash(self):
        return cash


number_of_entries = input("how many entries do you want to enter? ")
total_cashbook_debit = [CashBook]
total_cashbook_credit = [CashBook]
sum = 0
for i in range(0, number_of_entries):
    date = str(raw_input("Enter the date "))
    particulars = str(raw_input("Enter the particulars "))
    folio = str(raw_input("Enter the folio "))
    cash = int(raw_input("Enter the amount "))
    bank = int(raw_input("Enter the amount of cheque "))
    cashier = CashBook(date, particulars, folio, cash, bank)
    choice = input("Is this [1]Debit or [2]Credit or [3]Folio ")
    if choice == 1:
        total_cashbook_debit.append(cashier)
    if choice == 2:
        total_cashbook_credit.append(cashier)
    if choice == 3:
        total_cashbook_debit.append(cashier)
        total_cashbook_credit.append(cashier)
for i in range(0, total_cashbook_debit.__len__()):
    sum += total_cashbook_debit[i].cash
print sum
