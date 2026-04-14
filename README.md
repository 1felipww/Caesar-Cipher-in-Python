# Cesar Cipher in Python 🔐

This is a simple and straightforward Python script that implements the classic **Caesar Cipher**. It allows you to encrypt messages by shifting the letters of the alphabet based on a number (the key or "shift") chosen by the user.

> **Note:** I am aware it is traditionally spelled "Caesar", but I prefer **Cesar** as it's the Brazilian way of adapting and localizing things! 

## 🛠️ Features

* **Case-Sensitive Handling:** The code processes uppercase and lowercase letters separately, maintaining the original capitalization of the text.
* **Preservation of Special Characters:** Spaces, numbers, and punctuation marks (such as `!`, `?`, `.`) are left unaltered; the script simply ignores them and passes them straight to the final output.
* **Error Handling:** If the user enters something that is not an integer for the shift key, the program displays a friendly warning message instead of crashing.

## 🚀 How to Run

1.  Make sure you have Python  installed on your machine.
2.  Save the code in a file, for example, `cesar_cipher.py`.
3.  Open your terminal (or command prompt) and navigate to the folder where you saved the file.
4.  Run the following command:
  
    ``python cesar_cipher.py``
  

## 💻 Usage Example


``Send the word or phrase: Hello, world!
What is the cipher number (the pulse)? 3``

``Original: Hello World!
With the Caesar Cipher:  Khoor Zruog!``

## 🧠 How the logic works

The cesar_cipher(text, shift) function iterates through each character:

It checks if the letter is uppercase (isupper()) or lowercase (islower()).

It converts the letter to its numerical value in the ASCII table using ord().

It applies the shift and uses the modulo operation (% 26) to ensure the alphabet wraps around (after 'Z', it loops back to 'A').

-------------------------------------------------------------------------------------------------------------------------------------------

# Cifra de Cesar em Python 🔐

Este é um script simples e direto em Python que implementa a clássica **Cifra de Cesar**. Ele permite criptografar mensagens deslocando as letras do alfabeto com base em um número (a chave ou "pulo") escolhido pelo utilizador.

> **Nota:** Eu sei que o nome original é "Caesar", mas prefiro escrever **Cesar** por ser o jeitinho brasileiro de adaptar as coisas!

## 🛠️ Funcionalidades

* **Diferenciação de Maiúsculas e Minúsculas:** O código trata letras maiúsculas e minúsculas separadamente, mantendo a formatação original do texto.
* **Preservação de Caracteres Especiais:** Espaços, números e pontuações (como `!`, `?`, `.`) não são alterados; o script apenas os ignora e repassa para o resultado final.
* **Tratamento de Erros:** Se o utilizador digitar algo que não seja um número inteiro para a chave (o pulo), o programa avisa de forma amigável em vez de simplesmente fechar com erro.

## 🚀 Como executar

1.  Certifica-te de que tens o **Python 3.x** instalado na tua máquina.
2.  Guarda o código num ficheiro, por exemplo, `cifra_cesar.py`.
3.  Abre o terminal (ou prompt de comando) e navega até à pasta onde o ficheiro foi guardado.
4.  Corre o comando:
    
    ``python cifra_cesar.py``
    

## 💻 Exemplo de Uso

Ao correr o script, ele fará duas perguntas:


Manda a palavra ou frase: Ola Mundo!
Qual o numero da cifra (o pulo)? 3

``Original: Ola Mundo!
Cifrado:  Rqd Pxqgr!``

# 🧠 Como a lógica funciona?

A função cesar_cipher(text, shift) percorre cada letra do texto:

Verifica se é maiúscula (isupper()) ou minúscula (islower()).

Converte a letra para o seu valor numérico na tabela ASCII usando ord().

Aplica o "pulo" (shift) e usa a operação de módulo (% 26) para garantir que o alfabeto "dê a volta" (depois do 'Z', volta para o 'A').

Converte o número de volta para letra usando chr().

It converts the number back into a letter using chr().
