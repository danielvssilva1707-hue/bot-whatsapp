from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

SITE_ONG = "https://gerandofalcoes.com"


def menu():
    return (
        "Bem-vindo à ONG Gerando Falcões\n\n"
        "Digite uma opção:\n"
        "1 - Sobre a ONG\n"
        "2 - Doações\n"
        "3 - Projetos\n\n"
        "Digite MENU para voltar"
    )


def sobre_ong():
    return (
        "A Gerando Falcões é uma ONG brasileira que atua na transformação de comunidades em situação de vulnerabilidade social.\n\n"
        "Trabalha com educação, combate à fome, inclusão digital e geração de oportunidades.\n\n"
        "Objetivo: reduzir desigualdades e gerar oportunidades reais."
    )


def doacoes():
    return (
        "Para apoiar a ONG, acesse:\n\n"
        f"{SITE_ONG}\n\n"
        "Sua ajuda faz a diferença!"
    )


def projetos():
    return (
        "Projetos da ONG:\n\n"
        "1 - Educação\n"
        "Reforço escolar e apoio pedagógico para crianças e adolescentes.\n\n"

        "2 - Alimento Solidário\n"
        "Distribuição de cestas básicas para famílias em situação de vulnerabilidade.\n\n"

        "3 - Jovem Futuro\n"
        "Cursos profissionalizantes para preparação ao mercado de trabalho.\n\n"

        "4 - Inclusão Digital\n"
        "Aulas de tecnologia, informática e capacitação digital.\n\n"

        "5 - Ação Social\n"
        "Apoio direto a famílias com necessidades básicas e acompanhamento social."
    )


def processar_mensagem(msg):
    if not msg:
        return menu()

    msg = msg.lower().strip()

    if msg in ["menu", "oi", "ola", "olá", "iniciar"]:
        return menu()

    elif msg == "1":
        return sobre_ong()

    elif msg == "2":
        return doacoes()

    elif msg == "3":
        return projetos()

    else:
        return "Opção inválida.\nDigite MENU para ver as opções."


@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    try:
        msg = request.form.get("Body", "")
        print(f"Mensagem recebida: {msg}")

        resposta = processar_mensagem(msg)

        twilio_resp = MessagingResponse()
        twilio_resp.message(resposta)

        return Response(str(twilio_resp), mimetype="application/xml")

    except Exception as e:
        print(f"Erro: {e}")

        twilio_resp = MessagingResponse()
        twilio_resp.message("Erro interno. Tente novamente.")

        return Response(str(twilio_resp), mimetype="application/xml")


@app.route("/")
def home():
    return "Bot ativo "


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
