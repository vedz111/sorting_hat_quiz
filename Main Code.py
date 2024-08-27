from tkinter import *
from tkinter import messagebox
from functools import partial

#MODULE 1: Hogwarts House Quiz

def quiz1():
    import tkinter as tk
    from tkinter import messagebox
    import matplotlib.pyplot as plt
    import numpy as np
    import random

    class SortingHatQuiz:
        def __init__(self, root):
            self.root = root
            self.root.title("Sorting Hat Quiz")

            self.questions = [
                "1. Which character do you think you're most like?",
                "2. What type of a friend do you consider yourself?",
                "3. Tensions are high at Hogwarts this year, every student is picking a fight... Which wizard do you think you want to fight?",
                "4. A stranger is just a friend who doesn't know you properly yet... Which one of these qualities in a person scares you the most?",
                "5. What's your favorite color?",
                "6. O.W.L.S are just round the corner, which subject do you think you'll be the best at?",
                "7. You're locked in a duel with a skilled opponent. They fire an unknown spell at you, and you shout…",
                "8. Which of these Dumbledore quotations speaks to you?",
                "9. Which of your skills are you most proud of?",
                "10. It's Saturday, you've finished your homework, and you have some free time. Where do you go?",
                "11. It's finally time for the annual Hogwarts trip to Hogsmeade.... what are you doing as soon as you reach?"
            ]

            self.answers = {
                "Gryffindor": ["Neville Longbottom", "The Brave One", "Bellatrix Lestrange", "Breaking Trust",
                               "Orange", "Potions", "Expelliarmus!",
                               "Words are, in my not-so-humble opinion, our most inexhaustible source of magic.",
                               "My ability to keep secrets.", "The Room of Requirement", "Go have butterbeer"],
                "Hufflepuff": ["Newt Scamander", "The Loyal One", "Remus Lupin", "Complete Isolation",
                                "Golden", "Herbology", "Stupefy!",
                                "It matters not what someone is born, but what they grow to be.",
                                "My ability to make new friends.", "The Kitchens", "Window shop"],
                "Ravenclaw": ["Luna Lovegood", "The Creative One", "Barty Crouch Jr.", "Superiority Complex",
                               "Turquoise", "Astronomy", "Crucio!",
                               "It does not do to dwell on dreams and forget to live.",
                               "My ability to absorb new information.", "The Library", "Play outdoor games"],
                "Slytherin": ["Draco Malfoy", "The Logical One", "Dumbledore", "Double-faced",
                                "Beige", "Defence Against the Dark Arts", "Avada Kedavra!",
                                "Pity the living, and above all, those who live without love.",
                                "My ability to get what I want.", "The Forbidden Forest", "Mess with other students"]
            }

            self.current_question = 0
            self.house_points = {"Gryffindor": 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin": 0}
            self.label = tk.Label(root, text=self.questions[self.current_question])
            self.label.pack(pady=10)
            self.buttons = []

            for house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                button = tk.Button(root, text=self.answers[house][self.current_question], command=lambda h=house: self.answer_question(h))
                button.pack(side=tk.LEFT, padx=20)
                self.buttons.append(button)

        def answer_question(self, house):
            self.house_points[house] += 1

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.label.config(text=self.questions[self.current_question])
                for button, house in zip(self.buttons, ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]):
                    button.config(text=self.answers[house][self.current_question])
            else:
                root.destroy()
                max_house = self.display_result()
                self.piechart(max_house)
                

        def display_result(self):
            max_house = max(self.house_points, key=self.house_points.get)
            messagebox.showinfo("Result", f"You belong to {max_house}!")
            return max_house

#MODULE 2: using a pie chart to show the user the percentage of each house that they belong to

        def piechart(self, max_house):
            y = np.array([self.house_points["Gryffindor"], self.house_points["Slytherin"], self.house_points["Hufflepuff"], self.house_points["Ravenclaw"]])
            totalqs = 11
            mylabels = ["Gryffindor " + str(int(self.house_points["Gryffindor"] * 100 / totalqs)) + '%',"Slytherin " + str(int(self.house_points["Slytherin"] * 100 / totalqs)) + '%',"Hufflepuff " + str(int(self.house_points["Hufflepuff"] * 100 / totalqs)) + '%',"Ravenclaw " + str(int(self.house_points["Ravenclaw"] * 100 / totalqs)) + '%']
            mycolors = ["Maroon", "DarkGreen", "Gold", "MidnightBlue"]
            myexplode = [0, 0, 0, 0]
            index = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"].index(max_house)
            myexplode[index] = 0.1
            plt.pie(y, labels=mylabels, colors=mycolors, explode=myexplode, startangle=90)
            plt.show()
            
    if __name__ == "__main__":
            root = tk.Tk()
            app = SortingHatQuiz(root)
            root.geometry("850x700")
            root.mainloop()

#MODULE 3: Patronus Quiz

def quiz2():
    import tkinter as tk
    from tkinter import messagebox

    class PatronusQuiz:
        def __init__(self, root):
            self.root = root
            self.root.title("Patronus Quiz")

            self.questions = [
                "1. 'Oh to own everything in fantasy books'... What is one magical object you would love to own?",
                "2. I'm sooooo thirsty....I just want to drink some:",
                "3. 'If superman can fly, is superman a wizard...?' If you were to have a superpower, which one would you want to have?",
                "4. There is sky blue, turqouise blue, navy blue, ugh so many blues....' What color is your favourite?",
                "5. 'Oh my god you are such a teacher's pet...' Given the choice, who's good list would you want to be on?"
            ]

            self.answers = {
                "Dragon": ["time turner", "butterbeer", "teleportation", "pastels (lighter color shades)", "Albus Dumbledore"],
                "Stag": ["invisibility cloak", "tea", "super strength", "basics (white & black)", "Severus Snape"],
                "Phoenix": ["the elder wand", "hot chocolate", "healing powers", "cool colors", "Minerva McGonagal"],
                "Lion": ["every magical potion", "lemonade", "shapeshifting", "warm colors", "Rubeus Hagrid"]
            }

            self.current_question = 0
            self.patronus_points = {"Dragon": 0, "Stag": 0, "Phoenix": 0, "Lion": 0}

            self.label = tk.Label(root, text=self.questions[self.current_question])
            self.label.pack(pady=10)

            self.buttons = []
            for patronus in ["Dragon", "Stag", "Phoenix", "Lion"]:
                button = tk.Button(root, text=self.answers[patronus][self.current_question], command=lambda p=patronus: self.answer_question(p))
                button.pack(side=tk.LEFT, padx=10)
                self.buttons.append(button)

        def answer_question(self, patronus):
            self.patronus_points[patronus] += 1

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.label.config(text=self.questions[self.current_question])
                for button, patronus in zip(self.buttons, ["Dragon", "Stag", "Phoenix", "Lion"]):
                    button.config(text=self.answers[patronus][self.current_question])
            else:
                root.destroy()
                self.display_result()

        def display_result(self):
            max_patronus = max(self.patronus_points, key=self.patronus_points.get)
            
            messagebox.showinfo("Result", f"Your patronus is a {max_patronus.lower()}!")

    if __name__ == "__main__":
        root = tk.Tk()
        app = PatronusQuiz(root)
        root.geometry("850x700")
        root.mainloop()

#MODULE 4: Wand Quiz

def quiz3():
    import tkinter as tk
    from tkinter import messagebox

    class WandQuiz:
        def __init__(self, root):
            self.root = root
            self.root.title("Wand Quiz")

            self.questions = [
            "1. What's your favourite way to pass time?",
            "2. 'You don't choose a wand, the wand chooses you'.... Why do you think you need a good wand?",
            "3. Everbody loves nature, right? even if you don't you must have a favourite season?",
            "4. If an intruder broke into your house, what would you do?",
            "5. Which word would you use to describe your emotions?"
            ]

            self.answers = {
                "Hawthorn": ["Sleep","To watch the world crumble under my command","Monsoon", "probably slap them out of fear", "confusing"],
                "Vine": ["Read a good book","To protect myself against the darkness of the world of course","Summer", " hide in a corner, figure out the perfect time and then attack them with my carefully planned intruder system", "very carefully laid out"],
                "Ash": ["Watch/play sports","Aren't witches & wizards nothing without a wand?","Autumn", "instantly scream for help, i'm not taking any chances", "easily manipulated"],
                "Acacia": ["Bake (you can never have enough desserts)","They seem to be of great value","Winter", "divert their attention and then kick them out (im locking all the doors)", "strong"]
            }

            self.current_question = 0
            self.wand_points = {"Hawthorn": 0, "Vine": 0, "Ash": 0, "Acacia": 0}

            self.label = tk.Label(root, text=self.questions[self.current_question])
            self.label.pack(pady=10)

            self.buttons = []
            for wand in ["Hawthorn", "Vine", "Ash", "Acacia"]:
                button = tk.Button(root, text=self.answers[wand][self.current_question], command=lambda w=wand: self.answer_question(w))
                button.pack(side=tk.LEFT, padx=10)
                self.buttons.append(button)

        def answer_question(self, wand):
            self.wand_points[wand] += 1

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.label.config(text=self.questions[self.current_question])
                for button, wand in zip(self.buttons, ["Hawthorn", "Vine", "Ash", "Acacia"]):
                    button.config(text=self.answers[wand][self.current_question])
            else:
                root.destroy()
                self.display_result()

        def display_result(self):
            max_wand = max(self.wand_points, key=self.wand_points.get)
            if max_wand=="Hawthorn":
                max_wand="hawthorn wood with unicorn hair core"
            elif max_wand=="Vine":
                max_wand="vine wood with phoenix feather core"
            elif max_wand=="Ash":
                max_wand="ash with unicorn hair core"
            elif max_wand=="Acacia":
                max_wand="acacia with dragon heartstring core"
            messagebox.showinfo("Result", f"You get a wand of {max_wand}!")
            
        
    if __name__ == "__main__":
        root = tk.Tk()
        app = WandQuiz(root)
        root.geometry("850x700")
        root.mainloop()


#MODULE 5: Random Pet
        
def quiz4():
    import tkinter as tk
    import random

    
    pets = ['cat', 'owl', 'toad', 'mouse']

    
    def assign_pet():
        selected_pet = random.choice(pets)
        result_label.config(text=f"Congratulations on taking the quiz!\nHere is your Hogwarts pet: {selected_pet.capitalize()}")

    root = tk.Tk()
    root.title("PET")
    root.geometry("300x200")
    
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=20)

    
    assign_button = tk.Button(root, text="Assigning Pet", command=assign_pet)
    assign_button.pack()

    
    root.mainloop()


#MODULE 6: linking the above quizzes in a sub-menu to display all the options to the user
    
import tkinter as tk
def sub_quiz():
    root = tk.Tk()
    root.title("Sub Quiz section")

    
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    
    file_menu = tk.Menu(menu_bar, tearoff=0)

    
    file_menu.add_command(label="Click Me", command=show_message)

    

    label = tk.Label(root, text="WHICH QUIZ WOULD YOU LIKE TO ATTEMPT?")
    label.pack(pady=10)

    
    button1 = tk.Button(root, text="Sorting Hat", command=lambda: quiz1())
    button2 = tk.Button(root, text="Find my Patronus", command=lambda: quiz2())
    button3 = tk.Button(root, text="What's my wand", command=lambda: quiz3())
    button4 = tk.Button(root, text="Who's my animal companion", command=lambda: quiz4())

    
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)
    button4.pack(pady=5)

    
    root.mainloop()


#MODULE 7: creating a GUI and displaying book reviews

import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "Button clicked!")

def show_question(quiz_number):
    
    messagebox.showinfo("Quiz Question", f"Displaying question for Quiz {quiz_number + 1}")


def book_review():
    import tkinter as tk
    def button_click(button_number):
        messages = {
            1: """
    ‘Harry Potter and the Philosopher’s Stone’ is a very engaging read for children and adults alike. Since it is the first book in this series, we are introduced to an entirely new world in this book. The world of magic slowly builds itself as we read through the book. The genius of this book is using the protagonist Harry’s discovery of this world to parallel the readers’.

    ‘Harry Potter and the Philosopher’s Stone’ is definitely worth reading for an adult. While it was written as a children’s book, it has outlived this label, and there are people of all ages who not only read these books but also engage in community discussions and have fun playing games inspired by these books. Many people have found reading this book a very rewarding experience, as is evident from the sales and fame this book has garnered across all demographics.

    The first book in the series was, in my opinion, really good. Colourful characters, an enjoyable tone with sufficient darkness, and an interesting world-within-a-world all made The Philosopher’s Stone a really good children’s book for both kids and adults."""
    ,

        2: """
    A sleeping evil awakens under the castle of Hogwarts. Harry Potter and the Chamber of Secrets is the asecond installment to the Harry Potter series. A sequel that gives what we were looking for an solidifies a desire to read the entire series. Let’s dive in and see what this chapter of the series is all about. I will do my best not to spoil anything major for this book.

    While not as magical as the first book, this one’s still a great read for kids aged 8 and up. Violence includes deadly spiders, peril from basilisk, and a gross ghost party (including a ghost taking out his own head).But all in all an amazing read."""
    ,

        3: """
    I am both pleasantly surprised and mad that I ended up enjoying this book and getting invested in Sirius Black. The story really improved when we discovered more about the background story of events that happened before Harry's generation. I enjoyed learning more about the adult characters and being surprised at the plot developments.

    “Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.”
    As it seems my Harry Potter reviews don’t always start with a Dumbledore quote but always end up being “My thoughts about this book” reviews as well.

    August 2023. Rereading series to commemorate the twenty five years that Harry has been part of our collective history. Nothing like an all time favorite book to comfort me in the wake of an end of summer cold."""
    ,

        4: """
    Don't mind me, just crying my eyes out.
    This was WAY better than I remember it being, and I remember it being pretty darn good. J.K. Rowling is a writing goddess and I can't believe how much foresight and planning went into this series. She already hints at the horcruxes and many other things in this book that don't show up until much later. Definitely one of my favorites in the series (but I say that about all of them)!

    There is an incredibly somber mood that descends on me every time I finish this book in the series, and reading it with the illustrations did nothing to change that. I felt the drawings were impeccable, and I loved how some of the characters were reimagined to look a different way than portrayed in the movies, my favorite being Mad Eye Moody. Now, the long wait for the remainder of the illustrated editions. :(

    "I is a good elf"
    It's been proven three times now, that I always get ahead of myself when reviewing Harry Potter, incorrectly concluding the last one (out of the ones I've read so far) to be the best, but it cannot be helped. The standards are moved up - again. It's like Rowling just had a look at the first books, found them to be way too short, and came up with this one, which is much longer than the previous ones - combined! And the writing style keeps on improving, while plot getting more and more thrilling, making it oh so delightful to read."""
    ,

        5: """
    This book really made my CRY. And it was not just tears, I was CRYING out loud. If you've read it (or at least have seen the movie) you surely know that a very important character dies and GOD, it was heart wrenching, the tears came flowing like a waterfall. I didn't want him to die :(
    Overall, I really liked this book, but I think it was way too long, it had some chapters that weren't relevant to the story...

    This is my new routine to reread HP books to take
    a trip down my memory lane because reading these remarkable books make me remember the times I was so excited to get my hands on them: the younger, crazier, stupider, less experienced, naiver but always happy version of myself. These books always bring out the noisy, mischievous, fiery, cheery child we hid inside the walls as we grow up.

    This book used to be my least favorite book of the series and after rereading it, I can't understand why... I loved it!
    So many good things I had forgotten started here like the DA meetings. I still absolutely hate Umbridge and I'm out of my reading slump (hopefully!)."""
    ,

        6: """
    I'm not sure why, but this one took me completely by surprise. I was expecting this installment to be mainly filler to get us to the Deathly Hallows, but so much happened here that I must have forgotten from the movie. The Half-Blood prince was considerably darker than the previous 5 books, and I just adore how this series has progressed and grown just like most of its readers have. Obviously I knew what the big reveal was prior to finishing the book due to my viewing the films before, but it didn't take away from the experience the novel had to offer. I have this nervous lump in my throat knowing that the next book is the final one, but am simultaneously excited to finally read what the films surely have left out surrounding the conclusion of the series.

    " Should you feel that a family member, colleague, friend, or neighbor is acting in a strange manner, contact the Magical Law Enforcement Squad at once. They may have been put under the Imperius Curse."

    Time for interesting little subplots is over. We've arrived finally, where everything is closely tied to the core of the story and progressing fast. It's always delightful to see, everything that was great about the series still remains the same, if not better. However, disappointments, sorrow and hardships are what the reader is going to encounter for the most part. As I finished reading Half-Blood Prince, more than ever before, I feel being trapped in a hopeless situation filled with nothing but forebodings."""
    ,

        7: """
    "OI! There's a war going on here!"

    "Merlin's Pants!"

    The six-year build-up is over. The final adventure, towards which we've been sailing for - through six amazing Hogwarts years - is here at last. And yet again, Rowling surpasses her own standards to bring us the most adventurous book of the entire series, to conclude everything is a most dramatic way. Twist after twist after twist is going to keep the reader immersed more than ever. Be warned: once started, you won't have a moment's rest till your finish this one!"""
        }
        message_label.config(text=messages.get(button_number, "Invalid button"))
   
    root = tk.Tk()
    root.title("Button Messages")
    root.geometry("650x450")
   
    

    message_label = tk.Message(root, text="")

    
    frame=tk.Frame(root) 
    frame.pack(side = 'top')
    for i in range(1, 8):
        
        button = tk.Button(frame, text=f"Book {i}", command=lambda i=i: button_click(i))
        button.pack(side='left',padx=20, pady=10)

    
    message_label.pack(pady=30)

    
    root.mainloop()


#MODULE 8: creating a list of all existing users and their houses

def users():
    import tkinter as tk
    top=tk.Tk()
    top.geometry('400x250')
    frame = tk.Frame(top)
    for t in [("kiana-slytherin","saanvi-hufflepuff","adi-ravenclaw","harish-gryffindor","lina-ravenclaw","ana-slytherin")]:
     for x in range(1):
        for y in range(6):
            w = tk.Text(frame, width=20, height=2)
            w.grid(row=y,column=x)
            w.insert(END, t[y])
    frame.pack(side = TOP)
    top.mainloop()


#MODULE 9: creating a mini game for a fun user interaction using pygame
    
def golden_snitch():
    import tkinter as tk
    import pygame
    import random
    import sys

    
    pygame.init()

    
    width=800
    height=600
    fps = 60

    
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch the Golden Snitch')

    
    golden_snitch_img = pygame.image.load('golden_snitch.png')
    golden_snitch_img = pygame.transform.scale(golden_snitch_img, (75, 50))

    
    snitch_x = random.randint(0, width-75)
    snitch_y = random.randint(0, height-50)
    snitch_dx = random.randint(3,7)
    snitch_dy = random.randint(3,7)
    snitch_rect = pygame.Rect(snitch_x, snitch_y, 75, 50)

    
    def display_message(text):
        font = pygame.font.Font(None, 36)
        text = font.render(text, True, (250,250,250))
        text_rect = text.get_rect(center=(width//2, height//2))
        window.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)

        replay = None
        while replay is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        replay = True
                    elif event.key == pygame.K_n:
                        replay = False
        return replay

    
    playing = True
    while playing:
        window.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if snitch_rect.collidepoint(mouse_x, mouse_y):
                    replay = display_message("Congratulations! You caught the Golden Snitch! Play again? (Y/N)")
                    if replay:
                        snitch_x = random.randint(0, width-75)
                        snitch_y = random.randint(0,  height-50)
                        snitch_rect.topleft = (snitch_x, snitch_y)
                    else:
                        playing = False

        
        snitch_rect.x += snitch_dx
        snitch_rect.y += snitch_dy

        if snitch_rect.left < 0 or snitch_rect.right > width:
            snitch_dx = -snitch_dx
        if snitch_rect.top < 0 or snitch_rect.bottom > height:
            snitch_dy = -snitch_dy

        
        window.blit(golden_snitch_img, snitch_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(fps)

    window.fill((0,0,0))
    display_message("Thank you for playing!")


#MODULE 10: displaying the menu for the user to choose from
    
def menu():
    import tkinter as tk

    def show_message():
        messagebox.showinfo("Info", "You clicked the menu item!")

    root = tk.Tk()
    root.title("Home Screen")


    new_button = tk.Button(root, text="QUIZZES", command=lambda: sub_quiz())
    open_button = tk.Button(root, text="BOOK REVIEWS", command=lambda: book_review())
    side_button = tk.Button(root, text="CATCH THE GOLDEN SNITCH (GAME)", command=lambda: golden_snitch())
    left_button = tk.Button(root, text="LIST OF USERS", command= lambda: users())

    new_button.grid(row=0, column=0, padx=5, pady=5)
    open_button.grid(row=0, column=1, padx=5, pady=5)
    side_button.grid(row=0, column=2, padx=5, pady=5)
    left_button.grid(row=0, column=3, padx=5, pady=5)

    root.mainloop()

#MODULE 11: creating a login page

def validateLogin(username, password):
    
    inputpassword = str(password.get())
    
    code = ["alohomora","leviosa", "stupefy", "expelliarmus", "accio", "polyjuice"]
    if inputpassword in code:
        tkWindow.destroy()
        menu()
    else:
        messagebox.showerror("showerror", "Invalid Password") 

tkWindow = Tk()
tkWindow.geometry('250x300')
tkWindow.title('Tkinter Login Form - pythonexamples.org')
img= PhotoImage(file= 'hogwarts.png')
Label(tkWindow, image= img, bg= 'grey').place(x=0,y=0)



usernameLabel = Label(tkWindow, text="User Name").grid(row=5, column=5)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=5, column=6)

passwordLabel = Label(tkWindow,text="Password").grid(row=6, column=5)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=6, column=6)

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=9, column=5)

tkWindow.mainloop()


#MODULE 12: linking all the seperate codes together to create the final project
