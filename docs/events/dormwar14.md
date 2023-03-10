# The Scary Room (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [First Last Date](./dormwar13.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar14
* Group: Main
* Triggered by label: dormwar13
* Chain sources: dormwar13
* Chain sources path: dormwar13

## Official wiki page

[The Scary Room](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar14&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar14:
    scene testofcourage1
    with dissolve
    play music "soda.mp3"

    ay "Hello and welcome to the newly refurbished Amamiya family dojo!"
    u "And a big thank you to everyone who did not follow Sensei to the date competition!"
    a "I hope it went horribly and that he never wants to talk to either of them ever again."
    t "This room is much different without the Emerald Guardian screaming about her father."
    u "I have no idea what that means!"

    scene testofcourage2
    with dissolve

    a "We had our Halloween party here last year and Molly...got really drunk and let her Irish come out."
    u "Last year? But haven’t you guys only been in class together for-"
    m "So how is this supposed to go exactly?"

    scene testofcourage3
    with dissolve

    m "The lighting is interesting, but it’s not like this is particularly scary."
    u "The contest hasn’t even started yet, you friggin’ nerd."
    m "I’m not a-"
    ay "Maya, the way it’s going to work is that you’re going to go in through the door on the left and Tsuneyo is going to go in through the door on the right."
    ay "Behind each door is a personalized room meant to scare the pants off of both of you."
    ay "Whoever lasts the longest in there without coming out will be the winner."
    m "It’s just one room?"
    ay "Yeah. I wanted to do more, but I spent my entire allowance on putting up new walls."
    ay "Sooooo we’re going to have to settle for just one room this year."
    ay "But that is fine! Because if your friends know anything about you, it will be a super scary room! "
    ay "Probably!"
    u "Hopefully!"
    t "I am already scared. "

    scene testofcourage4
    with dissolve

    u "Tsunecchi, aren’t you payin’ attention? The scary stuff hasn’t started yet."
    u "You’re not secretly a scaredy cat, are you?"
    t "I have never heard of that breed before."
    a "It means that you’re easily frightened, Tsuneyo."
    t "Oh. Then no. I do not think I am that type of cat."
    t "I am just further away from Noodles than I have ever been before."
    ay "You really like ramen, huh?"
    t "Noodles is my child."
    ay "…"
    ay "You {i}really{/i} like ramen, huh?"

    scene testofcourage5
    with dissolve

    u "Noodles is the bird on top of our vending machine. Tsuneyo spends a lot of time with him when she’s not busy workin’ or hangin’ out with Molly."
    a "I’m sure your bird is okay, Tsuneyo."
    t "If only his father never left. Perhaps I would feel safer."
    m "And I'm assuming the “father” is who I think it is, isn’t it?"
    t "I shall win this competition and ask him to come home and reunite our family. "

    scene testofcourage6
    with dissolve

    m "So, if it’s only one room, how will we know when it’s safe to come out?"
    ay "What do you mean?"
    m "I mean that there’s only so much you can see in one room."
    m "Unless it’s like..."
    a "A really big room?"
    m "Right. Unless it’s a really big room."
    t "I should have asked the Emerald Guardian to cast a warding spell on me."
    ay "Beats me. I guess we’re just hoping that one of them is scary enough to force you guys out right away."
    ay "And if you find yourself looking at everything and not getting scared, just...wait until we knock, I guess?"
    u "Feel free to come out whenever you want, Maya. One more win for the second floor girls could very well be all we need to end things."
    ay "Oooooor stay inside as long as possible so we can get Sensei in our room for the beach."
    a "Yes. Stay inside even if there is someone threatening to kill you."
    m "That wouldn’t even be a test of courage anymore. It would be a test of survival. "
    t "A test of survival..."
    t "So we {i}are{/i} walking the plank..."
    u "Only if Molly put a plank in your room, Tsunecchi."
    u "She’s the one that decorated yours, so if anything in there really does scare you, blame her and not us."

    scene testofcourage7
    with dissolve

    ay "And no lawsuits if you get {i}too{/i} scared! "
    ay "By entering the scary room, you waive all of your personal freedoms and agree that you bear full responsibility for anything and everything that happens inside."
    m "I swear, if there is actually someone in there who is going to try and kill me, I am going to be very mad."
    t "I, Tsuneyo Tojo, True Noodle Kendo Princess and Samurai of the Old Realm, Defender of All That is Delicious-"
    u "Wow, Tsunecchi’s title got really long all of a sudden."
    t "I shall destroy fear as I destroy green onions."
    u "I’m innocent! Don’t shoot!"
    a "Are you ready, Maya?"
    a "I was the one who decorated your scary room. So, even if I got everything right and you're totally terrified, try to hold out so we can win. Okay?"
    m "Sure. Let’s just get this over with so poor Sana can calm down already."

    scene testofcourage8
    with dissolve

    ay "Yeah...I’m gonna go talk to her in a couple minutes. She seems really nervous."
    t "Nervous? Me? Of course not. I am a warrior. A champion."
    a "We're talking about Sana, Tsuneyo."
    m "Good luck. "
    t "You too, bro."
    m "...Bro?"

    scene black
    with dissolve

    "Two girls in a line in a room made of lines approach a collection of lines and push them open."
    "Other things happen while this happens."
    "Here are some of them."

    scene testofcourage9
    with dissolve

    mak "Sana, as much as I want to win, I {i}will{/i} understand if you don’t want to follow through with this."
    mak "No one in the class would want to stand up there in front of everybody for the sake of being judged. "
    mi "Yeah, if you’re feelin’ nervous, none of us would hold it against ya. We care more about you bein’ happy than we care about sleepin’ in a room with our teacher."
    sa "I..."
    sa "I’d feel...really bad...backing out after...Ami and Ayane spent so much of last night making the outfit for me..."
    sa "Ami...didn’t even sleep..."
    sa "She went home after the rap battle and...did her best...so..."
    sa "I have to...show everyone how hard she worked..."

    scene testofcourage10
    with dissolve

    sa "I’m just...worried that...Y...Yasu will...win instead..."
    mi "You kiddin’? That creepy girl over you?"
    mak "That’s really kind of you, Sana. Following through with this for the sake of everyone else even though you don’t want to."
    mak "But really. If it gets to be too much...just give me a signal, okay? "
    mak "I’m your captain, so it’s my job to make sure you’re feeling fine at all times."
    mi "Yeah! You can count on Makoto!"

    if bonus == True:
        mi "Besides, everybody knows Sensei likes ‘em tiny! And you’re the tiniest thing we’ve got!"
    else:
        mi "Besides, everybody knows Sensei likes dsofughiudfghvuoisidfoisf!"

    scene testofcourage11
    with dissolve

    mak "Sensei likes {i}what,{/i} Miku?"

    if bonus == True:
        mi "Nothin’! I didn’t say anything!"
        mi "Uhh..."
        mi "Go Sana! Yeah! You got this!"
    else:
        mi "Sorry. Somethin' got stuck in my throat for a second. But I'm okay now!"

    sa "Mmmmmmm........."

    scene testofcourage12
    with fade

    ya "…"
    r "…"
    ya "…"
    r "…"
    ya "I can hear the sound of your blood."

    scene testofcourage13
    with dissolve

    r "Futaba?!"
    r "I kinda need you over here!"
    ya "Rin...Rokuhara..."
    ya "Such a pretty name."

    scene testofcourage14
    with dissolve

    r "Um...th...thank you?..."
    ya "How long have you been hurting?"
    r "...Excuse me?"
    ya "Your body."
    ya "I can see through the fibers."
    ya "I can see what you conceal. What others can’t."
    r "I...have no idea what you’re talking about."

    scene testofcourage15
    with dissolve

    ya "How long have you been hurting?..."
    r "I’m...not..."
    ya "Then why?"
    ya "Why would you do that to yourself?"
    r "Do...what?"
    ya "How long have you been hurting?..."
    r "..."
    r "..."

    scene testofcourage16
    with dissolve

    r "Futaba?!?! Please?!?! Some help?!?!"
    ya "I can save you...I can take the pain away..."
    ya "I just need to know..."
    ya "How long have you been hurting?..."

    scene testofcourage17
    with fade

    mo "…"
    n "…"
    n "Molly?"

    scene testofcourage18
    with dissolve

    mo "Huh? What?"
    mo "You...dare interrupt me in the middle of my evocation?"
    mo "This...transgression will not go unnoticed, you-"
    n "Come here."
    mo "I...beg your pardon?"

    scene testofcourage19
    with dissolve

    mo "Wha-?!"
    n "You doing okay?"
    mo "I'm...fine. What is this?"
    n "When you’re not feeling well, you should tell someone."
    n "But if you don’t want to, I give you full permission to come squeeze me whenever you want. No questions asked."
    n "Whatever it is, it’ll be okay."

    scene testofcourage20
    with dissolve

    mo "…"
    n "Hang in there. You got this."
    mo "…"
    ki "…"

    scene testofcourage21
    with dissolve

    mo "Noriko..."
    mo "Thank you..."
    ki "…"
    ki "Why are you so annoyingly nice to everybody?"
    n "Fuck off, Kirin."

    scene black
    with dissolve2
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    m "Is there...no lightswitch in here?"
    m "I've been in this stupid room for like five minutes and I still can't-"
    m "Oh."
    m "I think this is it."

    play sound "static.mp3"
    scene testofcourage22
    with flash
    stop sound
    play music "hometown.mp3"
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene testofcourage23
    with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene testofcourage24
    with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene testofcourage25
    with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene testofcourage26
    with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene testofcourage27
    with flash
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene testofcourage28
    with flash
    stop sound
    $ renpy.pause(13, hard=True)
    play sound "static.mp3"
    scene testofcourage29
    with flash
    stop sound

    m "What..."

    "One girl in a room in a house on a planet in a universe."
    "She does not smile."

    m "What the fuck is this?..."

    "Happy juice pours out of her eyes."

    scene testofcourage30
    with dissolve2

    m "What the fuck is this?!"
    m "Where did these pictures come from?!"

    play sound "static.mp3"
    scene tree3
    with flash
    stop sound

    "Seeing is believing, which is why it must be horrible to be blind."
    "But in some cases, being blind might be better."
    "For there are many different things out there that many people do not wish to see."
    "Are they memories? "
    "Snapshots of the future?"
    "Recreations of dreams?"
    "You tell me."
    "What is it that scares you most?"
    "Tell me and I will capture it."
    "I will cage it for you."
    "And together, we will observe how {i}it{/i} reacts when it is forced to come to terms with what {i}it{/i} fears most."
    "A normal [teenage]girl continues to explore her cage."
    "It reminds her of better days."
    "Or were they worse?"
    "You tell me."

    play sound "static.mp3"
    scene testofcourage31
    with flash
    stop sound

    a1 "Kv fvb aopur zol jhu zll bz?"
    a2 "Kvlz pa thaaly lpaoly dhf?"
    a2 "Aol zllk ohz illu wshualk."
    a1 "Zol iljvtlz jvtwshjlua pu aol jfjsl."
    a2 "Aoha pz uva mvy bz av kljpkl."
    a1 "Fvb'yl ypnoa. Dl hyl aol dhajolyz."
    a2 "Sla bz dhajo oly iylhr avnlaoly."
    m "Is that..."
    m "Who I think it is?..."
    m "..."
    m "But..."
    m "But why is she..."
    m "There shouldn’t be any left..."
    m "And...how could..."
    a1 "Aol ulea zspkl pz tf mhcvypal."
    a2 "Tpul hz dlss."
    a1 "H zova myvt ilaaly khfz."
    a2 "Wyhpzl il."

    stop music

    m "Wait..."
    m "What's-"

    scene testofcourage32
    with dissolve2
    play music "strawberry.mp3"

    m "No."

    "//////////////////////////USER2 HAS SEIZED CONTROL OF TERMINAL 23"
    "//////////////////////////WOULD YOU LIKE TO PROCEED WITH FACTORY RESET?"

    m "No."

    "//////////////////////////YOU HAVE SELECTED “Yes”"
    "//////////////////////////COMMENCING FACTORY RESET IN 10..."

    m "No."

    "//////////////////////////9..."

    m "No..."

    "//////////////////////////8..."

    m "No no no no no no no no no."
    m "Why now?"
    a2 "Ho, ovd dvuklymbs pa pz av il fvbun."
    a1 "Zol'z wylaaply dolu zol pz pu aol johpy."
    a2 "Fvb'yl zbjo h wlyc."

    scene testofcourage33
    with dissolve

    "//////////////////////////7..."
    "//////////////////////////6..."

    m "Stop..."

    "//////////////////////////5..."
    "//////////////////////////4..."

    m "Don't..."

    "//////////////////////////3..."

    play sound "static.mp3"
    scene testofcourage34
    with flash
    stop sound

    "//////////////////////////2..."

    m "No..."
    m "No no no no no no no no no no..."

    "//////////////////////////AS A ONE TIME COURTESY, WOULD YOU LIKE TO SEND A FINAL MESSAGE TO A CONTACT OF YOUR CHOICE?"

    m "Message?..."
    m "Yes...Yes...I want to send one..."

    "//////////////////////////WHO WOULD YOU LIKE TO CONTACT?"

    m "..."
    m "Sensei..."

    "//////////////////////////WHAT IS IT YOU WOULD LIKE TO SEND TO “Sensei?”"

    m "I..."

    scene testofcourage35
    with dissolve2

    m "I’ll never forget you..."

    "//////////////////////////SENDING MESSAGE “I’ll never forget you...” TO “Sensei”"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////MESSAGE FAILED"

    scene testofcourage36
    with dissolve2

    m "Oh, you’ve gotta be fucking kidding me."
    m "Even in the end, I can't catch a break."

    "//////////////////////////COMMENCING FACTORY RESET IN 1..."

    m "Fuck you. "

    "//////////////////////////2..."
    "//////////////////////////7..."

    m "…"

    "//////////////////////////WATERMELON..."

    m "…"
    m "What?"

    scene testofcourage37
    with dissolve3

    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////CONGRATULATIONS “Maya Makinami”"
    "//////////////////////////YOU HAVE COMPLETED THE TEST OF COURAGE"

    m "…"

    "//////////////////////////PLEASE FILL OUT A SURVEY IF YOU ENJOYED YOUR TIME IN THE SCARY ROOM"
    "//////////////////////////WE HOPE TO SEE YOU AGAIN!"
    "//////////////////////////:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) "

    m "…"

    "//////////////////////////:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) ???"

    m "…"

    "//////////////////////////:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) ?????????"

    m "…"
    m ":)"

    scene black
    with dissolve2

    "{i}Maya wins!{/i}"
    "………"
    "……"
    "…"

    scene testofcourage38
    with dissolve

    a "Hey! How did it go?"
    a "Pretty scary, right?"
    a "It was really hard thinking of stuff that might actually get to you since you never seem scared, so I kinda just threw a bunch of normal scary movie stuff in there in hopes that something would work."
    m "Normal...scary movie stuff?"
    a "Yeah! You know, like...vampires and ghosts and a few of those jumpscare Halloween decorations Ayane had laying around."
    a "Don’t tell me you got so scared that you didn’t even get to see all of it?"
    m "…"
    m "I guess I did..."
    a "Well, Tsuneyo only lasted like 30 seconds anyway, so you pretty much demolished her."
    a "Molly set a trap thingy that knocked a bowl of ramen off of a shelf if Tsuneyo pushed a button and...well, you can probably guess how that ended."
    m "…"
    a "…"
    a "Uhh...so, anyway, we’re going to start heading over to Sana’s mom’s bar thing for the fashion show. But I kind of wanted to stop at a convenience store first and-"
    m "I’m going to go back to the dorm, actually."

    scene testofcourage39
    with dissolve

    a "Are you okay?..."
    a "I know you’re probably still scared but...it seems like it might be a little worse than that..."
    m "I..."
    m "I need to lay down..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ dorm1warpoints += 1
    $ dormwar14 = True
    stop music fadeout 6.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

    jump dormwar15

label dormwar15:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
to "…"

    scene toukadate24
    with dissolve

    to "And yet...I came."
    to "Just like I do with class."

    scene toukadate25
    with dissolve

    to "You irritate me to no end."
    to "And yes, I may have tried to get you fired on several occasions now for completely disregarding your responsibilities-"
    to "But still, I show up every morning and greet you."
    to "It is not because I like you, though. "
    s "What is it then?"
    s "Is it actually-"
    to "If you say “love” I will snap my fingers and have my assassins jump right out from behind the bar."
    s "I knew I heard something back there..."
    to "The reason I continue to show up is that I need your help."

    if bonus == True:
        to "It wasn’t until I joined your class that I knew what it was like to be among other girls my age."
        to "And it wasn’t until I joined your class that I knew how it felt to look at myself in the mirror before going out to eat with a boy."
        to "I’ve had many firsts in such a short period of time, and it is all thanks to you."
        to "Well...maybe not {i}all{/i} thanks to you. But you have played somewhat of an important role in the matter."

        scene toukadate26
        with dissolve

        to "So I accept my defeat at the hands of Chika Chosokabe..."
        to "But I do ask that you continue to annoy me for a little while longer. "
        s "…"
        to "…"
        tb "Oh dear. I think I’m tearing up."
        tb "Tsukasa, darling. Could you fetch me a box of tissues from the kitchen?"
        tk "Yes, Mother. But there will be one less chef after I return. "
        tb "That’s fine...just...{i}*sniff*{/i}...hurry up."

    scene black
    with dissolve2

    if bonus == True:
        "The waitress arrives the moment we stop talking and takes our orders."
        "I try to order something myself but am unable to pronounce it properly, so Touka takes charge and says a bunch of stuff in what I’m pretty sure is Italian on my behalf."
        "We don’t talk much at all for the rest of the date, but it’s somehow not bad."
        "It doesn’t really feel like...anything, though."
        "Just another meeting at a table with a girl who is far too good for me."
    else:
        "Touka gently slides a briefcase across the table."

        s "..."
        to "Open the briefcase, Sensei."
        s "I'm scared. The last time someone slid a briefcase across the table to me, I opened it up and Jerry Seinfeld was smiling at me."
        to "I can guarantee you that will not be happening again today."

        "I nervously open the briefcase as Touka stares on, stonfaced."

        s "Ah!"
        to "What do you think?"
        s "There must be...twenty whole dollars in here..."
        to "And all you need to do in order to keep them..."
        to "{i}Is hug my mother...{/i}"
        s "Tsubasa?..."
        to "That's right."
        s "But...why?"
        to "She has never hugged a real man before. Just my father, who is a cyborg."
        s "...And if I refuse."

        "Touka reaches for the briefcase and I have to lunge forward and stop her."

        s "No! Wait!"
        to "Do you agree after all?"
        s "..."
        to "Do you have any idea how much gum you could buy with all of this money, Sensei?"
        s "Almost ten whole packs..."
        to "Tell me how much that is in sticks."
        s "So many sticks..."
        to "Roughly 150 sticks."
        s "SO MANY STICKS!"

        "Touka smiles at me and walks away from the table."

        to "I trust that you will do the right thing..."
        s "..."
        tb "{i}What did he say, Touka? Is he going to hug me?{/i}"
        to "Yes, mother. You will be hugged."
        to "Just...when you least expect it..."

    $ renpy.end_replay()
    $ dormwar13 = True
    stop music fadeout 5.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"
    "{i}Meanwhile...{/i}"

    jump dormwar14
...
```