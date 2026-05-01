from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QTableWidgetItem, 
                             QApplication, QMessageBox, QFileDialog)
from ui_raporlar import Ui_MainWindow
import os
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush, QColor
from PySide6.QtCore import Qt, QDate
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=150): # DPI 150 netlik için idealdir
        # tight_layout grafiklerin çerçeveye tam oturmasını sağlar
        self.fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi, tight_layout=True)
        super(MplCanvas, self).__init__(self.fig)

class RaporEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=.\SQLEXPRESS05;' 
            r'DATABASE=spor_salonu;'
            r'Trusted_Connection=yes;'
        )

        # Başlangıç tarihleri (Filtreleme için)
        if hasattr(self.ui, 'date_baslangic'):
            self.ui.date_baslangic.setDate(QDate.currentDate().addMonths(-1))
            self.ui.date_bitis.setDate(QDate.currentDate())
            self.ui.btn_filtrele.clicked.connect(self.grafikleri_guncelle)

        # Dışa aktarma butonu bağlantısı
        if hasattr(self.ui, 'btn_pdf_aktar'):
            self.ui.btn_pdf_aktar.clicked.connect(self.raporu_pdf_kaydet)

      
        # İlk yükleme
        self.grafikleri_hazirla()
        self.borclu_uyeleri_getir()
        self.arizali_ekipmanlari_getir()
        self.arka_plan_ayarla()
        self.ui.btn_disa_aktar.clicked.connect(self.sadece_grafigi_kaydet)
        self.ui.btn_excel_aktar.clicked.connect(self.borclulari_excele_aktar)
        self.hesapla_ve_guncelle()
        self.riskli_uyeler()
        self.ciz_antrenor_performans()
        self.kritik_stok_kontrol()
        self.ciz_kantin_kar_analizi()
        self.hedef_analizi_ciz()
        
    def veritabanı_sorgula(self, query):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            conn.close()
            return data
        except Exception as e:
            print(f"SQL Hatası: {e}")
            return []

    def ciz_kantin_kar_analizi(self):
        try:
            # SQL: 'Kantin' kategorisindeki Gelir ve Gider toplamlarını ayrı ayrı alıyoruz
            sorgu = """
                SELECT islemTuru, SUM(miktar) 
                FROM kasa 
                WHERE kategori = 'Kantin' 
                GROUP BY islemTuru
            """
            veriler = self.veritabanı_sorgula(sorgu)

            # --- HATA ÇÖZÜMÜ: Canvas nesnesi yoksa oluştur ---
            if not hasattr(self, 'canvas_kantin'):
                # widget_kantin_analiz senin Qt Designer'da verdiğin isimdir
                self.layout_kantin = QVBoxLayout(self.ui.widget_kantin_analiz)
                self.canvas_kantin = MplCanvas(self) # MplCanvas sınıfının tanımlı olduğunu varsayıyoruz
                self.layout_kantin.addWidget(self.canvas_kantin)

            self.canvas_kantin.axes.clear()
            
            if veriler:
                # v[0] = islemTuru (Gelir/Gider), v[1] = miktar
                turler = [v[0] for v in veriler]
                miktarlar = [float(v[1]) for v in veriler]
                
                # Gelir Yeşil (#2ecc71), Gider Kırmızı (#e74c3c)
                renkler = ['#2ecc71' if t == 'Gelir' else '#e74c3c' for t in turler]
                
                self.canvas_kantin.axes.pie(
                    miktarlar, 
                    labels=turler, 
                    autopct='%1.1f%%', 
                    colors=renkler,
                    startangle=140,
                    wedgeprops=dict(width=0.4, edgecolor='#2b2b36')
                )
                self.canvas_kantin.axes.set_title("Kantin Nakit Akışı (Gelir vs Gider)", color='white')
            else:
                self.canvas_kantin.axes.text(0.5, 0.5, 'Veri Bulunamadı', color='white', ha='center')
            
            self.canvas_kantin.fig.patch.set_facecolor('#2b2b36')
            self.canvas_kantin.axes.set_facecolor('#2b2b36')
            self.canvas_kantin.draw()
            
        except Exception as e:
            print(f"Grafik Hatası: {e}")

    def hedef_analizi_ciz(self, hedef_ciro=50000):
        try:
            # Mevcut ciroyu çek
            sorgu = "SELECT SUM(miktar) FROM kasa WHERE islemTuru = 'Gelir' AND MONTH(islemTarihi) = MONTH(GETDATE())"
            mevcut_ciro = float(self.veritabanı_sorgula(sorgu)[0][0] or 0)
            
            yuzde = (mevcut_ciro / hedef_ciro) * 100
            if yuzde > 100: yuzde = 100 # %100'ü aşarsa taşmasın

            if not hasattr(self, 'canvas_hedef'):
                self.layout_hedef = QVBoxLayout(self.ui.widget_hedef_analiz)
                self.canvas_hedef = MplCanvas(self)
                self.layout_hedef.addWidget(self.canvas_hedef)

            self.canvas_hedef.axes.clear()
            
            # Gauge tasarımı (Yarım daire şeklinde)
            self.canvas_hedef.axes.pie([yuzde, 100-yuzde], colors=['#f39c12', '#34495e'], 
                                       startangle=180, counterclock=False, 
                                       wedgeprops=dict(width=0.4, edgecolor='#2b2b36'))
            
            # Orta kısma yüzdeyi yazalım
            self.canvas_hedef.axes.text(0, -0.2, f"%{yuzde:.1f}", ha='center', va='center', 
                                        fontsize=20, fontweight='bold', color='white')
            self.canvas_hedef.axes.set_title(f"Aylık Hedef: {hedef_ciro} TL", color='white', pad=20)
            
            self.canvas_hedef.fig.patch.set_facecolor('#2b2b36')
            self.canvas_hedef.draw()
            
        except Exception as e:
            print(f"Hedef Grafiği Hatası: {e}")

    def ciz_antrenor_performans(self):
        try:
            # 1. Veriyi Çek
            sorgu = """
                SELECT a.antrenor_Adi, COUNT(ud.uyeID) 
                FROM antrenorler a
                LEFT JOIN dersler d ON a.antrenor_id = d.antrenorId
                LEFT JOIN uyeDers ud ON d.dersID = ud.dersID
                GROUP BY a.antrenor_Adi
            """
            veriler = self.veritabanı_sorgula(sorgu)

            # 2. Canvas Hazırlığı (Tab 6'daki widget'ı kullandığını varsayalım)
            # Eğer yeni bir widget eklediysen ismini ona göre güncelle
            if not hasattr(self, 'canvas_antrenor'):
                self.layout_antrenor = QVBoxLayout(self.ui.widget_antrenor_analiz)
                self.canvas_antrenor = MplCanvas(self)
                self.layout_antrenor.addWidget(self.canvas_antrenor)

            self.canvas_antrenor.axes.clear()
            
            if veriler:
                hocalar = [v[0] for v in veriler]
                ogrenci_sayilari = [int(v[1]) for v in veriler]
                
                # Görselleştirme
                bars = self.canvas_antrenor.axes.barh(hocalar, ogrenci_sayilari, color='#556ee6')
                
                # Değerleri çubukların ucuna yazalım
                for bar in bars:
                    width = bar.get_width()
                    self.canvas_antrenor.axes.text(width + 0.3, bar.get_y() + bar.get_height()/2, 
                                                  f'{int(width)} Üye', va='center', fontweight='bold', color='white')

                self.canvas_antrenor.axes.set_title("Antrenör Üye Yükü Analizi", color='white', fontweight='bold')
                self.canvas_antrenor.axes.tick_params(axis='both', colors='white')
            
            self.canvas_antrenor.fig.patch.set_facecolor('#2b2b36')
            self.canvas_antrenor.axes.set_facecolor('#2b2b36')
            self.canvas_antrenor.draw()

        except Exception as e:
            print(f"Antrenör Analiz Hatası: {e}")

    def kritik_stok_kontrol(self):
        # Stok adedi, kritik seviyenin altına düşenleri bul
        sorgu = "SELECT urunAd, stokAdedi, kritikSeviye FROM stoklar WHERE stokAdedi <= kritikSeviye"
        kritik_urunler = self.veritabanı_sorgula(sorgu)
        
        # UI'daki tableWidget_stok tablosunu doldur
        self.ui.tableWidget_stok.setRowCount(0)
        for i, row in enumerate(kritik_urunler):
            self.ui.tableWidget_stok.insertRow(i)
            # Ürün adı
            self.ui.tableWidget_stok.setItem(i, 0, QTableWidgetItem(row[0]))
            # Kalan miktar (Kırmızı vurgu)
            item = QTableWidgetItem(f"{row[1]} ADET")
            item.setForeground(QBrush(QColor("red")))
            self.ui.tableWidget_stok.setItem(i, 1, item)
            kritik_deger = str(row[2]) if row[2] is not None else "Belirlenmedi"
            self.ui.tableWidget_stok.setItem(i, 2, QTableWidgetItem(kritik_deger+" ADET"))

    def hesapla_ve_guncelle(self):
        """Churn oranını hesaplar ve UI bileşenlerini günceller."""
        import pyodbc # Fonksiyon içinde tekrar import etmek bazen kapsama sorununu çözer
        
        try:
            # 1. Veritabanı işlemleri
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            
            # Riskli üye sorgusu
            cursor.execute("""
                SELECT COUNT(*) FROM (
                    SELECT u.uyeID FROM uyeler u
                    LEFT JOIN girisCikisKayitlari g ON u.uyeID = g.uyeId
                    WHERE u.durum = 'Aktif'
                    GROUP BY u.uyeID
                    HAVING DATEDIFF(day, MAX(g.giriszamani), GETDATE()) > 15 
                      
                ) as Riskli""")
            riskli_sayisi = cursor.fetchone()[0]
            
            # Toplam aktif üye sorgusu
            cursor.execute("SELECT COUNT(*) FROM uyeler WHERE durum = 'Aktif'")
            toplam_aktif = cursor.fetchone()[0]
            
            cursor.close()
            conn.close()

            # 2. Oran ve Metin Hazırlama
            if toplam_aktif > 0:
                oran = int((riskli_sayisi / toplam_aktif) * 100)
                metin = f"{toplam_aktif} aktif üyeden {riskli_sayisi} üye risk altında."
            else:
                oran = 0
                metin = "Sistemde aktif üye bulunamadı."

            # 3. Arayüzü GÜVENLİ Güncelleme
            # Önce Label'ı değiştirelim (Eğer burada hata alırsan isim yanlıştır)
            try:
                self.ui.lbl_detay.setText(metin)
                print(f"Label güncellendi: {metin}")
            except AttributeError:
                print("HATA: 'lbl_churn_detay' isminde bir label bulunamadı! Designer'daki ismini kontrol et.")

            # Sonra Progress Bar'ı değiştirelim
            try:
                self.ui.progressBar.setRange(0, 100)
                self.ui.progressBar.setValue(oran)
                print(f"Progress Bar güncellendi: %{oran}")
            except AttributeError:
                print("HATA: 'progressBar' isminde bir nesne bulunamadı!")

            # 4. Renk Ayarı
            renk = "#2ecc71" # Yeşil
            if oran >= 25: renk = "#e74c3c" # Kırmızı
            elif oran >= 10: renk = "#f1c40f" # Sarı

            self.ui.progressBar.setStyleSheet(f"QProgressBar::chunk {{ background-color: {renk}; }}")
            
            # Ekranın anında güncellenmesini zorla
            QApplication.processEvents()

        except Exception as e:
            print(f"VERİTABANI VEYA HESAPLAMA HATASI: {e}")

    def riskli_uyeler(self):
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    u.ad + ' ' + u.soyad as AdSoyad,
                    u.telefon,
                    ISNULL(CONVERT(VARCHAR, MAX(g.giriszamani), 104), 'Kayıt Yok') as SonGiris
                FROM uyeler u
                LEFT JOIN girisCikisKayitlari g ON u.uyeID = g.uyeId
                WHERE u.durum = 'Aktif'
                GROUP BY u.uyeID, u.ad, u.soyad, u.telefon
                HAVING DATEDIFF(day, MAX(g.giriszamani), GETDATE()) > 15 
                  
                ORDER BY MAX(g.giriszamani) ASC -- En uzun süredir gelmeyenden başla
            """)
            riskli_liste = cursor.fetchall()
            cursor.close()

            # UI'daki tabloyu doldurma (Tablonun adını ui dosyana göre kontrol et)
            if hasattr(self.ui, 'tableWidget_riskli'): # Örn: tableWidget_riskli
                self.ui.tableWidget_riskli.setRowCount(0) # Eski verileri temizle
                self.ui.tableWidget_riskli.setColumnCount(3)
                self.ui.tableWidget_riskli.setHorizontalHeaderLabels(["Ad Soyad", "Telefon", "Son Giriş"])
                
                for row_number, row_data in enumerate(riskli_liste):
                    self.ui.tableWidget_riskli.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.ui.tableWidget_riskli.setItem(row_number, column_number, item)
                
                # Sütunları içeriğe göre genişlet
                self.ui.tableWidget_riskli.resizeColumnsToContents()

    def borclu_uyeleri_getir(self):
        sorgu = "SELECT ad, soyad, telefon, toplamBorc FROM uyeler WHERE toplamBorc > 0 ORDER BY toplamBorc DESC"
        veriler = self.veritabanı_sorgula(sorgu)
        
        self.ui.tableWidget_borclular.setRowCount(0)
        for row_number, row_data in enumerate(veriler):
            self.ui.tableWidget_borclular.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                if column_number == 3: # Borç sütunu
                    item.setForeground(QBrush(QColor("red")))
                    item.setText(f"{float(data):,.2f} TL")
                self.ui.tableWidget_borclular.setItem(row_number, column_number, item)

    def arizali_ekipmanlari_getir(self):
        # Eğer UI'da tableWidget_ekipman varsa çalışır
        if not hasattr(self.ui, 'tableWidget_ekipman'): return
        
        sorgu = "SELECT ekipmanAdi, durum, sonBakimTarihi FROM ekipmanlar WHERE durum != 'Aktif'"
        veriler = self.veritabanı_sorgula(sorgu)
        
        self.ui.tableWidget_ekipman.setRowCount(0)
        for row_number, row_data in enumerate(veriler):
            self.ui.tableWidget_ekipman.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_ekipman.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def grafikleri_hazirla(self):
        if not self.ui.widget_gelir_2.layout():
            self.layout_gelir = QVBoxLayout(self.ui.widget_gelir_2)
        else:
            self.layout_gelir = self.ui.widget_gelir_2.layout()
            
        self.canvas_gelir = MplCanvas(self)
        self.layout_gelir.addWidget(self.canvas_gelir)
        
        # Üyelik Pasta Alanı
        self.layout_pasta = QVBoxLayout(self.ui.widget_pasta)
        self.canvas_pasta = MplCanvas(self)
        self.layout_pasta.addWidget(self.canvas_pasta)

        # Doluluk Analizi
        self.layout_doluluk = QVBoxLayout(self.ui.widget_doluluk_analiz)
        self.canvas_doluluk = MplCanvas(self)
        self.layout_doluluk.addWidget(self.canvas_doluluk)

        self.grafikleri_guncelle()
    def grafikleri_guncelle(self):
        # Tarih filtrelerini al (Varsa)
        bas = self.ui.date_baslangic.date().toString("yyyy-MM-dd") if hasattr(self.ui, 'date_baslangic') else "2000-01-01"
        bit = self.ui.date_bitis.date().toString("yyyy-MM-dd") if hasattr(self.ui, 'date_bitis') else "2099-12-31"

        self.ciz_gelir_gider(self.canvas_gelir, bas, bit)
        self.ciz_uyelik_dagilimi(self.canvas_pasta)
        self.ciz_doluluk_analizi(self.canvas_doluluk)

    def ciz_gelir_gider(self, canvas, bas, bit):
        try:
            # 1. SQL Sorgusu
            sorgu = "SELECT islemTuru, SUM(miktar) FROM kasa GROUP BY islemTuru"
            veriler = self.veritabanı_sorgula(sorgu)

            # 2. Canvas Eksenini Temizle (Artık self.canvas_gelir üzerinden gidiyoruz)
            canvas.axes.clear() 
            
            if veriler:
                labels = [v[0] for v in veriler]
                values = [float(v[1]) for v in veriler]
                
                # Renkler
                colors = ['#2ecc71' if l == 'Gelir' else '#e74c3c' for l in labels]
                
                # 3. Donut Chart Çizimi
                wedges, texts, autotexts = canvas.axes.pie(
                    values, 
                    labels=labels, 
                    autopct='%1.1f%%', 
                    startangle=90, 
                    colors=colors,
                    pctdistance=0.75,
                    explode=[0.05] * len(labels),
                    wedgeprops=dict(width=0.4, edgecolor='#1e1e27') # UI rengiyle uyumlu kenarlık
                )

                plt.setp(autotexts, size=10, weight="bold", color="white")
                plt.setp(texts, size=12, weight="bold", color="white")

                # Merkeze Net Durumu Yaz
                toplam_net = sum([v if l == 'Gelir' else -v for l, v in zip(labels, values)])
                canvas.axes.text(0, 0, f'Net Durum\n{toplam_net:,.0f} TL', 
                                 ha='center', va='center', fontsize=10, fontweight='bold', color='#34c38f')
                
                canvas.axes.set_title("Genel Mali Durum Analizi", pad=20, fontsize=14, fontweight='bold', color='white')
            else:
                canvas.axes.text(0.5, 0.5, 'Veritabanında İşlem Kaydı Yok', 
                                 ha='center', va='center', color='white')

            # Arka planı UI ile uyumlu yapalım
            canvas.fig.patch.set_facecolor('#2b2b36')
            canvas.axes.set_facecolor('#2b2b36')
            canvas.draw()

        except Exception as e:
            print(f"Kasa Özeti Çizim Hatası: {e}")
    def ciz_uyelik_dagilimi(self, canvas):
        sorgu = "SELECT t.tipAdi, COUNT(u.uyeID) FROM uyeler u JOIN uyelik_tipleri t ON u.uyelikTipiID = t.uyeliktipiID GROUP BY t.tipAdi"
        veriler = self.veritabanı_sorgula(sorgu)
        
        canvas.axes.cla()
        if veriler:
            labels = [v[0] for v in veriler]
            sizes = [int(v[1]) for v in veriler]
            colors = ['#3498db', '#f1c40f', '#e67e22', '#9b59b6']
            
            # Pasta grafiğini çiz (Donut efekti için wedgeprops kullanıldı)
            wedges, texts, autotexts = canvas.axes.pie(
                sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
                colors=colors, pctdistance=0.85, wedgeprops=dict(width=0.4, edgecolor='w')
            )
            
            # Yazı fontlarını ayarla (Detay 3)
            plt.setp(autotexts, size=10, weight="bold", color="white")
            plt.setp(texts, size=11)
            
            # Yan tarafa lejant ekle (Detay 4)
            canvas.axes.legend(wedges, labels, title="Paketler", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            
        canvas.axes.set_title("Üyelik Tipi Dağılım Analizi", fontsize=12, fontweight='bold')
        canvas.draw()
    

    def ciz_doluluk_analizi(self, canvas):
        sorgu = "SELECT DATEPART(HOUR, giriszamani), COUNT(*) FROM girisCikisKayitlari GROUP BY DATEPART(HOUR, giriszamani)"
        veriler = self.veritabanı_sorgula(sorgu)
        
        saatler = [int(v[0]) for v in veriler]
        sayilar = [int(v[1]) for v in veriler]

        canvas.axes.cla()
        # Gradient/Yumuşak çizgi grafiği
        canvas.axes.plot(saatler, sayilar, marker='o', color='#3498db', linewidth=2, label='Üye Sayısı')
        canvas.axes.fill_between(saatler, sayilar, color='#3498db', alpha=0.2) # Altını doldur
        
        # Detaylandırma
        canvas.axes.set_title("Saatlik Salon Yoğunluğu", fontsize=12, fontweight='bold')
        canvas.axes.set_xlabel("Saat")
        canvas.axes.grid(True, linestyle='--', alpha=0.5)
        canvas.axes.set_xticks(range(6, 24)) # 06:00 - 23:00 arası saatler
        
        canvas.draw()
    def raporu_disa_aktar(self):
        # Kullanıcıya dosya kaydetme penceresi aç (Varsayılan isim: Fitness_Rapor.png)
        dosya_yolu, secilen_filtre = QFileDialog.getSaveFileName(
            self, 
            "Raporu Kaydet", 
            "Fitness_Rapor.png", 
            "PNG Image (*.png);;PDF Files (*.pdf);;All Files (*)"
        )

        if dosya_yolu:
            try:
                # Sadece grafikleri değil, tüm pencerenin ekran görüntüsünü alır
                # Bu yöntemle tablolar ve grafikler bir bütün olarak kaydedilir
                ekran_goruntusu = self.grab()
                ekran_goruntusu.save(dosya_yolu)
                
                QMessageBox.information(self, "Başarılı", f"Rapor başarıyla kaydedildi:\n{dosya_yolu}")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Rapor kaydedilirken bir hata oluştu: {str(e)}")

    def sadece_grafigi_kaydet(self):
        try:
            # 1. Kontrol: Canvas tanımlı mı?
            if hasattr(self, 'canvas_gelir'):
                # Kullanıcıya nereye kaydetmek istediğini soralım (Hata payını düşürür)
                dosya_yolu, _ = QFileDialog.getSaveFileName(
                    self, "Grafiği Kaydet", "Gelir_Analizi.pdf", "PDF Files (*.pdf);;PNG Images (*.png)"
                )
                
                if dosya_yolu:
                    # 2. Kayıt işlemi: dpi=300 netlik sağlar
                    self.canvas_gelir.fig.savefig(dosya_yolu, dpi=300, bbox_inches='tight')
                    QMessageBox.information(self, "Başarılı", "Grafik yüksek çözünürlükte kaydedildi.")
            else:
                QMessageBox.warning(self, "Hata", "Grafik nesnesi bulunamadı!")
                
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Kaydedilirken bir sorun oluştu: {str(e)}")
   
    def borclulari_excele_aktar(self):
        try:
            # 1. Veritabanından veriyi çek
            sorgu = "SELECT ad, soyad, telefon, toplamBorc FROM uyeler WHERE toplamBorc > 0 ORDER BY toplamBorc DESC"
            veriler = self.veritabanı_sorgula(sorgu)

            if not veriler:
                QMessageBox.warning(self, "Uyarı", "Aktarılacak borçlu üye bulunamadı.")
                return

            # 2. Dosya kaydetme penceresini aç
            dosya_yolu, _ = QFileDialog.getSaveFileName(
                self, "Excel Olarak Kaydet", "Borclu_Uyeler_Listesi.xlsx", "Excel Files (*.xlsx)"
            )

            if dosya_yolu:
                # 3. Veriyi Pandas DataFrame'e dönüştür
                df = pd.DataFrame([list(row) for row in veriler], 
                                columns=["Ad", "Soyad", "Telefon", "Toplam Borç"])

                # 4. Excel dosyasına yaz
                df.to_excel(dosya_yolu, index=False)
                
                QMessageBox.information(self, "Başarılı", f"Liste Excel'e aktarıldı:\n{dosya_yolu}")

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Excel aktarımı sırasında hata oluştu: {str(e)}")
    
    def arka_plan_ayarla(self):
        resim_yolu = r"C:\Users\yigit\OneDrive\Belgeler\fitness\indir.png"
        if os.path.exists(resim_yolu):
            oImage = QPixmap(resim_yolu)
            sImage = oImage.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)

    def resizeEvent(self, event):
        self.arka_plan_ayarla()
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = RaporEkrani()
    pencere.show()
    sys.exit(app.exec())