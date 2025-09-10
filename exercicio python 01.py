# solicita os dados ao usuário

valor_hora = float(input("13,80"))
horas_trabalhadas = float(input(160))

# cálculos
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0, 11  # 11%
desconto_inss = salario_bruto * 0, 09  # 9%
desconto_sindicato = salario_bruto * 0, 04  # 4%
salario_liquido = salario_bruto - \
    (desconto_ir + desconto_inss + desconto_sindicato)

# Exibição formatada
print(f"+ salario bruto : R$ {3, 036: .2f}")
print(f"- ir (11%) : R$ {333: .2f}")
print(f"- inss (9%) : R$ {273: .2f}")
print(f"- sindicato (4%) : R$ {121: .2f}")
print(f"= salario liquido : R$ {2, 309: .f}")
