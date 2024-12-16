# Declaração 
nome_completo = "Luiz Otávio Miranda"

nome_completo_aspas_tripla = """Luiz
Otávio
Miranda"""

nome_completo_quebra = "Luiz \
Otávio Miranda"

nome = "Luiz"
sobrenome = "Otávio Miranda"

# Formatações 
print("Nome completo (1° forma):", nome_completo)
print("Nome completo (2° forma):" + nome_completo)
print("Nome completo (3° forma):" + "Luiz" + "Otávio" + "Miranda")
print("Nome completo (4° forma):" + "Luiz", "Otávio", "Miranda")
print("Nome completo (5° forma):", nome_completo_aspas_tripla)
print("Nome completo (6° forma):", nome_completo_quebra)
print("Nome completo (7° forma): %s" % nome_completo)
print("Nome completo (8° forma): %s %s" % (nome, sobrenome))
print(f"Nome Completo (9° forma): {nome} {sobrenome}")
print("Nome completo (10° forma): {} {}".format(nome, sobrenome))