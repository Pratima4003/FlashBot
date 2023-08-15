#bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat2.txt"

chatbot = ChatBot("Chatpot",
storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm afraid I did not understand this. PLease ask some other question..",
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)
'''trainer.train([
    "Hi",
    "Welcome, friend 😇️",
])
trainer.train([
    "Are you a plant?",
    "please refer to following: https://www.google.com/search?channel=fs&client=ubuntu-sn&q=BTS",
])'''

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("😉️ ")
    if query in exit_conditions:
        break
    else:
        print(f"👾️ {chatbot.get_response(query)}")
