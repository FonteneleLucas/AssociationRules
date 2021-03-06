from efficient_apriori import apriori

columns = ["SP_Length: ", "SP_Width: ", "PT_Legth: ", "PT_Width: ", "Class: "]
# columns = ["ID: ", "idade: ", "disturbios_visao: ", "astigmatico: ", "taxa_lagrimas: ", "Classe: "]

import csv

f = open('iris.csv', 'r').read()

dataList = [line.split(',') for line in f.split('\n') if line]

# print(dataList)

items = []


for i in range(len(dataList)):
    item = []
    for j in range(len(columns)):
        item.append(columns[j]+str(dataList[i][j]))

    items.append(item)

# print(items)

itemsets, rules = apriori(items, min_support=0.0, min_confidence=0.01)

rules_rhs = filter(lambda rule: len(rule.lhs) <= 2 and len(rule.rhs) == 2 , rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
  print(rule)



"""
    1) Baixar do Repositório de Dados UCI Machine Learning os datasets "Lenses" e "Iris"
    2) Realizar a extração de Regras de Associação de cada um dos datasets de 3 formas
        2.1) Todas as regras possíveis com minsup=0.1 e minconf=0.2
        2.2) Regras de tamanho 2, ou seja 1 elemento no antecedente e 1 no consequente da regra, com minsup=0.0 e minconf=0.01
        2.3) Regras com antecedente de tamanho 1 ou 2 e consequente de tamanho 2, com minsup=0.0 e minconf=0.01
"""