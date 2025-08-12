# Titanic Survival Classifier (scikit-learn)

Basit ama öğretici bir makine öğrenmesi projesi: Iris veri seti üzerinde sınıflandırma. Kod: `classifer.py`  

## 🚀 Özellikler
- Titanic veri setini yükler
- Eğitim/test ayrımı yapar
- Bir sınıflandırma modeli ile eğitir (ör. Logistic Regression / Random Forest)
- Doğruluk (accuracy) ve karışıklık matrisi (confusion matrix) raporlar
- (Opsiyonel) Basit görselleştirmeler üretir

## 📦 Gereksinimler
```
Python 3.10+   ⚠️
numpy
pandas
scikit-learn
matplotlib      (opsiyonel)
seaborn         (opsiyonel)
```

Kurulum:
```bash
# Proje kök dizininde
pip install -r requirements.txt
# requirements.txt yoksa:
pip install numpy pandas scikit-learn matplotlib seaborn
```

## ▶️ Çalıştırma
```bash
cd irisFlower
python classifer.py    # veya classifier.py
```

İsteğe bağlı argümanlar eklediyseniz (örnek):
```bash
python classifier.py --model random_forest --test-size 0.2 --random-state 42
```

## 📊 Çıktı / Değerlendirme
- Accuracy: **⚠️ örn. 0.96**
- Confusion Matrix: konsola yazdırılır veya `outputs/` klasörüne kaydedilir
- (Opsiyonel) Grafikler `figures/` klasörüne kaydedilir

## 📁 Proje Yapısı
```
Machine-Learning-Projects/
└─ irisFlower/
   ├─ classifer.py           # ana betik  ⚠️ (classifier.py olarak düzeltilebilir)
   ├─ README.md              # bu dosya
   ├─ requirements.txt       # (opsiyonel)
   └─ figures/               # (opsiyonel: çıktı görselleri)
```

## 🔬 Yeniden Üretilebilirlik
- Sabit bir `random_state`/`seed` kullanın (⚠️ örn. 42)
- Python ve paket sürümlerinizi belirtin
- Eğitim/test oranını README’de yazın (⚠️ örn. test_size=0.2)

## 🧪 Notlar
- Model hiperparametrelerini dosya içinden veya CLI argümanlarıyla değiştirebilirsiniz.
- Karışıklık matrisi ve sınıflandırma raporu (precision/recall/F1) eklemek için:
  ```python
  from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
  print("Accuracy:", accuracy_score(y_test, y_pred))
  print(confusion_matrix(y_test, y_pred))
  print(classification_report(y_test, y_pred, target_names=clf.classes_.astype(str)))
  ```

## 📚 Kaynaklar
- UCI Iris Dataset
- scikit-learn Kullanım Kılavuzu

