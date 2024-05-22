import tkinter as tk
from tkinter import messagebox

class TagihanListrik:
    def __init__(self, root):
        self.root = root
        self.root.title("Perhitungan Tagihan Listrik")

        self.entries = []

        self.Alat_Elektronik()

    def Alat_Elektronik(self):
        self.tarif_label = tk.Label(self.root, text="Tarif per kWh (Rp):")
        self.tarif_label.pack()
        self.tarif_entry = tk.Entry(self.root)
        self.tarif_entry.pack()        

        self.jumlah_label = tk.Label(self.root, text="Jumlah alat elektronik (1-50):")
        self.jumlah_label.pack()
        self.jumlah_entry = tk.Entry(self.root)
        self.jumlah_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.Masukan_input)
        self.submit_button.pack()

    def Masukan_input(self):
        try:
            self.tarif_per_kwh = float(self.tarif_entry.get())
            jumlah_alat = int(self.jumlah_entry.get())
            if jumlah_alat < 1 or jumlah_alat > 50:
                raise ValueError("Jumlah alat harus antara 1 hingga 50.")

            self.entries.clear()
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Frame):
                    widget.destroy()

            for i in range(jumlah_alat):
                frame = tk.Frame(self.root)
                frame.pack()

                watt_label = tk.Label(frame, text=f"Alat {i+1} - Watt:")
                watt_label.pack(side=tk.LEFT)
                watt_entry = tk.Entry(frame)
                watt_entry.pack(side=tk.LEFT)

                jam_label = tk.Label(frame, text=" Jam/hari:")
                jam_label.pack(side=tk.LEFT)
                jam_entry = tk.Entry(frame)
                jam_entry.pack(side=tk.LEFT)

                hari_label = tk.Label(frame, text=" Hari/bulan:")
                hari_label.pack(side=tk.LEFT)
                hari_entry = tk.Entry(frame)
                hari_entry.pack(side=tk.LEFT)

                self.entries.append((watt_entry, jam_entry, hari_entry))

            self.calculate_button = tk.Button(self.root, text="Hitung Tagihan", command=self.hitung_total)
            self.calculate_button.pack()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def hitung_total(self):
        try:
            total_biaya = 0
            for watt_entry, jam_entry, hari_entry in self.entries:
                watt = float(watt_entry.get())
                jam_per_hari = float(jam_entry.get())
                hari_per_bulan = float(hari_entry.get())

                biaya_alat = self.hitung_tagihan_listrik(watt, jam_per_hari, hari_per_bulan)
                total_biaya += biaya_alat

            messagebox.showinfo("Total Tagihan Listrik", f"Total tagihan listrik untuk semua alat: Rp{total_biaya:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Maukan input dengan benar.")

    def hitung_tagihan_listrik(self, watt, jam_per_hari, hari_per_bulan):
        kwh_per_hari = (watt * jam_per_hari) / 1000  # Mengonversi watt-jam ke kWh
        kwh_per_bulan = kwh_per_hari * hari_per_bulan
        biaya_per_bulan = kwh_per_bulan * self.tarif_per_kwh
        return biaya_per_bulan

if __name__ == "__main__":
    root = tk.Tk()
    app = TagihanListrik(root)
    root.mainloop()
