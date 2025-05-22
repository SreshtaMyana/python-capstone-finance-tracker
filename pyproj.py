'''
Code for the Capstone project: Personal Finance Tracker
'''

#welcome message
print("Welcome to the Personal Finance Tracker!")

#view expenses method
def view_expenses(data):
    for cat in data:
        print(f'Category: {cat}')
        for tu in data[cat]:
            print(f' - {tu[0]}: {tu[1]}')
        
#view summary method
def view_summary(data):
    print('Summary: ')
    for cat in data:
        val = 0
        for t in data[cat]:
            val += t[1]
        print(f'{cat}: {val}')

exp_data = {} #initializing the dictionary for exp
while True:
    act = int(input('What would you like to do? \
    1. Add Expense \
    2. View All Expenses \
    3. View Summary \
    4. Exit'))
    
    try:
        if act == 1:
            Expense_description = input('Enter expense description: ').strip()
            Category = input('Enter category: ').strip()
            #formatting the category string for ease of storage and adding
            Category = Category[0].upper() + Category[1:].lower()
            amount = float(input('Enter amount: '))
            try:
                if Category in exp_data:
                    exp_data[Category].append((Expense_description, amount))
                else:
                    exp_data[Category] = [(Expense_description, amount)]
                print('Expense added successfully.')
            except ValueError:
                print('Please enter only numbers for amount')
            except AttributeError:
                print('Please enter values for expense description and category.')
            except:
                print('Some error occured, please try again!')
        elif act == 2:
            view_expenses(exp_data)
        elif act == 3:
            view_summary(exp_data)
        elif act == 4:
            break
        else:
            print('Try again!')
    except:
        print('Please try again!')


    
    