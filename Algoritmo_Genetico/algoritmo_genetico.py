
from random import randint
from math import sqrt
from random import randint, random

objetivo = (50,50)


num_individuos = 20
num_genes = 8
probabilidade_mutacao = 0.4
def iniciarIndividuos(num_individuos, num_genes):
    individuos = []

    for i in range(num_individuos):
        posicao_inicial = [randint(0,5), randint(0,5)]
        cromossomo = []

        for j in range(num_genes):
            gene = [randint(-2,2), randint(-2,2)]  
            cromossomo.append(gene)

        individuo = {
            "posicao": posicao_inicial,
            "cromossomo": cromossomo
        }

        individuos.append(individuo)

    return individuos

def executar_genes(populacao, objetivo):
    for individuo in populacao:
        pos_atual = individuo["posicao"].copy()

        for gene in individuo["cromossomo"]:
            pos_atual[0] += gene[0]
            pos_atual[1] += gene[1]

        individuo["posicao_final"] = pos_atual
        individuo["fitness"] = round(sqrt((objetivo[0] - pos_atual[0])**2 + (objetivo[1] - pos_atual[1])**2),3)
    return populacao


def melhores(populacao):
    melhor1 = populacao[0]
    melhor2 = populacao[1]
    for i in populacao:
        if i["fitness"] < melhor1["fitness"]:
            melhor1 = i
    for i in populacao:
        if i["fitness"] > melhor1["fitness"] and i["fitness"] < melhor2["fitness"] and i["fitness"] != melhor1["fitness"] :
            melhor2 = i

    melhores_pop = [melhor1,melhor2]
    return melhores_pop





def populacao_nova(melhores):
    individuos_novos = []
    for i in range(num_individuos-2):
       cromossomo_novo = []
       for j in range(num_genes):
           if j < num_genes*0.80:
               gene_novo = melhores[0]["cromossomo"][j].copy()
               if random() <= 0.1:
                    gene_novo[0] += randint(-1,1)  
                    gene_novo[1] += randint(-1,1)
                    cromossomo_novo.append(gene_novo)
               else:
                   cromossomo_novo.append(gene_novo)
                   
           else:
               gene_novo = melhores[1]["cromossomo"][j].copy()
               
               if random() <= 0.1:
                    gene_novo[0] += randint(-1,1)  
                    gene_novo[1] += randint(-1,1)
                    cromossomo_novo.append(gene_novo)
               else:
                   cromossomo_novo.append(gene_novo)


       individuos = {"posicao": melhores[0]["posicao"].copy(), 
                     "cromossomo": cromossomo_novo}

       individuos_novos.append(individuos)
    return individuos_novos + melhores


populacao = iniciarIndividuos(num_individuos,num_genes)
g = 0
for i in range(50):

    populacao = executar_genes(populacao,objetivo)
    print(f"População {g}:\n")
    
    g += 1
    


    melhores12 = melhores(populacao)
    print(melhores12[0]["fitness"], melhores12[1]["fitness"])

    populacao = populacao_nova(melhores12) + melhores12

