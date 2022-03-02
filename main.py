# This program is a flashcard memorization tool for the
# Pimoroni Pico System, which uses the Raspberry Pi RP2040 chip.

import io
import math
import time
from text_for_main import* # This is for the flashcard information

view = 0
alt_view = 0
view_count = 10 # Update for the number of flashcards
flashcard_topic = "Typewright Tags" # Update this to reflect the flashcard subject


# CONTROLS: Up/Right advance the flashcards and Down/Left goes back
# The A button reveals the hidden flashcard info
# The B button restores the first view of the flashcard
def update(tick):
    global view
    global alt_view

    if(pressed(RIGHT)):
        view += 1
        alt_view = 0
        if view == view_count:
            view += 1
        
    if(pressed(LEFT)):
        view -= 1
        alt_view = 0
        if view == 0:
            view += 1
                
    if(pressed(UP)):
        view += 1
        alt_view = 0
        if view == view_count:
            view += 1
        
    if(pressed(DOWN)):
        view -= 1
        alt_view = 0
        if view == 0:
            view += 1
        
    if(pressed(A)):
        alt_view += 1
        if view == 0:
            view += 1
        
    if(pressed(B)):
        alt_view = 0
        if view == 0:
            view += 1
        

    view %= view_count

# This generates the banner at the top of each flashcard
def title(t):
    pen(15, 15, 15)
    frect(0, 0, 120, 11)
    pen(0, 0, 0)

    text(f"{t} ({view}/{view_count - 1})", 2, 2)
    

# view0 is the splash screen for the program. It appears once.
def view0(tick):
    
    pen(15, 15, 15)
    frect(5, 20, 120, 11)
    pen(0, 0, 0)
    text("Pico System", 10, 21)
    
    message = "Flashcard Tool"
        
    pen(15, 0, 0)
    text(message, 10, 40)


def view1(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message1
    
    if alt_view >= 1:
        message = alt_message1
    
    pen(8, 8, 8)
    text(message, 2, 32)
    
    
def view2(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message2
    
    if alt_view >= 1:
        message = alt_message2
    
    pen(8, 8, 8)
    text(message, 2, 32)
    
    
def view3(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message3
    
    if alt_view >= 1:
        message = alt_message3
    
    pen(8, 8, 8)
    text(message, 2, 32)
    

def view4(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message4
    
    if alt_view >= 1:
        message = alt_message4
    
    pen(8, 8, 8)
    text(message, 2, 32)


def view5(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message5
    
    if alt_view >= 1:
        message = alt_message5
    
    pen(8, 8, 8)
    text(message, 2, 32)
    
    
def view6(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message6
    
    if alt_view >= 1:
        message = alt_message6
    
    pen(8, 8, 8)
    text(message, 2, 32)
    

def view7(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message7
    
    if alt_view >= 1:
        message = alt_message7
    
    pen(8, 8, 8)
    text(message, 2, 32)
    

def view8(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message8
    
    if alt_view >= 1:
        message = alt_message8
    
    pen(8, 8, 8)
    text(message, 2, 32)
    

def view9(tick):
    title(flashcard_topic)

    pen(15, 15, 15)
    if alt_view <= 0:
        message = message9
    
    if alt_view >= 1:
        message = alt_message9
    
    pen(8, 8, 8)
    text(message, 2, 32)
    

def draw(tick):
    pen(0, 0, 0)
    clear()
    [view0, view1, view2, view3, view4, view5, view6, view7,
     view8, view9][view](tick)


start()
