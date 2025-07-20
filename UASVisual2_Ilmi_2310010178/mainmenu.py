import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mahasiswa0178 import Ui_MainWindow  # hasil convert dari Qt Designer

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Tombol navigasi
        self.ui.pushButton.clicked.connect(self.show_page_data)      
        self.ui.pushButton_2.clicked.connect(self.show_page_nilai)   
        self.ui.pushButton_9.clicked.connect(self.go_to_beranda)     
        self.ui.pushButton_07.clicked.connect(self.go_to_beranda)   
        self.ui.pushButton_6.clicked.connect(self.load_data_mhs)     
        self.ui.tableWidget.cellClicked.connect(self.tampil_ke_field)
        self.ui.pushButton_8.clicked.connect(self.tambah_data_mhs)
        self.ui.pushButton_3.clicked.connect(self.ubah_data_mhs)
        self.ui.pushButton_4.clicked.connect(self.hapus_data_mhs)
        self.ui.pushButton_7.clicked.connect(self.bersihkan_field)
        self.ui.pushButton_5.clicked.connect(self.clear_table_widget)
        self.ui.pushButton_06.clicked.connect(self.load_data_nilai)
        self.ui.tableWidget_4.cellClicked.connect(self.isi_field_nilai)
        self.ui.pushButton_01.clicked.connect(self.tambah_data_nilai)
        self.ui.pushButton_02.clicked.connect(self.ubah_data_nilai)
        self.ui.pushButton_03.clicked.connect(self.hapus_data_nilai)
        self.ui.pushButton_04.clicked.connect(self.bersihkan_field_nilai)
        self.ui.pushButton_05.clicked.connect(self.clear_table_nilai)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageBeranda)







    def go_to_beranda(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageBeranda)

    def show_page_data(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageData)

    def show_page_nilai(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageNilai)


    def load_data_mhs(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM mhs")
            result = cursor.fetchall()

            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(9)
            self.ui.tableWidget.setHorizontalHeaderLabels([
                "NPM", "Nama Lengkap", "Nama Panggilan", "No HP",
                "Email", "Kelas", "MATKUL", "Prodi", "Lokasi Kampus"
            ])

            for row_idx, row_data in enumerate(result):
                for col_idx, col_data in enumerate(row_data):
                    self.ui.tableWidget.setItem(
                        row_idx, col_idx, QTableWidgetItem(str(col_data))
                    )

            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print("Gagal mengambil data dari database:", e)

    def tampil_ke_field(self, row, column):
        self.ui.lineEdit.setText(self.ui.tableWidget.item(row, 0).text())   # NPM
        self.ui.lineEdit_2.setText(self.ui.tableWidget.item(row, 1).text()) # Nama Lengkap
        self.ui.lineEdit_3.setText(self.ui.tableWidget.item(row, 2).text()) # Nama Panggilan
        self.ui.lineEdit_4.setText(self.ui.tableWidget.item(row, 3).text()) # No HP
        self.ui.lineEdit_5.setText(self.ui.tableWidget.item(row, 4).text()) # Email
        self.ui.lineEdit_6.setText(self.ui.tableWidget.item(row, 5).text()) # Kelas
        self.ui.lineEdit_7.setText(self.ui.tableWidget.item(row, 6).text())# MATKUL
        self.ui.lineEdit_8.setText(self.ui.tableWidget.item(row, 7).text())# Prodi
        self.ui.lineEdit_9.setText(self.ui.tableWidget.item(row, 8).text())# Lokasi Kampus
    def tambah_data_mhs(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            cursor = conn.cursor()

            query = """
                INSERT INTO mhs (npm, nama_l, nama_p, no_hp, email, kelas, matkul, prodi, lokasi)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                self.ui.lineEdit.text(),
                self.ui.lineEdit_2.text(),
                self.ui.lineEdit_3.text(),
                self.ui.lineEdit_4.text(),
                self.ui.lineEdit_5.text(),
                self.ui.lineEdit_6.text(),
                self.ui.lineEdit_7.text(),
                self.ui.lineEdit_8.text(),
                self.ui.lineEdit_9.text(),
            )
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()

            self.load_data_mhs()  # refresh table
        except mysql.connector.Error as e:
            print("Gagal menambah data:", e)
    def ubah_data_mhs(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            cursor = conn.cursor()

            query = """
                UPDATE mhs SET 
                    nama_l=%s, nama_p=%s, no_hp=%s, email=%s,
                    kelas=%s, matkul=%s, prodi=%s, lokasi=%s
                WHERE npm=%s
            """
            data = (
                self.ui.lineEdit_2.text(),
                self.ui.lineEdit_3.text(),
                self.ui.lineEdit_4.text(),
                self.ui.lineEdit_5.text(),
                self.ui.lineEdit_6.text(),
                self.ui.lineEdit_7.text(),
                self.ui.lineEdit_8.text(),
                self.ui.lineEdit_9.text(),
                self.ui.lineEdit.text(),  # WHERE npm
            )
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()

            self.load_data_mhs()
        except mysql.connector.Error as e:
            print("Gagal mengubah data:", e)
    
    def hapus_data_mhs(self):
        try:
            npm = self.ui.lineEdit.text()
            if npm == "":
                print("NPM kosong, tidak bisa menghapus.")
                return

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mhs"
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM mhs WHERE npm = %s", (npm,))
            conn.commit()
            cursor.close()
            conn.close()

            self.load_data_mhs()
            self.bersihkan_field()
        except mysql.connector.Error as e:
            print("Gagal menghapus data:", e)

    def bersihkan_field(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()
    
    def clear_table_widget(self):
        self.ui.tableWidget.setRowCount(0)

    def load_data_nilai(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='db_mhs'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nilai_mhs")
            result = cursor.fetchall()

            self.ui.tableWidget_4.setRowCount(0)  # kosongkan dulu table
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_4.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_4.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Database error:", err)
    def isi_field_nilai(self, row, column):
            self.ui.lineEdit_28.setText(self.ui.tableWidget_4.item(row, 0).text())
            self.ui.lineEdit_29.setText(self.ui.tableWidget_4.item(row, 1).text())
            self.ui.lineEdit_30.setText(self.ui.tableWidget_4.item(row, 2).text())
            self.ui.lineEdit_31.setText(self.ui.tableWidget_4.item(row, 3).text())
            self.ui.lineEdit_32.setText(self.ui.tableWidget_4.item(row, 4).text())
            self.ui.lineEdit_33.setText(self.ui.tableWidget_4.item(row, 5).text())


    def tambah_data_nilai(self):
            id_val = self.ui.lineEdit_28.text()
            npm = self.ui.lineEdit_29.text()
            nilai_h = self.ui.lineEdit_30.text()
            nilai_t = self.ui.lineEdit_31.text()
            nilai_uts = self.ui.lineEdit_32.text()
            nilai_uas = self.ui.lineEdit_33.text()

            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='db_mhs'
                )
                cursor = conn.cursor()
                query = "INSERT INTO nilai_mhs (id_nilai, npm, nilai_h, nilai_t, nilai_uts, nilai_uas) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (id_val, npm, nilai_h, nilai_t, nilai_uts, nilai_uas)
                cursor.execute(query, values)
                conn.commit()
                cursor.close()
                conn.close()

                self.load_data_nilai()  # Refresh tampilan tabel
                print("Data berhasil ditambahkan.")
            except mysql.connector.Error as err:
                print("Gagal menambahkan data:", err)
    def ubah_data_nilai(self):
            id_val = self.ui.lineEdit_28.text()
            npm = self.ui.lineEdit_29.text()
            nilai_h = self.ui.lineEdit_30.text()
            nilai_t = self.ui.lineEdit_31.text()
            nilai_uts = self.ui.lineEdit_32.text()
            nilai_uas = self.ui.lineEdit_33.text()

            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='db_mhs'
                )
                cursor = conn.cursor()
                query = "UPDATE nilai_mhs SET npm=%s, nilai_h=%s, nilai_t=%s, nilai_uts=%s, nilai_uas=%s WHERE id_nilai=%s"
                values = (npm, nilai_h, nilai_t, nilai_uts, nilai_uas, id_val)
                cursor.execute(query, values)
                conn.commit()
                cursor.close()
                conn.close()

                self.load_data_nilai()
                print("Data berhasil diubah.")
            except mysql.connector.Error as err:
                print("Gagal mengubah data:", err)
    
    def hapus_data_nilai(self):
            id_val = self.ui.lineEdit_28.text()

            try:
                conn = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='db_mhs'
                )
                cursor = conn.cursor()
                query = "DELETE FROM nilai_mhs WHERE id=%s"
                cursor.execute(query, (id_val,))
                conn.commit()
                cursor.close()
                conn.close()

                self.load_data_nilai()
                self.bersihkan_field_nilai()
                print("Data berhasil dihapus.")
            except mysql.connector.Error as err:
                print("Gagal menghapus data:", err)



    def bersihkan_field_nilai(self):
        self.ui.lineEdit_28.clear()
        self.ui.lineEdit_29.clear()
        self.ui.lineEdit_30.clear()
        self.ui.lineEdit_31.clear()
        self.ui.lineEdit_32.clear()
        self.ui.lineEdit_33.clear()
    
    def clear_table_nilai(self):
        self.ui.tableWidget_4.setRowCount(0)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
