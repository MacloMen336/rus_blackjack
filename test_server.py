import random
import pickle
import socket

def rand_deck_of_cards(): #перетасовка колоды
    global deck_of_cards
    random.shuffle(deck_of_cards)
    #--Проверка--
    # global all_cards
    # for i in deck_of_cards:
    #     print(all_cards[i])
    # print('end')

BUFFER_SIZE = 10240 #4096

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
rand_deck_of_cards()

sock = socket.socket()
sock.bind(('26.41.8.62', 9090))
sock.listen(1)
print('Sock name: {}'.format(sock.getsockname()))

while True:
    conn, addr = sock.accept()
    print('Connected:', addr)
    
    print(f'Длинна {len(deck_of_cards)}')
    data = pickle.dumps(deck_of_cards)
    conn.sendall(data)

    # all_data = bytearray()
    # print('a')
    # while True:
    #     data1 = conn.recv(BUFFER_SIZE)
    #     if not data1:
    #         break
    #     #print('Recv: {}: {}'.format(len(data), data))
    #     all_data += data1
    # deck_of_cards = pickle.loads(all_data)
    # print(f'Длинна {len(deck_of_cards)}')

    print('Close')
    conn.close()



# import random
# import pickle
# import socket

# def rand_deck_of_cards(): #перетасовка колоды
#     global deck_of_cards
#     random.shuffle(deck_of_cards)
#     #--Проверка--
#     # global all_cards
#     # for i in deck_of_cards:
#     #     print(all_cards[i])
#     # print('end')

# BUFFER_SIZE = 10240 #4096

# deck_of_cards_default = [
#         ['sixK', 'sevenK','eightK','nineK','tenK','jackK','queenK','kingK','aceK'],
#         ['sixP', 'sevenP','eightP','nineP','tenP','jackP','queenP','kingP','aceP'],
#         ['sixH', 'sevenH','eightH','nineH','tenH','jackH','queenH','kingH','aceH'],
#         ['sixR', 'sevenR','eightR','nineR','tenR','jackR','queenR','kingR','aceR']
#         ]

# deck_of_cards = [] #пересоздание колоды в используемую
# for j in range(0,4,+1):
#     for i in deck_of_cards_default[j]:
#         deck_of_cards.append(i)
# rand_deck_of_cards()

# sock = socket.socket()
# sock.bind(('26.41.8.62', 9090))
# sock.listen(1)
# print('Sock name: {}'.format(sock.getsockname()))

# while True:
#     conn, addr = sock.accept()
#     #print('Connected:', addr)
    
#     #print(f'Длинна {len(deck_of_cards)}')
#     data = pickle.dumps(deck_of_cards)
#     conn.sendall(data)

#     # all_data = bytearray()
#     # while True:
#     #     data1 = conn.recv(BUFFER_SIZE)
#     #     if not data1:
#     #         break
#     #     all_data += data1
    
#     # deck_of_cards = pickle.loads(all_data)

#     #print(f'Длинна {len(deck_of_cards)}')
#     #print('Close')
#     #conn.close()