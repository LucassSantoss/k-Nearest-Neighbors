# Feito por: Bruno Mascioli de Souza e Lucas Pereira dos Santos
import math
from random import choice

def ler_exemplares():
  matriz = []
  arquivo = open('iris.data.csv', 'r')
  for linha in arquivo:
    dados = linha.strip().split(',')
    matriz.append(dados)
  arquivo.close()
  return matriz[1:]


def ler_sem_classificacao(nome_arquivo):
  matriz = []
  arquivo = open(nome_arquivo, 'r')
  for linha in arquivo:
    dados = linha.strip().split(',')
    matriz.append(dados)
  arquivo.close()
  return matriz

def distancia_euclidiana(exemplo, nao_classificados):
  distancia = math.sqrt(((exemplo[0]) - (nao_classificados[0]))**2 +
                            ((exemplo[1]) - (nao_classificados[1]))**2 +
                            ((exemplo[2]) - (nao_classificados[2]))**2 +
                            ((exemplo[3]) - (nao_classificados[3]))**2)
  return distancia

def calculo_distancias(matriz_exemplares, matriz_sem_classificacao, k):
  matriz = []
  for nao_classificados in matriz_sem_classificacao:
    distancias = []
    nao_classificados = list(map(float, nao_classificados))
    for exemplo in matriz_exemplares:
      especie = exemplo[4]
      exemplo = list(map(float, exemplo[:-1]))
      distancia = distancia_euclidiana(exemplo, nao_classificados)
      distancias.append([distancia, especie, nao_classificados])
    distancias_ordenadas = sorted(distancias)
    matriz.append(distancias_ordenadas[:k])
  return matriz


def determina_classe(matriz):
  arquivo = open('iris.data.csv', 'a')
  for especie_sem_classificacao in matriz:
    setosa, versicolor, virginica = 0, 0, 0
    for pontos in especie_sem_classificacao:
      if pontos[1] == 'setosa':
        setosa += 1
      elif pontos[1] == 'versicolor':
        versicolor += 1
      else:
        virginica += 1
    arquivo.write('\n')
    for elem in especie_sem_classificacao[0][2]:
      elem = str(elem)
      arquivo.write(elem)
      arquivo.write(',')
    #Casos em que existe um valor maior
    if setosa > versicolor and setosa > virginica:
      arquivo.write('setosa')
      print(especie_sem_classificacao[0][2], 'setosa')
    elif versicolor > setosa and versicolor > virginica:
      arquivo.write('versicolor')
      print(especie_sem_classificacao[0][2], 'versicolor')
    elif virginica > setosa and virginica > versicolor:
      arquivo.write('virginica')
      print(especie_sem_classificacao[0][2], 'virginica')
    #Casos de valores iguais
    #todas iguais
    elif virginica == versicolor == setosa:
      sorteio = choice(['virginica','setosa', 'versicolor'])
      arquivo.write(sorteio)
      print(especie_sem_classificacao[0][2], sorteio)
      #virginica = versicolor
    elif virginica == versicolor > setosa:
      sorteio = choice(['virginica','versicolor'])
      arquivo.write(sorteio)
      print(especie_sem_classificacao[0][2], sorteio)
      #virginica = setosa
    elif virginica == setosa > versicolor:
      sorteio = choice(['virginica','setosa'])
      arquivo.write(sorteio)
      print(especie_sem_classificacao[0][2], sorteio)
      #setosa = versicolor
    else:
      sorteio = choice(['setosa', 'versicolor'])
      arquivo.write(sorteio)
      print(especie_sem_classificacao[0][2], sorteio)
  arquivo.close()


def main():
  k = int(input('K: '))
  nome_arquivo = input('Nome do arquivo de dados não classificados: ')
  matriz_exemplares = ler_exemplares()
  matriz_sem_classificacao = ler_sem_classificacao(nome_arquivo)
  matriz = calculo_distancias(matriz_exemplares, matriz_sem_classificacao, k)
  determina_classe(matriz)


main()
