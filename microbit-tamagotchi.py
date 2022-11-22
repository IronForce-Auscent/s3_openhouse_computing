is_dead = True
called = False
game_start = False
fed_count = 1
timer = 0
time_since_last_feed = 0
"""

Defines what events occur

"""

def feed_pet():
    # Feeds the tamagotchi, can only be done a maximum of 5 every 3 minutes
    # WORKING (?)
    global fed_count, timer, time_since_last_feed
    if fed_count <= 5:
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.HAPPY)
        time_since_last_feed = 0
    else:
        basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
        """)
    fed_count += 1
    timer += 10
input.on_button_pressed(Button.A, feed_pet)

def game_init():
    global game_start, called, timer, is_dead
    # Starts up the game, can only be executed once per game, during the beginning
    # WORKING
    if is_dead and not called:
        is_dead = False
        game_start = True
        called = True
        timer = 60
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        . . . . .
        """)
input.on_button_pressed(Button.AB, game_init)

def pet_the_pet():
    global timer
    # Makes the pet happier, increases energy
    # WORKING
    if game_start and not is_dead:
        timer += 20
        basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SHAKE, pet_the_pet)

def on_forever():
    # Controls the main game
    # TESTING
    global fed_count, is_dead, timer, called, time_since_last_feed
    basic.show_leds("""
    . . . . .
    # # . # #
    . . . . .
    . # # # .
    . . . . .
    """)
    if game_start and not is_dead:
        # Let the hunger increase over time
        x = randint(0, 5)
        time_since_last_feed += 1
        if x > 3 and time_since_last_feed > 3:
            fed_count -= 1
        if timer <= 0:
            basic.show_icon(IconNames.SKULL)
            is_dead = True
            called = False
        elif timer > 0 and timer < 20:
            basic.show_icon(IconNames.SAD)
        else:
            timer = timer
        if timer > 0:
            # Reduces the timer
            timer -= 1
            basic.pause(1000)
    else:
        pass
basic.forever(on_forever)

