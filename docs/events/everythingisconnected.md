# Everything is Connected (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* connecttrack equal to False (unknown variable)

* Event [Nightvision](./soccer10.md) (Miku) is completed)



## Next events

None

## Event properties

* Id: everythingisconnected
* Group: Happy scenes
* Triggered by label: happyloop1

## Official wiki page

[Everything is Connected](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=everythingisconnected&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label everythingisconnected:
    scene neweverything1
    with pixellate
    play music "backwardsdancing.mp3"

    "I show up at the soccer field and everything is normal."
    "I begin to scan the area for Miku and find nothing but discarded wigs likely worn by women somewhere in their mid 60’s."
    "What a strange thing to find at a soccer field."
    "{s}When I was younger, I convinced myself that I’d be able to be an astronaut if I worked very hard.{/s}"
    "{s}This wasn’t true.{/s}"
    "{s}In my rage, I took to doing horrible things as a hobby instead.{/s}"
    "{s}Things you would struggle to believe even if you were able to see them with your own eyes.{/s}"
    "And so now, many years later, I know what the inside of a human body smells like."
    "If you close your eyes, you could even mistake it for {b}HEAVEN.{/b}"

    s "si enoyreve erehw rednow I"
    s "…"
    s "haoW"
    s "sdrawkcab tuo gnimoc si gnihtyrevE"

    "Welp, looks like normal talking is off the table. "

    s "..."

    "I guess I’ll just walk around the field and pick up these wigs to kill some time!"

    scene black
    with dissolve2

    "..."
    "......"
    "........."

    scene neweverything2
    with dissolve2

    "One by one, I pile the clumped and organized bundles of hair into my arms."
    "I scan the insides of them in search of scalp-remnants to sniff but find nothing."
    "These must be hand-made."
    "Sometimes, wigs made in factories still contain small bits of skin from the scalps of which they were stolen from. "
    "I bet this is something you didn’t know."
    "There are many things you don’t know that I do."
    "I am very, very smart."
    "I know everything."
    "Unfortunately, that wig fact wasn’t true. "
    "Though, it wouldn’t surprise me if large corporations started killing and skinning the poor to help create wigs."
    "People will do anything for money nowadays."

    s "I am having so much fun collecting wigs on the soccer field!"

    "Before I know it, my arms are full."
    "Why am I picking these up again? "
    "This is too much trouble."

    s "I am no longer having any fun collecting wigs on the soccer field!"

    play sound "thump.mp3"
    with hpunch

    "I drop the wigs on the ground and they make a strange noise."
    "Turns out, they weren’t wigs at all."
    "They were heads."
    "LOL!"

    s "I must have missed that during my scalp check."

    scene neweverything3
    with fade

    "Upon making contact with the ground, the disembodied heads regrow their necks. But they aren't normal necks."
    "They are more like stubby flower stems, sinking themselves into the ground and sucking up nutrients in an attempt to bring them back to life."
    "I have no idea if it is going to work or not, but I am not about to wait around and find out."
    "It's not every day that I get to use the head of a deceased teenager growing out of a fleshy flower stem as a sex toy."
    "I just have to hope that I'm able to get my business over and done with before they come back to life (Assuming they can)."
    "It looks like today's fellatio menu includes the following options: Kirin, Miku, and Karin."

    if bonus == True:
        "Which one do I want to engage in sexual activities with?"
    else:
        "Which one do I want to {b}HUG{/b}?"

label chooseahead:
    menu:
        "Miku":
            jump correcthead
        "K5r1n":
            "Please select Miku’s head for the sake of this experiment."
            jump chooseahead
        "m":
            "Please select Miku’s head for the sake of this experiment."
            jump chooseahead
        "Nothing is real":
            "Please select Miku’s head for the sake of this experiment."
            jump chooseahead
        "Kirin":
            "Please select Miku’s head for the sake of this experiment."
            jump chooseahead

label correcthead:
    "I have selected Miku’s head for the sake of this experiment."

    scene black
    with dissolve2

    "My fingers graze her soft cheeks."
    "They’re cold, but not incredibly cold. Probably like a 6.5/10 on the coldness scale."
    "It implies that either she has not been dead for very long or is currently in the process of coming back to life (I still have no idea)."
    "I wonder who it was that did such a horrible thing to her?"
    "Why would someone remove Miku's head when all she does is run around and smile and look vaguely like a boy, but the kind of boy you could have sex with and not be called gay for?"
    "Why do bad things always happen to good people?"

    if bonus == True:
        "Oh well."
        "I guess it is game time."
    else:
        s "{b}here comes the huggy boy{/b}"
        "I announce my arrival to the head when I am suddenly stricken with a harsh realization."

    scene neweverything4
    with dissolve2

    "It is a little hard to get my penis into her mouth because of the early-ish onset of rigormortis taking over her jaw."
    "However, once I do, the pressure from it attempting to close once again is actually rather enjoyable and very snug."
    "It appears that her teeth have been removed as well, so the dismemberment of my penis at this point in time is pretty unlikely."
    "The sensation of her 6.5/10 cold level gums grinding against my willy make me want to jump for joy, but I can not jump right now as it might pull her stem/neck from the ground."
    "Did you know that the act of removing dead petals from a flower is called deadheading?"
    "Did you know that the act of getting head from a dead girl who is also a flower is {i}not{/i} called deadheading? It is called necroanthophilia."
    "I am such a good teacher."
    "It is no wonder Miku so readily accepted my weiner."

    s "Enjoy the weiner, damn it."
    mi "(Currently deceased and incapable of responding, but there's a soft, mushy noise coming from her mouth that sounds kind of like fmp, fmp, fmp.)"

    "The two other flowers begin to rotate in circles like they are performing a ritual of sorts, but I am too absorbed in the pleasure of a tomboy's mouth to take part in it."
    "I wonder if my cum will help her grow faster."

    s "Are you ready for the semen?"
    mi "(Fmp, fmp, fmp.)"

    "I really start going to town on her mouth and can feel myself pressing up against the other side of her head."
    "But, it is at that moment that I realize this isn't Miku's head at all!"

    scene neweverything5
    with hpunch
    play sound "pop.mp3"

    "This is a watermelon!"
    "LOL!!!"

    s "Get ready for the semen!"

    "I have sex with the watermelon and it feels good."

    scene neweverything6
    with fade

    watermelon "Fmp, fmp, fmp."
    s "Hah...hah...hah..."
    s "Get ready for the semen..."
    watermelon "Fmp, fmp, fmp."
    m "Uhh..."

    play sound "static.mp3"
    scene neweverything7 with flash
    stop sound

    s "Oh. Hi, Maya."

    "I drop the watermelon because I am surprised and it lands on my shoes and cracks."

    s "I wasn't doing anything."
    m "…"

    if bonus == True:
        "Maya stays silent for a long period of time- probably because she is jealous of my intimate connection with her favorite food."
    else:
        "Maya stays silent for a long period of time. She’s probably just angry that I’m about to HUG her favorite food."

    m "That..."
    m "Uh..."
    m "You know, I was really starting to think I've already seen everything."
    m "And I...very clearly have not."
    m "This is definitely not how this normally goes."
    s "?og yllamron ti seod woH"

    "I’m backwards again."

    m "That’s something I can’t tell you just yet."
    m "You’re starting to disconnect."
    s "どういう意味?"
    m "Nothing I say will register in your memory."
    m "This {i}dream{/i} will be wiped away just like all of the others."
    s "どういう意味?"

    scene neweverything8
    with dissolve

    if bonus == True:
        "Maya looks away from me for a moment, probably because she is a fucking bitch who is taking too long to sleep with me."
        "Even though she gave me a handjob in one of my dreams once."
        "But that doesn’t count. Handjobs aren’t sex."
        "I want to deflower her in front of the {b}GOD{/b} she claims to hate."
        "I want to fuck {b}GOD's{/b} child while he watches and strokes himself, just like that one time Mary Magdalene rode his favorite son's dick reverse cowgirl style and came three times."
        "I wonder if Jesus's weiner was as big and awesome as mine."
        "Probably not."
    else:
        "Maya looks away from me for a moment, probably because she is a fucking bitch who is taking too long to HUG me."
        "The ending leg of a prayer jumps into my head, but only one line of it."

    m "We should...probably move on to the next part of the dream now."
    m "If we stay here any longer, I’m not sure you’ll make it back."
    s "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"

    "I cry out compulsively and my tongue begins to tangle around itself."

    s "Take me to your dream world. I want to speak to the manager."

    scene neweverything9
    with dissolve

    m "I’m the manager. Any questions you have can be directed to me."
    s "Okay. Then why are you so fucking {i}lame{/i}?"
    m "That was a joke. I’m not actually the manager. And I'm not {i}lame{/i} either."
    m "Is there really a need to insult me when I haven’t said a single harmful thing to you today?"
    m "For all you know, I could be genuinely worried about you right now."
    s "You’re genuinely {i}lame{/i}, that’s what you are."

    scene neweverything10
    with dissolve

    m "Right..."
    m "Anyway, please follow me."

    scene black
    with dissolve2

    "Maya begins to walk toward a tiny building on the far end of the soccer field that I have never seen before."
    "........."
    "......"
    "..."

    scene neweverything11
    with dissolve2

    m "Okay. We’re here."
    m "Please step inside."
    s "Step inside of {i}that{/i} thing? There is absolutely no way I will fit in there."
    m "What if I told you the inside was filled with boobies?"
    s "Step aside, melon girl."
    s "If there is anything I am good at, it is making myself fit inside of places no one would ever expect me to fit inside of."
    m "You are absolutely disgusting."
    s "Are you not coming into the boobie house with me?"
    m "I’m not."
    m "This is a place for you and you only."
    m "It will help get you back on track."

    "I point behind me."

    s "{i}But the track is right there.{/i}"
    m "Clever."
    m "Please step inside now. Dealing with you in this state is rather exhausting."
    s "FINE!"

    if bonus == True:
        s "But they better be good boobies and not the bad kind..."

    scene black
    with dissolve2

    "I step inside of the storage room and am suddenly hit by a wave of warmth."
    "It’s the feeling of sunlight."
    "Why can I only feel light when it is filtered through glass?"
    "Why can’t I feel anything directly?"
    "Why can’t I feel?"

    scene connect
    with dissolve2

    "Everything is connected."
    "That is something Maya taught me recently."
    "But if everything is connected-"
    "Why do I feel so detached?"
    "{i}Developer note: At this point in the game, all of your actions will be recorded via webcam and sent somewhere special.{/i}"
    "{i}Please click accept on the following screen to enable this feature.{/i}"

    scene connect2

    menu:
        "I accept":
            scene connect
            "{i}Thank you for accepting.{/i}"

    "{i}Please note: The following scene is a simulation that will test your aptitude at holding a conversation with a [[FEMALE HUMAN BEING].{/i}"
    "{i}You will not be graded at the end of this simulation.{/i}"
    "{i}It is only a test to see whether or not you are capable of performing such a task.{/i}"

    stop music

    "////STOP MUSIC"
    "{i}Please close your eyes if you are easily scared, disturbed, or prone to seizures as a series of flashing images will be displayed on the screen.{/i}"
    "{i}If you elect to close your eyes, you may open them again once the music starts.{/i}"
    "{i}The images will play on your {b}next mouse click{/b} and the simulation will begin. Thank you for playing Lessons in Love, an adult dating simulation game.{/i}"

    play music "static.mp3"
    scene ayhh1
    with flash
    scene ayhh2
    with flash
    scene ayhh3
    with flash
    scene ayhh4
    with flash
    scene ayhh5
    with flash
    scene ayhh6
    with flash
    scene ayhh7
    with flash
    scene ayhh8
    with flash
    scene ayhh9
    with flash
    scene ayhh10
    with flash
    scene ayhh11
    with flash
    scene ayhh12
    with flash
    scene ayhh13
    with flash
    scene ayhh14
    with flash
    scene ayhh15
    with flash
    scene ayhh16
    with flash
    scene club_day
    with flash
    stop music
    play music "daybreak.mp3"

    s "…"

    "I..."
    "Where am I?"
    "This isn’t the[school]’s storage room."
    "It’s a room I’ve never seen before."
    "The sweet scent of candy lingers in the air."
    "I feel oddly comfortable here."
    "I can’t even remember what I was doing before I opened my eyes."
    "…"
    "It’s warm."
    "Part of me wants to lie down and let the sun bleach my skin and wash
    away the uneasiness I’ve been feeling as of late."
    "Teaching is hard work, you know?"
    "In fact, just the other day, I was thinking-"

    play sound "slidedoor.mp3"

    q "Yuu, are you in-"

    show sakisurprised
    with dissolve2

    "A girl appears in front of me."
    "She has one less dimension than the girls I usually deal with."
    "I’m not sure how to handle this."

    mg "Um..."
    s "…"
    mg "Who...are you?"
    mg "Are you a new teacher here? Your uniform doesn't match our colors."
    s "I don’t think so. I just kind of woke up here."
    s "Can you tell me where we are? Or maybe how I can get back to Kumon-mi?"

    show sakicurious
    hide sakisurprised

    mg "Kumon-mi? That’s a strange name."
    mg "Is that the[school] you taught at before transferring here?"
    s "No...Well, kind of?"
    s "I’m not really sure if I know the name of the[school], now that I think about it..."
    mg "You don’t know the name of your own[school]?"
    s "That probably sounds a little hard to believe, huh?"

    show sakinormal
    hide sakicurious

    mg "Hehe~ Maybe a little..."
    mg "Hey, you didn't...by any chance see a boy around my age in here, did you?"
    s "Uhh, no. I only woke up a minute or two before you opened the door."
    s "Is he your boyfriend or something like that?"

    show sakiembarrassed
    hide sakinormal

    mg "W-What? No! Nothing like that. He’s...just a friend."
    s "Don’t give me that. Your true feelings are written all over your face."
    mg "They are not!"
    s "They definitely are..."

    "The girl pauses for a moment before sighing to herself and spilling her 'secret' to a perfect stranger."

    show sakinormal
    hide sakiembarrassed

    mg "Okay...So, he’s not my boyfriend..."
    mg "But he’s someone I like very much."
    mg "We’ve known each other for a long time now, and he can be kind of strange at times...but he has a good heart."
    s "I see."
    mg "How about you?"
    mg "Is there anyone you like?"
    s "That’s a strange question to be asking a teacher, don’t you think?"
    mg "Hmm...I don’t think so."
    mg "After all, you’re going to be going back home in a little while, aren’t you? To...Kumon-mi or whatever you called it?"
    s "That’s right..."
    s "I need to...get back..."

    "But how do I even get there?"
    "And what will happen once I do?"
    "I have this creeping feeling that things are going to get even more confusing after this."
    "But then again-"
    "This is probably just another dream."
    "Every time things get weird or scary-"
    "They always go away shortly after."
    "Sure, they might come rushing back in the next time I’m thrown into an uncomfortable situation, but..."
    "But that’s something I’ve learned to deal with."
    "And that’s something I feel like I’ll have to continue dealing with if I want to make the most of the new life I’ve been given."
    "And so-"
    "I’m sure I’ll find my way back."
    "I’m sure."

    mg "Umm...You doing okay, there?"
    s "Oh, sorry. Internal monologue."
    mg "Don’t worry, I’m used to it. That boy I was talking about gets those all the time."
    mg "Do you want to maybe use my phone to call someone or something?"
    s "I...don’t really remember anyone’s number, to be honest."
    mg "Ahh, another downside of modern technology."
    mg "We have no reason to remember anyone’s phone number anymore now that we can just dial by name."
    s "You’ve got that right, um..."
    saki "Saki."
    s "You’ve got that right, Saki."
    s "I should probably get going now. Thanks for helping, though."
    saki "I don’t know if I really helped at all...but you’re welcome. Umm-"
    s "Just call me Sensei."
    saki "You’re welcome, Sensei."
    saki "Enjoy your trip back to Kumon-mi."
    s "Thanks. Enjoy your time with whatever that guy’s name is."
    saki "Hahah...I’m sure I will."
    saki "Thank you."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "…"
    "I open the door of the mysterious club room and make my way into uncharted territory."

    stop music
    scene bedroom_day
    $ connecttrack = True
    $ connect = False

    "And then I wake up again."

    $ renpy.end_replay()

    "What do I want to do today?"

    jump happyloop1

label day98:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label happyloop1:
    menu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Koi Cafe":
                    scene cafe_day
                    with fade
                    "I arrive at the cafe."
                    "No one is there."
                    "Time passes."
                    "Where should I go now?"
                    jump happyloop2
                "Library":
                    scene library
                    with fade
                    "I arrive at the library."
                    "No one is there."
                    "Time passes."
                    "Where should I go now?"
                    jump happyloop2
                "Soccer field":
                    if connecttrack == False and soccer10 == True:
                        jump everythingisconnected
...
```