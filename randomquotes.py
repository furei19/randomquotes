import random
from imps import *

rqg = False
menu = True

while menu:
    choice = input("\n Press Y for another quote, N for exit ")
    if choice == 'y':
        rqg = True
        menu = False
    
    elif choice == 'n':
        exit()

    while rqg:
        clearScreen()
        rand = random.randint(1, 51)
        if str(rand) == '1':
            print("There is nothing like looking, if you want to find something. ",
                "You certainly usually find something, if you look, ",
                "but it is not always quite the something you were after.")
        elif str(rand) == '2':
            print("So comes snow after fire, and even dragons have their endings.")
        elif str(rand) == '3':
            print("The greatest glory in living lies not in never falling, but in rising every time we fall.")
        elif str(rand) == '4':
            print("The way to get started is to quit talking and begin doing.")
        elif str(rand) == '5':
            print("May the wind under your wings bear you where the sun sails and the moon walks.")
        elif str(rand) == '6':
            print("Decide to be fine until the end of the week. Make yourself smile, ",
                "because you're alive and that's your job. Then do it again the next week. ",
                "I call it being professional. Do it right, with a smile, or don't do it.")
        elif str(rand) == '7':
            print("If life were predictable it would cease to be life, and be without flavor.")
        elif str(rand) == '8':
            print("If you look at what you have in life, you'll always have more. ",
                "If you look at what you don't have in life, you'll never have enough.")
        elif str(rand) == '9':
            print("If you set your goals ridiculously high and it's a failure, ",
                "you will fail above everyone else's success.")
        elif str(rand) == '10':
            print("Life is what happens when you're busy making other plans.")
        elif str(rand) == '11':
            print("Spread love everywhere you go. Let no one ever come to you without leaving happier.")
        elif str(rand) == '12':
            print("When you reach the end of your rope, tie a knot in it and hang on.")
        elif str(rand) == '13':
            print("Don't judge each day by the harvest you reap but by the seeds that you plant.")
        elif str(rand) == '14':
            print("In the middle of every difficulty lies opportunity.")
        elif str(rand) == '15':
            print("Never allow a person to tell you no who doesn't have the power to say yes.")
        elif str(rand) == '16':
            print("Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.")
        elif str(rand) == '17':
            print("Because when I look at you, I can feel it. And I look at you and I'm home.")
        elif str(rand) == '18':
            print("What defines us is how well we rise after falling.")
        elif str(rand) == '19':
            print("If you believe in yourself, with a tiny pinch of magic, all your dreams can come true!")
        elif str(rand) == '20':
            print("The fool doth think he is wise, but the wise man knows himself to be a fool.")
        elif str(rand) == '21':
            print("Weaseling out of things is important to learn; it's what separates us from the animals… except the weasel.")
        elif str(rand) == '22':
            print("Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do.")
        elif str(rand) == '23':
            print("Do, or do not. There is no try.")
        elif str(rand) == '24':
            print("here is some good in this world, and it's worth fighting for.")
        elif str(rand) == '25':
            print("The best way to appreciate your job is to imagine yourself without one.")
        elif str(rand) == '26':
            print("Everyone has inside them a piece of good news. The good news is you don't know how great you can be!... And what your potential is.")
        elif str(rand) == '27':
            print("The only way to do great work is to love what you do. If you haven't found it yet, ",
                "keep looking. Don't settle. As with all matters of the heart, you'll know when you find it.")
        elif str(rand) == '28':
            print("When I had nothing to lose, I had everything. When I stopped being who I am, I found myself.")
        elif str(rand) == '29':
            print("The miracle is not that we do this work, but that we are happy to do it.")
        elif str(rand) == '30':
            print("The big secret in life is that there is no secret. Whatever your goal, you can get there if you're willing to work.")
        elif str(rand) == '31':
            print("Whatever you are, be a good one.")
        elif str(rand) == '32':
            print("Live each day like it's your second to the last. That way you can fall asleep at night.")
        elif str(rand) == '33':
            print("Even a stopped clock is right twice every day. After some years, it can boast of a long series of successes.")
        elif str(rand) == '34':
            print("If you let your head get too big, it'll break your neck.")
        elif str(rand) == '35':
            print("All our dreams can come true if we have the courage to pursue them.")
        elif str(rand) == '36':
            print("Waiting is painful. Forgetting is painful. But not knowing which to do is the worst kind of suffering.")
        elif str(rand) == '37':
            print("The secret of getting ahead is getting started.")
        elif str(rand) == '38':
            print("Impossible is just an opinion.")
        elif str(rand) == '39':
            print("You can't be great if you don't feel great. Make exceptional health your number one priority.")
        elif str(rand) == '40':
            print("Love is an untamed force. When we try to control it, it destroys us. ",
                "When we try to imprison it, it enslaves us. When we try to understand it, it leaves us feeling lost and confused.")
        elif str(rand) == '41':
            print("If you hear a voice within you say 'you cannot paint,' then by all means paint and that voice will be silenced.")
        elif str(rand) == '42':
            print("When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one which has been opened for us.")
        elif str(rand) == '43':
            print("And, when you want something, all the universe conspires in helping you to achieve it.")
        elif str(rand) == '44':
            print("We grow fearless when we do the things we fear.")
        elif str(rand) == '45':
            print("Do not go where the path may lead, go instead where there is no path and leave a trail.")
        elif str(rand) == '46':
            print("Whoever is happy will make others happy too.")
        elif str(rand) == '47':
            print("It is during our darkest moments that we must focus to see the light.")
        elif str(rand) == '48':
            print("The best and most beautiful things in the world cannot be seen or even touched")
        elif str(rand) == '49':
            print("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
        elif str(rand) == '50':
            print("The future belongs to those who believe in the beauty of their dreams.")
        elif str(rand) == '51':
            print("No matter how your heart is grieving, if you keep on believing, the dream that you wish will come true.")
        
        rqg = False
        menu = True
            
