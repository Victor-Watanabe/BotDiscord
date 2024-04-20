import discord
from discord.ext import commands

intents = discord.Intents.default()

# Capacitando o Bot Para Leitura de Mensagens
intents.message_content = True

# Capacitando o Bot Para Identificação de Membros do Servidor!
intents.members = True

# Adicionando um Prefixo, ou seja, uma String Para Identificação de Comando, Nesse Caso, "/"
bot = commands.Bot(command_prefix="/", intents=intents)

# Criando Comando Responsivo à Mensagem "ola"
@bot.command()
async def ola(ctx: commands.Context):
    usuario = ctx.author
    await ctx.reply(f"Hello {usuario.display_name}!")

# Criando Embed para Boas Vindas do Usuário
@bot.event
async def on_member_join(member:discord.Member):
    # Identificando o Canal de Recepção
    channel = bot.get_channel(1230590230323793995)

    # Título e Descrição
    my_embed = discord.Embed(title=f"Bem-vindo(a) ao Servidor Desenvolvedor(a), {member.name}!")
    my_embed.description = """Para garantir acesso ao servidor, basta clicar no botão abaixo e informar seu e-mail vinculado à compra, seu acesso será liberado automaticamente.

    Caso ocorra algum erro, entre em contato com nosso suporte!"""

    # Tratamento de Imagens e Visual de Embed
    image_author = discord.File('images/lucas_developer.png', 'lucas_developer.png')
    my_embed.set_author(name="Lucas Batista", url='https://www.instagram.com/lucasbatista.apk/', icon_url='attachment://lucas_developer.png')
    image_thumbnail = discord.File('images/thumbnail.jpeg', 'thumbnail.jpeg')
    my_embed.set_thumbnail(url = "attachment://thumbnail.jpeg")
    my_embed.color = discord.Color.dark_blue()
    my_embed.set_footer(text="Foque nos Estudos, Boa Sorte!")

    await channel.send(files = [image_thumbnail, image_author], embed=my_embed)
    try:
        await member.create_dm()
        await member.dm_channel.send("Olá, sou o Bot do Servidor do Watanabe_Developer. Por favor, digite seu e-mail:")
        print(f'Mensagem enviada para {member.name}')
    except discord.Forbidden:
        print(f'Não foi possível enviar mensagem para {member.name}. Permissão de enviar mensagens diretas pode estar faltando.')


# Verificando o Email Informado
@bot.command()
async def verify(ctx, email):
 print(f"E-mail recebido: {email}")
 await ctx.send("E-mail recebido com sucesso! Aguarde enquanto verificamos sua conta.")

# Enviando uma Mensagem Sempre que o Bot for Inicializado!
@bot.event
async def on_ready():
    print("I'm Ready!")

# Identificando o Bot com o Token de Acesso e Colocando o bot para funcionar!
bot.run("MTIzMDYwMDE2NDg0MzE5MjM1NQ.Gix1Vw.gFCOcnfI2pVzLNOOE2YaKssvCfUo-0KPG4xJXs")

# verificar ephemeral
# Configurar botões de acesso ao formulário e guardar o email em uma variável. 