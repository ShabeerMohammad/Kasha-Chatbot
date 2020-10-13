from flask import render_template,request,Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)
bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.MongoDatabaseAdapter")
bot = ChatterBotCorpusTrainer(bot)
bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == '__main__':
    app.run(debug=True)
    