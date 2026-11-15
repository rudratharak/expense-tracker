import json

exp=[]
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

def save_expense(exp):
  with open("expense.json","w") as f:
    json.dump(exp,f)
  

#menu 

choices = {
  '1': add_expense,
  '2': view_expense,
}

while True :
  pick=input("1.add\n2.view\n3.exit\n")
  if pick == '3':
    break
  if pick in choices:
    choices[pick](exp)
  else:
    print("select any one of the number 1,2 or 3")
    
