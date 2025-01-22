import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


states = pandas.read_csv('50_states.csv')
data = states['state']
guess_states = []
guess = True
while guess:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    for i in data:
        if i == answer_state:
            guess_states.append(answer_state)
            data_cor = states[states.state == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(data_cor.x.item(), data_cor.y.item())
            t.write(answer_state)

        else:
            pass

        if answer_state == 'Exit':
            missing_states = [k for k in data if k not in guess_states]

            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv('Missing States')
            guess = False
            break








