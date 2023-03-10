# The Man Who Loves Nothing (Tsuneyo)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Tsuneyo love greater than or equal to 10

* Event [A Short List](./ramen10.md) (Tsuneyo) is completed)

* Event [Drug Use & Jump-Rope](./tsuneyodorm5.md) (Tsuneyo) is completed)



## Next events

None

## Event properties

* Id: tsuneyodorm10
* Group: Tsuneyo
* Triggered by label: tsuneyodorm
* Triggered by branch label: tsuneyodorm
* Triggered by path: tsuneyodorm->tsuneyodorm10

## Official wiki page

[The Man Who Loves Nothing](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyodorm10&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label tsuneyodorm10:
    play sound "knock.mp3"

    s "Tsuneyo, are you in there?"
    s "Let’s hang out."

    "I hear a set of footsteps quietly approach the door and stop right in front of it."

    t "Why?"
    s "Why not? I’m bored and you’re not doing anything."
    t "I’m doing plenty of things."
    s "What could you possibly be doing in there?"
    t "Homework."
    s "I don’t give you any homework."
    t "Noodle homework."

    "...What the fuck does that even mean?"

    t "Studying different types of wheat."
    s "Why?..."
    t "Why not?"
    s "Put your noodles on hold for a few minutes and talk to me. "
    t "…"
    s "…"
    t "Okay."
    t "Please enter."
    s "Thank you..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Tsuneyo unlocks the door and I make my way into the room, stepping over a few plastic bags piled near the entrance along the way."

    scene tsuneyodormten1
    with dissolve

    t "Hello."
    s "Hey. What’s up with the pajamas?"
    t "What do you mean?"
    s "I mean like...They’re cute and everything...but what’s up with that smiley face?"
    s "It’s kind of creepy, don’t you think?"

    scene tsuneyodormten2
    with dissolve

    t "It’s a normal smile. Don't make fun of my clothes just because you hate joy."
    s "I don’t {i}hate{/i} joy."

    scene tsuneyodormten1
    with dissolve

    t "Then why don’t you ever smile?"
    t "You should try to be like this shirt. But with more energy and less cotton."
    s "You’re the last person I want to hear about energy from. You have like three facial expressions."
    t "Did you come here to fight?"
    s "What? No. I was just going along with your banter."
    s "Besides, I think you look cute. Even if your shirt is a little weird."

    scene tsuneyodormten3
    with dissolve

    t "Weird?"
    s "Well...Not weird. Just different."
    t "That doesn’t sound any better."

    scene tsuneyodormten1
    with dissolve

    t "This shirt was a gift from my father and I would greatly appreciate it if you would keep your comments to yourself."
    t "I am embarrassed enough to be seen like this in general."
    s "You don’t look very embarrassed to me."
    t "That's because I only have three facial expressions. You said it yourself."

    "Yeah, but I feel like one of those is actually the embarrassed one."
    "Tsuneyo seems fine to me. Sure, her posture is a little different than normal, but it’s not like she’s curled up in the corner or anything."

    scene tsuneyodormten4
    with dissolve

    t "So is there a real reason for your appearance today? Or is it just to hurt me?"
    s "I’m not here to hurt you..."
    t "You have the eyes of a man who is here to hurt a quirky noodle-girl."
    t "I know Kendo. I can kill you."
    s "I know you do. It’s one of your two defining interests."

    scene tsuneyodormten5
    with dissolve

    t "Tsuneyo Tojo, Soup Warrior."
    s "What happened to ‘Samurai of Flavor?’"
    t "Samurai by day, warrior by night. "
    s "Well, at least you know what you’re into. That’s more than I can say for myself."

    scene tsuneyodormten6
    with dissolve

    t "Ahh, right. You are the man who loves nothing."
    t "You said that at the restaurant the other day when the girl with the strange eyes asked you to list the things you enjoyed."

    "The man who loves nothing, huh? "
    "That’s a pretty badass nickname. "
    "Depressing, sure. But still cool. "
    "I can live with this."

    s "That's right. I hate everything."
    s "Speaking of Kaori, though, have you run into her at all since then?"

    scene tsuneyodormten7
    with dissolve

    t "I think she was looking around my backyard the other day."
    t "Is that legal?"
    s "Probably not. "

    scene tsuneyodormten8
    with dissolve

    t "Is she dangerous? Do I need to call the police?"
    t "She seems rather frail, so I could probably snap her neck instead if that’s easier."
    s "Okay, well definitely don’t do that. Kaori isn’t evil, she’s just...weird."
    s "She probably just thinks it was strange that you wouldn’t hire her. "
    t "The Soup Warrior needs no assistance. Just time and ingredients."
    s "And your father is totally cool with that? He doesn’t think you need any more help?"

    scene tsuneyodormten9
    with dissolve

    t "He has not weighed in on the matter. This is a decision I made for myself."
    t "My father has had a profound influence on the way I approach life, but he does not decide everything for me."
    s "Weren’t you just saying the other day how you tell him virtually everything you do?"
    t "Yes. But not because he asks. It’s because I want to. "
    t "Is it wrong to share your feelings with the person you love?"

    scene tsuneyodormten10
    with dissolve

    t "Wait, don’t answer that."
    t "You do not love anyone or anything. I’m sorry if my question offended you."
    s "Wow, you didn’t even give me a chance to respond that time."
    t "Sometimes, I accidentally think you’re a normal person and say more than I should."
    s "Why is it that every time you address me, I feel myself becoming less and less human?"

    scene tsuneyodormten11
    with dissolve

    t "Were you ever human to begin with?"
    s "This is exactly what I'm talking about."
    s "But what about you, Tsuneyo? Are {i}you{/i} human?"
    t "Is anyone human?"
    t "Or are we all simply objects put here for the enjoyment of some higher power?"
    t "Left to wander the earth in search of the ultimate flavor combination."
    s "That was actually a pretty thought-provoking question until you got to the flavor part."
    t "My father’s words. The flavor part was what I added to it. "
    t "I think it makes it more interesting. And delicious."

    scene tsuneyodormten12
    with fade

    "Tsuneyo moves over to her bed and sits down, bringing one of her hands to her arm and clutching it gently to steady the nerves that I imagine she's buried deep down inside somewhere."
    "She hasn’t really shown much emotion at all since I’ve met her."
    "And sure, maybe that’s just her personality...But maybe it’s something more than that?"
    "She has no problems talking about her father, it seems."
    "Maybe he is the key to her heart?"

    scene tsuneyodormten13
    with dissolve

    t "Why did you follow me to my bed?"
    s "Because we were in the middle of a conversation. Was I not supposed to?"
    t "I’d personally feel more comfortable if you stood by the door."
    s "But I’m already here."
    t "Are any of us {i}really{/i} here?"
    s "You’re pretty philosophical today for someone who has already admitted to that not being a strong point."
    t "And you’re a bitch."

    "..."

    s "Did Molly teach you that word as well?"

    scene tsuneyodormten14
    with dissolve

    t "Did I use it correctly?"
    t "I don’t need to do push-ups to break a curse this time, do I?"
    s "No. Just try not to use that to anyone you don’t inherently dislike. It’s not exactly a great word."
    t "Understood, bitch."
    s "…"
    t "…"

    scene tsuneyodormten15
    with dissolve

    t "Heh..."
    s "Woah, what’s this?"
    t "Proof that I have more facial expressions. "
    t "And also a joke. Feel free to laugh."
    t "I don’t think you are a bitch."
    s "That’s such a strange sentence, and yet it fills me with such joy..."

    scene tsuneyodormten14
    with dissolve

    t "Does it? I thought you were immune to joy?"
    s "I never said that. Those are your words."
    s "I’m one of the happiest people you’ll ever meet."
    s "I wake up every day, go to[school], talk to cute girls and, every once in a while, they’ll even let me into their rooms."
    s "What more out of life could I ask for?"
    t "…"
    s "…"

    scene tsuneyodormten16
    with dissolve

    t "That tangent filled me with disgust and I’m not sure why."
    t "Are you what they call a “pervert?”"

    if bonus == True:
        s "Probably, yeah."
    else:
        s "Absolutely not. And if I did anything to give you the idea that I am, I sincerely apologize."

    scene tsuneyodormten17
    with dissolve

    t "Mm..."
    t "And I’m in my pajamas..."
    t "I am becoming weaker."
    t "I should never have let my guard down."
    t "Please, just take my money and leave. I beg you."
    s "Tsuneyo, I’m not going to do anything to you."
    t "I don’t even know {i}what{/i} you would do to begin with. I just know it’s bad."

    scene tsuneyodormten18
    with dissolve

    t "{i}What was the spell she taught me again?...{/i}"
    t "Umm...Holy Bulwark!"
    s "Tsuneyo, what in the world are you doing?"
    t "Casting...Holy Bulwark?"

    scene tsuneyodormten19
    with dissolve

    t "Why doesn’t it have any effect?"
    t "Did I get the spell wrong?"
    s "There’s no spell to begin with..."

    scene tsuneyodormten20
    with dissolve

    t "Are you immune?!"
    s "I can’t tell if you’re joking right now or not."
    t "Who would joke at a time like this?! My magic is gone!"
    t "It was technically never there to begin with, but now it’s REALLY not there!"
    s "You’re spending way too much time with Molly."
    s "Put your hands down. I’m not going to hurt you."

    scene tsuneyodormten17
    with dissolve

    t "Mm..."
    s "I’ll also give you a little tip to prevent you from misfiring your spells if something like this ever comes up again, which I can guarantee it will."

    if bonus == True:
        s "Pretty much every male you have ever talked to is a pervert in some sense of the word."
    else:
        s "{i}All of the Pokemon are actually real.{/i}"

    scene tsuneyodormten21
    with dissolve

    t "All of them?!"
    s "Yup. Even your father, most likely."

    if bonus == False:
        t "He, too, is a Pokemon?!"
        s "Dark type."

    scene tsuneyodormten22
    with dissolve

    t "Then the Emerald Guardian was correct when she told me that girls are the ones I want to ally with."
    s "I mean, it’s not like there are that many men around anymore to begin with. "
    s "If you wanted to form an army of all women, I’m pretty sure you could take us down in a moment’s notice."
    t "…"
    s "…"

    scene tsuneyodormten23
    with dissolve

    t "You are absolutely correct."
    t "I’m beginning to question why I was so afraid in the first place."
    t "Men are weak."
    t "I will eliminate all of them."
    s "...All of them?"
    t "Except my father. I can not afford to live on my own yet."
    t "And his days are numbered anyway."
    s "That’s...incredibly morbid."
    t "As are all things, Sensei."

    scene tsuneyodormten24
    with dissolve

    t "Wherever there are perverts...The Samurai of Flavor will be there to cut them down."
    s "…"
    t "Wherever there is injustice...The Soup Warrior will be there to restore order."
    s "Okay Tsuneyo, I-"

    scene tsuneyodormten25
    with dissolve

    t "Wherever there are noodles...Tsuneyo Tojo will be there to eat them!"
    s "Okay, that one wasn’t inspiring in the slightest."
    t "I am hungry!"
    s "I...can see that."

    scene tsuneyodormten26
    with dissolve

    t "If we are going to be hanging out tonight, would you like to come with me to the convenience store?"
    s "Right now? It’s the middle of the night."
    t "Is that not the ideal time to go?"
    t "The Emerald Guardian recently introduced me to all of these 24-hour stores and I can feel my life changing every day."
    s "You...didn’t know about convenience stores?"
    t "I’ve only just been granted permission to leave the house."
    t "The entire world is new to me."

    "The entire world?"
    "That can’t be true, can it?"
    "Tsuneyo’s a [teenage]girl. The chances of her being cooped up in the same house for her entire life are slim to none."
    "And why now of all times?"
    "Why would she suddenly be allowed to start “living her life” in the middle of the[school] year?"
    "I imagine her father’s condition has something to do with it, but..."

    t "Sensei?"
    t "Food. Please."
    s "Oh, yeah. Sure. I’ll come with you."

    scene tsuneyodormten14
    with dissolve

    t "This is good news."
    s "Oh yeah? Because you want to spend more time with me?"

    scene tsuneyodormten13
    with dissolve

    t "No. Because now I won’t get lost."
    s "…"
    t "…"

    scene tsuneyodormten15
    with dissolve

    t "Heh..."

    scene black
    with dissolve2

    "Tsuneyo makes me leave the room so she can get dressed and I wind up standing in the barren second floor hallway for a minute or two before she finally comes back."
    "The two of us walk to the convenience store, where she proceeds to stock up on roughly ten different brands of instant ramen, before we decide to separate and head back to our respective homes."
    "It isn’t until ten minutes after we part ways that I realize there is a good chance that she wound up getting lost on the way back."
    "…"
    "Whoops."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm10 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm15:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label tsuneyodorm:
    if tsuneyo_love >= 5 and ramen1 == True and tsuneyofirsthall == True and tsuneyodorm5 == False:
        jump tsuneyodorm5
    if tsuneyo_love >= 10 and ramen10 == True and tsuneyodorm5 == True and tsuneyodorm10 == False:
        jump tsuneyodorm10
...
```