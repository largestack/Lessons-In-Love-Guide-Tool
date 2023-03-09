# Onward to Valhalla
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe15&go=Go)



## Event preconditions
✅Molly love greater than or equal to 15

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
* [Molly: The Legacy of Thaum Pt. II](./mollycafe20.md)

## Event properties
* ID: mollycafe15
* Group: Molly
* Triggered by label: mollycafe
* Triggered by branch label: mollycafe

## Event code
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe15:
    scene mollyoutside1
    with dissolve
    play music "molly.mp3"

    "It’s a cold winter night, as is customary for...winter."
    "Let me start over."
    "That was a horrible introduction to my nightly activities."
    "I make my way to the cafe to see what Molly is up to because I guess I’m in the mood to be confused tonight or something."
    "I suppose I just subconsciously enjoy spending time with her despite being at a complete disadvantage in around 100%% of our conversations."
    "Hell, I can’t even say something like “At least she’s fun” because, frankly, I don’t really {i}know{/i} how I feel around her."
    "Unique is a better word than fun, in her case."
    "But, then again, unique is the catch-all word you use to describe people that don't fit in. "
    "People with unclear sets of circumstances and ideals that have equally unclear outlooks on what people should enjoy or despise."
    "Unique used to be a bad character trait."
    "People used to be made fun of for not conforming."
    "But now it’s a sort of goal."
    "A finicky goal, but a goal nonetheless. "
    "You want to be unique, but not {i}so{/i} unique that you scare people away."
    "I think this is what Molly struggles with."
    "She hasn’t managed to scare me away yet, but she also seems to enjoy my class a lot more than her last one."
    "I wonder if they thought she may have been a little too unique as well?"
    "Probably."
    "But, somehow or another, her existence was enough to compel me to come here, of all places, in the middle of the night."
    "The middle of this cold, winter night."
    "As is customary for winter."

    scene mollyoutside2
    with fade

    "I find her seated outside of the cafe under the glow of a streetlight, closing her eyes and waiting for her coffee to cool off."
    "It’s rare seeing her without a fiery glare of determination or fists clenched out of passion for some...anime character or...paladin or other things she’s brought up throughout our brief time together."
    "And, strangely enough, despite being stripped of all of those qualities you can easily melt into her industrial grade pot of uniqueness-"
    "She looks more natural than ever."

    mo "Have you blessed yourself tonight, Sir?"
    s "Oh. You knew I was here."
    mo "You have a distinct aura that only someone with my affinity for holy magic is able to sense."
    s "Does that holy aura or whatever have something to do with you asking if I’ve blessed myself?"
    mo "Nay."
    mo "I ask because the moon is but a child."
    mo "Have you looked up at all in the last several hours, Sir?"
    s "...Probably?"
    s "That’s not something I normally keep track of."

    scene mollyoutside3
    with dissolve

    mo "There’s an old Irish superstition that says if you don’t bless yourself whenever you see a new moon, bad luck is sure to befall you."
    mo "But of course, it’s just a superstition...and those aren’t always true."

    scene mollyoutside4
    with dissolve

    mo "For example, I didn’t even drop a fork today and you still showed up."
    s "Ireland is weird."
    mo "Of course, Sir. What other country could have possibly birthed a girl like me?"
    s "I take it this weather is fine for you as well, then?"
    mo "Are you struggling with the cold, Sir?"

    if bonus == True:
        mo "Come! Embrace me! Share in my warmth!"
    else:
        s "Yeah, but I'm a big crybaby, so you can just ignore me."

    scene mollyoutside5
    with dissolve

    if bonus == True:
        mo "But yes. I actually think it’s rather nice tonight."
    else:
        mo "I actually think it’s rather nice tonight."

    mo "The perfect temperature to go on an adventure, even."
    mo "Unfortunately, my legs are far too weak and my body far too frail to embark on such a thing."
    mo "I shall confine myself to this bench instead, waiting patiently for my true love to return to me."
    s "And your true love is?"

    scene mollyoutside6
    with dissolve

    mo "Kagome Higurashi..."
    mo "But she is a story for another day..."
    s "Anime character, I’m guessing?"

    scene mollyoutside7
    with dissolve

    mo "I refuse to believe that it’s possible to have a first love who {i}isn’t{/i} some type of cartoon character."
    mo "Weren’t you particularly fond of a certain sailor scout, Sir? That’s what Ami claims, at least."
    s "Hey, Molly. Here’s an idea-"
    s "How about we talk about normal human stuff tonight instead of...whatever {i}you're{/i} talking about."

    scene mollyoutside8
    with dissolve

    mo "But I already used up all of my human knowledge when I told you about new moons and forks."
    s "Why is your human knowledge limited to such strangely specific things?"
    mo "Because I wiped everything else clear to make room for more otaku stuff. "
    mo "Besides, every conversation I’ve ever tried to have about life with Japanese people has fallen even flatter than my chest."
    s "That sounds pretty bad."

    if bonus == True:
        mo "It is, Sir. I am very much banking on you being a lolicon."

    s "Without divulging any additional information about my feelings on that matter, what’s so different about Japanese people compared to the Irish?"

    scene mollyoutside9
    with dissolve

    mo "Are you truly asking that?"
    mo "That’s like asking about the difference between a warlock and mage."
    s "Are those not the same thing?"

    scene mollyoutside10
    with dissolve

    mo "No! Not even close! I’m offended that you’d even say something like that!"
    mo "Mages are masters of the arcane arts and stupid warlocks get all their stupid powers from a stupid god! It’s barely even magic!"
    s "Maybe you should drink your coffee, Molly. "
    s "Isn’t caffeine good at helping people with...ADHD or whatever?"

    scene mollyoutside11
    with dissolve

    mo "I have also heard that. But you can't just go around bringing up people's conditions like that, Sir."
    mo "You’re going to hurt someone’s feelings that way."

    scene mollyoutside12
    with dissolve

    mo "However!"
    mo "I have become excellent at shielding myself from what {i}actual{/i} humans say!"
    mo "I will be completely fine as long as I don’t read it through a textbox on the bottom third of my computer screen!"
    mo "And since the night is just as [young]as the moon above, I suppose I wouldn’t mind educating you on what makes people like me different from people like you."
    mo "And I’m not just talking about our celestial affinities! Hahahahaha!"
    s "Haha..."

    "Our celestial what?"

    scene mollyoutside13
    with dissolve

    mo "What is the first thing that comes to your mind when you think of Ireland, Sir?"
    mo "I’d be willing to wager that it’s either potatoes or alcohol, am I correct?"
    s "Hey, you said it. Not me."
    mo "The fact of the matter is, there are stereotypes."
    mo "And being a girl implanted from another country, and one who was dedicated enough to learn the language and culture for the sake of my hobbies-"
    s "I’m definitely impressed by that, by the way. I’m not sure if I’ve told you that before."

    scene mollyoutside14
    with dissolve

    mo "Ah-"
    mo "Well, umm...Thank you, Sir."
    mo "But...umm..."

    scene mollyoutside15
    with dissolve

    mo "Like I was saying, there are a bunch of other stereotypes or...stuff people expect that just isn’t always true."
    mo "Like how the Irish are all liars or that they’re violent and...don’t have access to Internet or television."
    mo "You never really understand what people think about you until you go somewhere you don’t fit in."
    mo "But, at the same time, stereotypes exist for reasons and they don’t just come out of nowhere."

    scene mollyoutside16
    with dissolve

    mo "Like...like goblins! Or dwarves!"
    mo "What do you think of when you hear those things, Sir?!"
    s "That they’re short."

    scene mollyoutside17
    with dissolve

    mo "Oh."
    mo "Well, yeah. That’s true."
    mo "But anyone with even mild exposure to fantasy would say things like goblins are greedy and dwarves are masculine and spend all their time blacksmithing."
    mo "Point is, people like me are just like dwarves or goblins in a place like this."
    mo "I was raised a certain way and grew up surrounded by cultures and traditions that wouldn’t make sense here."
    mo "I still have a hard time remembering to take my shoes off inside or how I'm supposed to call out to servers at restaurants."
    mo "And if you threw a Japanese person into the Emerald Isle, they’d feel just as out of place."
    mo "The fact that I speak in...constant reference to things that even most Japanese don’t understand just makes things even harder for me."
    mo "If life’s a game, I’m basically playing on the hardest difficulty right now."
    mo "Like Ornstein & Smough, except there are two Ornsteins and five Smoughs."
    s "Are those...anime characters as well?"

    scene mollyoutside18
    with dissolve

    mo "You have...so much to learn, Sir."
    mo "So much to learn."
    s "Apparently so."
    s "I can’t really attest to what it must be like being “implanted” here, like you put it-"
    s "But even though you’re weird and draw way too much attention to yourself and talk too loudly pretty much all the time-"
    mo "Are you just...going to keep listing the things you don’t like about me?"
    s "And you always cause a commotion in class and never make me any of the things I order inside of the cafe and-"

    scene mollyoutside19
    with dissolve

    mo "When does it end?!"
    s "And all of the other things I find annoying about you-"
    mo "AHHHHHHHHH!"
    s "I think you’re doing great."
    mo "AHHHHH FINE, I’LL TRY TO CUT DOWN ON-"

    scene mollyoutside20
    with dissolve

    mo "Wait, repeat that last part. I was so torn up inside that I drowned it out with my fury."
    s "I think you’re doing great."
    s "I mean, my life was a lot easier before you showed up, but it’s not like I’d get rid of you if I had the choice now."
    s "So yeah, we’re different. Complete opposites even, but-"
    mo "But opposites attract..."
    s "Yeah. That."

    scene mollyoutside21
    with dissolve

    mo "Am I..."
    mo "Am I on the Sensei route already?!"
    mo "Are you in love with me?!"
    s "…"
    mo "…"
    s "I’m not in love with you."

    scene mollyoutside22
    with dissolve

    mo "Oh."
    mo "F’s in chat for the Irish girl. Please and thank you."
    s "Just because I’m not in love with you doesn’t mean I don’t want to spend more time with you, though."
    s "It’s a cold winter night and, instead of going inside and getting a hot beverage, I’ve stayed out here talking about Irish stereotypes and...warlocks."

    scene mollyoutside23
    with dissolve

    mo "If you’re not in love with me, can you stop saying things that will cause my puny gamer brain to think you are?"
    mo "This isn’t the bad end, is it? "
    mo "Is this what the friend zone feels like?"
    mo "You never even turned in your Cult of Molly paperwork so I can’t even contractually bind you to me as a servant."
    mo "Also, don’t get me started on warlocks. I could go on for hours."
    mo "Oh, and if you actually {i}do{/i} want a drink, allow me to purchase it for you so I can use my super awesome employee discount that definitely wasn’t the main selling point to me applying here."
    s "Sure. We'll go in in a few minutes."
    s "Actually, why are you out here anyway? Aren’t you supposed to be working right now?"
    s "It looks kind of busy in there tonight."

    scene mollyoutside24
    with dissolve

    mo "Hohohoho~ I am out here precisely {i}because{/i} it is busy, Sir."
    mo "Do you truly think someone like me is fit to serve that many customers while the owner herself is working?"
    mo "I would just ruin everything."
    s "You seem awfully proud to be bad at your job."

    scene mollyoutside25
    with dissolve

    mo "I learned from the best."
    mo "There’s this one teacher I have who is utterly horrible at his job and still manages to make the lives of everyone he knows marginally better."

    "Easier, sure. Better? No."
    "That’s just not true."

    mo "So if I, too, can make everyone’s lives better by never improving, I am ready to lay down my sword and surrender as well."
    mo "Onward to Valhalla, Sensei."
    mo "You, me, and our unearthly desire to be lazy!"
    s "…"

    "Oh my god."
    "Am I also a Molly?"

    s "I feel kind of sick all of a sudden."
    mo "That’s not illness, Sir. It’s {i}revelation{/i}."

    scene mollyoutside26
    with dissolve

    mo "Lay down your weapon! Shelve your armor!"
    mo "Today, our battle ends! But our war begins!"
    mo "For freedom! For love!"
    mo "For Ireland!"
    s "…"

    scene black
    with dissolve2

    "Molly and I wind up going inside and taking advantage of her employee discount shortly after that."
    "I order a drink directly from Haruka, who places her hand on my shoulder in a show of solidarity for my valiant sacrifice (AKA: spending time with Molly)."
    "But, even if I joke-"
    "It isn’t much of a sacrifice."
    "I mentioned earlier that I wouldn't describe her as “fun.”"
    "And, in doing that, I was wrong."
    "She {i}is{/i} fun."
    "Just..."
    "Not the type of fun I’m used to."
    "And she’s unique as well."
    "Just..."
    "Not the type that’s entirely bad."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe15 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe20:
...
```

## Code that triggers this event
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe:
    if molly_love >= 0 and mollycafe1 == False:
        jump mollycafe1
    if molly_love >= 5 and mollycafe1 == True and mollycafe5 == False:
        jump mollycafe5
    if molly_love >= 10 and mollycafe5 == True and mollydorm5 == True and mollycafe10 == False:
        jump mollycafe10
    if molly_love >= 15 and christmas7 == True and mollycafe15 == False:
        jump mollycafe15
...
```