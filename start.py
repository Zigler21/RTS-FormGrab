import pyautogui
import time

# clears up writing space for later.
hotkey = pyautogui.hotkey

click = pyautogui.click

write = pyautogui.typewrite


locate = pyautogui.locateOnScreen

wait = time.sleep

waitdefault = time.sleep

presskey = pyautogui.press

def enter():
    hotkey('enter')

def open_ticket_daily():
    wait(5)
    hotkey('alt', 'r')
    wait(.5)
    write('t')
    wait(.5)
    enter()
    wait(.5)
    write('d')
    wait(1.5)

def open_shift_report():
    hotkey('alt', 'r')
    wait(.2)
    enter()
    wait(1.5)
    click_on_image('images/total.png')
    wait(2)
    click_on_image('images/viewdep.png')

def open_conc_vs_inv():
    hotkey('alt', 'r')
    wait(.3)
    write('i')
    wait(.2)
    for i in range(2):
        write('c')
        time.sleep(0.2)
    enter()
    wait(1.5)

def printdoc():
    user_input = input("Do you want to print the documents? (yes/no): ")
    if user_input.lower() == "yes":
        click_on_image('images/printbutton.PNG')
    else:
        print("printing skipped!")
#Reports back on any clicked images and their pos.
def click_on_image(image_path):
    max_attempts = 50
    attempts = 0
    while attempts < max_attempts:
        try:
            image_location = pyautogui.locateCenterOnScreen(image_path, confidence=.9)
            if image_location is None:
                print(f"Could not find image: {image_path}")
                time.sleep(0.5)
                attempts += 1
                continue
            pyautogui.click(image_location)
            print(f"Found and clicked on image at {image_location}")
            break
        except Exception as e:
            print(f"Could not find image directory: {e}")
            time.sleep(0.5)
            attempts += 1
    if attempts == max_attempts:
        print(f"Max attempts reached. Could not find image: {image_path}")
        input('press enter to continue')
        wait(2)
        quit()



confirm = input('Make sure there is nothing on RTS, just login and press enter to continue')
print('The script will start in 5 seconds, swtich over to RTS')
#Gets the ticket report box, prints it and saves it as a PDF.
if confirm == '':
    open_ticket_daily()
    click_on_image('images/view-ticket.png')
    #This opens the view ticket document
    presskey('right')
    wait(.5)
    enter()
    click_on_image('images/printbutton.PNG')
    wait(1)
    enter()
    wait(.5)
    click_on_image('images/savebutton.PNG')
    wait(.5)
    printdoc()
    wait(1)
    enter()
    wait(.3)
    enter()
    wait(3)
    #after this we close the document and the pop up window for it
    click_on_image('images/closedoc.PNG')
    wait(1)
    click_on_image('images/closeblue.PNG')
    wait(.5)
    #here we get the deposit report
    open_shift_report()
    click_on_image('images/printbutton.PNG')
    wait(1)
    enter()
    wait(.5)
    click_on_image('images/savebutton.PNG')
    wait(1)
    printdoc()
    wait(1)
    enter()
    wait(.3)
    enter()
    wait(3)
     #closes document and popup
    click_on_image('images/closedoc.PNG')
    wait(1)
    click_on_image('images/depclose.png')
    wait(3)
    #open inv report
    open_conc_vs_inv()
    enter()
    click_on_image('images/savebutton.PNG')
    wait(.5)
    printdoc()
    wait(3)
    enter()
    wait(.2)
    enter()
    input('Press Enter to continue')
