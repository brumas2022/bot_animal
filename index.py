import telebot
from telebot import types
import mysql.connector
from datetime import date
import psycopg2




#chave api para o comunica_bot E O PROGRAMA NO GITHUB
##CHAVE_API = "6369586964:AAF2Mstx7eSk2c7B5jeG89snHBWlsv0uxjY" - ANTIGA
CHAVE_API = "6369586964:AAFm3QLWBNnLYUwtl2xyqi0145oYJd8OHNc"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["caes"])
def caes(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde um momento...")
    try:
        connection = psycopg2.connect(
            host='aws-0-sa-east-1.pooler.supabase.com',
            user='postgres.ibhcxtnwnonsnycfgjay',
            password='Hoje#estamos#firmes#como#geleia',
            database='postgres',
            port='5432'

        )

        cursor = connection.cursor()

        comando = f"""SELECT * FROM caninos WHERE genero='macho' and vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        bot.send_message(mensagem.chat.id, "O numero de machos é : " + str(len(resultado)))

        comando = f"""SELECT * FROM caninos WHERE genero='femea' and vivo=True"""
        cursor.execute(comando)
        resultado = cursor.fetchall()
        bot.send_message(mensagem.chat.id, "O numero de femeas é : " + str(len(resultado)))

    except Exception as ex:
        bot.send_message(mensagem.chat.id, ex)


@bot.message_handler(commands=["top"])
def top(mensagem):
    x = mensagem.content_type
    bot.reply_to(mensagem, x)
    print("Deu certo aqui")
    print(x)


@bot.message_handler(commands=["memo"])
def memo(mensagem):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1,input_field_placeholder="escolha sua opcao")
    itembtn1 = types.KeyboardButton('/compras')
    itembtn2 = types.KeyboardButton('/viabilidade')
    itembtn3 = types.KeyboardButton('/autorizacao')
    itenbtn4 = types.KeyboardButton('/solicitacao')

    markup.add(itembtn1, itembtn2, itembtn3, itenbtn4)
    bot.send_message(mensagem.chat.id, "Escolha o assunto do memorando", reply_markup=markup)


@bot.message_handler(commands=["visual"])
def visual(mensagem):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, input_field_placeholder="escolha sua opcao")
    itembtn1 = types.KeyboardButton('/Bob')
    itembtn2 = types.KeyboardButton('/Gorda')
    itembtn3 = types.KeyboardButton('/Jair')
    itenbtn4 = types.KeyboardButton('/Michele')
    itenbtn5 = types.KeyboardButton('/Branquelo')

    markup.add(itembtn1, itembtn2, itembtn3, itenbtn4, itenbtn5)
    bot.send_message(mensagem.chat.id, "Escolha o cachorrinho", reply_markup=markup)



@bot.message_handler(commands=["Gorda", "Bob", "Jair", "Michele", "Branquelo"])
def fotinhas(mensagem):

    dog = mensagem.text
    dog = dog.replace("/", "")
    print(dog)

    try:
        connection = psycopg2.connect(
            host='aws-0-sa-east-1.pooler.supabase.com',
            user='postgres.ibhcxtnwnonsnycfgjay',
            password='Hoje#estamos#firmes#como#geleia',
            database='postgres',
            port='5432'

        )

        cursor = connection.cursor()

        comando = f"""SELECT foto FROM caninos WHERE nome='{dog}'"""
        cursor.execute(comando)
        resultado = cursor.fetchone()

        bot.send_photo(mensagem.chat.id, str(resultado[0]))

    except Exception as ex:
           bot.send_message(mensagem.chat.id, ex)


def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)

def responder(mensagem):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('/memo')
    itembtn2 = types.KeyboardButton('/visual')
    itembtn3 = types.KeyboardButton('/caes')

    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(mensagem.chat.id, "Escolha uma opção", reply_markup=markup)


bot.infinity_polling()
