from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

SITE_ONG = "https://gerandofalcoes.com"


def menu():
    return (
        "Bem-vindo à ONG Geraldo Falcões\n\n"
        "Digite uma opção:\n"
        "1 - Sobre a ONG\n"
        "2 - Doações\n"
        "3 - Projetos\n"
        "MENU - Voltar"
    )


def sobre_ong():
    return (
        "A Gerando Falcões é uma ONG brasileira com atuação em São Paulo, focada na transformação de comunidades em situação de vulnerabilidade social.\n\n"
        "Desenvolve projetos de educação, combate à fome, inclusão digital e geração de oportunidades.\n\n"
        "Seu objetivo é reduzir desigualdades e criar oportunidades reais para jovens e famílias."

    )


def doacoes():
    return (
        "Para apoiar a ONG, acesse o site oficial:\n\n"
        f"{SITE_ONG}\n\n"
        "Lá você encontra informações sobre como contribuir."
    )


def projetos():
    return (
        "Projetos da ONG:\n\n"
        "1 - Educação: reforço escolar e apoio pedagógico para crianças e adolescentes.\n"
        "2 - Alimento Solidário: distribuição de cestas básicas para famílias em situação de vulnerabilidade.\n"
        "3 - Jovem Futuro: cursos profissionalizantes para preparação ao mercado de trabalho.\n"
        "4 - Inclusão Digital: aulas de tecnologia, informática e capacitação digital.\n"
        "5 - Ação Social: apoio direto a famílias com necessidades básicas e acompanhamento social."
    )


def processar_mensagem(msg):
    if not msg or msg.strip() == "":
        return "Olá\n\n" + menu()

    msg = msg.lower().strip()

    if msg in ["menu", "oi", "ola", "olá", "iniciar"]:
        return "Olá\n\n" + menu()

    elif msg == "1":
        return sobre_ong()

    elif msg == "2":
        return doacoes()

    elif msg == "3":
        return projetos()

    else:
        return "Opção inválida\nDigite MENU para ver as opções."


@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body", "")
    resposta = processar_mensagem(msg)

    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)

    return Response(str(twilio_resp), mimetype="application/xml")


@app.route("/")
def home():
    return "Bot ativo"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
