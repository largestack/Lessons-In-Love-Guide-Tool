# Haruka
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe10&go=Go)



## Event preconditions
✅Rin love greater than or equal to 10



## Next events
* [Rin: Rin's Secret](./rindorm10.md)

## Event properties
* ID: cafe10
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe

## Event code
File: \game\RinEvents.rpy
Code:
```python
...
label cafe10:
    scene cafe_day
    with dissolve
    play music "cafe.mp3" fadein 2.0

    "I make my way into the cafe a bit more tired than usual because, for some reason, the world decided to spite me by disallowing me to sleep for more than an hour at a time last night."
    "But apart from how hard it is to be me and how cruel the world can be at times, I am now prepared to see my favorite barista and consume whatever strange concoction she cooks up for me today."

    scene cafeten1
    with fade

    "Or not."

    nr "Good morning! How's your day going so far?"
    s "It's...fine. And yours?"
    nr "Living the dream."
    s "That bad, huh?"
    nr "Thank you for being the first person to ever understand how canned and robotic that response is."
    nr "I take it you've worked in customer service before?"
    s "No, I've just gotten very good at bantering with baristas lately."

    scene cafeten2
    with dissolve

    nr "Oh. So this isn't your first time here?"
    s "Nope. I guess you could say I've become a bit of a regular."
    nr "A bit of a-"

    scene cafeten3
    with dissolve

    nr "Wait, you wouldn't happen to be Rin's teacher, would you?"
    s "I would. I'm a little surprised to have you guess that based on...literally no information apart from being a new regular, though."

    scene cafeten4
    with dissolve

    nr "Well, it's not like we've had many customers that fit your description lately."
    s "That description being?"
    nr "The owner of a penis."
    s "Well, that's a fun new way to say {i}man.{/i}"

    scene cafeten5
    with dissolve

    nr "Thanks for always stopping by, though. I think you'll be happy to know that I let Rin add her mystery beverage to the menu after reading your comment card."
    nr "I don't really think the part about her being the best barista ever was necessary, though. Especially since I'm the proud owner of that title."
    s "Well, as the proud owner of a penis, I would like to congratulate you for being the actual best barista and will offer Rin my condolences the next time I see her."
    r "Sensei! Don't give in that easily! You know in your heart of hearts that it is I, Rin Rokuhara, who is the true champion of (copyrighted frozen beverages)!"

    "Rin calls out from behind me and I begin to question how I walked in without noticing her."

    nr "So, what would you like? I don't want to keep you from talking to your regular barista for too long."
    s "Just a black coffee is fine."
    s "Oh, and your name."

    scene cafeten6
    with dissolve

    h "Haruka."
    h "And yours?"
    s "You can just call me Sensei."
    h "..."
    s "..."

    scene cafeten7
    with dissolve

    h "Wait, really?"
    s "Yup. And I'll just take a black coffee, please."
    h "But...your name-"

    scene black
    with dissolve

    s "You can just write {i}Sensei{/i} on the cup. It's fine."
    h "But...but..."

    "Haruka stands there for a moment as if she's waiting for the punchline to a joke."
    "Unfortunately, that punchline never comes and she is forced to awkwardly pour me a drink without ever learning my true identity."
    "She finishes and hands it to me across the counter, eyes unblinking and focusing on mine."
    "I stare back, nod, then walk away."
    "........."
    "......"
    "..."

    scene cafeten8
    with dissolve

    r "What the Hell was that? You trying to look cool in front of my boss or something?"
    s "Did it work?"
    r "She's still staring at you, so...I think so?"

    "Excellent."

    r "Also, aren't you here a little later than normal today? You actually caught me on my real break for once."
    s "Yeah...I couldn't really get any sleep last night, so I wound up not getting out of bed until a little while later."
    r "How come? Nightmares or something?"
    s "Nothing like that. Just one of those nights, I guess."

    scene cafeten9
    with dissolve

    r "Guess I can feel that. I've had my share of sleepless nights, but I'm typically a pretty heavy sleeper when my brain isn't exploding."
    s "Really?"
    r "Oh yeah. You could probably beat me with a pillow or something and I'd stay asleep."
    s "That’s kind of worrying in the event of some type of emergency."

    scene cafeten10
    with dissolve

    r "Nah, I'm sure Futaba would rescue me if something like that ever happened."
    r "Unless she's just been pretending to like me all these years and is secretly waiting for me to die."
    s "That doesn't sound like Futaba."
    r "I don't think so either. But I guess you never truly know someone until they have to save your life due to unforeseen circumstances."
    s "That's...yeah, okay."

    scene cafeten11
    with dissolve

    r "So, you finally got to meet my boss."
    s "Yeah. And she even got me exactly what I asked for. I didn’t realize this place could do that."
    r "Thoughts? She your type?"
    s "That depends. Is this a trick question?"

    scene cafeten12
    with dissolve

    r "No way! You can tell me. We're pals, right?"
    r "Plus, we have today off, so it's kind of like you're not even my teacher."
    s "I mean, I don’t think the time of day really determines my relationship with you."
    r "Hot or not, Sensei? Hot or not?"
    s "She's attractive, yeah."
    s "And...{i}very{/i} well endowed."

    scene cafeten13
    with dissolve

    r "You've got that right. Those things could feed a village of starving children for like a decade."
    s "I...don't think starving children would need to breastfeed for ten whole years...but I...guess I wouldn't blame them for wanting to?"

    scene cafeten14
    with dissolve

    r "Well, sorry to break your heart, but she’s married."
    s "Then why did you make it sound like you were trying to hook me up?"
    r "Cause I figured that would be the easiest way to get you to tell the truth."
    s "Is her husband still around with the whole space war thing going on?"

    scene cafeten10
    with dissolve

    r "Nope. He got drafted a few years ago and she hasn’t seen him since."
    r "She's actually really torn up about it underneath the buxom, bubbly exterior, though."

    scene cafeten15
    with dissolve

    r "I {i}may{/i} know someone else who’s into you, though. And it may or may not be a girl you know pretty well."
    r "But you’ve gotta promise not to tell her I told you."
    s "I'm guessing it's one of the students, then?"

    scene cafeten16
    with dissolve

    r "Woah! How did you know?"
    s "Well if it’s not Haruka, it kind of has to be. I don't really know anyone else."
    r "Oh, true. Good point."
    r "But yeah, it's a student. And she may or may not be my roommate."
    s "Ahh, so it's Futaba you're talking about."

    scene cafeten15
    with dissolve

    r "Bingo! "
    s "Yeah, I kind of figured. She tends to trip over her words whenever she talks to me, so...kind of a dead giveaway."

    if futabadorm15 == True:
        "She has also had my penis in her hand, but I don't think that's a detail I should really divulge right now."

    scene cafeten17
    with dissolve

    r "Yeah...I guess she's never been good at hiding her feelings."
    r "Not that she's ever really had any romantic ones but, like...yeah. Just speaking her mind has always been kinda tough for her."
    r "Truth be told, she’s been head over heels for you since the first day of school."
    s "Is it really okay for you to be telling me this?"
    r "As long as you don’t tell her I told you, I don't think there's a problem with it."
    r "If anything, I see it as kind of a favor. Who knows when she'd tell you on her own?"
    s "How is revealing a friend's secret a favor, exactly?"
    r "Because now that you know someone as cute and cuddly as Futaba is attracted to you, aren't you tempted to take things a little further?"
    s "Is that...actually something you're okay with?"

    scene cafeten8
    with dissolve

    r "Hm? Why wouldn’t it be? If it makes the two of you happy, I’m all for it."
    s "That’s...a little unexpected."

    if bonus == True:
        s "You do realize how much older I am than you, right?"
    else:
        s "She is your friend and you should be vigorously screening all of her potential love interests to ensure that she is good hands."
        s "Also, I am, her teacher."

    scene cafeten9
    with dissolve

    r "Mm...That kind of stuff doesn't really matter to me."
    r "I'm sure it wouldn't really fly in school, but it's not my business to tell you where you can and can't stick your wiener."
    r "I know if {i}I{/i} had a wiener, {i}I'd{/i} want to stick it in Futaba. She smells nice and her skin is really soft."
    s "This is a side of you I did not expect to come out today."
    r "I regret nothing."
    h "Rin, are you almost done over there? Your break ended five minutes ago."

    scene cafeten18
    with dissolve

    r "Ahh...shoot. I didn't realize what time it was. I've gotta get back to work."

    scene cafeten14
    with dissolve

    r "Try and get some sleep tonight. Okay, Sensei?"
    r "And remember to not tell Futaba what I told you or I will sell your organs for discounted rates on the black market."
    s "You really scare me sometimes, Rin."
    r "Good."

    scene black
    with dissolve2

    "I follow Rin back to the counter to dispose of my remaining coffee and watch her disappear into the kitchen."
    "Haruka, still in an apparent state of shock after giving me her name only to be robbed of mine, stares blankly at me as I nod to her once more and make my way out of the cafe..."

    stop music fadeout 3.0

    $ renpy.end_replay()
    $ cafe10 = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label cafe15:
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
...
```