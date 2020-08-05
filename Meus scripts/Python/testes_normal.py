from scipy import stats
from scipy.stats import norm
import matplotlib.pylot as plt

dados = norm.rvs(size = 100)
stats.probplot(dados, plot = plt)

stats.shapiro(dados)
