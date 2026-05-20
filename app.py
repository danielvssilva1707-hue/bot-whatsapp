from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

PIX_ONG = "11930306451"

TELEFONE_ONG = "(11) 93030-6451"

# EMAIL
EMAIL_ONG = "contato@fazendoadiferenca.ong.br"

INSTAGRAM_ONG = "@fazendoadiferencagru"


def menu():
    return (
        "Seja bem-vindo à ONG Fazendo a Diferença\n\n"
        "Escolha uma opção:\n\n"
        "1 - Sobre a ONG\n"
        "2 - Doação\n"
        "3 - Projetos\n"
        "4 - Contatos\n\n"
        "Digite MENU para voltar ao menu principal."
    )


def sobre_ong():
    return (
        "SOBRE A ONG\n\n"
        "A ONG Fazendo a Diferença é uma instituição social localizada em Guarulhos-SP.\n\n"
        "A ONG realiza ações sociais e projetos voltados para crianças, jovens e famílias em situação de vulnerabilidade.\n\n"
        "Seu principal objetivo é transformar vidas através da educação, solidariedade, inclusão social e geração de oportunidades."
    )


def doacao():
    return (
        "DOAÇÃO\n\n"
        "Ajude a ONG Fazendo a Diferença através do PIX.\n\n"

        f"PIX: {PIX_ONG}\n\n"

        "Qualquer valor já faz a diferença na vida de muitas famílias."
    )


def projetos():
    return (
        "PROJETOS DA ONG\n\n"

        "Plataforma: Cursos Presencial e Online\n"
        "Cursos profissionalizantes e capacitação para jovens e adultos.\n\n"

        "Fábrica de Sonhos\n"
        "Festa de 15 anos, ações sociais e realização de sonhos.\n\n"

        "Sustentabilidade\n"
        "Oficinas de reaproveitamento e conscientização ambiental.\n\n"

        "Doações\n"
        "Entrega de cestas básicas, alimentos e campanhas solidárias.\n\n"

        "Incentivo ao Esporte\n"
        "Projetos esportivos em parceria com iniciativas sociais.\n\n"

        "Saúde e Bem Estar\n"
        "Campanhas Setembro Amarelo, Outubro Rosa e ações de saúde.\n\n"

        "Florescer\n"
        "Atividades no contraturno escolar para crianças e adolescentes.\n\n"

        "Mulheres Empreendedoras\n"
        "Workshops, palestras e treinamentos para mulheres.\n\n"

        "Capacitando\n"
        "Mentorias, workshops e visitas corporativas.\n\n"

        "Cozinha Solidária\n"
        "Distribuição de alimentação para famílias em vulnerabilidade."
    )


def contatos():
    return (
        "CONTATOS\n\n"

        f"Telefone:\n{TELEFONE_ONG}\n\n"

        f"E-mail:\n{EMAIL_ONG}\n\n"

        "SEDE:\n"
        "R. Porto Alegre, 179 - Parque Jandaia,\n"
        "Guarulhos - SP, 07261-080\n\n"

        "Escritório Central:\n"
        "SumForces Coworking - R. Três Marias, 22,\n"
        "Sala 12 Dubai - Centro,\n"
        "Guarulhos - SP, 07110-170\n\n"

        "Endereço - Guarulhos:\n"
        "Rua Cannes, 06 Água Azul - Guarulhos\n"
        "CEP 07224-110\n\n"

        "Endereço Jd das Pedras - SP:\n"
        "Rua Coronal Sezefredo Fagundes, 6928\n"
        "Jd das Pedras - SP\n"
        "CEP 02366-000\n\n"

        f"Instagram:\n{INSTAGRAM_ONG}"
    )


def processar_mensagem(msg):

    if not msg or msg.strip() == "":
        return menu()

    msg = msg.lower().strip()

    if msg in ["menu", "oi", "olá", "ola", "iniciar"]:
        return menu()

    elif msg == "1":
        return sobre_ong()

    elif msg == "2":
        return doacao()

    elif msg == "3":
        return projetos()

    elif msg == "4":
        return contatos()

    else:
        return (
            "Opção inválida.\n\n"
            "Digite MENU para voltar ao menu principal."
        )


@app.route("/whatsapp", methods=["POST"])
def whatsapp():

    msg = request.form.get("Body", "")

    resposta = processar_mensagem(msg)

    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)

    return Response(str(twilio_resp), mimetype="application/xml")


@app.route("/")
def home():
    return "Bot da ONG Fazendo a Diferença ativo!"


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
