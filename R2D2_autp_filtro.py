import numpy as np
import matplotlib.pyplot as plt
import obspy as oy 
import warnings
warnings.filterwarnings("ignore")

def Grafico(time_hhz, tr, i, flag):
    plt.figure(figsize=(32, 8))
    plt.title('HHZ', fontsize=15)
    plt.grid()
    plt.plot(time_hhz, tr, 'k')
    plt.ylabel("Amplitude m/s", fontsize= 19)
    plt.xlabel('segundos s', fontsize= 19)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    if flag == True:
        plt.suptitle(f'R2D2 Sinal filtrado {i}', fontsize=15)
        plt.savefig(f'Gráficos hhz/R2D2_HHZ Sinal filtrado {i}.PNG')
    elif flag == False:
        plt.suptitle(f'R2D2 sinal Puro {i}', fontsize=15)
        plt.savefig(f'Gráficos hhz/R2D2_HHZ Sinal puro {i}.PNG')
        
def leitura(i): # 293 - 306 horas
    st_HHZ = oy.read(f'HHZ.D/LS.R2D2..HHZ.D.2022.{i}')
    st_HHZ_D = st_HHZ.copy()
    st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=(3600*24))
    time_hhz = st_HHZ_D[0].times()
    tr = st_HHZ_D[0].data
    Grafico(time_hhz, tr, i, False)
        
def filtro(i):
    st_HHZ = oy.read(f'HHZ.D/LS.R2D2..HHZ.D.2022.{i}')
    st_HHZ_D = st_HHZ.copy()
    st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=(3600*24))
    st_HHZ_D[0].filter('bandpass', freqmin=1/8, freqmax=1/4)
    st_HHZ_D[0].filter('bandpass', freqmin=1/16, freqmax=1/12)
    st_HHZ_D[0].taper(max_percentage=0.05, type='hann', max_length=None, side='both')
    time_hhz = st_HHZ_D[0].times()
    tr = st_HHZ_D[0].data
    Grafico(time_hhz, tr, i, True)
    
i = 0
"""for i in range(293, 306):
    leitura(i)"""
for i in range(293, 306):    
    filtro(i) 
