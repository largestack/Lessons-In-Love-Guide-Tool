# Two Steps Back
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm30&go=Go)



## Event preconditions
✅Rin love greater than or equal to 30

✅Day of week is not Tuesday

✅Event "[Rin: Nothing Was Different](./cafe30.md)" is completed (event=cafe30)



## Next events
* [Rin: Ten Steps Forward](./rindorm35.md)

## Event properties
* ID: rindorm30
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm30:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "…"
    "I knock on the door and press my ear against it, waiting to see if Rin and Futaba are in."
    "Rin mentioned recently that the two of them would be hanging out and chatting sometime soon, so I’m wondering if that’s what’s going on tonight."

    f "Who is it?"
    s "Hey, Futaba. It’s me. Can I come in?"
    f "Sensei? One second. Rin just needs to-"
    r "I’m fine. He can come in."
    f "Wait...really? Are you sure?"
    r "Mhm. I don’t mind."
    f "That’s...Uhh, well...Okay."
    f "The door’s open, Sensei. You can come in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I pull the door open and make my way into the room."
    "The distorted sounds of some angsty garage band leak through the speakers of Rin’s laptop and make their way to the opposite side of the room, where the two of them are laying."
    "I gently bring myself to my knees and crouch down beside them."

    scene rinfutaba1
    with dissolve
    play music "closeto.mp3"

    r "Hey, man. Welcome to the bedroom."
    r "As you can see, I am not wearing pants. Please ignore this fact."
    s "I will do my best."
    f "That’s...why I was hesitant to let you in."
    f "I knew you two had gotten close, but I didn’t realize it was “No pants” close..."
    r "It’s whatever. I’m lacking the willpower to reject anything right now. "

    scene rinfutaba2
    with dissolve

    f "Please don’t say things that will make me worry about you even more."

    scene rinfutaba3
    with dissolve

    r "Heheh~ Sorry..."
    s "So...any new developments in Rin Rokuhara’s eternal struggle against heartbreak?"

    scene rinfutaba4
    with dissolve

    r "Just getting right to the point, huh?"
    f "There...is one thing that happened. Though, Rin seems to be taking it a lot worse than I think she should."
    s "Well what hap-"
    r "She texted me."
    s "Who? Chika?"
    r "Of course, Chika."
    s "Well, isn’t that a good thing?"
    f "That’s what I was saying. Rin won’t even reply to her."
    r "I’m too embarrassed."
    r "Besides, she said the three words no one ever wants to hear."
    s "...I love you?"

    scene rinfutaba5
    with dissolve

    r "I fucking wish."
    r "All she said was “Can we talk?”"
    r "Like, what am I supposed to say to that?"
    r "{i}Hey, remember when I confessed my feelings to you and then promptly ran away? Sorry about that. Wanna be friends again?{/i}"

    scene rinfutaba6
    with dissolve

    r "I fucked up. I did everything wrong."
    s "That’s not true."
    s "You were finally able to say how you’ve felt about her since middle[school] or whenever it was."
    s "That’s not something you should just dismiss. It’s a big step."
    r "A step backwards, yeah. Two steps, even."
    r "What’s the point of getting something off of your chest if you’re just going to lose something else in the process?"

    scene rinfutaba7
    with dissolve

    f "But...maybe you didn’t lose anything? That’s probably what Chika wants to talk about."
    s "I’m with Futaba on this. Chika isn’t the type to just cast you aside because you have feelings for her."
    r "…"
    f "Agreed. For example, what would you do if you found out I’ve always had feelings for you, Rin? "
    r "Probably make out with you. You’re hot."

    scene rinfutaba8
    with dissolve

    f "That’s not...the answer I was looking for."
    r "I know. You don’t like girls."
    f "What...I’m trying to get at is that you wouldn’t just leave me behind if you didn’t feel the same way."
    f "That’s not the type of person you are."
    f "And I don’t know Chika as well as you do, but I’m pretty sure she isn’t like that either."
    r "That doesn’t make it hurt any less, though."

    scene rinfutaba9
    with dissolve

    r "Is it...silly to say that it feels like I’m missing a part of myself now?"
    r "Actually, don’t answer that. I know it’s silly. "
    r "But it’s like...you spend so long wishing you were with someone and thinking up how things would be if you were together that..."
    r "Well, hearing that it won’t ever happen is kind of like taking all of those delusions and shoving them into a blender."
    r "And all you can do is watch them be shredded to bits in front of you. "
    s "Well, what if...whatever comes {i}out{/i} of the blender is even better?"

    scene rinfutaba10
    with dissolve

    r "I sure hope you have a good explanation for whatever the Hell you meant by that..."
    f "Me too. That was pretty bad."
    s "I’m not good at cheering people up. I’ve said this before."
    s "But what I mean is, maybe this will open some sort of door for you?"
    s "Didn’t you tell me on the beach that being rejected might be what you need to move on?"
    r "I don’t remember anything about the beach. I’ve wiped it all from my memory already."
    s "Well you did. And I think you might have been right."
    s "Love isn’t something you can go out searching for. It’s something that comes to you naturally."

    "During times like these, it’s best to regurgitate the words of people wiser than you."
    "I don’t even marginally believe what I just said to Rin, but I think it will make her happy."
    "If I were to speak from the heart, I’d tell her that true love doesn’t exist and to just go out and find someone she’s sexually attracted to."
    "I’d tell her to give up on feeling anything ever again. "
    "Life is better when you love nothing."
    "Sure, it’s still life at the end of the day, so it’s not something amazing."
    "But at least you’ll be able to end a confession to someone without spending the night crying afterwards."

    scene rinfutaba11
    with dissolve

    r "So...are you saying I should just...try my luck with someone else?"
    r "Are you really that far away from being attached to someone that this sounds like an easy feat to you?"

    scene rinfutaba12
    with dissolve

    r "It’s been years, dude..."
    r "I can’t just change my outlook on things at the drop of a hat. "
    s "You don’t have to. I just don’t want you to think that this one thing is going to be the end of your life."
    s "There’s still plenty you have going for you."

    scene rinfutaba13
    with dissolve

    f "That’s right. You still have us."
    f "Molly, too. "
    f "She’s been really worried about you, you know?"

    scene rinfutaba14
    with dissolve

    r "That doesn’t surprise me...she worries about everything."
    f "To be fair, I think her worrying is kind of warranted this time."
    s "Yeah, that’ll happen when you just disappear in the middle of a vacation."
    s "You two better be careful. Since both of you left before the end, people might start to think you guys don’t like them or something."

    scene rinfutaba15
    with dissolve

    f "Wait, really?! That’s not why I left at all! I just wasn’t feeling well and-"
    r "Excuse me, Futaba. But this is my time. Hearing about your stomach ache won’t help mend my broken heart."

    scene rinfutaba16
    with dissolve

    f "Oh...right. Sorry."
    r "Oh, come on. I’m only kidding. "
    r "Just letting me lay on you is enough to make me feel a little better."
    r "I know you two care about me and...somehow or another, I’ll get through this."
    r "It’s not the end of the world, it just feels like it."

    "That’s a good way of putting it."
    "I’ve seen the end of the world."
    "I think."
    "And, in a roundabout way, I can imagine that Rin {i}is{/i} feeling something similar to how I felt back then."
    "Confused. Alone. Hopeless."
    "An endless combination of unfortunate adjectives, all with their own negative connotations."
    "We find ways to weave them together into beautiful tapestries and drape them over our destinations, so when we walk out onto a roof to meet our end, it feels a little like home."
    "But home is nowhere."
    "And we are here."
    "So I guess all that’s left to do is build a new one."

    s "So, what now?"

    scene rinfutaba17
    with dissolve

    r "Hm? Well, I was planning on being a wimp for a few more days and crying until my tear ducts give up on me."
    f "And I was planning on doing laundry every night so I wouldn’t run out of pajamas from drying all of her tears."
    s "You two really are like sisters, aren’t you?"

    scene rinfutaba18
    with dissolve

    f "We are."
    f "And I also double as a pillow. And a support dog."
    f "I can be pretty multi-talented in times of desperation."
    r "She’s the best pillow. I’m happy that I’m coherent enough this time to take advantage of that."

    scene rinfutaba19
    with dissolve

    f "Me too. Your sadness is a lot easier to handle when I know what’s causing it. "
    r "Trust me, I know. "
    r "There was one weird thing that happened the night of the rejection, though."
    f "Weird? What do you mean?"
    r "It was almost like a delusion."
    r "When I was laying next to Sensei and he was rubbing my head, I started hearing things."
    r "It might sound crazy, but it was kind of like hearing time itself passing us by."
    r "It got me thinking, “Oh no. It’s happening again. I’m spiralling out of control.”"
    r "But, before I knew it, it was all gone."
    r "The sound of time turned into a deafening silence. And no matter how much I screamed, there just wasn’t anything there."
    r "Has anything like that ever happened to you?"
    f "Not that I can remember...And that sounds like something that would definitely leave a lasting impression on me."

    scene rinfutaba20
    with dissolve

    f "How about you, Sensei?"
    f "Have you ever experienced anything like what Rin is talking about?"

    stop music
    play sound "static.mp3"
    scene rinfutaba21
    with flash
    scene rinfutaba20
    with flash
    stop sound

    s "{s}Far too often.{/s} No. I’ve never experienced anything like that."
    r "It was probably just some weird...depression-related thing. Who even knows?"

    play music "sweetvermouth.mp3"

    r "No use dwelling on it now, though."
    r "I’ve just gotta keep moving forward. And when my feet get too heavy to lift, I always have you two to pick me up and carry me wherever I need to go next."
    s "That’s true. But don’t expect me to give you a piggyback ride to the cafe any time soon. That’s like three miles from here. "

    scene rinfutaba22
    with dissolve

    r "And you call yourself my friend..."
    r "I guess Futaba will just have to carry me."

    scene rinfutaba23
    with dissolve

    f "I’d be lucky if I could even make it down the block giving you a piggyback ride..."
    r "You deny me {i}and{/i} call me fat? What is this treachery?"
    s "Okay, well...I guess I’ll leave you two to it."

    scene rinfutaba24
    with dissolve

    r "Huh? You’re leaving already?"
    s "I am. I just wanted to help cheer you up, but I’m pretty sure Futaba is a lot more help than I am in that regard."
    s "But I’ll stop by the cafe again soon and we can talk. "
    r "You really don’t have to leave. I want you here."
    f "I’m okay with you staying, too."

    "One of the most important parts of life is figuring out when you are and aren’t needed."
    "If I remain here any longer, I’ll just wind up bringing things down in one way or another."
    "Besides, after hearing Rin’s tangent about time, I’m suddenly feeling a little bit off myself."
    "I’m not exactly sure why, but I feel like I need to go."
    "I should let these sisters just...be sisters for the night."

    s "Thanks, but I really should be going."
    s "Maybe we can all do something together soon, though?"

    scene rinfutaba25
    with dissolve

    r "Is this you volunteering to take us to an all-you-can-eat dessert buffet? "
    r "That’s the one thing guaranteed to mend any [young]maiden’s heart."
    s "Then why wasn’t that the first place you went after the beach?"
    r "Because I don’t have enough money, duhh."
    s "We’ll...figure something out."
    s "I can’t guarantee it will be {i}that{/i}, but we can definitely go out on a “Fix Rin’s Heart” trip soon."
    f "I’ll free up my calendar..."

    scene black
    with dissolve2

    "I say goodbye to the two of them and make my way back to the streets of Kumon-mi."
    "It’s another night teetering on the brink of being cold."
    "Summer is on life-support."
    "And I walk home thinking about clocks and how they correlate to the underlying sadness in everything."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm30 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm35:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
    if rin_love >= 20 and cafe20 == True and day50 == True and rindorm20 == False:
        jump rindorm20
    if rin_love >= 25 and rindorm20 == True and rindorm25 == False:
        jump rindorm25
    if rin_love >= 30 and day != 2 and cafe30 == True and rindorm30 == False:
        jump rindorm30
...
```