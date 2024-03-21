import pandas as pd
import matplotlib.pyplot as plt
from mpltern.datasets import get_triangular_grid

def yukle_ve_donustur(dosya_yolu):
    # Veri yükleme ve numpy array'e dönüştürme
    df = pd.read_excel(dosya_yolu)
    veri_np = df.to_numpy()
    return veri_np.T  # Transpoze edilmiş array'i döndür

def ternary_plot_olustur(t, l, r, veri_listesi, etiketler, basliklar):
    fig = plt.figure()
    ax = fig.add_subplot(projection="ternary")
    ax.triplot(t, l, r, color='k', lw='0.2')
    
    for veri, etiket in zip(veri_listesi, etiketler):
        if 'curve' not in etiket:
            ax.scatter(*veri, alpha=0.5, label=etiket)
        if 'curve' in etiket:  # Eğer veri seti için eğri çizilecekse
            ax.plot(*veri, color='k', alpha=0.8, lw='1', label=f'curve for {etiket}')
    
    ax.set_tlabel(basliklar[0])
    ax.set_llabel(basliklar[1])
    ax.set_rlabel(basliklar[2])
    ax.legend()

# Triangular grid için veriler
t, l, r = get_triangular_grid()

# Verileri yükleme ve ayrıştırma
veri_np = yukle_ve_donustur("veriler.xlsx")
lab_veri_np = yukle_ve_donustur("labveri.xlsx")

# Ternary plot oluşturma
veri_listesi = [veri_np, lab_veri_np, veri_np]  # Üçüncü veri seti eğri için
etiketler = ['given data', 'lab data', 'curve for given data']
basliklar = ['Acetic acid (W/W,%)', 'Water \n(W/W,%)', 'Butyl acetate \n(W/W,%)']
ternary_plot_olustur(t, l, r, veri_listesi, etiketler, basliklar)

plt.show()