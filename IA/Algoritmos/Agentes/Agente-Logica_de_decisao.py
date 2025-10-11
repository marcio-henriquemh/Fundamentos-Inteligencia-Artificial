import math

#variaveis e probabilidades
proba_chover=0.3
proba_nao_chover=0.7

#funcao valor esperado

def funcao_valor_esperado(proba_chover,proba_nao_chover):

    
   # Utilidades fornecidas
    levar_e_chover = 10
    levar_e_nao_chover = 5
    nao_levar_e_chover = 0
    nao_levar_e_nao_chover = 9


 # Cálculo do valor esperado para LEVAR guarda-chuva
    valor_esperado_levar = (levar_e_chover * proba_chover) + (levar_e_nao_chover * proba_nao_chover)
    
    # Cálculo do valor esperado para NÃO LEVAR guarda-chuva
    valor_esperado_nao_levar = (nao_levar_e_chover * proba_chover) + (nao_levar_e_nao_chover * proba_nao_chover)
    return valor_esperado_levar, valor_esperado_nao_levar

# Executando a função
ve_levar, ve_nao_levar = funcao_valor_esperado(proba_chover, proba_nao_chover)

# Exibindo resultados
print("=== ANÁLISE DE DECISÃO ===")
print(f"Probabilidade de chover: {proba_chover}")
print(f"Probabilidade de não chover: {proba_nao_chover}")
print("\--- VALORES ESPERADOS ---")
print(f"Levar guarda-chuva: {ve_levar:.2f}")
print(f"Não levar guarda-chuva: {ve_nao_levar:.2f}")
print("\--- RECOMENDAÇÃO ---")
if ve_levar > ve_nao_levar:
    print("RECOMENDAÇÃO: Levar guarda-chuva")
    print(f"Vantagem: {ve_levar - ve_nao_levar:.2f} pontos")
elif ve_nao_levar > ve_levar:
    print("RECOMENDAÇÃO: Não levar guarda-chuva")
    print(f"Vantagem: {ve_nao_levar - ve_levar:.2f} pontos")
else:
    print("RECOMENDAÇÃO: Indiferente (ambas têm o mesmo valor esperado)")