# Sistema simples de caixa - Hamburgueria

print("=== Hamburgueria - Caixa ===")
cliente = input("Nome do cliente: ").strip()

# Lê saldo aceitando vírgula ou ponto
saldo_str = input("Saldo do cliente (R$): ").strip().replace(",", ".")
try:
    saldo = float(saldo_str)
except ValueError:
    print("Saldo inválido. Use números, ex.: 35.50")
    raise SystemExit

# Cardápio (3 produtos)
produtos = {
    "1": ("X-Burger", 18.50),
    "2": ("Batata Frita", 9.00),
    "3": ("Refrigerante (lata)", 7.00),
}

print("\n--- Cardápio ---")
print("1. X-Burger ............ R$ 18,50")
print("2. Batata Frita ........ R$  9,00")
print("3. Refrigerante (lata).. R$  7,00")

opcao = input("Escolha o número do produto: ").strip()
if opcao not in produtos:
    print("Opção inválida.")
    raise SystemExit

produto, preco_unit = produtos[opcao]

# Quantidade
try:
    qtd = int(input("Quantidade: ").strip())
    if qtd <= 0:
        print("Quantidade deve ser um inteiro positivo.")
        raise SystemExit
except ValueError:
    print("Quantidade inválida. Digite um número inteiro.")
    raise SystemExit

# Cálculo do total
total = preco_unit * qtd

print("\n--- Resumo ---")
print(f"Cliente: {cliente}")
print(f"Produto: {produto} x{qtd} (R$ {preco_unit:.2f} cada)")
print(f"Total a pagar: R$ {total:.2f}")
print(f"Saldo disponível: R$ {saldo:.2f}")

# Verificação de pagamento com if
if saldo >= total:
    saldo -= total
    print("\nPagamento aprovado! ✅")
    print(f"Saldo final: R$ {saldo:.2f}")
else:
    falta = total - saldo
    print("\nSaldo insuficiente. ❌")
    print(f"Faltam R$ {falta:.2f} para concluir a compra.")
    print(f"Saldo suficiente: R$ {saldo:.2f}")
