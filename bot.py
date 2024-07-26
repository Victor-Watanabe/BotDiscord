import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
from google_sheet import main, secondary

# Lógica do Formulário de Email
class EmailForm(Modal):
    def __init__(self):
        super().__init__(title="Email de Aquisição do Curso.")
        self.email_input = TextInput(label="Email", placeholder="Exemplo: Exemplo@gmail.com", custom_id="email_field")
        self.add_item(self.email_input)  # Certifique-se de adicionar o campo ao modal

    async def on_submit(self, interaction: discord.Interaction):
        user = interaction.user
        email = self.email_input.value
        username = user.name
        reply = main(email, username)
        if not reply:
            await interaction.response.send_message(
                f"Senhor {user}, o email {email} NÃO foi localizado no banco de dados, Favor entre em contato com o nosso canal de Suporte!",
                ephemeral=True)
        else:
            role = user.guild.get_role(123456789012345678)  # Insira o ID correto do role aqui
            await user.add_roles(role)
            await interaction.response.send_message(
                f"Senhor {user}, seu Cadastro foi Concluído, Bem Vindo a Nossa Comunidade!", ephemeral=True)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command()
async def ola(ctx: commands.Context):
    user = ctx.author
    await ctx.reply(f"Hello {user.display_name}!")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel()

    my_embed = discord.Embed(
        title=f"Bem-vindo(a) ao Servidor Desenvolvedor(a){member.name}!",
        description="""Para garantir acesso ao servidor, basta clicar no botão abaixo e preencher o formulário com seu e-mail vinculado à compra. Seu acesso será liberado automaticamente.

Caso ocorra algum erro, entre em contato com nosso suporte!""",
        color=discord.Color.dark_green()
    )

    my_embed.set_footer(text="Foco nos Estudos, Boa Sorte!")

    view = create_button_view()
    await send_welcome_message(channel, my_embed, view)

def create_button_view():
    async def response_button(interact: discord.Interaction):
        await interact.response.send_modal(EmailForm())
        
    async def button_reloading(interact: discord.Interaction):
        my_embed = discord.Embed(
        title=f"Bem-vindo(a) ao Servidor Desenvolvedor(a)",
        description="""Para garantir acesso ao servidor, basta clicar no botão abaixo e preencher o formulário com seu e-mail vinculado à compra. Seu acesso será liberado automaticamente.

Caso ocorra algum erro, entre em contato com nosso suporte!""",
        color=discord.Color.dark_green()
    )

        my_embed.set_footer(text="Foco nos Estudos, Boa Sorte!")
        image_author = discord.File('images/lucas_developer.png', 'lucas_developer.png')
        my_embed.set_author(name="Lucas Batista", url='https://febatisplay.com/', icon_url='attachment://lucas_developer.png')
        image_thumbnail = discord.File('images/simple_thumbnail.jpeg', 'simple_thumbnail.jpeg')
        my_embed.set_thumbnail(url="attachment://simple_thumbnail.jpeg")

        view = create_button_view()
        await interact.response.send_message(files=[image_author, image_thumbnail], embed=my_embed, view=view, ephemeral=True)
        
    view = View()
    reloading_button = Button(label="Recarregar", style=discord.ButtonStyle.blurple, emoji="🔁", custom_id="reloading")
    support_button = Button(label="Suporte", url="https://discord.com/channels/1230590230323793992/1232132723888619560", style=discord.ButtonStyle.link, emoji="💬")
    access_button = Button(label="Acessar!", style=discord.ButtonStyle.green, emoji="✔️", custom_id="access_button")

    access_button.callback = response_button
    reloading_button.callback = button_reloading

    view.add_item(access_button)
    view.add_item(reloading_button)
    view.add_item(support_button)

    return view

async def send_welcome_message(channel, my_embed, view):
    image_author = discord.File('images/lucas_developer.png', 'lucas_developer.png')
    my_embed.set_author(name="Lucas Batista", url='https://febatisplay.com/', icon_url='attachment://lucas_developer.png')
    image_thumbnail = discord.File('images/simple_thumbnail.jpeg', 'simple_thumbnail.jpeg')
    my_embed.set_thumbnail(url="attachment://simple_thumbnail.jpeg")
    await channel.send(files=[image_author, image_thumbnail], embed=my_embed, view=view)

@bot.event
async def on_member_remove(member: discord.Member):
    name = member.name
    secondary(name)

@bot.event
async def on_ready():
    print("I'm Ready!")
# Identificando o Bot com o Token de Acesso e Colocando o bot para funcionar!
bot.run("")


# LEMBRAR DE ALTERAR TODOS OS ID DE COMANDO 
# ORIENTAR O LUCAS DE COLOCAR OS CARGOS EM ORDEM DE DOMINIO!