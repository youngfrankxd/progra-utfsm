'''
# CASO 1
>>> ingredientes(2, 'omelette')
{'huevos': 4, 'leche': 20, 'margarina': 30, 'sal': 2}
>>> ingredientes(3, 'te con leche')
{'leche': 30, 'azucar': 30, 'te': 3}

# FIN CASO 1

# CASO 2
>>> numero_de_porciones('omelette', inventario)
6
>>> numero_de_porciones('pan con queso', inventario)
4

# FIN CASO 2

# CASO 3
>>> cocinar_juntos([(2, 'omelette'), (2, 'te con leche')],
...                dict(inventario))
True
>>> cocinar_juntos([(1, 'omelette con queso'),
...                 (1, 'pan con queso'),
...                 (500, 'vaso de leche')], dict(inventario))
False

# FIN CASO 3
'''

# INVENTARIO
inventario = {
   'huevos': 12, 	# unidades
   'leche': 500, 	# ml
   'papas': 3, 		# unidades
   'margarina': 200, 	# gr
   'azucar': 200,	# gr
   'sal': 50, 		# gr
   'queso': 4, 		# rebanadas
   'pan': 12, 		# rebanadas
   'te': 5, 		# bolsas
   # ...
}
# FIN INVENTARIO

# RECETAS
recetas = {
   'omelette': [(2, 'huevos'), (15, 'margarina'),
                (1, 'sal'),    (10, 'leche')],
   'omelette con queso': [(2, 'huevos'), (10, 'margarina'),
                          (2, 'queso'),  (10, 'leche')],
   'pan con queso': [(2, 'pan'), (5, 'margarina'), (1, 'queso')],
   'te con leche':  [(1, 'te'), (10, 'leche'), (10, 'azucar')],
   'vaso de leche': [(500, 'leche')],
   # ...
}
# FIN RECETAS

