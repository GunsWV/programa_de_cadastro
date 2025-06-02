numeros = [1,2,3,4,5]
nomes = ["Larissa","Gustavo","Caio","Filipe"]

#print(numeros)
#print(nomes)
def mostra_linha():

    """Mostra uma linha de separação"""
    print('-' * 50)

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

mostra_linha()

nomes[0] = "João" #estava Larissa
nomes[1] = "Pedro" #estava Gustavo
nomes[2] = "Yuri" #estava Caio
nomes[3] = "Manuella" #estava Filipe

print(nomes[0]) #alterado para João
print(nomes[1]) #alterado para Pedro
print(nomes[2]) #alterado para Yuri
print(nomes[3]) #alterado para Manuella

mostra_linha()

#esta linha adiciona um nome no final da lista
nomes.append("Beatriz")
nomes.append("Enzo")

print(nomes[0]) 
print(nomes[1]) 
print(nomes[2]) 
print(nomes[3])
print(nomes[4])
print(nomes[5])

print(nomes)

mostra_linha()

#adicionar elementos em qualquer posição da lista, substituindo o elemento anterior

nomes.insert(1, "Fernanda") #insere "Fernanda" na posição 1
print("Após insert:", nomes)

mostra_linha()

#Modificando elementos
nomes[2] = "Paulo" #Modifica o elemento índice 2
print("Após modificação:", nomes)

mostra_linha()

#Removendo elementos

del nomes[3] #Remove o elemento no índice 3
print("Ápos del:", nomes)

nomes.remove("Enzo") #Remove a primeira ocorrência de "Enzo"
print("Ápos remove:", nomes)

removido = nomes.pop(2) #Remove e retorna o elemento no índice 2
print(f"Ápos pop (removido '{removido}'):", nomes)

nomes.clear() #Esvazia a lista
print("Ápos clear:", nomes)

