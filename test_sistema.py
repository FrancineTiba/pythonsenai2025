from cliente import cadastrar_cliente
from emails import gerar_email

def test_cadastrar_cliente():
    cliente = cadastrar_cliente("joão da silva")
    assert cliente["nome"] == "João Da Silva"

def test_gerar_email():
    email = gerar_email("MARIA FERNANDA")
    assert email == "Olá, maria fernanda. Seja bem vindo(a) ao nosso sistema!"    