import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp, ks_2samp, cramervonmises_2samp, mannwhitneyu
from hyppo.ksample import MMD

chat_id = 532761772 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
   pval = MMD(compute_kernel="rbf", gamma=1).test(x, y)[1]
   return pval < 0.05
