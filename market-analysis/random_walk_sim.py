import numpy as np
import matplotlib.pyplot as plt

def simulate_stock_price(start_price:float, days: int, volatility:float) -> np.ndarray: 
    """
    :param start_price: Başlangıç fiyatı
    :param days: Simüle edilecek gün sayısı
    :param volatility: Günlük değişim şidetti (Standart Sapma)
    """

    dt = 1
    
    price = np.zeros(days)
    price[0] = start_price
    
    for t in range(1, days):
        shock = np.random.randn() * volatility
        price[t] = price[t - 1] + shock

    return price

start_price = 100
days = 365
volatility = 1.5

series = simulate_stock_price(start_price, days, volatility)

plt.figure(figsize=(10, 6))
plt.plot(series, label="Simule Edilmis Hisse Fiyati", color='blue', linewidth=1.5)
plt.title("Random Walk Hipotezi: Piyasa Similasyonu", fontsize=14)
plt.xlabel('Gunler')
plt.ylabel('Fiyat')
plt.axhline(y=start_price, color='r', linestyle='--', label='Baslangic Fiyati')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()