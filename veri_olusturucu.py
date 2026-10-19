import pandas as pd
import numpy as np

def veri_seti_uret(satir_sayisi=2000): # Veriyi 2000 satıra çıkardım ki model daha iyi öğrensin
    np.random.seed(42)
    
    # Genişletilmiş Bitki Listesi
    bitkiler = [
        "Domates", "Biber", "Çilek", "Lavanta", "Kaktüs", 
        "Mısır", "Ayçiçeği", "Gül", "Orkide", "Zeytin Ağacı"
    ]
    
    # Bitkilere özel su katsayıları (Örn: Kaktüs çok az, Gül orta, Domates yüksek)
    # Bu katsayılar modelin bitki türünü gerçekten "anlamasını" sağlayacak
    su_katsayilari = {
        0: 15, 1: 12, 2: 10, 3: 5, 4: 2, 
        5: 18, 6: 14, 7: 13, 8: 7, 9: 4
    }
    
    bitki_kodlari = np.random.randint(0, len(bitkiler), satir_sayisi)
    
    data = {
        'sicaklik': np.random.uniform(10, 45, satir_sayisi), # Sıcaklık aralığını genişlettim
        'nem': np.random.uniform(5, 95, satir_sayisi),       # Nem aralığını genişlettim [cite: 8]
        'isik': np.random.randint(0, 3, satir_sayisi),      # [cite: 9]
        'bitki_turu_kod': bitki_kodlari
    }
    
    df = pd.DataFrame(data)
    
    # Gelişmiş Su Miktarı Formülü
    # Her satırın bitki koduna göre su katsayısını alıyoruz
    df['katsayi'] = df['bitki_turu_kod'].map(su_katsayilari)
    
    # Formül: (Sıcaklık * 1.2) - (Nem * 0.4) + (Işık * 8) + Bitki Özel Katsayısı
    df['su_miktari'] = (df['sicaklik'] * 1.2) - (df['nem'] * 0.4) + (df['isik'] * 8) + df['katsayi'] + 10
    
    df['su_miktari'] = df['su_miktari'].clip(lower=0) # Negatif değerleri engelle
    df = df.drop(columns=['katsayi']) # Yardımcı sütunu siliyoruz
    
    df.to_csv("bitki_verisi.csv", index=False)
    print(f"✅ {len(bitkiler)} farklı bitki türü içeren {satir_sayisi} satırlık veri seti hazır!")

veri_seti_uret()