import re
import random
import string

def validar_email(email):
    """Valida se o e-mail está no formato correto."""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def gerar_senha_forte(nome_usuario):
    """Gera uma senha forte baseada no nome do usuário."""
    random.seed(nome_usuario)
    senha_aleatoria = nome_usuario + ''.join(
        random.choice(string.ascii_letters + string.digits + string.punctuation) 
        for _ in range(10 - len(nome_usuario))
    )
    return senha_aleatoria

def validar_senha(senha):
    """Valida se a senha atende aos requisitos de segurança."""
    requisitos = {
        "Maiúsculas": any(char.isupper() for char in senha),
        "Minúsculas": any(char.islower() for char in senha),
        "Números": any(char.isdigit() for char in senha),
        "Especiais": any(char in string.punctuation for char in senha)
    }
    return sum(requisitos.values()) == len(requisitos)

def solicitar_dados():
    """Coleta os dados do usuário e retorna um dicionário com as informações."""
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    idade = int(input("Digite sua idade: "))

    if idade < 6:
        print("Não é possível cadastrar usuários menores de 6 anos.")
        return None

    nacionalidade = input("Digite sua nacionalidade: ")
    idiomas = input("Digite os idiomas que você fala, separados por vírgula: ").split(',')

    grau_escolaridade = input(
        "Qual é o seu grau de escolaridade (Ensino Fundamental, Ensino Médio, Superior)? "
    )
    serie, curso, periodo = None, None, None
    if grau_escolaridade.lower() == "ensino fundamental":
        serie = input("Digite a série que você está cursando (1 a 9): ")
    elif grau_escolaridade.lower() == "ensino médio":
        serie = input("Digite a série que você está cursando (1 a 3) ou 'completo' se já completou: ")
    elif grau_escolaridade.lower() == "superior":
        periodo = input("Digite o período que você está cursando: ")
        curso = input("Digite o nome do curso que você está cursando: ")

    trabalha = input("Você trabalha? (Sim/Não): ") if idade > 14 else "Não"
    profissao = input("Qual é sua profissão? ") if trabalha.lower() == "sim" else None

    objetivos = input("Resuma seus objetivos em 3 palavras: ")

    return {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Data de Nascimento": data_nascimento,
        "Idade": idade,
        "Nacionalidade": nacionalidade,
        "Idiomas": idiomas,
        "Grau de Escolaridade": grau_escolaridade,
        "Série/Período": serie or periodo,
        "Curso": curso,
        "Trabalha": trabalha,
        "Profissão": profissao,
        "Objetivos": objetivos
    }

def criar_senha(nome_usuario):
    """Cria e valida uma senha com base nas preferências do usuário."""
    print("\nCrie uma senha forte:")
    print("A senha deve conter:")
    print("- Letras maiúsculas")
    print("- Letras minúsculas")
    print("- Números")
    print("- Caracteres especiais (@#$%&*)")

    while True:
        senha = input("Digite sua senha: ").strip()
        if validar_senha(senha):
            return senha
        else:
            print("Senha fraca. Será gerada uma senha forte automaticamente.")
            senha_gerada = gerar_senha_forte(nome_usuario)
            print(f"Senha sugerida: {senha_gerada}")
            usar_sugerida = input("Deseja usar a senha sugerida? (S/N): ").strip().lower()
            if usar_sugerida == 's':
                return senha_gerada

def verificar_senha(senha_correta):
    """Permite que o usuário tente acessar com a senha fornecida."""
    tentativas, max_tentativas = 0, 3
    while tentativas < max_tentativas:
        tentativa = input("Digite sua senha para acesso: ").strip()
        if tentativa == senha_correta:
            print("Senha correta. Acesso liberado!")
            return
        else:
            tentativas += 1
            print(f"Senha incorreta. Restam {max_tentativas - tentativas} tentativas.")

    print("Número máximo de tentativas atingido. Acesso bloqueado.")

def main():
    print("Bem-vindo ao sistema!")
    # Validação de e-mail
    email = input("Digite seu e-mail: ").strip()
    if not validar_email(email):
        print("E-mail inválido. Reinicie o processo.")
        return

    print("E-mail válido! Agora prossiga com as demais informações.")
    dados = solicitar_dados()
    if not dados:
        return

    senha = criar_senha(dados['Nome'])
    verificar_senha(senha)

    print("\nInformações do Usuário:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()
