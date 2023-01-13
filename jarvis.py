import os
import openai
import time
import pyfiglet

judul = pyfiglet.figlet_format("Jarvis")
print(judul)
print()
print("*** Anda bertanya, AI menjawab ***")
print()

openai.api_key = "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"

while True:
  ask=input("Masukkan Pertanyaan Anda : ")
  if ask == "cukup":
    print("Oke, Terima Kasih sudah bertanya")
    time.sleep(5)
    os.system('cls')
    break
  print()
  print("Tunggu sebentar, sedang berpikir")
  print()
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= ask,
    temperature=0.9,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  text = response['choices'][0]['text']
  print("Jawaban : " + text)
  print()
