import os
import sys
import datetime

def obtener_ruta_base():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def cargar_proxies():
    lista = []
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "proxy_list.txt")
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                lines = [l.strip() for l in f.readlines() if l.strip()]
                for line in lines:
                    try:
                        parts = line.split(':')
                        if len(parts) == 4:
                            lista.append({'ip': parts[0], 'port': parts[1], 'user': parts[2], 'pass': parts[3]})
                    except: pass
        except: pass
    return lista

def cargar_kick_tokens():
    lista = []
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "kick_tokens.txt")
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                lista = [l.strip() for l in f.readlines() if l.strip()]
        except: pass
    return lista

def cargar_frases_chat():
    lista = []
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "Chat_MSN.txt")
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8', errors='ignore') as f:
                lista = [l.strip() for l in f.readlines() if l.strip()]
        except: pass
    return lista

def cargar_api_keys():
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "google_api_key.txt")
    keys = []
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                keys = [l.strip() for l in f.readlines() if l.strip()]
        except: pass
    return keys


def cargar_prompt_ia():
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "prompt_ia.txt")
    
    default_prompt = (
        "Actúa como un usuario más del chat del stream. "
        "DIRECTIVA SUPREMA: Tu personalidad debe basarse EXCLUSIVAMENTE en la 'CATEGORIA' y el 'TITULO STREAM'. "
        "1. Si la categoría es 'Just Chatting', 'Conversando', 'IRL' o 'Pools': NO hables de videojuegos ni uses jerga gamer. Comenta sobre lo que sucede en pantalla o el tema de conversación. "
        "2. Si la categoría es un videojuego (ej. Minecraft, Slots, CoD, Fortnite,...): Entonces sí comenta sobre videojuegos. "
        "3. Sé natural y reactivo."
    )
    
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content: return content 
        except: pass
    
    # Si no existe, creamos este prompt neutro
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(default_prompt)
    except: pass
    
    return default_prompt

def cargar_prompt_audio():
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "prompt_audio.txt")
    default_audio = "Escucha esto y dame una respuesta corta y natural."
    
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content: return content
        except: pass
        
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(default_audio)
    except: pass
    
    return default_audio

def guardar_prompt_audio(texto):
    ruta = os.path.join(obtener_ruta_base(), "Utilities", "prompt_audio.txt")
    try:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)
    except: pass

def log_gui(widget, message):
    import tkinter as tk
    timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
    full_msg = f"{timestamp} {message}"
    def _write():
        if widget: 
            widget.config(state='normal')
            widget.insert(tk.END, full_msg + "\n")
            widget.see(tk.END)
            widget.config(state='disabled')
    try: widget.after(0, _write)
    except: pass
