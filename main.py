import discord
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def get_champion_info():
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://u.gg")
  client = discord.Client()


@client.event
async def on_ready():
  print("We have logged in as {0.user}.format(client)")

@client.event
async def on_message(message):
  # Makes sure the message isn't the bot
  if message.author == client.user:
    return

  if message.content == "$u.gg":
    await message.channel.send("Welcome to the u.gg bot! This bot provides you a screenshot of champion information from the u.gg website. To start, type '$u.gg help'")

  if message.content == "$u.gg help":
    await message.channel.send("Command format:\n '$u.gg <game mode> <champion>'\n Example: '$u.gg aram masteryi'")

  split_msg = message.content.split()

  game_mode = split_msg[1]
  champion = split_msg[2]



# Makes sure no one can get the token for my bot
client.run(os.getenv("DISCORD_TOKEN"))

