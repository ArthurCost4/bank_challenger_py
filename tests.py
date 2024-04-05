def criar_gerador():
    contador = 1

    def gerar_id():
        nonlocal contador
        id_unico = str(contador).zfill(4)
        contador += 1
        return id_unico

    return gerar_id

# Criando um gerador de IDs
gerar_id = criar_gerador()

# Gerando IDs únicos
print("ID do usuário:", gerar_id())  # Saída: 0001
print("ID do usuário:", gerar_id())  # Saída: 0002
print("ID do usuário:", gerar_id())  # Saída: 0003
