import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
print('Média: {0}'.format(np.mean(jogadores)))
print('Mediana: {0}'.format(np.median(jogadores)))
print('Desvio Padrão: {0}'.format(np.std(jogadores, ddof=1)))

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])
print (quartis)

stats.describe(jogadores)
