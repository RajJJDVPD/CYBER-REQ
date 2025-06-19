import tkinter as tk
from tkinter import messagebox
import requests
import time
import threading
from PIL import Image, ImageTk
import pyfiglet

# === GLOBAL FLAG TO CANCEL ===
stop_requests = False

# === FUNCTION TO SEND REQUESTS ===
def send_requests(url, count, delay):
    global stop_requests
    stop_requests = False

    def insert_output(text):
        output.insert(tk.END, text)
        output.see(tk.END)

    def update_status(text):
        status_label.config(text=text)

    for i in range(1, count + 1):
        if stop_requests:
            root.after(0, insert_output, "[!] 🚫 Requesting cancelled by user.\n")
            break
        try:
            response = requests.get(url)
            root.after(0, insert_output, f"[{i}] ✅ Status: {response.status_code}\n")
        except Exception as e:
            root.after(0, insert_output, f"[{i}] ❌ Error: {e}\n")
        time.sleep(delay)

    root.after(0, update_status, "✅ Finished.")
    root.after(0, send_button.config, {"state": tk.NORMAL})
    root.after(0, cancel_button.config, {"state": tk.DISABLED})

# === CANCEL FUNCTION ===
def cancel_requests():
    global stop_requests
    stop_requests = True
    status_label.config(text="❌ Cancel requested...")

# === START BUTTON FUNCTION ===
def start_sending():
    url = url_entry.get().strip()
    try:
        count = int(count_entry.get())
        delay = float(delay_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers.")
        return

    if not url.startswith("http"):
        messagebox.showerror("URL Error", "URL must start with http or https.")
        return

    output.delete(1.0, tk.END)
    status_label.config(text="📡 Sending...")
    send_button.config(state=tk.DISABLED)
    cancel_button.config(state=tk.NORMAL)
    threading.Thread(target=send_requests, args=(url, count, delay)).start()

# === GUI SETUP ===
root = tk.Tk()
root.title("🛡️ CYBER-REQ | HTTP Request Tool by Yarra Rajkumar")
root.geometry("800x750")
root.configure(bg="#121212")
root.resizable(False, False)

# === WARNING BANNER ===
tk.Label(root, text="⚠️ WARNING: THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY ⚠️",
         font=("Segoe UI", 10, "bold"), fg="orange", bg="#121212").pack(pady=6)

# === LOGO IMAGE ===
try:
    logo_image = Image.open("logo.png")
    logo_image = logo_image.resize((80, 80))
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo, bg="#121212")
    logo_label.pack(pady=(0, 5))
except Exception as e:
    print("Logo could not be loaded:", e)

# === FIGLET BANNER ===
figlet_text = pyfiglet.figlet_format("CYBER-REQ", font="slant")
ascii_label = tk.Label(root, text=figlet_text, font=("Courier", 8),
                       fg="#00ff00", bg="#121212", justify="left")
ascii_label.pack(pady=(0, 5))

# === SUBTITLE ===
subtitle = tk.Label(root, text="Send HTTP Requests with Control - GUI Tool",
                    font=("Segoe UI", 10), fg="gray", bg="#121212")
subtitle.pack()

# === INPUT FIELDS ===
tk.Label(root, text="🌐 Target URL:", bg="#121212", fg="white").pack(pady=(15, 0))
url_entry = tk.Entry(root, width=65, bg="#1e1e1e", fg="#00ffcc", insertbackground="#00ffcc")
url_entry.pack(pady=(0, 10))

tk.Label(root, text="🔁 Number of Requests:", bg="#121212", fg="white").pack()
count_entry = tk.Entry(root, width=20, bg="#1e1e1e", fg="#00ffcc", insertbackground="#00ffcc")
count_entry.pack(pady=(0, 10))

tk.Label(root, text="⏱️ Delay Between Requests (sec):", bg="#121212", fg="white").pack()
delay_entry = tk.Entry(root, width=20, bg="#1e1e1e", fg="#00ffcc", insertbackground="#00ffcc")
delay_entry.pack(pady=(0, 10))

# === BUTTONS ===
button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=(10, 0))

send_button = tk.Button(button_frame, text="🚀 Launch", command=start_sending,
                        bg="#00ffcc", fg="black", font=("Segoe UI", 10, "bold"), padx=10, pady=5)
send_button.grid(row=0, column=0, padx=10)

cancel_button = tk.Button(button_frame, text="🛑 Cancel", command=cancel_requests,
                          bg="red", fg="white", font=("Segoe UI", 10, "bold"),
                          padx=10, pady=5, state=tk.DISABLED)
cancel_button.grid(row=0, column=1)

# === STATUS + OUTPUT ===
status_label = tk.Label(root, text="", fg="#00ffcc", bg="#121212", font=("Segoe UI", 10))
status_label.pack(pady=(5, 0))

output = tk.Text(root, height=15, width=90, bg="#000000", fg="#00FF00", insertbackground="#00ff00")
output.pack(pady=10)

# === FOOTER WITH YOUR DETAILS ===
footer_frame = tk.Frame(root, bg="#121212")
footer_frame.pack(pady=10)

tk.Label(footer_frame, text="🧑‍💻 Developed by:", fg="#00ffcc", bg="#121212", font=("Segoe UI", 10, "bold")).pack()
tk.Label(footer_frame, text="Yarra Rajkumar", fg="white", bg="#121212", font=("Segoe UI", 11)).pack()
tk.Label(footer_frame, text="📧 rajkumar0yarra@gmail.com", fg="#00ffff", bg="#121212", font=("Segoe UI", 10)).pack(pady=(0, 5))

tk.Label(footer_frame,
         text="⚠️ WARNING: This tool is for EDUCATIONAL PURPOSES ONLY.\nUnauthorized use is strictly prohibited.",
         fg="orange", bg="#121212", font=("Segoe UI", 10, "bold"), wraplength=600, justify="center").pack()

# === MAIN LOOP ===
root.mainloop()
