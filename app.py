from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

PIX_KEY = "24103596805"


def menu():
    return (
        "Bem-vindo à Gerando Falcões.\n\n"
        "Digite uma opção:\n"
        "1 - Sobre a ONG\n"
        "2 - Doações\n"
        "3 - Projetos\n"
        "4 - Atendente humano"
    )


def sobre_ong():
    return (
        "A Gerando Falcões é uma ONG brasileira com atuação em São Paulo, focada na transformação de comunidades em situação de vulnerabilidade social. "
        "A organização desenvolve projetos de educação, combate à fome, inclusão digital e geração de oportunidades. "
        "Seu objetivo é reduzir desigualdades e criar caminhos reais para que jovens e famílias tenham acesso à educação, trabalho e melhor qualidade de vida."
    )


def doacoes():
    return (
        f"Doações via PIX:\n{PIX_KEY}\n\n"
        "As doações ajudam em projetos de alimentação, educação e inclusão digital para famílias em situação de vulnerabilidade."
    )


def projetos():
    return (
        "Projetos da ONG:\n\n"
        "1 - Educação: reforço escolar para crianças e adolescentes\n"
        "2 - Alimento Solidário: distribuição de cestas básicas\n"
        "3 - Jovem Futuro: cursos profissionalizantes\n"
        "4 - Inclusão Digital: aulas de informática e tecnologia\n"
        "5 - Ação Social: apoio a famílias em vulnerabilidade"
    )


def atendente():
    return "Um voluntário irá te atender em breve."


def opcao_invalida():
    return "Opção inválida. Digite MENU para ver as opções."


def processar_mensagem(msg):
    if not msg:
        return menu()

    msg = msg.lower().strip()

    if msg in ["menu", "oi", "ola", "olá"]:
        return menu()
    elif msg == "1":
        return sobre_ong()
    elif msg == "2":
        return doacoes()
    elif msg == "3":
        return projetos()
    elif msg == "4":
        return atendente()
    else:
        return opcao_invalida()


@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body", "")
    resposta = processar_mensagem(msg)

    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)

    return Response(str(twilio_resp), mimetype="application/xml")


@app.route("/")
def home():
    return "Chatbot ativo"


if __name__ == "__main__":
    app.run(port=5000, debug=True)