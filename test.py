from expense import Expense as plt
import pandas as pd
#import csv

f = open('expenses.csv', 'r').read()

word = pd.read_csv('expense.py')
plt.bar(word.name, word.category, word.amount)
