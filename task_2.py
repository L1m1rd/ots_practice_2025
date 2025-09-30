import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5  # сколько витков

    if state == "UP":
        t.forward(10)
        if y >= turn:
            state = "RIGHT"
            t.setheading(0)
            return state, turn
        return state, turn

    if state == "LEFT":
        t.forward(10)
        if x <= -turn:
            state = "UP"
            t.setheading(90)
            return state, turn
        return state, turn

    if state == "DOWN":
        t.forward(10)
        if y <= -turn:
            state = "LEFT"
            t.setheading(180)
            return state, turn
        return state, turn

    if state == "RIGHT":
        t.forward(10)
        if x >= turn:
            state = "DOWN"
            t.setheading(270)
            turn += 1   # <<< добавили шаг спирали
            if turn > num_turns:
                state = "STOP"
            return state, turn
        return state, turn

    if state == "INIT":
        state = "RIGHT"
        t.setheading(0)
        return state, turn

    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)

    turtle.done()


if __name__ == "__main__":
    draw()
