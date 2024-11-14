import tkinter as tk
from tkinter import ttk

# Função para atualizar as estatísticas
def update_statistics(*args):
    try:
        anime = int(anime_input.get())
        desenhos = int(desenhos_input.get())
        series = int(series_input.get())
        filmes = int(filmes_input.get())
        ambos = int(ambos_input.get())
    except ValueError:
        anime, desenhos, series, filmes, ambos = 0, 0, 0, 0, 0

    total = anime + desenhos + series + filmes + ambos
    total_label.config(text=f"Total: {total}")

    # Limpa a exibição atual das estatísticas
    for widget in stats_display.winfo_children():
        widget.destroy()

    # Adiciona barras de progresso e percentagens para cada categoria
    for label, value, color in [
        ("Anime", anime, "green"),
        ("Desenhos Animados", desenhos, "blue"),
        ("Séries", series, "purple"),
        ("Filmes", filmes, "orange"),
        ("Ambos", ambos, "red")]:
        
        percentage = (value / total * 100) if total > 0 else 0
        percentage_text = f"{percentage:.2f}%"

        # Cria a linha com a porcentagem e a barra de progresso
        frame = tk.Frame(stats_display, bg="#f0f0f0")
        frame.pack(fill="x", pady=5, padx=10)
        
        label_text = tk.Label(frame, text=f"{label}: {value} pessoas ({percentage_text})", width=30, anchor="w", bg="#f0f0f0", font=("Arial", 10))
        label_text.pack(side="left")
        
        bar = ttk.Progressbar(frame, length=200, maximum=100, style="TProgressbar")
        bar['value'] = percentage
        bar.pack(side="left", padx=5, fill="x", expand=True)
        
        percent_label = tk.Label(frame, text=percentage_text, bg="#f0f0f0", font=("Arial", 10))
        percent_label.pack(side="left")

# Inicialização da janela principal
root = tk.Tk()
root.title("Estatísticas de Preferências")
root.geometry("650x550")
root.config(bg="#e0e0e0")

# Título
tk.Label(root, text="Estatísticas de Preferências", font=("Arial", 18, "bold"), bg="#e0e0e0", fg="darkblue").pack(pady=10)

# Entrada de dados
input_frame = tk.Frame(root, bg="#e0e0e0")
input_frame.pack(pady=10)

for text, var_name in [
    ("Quantidade de pessoas que gostam de Anime:", "anime"),
    ("Quantidade de pessoas que gostam de Desenhos Animados:", "desenhos"),
    ("Quantidade de pessoas que gostam de Séries:", "series"),
    ("Quantidade de pessoas que gostam de Filmes:", "filmes"),
    ("Quantidade de pessoas que gostam de Ambos (Tudo):", "ambos")]:
    
    frame = tk.Frame(input_frame, bg="#e0e0e0")
    frame.pack(fill="x", pady=5, padx=10)
    
    tk.Label(frame, text=text, bg="#e0e0e0", font=("Arial", 10)).pack(side="left")
    entry = tk.Entry(frame, width=5, font=("Arial", 10))
    entry.insert(0, "0")
    entry.pack(side="right", padx=5)
    
    locals()[f"{var_name}_input"] = entry
    entry.bind("<KeyRelease>", update_statistics)

# Exibição do total e estatísticas
total_label = tk.Label(root, text="Total: 0", font=("Arial", 12, "bold"), bg="#e0e0e0", fg="darkred")
total_label.pack(pady=5)

stats_display = tk.Frame(root, bg="#f0f0f0", bd=1, relief="sunken")
stats_display.pack(pady=10, fill="x", padx=10)

# Estilos das barras de progresso
style = ttk.Style()
style.configure("TProgressbar", thickness=20)
style.configure("green.Horizontal.TProgressbar", troughcolor="#c0e6c9", background="green")
style.configure("blue.Horizontal.TProgressbar", troughcolor="#c0d9f0", background="blue")
style.configure("purple.Horizontal.TProgressbar", troughcolor="#e2d1f0", background="purple")
style.configure("orange.Horizontal.TProgressbar", troughcolor="#f0dcc7", background="orange")
style.configure("red.Horizontal.TProgressbar", troughcolor="#f0c5c5", background="red")

# Inicializa as estatísticas ao abrir o aplicativo
update_statistics()

root.mainloop()
