import discord 
from discord.ext import commands
# access youtube vids:
import youtube_dl
# to play audio files:
from discord import FFmpegPCMAudio
import random
import itertools

# repeat = True
sound1 = 0
sound2 = 0
sound3 = 0
sound4 = 0
sound5 = 0
sound6 = 0
sound7 = 0
sound8 = 0
sound9 = 0
sound10 = 0
sound11 = 0
sound12 = 0
sound13 = 0
sound14 = 0
sound15 = 0
sound15 = 0
sound16 = 0
sound17 = 0
sound18 = 0
sound19 = 0 
sound20 = 0
sound21 = 0
sound22 = 0
sound23 = 0
sound24 = 0
sound25 = 0
sound26 = 0
sound27 = 0
sound28 = 0

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    # adding a check ping command:
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'**Heres the ping!** Latency: {round(commands.Bot.latency * 1000)}ms ')

    # adding a "join" command:
    @commands.command()
    async def join(self,ctx):
        global sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, sound12, sound13, sound14, sound15, sound15, sound16, sound17, sound18, sound19, sound20, sound21, sound22, sound23, sound24, sound25, sound26, sound27, sound28
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            # random audio array:
            audio_file = ['1.wav','2.wav','3.wav','4.wav','5.wav','6.wav','7.wav','8.wav','8.wav','9.wav','9.wav','10.wav','11.wav','12.wav','13.wav','14.wav','15.wav','16.wav','17.wav','18.wav','19.wav','20.wav','21.wav','22.wav','23.wav','24.wav','25.wav','26.wav','27.wav','28.wav']
            randomized = random.SystemRandom()
            item = randomized.choice(audio_file)
            if item == '1.wav':
                sound1 += 1
            if item == '2.wav':
                sound2 += 1
            if item == '3.wav':
                sound3 += 1
            if item == '4.wav':
                sound4 += 1
            if item == '5.wav':
                sound5 += 1
            if item == '6.wav':
                sound6 += 1
            if item == '7.wav':
                sound7 += 1
            if item == '8.wav':
                sound8 += 1
            if item == '9.wav':
                sound9 += 1
            if item == '10.wav':
                sound10 += 1
            if item == '11.wav':
                sound11 += 1
            if item == '12.wav':
                sound12 += 1
            if item == '13.wav':
                sound13 += 1
            if item == '14.wav':
                sound14 += 1
            if item == '15.wav':
                sound15 += 1
            if item == '16.wav':
                sound16 += 1
            if item == '17.wav':
                sound17 += 1
            if item == '18.wav':
                sound18 += 1
            if item == '19.wav':
                sound19 += 1
            if item == '20.wav':
                sound20 += 1
            if item == '21.wav':
                sound21 += 1
            if item == '22.wav':
                sound22 += 1
            if item == '23.wav':
                sound23 += 1
            if item == '24.wav':
                sound24 += 1
            if item == '25.wav':
                sound25 += 1
            if item == '26.wav':
                sound26 += 1
            if item == '27.wav':
                sound27 += 1
            if item == '28.wav':
                sound28 += 1
            print(item)
            voice = await voice_channel.connect()
            # making the bot say something upon entering:
            source = FFmpegPCMAudio(f'{item}')
            voice.play(source)
            return sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, sound12, sound13, sound14, sound15, sound16, sound17, sound18, sound19, sound20, sound21, sound22, sound23, sound24, sound25, sound26, sound27, sound28
        else:
            await ctx.voice_client.move_to(voice_channel)

    # adding a "disconnect" command:
    @commands.command()
    async def d(self,ctx):
        await ctx.voice_client.disconnect()

    # playing new song if new song is added:
    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        # ffmpeg handles the steaming on discord official api:
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        # YDL options for audio format:
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        # streaming the audio:
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            await ctx.channel.send('**Now playing** - ' + info.get('title'))

        # adding to queue:
        # async with ctx.typing():
        #     player = await music.from_url(queue[0], loop=commands.Bot.loop)
        #     vc.play(player, after=lambda e: print('Player error: %s' %e) if e else None)
        # await ctx.send('**Now playing:** {}'.format(player.title))
        # del(queue[0])

    # adding check queue button:
    # @commands.command()
    # async def queue_(self,ctx,url):
    #     global queue
    #     queue.append(url)
    #     await ctx.send(f'`{url}` is added to queue')

    # adding pause button:
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused ⏸")

    # adding resume button:
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resume ▶")

    # adding skip button:
    # @commands.command()
    # async def skip(self,ctx):
    #     vc = ctx.voice_client
    #     if not vc or not vc.is_connected():
    #         return await ctx.send('Not currently playing anything!', delete_after=20)
    #     if vc.is_paused():
    #         pass
    #     elif not vc.is_playing():
    #         return

    # adding talk button:
    @commands.command()
    async def talk(self,ctx):
        global sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, sound12, sound13, sound14, sound15, sound15, sound16, sound17, sound18, sound19, sound20, sound21, sound22, sound23, sound24, sound25, sound26, sound27, sound28
        audio_file = ['1.wav','2.wav','3.wav','4.wav','5.wav','6.wav','7.wav','8.wav','8.wav','9.wav','9.wav','10.wav','11.wav','12.wav','13.wav','14.wav','15.wav','16.wav','17.wav','18.wav','19.wav','20.wav','21.wav','22.wav','23.wav','24.wav','25.wav','26.wav','27.wav','28.wav']
        randomized = random.SystemRandom()
        item = randomized.choice(audio_file)
        audio_source = discord.FFmpegPCMAudio(item)
        if not ctx.voice_client.is_playing():
            print(audio_source)
            ctx.voice_client.play(audio_source, after=None)
            print("audio is done")
            if item == '1.wav':
                sound1 += 1
            if item == '2.wav':
                sound2 += 1
            if item == '3.wav':
                sound3 += 1
            if item == '4.wav':
                sound4 += 1
            if item == '5.wav':
                sound5 += 1
            if item == '6.wav':
                sound6 += 1
            if item == '7.wav':
                sound7 += 1
            if item == '8.wav':
                sound8 += 1
            if item == '9.wav':
                sound9 += 1
            if item == '10.wav':
                sound10 += 1
            if item == '11.wav':
                sound11 += 1
            if item == '12.wav':
                sound12 += 1
            if item == '13.wav':
                sound13 += 1
            if item == '14.wav':
                sound14 += 1
            if item == '15.wav':
                sound15 += 1
            if item == '16.wav':
                sound16 += 1
            if item == '17.wav':
                sound17 += 1
            if item == '18.wav':
                sound18 += 1
            if item == '19.wav':
                sound19 += 1
            if item == '20.wav':
                sound20 += 1
            if item == '21.wav':
                sound21 += 1
            if item == '22.wav':
                sound22 += 1
            if item == '23.wav':
                sound23 += 1
            if item == '24.wav':
                sound24 += 1
            if item == '25.wav':
                sound25 += 1
            if item == '26.wav':
                sound26 += 1
            if item == '27.wav':
                sound27 += 1
            if item == '28.wav':
                sound28 += 1
            
    # to check statistics of audio clip frequency: 
    @commands.command()
    async def check(self,ctx):
        await ctx.channel.send(f'Audio 1: {sound1} \nAudio 2: {sound2} \nAudio 3: {sound3} \nAudio 4: {sound4} \nAudio 5: {sound5} \nAudio 6: {sound6} \nAudio 7: {sound7} \nAudio 8: {sound8} \nAudio 9: {sound9} \nAudio 10: {sound10} \nAudio 11: {sound11} \nAudio 12: {sound12} \nAudio 13: {sound13} \nAudio 14: {sound14} \nAudio 15: {sound15} \nAudio 16: {sound16} \nAudio 17: {sound17} \nAudio 18: {sound18} \nAudio 19: {sound19} \nAudio 20: {sound20} \nAudio 21: {sound21} \nAudio 22: {sound22} \nAudio 23: {sound23} \nAudio 24: {sound24} \nAudio 25: {sound25} \nAudio 26: {sound26} \nAudio 27: {sound27} \nAudio 28: {sound28}')

    # sound board:
    @commands.command() 
    async def ik(self,ctx):
        line1 = discord.FFmpegPCMAudio('21.wav')
        if not ctx.voice_client.is_playing():
            print(line1)
            ctx.voice_client.play(line1, after=None)

    @commands.command() 
    async def ap(self,ctx):
        line2 = discord.FFmpegPCMAudio('3.wav')
        if not ctx.voice_client.is_playing():
            print(line2)
            ctx.voice_client.play(line2, after=None)

    @commands.command() 
    async def n(self,ctx):
        line3 = discord.FFmpegPCMAudio('11.wav')
        if not ctx.voice_client.is_playing():
            print(line3)
            ctx.voice_client.play(line3, after=None)

    @commands.command() 
    async def sir(self,ctx):
        line4 = discord.FFmpegPCMAudio('14.wav')
        if not ctx.voice_client.is_playing():
            print(line4)
            ctx.voice_client.play(line4, after=None)

    @commands.command() 
    async def man(self,ctx):
        line5 = discord.FFmpegPCMAudio('9.wav')
        if not ctx.voice_client.is_playing():
            print(line5)
            ctx.voice_client.play(line5, after=None)


def setup(client):
    client.add_cog(music(client))