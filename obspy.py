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
    plt.ylabel("Amplitude m/s", fontsize= 19)
    plt.xlabel('segundos s', fontsize= 19)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    if flag == True:
        plt.suptitle(f'Gráficos do sinal filtrado {i}:00h ', fontsize=15)
        plt.savefig(f'filt_Natal/NATLS_HHZ Sinal filtrado 0{i}_00.PNG')
    elif flag == False:
        plt.suptitle(f'Gráficos do sinal Puro {i}:00h', fontsize=15)
        plt.savefig(f'Puro_Natal/NATLS_HHZ Sinal puro {i}_00 H.PNG')
        
def leitura(i): # 0 - 9 horas
    st_HHZ = oy.read(f'NATLS/LS.NATLS..HHZ.D.2022.160.0{i}0000.sac_vel')
    st_HHZ_D = st_HHZ.copy()
    #st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=36000)
    time_hhz = st_HHZ_D[0].times()
    tr = st_HHZ_D[0].data
    Grafico(time_hhz, tr, i, False)
    
def Leitura(i): # 10 - 23 horas
    st_HHZ = oy.read(f'NATLS/LS.NATLS..HHZ.D.2022.160.{i}0000.sac_vel')
    st_HHZ_D = st_HHZ.copy()
    """st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 32, dspline=36000)"""
    time_hhz = st_HHZ_D[0].times()
    tr = st_HHZ_D[0].data
    Grafico(time_hhz, tr, i, False)
    
def filtro(i):
    if i <=9:
        st_HHZ = oy.read(f'NATLS/LS.NATLS..HHZ.D.2022.160.0{i}0000.sac_vel')
        st_HHZ_D = st_HHZ.copy()
        st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=36000)
        st_HHZ_D[0].filter('bandpass', freqmin=1/8, freqmax=1/4)
        st_HHZ_D[0].filter('bandpass', freqmin=1/16, freqmax=1/12)
        st_HHZ_D[0].taper(max_percentage=0.05, type='hann', max_length=None, side='both')
        time_hhz = st_HHZ_D[0].times()
        tr = st_HHZ_D[0].data
        Grafico(time_hhz, tr, i, True)
    elif i>9:
        st_HHZ = oy.read(f'NATLS/LS.NATLS..HHZ.D.2022.160.{i}0000.sac_vel')
        st_HHZ_D = st_HHZ.copy() 
        st_HHZ_D[0] = st_HHZ_D[0].detrend('spline', order = 3, dspline=36000)
        st_HHZ_D[0].filter('bandpass', freqmin=1/8, freqmax=1/4)
        st_HHZ_D[0].filter('bandpass', freqmin=1/16, freqmax=1/12)
        st_HHZ_D[0].taper(max_percentage=0.05, type='hann', max_length=None, side='both')
        time_hhz = st_HHZ_D[0].times()
        tr = st_HHZ_D[0].data
        Grafico(time_hhz, tr, i, True)
i = 0
for i in range(5, 6):
    leitura(i)
for i in range(10, 24):
    Leitura(i)
for i in range(0, 24):    
    filtro(i) 
