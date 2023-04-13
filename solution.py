import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp, ks_2samp, cramervonmises_2samp, mannwhitneyu

chat_id = 532761772 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
   return cramervonmises_2samp(x, y).pvalue < 0.05 # Ваш ответ, True или False
