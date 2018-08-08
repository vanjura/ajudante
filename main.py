import discord

client = discord.Client()
link_regras = 'http://services.runescape.com/m=clan-forum/l=3/a=869/c=MQSeh4dlhzk/threads.ws?threadid=7ziv'
comandos = 'Os comandos disponiveis são:'
comandos += '\n**adm**\n    - Ver a equipe administrativa do clã'
comandos += '\n**ajuda**\n    - Ver os comandos disponiveis'
comandos += '\n**regras**\n    - Ver as regras do clã'
comandos += '\n**criador**\n    - Ver o nome de meu criador'
comandos += '\n**quem é "nome de um membro"**\n    - Ver informações sobre um membro do clã (para cadastrar ou modificar informações sobre você entre em contato com meu criador)'


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Olá Bot'):
        msg = 'Olá {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
		
	if message.content.startswith('\'-\''):
        msg = 'Enfie no cu esse emoji do caralho.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('Bot, regras'):
        msg = 'As regras se encontram no seguinte link: ' + link_regras
        await client.send_message(message.channel, msg)

    if message.content.startswith('Bot, adm'):
        msg = 'Dona: <@410269554145492993>\n'
        msg += 'Vice: <@466687996649930762>\n'
        msg += 'Fiscal: <@430523864133402645>'
        await client.send_message(message.channel, msg)

    if message.content.startswith('Bot, criador'):
        msg = 'Meu criador é o <@430523864133402645> :heart:'
        await client.send_message(message.channel, msg)

    if message.content.startswith('Bot, ajuda'):
        msg = 'Olá, eu sou <@474629458616123412>\n'
        msg += 'Para usar um comando utilize "Bot, " antes do comando.\n\n'
        msg += comandos
        await client.send_message(message.channel, msg)

    if message.content.startswith('Bot, quem é Lethanus'):
        msg = '<@430523864133402645> é o cara mais lindo do clã, Fiscal do clã, e também é meu criador :heart:'
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=''))
    print('Logado')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDc0NjI5NDU4NjE2MTIzNDEy.DkzHnw.ntlvvsjQq_5fdrEim5Qx01UvPdE')
