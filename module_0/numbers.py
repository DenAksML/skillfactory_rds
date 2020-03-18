import numpy as np

def game_core_v3(number):
    count = 0
    predict =50.0
    delta = predict
    while number != int(predict):
        count+=1
        delta /= 2
        if number > predict: 
            predict += delta
        elif number < predict: 
            predict -= delta
    return(count) # выход из цикла, если угадали      
        
def score_game():
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game()