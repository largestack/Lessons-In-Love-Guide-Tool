# Between the Slurps of Pork Broth
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen5&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 5

✅Event "[Tsuneyo: Snake Venom](./ramen1.md)" is completed (event=ramen1)



## Next events
* [Tsuneyo: A Short List](./ramen10.md)

## Event properties
* ID: ramen5
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop

## Event code
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramen5:
    scene tsuneysecondramen1
    with dissolve
    play music "kashiwagi.mp3"

    t "…"

    "I enter the ramen shop to be greeted by yet another blank stare from none other than the Kendo princess of whatever."
    "I’ve never been good with nicknames."

    t "Good evening. Welcome to Tojo Ramen."
    t "Please take your time looking over the menu and let me know if you have any questions."
    s "That’s exactly what you say every time I come here."
    t "Please let me know if you have any questions."
    s "I don’t have any questions, Tsuneyo. "
    t "I see."
    t "Then let me know when you are ready to order."
    s "Woah. Where’s your normal “Ah-” that happens almost every time I say your name? I was just starting to get used to it."
    t "I must have forgotten."
    s "Are you sure you’re not just getting comfortable around me?"
    t "Is there a reason for me to be uncomfortable?"

    if bonus == True:
        s "Well, yeah. I’m an older guy and you’re a girl. Doesn’t that sort of thing happen naturally?"
        t "Does it?"
    else:
        s "I exude cool dad energy. I figured it would start like, making you want to learn how to grill or something."

    t "I am alone with my father often and have never once felt uncomfortable."
    s "Well that’s your father. It’s different."
    t "I don’t understand how."
    t "We are all humans."
    t "Man. Woman. Child. Dog."
    t "We all breathe air and we all eat noodles."
    t "Such is life."
    s "Once again, I think your philosophical side is falling a bit short."
    t "I’ll get it one day."
    s "Also, I’m not sure if I have to actually remind you this or not, but dogs don’t count as humans."
    t "They should. "

    scene tsuneysecondramen2
    with dissolve

    t "Have you ever had a dog, Sensei?"
    t "I did when I was younger. "
    s "...Please tell me that you didn’t snap its neck and serve it to customers."

    scene tsuneysecondramen3
    with dissolve

    t "Disgusting."
    t "You should be ashamed of yourself for even thinking that."
    t "He was killed humanely and not served to anyone. He’s buried several blocks from here in an empty lot."
    s "Oh. Uhh...Sorry for your loss?"
    s "I’m not really sure how to follow up to a spontaneous reveal like that."

    scene tsuneysecondramen2
    with dissolve

    t "It’s okay. Sickness gets to everyone eventually."
    t "Just as I’m sure it will claim you and I someday."
    s "That’s less philosophical and more depressing. I give it a 6/10."
    t "A passing grade. I accept."

    "Tsuneyo begins to fidget with something behind her back, adjusting her shoulders so I can’t see whatever it is she’s holding."
    "But knowing her, I imagine it’s some sort of noodle-related paraphernalia."

    s "Are you hiding something from me, Tsuneyo?"

    scene tsuneysecondramen1
    with dissolve

    t "Of course."
    t "I’m hiding many things from you. It is common nature to not open up right away to someone you don’t know or trust."
    s "No, like literally hiding something. Behind your back."
    t "Oh."
    t "Yes."
    s "…"
    t "…"
    s "Why?"
    t "…"
    t "I don’t know."
    s "...Can I see it?"
    t "Sure."

    scene tsuneysecondramen4
    with dissolve

    s "..."
    t "..."

    "Tsuneyo brings the object she was hiding into view and it is...a large chef’s knife."

    t "Prepare to die, you bastard."
    s "Tsuneyo, would you mind explaining to me why you were hiding a knife behind your back this entire time?"
    t "It will be a boring explanation."
    t "Would you like to hear it anyway?"
    s "Yes, please. I’d like to confirm that I can still come here without the risk of being murdered."
    t "You walked in while I was cutting ingredients and I forgot to put it down."
    t "By the time you got to the counter, I realized I was still holding it and hid it behind my back so you wouldn’t think I was going to kill you."
    s "Oh. That actually {i}is{/i} a boring explanation."
    t "I know."
    s "But wait. Then what was with that “Prepare to die, you bastard” line?"
    s "Why would you say that if you didn’t want me to think you were going to kill me?"
    t "I thought it would help create a more fun atmosphere for the ramen shop."
    t "I can see it now. People flocking in from all over the world because of the quirky, upbeat ramen girl, Tsuneyo Tojo."
    s "Quirky and upbeat are perhaps two of the only words I would {i}not{/i} use to describe you."
    t "Then I will have to end your life."
    t "Prepare to die at the hands of the flavor-samurai. "
    s "Can I at least have one last bowl of ramen before I pass on? "

    scene tsuneysecondramen5
    with dissolve

    t "Of course. A death is not truly honorable unless you are full of noodles."

    "Despite these one liners and philosophies (If you even want to call them that) making absolutely no sense, they’re definitely...amusing. "
    "It’s actually kind of impressive how horrible Tsuneyo is at communicating."
    "Either that or she’s actually way better at it than she lets on and is simply pulling my leg in every single conversation."
    "Maybe she’s some sort of super genius and I’m just not aware of it?"

    t "..."
    s "..."
    t "...?"
    s "What? Why are you looking at me like that?"
    t "I’m waiting for your order."
    t "It is your last meal, so I will make sure it is one to remember."
    t "Even if you won't actually get to remember it."
    s "Wait, you’re not actually going to kill me, are you?"
    t "You have insulted the integrity of the Tojo family. I must do my job and uphold it by any means possible."
    s "How can you say something so serious with a smile on your face?"
    t "Because I’m joking."
    s "Really? You kept this one going for so long that I was beginning to think you might actually be serious."
    t "Killing a customer during store hours would lead to bad reviews."
    t "We’d need to create a new tag line just to get the restaurant back on track."

    scene tsuneysecondramen6
    with dissolve

    t "Tojo Ramen. All of the flavor, none of the violence."
    t "Something like that."
    s "What a totally inconspicuous slogan for a store where the Yakuza hang out."

    scene tsuneysecondramen5
    with dissolve

    t "Real estate is not a violent business, Sensei. You should know this if you are going to teach people."
    t "I lack any sort of formal education and even I know that."
    s "Tsuneyo, the Yakuza are more than just-"
    s "Ahh, fuck it. What’s even the point?"

    scene tsuneysecondramen7
    with dissolve

    t "The curse appears again..."
    s "Didn’t you learn that “Fuck” isn’t an {i}actual{/i} curse, though?"
    t "That does not make it any less intimidating. "
    t "If I told you the knife I am holding is plastic, you would still fear it, wouldn’t you?"
    s "...Not really. No."
    s "Even if you are some sort of Kendo god, I don’t think you’d have it in you to actually kill someone."

    scene tsuneysecondramen1
    with dissolve

    t "Would you?"
    s "Kill someone?"
    t "Yes. Would you be able to take the life of another person? And if so, why?"
    s "You’re not an undercover cop or anything, are you?"

    scene tsuneysecondramen2
    with dissolve

    t "If I am, I’m a very bad one."
    t "I haven’t shown up to work in years..."

    "Huh..."
    "Would I actually be able to kill someone?"
    "I mean...Maybe? I haven’t ever really put much thought into it before."
    "There would have to be a good reason for it and-"
    "Wait, why are we talking about something like this in a ramen shop?"

    s "I have no idea. And I don’t really have any plans to figure that out any time soon."
    t "Good. I no longer have to fear for my life. "
    t "Praise be."
    s "Praise be."

    scene tsuneysecondramen5
    with dissolve

    t "Heheh..."
    s "Wait, why do you keep saying that and why do I just repeat it like it’s some sort of reflex?"
    t "I don’t know. But it’s funny, isn’t it?"

    scene tsuneysecondramen8
    with dissolve

    t "Much funnier than my actual jokes, anyway."
    t "I’m fully aware that those are not what they should be yet."
    t "But just as a marinating-egg, they will get better in time. And Tsuneyo Tojo will go on to be more than a mysterious noodle-woman."

    "For a moment, I ponder if whether this whole comedy thing is something Tsuneyo is actually interested in or if it’s just a way for her to get her personality across better."
    "The truth is, I’m kind of hoping that she doesn’t get any better if it’s the former."
    "Is it wrong of me to want to hold back the dreams of someone else for my own personal benefit?"
    "Change is a terrifying thing when it affects those around us."
    "And even if Tsuneyo is a bit of a blank slate when it comes to personality, I think that’s what makes her {i}her{/i}."
    "{s}And if I need to be the one to prevent her from changing, I will give up my arms for it.{/s}"
    "{s}74 68 65 72 65 20 69 73 20 6e 6f 20 67 6f 64 20 68 65 72 65 2e 20 6a 75 73 74 20 6e 6f 6f 64 6c 65 73 2e{/s}"

    scene tsuneysecondramen1
    with dissolve

    t "You are taking much longer to decide than normal today."
    t "Would you like an explanation of the menu?"
    s "It doesn’t take a rocket scientist to figure out how a menu works, Tsuneyo."

    scene tsuneysecondramen9
    with dissolve

    t "Ah-"
    s "Oh, there it is again."
    s "I guess you’re not getting comfortable around me after all."

    scene tsuneysecondramen1
    with dissolve

    t "I am not allowed to get comfortable around men."
    t "All I can do is serve them food and hope that they will stay several feet away from me so I don’t get pregnant."
    s "It takes a little more than that to get someone pregnant."
    t "You’d be surprised in today’s society."
    s "What do you know about society, Tsuneyo? You didn’t even start going to[school] until recently."
    t "I’ve learned much from the people who sit on the opposite side of the counter."
    t "One of the many, {i}many{/i} wonderful things about ramen shops are the conversations to be shared between perfect strangers in between the slurps of pork broth."

    scene tsuneysecondramen2
    with dissolve

    t "“How was your day? What did you see on the way here? Are your children well?”"
    t "This is more than just a home for me and my father. It’s a home for anyone who has 700 yen and a little bit of time to spare."
    t "So to say I don’t understand society because of my homeschooling just isn’t true."
    t "There is more here than you would believe, Sensei."
    s "…"

    "For the first time ever, Tsuneyo breaks into a well-spoken tangent that goes on to show just how much she {i}does{/i} care about this place."
    "It becomes clear that the whole noodle thing isn’t just a running gag...And that she isn’t being forced into carrying on her father’s business just because she was born into it."
    "She...was raised by noodles."

    scene tsuneysecondramen1
    with dissolve

    t "..."
    t "You have a strange look on your face again."
    s "...Yeah."
    s "I just thought of a really weird sentence."
    s "I’ll have the Green Dragon again, please."

    scene tsuneysecondramen5
    with dissolve

    t "Of course. One Green Dragon. "
    t "I will be right back. Please do not rob the cash register while I am preparing your food."
    s "I didn’t plan on it..."

    scene tsuneysecondramen10
    with dissolve

    "Tsuneyo disappears into the kitchen the same way she always does when I order."
    "And I hear the same sounds I always do as she puts her all into making sure everything comes out perfectly."
    "…"
    "You know-"
    "Maybe places like this really {i}are{/i} more than they appear to be on the outside."
    "And even in this horrible part of town-"
    "Somewhere good exists."
    "Maybe."
    "Nothing is ever certain."

    scene black
    with dissolve2

    "But it doesn’t hurt to believe that."
    "At least for now."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen5 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen10:
...
```

## Code that triggers this event
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
    if tsuneyo_love >= 5 and ramen1 == True and ramen5 == False:
        jump ramen5
...
```