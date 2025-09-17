from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "Whether you think you can or you think you can't, you're right. - Henry Ford",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "I have learned over the years that when one's mind is made up, this diminishes fear. - Rosa Parks",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "Act as if what you do makes a difference. It does. - William James",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Don't be distracted by criticism. Remember—the only taste of success some people get is to take a bite out of you. - Zig Ziglar",
    "The successful warrior is the average. - Bruce Lee",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "If you really look closely, most overnight successes took a long time. - Steve Jobs",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "Success seems to be connected with action. Successful people keep moving. - Conrad Hilton",
    "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
    "The secret of success is to do the common thing uncommonly well. - John D. Rockefeller Jr.",
    "I never dreamed about success. I worked for it. - Estée Lauder",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't let the fear of losing be greater than the excitement of winning. - Robert Kiyosaki",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn"
]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote, quotes=quotes)

if __name__ == '__main__':
    app.run()