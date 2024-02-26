import random
import telebot
import executor
from telebot import types

# Создаем бота с токеном
bot = telebot.TeleBot("6552714340:AAE-YwKIZTRU_XtfHp6DXG_OIoeIoJwvx5I")

# Список вопросов и ответов
questions = [
    {
        'question': 'Какая планета самая близкая к солнцу?',
        'answer': 'Меркурий'
    },
    {
        'question': 'Сколько планет в солнечной системе?',
        'answer': '8'
    },
    {
        'question': 'На какой планете мы живем?',
        'answer': 'Земля'
    },
    {
        'question': 'Самая большая планета солнечной системы?',
        'answer': 'Юпитер'
    },
    {
        'question': 'В каком году человек впервые полетел в космос?',
        'answer': '1961'
    },
    {
        'question': 'Последняя по удаленности от солнца?',
        'answer': 'Нептун'
    },
    {
        'question': 'Газовый гигант, наполненный в основном водородом и гелием?',
        'answer': 'Уран'
    },
    {
        'question': 'В каком году полетел первый спутник?',
        'answer': '1957'
    }
]


# Обработчик команды /question
@bot.message_handler(commands=["question"])
def question(message):
    # Выбор случайного вопроса
    random_question = random.choice(questions)
    bot.send_message(message.chat.id, random_question['question'])

    # Сохранение правильного ответа для проверки
    bot.register_next_step_handler(message, check_answer, random_question['answer'])


# Обработчик ответов пользователя
def check_answer(message, correct_answer):
    user_answer = message.text.lower()

    if user_answer == correct_answer.lower():
        bot.send_message(message.chat.id, 'Правильно!')
    else:
        bot.send_message(message.chat.id, f'Неправильно. Правильный ответ: {correct_answer}')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Выберите режим:")
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(types.KeyboardButton('Учения'), types.KeyboardButton('Тест'))
    bot.send_message(message.chat.id, 'Выберите режим:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Учения')
def mode_1(message):
    bot.reply_to(message, "Чтобы начать учение напишите /learn")


@bot.message_handler(func=lambda message: message.text == 'Тест')
def mode_2(message):
    bot.reply_to(message, "Чтобы начать тест напишите /question")


@bot.message_handler(commands=['learn'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Меркурий')
    button2 = types.KeyboardButton('Венера')
    button3 = types.KeyboardButton('Земля')
    button4 = types.KeyboardButton('Марс')
    button5 = types.KeyboardButton('Юпитер')
    button6 = types.KeyboardButton('Сатурн')
    button7 = types.KeyboardButton('Уран')
    button8 = types.KeyboardButton('Нептун')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    bot.send_message(message.chat.id, "Привет! Ты выбрал режим учения|Учись!:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Меркурий':
        bot.send_message(message.chat.id,
                         "Наименьшая планета Солнечной системы и самая близкая к Солнцу. Названа в честь древнеримского бога торговли — быстрого Меркурия, поскольку она движется по небу быстрее других планет. Её период обращения вокруг Солнца составляет всего 87,97 земных суток — самый короткий среди всех планет Солнечной системы.")
    elif message.text == 'Венера':
        bot.send_message(message.chat.id,
                         "Вторая по удалённости от Солнца и шестая по размеру планета Солнечной системы, наряду с Меркурием, Землёй и Марсом принадлежащая к семейству планет земной группы. Названа в честь древнеримской богини любви Венеры. По ряду характеристик — например, по массе и размерам — Венера считается «сестрой» Земли.")
    elif message.text == 'Земля':
        bot.send_message(message.chat.id,
                         "Третья по удалённости от Солнца планета Солнечной системы. Самая плотная, пятая по диаметру и массе среди всех планет Солнечной системы и крупнейшая среди планет земной группы, в которую входят также Меркурий, Венера и Марс..")
    elif message.text == 'Марс':
        bot.send_message(message.chat.id,
                         "Это четвертая по удаленности от Солнца планета (четвертая планета Солнечной системы). Марс относится к планетам земной группы и назван в честь древнеримского бога войны, аналога древнегреческому Аресу. У Марса есть два естественных спутника – Фобос и Деймос (обозначают «страх» и «ужас»).")
    elif message.text == 'Юпитер':
        bot.send_message(message.chat.id,
                         "Самая большая планета Солнечной системы, газовый гигант. Его экваториальный радиус равен 71,4 тыс. км, что в 11,2 раза превышает радиус Земли . Юпитер — единственная планета, у которой центр масс с Солнцем находится вне Солнца и отстоит от него примерно на 7 % солнечного радиуса.")
    elif message.text == 'Сатурн':
        bot.send_message(message.chat.id,
                         "Газовый гигант, наполненный в основном водородом и гелием. Его размеры позволяют разместить в себе 760 планет типа Земли, а масса больше земной в 95 раз. У Сатурна самая низкая плотность. Осевой оборот Сатурна 10 с половиной часов.")
    elif message.text == 'Уран':
        bot.send_message(message.chat.id,
                         "Планета Солнечной системы, седьмая по удалённости от Солнца, третья по диаметру и четвёртая по массе. Была открыта в 1781 году английским астрономом Уильямом Гершелем и названа в честь греческого бога неба Урана.")
    elif message.text == 'Нептун':
        bot.send_message(message.chat.id,
                         "Непту́н — восьмая и самая дальняя от Солнца планета Солнечной системы. Его масса превышает массу Земли в 17,2 раза и является третьей среди планет Солнечной системы, а по экваториальному диаметру Нептун занимает четвёртое место, превосходя Землю в 3,9 раза. Планета названа в честь Нептуна — римского бога морей.")
    else:
        bot.send_message(message.chat.id, "Я не понимаю вашего сообщения.")

        # Запускаем бота
bot.polling()