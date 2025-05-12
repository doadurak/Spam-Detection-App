# 📧 Spam Tespit Web Uygulaması - 222803021 Turkan Doğa Durak

Bu proje, e-postaların spam olup olmadığını tahmin eden bir **makine öğrenmesi modeli** ve ona entegre edilmiş bir **Streamlit tabanlı web arayüzü** sunar. Kullanıcıdan alınan çeşitli e-posta özelliklerine göre model, mesajın spam olup olmadığını sınıflandırır.

---

## 🎯 Projenin Amacı

- Gerçek hayattaki basit e-posta verileri üzerinden bir sınıflandırma modeli oluşturmak
- Bu modeli `.joblib` dosyası olarak kaydedip yeniden kullanılabilir hale getirmek
- Kullanıcıların doğrudan giriş yapabileceği sade bir web arayüzü geliştirmek

---

## 🚀 Web Uygulamasında Neler Var?

**Streamlit Arayüzü ile:**
- Kullanıcıdan e-posta ile ilgili 4 özellik alınır:
  - Kelime sayısı
  - Özel karakter sayısı
  - Link içerip içermediği
  - Spam kelime sayısı
- Model bu girdilere göre spam olup olmadığını anında tahmin eder

---

## 🧠 Kullanılan Teknolojiler

- Python 3.x
- pandas, numpy, scikit-learn
- joblib (model kaydı)
- **Streamlit** (web arayüz)
- Jupyter Notebook (model eğitimi ve analiz)

---

## ⚙️ Uygulamayı Çalıştırma

### Jupyter Notebook için:
```bash
jupyter notebook algoritma.ipynb

### Web Arayüzü
streamlit run app.py

Gerekli kurulumlar:
pip install -r requirements.txt

