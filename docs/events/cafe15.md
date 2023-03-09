# Window of the Waking Mind
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe15&go=Go)



## Event preconditions
✅Rin love greater than or equal to 15

✅Event "[Rin: Rin's Secret](./rindorm10.md)" is completed (event=rindorm10)

✅Event "[Rin: Boundaries](./rindorm15.md)" is completed (event=rindorm15)

✅Event "[Main: Drowning](./day30.md)" is completed (event=day30)



## Next events
* [Main: Missing](./day50.md)
* [Rin: Nothing Was Missing, Except Me](./cafe20.md)

## Event properties
* ID: cafe15
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe

## Event code
File: \game\RinEvents.rpy
Code:
```python
...
label cafe15:
    scene cafe_day
    with fade
    play music "cafe.mp3" fadein 3.0

    r "Next customer, please!"

    "..."

    scene cafe1
    with fade

    r "Oh hey, Sensei. What’s up?"
    s "Morning, Rin. Just stopping by to play my weekly game of coffee-roulette."

    scene cafe4
    with dissolve

    r "Well, you’re in luck because I’m actually about to clock out."
    s "Already? Are you getting your hours cut or something?"

    scene cafe6
    with dissolve

    r "Huh? No, it’s nothing like that."
    r "Haruka would never cut my hours. I’m too good at this stuff."
    r "So good that I have {i}two{/i} shifts, actually. I just need to clock out between them for a doctor's appointment."

    scene cafe4
    with dissolve

    r "But, hey! Drop by again later and you can get all the Rin you want!"
    s "A doctor’s appointment? Is something wrong?"

    scene cafe3
    with dissolve

    r "Oh, nah. It's no big deal. Just some...check-up sorta thing. You don’t need to worry about it."
    s "Well, I'm not going to try and get involved where I'm not welcome. Hope it goes well, though."

    scene cafe4
    with dissolve

    r "I'm sure it will!"
    r "So, what can I get for you today, sir?"
    s "I appreciate that you still ask even though we both know you aren’t going to listen."
    r "Just doing my job, Sensei!"

    "Are you really, though?..."

    scene black
    with dissolve

    "I choose a random drink off of the menu and prepare myself for whatever it is Rin will be making for me today."
    "Considering that her last drink wasn't as solid as the preceding ones, I'm thinking that this time-"

    r "Done!"

    scene cafemocharedux1
    with dissolve

    s "What? Already? But I haven't even sat down yet."
    r "Yup! Here ya go! One cafe mocha!"
    s "Like...a normal cafe mocha? With nothing weird about it?"
    s "Did you just have one left over from another customer or something?"
    r "Nope. Just the greatest barista in the world working extra hard to deliver quality beverages to her favorite teacher."
    s "..."
    r "...What?"
    s "Are you dying or something?"

    scene cafemocharedux2
    with dissolve

    r "What? Of course not. I told you it was just a check-up."
    s "Then why are you giving me a normal drink? Have I done something to offend you?"

    scene cafemocharedux3
    with dissolve

    r "No...it's not like that. I just wasn't really feeling creative today."
    r "But if you really want, I can go dump a bunch of stuff into a cup and see how that comes out instead. Just didn't wanna give you something I couldn't put my heart into, you know?"
    s "I don't think that's necessary. I'm just a little surprised to see you going through such a slump."

    scene cafemocharedux4
    with dissolve

    r "A...slump?"
    s "Maybe that's not the right word for it. You've just seemed a little out of sorts lately."
    r "Out of sorts?"
    s "Besides, I thought you loved making weird drinks and laughing silently to yourself as I test them before anyone else."

    scene cafemocharedux5
    with dissolve

    r "I do, though. Just not today, okay?"
    s "You know you can talk to me if-"
    r "Didn't I like, just tell you the other day that I was fine? You don’t have to worry about me, Sensei. Really."
    s "It’s not just me, though. Chika is worrying about you too."

    scene cafemocharedux6
    with dissolve

    r "Wait...what? Chika is...worrying about {i}me?{/i} Are you sure? What if she was talking about another Rin?"
    s "I really don't think she was."
    r "But why? Like, how does she even know something is wrong?"
    s "I thought nothing was wrong?"
    r "Yeah, that. That's what I meant to say. Why does she think that something is wrong?"
    s "Because you keep getting all weird around her."
    s "She's noticed that you haven't been acting like yourself and seems to think it might be her fault."
    r "She thinks...it's {i}her{/i} fault?"
    s "That’s not the case though, is it?"
    r "Of course that's not the case. It's just..."

    scene cafemocharedux7
    with dissolve

    r "Hah..."

    "I decide to let Rin stay quiet for a little while as she figures out the best way to talk about this."
    "When she remains quiet for an uncomfortable amount of time, though, I decide it might be best to provide a little positive reinforcement..."

    s "Take your time, Rin."
    s "I’m not going anywhere anytime soon. So if you-"

    scene cafemocharedux8
    stop music

    r "Sensei, do you ever have any thoughts that you wish you didn’t?"
    s "..."
    s "What do you mean exactly?..."
    r "You know. Like, stuff that pops into your head that you realize shouldn’t be there but, like..."
    r "You can’t really do anything about it."

    if roomwithtrack == True:
        scene newroom1
        with flash
        play sound "static.mp3"
        scene newroom9
        with flash
        scene newroom17
        with flash
        scene newroom8
        with flash
        scene cafemocharedux8
        stop sound

        s "I guess I do sometimes."

    else:
        play sound "static.mp3"
        scene whygodwhy
        with flash
        scene cafemocharedux8
        stop sound

        s "Maybe every now and then, sure."

    r "Okay."
    r "Good."
    r "Well, {i}not{/i} good. But I’m at least glad that I’m not the only one it happens to."
    s "Do you want to talk about what you’re-"
    r "Not really. But thanks."

    play music "cafe.mp3"
    scene cafemocharedux1

    r "You know what? Why don't we just talk about something else?"

    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy3
    with flash
    stop sound
    scene cafemocharedux9
    with flash

    r "{b}Like the inevitable collapse of our relationship when you start fucking the girl I habitually touch myself to.{/b}"
    r "{b}Or the ever present, looming darkness bubbling up inside of us. Expanding in size until it's brave enough to crawl through our throats.{/b}"
    r "{b}Frothing like the foam atop a cafe mocha.{/b}"
    r "{b}A window of the waking mind, thick with saliva and the remnants of days gone by.{/b}"
    r "{b}Why don't we talk about that?{/b}"
    r "{b}Or better yet-{/b}"

    scene cafemocharedux10
    stop music

    r "why dont we talk about nothing"

    play sound "alert.mp3"
    scene colorbars
    $ renpy.pause(4, hard=True)
    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy3
    with flash
    scene cafemocharedux11
    with flash
    stop sound
    play music "reversecafe.mp3"

    "//////////////////TERMINAL 23 IS EXPERIENCING A DISRUPTION IN SERVICE"
    "//////////////////A SUSPICIOUS AMOUNT OF FAILED LOGIN ATTEMPTS HAVE BEEN MADE"
    "{s}//////////////////PLEASE RENEW YOUR MEMBERSHIP IN ORDER TO{/s} NO"
    "GREETINGS, YOU ARE HIGHLY FAVORED"
    "GAZE AT THE MARTYR BEFORE YOU AND TELL ME WHAT YOU SEE"
    "IS THIS STRENGTH???"
    "OR IS THIS SOMETHING ELSE???"
    "THIS IS WHAT BECOMES OF THOSE WHO CAN NOT WALK ON THEIR OWN TWO FEET"
    "THIS IS WHAT BECOMES OF THOSE WHO LEAD INSTEAD OF FOLLOW"
    "THE WAY OUT IS LIT WITH THE LIGHT OF A THOUSAND SUMMERS"
    "HOW MANY OF THEM WILL YOU SEE???"
    "WHO WILL BE DRAGGED DOWN WITH YOU???"

    scene cafemocharedux12
    stop music

    "IF I TOLD YOU THE ANSWER, WOULD YOU EVEN BELIEVE ME???"
    "OR WOULD YOU RATHER THE DREAMS REMAIN???"
    "SHE HURTS WHILE SHE WAITS"
    "HER BODY IS FULL OF NEW GUINEA FLATWORMS"
    "GIVE HER WHAT SHE WANTS"
    "FILL HER WITH YOUR CUM"

    scene cafemocharedux13
    play music "cafe.mp3"

    s "{s}Why won’t you tell me what's wrong with you?{/s} Sure. What would you like to talk about instead?"
    r "Thanks, Sensei..."
    r "And, umm...this is probably pretty predictable...but since we're already on the topic..."

    scene cafemocharedux14
    with dissolve

    r "Did...Chika say anything else about me?"
    s "Hmm...Well, it’s not like we really had a lot of time to talk when you were only gone for a couple of minutes."
    r "But like...she hasn't said anything about me apart from when the three of us were here together?"
    s "Not really. Nothing worth mentioning, at least."

    scene cafemocharedux15
    with dissolve

    r "UGH. Fuck my life."
    s "So...how long have you had a crush on her?"

    scene cafemocharedux16
    with dissolve

    r "Hah...Was only a matter of time until you figured it out."
    s "I had a feeling ever since I caught you staring at her in the hallway. What I didn't know was how long you've felt this way."
    r "I literally have not stopped thinking about her for like two years."
    s "Interesting choice, Rin."
    s "I mean, Chika’s definitely cute. She just seems like the complete polar opposite of you."

    scene cafemocharedux8
    with dissolve

    r "I mean, she’s not {i}that{/i} different, is she? We’re both girls and we both...like...you know..."
    r "..."

    scene cafemocharedux6
    with dissolve

    r "Holy shit. We’re nothing alike, are we?"
    s "Did...that really not ever occur to you?"
    r "Not even once."

    "How?..."

    s "Either way, I’m glad it's finally out in the open."

    scene cafemocharedux17
    with dissolve

    r "Let's...not use the word {i}open{/i} just yet. Because if you leak this to anyone, I will chop your body in half and feed it to sharks."
    s "Deal."
    r "Oh, and don’t try and steal her from me either! I see the way you look at her sometimes!"

    if chikatownfirst == True:
        "Yeah...it might be a little too late for that."

    else:
        "I don’t think I’ve looked at Chika any differently than the others?..."

    s "I'll stay away, but...do you even know if she's into girls?"
    r "…"
    s "…"

    scene cafemocharedux18
    with dissolve

    r "You're really killing my vibes today, Sensei. I don't appreciate it."
    s "I think what I asked was a pretty decent question, Rin."
    r "All girls are at least {i}kind of{/i} into other girls! I mean...come on!"
    r "Have you {i}seen{/i} girls? How can you not be?!"
    r "But even if she pretends she isn't! Keep your hands to yourself until she properly rejects me!"

    if chikadorm20 == True:
        "I obviously can't find it in myself to tell Rin that Chika and I are already a little more than just friends."
        "But even if Rin had come to me with this request before all that, would it have changed anything?"
        "When have I ever allowed my choices to be guided by the hands of others?"
        "Chika and Rin have known each other for a long time now."
        "If anything was going to happen..."
        "Well, I think it would have happened already."

    s "Are you actually planning on asking her out?"

    r "Well...yeah. Eventually."
    r "I just don't know when."
    s "…"

    scene cafemocharedux19
    with dissolve

    r "What?! Stop judging me! I’ve never done something like this before! I don’t know what the correct order to do things in is!"
    r "And like you said, I don’t even know if she’s into girls yet! Let alone {i}me{/i}."
    r "She’s probably just being friendly with me like she is with literally everyone else but my stupid brain is all like “AHHH CHIKA!” or whatever."
    s "This sounds a little more serious than just a normal crush."

    scene cafemocharedux8
    with dissolve

    r "I have an actual folder of her Instagram photos saved on my laptop."
    s "You...do realize that's essentially stalking, right?"
    r "Nuh-uh. I'm nice. Stalkers aren’t normally nice. Probably."
    r "I'm sure some are. But I'm not one of them. Probably."
    s "You can't just keep adding {i}probably{/i} to the ends of sentences to dodge blame, Rin."
    r "Sure I can. Probably."
    s "..."
    r "..."

    scene cafemocharedux20
    with dissolve

    h "Rin, you can head out now! I’ve got it from here. And thanks again for coming in to open."
    r "No prob, Haruka! I’ll be back later! Probably!"
    h "Wait, what do you mean probably?"

    scene cafemocharedux1
    with dissolve

    r "I guess I’ll...see you later, Sensei."
    h "Rin, seriously! What did you mean by that?"
    r "And sorry if I've been acting weird and making you worry lately. I really do appreciate that you're looking out for me."
    r "I'm sure I'll be back to normal in no time at all and you'll be free to become my {s}NEW GUINEA FLATWORM{/s} guinea pig once more."
    s "Sounds good. Best of luck with your check-up."
    r "Gracias, mi amigo. ¡Adiós!"

    scene black
    with dissolve2

    "Rin quickly grabs her bag from behind the counter and rushes out of the cafe."
    "I watch her jog down the street toward the bus stop and decide it’s best to stay inside for a little while longer so I don't have to awkwardly pass by her again."
    "Or at least that's what I intend to do before the thought of her and Chika together forces me into the bathroom for several minutes before I decide to go home."

    $ renpy.end_replay()
    $ cafe15 = True
    $ rin_love += 1
    $ lettert = True

    "{i}You masturbate to a lesbian fantasy and Rin’s affection increases to [rin_love]!{/i}"

    stop music fadeout 5.0

    "………"
    "……"
    "…"

    jump saturdayafternoon

label cafe20:
...
```

## Code that triggers this event
File: \game\RinEvents.rpy
Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
...
```