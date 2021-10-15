import discord 
from discord.ext import commands
# access youtube vids:
import youtube_dl
# to play audio files:
from discord import FFmpegPCMAudio
import random

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    # adding a "join" command:
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            # random audio array:
            audio_file = ['Wiiliam_Hello.wav', 'Give_a_dam.wav', 'do-you-like-it.wav', 'you-are-acting-so-weird.wav', 'shes-a-crazy-psycho-2.wav', 'oh-thats-okay.wav']
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
    async def disconnect(self,ctx):
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


def setup(client):
    client.add_cog(music(client))