import discord 
from discord.ext import commands
# access youtube vids:
import youtube_dl
# to play audio files:
from discord import FFmpegPCMAudio
import random
import itertools

repeat = True

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
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            # random audio array:
            audio_file = ['1.wav','2.wav','3.wav','4.wav','5.wav','6.wav','7.wav','8.wav','8.wav','9.wav','9.wav','10.wav','11.wav']
            randomized = random.SystemRandom()
            item = randomized.choice(audio_file)
            print(item)
            voice = await voice_channel.connect()
            # making the bot say something upon entering:
            source = FFmpegPCMAudio(f'{item}')
            voice.play(source)
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


def setup(client):
    client.add_cog(music(client))