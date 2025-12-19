import re   

# Função Teste 1: Correção do Range e Espaços
def remover_caracteres_especiais(texto):
    """Mantém apenas letras, números e ESPAÇOS"""
    if not isinstance(texto, str):
        return str(texto)
    # Correção: Era [^a-zA-Z0-0], mudamos para [^a-zA-Z0-9 ]
    # Note o espaço em branco antes do fecha colchetes!
    return re.sub(r'[^a-zA-Z0-9 ]', '', texto)

# Função Teste 2: Agora vai funcionar porque a func 1 manteve os espaços
def padronizar_snake_case(texto):
    """Substitui espaços por '_'"""
    if not isinstance(texto, str):
        return str(texto)
    texto_limpo = remover_caracteres_especiais(texto)
    return re.sub(r'\s+', '_', texto_limpo).lower()

# Função Teste 3: Estava correta!
def extrair_emails(texto):
    """Extrai apenas os emails do texto"""
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(padrao, texto)

# Função Teste 4: Correção do .strip() e da substituição
def limpar_espacos_extras(texto):
    """Normaliza espaços (remove duplos e trim)"""
    # 1. Substitui 'vários espaços' (\s+) por 'um espaço' (' ')
    # 2. Adicionados os parênteses no .strip()
    return re.sub(r'\s+', ' ', texto).strip()

# --- Execução ---
if __name__ == "__main__":
    print('-- Teste Regex Corrigido --')

    # Teste 1
    raw = "Preço: R$1.200,00!!"
    # Esperado: Preco R120000 (O 'ç' some pois não está no range a-z, isso é normal para essa regex simples)
    print(f"1. Remove Especiais:\nOriginal: {raw}\nResultado: {remover_caracteres_especiais(raw)}\n")

    # Teste 2
    texto = "Matheus Ribeiro Marafon"
    # Esperado: matheus_ribeiro_marafon
    print(f"2. Snake Case:\nOriginal: {texto}\nResultado: {padronizar_snake_case(texto)}\n")

    # Teste 3
    msg = "Entre em contato: marafonmatheus@gmail.com ou matheusmarafon@gmail.com"
    print(f"3. Emails:\n{extrair_emails(msg)}\n")

    # Teste 4
    texto_sujo = "Matheus     Ribeiro     Marafon"
    # Esperado: Matheus Ribeiro Marafon
    print(f"4. Espaços:\nOriginal: '{texto_sujo}'\nResultado: '{limpar_espacos_extras(texto_sujo)}'")