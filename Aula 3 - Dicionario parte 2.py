clientesShopping = {
    'Cliente Bobs': {

    },
    "Cliente BK": {
        "Cliente1": {
            "Nome": "Kauê",
            "Sobrenome": "Luiz de Borba",
            "CPF": "015.202.434-62",
        },
        "Cliente2": {
            "Nome": "Miguel",
            "Sobrenome": "de Jesuis",
            "CPF": "110.202.442-62"
        },

    },
    "Cliente MeC": {
        "Cliente1": {
            "Nome": "Miguel",
            "Sobrenome": "de Jesuis",
            "CPF": "110.202.442-62"
        }
    }
}
## Iterando o dicionario
for clientes_k, clientes_v in clientesShopping.items():
    print(f'Exibindo {clientes_k}:')
    print()
    for v, k in clientes_v.items():
        for cliente_chave, clientes_valor in k.items():
            print(f'{cliente_chave} = {clientes_valor}')
        print()
