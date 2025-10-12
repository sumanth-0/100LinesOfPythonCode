# wikipedia_app.py  (<=100 lines)
# pip install wikipedia
import sys, signal, tkinter as tk
from tkinter import ttk
import wikipedia

wikipedia.set_lang("en")
_SHUTDOWN = {"flag": False}

def resolve_title(q: str) -> str | None:
    if not q: return None
    try:
        hits = wikipedia.search(q, results=1, suggestion=True)
        if isinstance(hits, tuple): hits = hits[0]
        return hits[0] if hits else None
    except Exception:
        return None

def fetch_para_and_url(topic: str) -> tuple[str, str | None]:
    title = resolve_title(topic)
    if not title: return ("No page found for that topic.", None)
    try:
        txt = wikipedia.summary(title, sentences=3, auto_suggest=False, redirect=True).strip()
        url = wikipedia.page(title, auto_suggest=False, redirect=True).url
        return (txt or "No content found.", url)
    except wikipedia.DisambiguationError as e:
        opts = "\n".join(f"• {o}" for o in e.options[:10])
        return (f"That topic is ambiguous. Try one of:\n{opts}", None)
    except wikipedia.PageError:
        return ("No page found for that topic.", None)
    except Exception as ex:
        return (f"Error: {ex}", None)

def on_search(*_):
    out.configure(state="normal"); out.delete("1.0","end")
    out.insert("end","Searching...\n"); out.update_idletasks()
    text, url = fetch_para_and_url(entry.get().strip())
    out.delete("1.0","end"); out.insert("end", text + ("\n\n" + url if url else ""))
    out.configure(state="disabled")

def on_clear():
    entry.delete(0,"end"); out.configure(state="normal")
    out.delete("1.0","end"); out.configure(state="disabled")

def exit_app(*_):
    try: root.quit()
    except Exception: pass
    try: root.destroy()
    except Exception: pass
    sys.exit(0)

def sigint_handler(*_): _SHUTDOWN["flag"] = True
def heartbeat():
    if _SHUTDOWN["flag"]: return exit_app()
    root.after(100, heartbeat)

root = tk.Tk()
root.title("Wikipedia First Paragraph"); root.geometry("720x420"); root.minsize(480,320)
signal.signal(signal.SIGINT, sigint_handler)
root.protocol("WM_DELETE_WINDOW", exit_app)

frm = ttk.Frame(root, padding=12); frm.pack(fill="both", expand=True)
ttk.Label(frm, text="Enter topic:").grid(row=0, column=0, sticky="w")
entry = ttk.Entry(frm); entry.grid(row=0, column=1, sticky="ew", padx=6); entry.focus()
ttk.Button(frm, text="Search", command=on_search).grid(row=0, column=2, padx=(6,0))
ttk.Button(frm, text="Clear", command=on_clear).grid(row=0, column=3, padx=(6,0))
out = tk.Text(frm, wrap="word", height=18, state="disabled")
out.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(10,0))
scroll = ttk.Scrollbar(frm, command=out.yview); out.configure(yscrollcommand=scroll.set)
scroll.grid(row=1, column=4, sticky="ns", pady=(10,0))
frm.columnconfigure(1, weight=1); frm.rowconfigure(1, weight=1)
root.bind("<Return>", on_search)

root.after(100, heartbeat)
root.mainloop()
