import time
import random
import functools
import turtle
import os.path

MAX_X = 600
MAX_Y = 800
DEFAULT_SIZE = 20
SNAKE_SHAPE = 'square'
HIGH_SCORES_FILE_PATH = './high_scores'
# Controla a velocidade da cobra. Quanto menor o valor, mais rápido é o movimento da cobra.

def load_high_score(state):
    if (os.path.exists(HIGH_SCORES_FILE_PATH)): #verifica se existe ficheiro para abir
        ficheiro=open(HIGH_SCORES_FILE_PATH, 'r')
        state['high_score']=int(ficheiro.read()) #Põe o valor lido no ficheiro em state['high_score']
        ficheiro.close()
    else:
        pass

def write_high_score_to_file(state):
    if (os.path.exists(HIGH_SCORES_FILE_PATH)):  #verifica se existe ficheiro para abir
        ficheiro=open(HIGH_SCORES_FILE_PATH, 'w')
        ficheiro.write(str(state['high_score'])) #Escreve o valor de state['high_score'] no ficheiro
        ficheiro.close()
    else:
        ficheiro=open(HIGH_SCORES_FILE_PATH, 'x') #Cria um novo ficheiro
        high_score=state['high_score']
        ficheiro.write(str(high_score))
        ficheiro.close()

def create_score_board(state):
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.shape("square")
    score_board.color("black")
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, MAX_Y / 2.2)
    state['score_board'] = score_board
    load_high_score(state)
    update_score_board(state)

def update_score_board(state):
    state['score_board'].clear()
    state['score_board'].write("Score: {} High Score: {}".format(state['score'], state['high_score']), align="center", font=("Helvetica", 24, "normal"))

def lose_board(state): #Da print a uma mensagem especifica no board quando o jogador perde
    state['score_board'].clear()
    state['score_board'].write("YOU LOSE!  Your Score Was: {}".format(state['score']), align="center", font=("Helvetica", 24, "normal"))

def win_board(state):#Da print a uma mensagem especifica no board quando o jogador ganha
    state['score_board'].clear()
    state['score_board'].write("CONGRATULATIONS YOU WON!!", align="center", font=("Helvetica", 25, "bold"))


def go_up(state):
    if state['snake']['current_direction'] != 'down':
        state['snake']['current_direction'] = 'up'

def go_down(state):
    if state['snake']['current_direction'] != 'up':
        state['snake']['current_direction'] = 'down'

def go_left(state):
   if state['snake']['current_direction'] != 'right':
        state['snake']['current_direction'] = 'left'

def go_right(state):
    if state['snake']['current_direction'] != 'left':
        state['snake']['current_direction'] = 'right'

def init_state():
    state = {}
    # Informação necessária para a criação do score board
    state['score_board'] = None
    state['new_high_score'] = False
    state['high_score'] = 0
    state['score'] = 0
    # Para gerar a comida deverá criar um nova tartaruga e colocar a mesma numa posição aleatória do campo
    state['food'] = None
    state['window'] = None
    snake = {
        'head': None,                  # Variável que corresponde à cabeça da cobra
        'current_direction': None,     # Indicação da direcção atual do movimento da cobra
        'body' : [],                    # Contem todas as tartatugas que compoem o corpo
        'speed' : 0.5
    }
    state['snake'] = snake
    return state

def setup(state):
    window = turtle.Screen()
    window.setup(width=MAX_X, height=MAX_Y)
    window.listen()
    window.onkey(functools.partial(go_up, state), 'w')
    window.onkey(functools.partial(go_down, state), 's')
    window.onkey(functools.partial(go_left, state), 'a')
    window.onkey(functools.partial(go_right, state), 'd')
    window.tracer(0)
    state['window'] = window
    snake = state['snake']
    snake['current_direction'] = 'stop'
    snake['head'] = turtle.Turtle()
    snake['head'].shape(SNAKE_SHAPE)
    snake['head'].showturtle()
    snake['head'].pu()
    snake['head'].color('green')
    create_score_board(state)
    create_food(state)

def move_head(state):
    head = state['snake']['head']
    direction = state['snake']['current_direction']

    if direction == "up":
        y = head.ycor()
        head.sety(y+20) 
    if direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if direction == "right":
        x = head.xcor()
        head.setx(x+20)
    #nesta função coloca a cabeça da snake um "bloco" para a frente de onjde estava na direção indicada pelo utilizador
def move_body(state):
    body=state['snake']['body']
    head=state['snake']['head']
    
    for i in range(len(body)-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)
    #nesta função faz com que cada bloco do corpo da cobra fique na posição do bloco antes desse. Excepto o promeiro bloco que fica na posição de onde está a cabeça
def create_food(state):
    xcord=random.randint(-270,270)
    ycord=random.randint(-370,370)
    food=turtle.Turtle()
    food.hideturtle()
    food.up()
    food.goto(xcord,ycord) 
    food.down()
    food.dot(20,'red')
    state['food']=food
    #nesta função cria uma tartaruga e duas variaveis com numeros aleatórios e manda a tartaruga para essas coordenadas e desenha um circulo, simbolizando assim a comida que aparece numa zona aleatoria do ecra
def add_body(state):
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")  # tail colour
        new_segment.penup()
        state['snake']['body'].append(new_segment) 

def check_if_food_to_eat(state):
    food = state['food']
    snake=state['snake']['head']
    if snake.distance(food) < 15:
        food.clear()
        state['score']+=10
        state['snake']['speed']-=0.01 #aumenta a velocidade da cobra e consequentemente a dificuldade do jogo
        if (state['score']>state['high_score']):
            state['high_score']=state['score']
            state['new_high_score']=True
        add_body(state)
        update_score_board(state)
        create_food(state)
    #nesta função verifica se a cabeça da tartaruga está a menmos e 15 pixeis da 'comida' e se estiver, cria uma nova comida, aumenta a tartaruga, atualiza o score com +10 e aumenta a velocidade da tartaruga

def boundaries_collision(state):
    snake=state['snake']['head']
    if(snake.xcor()>=MAX_X/2 or snake.ycor()>=MAX_Y/2 or snake.xcor()<=(-MAX_X)/2 or snake.ycor()<=(-MAX_Y)/2):
        return True
        
    return False
    #Verica se a cabeça da tartaruga passa osa limites da tela de jogo

def check_collisions(state):
    head = state['snake']['head']
    body = state['snake']['body']

    for i in body:
        if head.distance(i)<20:
            return True

    return boundaries_collision(state)
    #Verifica se a cabeça da tartaruga colide com o seu corpo

def main():
    state = init_state()
    setup(state)
    while (not check_collisions(state)): #até o jogador perder

        if (state['snake']['speed']==0): #se o jogador ganhar o jogo
            state['window'].update()
            if state['new_high_score']:
                write_high_score_to_file(state)
            win_board(state)
            state['window'].exitonclick()
            return
        
        state['window'].update()
        check_if_food_to_eat(state)
        move_body(state)
        move_head(state)
        time.sleep(state['snake']['speed'])   

    if state['new_high_score']:
        write_high_score_to_file(state)
    lose_board(state)
    state['window'].exitonclick()


main()
