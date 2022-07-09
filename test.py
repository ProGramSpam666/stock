import numpy as np
from fundamental import stockDate
from volatility import VolatilityIndicators
from fundamental import Fundamental
from investigation import Investigation
import matplotlib.pyplot as plt



vol = VolatilityIndicators()
fun = Fundamental()
inv = Investigation()



def test():
    dates = fun.getDate('GME')
    volit = vol.getVol_ST('GME')
    plt.plot(dates, volit, 'r')
    plt.show()
    return 
print(test())




