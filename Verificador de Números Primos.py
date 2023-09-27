import tkinter as tk

# teste condicional
def teste_primo(n):
    auxiliar = 0
    for i in range(1, n + 1):
        if n % i == 0:
            auxiliar += 1
    return auxiliar == 2

def verificar_primo():
    numero = int(entrada_numero.get())
    resultado = teste_primo(numero)
    if resultado:
        resultado_label.config(text=f"O número {numero} é primo.")  # true
    else:
        resultado_label.config(text=f"O número {numero} não é primo.")  # false


# interface grafica
# Crie uma instância da janela principal
janela = tk.Tk()
janela.title("Verificador de Números Primos")

# Crie uma etiqueta
etiqueta = tk.Label(janela, text="Digite um número inteiro positivo:")
etiqueta.pack()

# Crie uma entrada de texto
entrada_numero = tk.Entry(janela)
entrada_numero.pack()

# Crie um botão para verificar o número
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_primo)
botao_verificar.pack()

# Crie um rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Inicie o loop de eventos da interface gráfica
janela.mainloop()
