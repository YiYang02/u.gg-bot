import discord
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Constant Variables
GAMEMODES = set(["normals", "aram"])
CHAMPIONS = set(['aatrox', 'ahri', 'akali', 'akshan', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelionsol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'chogath', 'corki', 'darius', 'diana', 'drmundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 'jax', 'jayce', 'jhin', 'jinx', 'kaisa', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'khazix', 'kindred', 'kled', 'kogmaw', 'leblanc', 'leesin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'masteryi', 'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunuandwillump', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', 'reksai', 'rell', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahmkench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'velkoz', 'vi', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xayah', 'xerath', 'xinzhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'ziggs', 'zilean', 'zoe', 'zyra'])


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


def get_champion_png(gamemode, champion, PNG_PATH):

  if gamemode == "normals":
    website = "https://u.gg/lol/champions/" + champion + "/build"

  elif gamemode == "aram":
    website = "https://u.gg/lol/champions/aram/" + champion + "-aram"

  driver.get(website)
  print("Opened " + website)

  # Gets the champion tier
  tier = driver.find_element_by_class_name("tier-header").text

  driver.execute_script("window.scrollTo(0, 500)") 
  driver.save_screenshot(PNG_PATH)


  driver.quit()
  print("Driver has quit")

  return tier


client = discord.Client()

@client.event
async def on_ready():
  print("Bot has logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  # Makes sure the message isn't the bot
  if message.author == client.user:
    return

  if message.content == "$u.gg":
    await message.channel.send("Welcome to the u.gg bot! This bot provides you a screenshot of champion information from the u.gg website. To start, type '$u.gg help'")
    return

  if message.content == "$u.gg help":
    await message.channel.send("Command format:\n '$u.gg <game mode> <champion>'\n Example: '$u.gg aram masteryi'\n Example: '$u.gg normals masteryi' ")
    return

  if message.content.startswith("$u.gg aram") or message.content.startswith("$u.gg normals"):
    split_msg = message.content.split()

    # Pre-processing text
    game_mode = split_msg[1].lower().strip()
    champion = split_msg[2].lower().strip()

    print(game_mode)
    print(champion)

    if game_mode in GAMEMODES and champion in CHAMPIONS:
      PNG_PATH = game_mode + "_" + champion + ".png"
      await message.channel.send("Getting champion information, please wait...")
      # Gets the tier of the champion
      tier = get_champion_png(game_mode, champion, PNG_PATH)
      # Uploads the image to the discord server
      await message.channel.send("Champion information for: " + champion)
      await message.channel.send("Tier: " + tier)
      await message.channel.send(file=discord.File(PNG_PATH))

      
# Makes sure no one can get the token for my bot
client.run(os.environ['DISCORD_TOKEN'])

