# Env var set up
from decouple import config

# Selenium to run Chrome
from selenium import webdriver
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('D:\Chromedriver\chromedriver_win32\chromedriver.exe', options=op)

# Webpage
driver.get("https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=brand_facet%3DBrand~NVIDIA&st=rtx+3080")

# Cache out of stock page text
outOfStockString = 'This item is currently sold out but we are working to get more inventory.'

# Discord set up
import discord
from discord.ext import tasks
# KEY is in an environment variable passed from a .env file (be sure to add that .env file to .gitignore)
TOKEN = config('KEY')
client = discord.Client()

# Register an event
@client.event
async def on_ready():
  checkGpuStockLoop.start()

# Repeat every 5 minutes
@tasks.loop(seconds = 300) 
async def checkGpuStockLoop():
    driver.refresh()
    gpuSpans = driver.find_elements_by_xpath("//*[@class='fulfillment-fulfillment-summary']//span")
    channel = client.get_channel(907044147532288050) # Discord channel to send message to

    # A message will only be sent if a GPU is in stock, otherwise it will run silently in the background.
    if any(gpu.text != outOfStockString for gpu in gpuSpans):
        await channel.send('A GPU is in stock! https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=brand_facet%3DBrand~NVIDIA&st=rtx+3080')

client.run(TOKEN)