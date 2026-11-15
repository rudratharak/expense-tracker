# Expense Tracker

A simple command-line expense tracker written in Python.

## Features

- Add an expense: amount, what it was spent on, date, optional description
- View all expenses
- Save expenses to `expense.json`
- Menu built with a dictionary that maps each choice to a function
- Input check: a wrong amount (letters) does not crash the program

## How to run

Requires Python 3.

```
python main.py
```

Menu:

```
1.add
2.view
3.exit
```

## Project structure

- `main.py` - the program
- `expense.json` - saved data (created when you add an expense; ignored by git)

## Planned

- Load saved expenses when the program starts
- Delete and edit an expense
- Total spending and filter by date or category
