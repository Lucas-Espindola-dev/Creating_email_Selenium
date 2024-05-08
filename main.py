from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# sheet selected to be worked with.
archive = load_workbook(filename='Relatorio.xlsx')
selected_sheet = archive['Dados_gerais_alunos_turma2']


