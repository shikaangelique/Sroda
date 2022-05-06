from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# def __init__(self, invoice_database_file='streak_database.csv'):
#     self.streak_database_file = streak_database_file
#     # self.streak_data = {}
#     self.streak = 0
#
#     try:
#         with open(self.streak_database_file, 'r') as streak_database:
#             for line in streak_database:
#                 self.streak += 1
#
#     except FileNotFoundError:
#         with open(self.streak_database_file, 'w') as streak_database:
#             self.streak += 0
#             pass
