class Produto:
    def __init__(self,nome, categoria, quantidade, preco, preco_normal):
        self.nome = nome
        self.categoria =  categoria
        self.quantidade = quantidade
        self.preco = preco
        self.preco_normal = preco_normal
        
    def adicionar_produto(self):
        estoque = []
        estoque.append(self)
        print(f"Produto {self.nome} adicionado ao estoque.")

    def remover_produto(self):
       estoque.remove(self)
       print(f"Produto {self.nome} removido do estoque.")
       