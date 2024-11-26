import discord
from discord.ext import commands
import asyncio
import os
import glob
import json

from config import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    status = "False"
    with open('var/status.txt', 'w') as f:
        f.write(status)
        
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def set_word(ctx, word: str):

    global length
    length = len(word)
    with open('var/length.txt', 'w') as f:
        f.write(str(length))
    with open('var/word.txt', 'w') as f:
        f.write(word)

    if length == 0:
        await ctx.send('Please enter a word')
        return
    elif length == 2:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
    elif length == 3:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
    elif length == 4:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
    elif length == 5:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
        with open('var/char5.txt', 'w') as f:
            f.write(word[4])
    elif length == 6:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
        with open('var/char5.txt', 'w') as f:
            f.write(word[4])
        with open('var/char6.txt', 'w') as f:
            f.write(word[5])
    elif length == 7:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
        with open('var/char5.txt', 'w') as f:
            f.write(word[4])
        with open('var/char6.txt', 'w') as f:
            f.write(word[5])
        with open('var/char7.txt', 'w') as f:
            f.write(word[6])
    elif length == 8:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
        with open('var/char5.txt', 'w') as f:
            f.write(word[4])
        with open('var/char6.txt', 'w') as f:
            f.write(word[5])
        with open('var/char7.txt', 'w') as f:
            f.write(word[6])
        with open('var/char8.txt', 'w') as f:
            f.write(word[7])
    elif length == 9:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
        with open('var/char5.txt', 'w') as f:
            f.write(word[4])
        with open('var/char6.txt', 'w') as f:
            f.write(word[5])
        with open('var/char7.txt', 'w') as f:
            f.write(word[6])
        with open('var/char8.txt', 'w') as f:
            f.write(word[7])
        with open('var/char9.txt', 'w') as f:
            f.write(word[8])
    elif length == 10:
        with open('var/char1.txt', 'w') as f:
            f.write(word[0])
        with open('var/char2.txt', 'w') as f:
            f.write(word[1])
        with open('var/char3.txt', 'w') as f:
            f.write(word[2])
        with open('var/char4.txt', 'w') as f:
            f.write(word[3])
        with open('var/char5.txt', 'w') as f:
            f.write(word[4])
        with open('var/char6.txt', 'w') as f:
            f.write(word[5])
        with open('var/char7.txt', 'w') as f:
            f.write(word[6])
        with open('var/char8.txt', 'w') as f:
            f.write(word[7])
        with open('var/char9.txt', 'w') as f:
            f.write(word[8])
        with open('var/char10.txt', 'w') as f:
            f.write(word[9])
    
    await ctx.send(f'Word was set to {word} with lenght of {length}')

@bot.command()
async def g(ctx, gword: str):

    success = False

    with open('var/status.txt', 'r') as f:
        status = f.read()

    user_id = str(ctx.author.id)

    lives_file = f'var/lives/{user_id}.txt'
    if not os.path.isfile(lives_file):
        with open(lives_file, 'w') as f:
            f.write('5')
    with open(lives_file, 'r') as f:
        lives = f.read()

    if lives == '5':
        lives = 5
    elif lives == '4':
        lives = 4
    elif lives == '3':
        lives = 3
    elif lives == '2':
        lives = 2
    elif lives == '1':
        lives = 1
    elif lives == '0':
        lives = 0

    if lives == 0:
        await ctx.message.add_reaction('💀')
        return

    with open('var/status.txt', 'r') as f:
        status = f.read()

    with open('var/char1.txt', 'r') as f:
        char1 = f.read()
    with open('var/char2.txt', 'r') as f:
        char2 = f.read()
    with open('var/char3.txt', 'r') as f:
        char3 = f.read()
    with open('var/char4.txt', 'r') as f:
        char4 = f.read()
    with open('var/char5.txt', 'r') as f:
        char5 = f.read()
    with open('var/char6.txt', 'r') as f:
        char6 = f.read()
    with open('var/char7.txt', 'r') as f:
        char7 = f.read()
    with open('var/char8.txt', 'r') as f:
        char8 = f.read()
    with open('var/char9.txt', 'r') as f:
        char9 = f.read()
    with open('var/char10.txt', 'r') as f:
        char10 = f.read()

    with open('var/c1.txt', 'r') as f:
        c1 = f.read()
    with open('var/c2.txt', 'r') as f:
        c2 = f.read()
    with open('var/c3.txt', 'r') as f:
        c3 = f.read()
    with open('var/c4.txt', 'r') as f:
        c4 = f.read()
    with open('var/c5.txt', 'r') as f:
        c5 = f.read()
    with open('var/c6.txt', 'r') as f:
        c6 = f.read()
    with open('var/c7.txt', 'r') as f:
        c7 = f.read()
    with open('var/c8.txt', 'r') as f:
        c8 = f.read()
    with open('var/c9.txt', 'r') as f:
        c9 = f.read()
    with open('var/c10.txt', 'r') as f:
        c10 = f.read()
    with open('var/word.txt', 'r') as f:
        word = f.read()

    if c1 == '.':
        c1 = '🔵'
    if c2 == '.':
        c2 = '🔵'
    if c3 == '.':
        c3 = '🔵'
    if c4 == '.':
        c4 = '🔵'
    if c5 == '.':
        c5 = '🔵'
    if c6 == '.':
        c6 = '🔵'
    if c7 == '.':
        c7 = '🔵'
    if c8 == '.':
        c8 = '🔵'
    if c9 == '.':
        c9 = '🔵'
    if c10 == '.':
        c10 = '🔵'

    if status == "True":
        if gword == char1:
            await ctx.message.add_reaction('✔️')
            c1 = char1
            with open('var/c1.txt', 'w', encoding='utf-8') as f:
                f.write(c1)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char2:
            await ctx.message.add_reaction('✔️')
            c2 = char2
            with open('var/c2.txt', 'w', encoding='utf-8') as f:
                f.write(c2)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char3:
            await ctx.message.add_reaction('✔️')
            c3 = char3
            with open('var/c3.txt', 'w', encoding='utf-8') as f:
                f.write(c3)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char4:
            await ctx.message.add_reaction('✔️')
            c4 = char4
            with open('var/c4.txt', 'w', encoding='utf-8') as f:
                f.write(c4)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char5:
            await ctx.message.add_reaction('✔️')
            c5 = char5
            with open('var/c5.txt', 'w', encoding='utf-8') as f:
                f.write(c5)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char6:
            await ctx.message.add_reaction('✔️')
            c6 = char6
            with open('var/c6.txt', 'w', encoding='utf-8') as f:
                f.write(c6)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char7:
            await ctx.message.add_reaction('✔️')
            c7 = char7
            with open('var/c7.txt', 'w', encoding='utf-8') as f:
                f.write(c7)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char8:
            await ctx.message.add_reaction('✔️')
            c8 = char8
            with open('var/c8.txt', 'w', encoding='utf-8') as f:
                f.write(c8)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char9:
            await ctx.message.add_reaction('✔️')
            c9 = char9
            with open('var/c9.txt', 'w', encoding='utf-8') as f:
                f.write(c9)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == char10:
            await ctx.message.add_reaction('✔️')
            c10 = char10
            with open('var/c10.txt', 'w', encoding='utf-8') as f:
                f.write(c10)
            embed3 = discord.Embed(title="Hangman", description=f"You guessed a character correctly\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
            await ctx.reply(embed=embed3)
            success = True
        if gword == word:
            await ctx.message.add_reaction('✔️')

            status = "False"
            with open('var/status.txt', 'w') as f:
                f.write(status)

            files = glob.glob('var/lives/*')
            for f in files:
                os.remove(f)
            
            for i in range(1,11):
                with open(f'var/char{i}.txt', 'w') as f:
                    f.write('')
        
            user = ctx.author.display_name
            embed4 = discord.Embed(title="Hangman Ended", description=f"{user} guessed the correct word and won, the correct word was {word}", color=0x6F8FAF)
            await ctx.reply(embed=embed4)
            success = True
        else:
            if success == True:
                pass
            else:
                await ctx.message.add_reaction('❌')
            
                lives = lives - 1

                with open(lives_file, 'w') as f:
                    json.dump(lives, f)

                if lives == 5:
                    await ctx.message.add_reaction('5️⃣')
                if lives == 4:
                    await ctx.message.add_reaction('4️⃣')
                if lives == 3:
                    await ctx.message.add_reaction('3️⃣')
                if lives == 2:
                    await ctx.message.add_reaction('2️⃣')
                if lives == 1:
                    await ctx.message.add_reaction('1️⃣')
                if lives == 0:
                    await ctx.message.add_reaction('💀')
            

    else:
        await ctx.reply('The game has not started')

@bot.command()
async def start(ctx):
    embed = discord.Embed(title="Hangman", description="Hangman game is starting in 10 sec. Here is how to play:", color=0x6F8FAF)
    embed.add_field(name="1. Game Start", value="When the game begins, the bot will send a message with the word hidden using 🔵 symbols (e.g., 🔵🔵🔵🔵).", inline=False)
    embed.add_field(name="2. Guess a Letter:", value="Type a single letter in the chat (e.g., a). If the letter is in the word, it will be revealed in the appropriate positions (e.g., a🔵🔵🔵). If the letter is not in the word, the bot will react with ❌ and show how many lives you have left. **Note:** All messages not containing space will count as a guess", inline=False)
    embed.add_field(name="Lives:", value="Each player starts with 5 lives. Incorrect guesses will reduce your remaining lives by 1. Once you run out of lives, you can no longer guess.", inline=False)
    embed.add_field(name="Guess the Whole Word:", value="When you think you know the word, type the entire word in lowercase (e.g., word). If you guess correctly, you win the game! If you guess incorrectly, you lose a life.", inline=False)
    embed.add_field(name="Game End:", value="Game ends when someone has guessed the correct word", inline=False)
    await ctx.send(embed=embed)

    await asyncio.sleep(10)

    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global length

    with open('var/length.txt', 'r') as f:
        length = int(f.read())

    if length ==2:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = ''
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = ''
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = ''
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = ''
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = ''
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = ''
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==3:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = ''
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = ''
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = ''
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = ''
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = ''
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==4:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = ''
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = ''
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = ''
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = ''
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==5:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = '.'
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = ''
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = ''
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = ''
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==6:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = '.'
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = '.'
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = ''
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = ''
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==7:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = '.'
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = '.'
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = '.'
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = ''
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==8:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = '.'
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = '.'
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = '.'
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = '.'
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = ''
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==9:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = '.'
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = '.'
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = '.'
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = '.'
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = '.'
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = ''
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)
    elif length ==10:
        c1 = '.'
        with open('var/c1.txt', 'w', encoding='utf-8') as f:
            f.write(c1)
        c2 = '.'
        with open('var/c2.txt', 'w', encoding='utf-8') as f:
            f.write(c2)
        c3 = '.'
        with open('var/c3.txt', 'w', encoding='utf-8') as f:
            f.write(c3)
        c4 = '.'
        with open('var/c4.txt', 'w', encoding='utf-8') as f:
            f.write(c4)
        c5 = '.'
        with open('var/c5.txt', 'w', encoding='utf-8') as f:
            f.write(c5)
        c6 = '.'
        with open('var/c6.txt', 'w', encoding='utf-8') as f:
            f.write(c6)
        c7 = '.'
        with open('var/c7.txt', 'w', encoding='utf-8') as f:
            f.write(c7)
        c8 = '.'
        with open('var/c8.txt', 'w', encoding='utf-8') as f:
            f.write(c8)
        c9 = '.'
        with open('var/c9.txt', 'w', encoding='utf-8') as f:
            f.write(c9)
        c10 = '.'
        with open('var/c10.txt', 'w', encoding='utf-8') as f:
            f.write(c10)

    if c1 == '.':
        c1 = '🔵'
    if c2 == '.':
        c2 = '🔵'
    if c3 == '.':
        c3 = '🔵'
    if c4 == '.':
        c4 = '🔵'
    if c5 == '.':
        c5 = '🔵'
    if c6 == '.':
        c6 = '🔵'
    if c7 == '.':
        c7 = '🔵'
    if c8 == '.':
        c8 = '🔵'
    if c9 == '.':
        c9 = '🔵'
    if c10 == '.':
        c10 = '🔵'
    

    embed2 = discord.Embed(title="Hangman", description=f"Guess the word by sending one and one character in this channel\n\n{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}{c9}{c10}", color=0x6F8FAF)
    await ctx.send(embed=embed2)
    status = "True"
    with open('var/status.txt', "w") as f:
        f.write(status)

@bot.command()
async def stop(ctx):
    status = "False"
    with open('var/status.txt', 'w') as f:
        f.write(status)

    files = glob.glob('var/lives/*')
    for f in files:
        os.remove(f)
    
    await ctx.reply('Game stopped')

    for i in range(1,11):
        with open(f'var/char{i}.txt', 'w') as f:
            f.write('')

bot.run(token)

