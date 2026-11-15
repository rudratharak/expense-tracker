import json
import os

def add_():
    try:
      amount=float(input("enter the amount spent:"))
    except ValueError:
      print("Enter a number:")
      return None
    on=input("enter the amount spent on:")
    date=input("enter the date:")
    description=input("enter the description(optional):")
    if description == '':
         description="nothing"
    dit = {
        "amount_spent":amount,
        "spent_on":on,
        "date":date,
        "description":description
    }
    return dit 

def add_expense(exp):
   E=add_()
   if E is not None:
    exp.append(E)
    save_expense(exp)
   return None

def view_expense(exp1):
    for i in exp1:
        print(f"Amount:{i['amount_spent']}\non:{i['spent_on']}\ndate:{i['date']}\ndescription:{i['description']}")
    return None

def delete_expense(exp):
    if not exp:
        print("No expenses to delete")
        return None
    for n,i in enumerate(exp,1):
        print(f"{n}.{i['amount_spent']} on {i['spent_on']} ({i['date']})")
    try:
        num = int(input("Enter a Number to delete:"))
    except ValueError:
        print("Enter a number")
        return None
    if num<1 or num>len(exp):
        print("NO expense with that number")
        return None
    removed = exp.pop(num - 1)
    save_expense(exp)
    print(f"Deleted: {removed['spent_on']} ({removed['amount_spent']})")
    
def save_expense(exp):
  with open("expense.json","w") as f:
    json.dump(exp,f)

def load_expenses():
    if os.path.exists("expense.json"):
        with open("expense.json","r") as f:
            return json.load(f)
    return []

exp = load_expenses()
#menu 

choices = {
  '1': add_expense,
  '2': view_expense,
  '3': delete_expense,
}

while True :
  pick=input("1.add\n2.view\n3.delete\n4.exit\n")
  if pick == '4':
    break
  if pick in choices:
    choices[pick](exp)
  else:
    print("select any one of the number 1,2,3 or 4")
    
