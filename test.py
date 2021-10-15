import random 

def test():
    audio_file = ['Wiiliam_Hello.wav', 'Give_a_dam.wav']
    randomized = random.SystemRandom()
    item = randomized.choice(audio_file)
    print(item)

test()