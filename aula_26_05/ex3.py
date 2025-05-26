class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

p1 = produto("morango:",4.00, 1000)
p2 = produto("melancia:", 10.00, 1200)


print(p1.nome, p1.preco, p1.quantidade)  
print(p2.nome, p2.preco, p2.quantidade) 