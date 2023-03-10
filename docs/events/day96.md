# Recall (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 96

* Day of week is Monday

* Event [You and Me](./shrine15.md) (Maya) is completed)

* Event [Imprinting](./ayanenew1.md) (Ayane) is completed)



## Next events

* [Main: Rewrite](./day102.md)

## Event properties

* Id: day96
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day96

## Official wiki page

[Recall](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day96&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day96:
    scene newrecall1
    with dissolve2
    play music "justbehappy.mp3"

    a "We’re finally free! I felt like today was dragging on forever."
    a "I was {i}this{/i} close to faking a stomach ache so I could go home, Sensei. You better be proud of me for toughing it out."
    s "Ami, if you ever want to leave, you can just tell me. I literally do not care at all."

    scene newrecall2
    with dissolve

    a "Well, you should! Like you always used to say, a mind is a terrible thing to waste."

    scene newrecall3
    with dissolve

    a "Hey, come to think of it...you never really say anything encouraging like that anymore. How come?"
    a "Have I already peaked as a student in your eyes? Is it all downhill from here?"
    m "Maybe it's just the fact that he's changed and is an entirely different person now? That sounds reasonable, doesn't it?"
    s "..."

    scene newrecall4
    with dissolve

    a "Oh, hi Maya. Thanks for joining in. You've been so quiet since the last bell rang that I forgot you were even there."
    m "I apologize for not making my presence more apparent. I’ve been a little distracted all day."

    scene newrecall5
    with dissolve

    m "And it certainly doesn’t help that {i}he’s{/i} with us for some reason."
    s "Hey, I’ve been respectful and haven’t spoken to you at all. The least you can do is refrain from insulting me for a little bit."
    m "Why? Are the feelings you pretend to have hurt in some way? Would you like me to apply a make-believe bandage to them?"
    m "Here. Let me reach into my make-believe purse and get one for you."
    s "..."

    "Maya seems abnormally...agitated today- which is surprising given that she’s normally pretty agitated to begin with."
    "The thing is I {i}really{/i} haven't done anything this time, though. At least not to my knowledge. So this is just completely bizarre to me."

    scene newrecall6
    with dissolve

    a "So, uhh...ignoring how cranky you are, is it okay if we stop at the convenience store on the way home?"
    a "It’s been crazy hot lately and I think I might die if I don’t have a drink in the next few minutes."
    m "Feel free. I actually have somewhere else I need to be anyway, so I'll be heading back on my own now."

    scene newrecall7
    with dissolve

    a "Wait, what? I thought we were studying together tonight."
    m "Something came up and I’m not going to be able to make it."
    a "What came up? Is everything okay?"
    a "Is {i}that{/i} why you've been in such a bad mood?"
    a "We’re best friends, so you can always tell me if something is on your-"
    m "I’ll see you later."
    m "Goodbye, Ami."

    scene newrecall8
    with dissolve

    "Maya takes off down the road (The road {i}opposite{/i} from the one that leads to the dorms, mind you) and vanishes from our sight, leaving the two of us equally confused."
    "I can tell that Ami is worried, but I chalk this sudden disappearance up to just another one of Maya's mood swings. I highly doubt it's anything substantial."

    a "The heck is with her today? That was totally rude."
    s "It's probably just that time of the month or something."

    scene newrecall9
    with dissolve

    a "Sensei, ew! Don't you know it's impolite to say things like that?"
    s "Sorry. I’ve just stopped expecting Maya to ever behave predictably, so I'm not too surprised by her sudden, as you put it, {i}crankiness.{/i}"
    a "Well...I guess she {i}does{/i} randomly start acting different sometimes. Like all those random speeches about the universe and stuff."
    s "You get to hear those too? I thought I was a special case."
    a "Not so much anymore. She stopped saying that kind of stuff to me when I told her I didn’t really care about or understand any of it."
    a "I used to get it all the time, though."

    scene newrecall10
    with dissolve

    a "But anyway! Is it okay with {i}you{/i} if we stop at the store on the way home?"
    a "If I take like ten more steps into this hateful summer heat without a drink I am going to melt."
    s "The store is more than ten steps away, so the chances of you melting on the way there seem pretty high."
    a "Not if you give me a piggyback ride!"
    s "Sure. Hop on."

    scene newrecall11
    with dissolve

    a "Wait...really?"
    a "Because I was kind of just kidding. I’m fine walking on my own for a little while longer."
    s "You sure? Because I really don't mind."
    a "You mean you...won't feel embarrassed or anything?"
    s "Embarrassed? Not really. I'll probably feel like an idiot, but I've also noticed how flushed you've been since we stepped outside."
    s "So if having you on my back is all it takes for you to {i}not{/i} die, that's fine by me."
    s "Besides, it’s only a couple blocks away. If it was any longer, I doubt I'd have the stamina or the willpower to continue."
    a "Well...thanks, [amimaster]. I-"

    scene newrecall12
    with hpunch

    a "Hey! Wait a second! What do you mean {i}stamina or willpower?!{/i} Are you calling me fat?!"
    s "Just get on my back, Ami."
    a "Fine! But if you complain even once about me being heavy, I’m pulling your hair out!"

    scene black
    with dissolve2

    "Ami hops onto my back and throws her arms around my neck."
    "Of course, she isn’t heavy at all. It's like carrying a large backpack if the backpack cooked you dinner and occasionally said mildly suggestive things about your relationship."
    "We get some strange looks from people as we make our way down the street, but neither of us seem to really care."
    "In fact, Ami seems quite happy about not having to walk anymore."
    "Her fingers grab hold of the collar of my shirt and cause my tie to get messed up, but she takes a moment to playfully tuck it back in as we round the corner and wind up in front of the shop..."
    "………"
    "……"
    "…"

    scene amicon1
    with dissolve2

    a "Thanks for the ride, [amimaster]! And thanks for buying me a drink as well!"
    s "Well it’s not like you had any money, so..."

    scene amicon2
    with dissolve

    a "Heheh...silly me, forgetting my wallet and asking you to pay for me. Good thing I have the best [uncle] in the whole wide world."

    if bonus == True:
        s "Yeah, yeah. Flattery won’t get you anywhere."
    else:
        s "You are supposed to be protecting my money, not destroying it."

    if amifingered == True:
        scene amicon3
        with dissolve

        if bonus == True:
            a "Really? Cause I could have sworn that all of that ‘flattery’ was one of the things helping get you into my dorm room at night."
            s "You really want to talk about our relationship in front of a convenience store in the middle of the day?"
            a "What's wrong? No one here knows we’re related."
            s "I think you might also be forgetting the issue with our age gap as well."
        else:
            a "The only thing I'm going to destroy is your pillow during our upcoming pillow fight championship."
            s "For the last time, stop using my pillow for contests. Use your own."

        scene amicon2
        with dissolve

        a "Pfft...whatever. I'll save the flirting for until we're home."

    else:
        scene amicon3
        with dissolve

        if bonus == True:
            a "Awww, why not? I was hoping I’d {i}at least{/i} get a raise on my allowance or something."
            s "You don’t even get an allowance, Ami."
        else:
            a "Awww, why not? I was hoping I’d {i}at least{/i} get a raise on my salary or something."
            s "Do you even get a salary? Because I don't really ever remember directly paying you."

        scene amicon2
        with dissolve

        if bonus == True:
            a "Well I {i}did{/i} until you decided you just weren't going to give me one anymore."
            s "I put a roof over your head. Isn't that enough?"
        else:
            a "I have access to all of your accounts, so I just pay myself whenever I want."
            s "That seems like a complete breach of privacy."

        a "Not really, but I guess it's not up to me to decide what you do with your money."

    scene amicon4
    with dissolve

    a "Oh! So, I had a question about this test thingy I totally forgot to ask you."
    s "This again? I thought we were finally done talking about that."
    a "Nononono, this one isn’t about studying or anything like that. I was just wondering what you planned on doing {i}after{/i} the tests."
    s "What do you mean?"
    a "I mean that as soon as those are over, we start the last semester of the[school] year."
    a "Which means that a few months later, summer vacation starts."

    scene amicon5
    with dissolve

    a "Which means that..."
    a "You won’t be my teacher for much longer..."

    "Is the end of the year really that close?"
    "I remember talking about it with Sana recently, but...I didn’t think it would get here {i}this{/i} quickly."
    "Maybe I {i}should{/i} talk to one of the staff members and see about carrying my class over into the next year?"
    "It would be a shame having to start all over after coming so far with so many of them."

    s "Don’t worry just yet, Ami. There’s still...some semblance of hope that I’ll be able to teach you again next year."

    scene amicon4
    with dissolve

    a "Huh? What do you mean?"
    s "I mean that I can try to talk to someone about just...keeping the same class?"
    s "I don’t know. I haven’t figured it out yet."

    scene amicon5
    with dissolve

    a "That somehow makes me feel even {i}less{/i} confident about you teaching me again..."
    a "You at least need a {i}plan,{/i} Sensei..."

    scene amicon4
    with dissolve

    a "Oh! What if you, like...go up to the principal and start crying or something?"
    a "Remember how I always used to cry when you wouldn’t buy me anything from the convenience store?"
    s "You mean like what happened two minutes ago?..."

    scene amicon6
    with dissolve

    a "Ahh...I remember it like it was yesterday."
    s "Again, it was two minutes ago."

    scene amicon1
    with dissolve

    a "Maybe if you try that with the principal, he’ll let you teach us all again!"
    s "I can’t imagine that working, to be honest. There comes a time in your life where crying just doesn’t always get you what you want anymore."

    scene amicon2
    with dissolve

    a "Really? Cause I’m getting older and it’s clearly still working for me."
    s "Yeah, well you’re cute. The world works differently for cute girls."
    s "You can pretty much cry your entire way through life and everything will work out."

    scene amicon7
    with dissolve

    a "Ah! Am I...experiencing sexism for the first time? Is that what this is?"
    a "Is this a taste of the world yet to come?"
    a "I don’t like this at all, Sensei! I feel strange! Please, hold me and make me feel better!"
    s "I’m not going to hold you with all of these people around."

    scene amicon8
    with dissolve

    a "That’s no fair! You already gave me a piggyback ride! How is a little hug any different?!"
    s "It just is, okay? Besides, you’re not even upset right now."
    a "How do you know that?!"
    s "Because you never get angry-eyebrows when you’re upset. You always go into puppydog-mode."
    a "Puppies can get angry!"
    s "So you’re a literal puppy now?"
    a "Yes! Woof~!"
    s "…"
    a "…"

    scene amicon5
    with dissolve

    a "Can you at least hold my hand?"
    s "..."
    a "..."

    if bonus == True:
        s "Ugh, fine."

        scene amicon6
        with dissolve

        a "Yay!"
        s "When we get home."

        scene amicon9
        with dissolve

        a "GAAAAAAAHHHHHHHHH!"
        s "Wow. You must really like holding hands."

        scene amicon8
        with dissolve

        a "No! I really like {i}you{/i}! Get the hint already!"

        if amifingered == True:
            "Of course I have obviously {i}gotten the hint{/i}. It's kind of hard not to after bringing your niece to orgasm. "
            "But there’s a time and a place for everything. And I don’t think the two of us are at the point where we should be expressing those feelings in public just yet..."
            "And honestly, I doubt a time where that will be acceptable will ever come."
        else:
            "Of course I know how Ami feels about me...but I’m supposed to be her [uncle] now."
            "It just wouldn't be right to use that position to take advantage of her. And it {i}especially{/i} would not be right in public."
    else:
        s "Absolutely not. Act more professional while we're out in public."
        a "But if you don't hold it, it will float away!"

    s "Can we just get back to the topic at hand?"

    if bonus == False:
        a "The topic {i}is{/i} my hand! And how it longs to be held!"

    s "You asked me what my plans were after the next batch of tests were over, but what about yours?"

    scene amicon4
    with dissolve

    a "Mine? What do you mean?"
    s "Well...how are you going to spend your last couple months in[school]?"

    scene amicon1
    with dissolve

    a "Umm...The same way I have been, I guess?"
    a "I’ve been trying not to think about it, to be honest."
    a "I already have a problem with getting attached to stuff, so if I dwell on this[school] year ending, I’ll just wind up feeling even worse once it’s actually over."

    scene amicon10
    with dissolve

    a "We’re so close to the end at this point and...there isn’t really anything we can do about it."
    a "I’ve accepted that."
    a "It might sound kinda sad, but...that’s just life, isn’t it?"

    scene amicon11
    with dissolve

    if bonus == True:
        a "You always told me when I was little that time won’t ever wait for us."
        a "And that even if I sit down and wish as hard as I can, over and over...there’s no guarantee that any of those wishes will ever come true."
    else:
        a "You told me after you first hired me that aneurysms can strike at any moment, which makes living inherently terrifying because we can just randomly die in the middle of the night one day."

    a "So...ever since then, I’ve just taken things day by day. And it’s worked out so far!"
    a "I mean, the two of us are closer than ever. That’s gotta be a plus, right?"
    s "Right..."

    scene amicon12
    with dissolve

    a "Um...sorry for getting sappy out of nowhere like that. I think this coffee’s got espresso in it or something because my brain’s moving at like, twice the speed it normally does."
    a "Would you mind giving me another piggyback ride on the way home by any chance? If I can't keep up with my own thoughts, I doubt I'll be able to keep up with...my legs. Or something."
    s "What?"
    a "I think...walking might be kinda bad for my over-caffeinated [teenage]heart right now."
    s "That's an excuse if I've ever heard one. You're walking and that's that. Your piggyback quota for the day has already been exceeded, unfortunately."

    scene amicon5
    with dissolve

    a "Hah...I had a feeling you were going to say something like that..."

    scene black
    with dissolve2

    "Ami and I begin the short voyage to the bus station, this time walking several feet apart from one another."
    "She talks more about potential plans for getting me to be her teacher again, but none of them seem all that feasible."
    "I’ll just have to figure something else out."
    "..."
    "I really don't want to start all over."

    $ renpy.end_replay()
    $ ami_love += 1
    $ day96 = True
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label day102:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
$ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
    if totaldays >= 86 and futaba_lust >= 5 and day == 5 and day86 == False:
        jump day86
    if totaldays >= 89 and day65 == True and day89 == False:
        jump day89
    if totaldays >= 91 and day63 == True and day65 == True and day91 == False:
        jump day91
    if totaldays >= 96 and day == 1 and shrine15 == True and ayanenew1 == True and day96 == False:
        jump day96
...
```