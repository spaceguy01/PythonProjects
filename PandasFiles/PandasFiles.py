import pandas as pd

"""Reading CSV, JSON, XLSX, Comma TXT, Semi-Colon TXT Using Pandas"""

"""Using sample Supermarket File"""


""" Reading CSV Files """
csv_df = pd.read_csv('supermarkets.csv')
csv_df.set_index('ID')


""" Reading JSON Files """
json_df = pd.read_json('supermarkets.json')
json_df.set_index('ID')


""" Reading EXCEL Files """
xlsx_df = pd.read_excel('supermarkets.xlsx', sheet_name =0)
xlsx_df.set_index('ID')


""" Reading Comma Separated Text Files """
commatxt_df = pd.read_csv('supermarkets-commas.txt')
commatxt_df.set_index('ID')


"""Reading Semi-Colon Separated Text Files """
semicolon_df = pd.read_csv('supermarkets-semi-colons.txt', sep=";")
semicolon_df.set_index('ID')
