# NTR & Pregnancy
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe1&go=Go)



## Event preconditions
✅Molly love greater than or equal to 0

✅Event "[Main: Lifting the Curse](./day154.md)" is completed (event=day154)



## Next events
* [Molly: Remnants of Forgotten Memes](./mollycafe5.md)
* [Molly: Torrent of Power](./mollydorm5.md)
* [Maki: Beautiful Porn Salesman](./makidate1.md)
* [Karin: If Only](./karindate10.md)

## Event properties
* ID: mollycafe1
* Group: Molly
* Triggered by label: mollycafe
* Triggered by branch label: mollycafe

## Event code
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe1:
    scene cafe_night
    with dissolve
    play music "cafe.mp3"

    "I decide to check out the cafe at night for once."
    "I’ve known that they’re open later than just mornings for quite a while, but I guess I really haven’t had any reason to go knowing that Rin wouldn't be working."
    "But hey, this is a cafe."
    "I’m sure there’s bound to be another overly-perky, slightly-weird girl behind the counter no matter what."

    scene mollycafe1
    with dissolve

    mo "Greeting and salutations, Supreme Overlord!"
    s "Oh, right. You work here."
    mo "I do! Though, some of my co-workers may disagree with that statement!"
    mo "What can I get for you today, Sir? A cappuccino? Double espresso? Or perhaps..."

    scene mollycafe2
    with dissolve

    mo "DESTRUCTION?!"
    s "Yes, Molly. One order of destruction."
    mo "Small, medium, or THE GATES OF HELL?"
    s "How much coffee have you had to drink tonight?"

    scene mollycafe3
    with dissolve

    mo "I CAN’T EVEN FEEL MY HANDS ANYMORE!"

    "I guess it’s not surprising that Molly works here..."
    "Her and Rin seem like pretty good friends, so I’m sure that them being together all the time has something to do with that."
    "Still, though...why did Haruka hire {i}Molly{/i} of all people? Isn’t she a little too...{i}everything{/i} for this place?"

    s "Molly, just out of curiosity, how do you still have a job?"

    scene mollycafe4
    with dissolve

    mo "That question would be better answered by the Magistrate of Mammaries, Sir. Though, I'm sure Rin has something to do with it."
    mo "I'm sure it helps that I only work nights now and no one has to deal with me directly anymore."
    mo "I'm surprised to see you here so late, though. I was under the impression you only showed up in the mornings- and quite often at that!"
    s "How exactly do you know about how often I come here if you don't directly work with Haruka or Rin anymore?"

    scene mollycafe5
    with dissolve

    mo "I may have mentioned something along the lines of a...contract with a new master in our group chat. Which then evolved into a conversation about you. "

    "Oh, good. A private group chat where three girls I see on a near daily basis are free to gossip about me. That is exactly what I needed."

    s "I'm guessing that means Haruka knows you're in my class now?"
    mo "Well, I didn’t exactly word it like that, but yes. I believe that is the impression she got."

    scene mollycafe4
    with dissolve

    mo "Can I take this visit as an omen that you will be visiting me at night more often, Sir? "
    mo "Not that...you can visit me in the mornings on account of the whole {i}how hard I am to handle{/i} thing."
    s "To be completely honest, you don’t seem any easier to handle at night."
    mo "You’re just not a high enough level yet, Sir."
    mo "I can't be equipped until much later into the game."

    if bonus == True:
        s "I really hope that’s not foreshadowing."
        mo "I don’t...think it is?"
        mo "It's probably just gamer-brain, Sir. You know- like items, skill levels, party members...etcetera, etcetera."
        mo "Just assume that it's stuff you don’t care about that I am going to {i}make{/i} you care about."
    else:
        s "Stop hinting at a future for us. I am your teacher and that is disgusting."
        mo "I will make you mine through methods unknown to mere mortals."

    s "And how do you plan on doing that, exactly?"

    scene mollycafe5
    with dissolve

    mo "Mind control, perhaps? "
    mo "Or maybe I’ll just win you over with my feminine wiles?"
    s "What wiles? You haven’t done a single {i}feminine{/i} thing since I’ve met you."

    scene mollycafe1
    with dissolve

    mo "I don’t know! Foreigners are appealing to men, aren’t they?"
    mo "And now that we’re alone, I bet you’re thinking something like, “WOW, WHAT A CUTE GIRL” or whatever it is h-game protagonists think."
    s "Not really. I'm still stuck on trying to figure out why you haven't been fired yet."

    scene mollycafe6
    with dissolve

    mo "I’m plenty good at my job!"
    s "We've been talking for five minutes and you haven't even finished taking my order yet."
    mo "I just like talking and I’m excited to see my teacher after school!"
    mo "Ms. Watabe never came to the cafe! She always talked about how tea was better and that coffee was just hot bean water!"
    mo "And any time I tried to tell her we had tea as well, she told me to leave her alone and that she just wanted to die!"
    s "Huh. Coffee really is just hot bean water, isn't it?"

    scene mollycafe7
    with dissolve

    mo "Well...yes. I believe it is. But it’s good for other stuff too. Like when you need to stay up late....{i}studying{/i} and stuff."
    s "Molly, please don’t feel the need to pretend you study around me. I might be your teacher, but it’s not like I have any intention of-"
    s "Well, teaching."

    scene mollycafe2
    with dissolve

    mo "Fuck yeah!"
    mo "Ami was right when she said you were the best [uncle] in the world!"
    mo "Will you be my [uncle] too, Sir?"
    s "I don’t think that’s possible."
    mo "Then will you adopt me and become my new father?!"
    mo "I’m not good at cooking or cleaning, but I’m certain I would make decent company on a rainy day!"
    s "I'm not really looking to adopt right now. Nor do I think Ami would be okay with it."
    s "I know you guys are in the manga club together, but she hasn’t ever really talked about you before and I doubt she views you as a sister."

    scene mollycafe8
    with dissolve

    mo "Ami hasn't talked about me before?!"
    s "Is that really something to yell about?"
    mo "Of course! Ami is a loyal member of the Cult of Molly! "
    mo "We have plans to conquer the demon king and restore order to the forest one day!"
    s "You’re really going to need to learn to talk about things I actually understand if this relationship is ever going to work out."

    scene mollycafe9
    with dissolve

    mo "Oh ho ho ho~ So you accept my contract after all?"
    s "Contract? What contract?"
    mo "You just said we’re in a relationship. "
    mo "And even if it were a slip of the tongue, these are words that will greatly shape the rest of our time together, Supreme Overlord."
    mo "If Molly MacCormack is to become the lead heroine of this visual novel, hearing things like “relationship” only allude to its truth!"
    s "Just out of curiosity, you haven't heard anything about how much time I’ve spent with the other students, right?"
    s "Because you seem pretty dead-set on this whole heroine thing and I’m not quite sure if you fully understand what you're getting yourself into."
    mo "Oh ho ho~ You underestimate me, Sir."
    mo "I just so happen to be an expert in the world of dating sims. "
    s "But not...actual dating? Why choose to live a life like that when real humans exist?"

    scene mollycafe10
    with dissolve

    mo "You don’t choose 2D, Sir. 2D chooses you."

    scene mollycafe2
    with dissolve

    mo "But even if it didn’t, I would have wound up here eventually!"
    mo "There’s nothing quite like watching romance flourish from textbox to textbox. H-Scene to H-Scene!"
    s "Would you mind explaining to me what some of those things mean? Because I feel like I need to understand what an “H-Scene” is if I'm ever going to catch up with this conversation."

    scene mollycafe11
    with dissolve

    mo "The “H-Scene” is the holy grail of dating sims, Sir!"
    mo "The moment where two characters consummate their love for another in the form of...{i}you know what{/i}."
    s "…"
    mo "…"

    if bonus == True:
        s "You mean sex?"
    else:
        s "You mean by throwing peanuts at each other and pretending it was an accident?"

    scene mollycafe12
    with dissolve

    mo "..."
    mo "Yup!"
    s "So, let me get this straight-"
    s "You would willingly choose a life where the only physical contact you have with anyone is done through a computer screen with a fictional character?"

    scene mollycafe13
    with dissolve

    mo "..."
    s "..."
    mo "You don’t get it at all."
    mo "It’s not just about the physical part, Sir. "
    mo "It’s about the emotions leading up to it! The build-up! The will-they, won’t-they!"
    s "That exists in real life too, though."

    scene mollycafe14
    with dissolve

    mo "REAL LIFE IS STUPID! THERE’S NO BACKGROUND MUSIC OR TSUNDERE CHARACTERS! JUST NTR AND PREGNANCY!"
    s "And what is NTR exactly?..."
    mo "HORRIBLE! THAT’S WHAT!"

    "I can feel passion and anger beginning to exude from Molly’s being, turning the cafe roughly three degrees hotter."
    "And in other news, we are now roughly ten minutes into this and I still do not have a drink in my hands."

    s "Uhh, Molly."
    mo "What do you want?! I’m having a crisis and remembering a thing that happened in a game I played!"
    mo "NTR warnings should be mandatory! Not everyone is into that! It genuinely hurts some people!"
    s "Molly, I would like to order a drink now."

    scene mollycafe15
    with dissolve

    mo "Oh, right. I’m at work. "
    mo "What would you like? It’s on me today."
    s "Woah, really? Rin never offers to give me anything for free and I’ve been ordering from her for months."
    mo "Rin is much better at her job than I am."
    mo "It is not often I form connections with live males, so I must do everything in my power to keep this one going strong."

    if bonus == True:
        mo "Even if you are three times my age."
        s "Okay, come on. I’m definitely not three times your age."

        scene mollycafe16
        with dissolve

        mo "Okay! {i}Four{/i} times my age!"
        s "How old do you think I am?..."
        mo "Old enough that my father would disown me for becoming romantically involved with you!"
        s "Okay, fair point. Let’s avoid that for the indefinite future as I have no intention of literally ever meeting your father."
    else:
        s "The best course of action would be for me to meet your father and inform him that my intentions are nothing but pure."

    mo "That is fine with me, Sir!"
    mo "I believe it is customary for me to meet {i}your{/i} parents, though."
    mo "It would make for a heartwarming scene where I bond with your mother and cook dinner with her."
    s "That sounds...great. But I honestly don’t even know if my parents are still alive."

    scene mollycafe17
    with dissolve

    mo "Oh! Shoot. I’m sorry, Sir. I didn’t mean anything by it. I just got swept up in my-"
    s "It’s fine, Molly. Don’t beat yourself up over it. I really couldn’t care less, to be honest."

    scene mollycafe18
    with dissolve

    mo "But that’s so sad..."
    s "Yeah, that's life for you."
    s "We’re all going to die someday, so we might as well live it up while we can, right?"

    scene mollycafe19
    with dissolve

    mo "Master!"
    s "...What?"
    mo "Thank you!"
    s "What’s going on? Why are you thanking me?"
    mo "That was just the inspiration I needed to convince myself to level-cap my druid tonight!"
    s "Your...what?"
    mo "That doesn’t matter!"
    mo "Just know that I greatly appreciate it!"
    s "Okay, but can I-"
    mo "Coffee! Yes! I will infuse it with a special buff just for you as well!"
    s "I’m not really a fan of sugar-"

    scene mollycafe3
    with dissolve

    mo "ONE MOLLY-SPECIAL, COMING RIGHT UP!"

    scene black
    with dissolve2

    "As it turns out, it isn’t just Rin who vehemently refuses to make anything that is actually on the menu here."
    "The only difference is that Rin’s custom drinks are actually fit for human consumption."
    "And I’m pretty sure that whatever Molly winds up making for me contains cocaine, because I wind up walking home with my hands shaking uncontrollably after just one sip..."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe1 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "........."
    "......"
    "... "

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe5:
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
...
```