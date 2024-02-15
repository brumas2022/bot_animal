import telebot
from telebot import types
import mysql.connector
from datetime import date

import psycopg2




#chave api para o comunica_bot E O PROGRAMA NO GITHUB
##CHAVE_API = "6369586964:AAF2Mstx7eSk2c7B5jeG89snHBWlsv0uxjY" - ANTIGA
CHAVE_API = "6369586964:AAFm3QLWBNnLYUwtl2xyqi0145oYJd8OHNc"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["bob"])
def bob(mensagem):
    bot.send_animation(mensagem.chat.id, 'https://lh3.googleusercontent.com/pw/AIL4fc8Msh2YnD1gFjfQrDc0RjqUhym2gLksZRdl_6fbDMz47bCb1mpaYppPjA_MNpm8xJ_P6sxuzjE95n1UxPLzg5SWzIlXU96oLZHrafmiN86tMxmp7o4YO6PjMcfzciD6zackYRyBmPz6N9B2UIehb5ljBef7aFLBCLucwN25sBnBktdaYbMAHXstbAi6YvDaS0w3ZAr_KcIpl0GZ0y5WP-mYco0EcJD_CRyftsiXQJEoH7nkS3w52msRVxaJxnAv2Mi9SPCXbvjb3P_QlPVvq4fONmk2vrcixq6oufqtrc7onWS8jGLMS96yWDIKLP40Udx5tf6pCFonoGv9kX2E0C6Yqg0Deto3oKvckycOZl1332J5uagL2qd2KwyesOaXjVLvdMG3wIv54b2prBkGvR5847EGPPLeuN5M8qqvMqpXVS0eLglmG5ZZZCRtu-VlrkPzSXTFNvhgG5nKL_OzApJZwj85-sqQyBLrjGLT9tec5wbEy1Ha6fTOE-gxxi-Awyv5Uw7CEagL_OhP7w_At-A_uolJLAUEYajewQsPf1CY8LLQ1UJTp0xftf05ioNf9b6QzNwDd7F43SEyyIt6RWqR96NSg9sxnbbxyS3fqkHP5I1SOJ51139bKQRADosATAHulkkj7GcKh_QuPS1d0pFwearpZdnRAbp8klz-nVl9RkajlbPSyduHyuU3_1ABPPyXhLFMjqy5Mx9vHJInM9aZduwSL1LMKq9pjP8jX4kv-qDY3E4NaILv3QkPUmdlgUCaWYQ4cOZunHPJnGpLiohNdeZg6dKW08O5wo7yKTPMk4yLuutVMao4vvYvnh_6ZGJvfAvEMLUUBrwET1LUS30DotceBmVPXPBT2RzOQuSxevUmgrmemdsUHQ1Ql_2uLctTbzpUBeIMvwIjEEUKNsivqgu4vXRhjb4GrR5n4bPtA1TtPWzOuzIk1A8W=w666-h315-s-no?authuser=0&authuser=0')
    #bot.send_animation(mensagem.chat.id, 'C:/Users/Compras/PycharmProjects/pythonProject/Imagens/img.png')
    #bot.send_photo(mensagem.chat.id, 'C:/Users/Compras/PycharmProjects/pythonProject/Imagens/img.png' )



#@bot.message_handler(content_types=["text"])
#def greetings(mensagem):
#    if mensagem.text.lower() == 'hello':
#        bot.send_message(mensagem.chat.id, f'Hello {mensagem.from_user.first_name}')
#    elif mensagem.text.lower() == 'bye':
#        bot.send_message(mensagem.chat.id, f'Goobye')
#    else:
#        pass

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


@bot.message_handler(commands=["compras","viabilidade","autorizacao",'solicitacao'])
def inserememo(mensagem):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Lula#2022',
        database='new_schema',
    )
    cursor = conexao.cursor()
    entrada = mensagem.from_user.first_name + " " + mensagem.from_user.last_name
    datamem = mensagem.date
    datamem1 = date.fromtimestamp(datamem)


    assunto = mensagem.text
    assunto = assunto.replace("/","") #tira a barra invertida do inicio para gravar no bando de dados



    comando = f'INSERT INTO memorando (data, idservidor, memorandocol) VALUES ("{datamem1}", "{entrada}", "{assunto}")'
    cursor.execute(comando)
    conexao.commit()
    comando = f'SELECT * FROM memorando ORDER BY idmemorando DESC'
    cursor.execute(comando)
    resultado = cursor.fetchone()
    print(resultado)
    # print(mensagem)

    # print(entrada, datamem, datamem1)

    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "Anote o numero do seu memorando:  " + str(resultado[0]))


@bot.message_handler(commands=["memo"])
def memo(mensagem):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1,input_field_placeholder="escolha sua opcao")
    itembtn1 = types.KeyboardButton('/compras')
    itembtn2 = types.KeyboardButton('/viabilidade')
    itembtn3 = types.KeyboardButton('/autorizacao')
    itenbtn4 = types.KeyboardButton('/solicitacao')

    markup.add(itembtn1, itembtn2, itembtn3, itenbtn4)
    bot.send_message(mensagem.chat.id, "Escolha o assunto do memorando", reply_markup=markup)








@bot.message_handler(commands=["retorna","zebu"])
def zebu(mensagem):


    bot.reply_to(mensagem, "Zebu é pra jacu")
    print("Zebu é pra jacu")


    bot.send_photo(mensagem.chat.id, "")




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



    #texto = """
    #Clique em uma das opções
    #/memo - retorna um numero de memorando
    #/oficio - retornar um numero de oficio
    #/random
    #--------------------------------------------------
    #"""
    # bot.reply_to(mensagem, texto)

bot.infinity_polling()
