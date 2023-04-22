from tkinter import *
from tkinter import ttk
import random
from PIL import ImageTk, Image
import tkinter.messagebox as mb

import time

def MakeTexture():
    global texture
    # global back_of_card

    im = Image.open("res\cards_texturs_rus.png") #открыть файл текстуру карт
    height = 246 #высота
    width = 158 #ширина
    for j in range(0,4,+1):
        for i in range(0,9,+1): #внести
            crop_rectangle1 = (width*i, height*j, width*(i+1), height*(j+1))
            cropped_im1 = im.crop(crop_rectangle1)
            texture.append(cropped_im1)

    # im1 = Image.open("res\cards_texturs.png")
    # crop_rectangle1 = (width*2, height*4, width*3, height*5)
    # back_of_card = im1.crop(crop_rectangle1)
    #back_of_card.show()
            

def take_card(): #взять ещё карту
    global deck_of_cards, my_cards_sum, my_cards, texture, canv
    global canvas1, bg, img1, fWidth
    global all_cards

    my_cards.append(deck_of_cards[0])
    my_cards_sum = my_cards_sum + all_cards[deck_of_cards[0]]
    img1.clear()
    canv.delete("all")
    for i in range(0,len(my_cards),+1):
        img1.append(ImageTk.PhotoImage(texture[list(all_cards).index(my_cards[i])]))
        canv.create_image(14+((fWidth/2+79)/(len(my_cards)+1)*(i)),14,image=img1[i],anchor=NW)
        
        #--test--
        # print(texture[0][list(cards).index(my_cards[i])])
        # print(img1)
        # print(i)
        # print(my_cards[i])
    deck_of_cards.pop(0)
    my_cards_lbl.configure(text=f"Мои карты: {my_cards}")
    card_scors_lbl.configure(text=f"Очков {my_cards_sum}")
    #--test--
    #print('Мои карты: ',my_cards,'\nСумма: ',my_cards_sum) #Проверка в консоли
    
    if my_cards_sum > 21:
        show_info(0)


def rand_deck_of_cards(): #перетасовка колоды
    global deck_of_cards
    random.shuffle(deck_of_cards)
    #--Проверка--
    # global all_cards
    # for i in deck_of_cards:
    #     print(all_cards[i])
    # print('end')

def new_game(): #игра заново
    global deck_of_cards, my_cards, my_cards_sum, deck_of_cards_default
    global oponent_res
    deck_of_cards = [] #пересоздание колоды в используемую
    for j in range(0,4,+1):
        for i in deck_of_cards_default[j]:
            deck_of_cards.append(i)

    my_cards = []
    my_cards_sum = 0
    my_cards_lbl.configure(text=f"Мои карты: {my_cards}")
    card_scors_lbl.configure(text=f"Очков {my_cards_sum}")
    canv.delete("all")

    rand_deck_of_cards()
    #--тест локального опанента
    oponent_res = random.randint(10,21)
    #print(oponent_res)

    btn1.configure(bg='SystemButtonFace', command=take_card)
    btn3.configure(bg='SystemButtonFace', command=end_game)

def end_game():
    #тест всплывающего окна с проигрышем
    if my_cards_sum > 21:
        show_info(0)
        return 0
    if my_cards_sum > oponent_res:
        show_info(1)
        return 0
    if my_cards_sum < oponent_res:
        show_info(2)
        return 0
    if my_cards_sum == oponent_res:
        show_info(3)
        return 0


def show_info(result): #тест всплывающего окна
    #global btn1, btn3
    match result:
        case 0:
            msg = "Вы проиграли"
        case 1:
            msg = f"Вы выиграли. У опонента {oponent_res} очков"
        case 2:
            msg = f"Вы проиграли. У опонента {oponent_res} очков"
        case 3:
            msg = "Ничья"

    btn1.configure(bg='gray', command='')
    btn3.configure(bg='gray', command='')
    mb.showinfo("Результат", msg)
        

if __name__ == '__main__':
    #--Переменные--
    #cards = {'six':6, 'seven':7,'eight':8,'nine':9,'ten':10,'jack':2,'queen':3,'king':4,'ace':1}
    all_cards ={
                'sixK':6, 'sevenK':7,'eightK':8,'nineK':9,'tenK':10,'jackK':2,'queenK':3,'kingK':4,'aceK':1,
                'sixP':6, 'sevenP':7,'eightP':8,'nineP':9,'tenP':10,'jackP':2,'queenP':3,'kingP':4,'aceP':1,
                'sixH':6, 'sevenH':7,'eightH':8,'nineH':9,'tenH':10,'jackH':2,'queenH':3,'kingH':4,'aceH':1,
                'sixR':6, 'sevenR':7,'eightR':8,'nineR':9,'tenR':10,'jackR':2,'queenR':3,'kingR':4,'aceR':1
                }
    deck_of_cards_default = [
        ['sixK', 'sevenK','eightK','nineK','tenK','jackK','queenK','kingK','aceK'],
        ['sixP', 'sevenP','eightP','nineP','tenP','jackP','queenP','kingP','aceP'],
        ['sixH', 'sevenH','eightH','nineH','tenH','jackH','queenH','kingH','aceH'],
        ['sixR', 'sevenR','eightR','nineR','tenR','jackR','queenR','kingR','aceR']
        ]
    deck_of_cards = [] #пересоздание колоды в используемую
    for j in range(0,4,+1):
        for i in deck_of_cards_default[j]:
            deck_of_cards.append(i)

    my_cards = []
    my_cards_sum = 0

    img1 = [] #глобальный список переменная текстуры 1-ой карты

    fWidth = 500 #Ширина фрейма
    fHeight = 250 #Высота фрейма
    #--тест локального опанента
    oponent_res = random.randint(10,21)

    #--Создание массива текстур
    # back_of_card = 0

    texture = [] #список с текстурами
    MakeTexture()
    #--Вывод списка текстур
    #print(texture)
    #--Перетасовка колоды карт
    rand_deck_of_cards()
    #--Освнова окна
    window = Tk()
    window.title("Игра в 21")
    window.geometry('900x600')
    #--Взятие фона
    bg = ImageTk.PhotoImage(file = "res/backgraund_small_1.png")
    #--Установка фона в холст
    canvas1 = Canvas(window, width = 400,height = 400, bg='black')
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")

    #--Фрэйм и Холст где появляются карты
    f = LabelFrame(window,text="Мои карты",width=fWidth,height=fHeight,background='#986960') # root можно не указывать
    f.place(relx=0.5, rely=0.75,anchor=CENTER)
    canv = Canvas(f,width=fWidth,height=fHeight,background='#986960',bd=10,relief=RIDGE) #,bd=0,relief=RIDGE
    canv.place(x=0, y=0,anchor=SW)
    canv.grid(row=0,column=1)
    #--Фреэм и Хрлст опонента
    # back_of_card1 = ImageTk.PhotoImage(back_of_card)
    # f1 = LabelFrame(window,text="Карты опонента",width=fWidth,height=fHeight,background='#986960') # root можно не указывать
    # f1.place(relx=0.5, rely=0, anchor=N)
    # canv1 = Canvas(f1,width=fWidth,height=fHeight,background='#986960',bd=10,relief=RIDGE) #,bd=0,relief=RIDGE
    # canv1.place(x=0, y=0,anchor=SW)
    # canv1.grid(row=0,column=1)
    # canv1.create_image(12+0,14,image=back_of_card1,anchor=NW)
    # canv1.create_image(12+50,14,image=back_of_card1,anchor=NW)
    # canv1.create_image(12+100,14,image=back_of_card1,anchor=NW)

    #--Текстовые
    my_cards_lbl = Label(window, text="Мои карты",justify='center') 
    my_cards_lbl.place(relx=0.5, rely=0.98,anchor=CENTER)
    card_scors_lbl = Label(window, text=f"Очков {my_cards_sum}",justify='center')
    card_scors_lbl.place(relx=0.9, rely=0.1,anchor=CENTER)
    #--Кнопки
    btn1 = Button(window, text="Ещё карту",command=take_card, cursor='target', font=25,border=5)
    btn1.place(relx=0.9, rely=0.86,anchor=CENTER)
    btn2 = Button(window, text="Начать заново!",command=new_game, cursor='target',border=5)
    btn2.place(relx=0.9, rely=0.92,anchor=CENTER)
    btn3 = Button(window, text="Готов!",command=end_game, cursor='target',border=5)
    btn3.place(relx=0.9, rely=0.80,anchor=CENTER)

    #--тест локального опанента
    #print(oponent_res)

    window.mainloop()

#--Work version only Pic Card--
# from tkinter import *
# from tkinter import ttk
# import random
# from PIL import ImageTk, Image

# def MakeTexture():
#     global texture
#     im = Image.open("res\cards_texturs_rus.png") #открыть файл текстуру карт
#     height = 246 #высота
#     width = 158 #ширина
#     for j in range(0,4,+1):
#         for i in range(0,9,+1): #внести
#             crop_rectangle1 = (width*i, height*j, width*(i+1), height*(j+1))
#             cropped_im1 = im.crop(crop_rectangle1)
#             texture[j].append(cropped_im1)

# def take_card(): #взять ещё карту
#     global deck_of_cards, cards, my_cards_sum, my_cards, texture, canv
#     global canvas1, bg, img1, fWidth
#     my_cards.append(deck_of_cards[0])
#     my_cards_sum = my_cards_sum + cards[deck_of_cards[0]]
    
#     img1.clear()
#     canv.delete("all")
#     # #--work test--
#     # canvas1.delete("all")
#     # canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#     for i in range(0,len(my_cards),+1):
#         img1.append(ImageTk.PhotoImage(texture[0][list(cards).index(my_cards[i])]))
#         canv.create_image(14+((fWidth/2+79)/(len(my_cards)+1)*(i)),14,image=img1[i],anchor=NW)
#         #--test--
#         # print(texture[0][list(cards).index(my_cards[i])])
#         # print(img1)
#         # print(i)
#         # print(my_cards[i])
    
#     deck_of_cards.pop(0)
#     my_cards_lbl.configure(text=f"Мои карты: {my_cards}")
#     card_scors_lbl.configure(text=f"Очков {my_cards_sum}")

#     print('Мои карты: ',my_cards,'\nСумма: ',my_cards_sum) #Проверка в консоли


# def rand_deck_of_cards(): #перетасовка колоды
#     global deck_of_cards, cards
#     random.shuffle(deck_of_cards)
#     #--Проверка--
#     # for i in deck_of_cards:
#     #     print(cards[i])
#     # print('end')

# def new_game(): #игра заново
#     global deck_of_cards, my_cards, my_cards_sum, deck_of_cards_defoult
    
#     deck_of_cards = [] #пересоздание колоды
#     for i in deck_of_cards_defoult:
#         deck_of_cards.append(i)

#     my_cards = []
#     my_cards_sum = 0
#     my_cards_lbl.configure(text=f"Мои карты: {my_cards}")
#     card_scors_lbl.configure(text=f"Очков {my_cards_sum}")
#     #img_card_lbl.configure(image = '')
#     canv.delete("all")

#     rand_deck_of_cards()

# if __name__ == '__main__':
#     #--Переменные--
#     cards = {'six':6, 'seven':7,'eight':8,'nine':9,'ten':10,'jack':2,'queen':3,'king':4,'ace':1}
#     deck_of_cards_defoult = ['six', 'seven','eight','nine','ten','jack','queen','king','ace']
    
#     deck_of_cards = [] #пересоздание колоды в используемую
#     for i in deck_of_cards_defoult:
#         deck_of_cards.append(i)
    
#     my_cards = []
#     my_cards_sum = 0

#     img1 = [] #глобальная переменная текстуры 1-ой карты

#     fWidth = 500 #Ширина фрейма
#     fHeight = 250 #Высота фрейма
#     #--Создание массива текстур
#     texture = [[],[],[],[]] #список с текстурами
#     MakeTexture()
#     #--Перетасовка колоды карт
#     rand_deck_of_cards()
#     #--Вывод списка текстур
#     #print(texture)
#     #--Освнова окна
#     window = Tk()
#     window.title("Игра в 21")
#     window.geometry('900x600')
#     #--Взятие фона
#     bg = ImageTk.PhotoImage(file = "backgraund_small_1.png")
#     #--Установка фона в холст
#     canvas1 = Canvas(window, width = 400,height = 400)
#     canvas1.pack(fill = "both", expand = True)
#     canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#     #--Фрэйм и Холст где появляются карты
#     f = LabelFrame(window,text="Мои карты",width=fWidth,height=fHeight,background='#986960') # root можно не указывать
#     f.place(relx=0.5, rely=0.75,anchor=CENTER)

#     canv = Canvas(f,width=fWidth,height=fHeight,background='#986960',bd=10,relief=RIDGE) #,bd=0,relief=RIDGE
#     canv.place(x=0, y=0,anchor=SW)
#     canv.grid(row=0,column=1)


#     img1.append(ImageTk.PhotoImage(texture[0][8]))
#     img1.append(ImageTk.PhotoImage(texture[0][7]))
#     # canv.create_image(12+0,14,image=img1[0],anchor=NW)
#     # canv.create_image(12+50,14,image=img1[1],anchor=NW)
#     ##canv.create_image(260/len(my_cards)*i,14+123,image=img1[1],anchor=CENTER)
#     # canv.create_image(260,14+123,image=img1[1],anchor=CENTER)
#     # 260/len(my_cards)*i
#     #canv.delete("all")

#     #--Текстовые
#     my_cards_lbl = Label(window, text="Мои карты",justify='center') 
#     my_cards_lbl.place(relx=0.5, rely=0.98,anchor=CENTER)
#     card_scors_lbl = Label(window, text=f"Очков {my_cards_sum}",justify='center')
#     card_scors_lbl.place(relx=0.9, rely=0.1,anchor=CENTER)
#     #--Кнопки
#     # btn = Button(window, text="Перемешать колоду",command=rand_deck_of_cards, cursor='target')
#     # btn.place(relx=0.9, rely=0.8,anchor=CENTER)
#     btn1 = Button(window, text="Ещё карту",command=take_card, cursor='target', font=25,border=5)
#     btn1.place(relx=0.9, rely=0.86,anchor=CENTER)
#     btn2 = Button(window, text="Начать заново!",command=new_game, cursor='target')
#     btn2.place(relx=0.9, rely=0.92,anchor=CENTER)

    

#     window.mainloop()
