import requests
import json
from bs4 import BeautifulSoup as bs
import threading
import time
import names
import random
import datetime
import discord
from discord.ext.commands import Bot
from discord.ext import commands



client=Bot('!')

client.remove_command('help')

@client.event
async def on_ready():
    print('The bot is up')

@client.command(pass_context=True)
async def krispy(ctx,catchall):
    author = ctx.message.author
    with requests.Session() as s:
        url = "https://www.krispykreme.com/account/create-account"
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        result = s.get(url, headers=headers)
    
        url2 = 'https://www.krispykreme.com/account/create-account'
        headers2 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'dnt': '1',
        'origin': 'https://www.krispykreme.com',
        'referer': 'https://www.krispykreme.com/account/create-account',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        soup = bs(result.text, "lxml")
        csrf = soup.findAll('input', {'id':'__CMSCsrfToken'})[0]['value']
        viewstate = soup.findAll('input', {'id':'__VIEWSTATE'})[0]['value']
        evalid = soup.findAll('input', {'id':"__EVENTVALIDATION"})[0]['value']
        realemail = "{}@{}".format(str(random.randint(1111111, 999999999)), catchall)
        data = {
        '__CMSCsrfToken': str(csrf),
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': str(viewstate),
        'lng': 'en-US',
        '__VIEWSTATEGENERATOR': '921C936E',
        '__EVENTVALIDATION': str(evalid),
        'ctl00$plcMain$txtFirstName': names.get_first_name(),
        'ctl00$plcMain$txtLastName': names.get_last_name(),
        'ctl00$plcMain$txtBirthday': datetime.datetime.today().strftime('%m/%d'),
        'ctl00$plcMain$txtZipCode': '90210',
        'ctl00$plcMain$ucPhoneNumber$txt1st': str(random.randint(111, 999)),
        'ctl00$plcMain$ucPhoneNumber$txt2nd': str(random.randint(111, 999)),
        'ctl00$plcMain$ucPhoneNumber$txt3rd': str(random.randint(1111, 9999)),
        'ctl00$plcMain$txtEmail': realemail,
        'ctl00$plcMain$txtPassword': 'awodkawokdw!!1D',
        'ctl00$plcMain$txtPromoCode':'',
        'ctl00$plcMain$cbTermsOfUse': 'on',
        'ctl00$plcMain$btnSubmit': 'Sign Up'
        }
        newres = s.post(url2, data = data, headers=headers2)
        if newres.url == "https://www.krispykreme.com/account/profile":
            embed = discord.Embed(
            colour = discord.Colour.dark_blue()
            )
            embed.add_field(name='Krispy Kreme Account Details', value='Donuts can take a few hours to appear. You will get an email and the free donut will be in your offers tab')
            embed.add_field(name='Email', value=vemail, inline=False)
            embed.add_field(name='Password', value='awodkawokdw!!1D', inline=False)
            embed.set_footer(text='@preorderd')
            await client.say('Account generated successfully! Check your dm for login details.')
            await client.send_message(author, embed=embed)
        else:
            await client.say('Oh no! An error occurred.')
client.run('Your Bot Token Here')
