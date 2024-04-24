import discord
from discord.ext import commands
from discord.ui import Button

# Lógica do Formulário de Email
class email_form(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Email de Aquisição do Curso.")

    email_input = discord.ui.TextInput(label="Email", placeholder="Exemplo: Exemplo@gmail.com")
    async def on_submit(self, interect:discord.Interaction):
        await interect.response.send_message(f"Email informado {self.email_input}", ephemeral = True)

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
async def on_member_join(member: discord.Member):
    # Identificando o Canal de Recepção
    channel = bot.get_channel(1230590230323793995)

    # Título e Descrição
    my_embed = discord.Embed(title=f"Bem-vindo(a) ao Servidor Desenvolvedor(a), {member.name}!")
    my_embed.description = """Para garantir acesso ao servidor, basta clicar no botão abaixo e preencher o formulário com seu e-mail vinculado à compra. Seu acesso será liberado automaticamente.

    Caso ocorra algum erro, entre em contato com nosso suporte!"""

    # Tratamento de Imagens e Visual de Embed
    image_author = discord.File('images/lucas_developer.png', 'lucas_developer.png')
    my_embed.set_author(name="Lucas Batista", url='https://febatisplay.com/', icon_url='attachment://lucas_developer.png')
    image_thumbnail = discord.File('images/simple_thumbnail.jpeg', 'simple_thumbnail.jpeg')
    my_embed.set_thumbnail(url="attachment://simple_thumbnail.jpeg")
    my_embed.color = discord.Color.dark_green()
    my_embed.set_footer(text="Foco nos Estudos, Boa Sorte!")

    # Função para criar o botão
    async def button(ctx: commands.Context):
        async def response_button(interact:discord.Interaction):
            await interact.response.send_modal(email_form())
        view = discord.ui.View()
        acess_button = Button(label="Acessar!", style=discord.ButtonStyle.green, emoji="✔️", custom_id="acessar_button")
        acess_button.callback = response_button
        support_button = Button(label="Suporte.", url="https://discord.com/channels/1230590230323793992/1232132723888619560", style=discord.ButtonStyle.link, emoji="💬")

        # Adicionando o botão de acesso
        view.add_item(acess_button)  
    
        # Adicionando o botão de suporte
        view.add_item(support_button)
        return view

    # Adicionando a visualização com o botão à mensagem de boas-vindas
    view = await button(channel)  # Chamando a função button para obter a visualização
    await channel.send(files= [image_author, image_thumbnail], embed=my_embed, view=view)  # Enviando a mensagem com o embed e a visualização
    
# Enviando uma Mensagem Sempre que o Bot for Inicializado!
@bot.event
async def on_ready():
    print("I'm Ready!")

# Identificando o Bot com o Token de Acesso e Colocando o bot para funcionar!
bot.run("MTIzMDYwMDE2NDg0MzE5MjM1NQ.Gix1Vw.gFCOcnfI2pVzLNOOE2YaKssvCfUo-0KPG4xJXs")


# Verificar lógica de programação para apresentar um comando de input após pressionado botão.
# Verificar como funciona o armazenamento da variável 
# Estudar como utilizar a API do google Sheets