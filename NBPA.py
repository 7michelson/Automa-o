import numpy as np
import matplotlib.pyplot as plt
import obspy as oy 
import warnings
warnings.filterwarnings("ignore")

def Grafico(time_hhz, tr, i, flag):
    plt.figure(figsize=(24, 6))
    plt.title('Componente HHZ')
    plt.grid()
    plt.plot(time_hhz, tr, 'k')
    plt.ylabel("Amplitude", fontsize=9)
    plt.xlabel('segundos')
    if flag == True:
        plt.suptitle(f'Gráficos do sinal filtrado {i}:00h', fontsize=15)
        plt.savefig(f'Gráficos_NBPA/Sinal filtrado {i}-00h')
    elif flag == False:
        plt.suptitle(f'Gráficos do sinal Puro {i}:00h', fontsize=15)
        plt.savefig(f'Gráficos_NBPA/Sinal puro {i}-00h')
        
def leitura(i): # 1 - 9 horas 
    st_HHZ = oy.read(f'NBPA/NB.NBPA..HHZ.D.2022.160.0{i}5959.sac_vel')
    st_HHZ_D = st_HHZ.copy()
    #st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 4, dspline=3600)
    time_hhz = st_HHZ_D[0].times()
    tr = st_HHZ_D[0].data
    Grafico(time_hhz, tr, i, False)
    return st_HHZ_D

def Leitura(i): # 10 - 23 horas
    st_HHZ = oy.read(f'NBPA/NB.NBPA..HHZ.D.2022.160.{i}5959.sac_vel')
    st_HHZ_D = st_HHZ.copy()
    #st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 2, dspline=3600)
    time_hhz = st_HHZ_D[0].times()
    tr = st_HHZ_D[0].data
    flag = False
    Grafico(time_hhz, tr, i, flag)
    return st_HHZ_D

def filtro(i):
    if i <=9:
        st_HHZ = oy.read(f'NBPA/NB.NBPA..HHZ.D.2022.160.0{i}5959.sac_vel')
        st_HHZ_D = st_HHZ.copy()
        st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=3600)
        st_HHZ_D[0].filter('bandpass', freqmin=1/6, freqmax=1/4)
        st_HHZ_D[0].filter('bandpass', freqmin=1/14, freqmax=1/10)
        st_HHZ_D[0].taper(max_percentage=0.5, type='hann', max_length=None, side='both')
        time_hhz = st_HHZ_D[0].times()
        tr = st_HHZ_D[0].data
        Grafico(time_hhz, tr, i, True)
    
    elif i>9:
        st_HHZ = oy.read(f'NBPA/NB.NBPA..HHZ.D.2022.160.{i}5959.sac_vel')
        st_HHZ_D = st_HHZ.copy()
        st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=3600)
        st_HHZ_D[0].filter('bandpass', freqmin=1/6, freqmax=1/4)
        st_HHZ_D[0].filter('bandpass', freqmin=1/14, freqmax=1/10)
        st_HHZ_D[0].taper(max_percentage=0.005, type='hann', max_length=None, side='both')
        time_hhz = st_HHZ_D[0].times()
        tr = st_HHZ_D[0].data
        Grafico(time_hhz, tr, i, True)
           
i = 0
for i in range(0, 10):
    leitura(i)
for i in range(10, 24):
    Leitura(i)
for i in range(0, 24):    
    filtro(i)