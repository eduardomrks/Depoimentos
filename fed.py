import random
import asyncio
from telethon import TelegramClient, Button

# Informações do seu bot
api_id = '25852424'
api_hash = 'e51922dc0c686c1e19c97d1eadbbd9da'
bot_token = '8011328611:AAG-3kmaQBQOjFCRHUoVAciGS61toL3LKw4'

# Lista de chat_ids
chat_ids = [
    -1002193276009,  # Substitua pelos IDs dos chats corretos
    -1002116848333,
    -1002247874958,
    -1002205711968,
    -1001935737212,
    -1002139156285,  
    -1002140261074,
    -1001910015155,
    -1002108499341,
    -1002376978863,
    -1002151997245, # Novo nono chat_id
]

# Inicializa o cliente do Telegram
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Listas de mensagens e imagens
mensagens = [
    "APOSTE COM SEGURANÇA NAS CASA REGULARIZADAS E GANHE PRÊMIOS INCRÍVEIS! 💰✨",
    "SINAIS QUENTES TODOS OS DIAS! VENHA FAZER PARTE DA VITÓRIA! 🏆🔥",
    "GANHOS ALTOS ESPERAM POR VOCÊ! ENTRE NO JOGO AGORA! 💵⚡",
    "TRANSFORME SUAS APOSTAS EM LUCROS! JUNTE-SE A NÓS! 🚀🎉"
]

# Lista de imagens no formato desejado
imagens = [f"depoi{i:02}.jpg" for i in range(1, 43)]

# Função para enviar depoimento
async def enviar_depoimento():
    ultima_mensagem = None

    # Embaralha a lista de imagens
    imagens_em_uso = imagens.copy()
    random.shuffle(imagens_em_uso)

    for imagem in imagens_em_uso:
        mensagem = f"**{random.choice(mensagens)}**"
        while mensagem == ultima_mensagem:
            mensagem = f"**{random.choice(mensagens)}**"

        ultima_mensagem = mensagem

        # Botões organizados em uma lista de listas para ficarem um embaixo do outro
        botoes = [
            [Button.url("🚨JOGAR AGORA🚨", "https://abre.news/MinutosPagantes")],
            [Button.url("🎁CADASTRE-SE 🎁", "https://abre.news/MinutosPagantes")]
        ]

        # Envia mensagem para cada chat_id na lista
        for chat_id in chat_ids:
            try:
                await client.send_file(
                    chat_id,
                    imagem,
                    caption=mensagem,
                    buttons=botoes
                )
            except Exception as e:
                print(f"Erro ao enviar mensagem para o chat {chat_id}: {e}")

        # Aguarda 3300 segundos (55 minutos) antes do próximo envio
        await asyncio.sleep(3300)

    # Reinicia o processo embaralhando as imagens novamente
    await enviar_depoimento()  # Chama novamente a função para reiniciar o envio

# Executa o script
with client:
    client.loop.run_until_complete(enviar_depoimento())
