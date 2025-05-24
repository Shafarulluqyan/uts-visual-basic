import tkinter as tk
from tkinter import ttk, messagebox

# Constants untuk harga fasilitas
HARGA_INTERNET = 50000
HARGA_TV = 40000

def clear_fields():
    entry_nama_tamu.delete(0, tk.END)
    entry_kode_kamar.delete(0, tk.END)
    entry_nama_kamar.delete(0, tk.END)
    entry_biaya_sewa.delete(0, tk.END)
    entry_total_sewa.delete(0, tk.END)
    entry_bayar.delete(0, tk.END)
    entry_kembali.delete(0, tk.END)
    tipe_kamar.set(None)
    cb_internet_var.set(0)
    cb_tv_var.set(0)

def exit_app():
    root.destroy()

def only_numeric(char):
    return char.isdigit() or char == ""

def hitung_total_kembali():
    try:
        biaya_sewa = int(entry_biaya_sewa.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan Biaya Sewa yang valid (angka)!")
        return
    fasilitas = 0
    if cb_internet_var.get():
        fasilitas += HARGA_INTERNET
    if cb_tv_var.get():
        fasilitas += HARGA_TV
    total_sewa = biaya_sewa + fasilitas
    entry_total_sewa.delete(0, tk.END)
    entry_total_sewa.insert(0, str(total_sewa))

    try:
        bayar = int(entry_bayar.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan Bayar yang valid (angka)!")
        return
    kembali = bayar - total_sewa
    entry_kembali.delete(0, tk.END)
    entry_kembali.insert(0, str(kembali))

# Window Utama
root = tk.Tk()
root.title("HOTEL PERDANA")
root.geometry("700x460")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

# Style
style = ttk.Style(root)
style.theme_use('clam')

style.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 11), foreground="#34495E")
style.configure("Header.TLabel", font=("Segoe UI", 24, "bold"), foreground="#2C3E50", background="#f0f4f8")
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=6)
style.map("TButton",
          background=[('active', "#1A5276"), ('!active', '#2980B9')],
          foreground=[('active', 'white'), ('!active', 'white')])
style.configure("TRadiobutton", background="#f0f4f8", font=("Segoe UI", 10))
style.configure("TCheckbutton", background="#f0f4f8", font=("Segoe UI", 10))

# Validation untuk numeric input
vcmd = (root.register(only_numeric), '%S')

# Judul
judul = ttk.Label(root, text="HOTEL PERDANA", style="Header.TLabel")
judul.grid(row=0, column=0, columnspan=4, pady=20)

# Frame kiri
frame_kiri = ttk.Frame(root)
frame_kiri.grid(row=1, column=0, padx=30, sticky="n")

ttk.Label(frame_kiri, text="Nama Tamu").grid(row=0, column=0, sticky="w", pady=6)
entry_nama_tamu = ttk.Entry(frame_kiri, width=30)
entry_nama_tamu.grid(row=1, column=0, pady=4)

ttk.Label(frame_kiri, text="Kode Kamar").grid(row=2, column=0, sticky="w", pady=6)
entry_kode_kamar = ttk.Entry(frame_kiri, width=30)
entry_kode_kamar.grid(row=3, column=0, pady=4)

ttk.Label(frame_kiri, text="Nama Kamar").grid(row=4, column=0, sticky="w", pady=6)
entry_nama_kamar = ttk.Entry(frame_kiri, width=30)
entry_nama_kamar.grid(row=5, column=0, pady=4)

ttk.Label(frame_kiri, text="Tipe Kamar").grid(row=6, column=0, sticky="w", pady=10)
tipe_kamar = tk.StringVar()
rb_superior = ttk.Radiobutton(frame_kiri, text="Superior", variable=tipe_kamar, value="Superior")
rb_deluxe = ttk.Radiobutton(frame_kiri, text="Deluxe", variable=tipe_kamar, value="Deluxe")
rb_suite = ttk.Radiobutton(frame_kiri, text="Suite", variable=tipe_kamar, value="Suite")

rb_superior.grid(row=7, column=0, sticky="w", pady=2)
rb_deluxe.grid(row=8, column=0, sticky="w", pady=2)
rb_suite.grid(row=9, column=0, sticky="w", pady=2)

# Frame tengah
frame_tengah = ttk.Frame(root)
frame_tengah.grid(row=1, column=1, padx=30, sticky="n")

ttk.Label(frame_tengah, text="Biaya Sewa").grid(row=0, column=0, sticky="w", pady=6)
entry_biaya_sewa = ttk.Entry(frame_tengah, width=25, validate="key", validatecommand=vcmd)
entry_biaya_sewa.grid(row=1, column=0, pady=4)

ttk.Label(frame_tengah, text="Fasilitas Tambahan").grid(row=2, column=0, sticky="w", pady=10)
cb_internet_var = tk.IntVar()
cb_tv_var = tk.IntVar()
cb_internet = ttk.Checkbutton(frame_tengah, text=f"Internet (+Rp{HARGA_INTERNET:,})", variable=cb_internet_var)
cb_tv = ttk.Checkbutton(frame_tengah, text=f"TV Kabel (+Rp{HARGA_TV:,})", variable=cb_tv_var)

cb_internet.grid(row=3, column=0, sticky="w", pady=2)
cb_tv.grid(row=4, column=0, sticky="w", pady=2)

ttk.Label(frame_tengah, text="Total Sewa").grid(row=5, column=0, sticky="w", pady=6)
entry_total_sewa = ttk.Entry(frame_tengah, width=25)
entry_total_sewa.grid(row=6, column=0, pady=4)

ttk.Label(frame_tengah, text="Bayar").grid(row=7, column=0, sticky="w", pady=6)
entry_bayar = ttk.Entry(frame_tengah, width=25, validate="key", validatecommand=vcmd)
entry_bayar.grid(row=8, column=0, pady=4)

ttk.Label(frame_tengah, text="Kembali").grid(row=9, column=0, sticky="w", pady=6)
entry_kembali = ttk.Entry(frame_tengah, width=25)
entry_kembali.grid(row=10, column=0, pady=4)

# Frame tombol
frame_tombol = ttk.Frame(root)
frame_tombol.grid(row=2, column=0, columnspan=2, pady=30)

btn_hitung = ttk.Button(frame_tombol, text="HITUNG", command=hitung_total_kembali)
btn_hitung.grid(row=0, column=0, padx=15)

btn_clear = ttk.Button(frame_tombol, text="CLEAR", command=clear_fields)
btn_clear.grid(row=0, column=1, padx=15)

btn_exit = ttk.Button(frame_tombol, text="EXIT", command=exit_app)
btn_exit.grid(row=0, column=2, padx=15)

root.mainloop()
