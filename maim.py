#escribe en la shell todo esto, te debe crear 2 archivos
#uno Pipfile
#otro Pipfile.lock
#pip install pipenv
#pip install discord.py
#pipeenv shell


import discord
from discord.ext import commands 
from urllib import  parse, request
import  re
import datetime

bot = commands.Bot(command_prefix="!", description="¡Hola soy un bot de ayuda! Te puedo servir en algo")

#bot_status
@bot.command()
async def hola(ctx):
  await ctx.send("Hola mi creador es César Arias.")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def version(ctx):
    await ctx.send("""
    version 0.0.2
    Futura actualizacion muy pronto
    """)

#comanodos_de_ayuda
@bot.command()
async def comandos(ctx):
  await ctx.send("""
  !hola !ping !ip !ayuda !etc !bug !trampa !surgerencia !hacks !otros !modalidades !bedwars !skywars !survival !hardcode !status !reglas !suma !resta !times !divide
  """)

@bot.command()
async def ayuda(ctx):
    await ctx.send("!modalidades" "etc")

@bot.command()
async def etc(ctx):
    await ctx.send("!bug" "!trampa" "!otros" "surgerencia")

#comandos_en_general
@bot.command()
async def ip(ctx):
    await ctx.send("IP: Proximamente")

@bot.command()
async def bug(ctx):
    await ctx.send("Si has encontrado un **BUG** por favor comunicate con un superior")

@bot.command()
async def trampa(ctx):
    await ctx.send("Si has encontrado a un usuario haciendo **TRAMPA** por favor notificalo con un superior")

@bot.command()
async def surgerencia(ctx):
    await ctx.send("Si tienes alguna **SURGERENCIA** hazlo por el canal #comandos , con el comando !suggest")

@bot.command()
async def hacks(ctx):
  await ctx.send("Si has encontrado a un usuario utilizando **HACKS** por favor notificalo con un superior")


@bot.command()
async def otros(ctx):
    await ctx.send("Cualquier consulta ponte en contacto con superior")    


@bot.command()
async def modalidades(ctx):
    await ctx.send("""
    !bedwars! skywars! survival! harcode""")

@bot.command()
async def bedwars(ctx):
    await ctx.send("BEDWARS: Proximamente")

@bot.command()
async def skywars(ctx):
    await ctx.send("SKYWARS: Proximamente")
  
@bot.command()
async def survival(ctx):
  await ctx.sed("SURVIVAL: Proximamente")

@bot.command()
async def hardcode(ctx):
    await ctx.send("HARDCODE: Proximamente")

@bot.command()
async def status(ctx):
    await ctx.send("Status Server: En Mantenimiento")

@bot.command()
async def reglas(ctx):
    await ctx.send("""
    ■ No hacer spam 
    ■ No dejar links
    ■ No insultar 
    ■ Y lo mas importante  divierte y pasa el rato
    """)



#operaciones  
@bot.command()
async def operaciones(ctx):
  await ctx.send("""
  Pon los numeros separados de un espaio
  suma (suma)
  resta (resta)
  divide(divide)
  times (multiplica)
  """)


@bot.command()
async def suma(ctx, uno: int, dos: int):
    await ctx.send(uno + dos)

@bot.command()
async def resta(ctx, uno: int, dos: int):
    await ctx.send(uno - dos)

@bot.command()
async def times(ctx, uno: int, dos: int):
    await ctx.send(uno * dos)

@bot.command()
async def divide(ctx, uno: int, dos: int):
    await ctx.send(uno / dos)

#youtube
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    #print(search_results)
    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])

#eventos
@bot.event
async def on_ready():
    print("El Bot esta listo para su uso!")


bot.run("tu token aqui")
