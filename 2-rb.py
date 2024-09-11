#!/usr/bin/env python
# coding: utf-8

# In[6]:


def verificar_letra_a(texto):
    contador = 0
    
    # Percorre a string e verifica se o caractere é 'a' ou 'A'
    for caractere in texto:
        if caractere == 'a' or caractere == 'A':
            contador += 1
    
    # Verifica se a letra 'a' existe e imprime a quantidade
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Informe uma string: ")
verificar_letra_a(texto)


# In[ ]:




