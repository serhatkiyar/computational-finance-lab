import hashlib
import time

class TradingSignalMap():

    def __init__(self):
        self.signal_map = {}

    def update_signal(self, symbol: str, score: float, side: str):
        
        signal_data = {
            'score' : score, # Örn: 85.5 (RSI, Momentum vb.)
            'side' : side,   # Örn: 'LONG', 'SHORT', 'FLAT'
            'timestamp' : time.time()
        }
        
        self.signal_map[symbol] = signal_data
        print(f"[Update] {symbol} sinyal guncellendi. | Yon {side} | Skor {score}")

    def get_signal(self, symbol: str):
        
        if symbol in self.signal_map:
            data = self.signal_map[symbol]
            return data
        else:
            return None
        
    def _debug_hash_function(self, symbol: str):
        """
        Cormen Teorik Analizi:
        Python'un soyutladığı 'Hash Fonksiyonu' mantığını görselleştirmek için.
        Gerçekte bellekte nereye gittiğini simüle eder.
        """
        # SHA256 ile string'i matematiksel bir değere çeviriyoruz
        hash_val = hashlib.sha256(symbol.encode()).hexdigest()

        # İlk 8 karakteri adresmis gibi düşünelim
        return hash_val[:8]
    
if __name__ == "__main__":
    
    # 1. Hafızayı Başlat
    market_memory = TradingSignalMap()

    # 2. Sinyalleri İşle (Veri Akışı)
    # Bot piyasayı tarıyor ve hafızaya yazıyor
    market_memory.update_signal("BTCUSDT", 92.5, "LONG")
    market_memory.update_signal("ETHUSDT", 45.0, "NEUTRAL")
    market_memory.update_signal("SOLOUSDT", 88.0, "LONG")


    # 3. Lookup (Sorgu) Performansı
    # Bot işlem açmak için BTC'nin durumunu soruyor
    target = "BTCUSDT"
    signal = market_memory.get_signal(target)

    if signal:
        print(f"Bulunan Sinyal ({target}):")
        print(f"  -> Yön: {signal['side']}")
        print(f"  -> Skor: {signal['score']}")
    else:
        print(f"{target} için sinyal yok.")



# 4. _________________________________Cormen Teorik Gösterim______________________________________________________
    print("\n--- Cormen: Under The Hood (Hash Map Mantığı) ---")
    print(f"Key: 'BTCUSDT' -> Hash Function -> Address: {market_memory._debug_hash_function('BTCUSDT')}")
    print(f"Key: 'ETHUSDT' -> Hash Function -> Address: {market_memory._debug_hash_function('ETHUSDT')}")
