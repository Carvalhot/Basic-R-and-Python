from scipy.stats import binom

#jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
prob = binom.pmf(3,5,0.5)

#passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde
#nenhuma, 1,2,3 ou 4 vezes seguidas.

binom.pmf(0,4,0.25)
binom.pmf(1,4,0.25)
binom.pmf(2,4,0.25)
binom.pmf(3,4,0.25)
binom.pmf(4,4,0.25)

#e se forem sinais de dois tempos?
binom.pmf(4,4,0.5)

#probabilidade acumulativa
binom.cdf(4,4,0.25)

#concurso com 12 questoes. Qual a probabilidade de acertar 7 questoes chutando todas?
binom.pmf(7,12,0.25) * 100
