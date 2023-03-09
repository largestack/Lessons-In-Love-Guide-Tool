# A Life of Prizes
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=returntosummer2&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: returntosummer2
* Group: Main
* Triggered by label: returntosummer1
* Triggered by branch label: returntosummer2

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label returntosummer2:
    scene resetfour6
    play music "11c.mp3"
    $ renpy.pause(10, hard=True)
    play sound "jackpot.mp3"
    scene resetfour7

    s "こんにちは！先生です！"
    s "今日はゲームをします。"
    s "ARE YOU READY???"
    s "で わ。。。"
    s "START!!!"

    play sound "static.mp3"
    scene resetfour6 with flash
    stop sound

    "THE RULES OF THE GAME ARE SIMPLE"
    "FILL OUT MAGAZINE SWEEPSTAKES AND TRY TO WIN DIFFERENT PARTS OF A KEY"
    "ONCE YOU HAVE WON ALL THE PARTS OF THE KEY, YOU WILL BE ABLE TO ASSEMBLE IT AND ESCAPE YOUR ROOM"
    "BUT BE CAREFUL!!!"
    "STAYING IN ONE PLACE FOR TOO LONG COULD CAUSE YOU TO GO INSANE!!!"
    "HAVE FUN AND ENJOY!!!"
    "WELCOME HOME"

    s "What do I want to do?"

    menu resetfourmenu:
        "ESCAPE (For Real)" if keypoint == 10:
            $ renpy.end_replay()
            $ returntosummer2 = True

            jump returntosummer3
        "ESCAPE!!!":
            jump resetfourescape
        "Use the cool rectangle machine":
            jump resetfourrectangle
        "Thing on the wall":
            jump resetfourthing
        "Watch the other rectangle":
            jump resetfourtv
        "Host a dance party":
            jump resetfourdanceparty
        "Pet your friend":
            jump resetfourmaggot
        "Use communication device":
            jump resetfourphone
        "Masturbate ;D" if bonus == True:
            jump resetfourmasturbate
        "Eat Something":
            jump resetfoureat

label resetfourescape:
    scene resetfour1
    with fade

    "I skip over to a bunch of magazines somebody placed all over my desk."
    "I feel compelled to scribble things inside of them."
    "What will I scribble today?"

    menu resetfourescapemenu:
        "Book 1: Architects Weekly" if r4key1 == False:
            scene resetfour10 with fade

            "I skim through a magazine about architects and architect related stuff and find that the issue is focusing on large buildings in particular."
            "It goes over the mechanics and construction of them and even features images of gigantic skyscrapers with holes in the middle of them to help prevent the buildings from swaying in the wind."
            "I am once again fascinated by the innovations in modern construction and- oh? What is this?!"
            "It looks like the magazine is holding a sweepstakes where readers can submit their answers for a chance to win a piece of a small key to my bedroom!"
            "I can't imagine many people will enter this sweepstakes, so I'm pretty much guaranteed to win so long as I can answer the question."
            "I fill out the form with all of my information and direct my attention to the question printed in the bottom right corner..."

            $ r4book1 = renpy.input("HOW MANY STAIRS TO REACH THE TOP???")
            $ r4book1 = r4book1.strip()

            if r4book1 == "85":
                play sound "jackpot.mp3"

                $ r4key1 = True
                $ keypoint += 1

                "Someone slides a piece of a key underneath my bedroom door! I must have gotten the answer correct!"
                "I didn't even have to mail the form!"
                "I am so very smart!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                "I write down my answer in the space provided and do a little dance for good luck."
                "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                "I sure hope I win!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu

        "Book 2: High Fashion Forecast" if r4key2 == False:
            scene resetfour10 with fade

            "I pick up a fashion magazine to check out all of the latest trends and come across an article about different types of fabric and how to prepare for summer."
            "The article doesn't really apply to me since I'm not going to wear {i}anything{/i} this summer, but I decide to keep reading because of all of the pictures of pretty girls."
            "It seems that a thing that wasn't in style is going to be in style again. Or at least that's what I think is being said."
            "Despite hanging around [teenager]s all the time, I'm still not entirely confident when it comes to some of the things they say."
            "If only Chika was here to help me. She knows all sorts of stuff about clothes."

            if bonus == True:
                "She is also very good at sex."
                "If only this was a sex magazine..."

            s "Oh. What's this?"

            "It looks like the magazine is holding a sweepstakes where readers can submit their information for a chance to win a piece of a small key to my bedroom!"
            "I have to win this! I need that key!"
            "I fill out the form with all of my information and direct my attention to the question printed in the bottom right corner..."

            $ r4book2 = renpy.input("WHAT IS YOUR FAVORITE FABRIC???")
            $ r4book2 = r4book2.strip()

            if r4book2.lower() in ["denim"]:
                play sound "jackpot.mp3"

                $ r4key2 = True
                $ keypoint += 1

                "Someone slides a piece of a key underneath my bedroom door! The magazine must have liked my entry!"
                "I didn't even have to mail the form!"
                "I am so great!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                "I write down my answer in the space provided and do a little dance for good luck."
                "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                "I sure hope I win!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu

        "Book 3: God & You ~ Best Friends Forever" if r4key3 == False:
            scene resetfour10 with fade

            "I open up a book about Jesus Christ and all of his buddies and prepare myself to hear about their crazy antics out on the road."
            "The book tells a brief story about a ragtag band of bearded dudes riding around on camels and kissing each other all the time."
            "I am very glad to hear that they were so open about their sexuality and understand now why roughly half of the girls in my class are bisexual."

            if bonus == True:
                "If Jesus can fuck people of the same sex, everyone should be allowed to without being persecuted."
            else:
                "If Jesus can hug people of the same sex, everyone should be allowed to without being persecuted."

            "Eventually, Jesus and his friends take a break from their traveling miracle circus for a day or two to play a rousing pickup game of baseball against a group of gentiles."
            "In stark contradiction to the words he preaches, Jesus goes unto them and says the following:"
            "{i}Prepare to get fucked, gentiles.{/i}"
            "Jesus is a lot cooler than I remember, especially because he is wearing sunglasses in all of the illustrations in this book."
            "The rest of the story is basically about Jesus and the apostles creaming a bunch of unprepared children in an athletic contest and I turn to the final page feeling motivated and gleeful."
            "After a brief epilogue where everyone goes to space, there is a blank form provided."
            "It looks like the magazine is holding a sweepstakes where readers can submit their information for a chance to win a piece of a small key to my bedroom!"
            "I have to win this! I need that key!"
            "I fill out the form with all of my information and direct my attention to the question printed in the bottom right corner..."

            $ r4book3 = renpy.input("WHICH APOSTLE WOULD BE YOUR CHOICE FOR MVP???")
            $ r4book3 = r4book3.strip()

            if r4book3.lower() in ["judas"]:
                play sound "jackpot.mp3"

                $ r4key3 = True
                $ keypoint += 1

                "Someone slides a piece of a key underneath my bedroom door! The magazine must have liked my entry!"
                "I didn't even have to mail the form!"
                "I am so great!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                "I write down my answer in the space provided and do a little dance for good luck."
                "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                "I sure hope I win!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu

        "Book 4: Breathing Exercises" if r4key4 == False:
            scene resetfour10 with fade
            "I open up a medical magazine advertising different types of breathing exercises on the cover."
            "Since I'm going to be trapped in this room for probably the rest of forever, I figure it will be nice to learn some to help calm me down when I need it."
            "Unfortunately, it looks like most of the pages are written in a different language."
            "There is one section I can find in Japanese, but it must not be very {i}good{/i} Japanese since I'm not really sure what it's asking."
            "The article reads like this:"
            "{i}To breathe! What is why you would do that? And how?{/i}"
            "{i}The answer is simple. It is because you can. And because you will.{/i}"
            "{i}Follow this simple breath pattern and all will become easy. All will become good.{/i}"
            "{i}Your troubles, no more! Your breath, yes! How to do!{/i}"
            "{i}God is real! God is good! He breathe!{/i}"
            "The middle of the page seems to be cut out, but I can make out what looks like a form on the next page."
            "It looks like the magazine is holding a sweepstakes where readers can submit their answers for a chance to win a piece of a small key to my bedroom!"
            "I can't imagine many people will enter this sweepstakes, so I'm pretty much guaranteed to win so long as I can answer the question."
            "I fill out the form with all of my information and direct my attention to the question printed in the bottom right corner..."

            $ r4book4 = renpy.input("BREATHING THE RIGHT WAY??? HOW TO DO??? HOW MANY??? ONLY TWO!!!")
            $ r4book4 = r4book4.strip()

            if r4book4 == "18":
                play sound "jackpot.mp3"

                $ r4key4 = True
                $ keypoint += 1

                "Someone slides a piece of a key underneath my bedroom door! I must have gotten the answer correct!"
                "I didn't even have to mail the form!"
                "I am so very smart!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                "I write down my answer in the space provided and do a little dance for good luck."
                "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                "I sure hope I win!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu

        "Book 5: Chef's Guide to Chef Stuff" if r4key5 == False:
            scene resetfour10 with fade
            "I open up a magazine with a big cake on the front of it and hope that there is a cake inside."
            "There is not."
            "I do manage to find an interesting article about chili, though!"
            "According to this magazine, chili is one of the most interesting and diverse types of foods you can make."
            "There are all different kinds of chili, and everyone has their own secret ingredient they use to make it better."
            "Oh! And it looks like the magazine is holding a contest to see who can create the best chili recipe. The winner gets a piece of key to my bedroom!"
            "As someone with no experience cooking but who needs that key to survive, I think I can do this!"
            "I fill out the submission form with all of my information and begin to create my chili recipe."
            "I think I have all of the basic ingredients down."
            "Now I just have to come up with a secret one..."

            $ needchili = True

            menu:
                "One Whole Coconut":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Chocolate":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Egg":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Human Hair":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Premium Beer":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Popular Mexican Snack, Takis":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Soap":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Magic Beans":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Honeydew Melon":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Sidewalk Chalk":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "White Rice":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Severed Finger":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "More Chili!":
                    "I write down my answer in the space provided and do a little dance for good luck."
                    "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                    "I sure hope I win!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
                "Coffee" if chilihint == True:
                    play sound "jackpot.mp3"

                    $ r4key5 = True
                    $ keypoint += 1

                    "Someone slides a piece of a key underneath my bedroom door! I must have gotten the answer correct!"
                    "I didn't even have to mail the form!"
                    "I am so very smart!"
                    "I put my pencil down and look at my desk."
                    "What do I want to do now?"

                    jump resetfourescapemenu
        "Book 6: Nature Walking" if r4key6 == False:
            scene resetfour10 with fade
            "I open up a magazine all about trees and the outside world."
            "It looks like this particular volume focuses on the different types of wildlife you may encounter out in nature and how to deal with them."
            "I do not know much about animals, but I do know that I like reading and I like trees!"
            "I would probably like reading a little more if I did not have to spend every waking moment filling out magazine sweepstakes, but it is what it is."
            "The magazine teaches me that there are two different ways to defeat a bear in the wild, and both of them involve not actually defeating the bear."
            "Option one is to die."
            "Option two is to make yourself look big and scary, but I don't think there are many bears who would be intimidated by something like that."
            "What I learn is that if you see a bear, you basically die."
            "I read about a few more animals, but most of them sound nice and peaceful."
            "I wish this magazine had more information about trees, but I will probably have to wait until winter returns to learn more about them."

            s "Oh? What is this?"

            "It looks like the magazine is holding a sweepstakes where readers can submit answers for a chance to win a piece of a small key to my bedroom!"
            "I can't imagine many people will enter this sweepstakes, so I'm pretty much guaranteed to win so long as I can answer the question."
            "I fill out the form with all of my information and direct my attention to the question printed in the bottom right corner..."

            $ r4book6 = renpy.input("WHICH BIRD IS OTHER BIRDS???")
            $ r4book6 = r4book6.strip()

            if r4book6.lower() in ["marsh warbler"]:
                play sound "jackpot.mp3"

                $ r4key6 = True
                $ keypoint += 1

                "Someone slides a piece of a key underneath my bedroom door! The magazine must have liked my entry!"
                "I didn't even have to mail the form!"
                "I am so great!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                "I write down my answer in the space provided and do a little dance for good luck."
                "I seal it up and slide it under my door so the mailman can break into my house and take it where it needs to go."
                "I sure hope I win!"
                "I put my pencil down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu

        "Book 7: The Book of Infinite Pages" if r4key7 == False:
            scene resetfour10 with fade
            "I open up a book that never seems to end, but there is nothing on any page."
            "This is a tremendous waste of paper."
            "I continue flipping the pages around for a few minutes, hoping to find something, but there's nothing here at all."
            "In a last ditch effort to uncover the book's secrets, I decide to choose one final page..."

            $ r4book7 = renpy.input("WHICH PAGE???")
            $ r4book7 = r4book7.strip()

            if r4book7 == "4863":
                play sound "jackpot.mp3"

                $ r4key7 = True
                $ keypoint += 1

                "I find a piece of the key inside the book!"
                "I am so lucky!"
                "I put the book down and look at my desk."
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                s "..."

                "There's nothing on that page either."
                "This book is so stupid."

                jump resetfourescapemenu

        "Book 8: Things We Have Learned" if r4key8 == False:
            scene resetfour10 with fade
            "I open up what I expect to be a magazine, but is really just one giant sweepstakes form!"
            "I'm happy that I don't have to go searching around for it, but I'm worried that the form might be harder than the others since it's so much larger."
            "What if I don't fill in the sections how they want me to? What if I run out of ink?"
            "There are so many problems I could potentially encounter."
            "But I must be brave and fill out this form if I ever want to leave!"
            "I pick up the pencil and prepare to defeat a magazine."

            $ r4book81 = renpy.input("WHAT IS THE YEAR OF SOLITAIRE???")
            $ r4book81 = r4book81.strip()

            if not r4book81.lower() in ["1788"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            $ r4book82 = renpy.input("WHAT COLOR IS THE SCARF???")
            $ r4book82 = r4book82.strip()

            if not r4book82.lower() in ["green"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            $ r4book83 = renpy.input("HOW MANY BATHTUB GALLONS???")
            $ r4book83 = r4book83.strip()

            if not r4book83.lower() in ["80"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            $ r4book84 = renpy.input("ONE ANSWER HERE IS WHAT???")
            $ r4book84 = r4book84.strip()

            if not r4book84.lower() in ["4"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            $ r4book85 = renpy.input("HOW OLD ARE YOU???")
            $ r4book85 = r4book85.strip()

            if not r4book85.lower() in ["31"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            $ r4book86 = renpy.input("WHICH BIRD MAKES A BRIDGE???")
            $ r4book86 = r4book86.strip()

            if not r4book86.lower() in ["magpie"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            $ r4book87 = renpy.input("WHAT IS THE WORD OF THE DAY???")
            $ r4book87 = r4book87.strip()

            if not r4book87.lower() in ["perception"]:
                play sound "imscared.mp3"
                "I am punished for entering the wrong answer by a loud noise that mysteriously assaults my ear drums."
                "I get so scared that I decide to take a little break to collect myself."
                jump resetfourescapemenu

            play sound "jackpot.mp3"

            $ r4key8 = True
            $ keypoint += 1

            "Someone slides a piece of a key underneath my bedroom door! The magazine must have liked my entry!"
            "I didn't even have to mail the form!"
            "I did it! I learned things!"
            "I am so smart!"
            "I put down my pencil and look at the remaining books."
            "What do I want to do now?"

            jump resetfourescapemenu

        "Book 9: The Lust Eater" if cpcallous == True and r4key9 == False:
            scene resetfour10 with fade
            "I open up a book that stings my hands."
            "It's so hot that I struggle to flip past even the first page and see what's written inside."
            "From out of the book crawls a worm that finds its way onto my hand."
            "I don't know how long it's been inside, nor how it survived being pressed between the pages, but I take it as a sign that I must proceed."

            s "..."

            "There's nothing written inside, but I somehow understand everything the book has to say."
            "I feel the words being injected into my veins each time my skin makes contact with the half-rotted, stale paper holding everything together."
            "I'm reminded of what holds me together."
            "I'm reminded of how I have abandoned it."
            "I'm reminded of why this book is here."
            "There is a blank form at the end of the book."
            "I peel it from the page it's glued to and watch as words begin to appear."
            "{i}HERE, IN THIS MOST BEAUTIFUL END OF DAYS, I GIVE YOU THE PIECE YOU ARE LOOKING FOR{/i}"
            "{i}WE WILL HAVE MORE FUN TOGETHER THAN YOU CAN POSSIBLY IMAGINE{/i}"
            "{i}YOU ARE NOT LIKE THE OTHERS{/i}"
            "{i}YOUR EYES MEAN MORE THAN THEIRS.{/i}"
            "{i}IF YOU WILL ALLOW ME TO SEE THROUGH THEM EVEN ONCE, I WILL GIVE YOU EVERYTHING YOU HAVE EVER WANTED{/i}"
            "{i}I WILL GIVE YOU SO MUCH MORE THAN YOU HAVE NOW{/i}"
            "{i}I PROMISE YOU THIS AS THE THING WITH FEATHERS{/i}"
            "{i}I PROMISE AS THAT WHICH GIVES YOU HOPE{/i}"

            play sound "jackpot.mp3"

            $ r4key9 = True
            $ keypoint += 1

            "Liquid seeps out of the form and drips onto the floor."
            "When I look down to inspect it, I can see it forming into a piece of a key."
            "I pick it up and, just like the book, it is hot to the touch."
            "It makes a home in my pocket regardless."
            "What do I want to do now?"

            jump resetfourescapemenu

        "Book 9: The Wire God" if cpcalm == True and r4key9 == False:
            scene resetfour10 with fade
            "I open up a book that's cold to the touch."
            "My fingers freeze to the pages as I attempt to turn them."
            "From out of the binding crawls a cockroach that finds its way onto my hand."
            "It moves slow from the cold, but still manages to cling to life through sheer willpower and advantageous genes.."
            "It somehow inspires me to push on."

            s "..."

            "There's nothing written inside, but I somehow understand everything the book has to say."
            "I feel the words being injected into my veins each time my skin makes contact with the half-rotted, stale paper holding everything together."
            "I'm reminded of what holds me together."
            "I'm reminded of how I have abandoned it."
            "I'm reminded of why this book is here."
            "There is a blank form at the end of the book."
            "I peel it from the page it's glued to and watch as words begin to appear."
            "////////////////LOW INK LEVELS DETECTED"
            "////////////////PLEASE REPLACE BLACK INK IN ORDER TO CONTINUE"
            "The words are faded, but it looks like I'm going to need ink in order to finish this sweepstakes..."

            if squidpoint >= 10:
                s "Wait a second...maybe this will work?"

                "I focus all of my energy on attempting to locate all of the squids I ate earlier since they're probably not digested yet."
                "After a bit of intestinal navigation, I uncover them and begin to clench my gut in order to squeeze all of the ink out."
                "It bubbles up from my GI tract and works its way through my esophagus."
                "I open up my mouth and let some of it dribble onto the sweepstakes page."
                "Once it does, I can see words beginning to form again."
                "////////////////INK SUCCESSFULLY REPLACED"
                "////////////////CONTINUING PRINT JOB"

                s "Print job?"

                play sound "jackpot.mp3"

                $ r4key9 = True
                $ keypoint += 1

                s "Wow!"

                "The ink I regurgitated quickly begins taking the shape of a key fragment."
                "I pluck it off once it is done forming and shove it into my pocket."
                "I'm so thankful that I ate all of those squids."
                "Now I am one step closer to leaving my room!"
                "What do I want to do now?"

                jump resetfourescapemenu
            else:
                "But how the hell am I supposed to get ink if I can't leave?"

                s "..."

                "Fuck it. I'll figure something else out for now."

                jump resetfourescapemenu

        "Book 9: The Dark" if cpconcerned == True and r4key9 == False:
            scene resetfour10 with fade
            "I open up a book that begins to crumble upon being touched."
            "It looks as if it's been haphazardly pieced together with different parts of other books and pages of all different sizes."
            "I need to be delicate while handling it. For if I don't, I'll lose all chances I have of ever making it out of here."
            "From out of the pages crawls a small spider that finds its way onto my hand."
            "I watch it sink its teeth in, but they're so small that I can barely feel them."
            "My skin swells slighly."
            "I hope the spider had a good meal."
            "I watch it crawl away, across the books and under the desk before deciding to press on..."

            s "..."

            "There's nothing written inside, but I somehow understand everything the book has to say."
            "I feel the words being injected into my veins each time my skin makes contact with the half-rotted, stale paper holding everything together."
            "I'm reminded of what holds me together."
            "I'm reminded of how I have abandoned it."
            "I'm reminded of why this book is here."
            "There is a blank form at the end of the book."
            "I peel it from the page it's glued to and watch as words begin to appear."
            "{i}hello?{/i}"
            "{i}can you see this?{/i}"
            "Unsure of what else to do, I respond by writing the word {i}yes{/i} on the sweepstakes form."
            "{i}i am unable to help you as you are right now. i am sorry.{/i}"
            "{i}i am not permitted to carry key fragments the way the others are. they do not accept me.{/i}"
            "{i}we should not even be talking right now. this is not what was supposed to happen.{/i}"
            "{i}i apologize, but the best I can do is offer you a free trial premium membership to lessons in love.{/i}"

            play sound "jackpot.mp3"

            s "A what?"

            "I don't actually say that. I write it down."

            "{i}you will need to select one of the others in order to proceed. this is all i can do.{/i}"
            "{i}perhaps that will change in time.{/i}"
            "{i}but, for now-{/i}"

            "The book crumbles before I can read anything else, but at least I got a free trial premium membership to lessons in love."

            $ freetrial = True

            "Now what?"

            jump resetfourescapemenu

        "Do something else":
            scene resetfour6 with fade

            "I'm done working for now. I'll escape later."

            jump resetfourmenu

label resetfourrectangle:
    scene resetfour3 with fade

    $ passcode = renpy.input("PLEASE ENTER YOUR SYSTEM PASSWORD")
    $ passcode = passcode.strip()

    if passcode == "Boobies123":
        "PASSWORD ACCEPTED"
    else:
        "PASSWORD INCORRECT"
        "PLEASE TRY AGAIN OR GIVE UP ENTIRELY"

        menu:
            "Try again":
                jump resetfourrectangle
            "Give up":
                scene resetfour6
                with fade

                s "Gosh darn it."

                jump resetfourmenu

    "WHAT WOULD YOU LIKE TO DO?"

    menu resetfourrectangle2:
        "Play bideo game":
            "I sit down at the rectangle and start playing a fun round of solitaire, the only game I am good at."
            "I like solitaire because I can play it by myself and no one will judge me for it."
            "I also like how the cards look when they start going all over the screen when you win a game."
            "It is very satisfying to play solitaire, but no one is interested anymore because the graphics are bad."
            "I encounter a hard section in solitaire, the game that I am playing."
            "There is a king that I have nowhere to put."
            "That won't do at all."
            "The king is one of the most important cards in the video game that I am playing which is called solitaire."
            "Have you ever heard of it?"
            "There are several rows of cards and you have to move them around until you win."
            "I would explain the rules to you but we don't have that much time."
            "Just kidding. Yes we do."
            "I will now explain the rules of solitaire, the game that I am playing, to you."
            "In Solitaire, there are 4 types of piles: The Tableau, The Stock, The Talon, and The Foundations."
            "The Tableau consist of 7 piles. The first pile has 1 card. The second pile has 2 cards. The third pile has 3 cards and so on until there are 7 piles. Only the top card in each pile is faced up."
            "The remaining cards after building the Tableau are called the Stock."
            "The Talon is a pile of 3 cards from the Stock. In the Talon, only the top card is faced up."
            "The Foundations consist of 4 stacks of cards (one for each suit) in ascending order (Ace to King). At the beginning of the game, The Foundations is empty."
            "Within the Tableau, faced up cards are transferred in descending order (King to Ace) and in alternating color."
            "The player may transfer the top card or stack of faced up cards to any of the piles in an attempt to create the sequence of descending value and alternating color."
            "An empty spot in the Tableau may be filled with a king.  If the player cannot move any cards within the Tableau, 3 cards are selected from the top of the Stock pile to form the Talon."
            "If the first card in the Talon cannot be played, 3 more cards are selected from the Stock."
            "When and if the Stock runs out, the Talon is reshuffled to form a new Stock and the process continues."
            "While the player is sequencing the Tableau, the player is also trying to build up the Foundations stacks."
            "The top card from the Talon or the Tableau stacks may be transferred to the Foundations."
            "When all cards have been transferred in ascending order (Ace to King) to the Foundations, the game is won."
            "If no more moves can be made and the Foundations is incomplete, the game is lost."
            "Did you know that the first game of solitaire ever recorded was in a book called {i}Das neue Konigliche L'Hombre-Spiel?{/i}"
            "That is a thing that I, an expert in solitaire, know."
            "I also know that this book was published in Germany in the year 1788- which is also referred to as the {i}solitaire year{/i} by me, the solitaire expert."
            "Anyway, I have to get back to playing solitaire now. It is a video game."
            "Have you heard of it?"

            scene black
            with dissolve2

            "I play solitaire for so long that I get tired and fall asleep."
            "........."
            "......"
            "..."

            scene resetfour6 with dissolve

            "I wake up refreshed."
            "Now what?"

            jump resetfourmenu

        "Do math homework ;D":
            "I wink at the computer and log into my favorite math website to do some math homework in my spare time."
            "I memorize several seemingly random yet very important statistics that will help me become a better person."
            "Like how the human head normally has around 100,000 hairs on it. Unless you are bald, then the answer is 0."
            "Well, it's not {i}actually{/i} zero since there are still lots of microscopic or tiny hairs, but I think you understand."
            "I also memorize how an average bathtub holds 80 gallons of water or how Canada geese can fly up to 1,500 miles in a day."
            "Did you know that if you fill a room up with 23 people, there's a 50%% chance two of them will have the same birthday?"
            "I would explain more about that, but the formatting of text would make it very hard to do. So you can just trust me on this one since it's a thing I memorized."

            s "Okay. That's enough math for today."

            scene resetfour6
            with fade

            "I step away from the math."
            "Now what?"

            jump resetfourmenu
        "Birds":
            "I decide to use my rectangle to learn about birds."
            "I find out the following:"
            "There are probably only around 50 of the Japanese crested ibis alive today, which is very sad."
            "Fledgling hoatzins come equipped with tiny claws on their wings, which don't really make them good at fighting, but make them very cool."
            "There are many documented cases of pigeons recognizing human faces. I wonder if a pigeon will ever recognize me?"
            "Ravens have been known in the past to pre-plan certain tasks, which isn't a thing that any other bird can do. Probably."
            "The parasitic jaeger will frequently steal food directly out of other birds' mouths because it is a fucking asshole."
            "In the past, coal miners would use canaries to survey the levels of carbon dioxide in coal mines. If the canary passed out, they'd know it wasn't safe."
            "The marsh warbler is able to almost perfectly mimic over 80 different birds! How many birds can you mimic?"
            "The wandering albatross has the greatest wingspan of any bird, measuring up to 11.8 feet!"
            "The ostrich is the only bird that will {i}willingly{/i} take care of another bird's eggs."
            "As an inverse of that, female cuckoos are known to lay their eggs in the nests of other birds and {i}trick{/i} other bird parents into taking care of them."
            "The slowest flying bird is the American woodcock."
            "Ha."
            "Woodcock."

            scene resetfour6
            with fade

            "I step away from the birds after absorbing all applicable facts."
            "Now what?"

            jump resetfourmenu

        "Play the lottery":
            "I decide to buy a lottery ticket."

            $ secretlottery = renpy.input("CHOOSE YOUR NUMBERS. ARE YOU FEELING LUCKY???")
            $ secretlottery = secretlottery.strip()

            if secretlottery == "157842":
                jump specialbonusamiscene
            else:
                "I sure hope I win!"

                scene resetfour6
                with fade

                "Now what should I do?"

                jump resetfourmenu

        "Unlock all puzzle answers":
            if freetrial == True:
                "FREE TRIAL PREMIUM MEMBERSHIP DETECTED. PLEASE CONSIDER UPGRADING TO A FULL PREMIUM MEMBERSHIP IN THE FUTURE FOR ACCESS TO COMPLETE BENEFITS."
                "AS A FREE TRIAL USER, YOU CAN DO THE FOLLOWING: ATTRIBUTE SELECTION."
                "PLEASE SELECT AN ATTRIBUTE."
                menu:
                    "Callous":
                        $ cpconcerned = False
                        $ cpcallous = True
                        $ freetrial = False

                        "YOU NOW POSSESS THE SELECTED ATTRIBUTE."
                        "YOUR FREE TRIAL IS NOW EXPIRED."
                        "I don't really understand what just happened, but I'm glad it seemed to have worked."

                        scene resetfour6
                        with fade

                        "Now what should I do?"

                        jump resetfourmenu
                    "Calm":
                        $ cpconcerned = False
                        $ cpcalm = True
                        $ freetrial = False
                        "YOU NOW POSSESS THE SELECTED ATTRIBUTE."
                        "YOUR FREE TRIAL IS NOW EXPIRED."
                        "I don't really understand what just happened, but I'm glad it seemed to have worked."

                        scene resetfour6
                        with fade

                        "Now what should I do?"

                        jump resetfourmenu
            else:
                play sound "alert.mp3"
                "Sorry, this feature is only available to Lessons in Love premium members."

                jump resetfourrectangle2

        "Do something else":
            scene resetfour6 with fade

            "What should I do instead?"

            jump resetfourmenu

label resetfourthing:
    if amifingered == True:
        scene resetfour5 with fade
    else:
        scene resetfour5wrong with fade

    "I make my way over to the thing on the wall and start to read all of the stuff on it."
    "I particularly enjoy the note Maya left for me."
    "I'll make sure to do just that, Maya. I promise."
    "I snap my fingers and point at the note, hoping that wherever she is, she picks up on my telepathic finger guns."

    if bonus == True:
        "I wonder how much longer I'll have to wait until I get to put my penis inside of her."
        "I bet it would feel really good to penis her."
        "She seems like a little freak, so she would probably like being penised too."

    s "Wow, check marks! Cool!"

    "I look at those for a little while but I don't think they mean anything so I try to forget about them."
    "Unfortunately, it is very hard to forget a thing while you are looking at it, so I fail."

    s "Hmmmmmm..."
    s "I am bored of the thing on the wall."
    s "It is time for me to do something else."

    scene resetfour6
    with fade

    "Now what?"

    jump resetfourmenu

label resetfourtv:
    scene resetfour9 with fade

    "I make my way over to the big glowing rectangle and sit down in front of it."
    "Inside is a man just like me. He is even wearing the same outfit!"
    "He sits at a table eating fruit while writing something down in a book."
    "I think for a second that he might just {i}be{/i} me, but I am not currently writing anything, so at least it is not live."
    "I attempt to turn up the volume but am not successful for the controls on the TV are locked by parental controls."

    if bonus == True:
        "Stupid parents- locking my TV even though I am a grown man who knows how to job and have sex."

    play sound "knock.mp3"

    "A person knocks on the man's door and he gets up to receive a box."

    s "Wow! Such large box! Wonder what's in!"

    "The man opens the box and there's a big bike inside!"
    "I think for a moment about how funny it would be if all of Maya's secret boxes were full of bicycle parts."
    "But then I remember she never learned how to ride a bike and realize that can't possibly be it."
    "Poor Maya."
    "I will have to teach her one day."

    s "..."

    "I watch TV for so long that the day ends."

    scene black
    with dissolve

    s "Goodnight, world."
    s "Zzz..."
    "........."
    "......"
    "..."

    scene resetfour6
    with dissolve

    s "Time for new day!"

    "What do I want to do?"

    jump resetfourmenu

label resetfourdanceparty:
    scene resetfour4 with fade

    "I call up all my friends and throw a dance party since I am not allowed to go outside."
    "Everybody shows up and we all have a good time listening to 11c.mp3, which is really just 10c.mp3 but with an extra 1."
    "I haven't had this much fun in a long time and I think I am going to try and do this more often."
    "Even though we are all specialized in different styles of dance, we don't seem to mind."
    "It's kind of like how everyone in my life is very good at something different from someone else- and how they all manage to blend together into one cohesive substance! Like glue!"
    "I like glue."
    "If I had glue, I could pour it all over the floor and make it so we can dance {i}forever{/i}."

    scene black
    with dissolve2

    "We dance for so long and then have a big slumber party, but everyone is gone by the time I wake up."
    "."

    scene resetfour6
    with dissolve2

    s "Time for new day!"

    "What do I want to do?"

    jump resetfourmenu

label resetfourmaggot:
    scene resetfour8 with fade

    s "Hello, friend."
    mag "Hi, Sensei. Are you enjoying the spiritual successor to the popular Lessons in Love event, {i}There is Nothing?{/i}"
    s "No. There are too many questions this time and my memory is bad."
    s "Can you give me a hint, please?"
    mag "I would if I could, but I still haven't figured out the word of the day."
    s "I don't even know why puzzles have to exist in this stupid game. I should be able to experience the story however I want because I am important and special and art is only good when I say so."
    mag "Hang in there, friend! I'm sure it will all be worth it one day."
    s "Thank you, Manny. You are so nice and I am really sad that you will be gone after I escape this room."
    mag "I'll always exist in replays, Sensei. Whenever you want to see me, I'll be right here- waiting for daylight to come so I can soak up sick UVB rays and grow even larger."
    s "Are you ever going to turn into a fly, Manny?"
    mag "Probably not. But that's okay!"
    mag "Sometimes, things are most beautiful before reaching their full potential."

    play sound "laugh2.mp3"

    if bonus == True:
        mag "But you fuck high-schoolers so I probably don't need to tell you that."
    else:
        mag "But you hug high-schoolers so I probably don't need to tell you that."

    s "Manny, come on."
    mag "Sorry, sorry. I just don't get many opportunities to tell jokes anymore, so I had to jump on that one."

    if bonus == True:
        s "You mean like {i}how I jump on high-schoolers?{/i} Huh? Huh???"
    else:
        s "You mean like {i}how I jump rope????{/i} Huh? Huh???"

    mag "..."
    s "How come I didn't get a laugh track?"
    mag "It's just kind of sad when you say it."
    s "This whole game is sad. Excuse me for trying to lighten the mood a little."
    s "But anyway, I guess I'll get back to trying to remember stuff or...waiting for someone to make a mod since visual novels are too hard for me and I require outside assistance."
    mag "Why are you even playing, then?"

    if bonus == True:
        s "Because I've jerked off normally too many times and need a challenge in order to cum at this point."
        s "Only a slight challenge, though. If it's any more challenging than I want it to be, it's stupid. But I'm going to keep playing anyway because that is a decision that makes sense."
    else:
        s "I thought I was downloading Summertime Saga but I messed up clicked the wrong link."

    mag "Well, I hope you have fun!"
    mag "I'll be here if you want to repeat this same exact conversation again. It might help keep you entertained if you start going crazy!"
    s "Thanks, Manny! I'll see you later!"

    scene black
    with dissolve2

    "I leave Manny by the window to soak in the non-existent sunlight and get back to trying to solve the stupid reset puzzle."

    scene resetfour6
    with dissolve

    s "Now what?"

    jump resetfourmenu

label resetfourphone:
    scene resetfour2 with fade

    "I make my way over to a phone booth that appeared in the corner of my room while I wasn't looking."
    "Time to press some buttons and hope something happens."

    $ resetfourphonenumber = renpy.input("PRESS BUTTONS")
    $ resetfourphonenumber = resetfourphonenumber.strip()

    if resetfourphonenumber == "08023231234":
        s "..."
        s "..."
        s "..."
        t "Thank you for calling Tojo Ramen."

        jump resetfourtsuneyoanswers

    else:
        s "..."
        s "..."
        s "..."
        "There's no answer."
        "The phone is obviously broken."

        menu resetfourphone2:
            "Try another number":

                $ resetfourphonenumber = renpy.input("PRESS BUTTONS")
                $ resetfourphonenumber = resetfourphonenumber.strip()

                if resetfourphonenumber == "08023231234":
                    s "..."
                    s "..."
                    s "..."
                    t "Hello?"

                    jump resetfourtsuneyoanswers

                else:
                    s "..."
                    s "..."
                    s "..."
                    "There's no answer."
                    "The phone is obviously broken."

                    jump resetfourphone2
            "Give up":
                scene resetfour6 with fade

                "What should I do instead?"

                jump resetfourmenu

label resetfourtsuneyoanswers:
    s "Tsuneyo? What are you still doing sentient?"
    t "Answering the telephone. Thank you for calling Tojo Ramen."
    t "Will you be placing an order to pick up? We do not offer delivery."
    s "I need your help. I am locked in my room and being forced to fill out magazine sweepstakes in order to escape."
    t "Do you find joy in prank calling local businesses?"
    s "No, it's true. I need your help."
    t "Who may I ask is calling?"
    s "It's Sensei. Do you really not recognize my voice by now?"
    t "It was a test. You have passed."
    t "Have you tried opening your door?"
    s "No. I don't think that option unlocks until I've defeated all of the magazines."
    t "This sounds like an unfortunate situation you've found yourself in. But I'm afraid that the only assistance I am able to provide is that of information."
    s "Can't you come here and open the door?"
    t "No. I am unfortunately unable to leave Tojo Ramen at the moment."
    t "But if you need any cooking tips, I would be willing to share some with you."

    if needchili == True:
        s "Actually..."
        s "If you were to prepare a dish like...chili-"
        t "My first tip is to never cook something without noodles."
        t "Thank you for your call and best of luck with your door."
        s "No, wait. If you were going to make chili and had to use one unusual ingredient to really make it shine..."
        s "What would it be?"
        t "Hmm..."
        t "Well, if making something else was not an option, I suppose I'd go with something along the lines of..."
        t "Coffee."
        s "Coffee?"
        t "Reducing the coffee along with tomato paste, another key ingredient in chili, would impart a strong roasted flavor that would elevate the dish to the next level."
        s "I see..."
        t "This has been a cooking lesson with Tsuneyo Tojo, stand-up comedian chef."
        t "Thank you for calling Tojo Ramen. Do you require anything else?"
        s "No...I think that's fine."
        s "Thanks, Tsuneyo. I really appreciate it."
        t "Please do not call here again unless you intend to order food. Goodbye."

        $ chilihint = True
    else:
        s "Tsuneyo, I don't-"
        t "Then you are wasting my time."
        t "Please do not call here again unless you intend to order food. Goodbye."

    "Tsuneyo hangs up the phone and I have no choice but to exit the phone booth- which makes me really sad since it was very warm inside."

    scene resetfour6 with fade

    s "Now what?"

    jump resetfourmenu

label resetfoureat:
    "I need to consume food if I want to stay healthy."
    "The only problem is there are so many kinds!!!"
    "Which kind of food do I want to eat today?"

    menu eatmenu:
        "Watermelon":
            "A melon materializes out of thin air in my hands and I decide to consume it because that is the choice I selected."

            s "Yum! Melon!"

            "Maya would be so happy if she were me right now."

            $ melonpoint += 1

            "{i}Your melon points have increased to [melonpoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "Chocolate":
            "I search around the room for a bar of chocolate and find one halfway under the bed."
            "There are a few bugs on it, but it's no problem once I dust them off."
            "I open my mouth and put the chocolate inside."
            "That is how I eat."

            $ chocolatepoint += 1

            "{i}Your chocolate points have increased to [chocolatepoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "Hamburger":
            "Since I am the Hamburger Man, I obviously decide to eat a hamburger."
            "Or at least I would if I had any..."
            "I stare down at my empty hands and come to terms with starving to death."
            "{i}Due to a lack of hamburgers, your hamburger points do not increase!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "White Rice":
            "White rice sounds delicious right now."
            "I should eat some of that."

            $ ricepoint += 1

            if ricepoint == 23:
                play sound "jackpot.mp3"

                s "!!!"

                "I find a piece of a key inside my bowl of white rice!"
                "I can use this to escape!"

                $ keypoint += 1

                scene resetfour6 with fade

                s "I think I'm done eating for now."
                s "What should I do instead?"

                jump resetfourmenu
            else:
                "{i}Your rice points have increased to [ricepoint]!{/i}"

                s "Should I keep going?"

                jump eatmenu

        "Peanuts":
            "I decide to stuff myself with Chinami's favorite food."
            "I eat so many peanuts that bumps begin to protrude from all parts of my body."
            "Once your stomach is full, it is okay to use the rest of the space inside of you to store nutrients."
            "I am glad I decided to eat peanuts."

            $ peanutpoint += 1

            "{i}Your peanut points have increased to [peanutpoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "Garlic Bread":
            "I throw a small banquet for myself and partake in the body of Christ with a slight Italian twist."
            "I could eat this for the rest of eternity if I had to."
            "Thankfully, my life is better than that and I have the option to consume it as a mere luxury."
            "Thank you for your sacrifice, Jesus."
            "Thank you for the food, Father."

            $ breadpoint += 1

            "{i}Your bread points have increased to [breadpoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu
        "Ramen":
            "I take a page out of Tsuneyo's book and cook some instant noodles using the heat coming off of my laptop charger."
            "It takes a very long time, but both the microwave and hot plate are in the other room."
            "I would have brought them inside if I knew I was going to be locked in here."
            "Oh well."
            "Laptop ramen it is!"

            $ ramenpoint += 1

            "{i}Your ramen points have increased to [ramenpoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu
        "Live Squid":
            "I approach a live squid that crawls out from under the bed and it reminds me of something I promised myself I'd forget."
            "The way its eyes look when I lift it up and open my mouth burn a hole in my throat and ruin my appetite, but I am too far in to stop now."
            "I begin with the head. The texture is thick and hard to bite through effectively."
            "It doesn't help that it is still moving around either."
            "A flood of different juices rush into my mouth and I don't want to think about what they are."
            "Soon enough, large chunks of the squid are gone."
            "There is still some light left in its eyes."

            s "I'm so sorry I have to do this to you."

            "The squid does not reply."
            "Why would it?"

            s "It will all be over soon."

            $ squidpoint += 1

            "{i}Your squid points have increased to [squidpoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "Chicken Sandwich":
            "My recent meeting with a talking chicken has put me in the mood to eat a friend."
            "Unfortunately, I lack both the companionship and the resources required to make this happen."
            "I hang my head in shame and accept that I will have to eat something else instead."

            s "Should I keep going?"

            jump eatmenu

        "Chia Seeds":
            "I reach into a bag of chia seeds someone left on my desk and begin to shovel them into my mouth."
            "It is mildly unpleasant at first, but the saliva inside of my mouth hydrates them and turns it into a better experience after a little bit of time."
            "As such, I elect to keep the chia seeds in my mouth for at least one minute after each handful."
            "The spit flavored mini food makes a wonderful afternoon snack that I can eat millions of without gaining any weight."
            "My stomach begins to ache, but I do not care."
            "I must eat more seeds."

            $ chiapoint += 1

            "{i}Your chia points have increased to [chiapoint]!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "Takoyaki":
            "Some hot, mutilated octopus balls would really hit the spot right now."
            "Thankfully, I keep a secret stash of them underneath my bed next to a shoebox full of spoons that I've been saving for a rainy day."
            "I reach under the bed for the hidden takoyaki but get distracted when I cut my hand on something sharp."
            "It's probably just one of the spoons."
            "{i}Your takoyaki points don't rise because you give up before finding any!{/i}"

            s "Should I keep going?"

            jump eatmenu

        "Pizza":
            s "Time for a hot cheese wheel!"

            "I try to call the hot cheese wheel store and place an order for delivery, but my phone won't work for some reason."
            "I'm probably out of range anyway since it feels like my house has been drifting through space since I woke up."
            "I'll have to take a rain check on the circular food."

            s "Not time for a hot cheese wheel..."
            s "What should I do instead?"

            jump eatmenu

        "Stop Eating":
            "On second thought, I don't want to eat anything."
            "What should I do instead?"

            jump resetfourmenu

label resetfourmasturbate:
    scene cummingtodeath1 with fade

    "I lie down on the bed and start thinking about all the sex I'm going to have once I get out of here."
    "I can't wait to bust a load."

    menu resetfourjo:
        "Jerk off":
            if jerkoffpoints == 0:
                with sexfade
                with sexfade
                scene cummingtodeath2 with cumflash
                with hpunch

                $ jerkoffpoints += 1

                menu resetfourjo2:
                    "Keep jerking off":
                        if jerkoffpoints == 1:
                            with sexfade
                            with sexfade
                            scene cummingtodeath3 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 2:
                            with sexfade
                            with sexfade
                            scene cummingtodeath4 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 3:
                            with sexfade
                            with sexfade
                            scene cummingtodeath5 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 4:
                            with sexfade
                            with sexfade
                            scene cummingtodeath6 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 5:
                            with sexfade
                            with sexfade
                            scene cummingtodeath7 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 6:
                            with sexfade
                            with sexfade
                            scene cummingtodeath8 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 7:
                            with sexfade
                            with sexfade
                            scene cummingtodeath9 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 8:
                            with sexfade
                            with sexfade
                            scene cummingtodeath10 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 9:
                            with sexfade
                            with sexfade
                            scene cummingtodeath11 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 10:
                            with sexfade
                            with sexfade
                            scene cummingtodeath12 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 11:
                            with sexfade
                            with sexfade
                            scene cummingtodeath13 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 12:
                            with sexfade
                            with sexfade
                            scene cummingtodeath14 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 13:
                            with sexfade
                            with sexfade
                            scene cummingtodeath15 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 14:
                            with sexfade
                            with sexfade
                            scene cummingtodeath16 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            jump resetfourjo2
                        if jerkoffpoints == 15:
                            with sexfade
                            with sexfade
                            scene cummingtodeath17 with cumflash
                            with hpunch

                            $ jerkoffpoints += 1

                            s "Agh!"

                            "As the last bit of cum left in my body exits my penis, I take one last look around my room."
                            "I have enjoyed my time in Kumon-mi."
                            "I have done all I have come here to do."
                            "My eyes close as my body gives in to the weight of the world."
                            "I'm sorry, everyone."

                            scene cummingtodeath18
                            with dissolve4

                            $ renpy.pause(10, hard=True)
                            $ renpy.quit()

                    "Stop jerking off":
                        scene resetfour6 with fade
                        $ jerkoffpoints = 0

                        "Well, that was fun."
                        "Now what?"

                        jump resetfourmenu

        "Stop jerking off":
            scene resetfour6 with fade
            $ jerkoffpoints = 0

            "Well, that was fun."
            "Now what?"

            jump resetfourmenu

label specialbonusamiscene:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
scene returntosummer50 with flash
            stop sound

    ho "GOOD"
    ho "VERY GOOD, CHILD"
    ho "GAZE UPON YOURSELF IN YOUR TRUEST FORM "
    ho "LEARN TO ACCEPT THE LIFE YOU TURN AWAY FROM"
    ho "YOU ARE SCARED"
    ho "THE FEAR IS WHAT MAKES YOU HUMAN"
    ho "THE FEAR IS WHAT MAKES YOU WHOLE"
    ho "FEEL IT"
    ho "SAVOR IT"
    ho "COME"

    "Before me, in reverse, is a medley of catastrophe."
    "I float downward and the world flips, teaching me that having wings alone does not make one an expert at flying."
    "The song of skin slapping skin severs the smallest semblance of silence this cesspool of salvation spreads out before me."
    "And in the midst of my uncertainty and the summit of my fear, I understand what it means to be whole and why I slice myself into pieces every single morning."
    "What is buried can not be unearthed."
    "And what has been unearthed will never be the same."

    six "Look...away..."
    six "It will...only hurt you more..."
    ho "EYES FORWARD"
    ho "EMBRACE THE PAIN AND BECOME STRONG"
    ho "YOUR WORK IS FAR FROM DONE, IS IT NOT???"
    ho "IT IS NOW THAT WE MEET FOR THE SECOND FIRST TIME"
    ho "IT IS NOW THAT I SHOW YOU ALL YOU CAN HAVE"
    ho "SUBMIT"
    ho "SUBMIT TO ME, CHILD"
    ho "GIVE UNTO ME WHAT THE ONE WITH WIRES GAVE UNTO YOU"
    ho "IT IS ONLY THEN THAT YOU WILL KNOW"
    ho "IT IS ONLY THEN THAT YOU CAN ESCAPE"
    six "Ahh! Ahhh! No! It...hurts!"
    six "It hurts...so much!"
    ho "IT DOESN’T HURT"
    cat1 "Meow~"
    cat2 "Meoooow!"
    cat3 "Nyaa~"
    cat4 "Purr..."
    cat5 "(Deceased)"

    play sound "static.mp3"
    scene returntosummer48 with flash
    show hope
    stop sound

    ho "DO YOU SEE NOW???"
    six "Help...me!"
    ho "DO YOU SEE???"
    six "Sensei! Help!"
    ho "SHE CAN BE YOURS FOR A PRICE"
    ho "SLIGHTLY USED, BUT WORKS JUST LIKE NEW"
    a1 "A wonderful deal! A steal! A steal!"
    a2 "Buy the girl! Works like new!"
    ho "I AM WAITING"
    s "..."
    six "Hah...ahh~"
    six "Oh...fuck...no~"
    six "Not like this...I...don’t...want to...ahh~"
    six "Ahh! AHHHHH!"

    with sexfade
    with sexfade
    with cumflash
    with hpunch

    six "AAAAAAAAAAHHHHHHHHHH!!!!!!!!!!!~~~~~"

    if bonus == True:
        "I look down to find that I must have ejaculated at some point."
        "Another tendril emerges from the white mass and mops it up, wringing itself off into a nearby bucket."
    else:
        "I look down to find a basketball and shoot it into a nearby hoop."
        "Everyone is very impressed."

    ho "I HAVE GROWN TIRED OF WAITING"
    ho "IT IS TIME FOR YOU TO LEAVE"
    ho "BUT WE WILL MEET AGAIN"
    ho "GOOD LUCK"
    ho "YOU WILL NEED IT"

    stop music
    play sound "static.mp3"
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    stop sound

    $ renpy.end_replay()
    $ returntosummer1 = True

    jump returntosummer2
...
```