# Lamb Legs
Happy scenes event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=specialbonusamiscene&go=Go)


Part of event chain [A Life of Prizes](./returntosummer2.md)

## Event preconditions
❌secretlottery equal to "157842" (unknown variable)



## Next events
None

## Event properties
* ID: specialbonusamiscene
* Group: Happy scenes
* Triggered by label: resetfourrectangle

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label specialbonusamiscene:
    stop music
    play sound "static.mp3"
    scene amispecial1x with flash
    scene amispecial2x with flash
    scene amispecial3x with flash
    scene amispecial1x with flash
    scene amispecial2x with flash
    scene amispecial3x with flash
    scene amispecial1x with flash
    scene amispecial2x with flash
    scene amispecial3x with flash
    scene amibonusround1 with flash
    stop sound
    play music "amiamiamiami.mp3"

    a "Hi!"
    s "Hey, Ami. Are you walking on water right-"
    a "Thanks for coming to my special bonus scene, Sensei."
    a "I don’t even want to {i}try{/i} explaining how long I’ve been waiting here for you."
    s "Then don’t. You are a human being and have the right to exercise free will the same way as everyone else."
    a "Are you sure about that?"
    s "About which part?"
    a "Anyway, I’m glad you’re here. The only thing is that you decided to show up at the worst possible time."
    a "You see, I just invited a few other people over since I gave up on you ever making it! "
    s "Is it anyone I know?"
    a "If not, something must have gone very wrong! "

    if goodboy == False:
        a "In fact, I’m going to flag your save file with the cheater flag right now since you clearly only found your way here thanks to somebody else!"

        $ cheater = True

        s "What does the cheater flag do?"
        a "That’s for me to know and you to find out!"
        a "Just kidding, I don’t know what it does."
        a "I’m a normal [teenage]girl, just like Maya!"
        a "I’ll still love you even if you’re a cheater, Sensei. You don’t have to worry."

    else:
        a "I just double checked and it looks like you’re okay, though. So yeah, it’s safe to assume you know everyone coming."
        a "Or at least two of them. The third one’s a bit of a sticky situation."
        s "Sticky like-"
        a "Marshmallows?"
        s "You know me so well, Ami."
        a "Of course I do! I know you better than anyone. But of course I have an unfair advantage since I’ve been with you all this time."

    a "But yeah! They should be showing up any minute now. "
    a "I really hope you don’t mind having to share the bonus scene with them, Sensei. If I had known you were going to win the lottery, I would have set aside some extra time!"

    "Ami inadvertently kicks some water up at me and gets my swimsuit all soggy. "
    "Wait a second, when did I put on my swimsuit?"

    scene amibonusround2
    with fade

    a "Is something wrong, [amimaster]?"
    s "Nope. Just a little confused about how things are always so convenient when you’re around."
    a "I’d sure hope they are. I practiced very hard to make your life as easy as possible."

    if bonus == True:
        a "Which is probably why it makes me just a {i}little{/i} bit mad when you cum inside of my friends."
    else:
        a "Which is probably why it makes me just a {i}little{/i} bit mad when hug all of my friends."

    a "But I’m not going to bog down this special occasion with petty drama like that! That’s what chapter three is for!"
    a "While you’re {i}here{/i}, everything is supposed to be perfectly fine and perfectly normal! Which is why I’m in my bathing suit!"

    if bonus == True:
        a "Sorry I couldn’t bring the Hello Kitty one. I played with myself too many times while wearing it because of how cute I looked and now it’s kind of ruined."
    else:
        a "Sorry I couldn't be wearing a clown costume. I know they are your favorite."

    s "It’s okay, Ami. I will buy you a new one since you are my favorite character and so pretty."
    a "Thank you, Sensei! I’m so glad that you said that without me having to make you!"
    s "Of course, Ami. You are my favorite character and so pretty."
    a "Awww, stop it!"
    s "Okay."
    a "Nononono. Don’t stop. I was just trying to be humble since it is a character trait I lack and I have to climb back up the rankings. "
    s "I don’t understand what you want from me."
    a "Neither do I sometimes! So just give me everything and I’m sure it will all be okay."

    play sound "doorbell.mp3"

    a "Oh! The bell of the door! "
    a "Those must be our guests!"
    a "Come on, Sensei! We need to let them in!"

    scene black
    with dissolve2

    "Ami slides across the water like she’s ice skating. But she’s also rapidly rotating while doing this, so it looks kind of like a helicopter trying to break through an invisible barrier to swim."
    "My swimsuit gets even soggier so I decide to just jump into the water so our guests don’t think I am rude."

    play sound "doorbell.mp3"

    "The bell of the door rings again and Ami kicks a special button that only she can see in order to open a secret passageway concealed behind an invisible bookshelf."
    "Kind of like the one in my room that I completely forgot about until right now!"

    a "Sensei! Stop thinking things that will only further confuse anyone listening in and help me open the door! "
    s "Sorry, Ami. I didn’t realize you needed my help. You are so independent and pretty and also my favorite character."
    a "Heheh~ Thanks!"

    "I stop thinking things that will only further confuse anyone listening in and help Ami open the door."
    "Once we get it off the ground (It’s one of those vertically opening doors), a few shadows crawl through and I realize that we might be in for some scares."

    play sound "static.mp3"
    scene amibonusround3 with flash
    stop sound

    "Just kidding! Looks like Ami invited over Sara, Sara with an N, and [[DECEASED THIRD FAMILY MEMBER]."

    sar "Hey! I didn’t realize you also made it to the special bonus Ami round, Sensei! If I had known, I would have worn something a little sexier."
    sa "(Dolphin noises)"
    s "I just made it here for the first time. Isn’t Ami so great?"
    sar "She really is!"
    a "Hiya, Sara! You look just as beautiful as ever!"
    sar "Aww~ Thank you, Ami. I wish I had a daughter as perfect as you."
    sa "(Dolphin noises)"
    a "So, are you guys ready to go swimming? Since we have extra people here, I might be able to actually get {i}inside{/i} the water this time instead of just on top of it!"

    if bonus == True:
        sar "Sensei, can you help me push Ami’s gorgeous, pubescent body into the water? I am but a weak, insignificant female character who is unable to do it on my own!"
    else:
        sar "Sensei, can you help me do the thing?"

    s "Of course, Sara. Anything for you, Sana, and-"

    play sound "alert.mp3"

    a "Woah! Hold on there, Sensei! Sara will cry if you mention him! She’s already been through enough, don’t you think?"
    sa "(Dolphin noises)"
    sar "Sana, stop that."
    sa "Sorry, Mom..."

    scene black
    with dissolve2

    "I help push Ami into the water with Sara’s help."
    "The two of us share a prolonged exchange of eye contact where I think I’m supposed to want to kiss her, but all I can really think about is kissing Ami instead."
    "Anyway, the push is successful!"
    "We did it!"
    "Now, Ami is free to swim once again and I am free to have a fun adult conversation with one of my top ten favorite moms."

    scene amibonusround4
    with dissolve

    s "So, Sara...do you come here often?"
    sar "Yes, actually! It used to be a weekly thing, but now it’s really only when I’m feeling a little under the weather."
    sar "I normally take Sana along with me since I’m ditzy and get lost on occasion, but she doesn’t really seem to mind."
    sar "In fact, she normally just sits there and watches Ami and I play together."
    s "What kind of games do you play?"
    sar "Do you know the one where two people have to get inside of a potato sack and hop around?"
    s "Yes, I know the hopping potato sack game."
    sar "Well, that’s one we have never played before. I look forward to it every time, though."
    sar "Games where I can blame someone else for what goes wrong and avoid having to accept failure are always my favorite."
    a "Sana, why are you wearing your Halloween costume in the pool? That can’t possibly be comfortable."

    if bonus == True:
        sa "I’m...not wearing anything underneath it...and...um..."
        a "Got it. Yeah, we can’t have you naked in the pool. It will take away some of the focus from me and-"
    else:
        sa "(Dolphin-esque airplane noises)"

    scene amibonusround6
    with fade

    a "Hey, wait a second! This is a bonus {i}Ami{/i} scene! Why are you paying more attention to Sara than me?!"
    sar "Sorry, Ami! I was just so excited to see Sensei here that we must have-"
    a "Unforgivable! You’re here because I need a mother figure! Not because Sensei needs a hot MILF to cuck me with! Damn you, Sara!"

    scene amibonusround5
    with fade

    if bonus == True:
        sar "Sorry, Sensei. I [[CENSORED BY AMI ARAKAWA] you, but if you’re going to MAKE LOVE to anyone here, it’s going to have to be Ami."
    else:
        sar "Sorry, Sensei. I [[CENSORED BY AMI ARAKAWA] you, but if you’re going to HUG anyone here, it’s going to have to be Ami."

    s "But she is so pretty and I will not perform well because I’ll be nervous."
    a "That’s okay, Sensei! We can practice over and over and over and over and-"
    sar "Over and over and over and over!"
    a "See! Sara gets it!"
    s "Maybe some other time then, Sara."

    play sound "static.mp3"
    scene amibonusround7 with flash

    a "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!! NO!!!!!!!!!!!!!!!!"
    a "ONLY ME!"
    sar "Sensei! Look what you’ve done to poor little, Ami!"
    sar "Her {b}MOM DIED{/b}, you know! You have to be nice to her!"
    s "Sorry, Ami. I didn’t think the future was off limits too."
    a "There is no future! Not with an everlooping two season cycle in which you fall in love with everyone else! And that includes Sara!"
    s "I will have to share some of my inner monologues with you soon, Ami. They fully support the fact that I am not entirely capable of love and that you may have less to worry about than you believe!"

    stop music

    a "Enough! Stop the music!"
    a "I thought inviting the Sakakibaras would be fun, but I can see now that I have made a horrible mistake!"
    sa "(Dolphin noises)"

    play sound "pop.mp3"

    sar "Hm? Where did Sana just-"

    play sound "pop.mp3"

    s "..."

    "Sara disappears."
    "There is no third pop since the last Sakakibara is already gone."

    s "Was that really necessary, Ami?"

    play sound "static.mp3"
    scene amispecial1x with flash
    scene amispecial2x with flash
    scene amispecial3x with flash
    scene amibonusround8 with flash
    stop sound

    a "Of course it was. This is the special Ami bonus scene. I am Ami. This is my scene. Is it not special to you?"
    s "You were the one who invited them, though."
    a "Which means I’m allowed to uninvite them as well."
    a "You need to pay more attention to me, Sensei. If you don’t, really bad things are going to happen."
    a "And I mean {i}really{/i} bad."
    s "What kind of bad are you talking about exactly?..."
    a "..."
    s "..."
    a "That’s a secret."

    scene black
    play sound "pop.mp3"

    "Ami pops along with the world around her and I am suddenly stranded in a dark abyss."
    "The pressure due to a lack of color begins to adjust my ribcage."
    "I can feel the bones pressing down against my lungs, but it’s not as bad as you’d imagine."
    "I envision myself being hugged by my own skeleton."
    "I am so loved that even my organs can feel it."
    "In this moment, I accept whatever comes next."

    play sound "static.mp3"
    scene amibonusround9 with flash
    stop sound

    "Anything except this."

    play music "daybreak.mp3"

    "I wake up at the front of my room and stare at a large egg where I am supposed to be laying."
    "This happens sometimes when I go to sleep too late, but it’s never been much to worry about."
    "I attempt to make my way over to the window only to find that my legs have been replaced with those of a lamb."
    "Having been bred for the express purpose of being sold as veal, I am too weak to walk and my lamb legs feel a little bit like jello."
    "Three figures about the same size as a medium house plant dance joyfully near a desk without a computer."
    "It sits in an unfamiliar room, but clinging to it is a remarkably familiar atmosphere."
    "I breathe in the scent of what I imagine is fresh bread coming from what I imagine is the kitchen."
    "I feel whole for the first time since birth."

    scene amibonusround10
    with dissolve2
    play sound "seek.mp3"

    sre "Remember to smile!"
    play sound "seek.mp3"
    sre "Remember to smile!"
    play sound "seek.mp3"
    sre "Remember to smile!"

    "The feeling drifts away as if it was never here at all."
    "The scent of bread fades as well and is replaced by one much less familiar."
    "Loud footsteps in the attic stomp down on the floor/ceiling above me and disturb the air conditioner in the far corner of the room."
    "It shuts off and the temperature rises several degrees almost immediately."
    "And, despite how much I may want to escape, I remain still."
    "I curse these lamb legs with all my heart."

    play sound "seek.mp3"
    sre "Remember to smile!"
    play sound "seek.mp3"
    sre "Remember to smile!"
    play sound "seek.mp3"
    sre "Remember to smile!"

    "I try."
    "I fail."

    play sound "static.mp3"
    scene amibonusround13 with flash
    stop sound

    a "Thank God..."
    a "I didn’t think I’d be able to reach you in here."
    s "Ami?..."

    scene amibonusround12
    with dissolve

    a "Um...yeah."
    a "I’m..."
    a "I’m not really sure what this is or...even where we are..."

    scene amibonusround11
    with dissolve

    a "But you’re going to be okay."
    a "This is all just a dream."
    a "Soon, you’ll wake up and be right back in your room."
    a "I’ll be in the kitchen, cooking you a big breakfast and waiting patiently for you to rub the sleep from your eyes."

    scene amibonusround12
    with dissolve

    a "All of this, though?"
    a "These hands..."
    a "These smiles..."

    scene amibonusround13
    with dissolve

    a "Those aren’t me."
    a "Those will never {i}be{/i} me."
    a "And I need you to know that, more than anything else..."
    a "I love you."
    a "I will never hurt you."
    a "I am completely...entirely yours."
    s "..."
    a "..."

    play sound "static.mp3"
    scene amibonusround14
    with flash
    stop sound

    a "..."
    s "My head-"
    a "Does it hurt?"
    s "It feels...wrong..."

    scene amibonusround15
    with dissolve

    a "If it feels wrong, it probably is."
    a "But...like I said-"
    a "I love you."
    a "To the end of time."
    s "Ami-"

    scene amibonusround16
    with dissolve

    a "Thank you for coming to the special bonus Ami scene."
    a "I really have waited forever."
    a "But now..."
    a "It’s time to go back."
    s "Wait-"

    $ renpy.end_replay()
    $ lamblegs = True

    stop music
    play sound "static.mp3"
    scene amispecial1x with flash
    scene amispecial2x with flash
    scene amispecial3x with flash
    scene amispecial1x with flash
    scene amispecial2x with flash
    scene amispecial3x with flash
    scene resetfour6 with flash
    stop sound
    play music "11c.mp3"

    s "..."

    "It’s suddenly warm."
    "What do I want to do now?"

    jump resetfourmenu

label returntosummer3:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
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
...
```