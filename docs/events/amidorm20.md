# Divergence (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 20

* Day of week is not Monday

* Day of week is not Friday

* Event [Cute Girls and Stuff](./amisroom20.md) (Ami) is completed)



## Next events

* [Ami: Such Small Hands](./amisroom25.md)
* [Ami: Everlasting Love](./amidorm25.md)

## Event properties

* Id: amidorm20
* Group: Ami
* Triggered by label: amidorm
* Triggered by branch label: amidorm
* Triggered by path: amidorm->amidorm20

## Official wiki page

[Divergence](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidorm20&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm20:
    scene amimayamaid1
    with dissolve
    play sound "knock.mp3"

    "I walk up to Ami’s door and knock on it."
    "It’s surprisingly nice outside tonight so I figure it might be a good chance to check out that maid cafe we talked about during our trip to the mall recently."

    a "One sec! Coming!"
    m "I recognize that knock. Why is he here?"
    a "Shh. He can hear you through the door, Maya!"
    m "Oh, my mistake. I’ll ask him directly."
    a "What? N-"
    m "Sensei, why are you here?"

    play sound "dooropen.mp3"

    scene amimayamaid2
    with dissolve

    s "Oh, Maya’s here too."
    m "I live here."
    a "Hey! What’s up? You’re here to see me, right?"
    a "Did you need something?"
    a "Maya and I were about to head over to the maid cafe if you want to tag along."
    m "Or you can not tag along. That works just as well."
    s "I was actually going to suggest going over there tonight. What a fortunate coincidence this is."
    m "Yes, how fortunate indeed. "
    m "I’m practically jumping for joy."
    a "Sorry, Sensei. Maya has been in a bad mood all day for some reason."
    a "She’s probably just hungry. She gets like that sometimes when she hasn’t eaten for a while."

    scene amimayamaid3
    with dissolve

    m "I’m annoyed by how true that is. But yes, I require food immediately or I am probably going to kill someone. "
    s "Not it. Take Ami instead."

    scene amimayamaid4
    with dissolve

    a "What?! Why are you willing to sacrifice me so easily?!"
    m "Understood. She would be easier to kill anyway. "
    m "As much as I hate to say it, you’re obnoxiously tall and I’d probably have trouble taking you down."
    s "Just make sure that you kill her {i}at{/i} the cafe so you can have her body flavor beamed before the funeral."
    a "I don’t want to be flavor beamed! I just want a job!"

    scene amimayamaid5
    with dissolve

    m "Well then we should probably be leaving, shouldn’t we?"
    m "Unless you want to just pick something up for me. That works too."
    m "Hold the flavor beam, please. I don’t think it has any real effect. "
    s "I’ll take Maya’s flavor beam."

    scene amimayamaid6
    with dissolve

    a "I’m annoyed that you even know what the flavor beam is."
    a "I knew you liked maids but I didn’t think you liked that part of them too."
    a "Am I going to have to flavor beam all of your food at home from now on?"
    s "That won’t be necessary. I’ll just ask Uta-chan for her number and have her come over and do it."

    scene amimayamaid7
    with dissolve

    a "Over my dead body..."

    scene black
    with dissolve2
    stop music fadeout 5.0

    "The three of us make our way out of the dorm shortly after Ami tells Maya she doesn’t want to be bothered carrying food all the way home."
    "I think it’s a little rude when I first hear it and even go as far as almost offering to carry it myself-"
    "But then I remember exactly how much Maya is able to eat and decide against it considering that I’d likely need to rent a forklift in order to get all of it back to her."
    "………"
    "……"
    "…"
    "{i}Some time later...{/i}"

    scene amimayamaid8
    with dissolve
    play music "shiningstarinstrumental.mp3" fadein 8.0

    a "Huh...There’s no one here."
    m "That’s usually how it works. You should know this by now."
    m "Someone will show up soon enough."
    a "Maybe it would be better if we just came at a different time? Isn’t it kind of rude to apply somewhere in the middle of the night?"
    s "Chickening out already? You haven’t even talked to anyone yet."
    m "Chicken sounds good. Thank you for the suggestion."

    scene amimayamaid9
    with dissolve

    a "I’m not being a chicken! I just feel really jittery all of a sudden. My legs feel all wobbly and my tummy is doing cartwheels."
    a "Is this what cancer is, Sensei? Do I have cancer?"
    s "What? No."
    s "Why would you even assume that?"

    scene amimayamaid10
    with dissolve

    a "Ahhhh I’m not even wearing a suit!"
    s "You don’t even own a suit."
    m "Do they even have chicken here? They have to, right?"
    u "Ahh! Customers!"
    u "I’ll be right with you, masters! I’ve just...gotta..."
    u "…"
    u "OH NO!"

    play sound "dishes.mp3"
    with hpunch

    "The sounds of glassware shattering in the kitchen echo throughout the room but neither Ami nor Maya react."
    "I guess this sort of thing happens often enough for them to just...shrug it off?"

    scene amimayamaid11
    with dissolve

    u "Ah! Master! You’ve returned!"
    s "What just happened in the-"
    u "Nothing! Don’t mind that."
    u "Here I was thinkin’ you’d take the next trillion years finishing all of those cakes you bought from me last time you were here."
    s "There is no amount of cakes that can keep me away from you, Uta-chan."

    scene amimayamaid12
    with dissolve

    m "Uhh, ew."
    a "Excuse me? What did you just say to Uta-chan, Sensei?"
    u "Awww, stop! You don’t mean that~"
    u "Either way, I’m really happy you came back to see me, Master! Is there anything I can get for you tonight?"

    scene amimayamaid13
    with dissolve

    u "You’ve gotta remember, though, I’m not on the menu~"
    s "One of everything please."
    a "This is why you have no money to buy me things?! Because you spend all of it on Uta-chan?!"
    s "Don’t mind her, Uta-chan. That’s just my [niece]."

    scene amimayamaid14
    with dissolve

    u "Princess Ami is your [niece]? That’s so cool! You two look nothing alike!"

    if bonus == True:
        u "It's so cute that you two hang out together!"
        u "If anything, I would have thought you were here with-"
    else:
        s "I don't think you understand what an accountant is, Uta."
        u "(Airplane noises)"

    scene amimayamaid15
    with dissolve

    s "Wait. Hold on a second. "

    "I step closer to Uta and cover my mouth with the side of my hand so Ami can’t see what I’m saying."
    "I notice her clenching a fist out of the corner of my eye so I do my best to keep what I have to say short."

    s "{i}Don’t say that I was here with Maya last time. Ami will get jealous.{/i}"
    u "…"

    scene amimayamaid16
    with dissolve

    u "Ohohohoh..."
    u "I see. I see."

    scene amimayamaid17
    with dissolve

    if bonus == True:
        u "That’s really naughty, Master. "
        u "A secret relationship with a girl that much smaller than you?"
        u "Is that what you’re trying to get out of Uta-chan as well?"
        s "That’s not exactly what was happening last time."
        u "Right, right. And I’m not exactly a maid~"
        u "Your secret’s safe with me, Master. I won’t tell a soul as long as you promise to come see me again~"
        s "I will literally live here if you let me."
        a "I’m trying really hard to not freak out on you two right now and you’re making it quite difficult."
        s "Oh. Right."
        s "Uta-chan, Ami had something she wanted to talk to you about."
    else:
        u "So Maya is planning on opening a rival accounting firm?"
        s "Exactly. Ami can't know."
        u "Don't worry, Master. Uta-chan has your back."

    scene amimayamaid18
    with dissolve

    u "Princess Ami had something she wanted to talk to {i}me{/i} about? I wonder what it could be?"
    a "Oh, umm...Yeah."
    a "Uhhh. Hi."
    u "Hi~"
    a "I...uhh..."
    s "She wants a job."

    scene amimayamaid19
    with dissolve

    a "I was getting there!"

    scene amimayamaid20
    with dissolve

    u "A job? Here? With me?"
    u "OHMYGOD! That sounds so fun!"
    u "Come talk to me on the couch for a little while. "
    u "I’m not really able to hire you myself, but I can definitely put a good word in for you since I know you so well!"
    s "I didn’t realize you two were on such good terms, Ami."

    scene amimayamaid19
    with dissolve

    a "Well...Like I said, Maya and I come here sometimes. And Uta-chan is pretty much always here, so."
    u "Princess! Couch! Now! Come!"

    scene amimayamaid21
    with dissolve

    a "Ah! Yes! Sorry!"

    scene black
    with dissolve

    "Uta pulls Ami to the side and begins asking her a ton of questions I can’t be bothered to follow along with. "
    "I should have probably coached Ami on how to properly conduct herself in an interview beforehand but...eh."
    "She’s smart enough to figure it out and it’s not like wearing a dress and calling people “Master” is a particularly hard job. "
    "She’ll be fine. I know she will."

    scene amimayamaid22
    with dissolve

    m "Are you sure about this?"
    s "Sure about what? Ami getting a job?"
    s "It was her idea."
    s "Well, kind of."
    s "I didn’t really expect her to follow through with it, but she’s free to do what she wants."
    s "Is there something wrong with that?"
    m "It’s just not something that’s ever happened before."
    m "I doubt something this small would have any effect on the world itself, but it’s still weird."
    s "You’re not going to start talking about that butterfly effect thing, are you?"
    m "I was going to, but I can just...not do that if you already know what it is."
    s "It’s that thing about how a butterfly flapping its wings could...you know. Tornadoes and stuff."
    m "…"
    s "…"
    m "Well that’s definitely one way to put it."
    m "I’m honestly more concerned about why you’re so open to this if you’re just going to-"

    scene amimayamaid23
    with dissolve

    if bonus == True:
        m "Wait...You’re not just doing this because you want to see her in the costume, are you?"
        s "Not {i}entirely{/i}..."
        m "She’s your [niece]..."
        s "Is she really, though?"
        m "You’re disgusting."
        s "Yes I am, Maya. Yes I am."
    else:
        m "Wait..."
        m "You just want to wear the costume, don't you?"
        s "..."
        m "You’re disgusting."
        s "Yes I am, Maya. Yes I am."

    scene black
    with dissolve

    "{i}Meanwhile...{/i}"

    scene amimayamaid24
    with dissolve

    u "So, you really wanna work here? "
    u "Like, really really REALLY {i}really{/i} wanna work here?"
    a "I kind of just...want some spending money. And to see Sensei more, if I’m being totally honest."

    scene amimayamaid25
    with dissolve

    u "You mean your [uncle]? You call him Sensei?"
    u "That’s kinda weird."
    a "Well, he’s also my teacher. So it’s...less weird."
    u "Still weird, though."
    a "Yeah...I try not to think too much about it."

    scene amimayamaid26
    with dissolve

    u "Why do you think working here will help you see him more, though?"
    u "I’m pretty sure he’s only shown up the one time."
    u "I mean, he did buy like, every single cake we had when he was here. But yeah."
    u "You’d probably see him more if you just stayed at home."

    scene amimayamaid27
    with dissolve

    u "Ah! Not saying I don’t think you should work here or anything!"
    u "You’d fit right in with how cute you are. And besides, we don’t have anybody with twintails on the staff and that’s like, only one of the most fetishy hairstyles out there."
    a "Has Sensei really only come here once?"
    a "When we talked earlier, he made it sound like he basically lived here."
    u "You sure that wasn’t just you jumping to conclusions?"

    scene amimayamaid28
    with dissolve

    u "Besides, even if he {i}was{/i} addicted to this place, it’s not like it would be weird or anything."
    u "Everybody loves maids. And he’s a boy so you can’t even hold that against him."
    a "Well...I guess that’s true."
    a "I don’t know. It’s just kind of strange thinking about how I wound up here in the first place."
    a "Like, just this morning, I was making breakfast for him and thinking of how nice it would be to just...keep doing that for the rest of eternity."

    scene amimayamaid29
    with dissolve

    u "Aww~ You really love him, don’t you?"

    if bonus == True:
        a "Of course. He’s the only family I have."
    else:
        a "Of course. He’s the only client I have."

    u "I get that. I moved here two years ago and the rest of my family is still in Nara. It gets really lonely sometimes."

    scene amimayamaid30
    with dissolve

    a "Nara?! Isn’t that the place with all of the deer?!"
    u "Yup! There was actually a whole family of deer that lived in our backyard."
    u "They were super cute until my big brother just shot them all one day."

    scene amimayamaid31
    with dissolve

    u "They were a lot less cute after that. "
    u "Really tasty, though."
    a "What?..."
    a "Where did he even get a gun?..."
    u "Idunno. He’s in jail now so I can’t really ask. My parents might know, though."
    a "What did this conversation turn into?..."
    u "Who knows?"
    u "But anyway, I’ll put in a good word for ya. "
    u "I’m not gonna make you fill out an application or any of that boring stuff."

    scene amimayamaid32
    with dissolve

    u "I’ll make sure you get hired, too, so we can take this friendship to the next level!"
    u "You’ll have fun here. I know it."
    u "And just in case you’re having any doubts, I’ll even let you take one of my costumes home to try on!"
    u "I swear you’ll be even more excited to work once you see yourself in it."

    scene amimayamaid33
    with dissolve

    a "That’s really nice of you, but..."

    if bonus == True:
        a "Do you have any costumes for girls that are still...growing?"
        u "Hm?"
        a "…"
        u "…"

        scene amimayamaid34
        with dissolve

        u "Oooooohhhh...I get it. You mean boobs."
        u "Yeah. I’ll look."
        u "Don’t worry, Ami. We’ll get through this together."
        a "Life is miserable..."
    else:
        a "Do you have any costumes for girls that have detachable arms?"
        u "..."
        a "..."
        u "..."
        a "..."
        u "..."
        a "..."

    scene black
    with dissolve2

    "Ami returns to the table Maya and I had taken a seat at several minutes later with a look of dejection spreading across her face."
    "I figure it’s due to not getting the job or something like that, but I'm quickly informed that she’ll be starting soon and that the look is due to something else."
    "It’s actually kind of similar to the look Maya’s had ever since she realized she was going to need to wait before ordering her food."
    "Either way, I’m glad things ended up well for Ami."
    "I just hope I can see her in the outfit soon."

    $ renpy.end_replay()
    $ amidorm20 = True
    $ ami_love += 1
    stop music fadeout 5.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amidorm25:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
            if ami_love >= 10 and day > 5 and day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True:
                jump amidorm10
            if ami_love >= 15 and amidorm10 == True and mayadorm5 == True and amidorm15 == False:
                jump amidorm15
            if ami_love >= 20 and day != 1 and day != 5 and amisroom20 == True and amidorm20 == False:
                jump amidorm20
...
```