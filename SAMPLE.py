

# from bardapi import Bard

token = 'dwgPH_3EK0bLRMBD-7nM0jGIdJq62s0Gzg7FEGckbc26gmzGXbHI9Zb18e1NzgrPSM5e6w.'
# bard = Bard(token=token)
# print(bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content'])

from bardapi import Bard

bard = Bard(token=token)
res = bard.get_answer("Do you like cookies?")
print(res['content'])

# from bardapi import Bard

# bard = Bard(token='xxxxxxx')
# audio = bard.speech('Hello, I am Bard! How can I help you today?')
# with open("speech.ogg", "wb") as f:
#   f.write(bytes(audio['audio']))

# https://chat-bot-compitation.vercel.app/