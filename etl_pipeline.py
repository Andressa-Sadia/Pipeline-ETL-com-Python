import pandas as pd

# ETAPA 1 - EXTRAÇÃO
dados = pd.read_csv("dados_entrada.csv")

# ETAPA 2 - TRANSFORMAÇÃO
def gerar_mensagem(nome, conta, cartao):
    return (
        f"Olá {nome}, tudo bem? 😊\n"
        f"Temos novidades para sua conta {conta}. "
        f"Aproveite os benefícios do seu cartão {cartao}!"
    )

dados["mensagem"] = dados.apply(
    lambda row: gerar_mensagem(row["nome"], row["conta"], row["cartao"]),
    axis=1
)

# ETAPA 3 - CARREGAMENTO
dados.to_csv("dados_saida.csv", index=False)

print("Pipeline ETL executado com sucesso!")
