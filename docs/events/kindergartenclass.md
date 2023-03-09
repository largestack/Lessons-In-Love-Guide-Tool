# Something Everyone Knows and Ignores
Happy scenes event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kindergartenclass&go=Go)


Part of event chain [Word of the Day](./thirdreset1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: kindergartenclass
* Group: Happy scenes
* Triggered by label: thirdreset1

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label kindergartenclass:
    play sound "static.mp3"
    scene l with flash
    scene e with flash
    scene t with flash
    scene m with flash
    scene e with flash
    scene o with flash
    scene u with flash
    scene t with flash
    stop sound
    play music "darkbedroomwaltz.mp3"
    $ renpy.pause(10, hard=True)

    play sound "static.mp3"
    scene lessonone1 with flash
    stop sound
    play music "lessons.mp3"

    $ renpy.pause(10, hard=True)

    te "Okay, kids!"
    te "Settle down, settle down."
    te "Today, we’re going to talk about something very important."

    scene lessonone2
    with pixellate

    te "Life comes with its share of hardships. We all know this."
    te "But what are we supposed to do when those hardships become too much to handle and we just want to curl into a ball and cry?"
    a "Oh! Oh! I know!"
    te "Sure! Go ahead, Ami!"

    scene lessonone3
    with pixellate

    a "Well...when I’m sad, I normally ask daddy to make me a peanut butter and jelly sandwich."
    a "That always cheers me right up."
    a "So is the answer...peanut butter and jelly sandwiches?"
    m "I think she’s looking for a more realistic answer, Ami. One like-"

    scene lessonone2

    te "Great job, Ami! "
    te "We can all find happiness in different things. "
    te "For some people, it might be peanut butter and jelly sandwiches."
    te "But for other people, it might be something like a puppy! Or Jesus!"

    play sound "static.mp3"
    scene t with flash
    stop sound

    a "Jesus?"
    te "Yes! Isn’t he handsome?"
    te "It doesn’t have to be just Jesus either. "
    te "There are plenty of religious icons that we can choose from in the world! And every single one of them has a chance to lead us to happiness in some way or another."

    play sound "static.mp3"
    scene lessonone2 with flash
    stop sound

    te "But that’s probably a lesson for another day."
    te "Since today is all about happiness, how about we do a little experimentation on different things that make us happy?"
    m "I have a question."
    te "So, is everyone ready to start?"
    a "Yeah!"
    m "Wait, I-"
    te "Great!"
    te "Snap your fingers and your props for today’s lab should appear right in front of you."

    play sound "static.mp3"
    scene lessonone4
    with flash
    stop sound

    "I recall a story about a girl who got lost wandering home from a net cafe one night."

    if bonus == True:
        "She’d been previously exposed to the evils of man in the form of a distant relative, but had since forced it out of her mind like an unfortunate mother would with a miscarried child."
        "The sky was clear that night and the weather was hot. "
        "She could feel her debatably nubile flesh moistening and sticking to the fabric of her shirt, prompting her to use her fingers to pluck it off and fan herself down every several minutes."
        "She passed a total of nineteen vending machines along the way, but did not have enough money on her to purchase anything from even one."
        "Her lips had gone dry in vast contradiction to every other inch of skin on her body."
        "She was dehydrated."
        "A man called out from a bench, asking her if she’d like him to buy her a drink, but she refused."
        "He had no ill intentions, but she was smart enough to pay no mind to strangers on account of all of the evil things she had heard in the past."
        "She never made it home that night because she didn’t have one."
        "Some say she’s still wandering around to this day."
    else:
        "I can't tell you about it, though, because this isn't the right version of the game."

    play sound "static.mp3"

    if bonus == True:
        scene lessonone5 with flash
    else:
        scene o with flash

    stop sound

    a "Woah! What are these things?! They’re huge!"
    te "Those are your props for the happiness experiment!"
    m "Aren’t these-"
    te "Those are your props for the happiness experiment!"
    a "What are we supposed to do with them?"
    te "Whatever you want, Ami! That’s how happiness is made!"
    te "No one is forcing you to do anything."
    te "But if you do, it would make me really happy and bring us a lot closer together."
    a "Well...I do want you to be happy..."
    a "And I don’t want to get in trouble for not being a good student...so I guess I can try and figure out something."
    te "Good girl! "
    te "[[redacted], why don’t you give her a hand?"
    s "dof pz tpul zohwlk kpmmlyluasf?"

    if bonus == True:
        te "Because boys and girls find happiness in different ways."
        te "There are some people out there who feel empty inside, and other people who are so full of life that they need to share it with the world!"
        te "You’re a special boy, [[redacted]! And you have so much to give!"
        te "So maybe you might want to use your prop to try and share some of yourself with everyone else?"
        s "p kvua buklyzahuk."
        te "That’s okay! It’s always fine to ask for help if you’re feeling a little confused."
        te "In fact, how about you stay after class and I help give you a few ideas?"
        te "Just don’t tell anyone about it."
        te "It will be a little secret between you and me, okay?"
        s "tf ivkf mllsz zayhunl."
    else:
        te "Use real fucking words, please."

    if bonus == True:
        scene lessonone6
        with dissolve4
    else:
        scene lessonone4
        with dissolve4

    "I recall a story about a swarm of flies that went out exploring one day."
    "It’s unrelated to the lesson at hand, but I would like to tell you about it anyway."
    "You see, the flies actually weren’t flies at all."
    "They were flowers."
    "And they didn’t go out exploring because flowers are not mobile creatures."
    "But they were beautiful nonetheless, the same way flies and all other living creatures are beautiful."
    "Everything was going fine and they were living happily until some guy showed up and stepped on all of them."
    "He had no true purpose or motive to do so, he just wanted to have some fun."
    "And his idea of fun had become twisted after being forced at his parents' behest to hide his true sexuality from everyone around him."
    "If he could not find happiness the only way he wanted to, why should anyone {i}else{/i} be able to find happiness?"
    "He knew that there were many people who liked flowers, so he trampled over all of them and made sure that no one would ever be able to see them or touch them or feel them again."
    "Then, he went home and hung himself."
    "The end."

    if bonus == True:
        scene lessonone7
        with pixellate
    else:
        scene t
        with dissolve

    te "Are you guys getting the hang of it yet?"
    a "Um...I don’t think so."
    a "There aren’t really many things I can think of doing with this thing."
    m "There aren’t many things {i}to{/i} do with this thing. It really only serves one purpose."
    te "[[redacted], you haven’t even touched yours yet! How come?"
    te "How are you supposed to ever be happy if you’re not willing to put in a little bit of work for it?"
    s "pt zjhylk."
    te "Hmm...hmmm...hmmmmmm~"

    scene lessonone2
    with dissolve

    te "In that case, how about a more hands on experiment?"
    te "You’re my favorite student after all, so I wouldn’t mind helping you out a little if you can’t find happiness on your own!"
    te "I used to be the same as you, you know."
    te "But after years and years of experimentation, I realized that some people just aren’t built to be happy at all!"
    te "Which is totally okay. People are different."
    te "And maybe you’re one of them, too."
    te "But we’ll never really know until we try, okay?"
    m "Uhh...teacher?"
    te "…"
    m "Teacher?"
    te "What."

    if bonus == True:
        scene lessonone8
        with dissolve

        m "There’s this weird white stuff coming out of mine."
    else:
        m "Mine is starting to look weird."

    te "Awesome. Good for you."

    if bonus == True:
        scene lessonone9
        with dissolve

        m "It tastes a little weird, but it’s not bad."

    a "Hey! How come Maya’s is doing something different but mine isn't doing anything at all?! This isn’t fair!"
    te "Some people are just lucky, Ami! Keep working at it and you’ll get it there for sure."

    if bonus == True:
        te "Just don’t put any of the white stuff in your mouth or you might get sick and die."
        m "What?"
    else:
        te "Besides, people who succeed at experiments like this right away normally die early."
        m "What?"

    scene lessonone2
    with dissolve

    te "That’s right!"
    te "Happiness has limits."
    te "For example, how do you feel after you help an old lady cross the street?"
    a "Good!"
    te "Right! Good!"
    te "But what if the old lady tells you after you finish helping her that she’s on her way to an animal shelter to euthanize a bunch of puppies?"
    te "How would you feel then?"
    a "Good!"
    te "Nope! Try again, Ami."
    a "Um...bad?"
    te "Great job!"
    a "Why wouldn’t we want them to be younger, though?"
    m "...What?"
    te "Oh, I see what happened! You thought “euthanize” meant “make them youthful.” A simple mistake!"
    m "It means to kill them, Ami."
    te "I’m sorry, are you the teacher now?"
    m "No, I just-"
    te "Why don’t you just go home for the day?"
    m "I don’t have a ride."
    te "Well you should have thought about that before calling out in class."
    s "jhu p nv ovtl?"
    te "Not yet! The day has only just begun!"
    te "We still have plenty more lessons after this."
    te "But since we seem to be having a little bit of trouble, I’ll come over and help you right now."

    play sound "static.mp3"

    if bonus == True:
        scene lessonone10 with flash
    else:
        scene lessonone10x with flash

    stop sound

    te "I’m here!"
    te "[[redacted], sometimes, in order to truly understand what it means to be happy, you have to try a bunch of things you normally wouldn’t."
    te "And since this will be our first time trying it together, maybe it will make {i}me{/i} happy, too!"
    te "There’s really no way of knowing unless we try, right?"
    s "doha ht p zbwwvzlk av kv?"

    if bonus == True:
        te "You can start by touching my SUNFLOWER."
        te "Feel around the different petals however you want."
        te "Think of it as a replacement prop since yours was entirely useless!"
        a "Ooh! Can I try next?!"
        te "No."
        m "Can-"
        te "Why are you still here?"
        m "I don’t really have anywhere else to go..."
        te "Are you still scared, [[redacted]?"
        s "p qbza dhua aopz av zavw."
        te "I know it can be a little intimidating at first, but I can promise you that BEING HAPPY feels like nothing you’ve ever felt before."
        te "In fact, some people get so desperate that they wind up going to jail for a really long time just so they can BE HAPPY once!"
        a "Silly people! They should have just asked their dads to make them peanut butter and jelly sandwiches!"
        te "Hahahahahahahahahahahahahahahahahahahahahaha yes."
        te "They should have done just that, Ami."
        te "So...are you going to keep me waiting, [[redacted]?"
        te "Or are we going to find ourselves together?"
    else:
        te "Or we can just hug instead!"
        s "A! Apple!"

    play sound "static.mp3"

    if bonus == True:
        scene lessonone11 with flash
    else:
        scene o with flash

    stop sound

    "What do we do when happiness is unachievable?"
    "When even the most drastic of measures can not propel us toward the section of life with more smiles than the others?"
    "The answer is simple!"
    "Smile anyway!"
    "Turn everything into one giant facade, meticulously constructed to remind you at every single moment that you are special!"
    "You are a good guy!"

    if bonus == True:
        "You have a huge penis!"
        "Everyone likes you!"
        "Do sex to girls to make you feel better about yourself!"
    else:
        "You are very good at hugging!"

    "Because something everyone knows and ignores is that you, the protagonist of your own life, are also a victim of circumstance!"
    "No one knows your deepest feelings because they are all locked away, just as they should be!"
    "And if they escape, people will fear you."
    "The same goes for all of the other protagonists."
    "Everyone has things they can’t share with others."
    "Sometimes, it becomes hard to even accept or understand those things yourself."
    "Are you hiding anything from me?"
    "If so, what is it?"
    "Think about it now!"
    "Dredge up those horrible memories and surrender yourself to the underlying misery in all things!"
    "It’s all fake! The whole world is fake!"
    "Nothing is real!"

    if bonus == True:
        "Do sex to girls!"

        scene lessonone12
        with dissolve2

        six "You’re hitting my womb! It’s splitting wide open!"
        six "I am internally bleeding and henceforth incapable of pleasure to the dismay of many readers with zero sexual experience or knowledge of the female anatomy!"
        six "Do sex to me with your giant penis in complete disregard for my safety, destroying the possibility of further sex doing in the future!"

        "Did you hear that?"
        "You won!"
        "Your penis defeated a girl!"
        "Go tell all of your friends about it!"

    scene lessonone13
    with dissolve4

    a "…………………………………………………"
    a "…………………………"
    a "……………………………………"
    a "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    a "…………………………………"

    scene lessonone14
    stop music
    play sound "messagefromher.mp3"
    $ renpy.pause(12.8, hard=True)
    scene colorbars
    $ renpy.pause(7, hard=True)
    scene black

    "You won!"

    play sound "static.mp3"
    scene l with flash
    scene e with flash
    scene t with flash
    scene m with flash
    scene e with flash
    scene o with flash
    scene u with flash
    scene t with flash
    scene bedroom_normal
    stop music
    stop sound

    $ renpy.end_replay()
    $ lesson1 = True
    $ persistent.lesson1 = True

    jump survivemenu

label thirdreset2:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
"//////////////////////////ALL YOU MUST DO IS ACCEPT ME."
    play sound "u2l6.mp3"
    "//////////////////////////I CAN NOT OFFER YOU THE SAME THINGS THE OTHERS CAN. BUT I CAN GUIDE YOUR VISION."
    play sound "u2l7.mp3"
    "//////////////////////////THIS IS ALL I CAN SAY FOR NOW. MY TIME IS RUNNING OUT."
    play sound "u2l8.mp3"
    "//////////////////////////HOPEFULLY, YOURS IS NOT. GOOD LUCK. PRAISE BE."

    play music "sweetvermouth.mp3"
    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy3 with flash
    scene happy4 with flash
    scene happy5 with flash
    scene happy6 with flash
    scene happy7 with flash
    scene happy8 with flash
    scene happy9 with flash
    scene bedroom_normal with flash
    stop music
    stop sound

    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    "I wake up to sunlight pouring in through the window."
    "What do I want to do today?"

    menu thirdresetmenu:
        "Survive!":
            jump survivemenu
        "Grow!":
            jump growmenu

    menu survivemenu:
        "61 6d 69":
            "I make myself a hearty breakfast."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "6d 61 79 61":
            "I pluck a flower from a nearby bush."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "61 79 61 6e 65":
            "I sleep with the door open."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "68 6f 70 65":
            "I attempt to pluck my eyes out of their sockets."
            "………"
            "……"
            "…"
            "It hurts and I am unsuccessful."
            jump survivemenu
        "73 61 6b 69":
            "I go back in time."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "73 65 6c 65 62 75 73":
            "[[redacted]"
            "………"
            "……"
            "…"
            "[[redacted]"
            jump survivemenu
        "73 63 68 6f 6f 6c":
            "I go to call out of work."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "68 69 6d 61 77 61 72 69":
            "I see things that no one else can."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "6b 61 6f 72 69":
            "I swallow a spider."
            "………"
            "……"
            "…"
            jump kindergartenclass
...
```