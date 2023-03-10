# Dodging Snowflakes (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Room to Grow](./christmastwo3.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo4
* Group: Main
* Triggered by label: christmastwo3
* Chain sources: christmastwo3
* Chain sources path: christmastwo3

## Official wiki page

[Dodging Snowflakes](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo4&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo4:
    scene wintersky
    with dissolve2
    play music "justlights.mp3"

    "The work week comes to a close, but not without reminding me one final time on my way out of the building that, at least for a little while longer, I’m going to have to keep dealing with snow."
    "You know, when winter first began, I didn’t really expect to come to hate it as much as I have. "
    "But I guess it’s kind of inevitable that you'll wind up hating something when you’re both surrounded and inconvenienced by it multiple times a week."
    "Obviously there are exceptions to that rule- like the one with red hair who makes me breakfast every morning."

    if ayanelust20 == True and bonus == True:
        "Or the blonde one that I came inside of earlier today."

    "But {i}most{/i} things are only good in moderation, so I think I should be forgiven for suddenly wanting something other than the thing I wanted originally."
    "And, soon enough, I’m sure I’ll be silently complaining about the heat again instead."
    "But at least then, I won’t be wet. "
    "I move through the streets in hope of maybe finding someone who can make my journey to the dorms a little less boring, but I left school late enough that the chances of that seem unlikely."
    "I probably could have asked Imani to come with me, but I think I could use a little break from her since she was the reason I had to stay late."
    "Apparently, just having a beautiful woman show up to teach my class in my stead isn’t as easy as it sounds."
    "But maybe this could be good for me?"

    if bonus == True:
        "Not in the fact that it will surely detract from the amount of time I’m able to focus on things like my seemingly indefinite life in Kumon-mi or the frequency of my masturbatorial habits-"
        "But in the fact that I’ll feel a little better about constantly dragging everyone down alongside me if they’re learning something during their descent."
        "Is that something I should have been able to accomplish on my own without the help of a student teacher? Yes."
        "But convincing myself to do anything when it’s as cold out as this is impossible."
        "And convincing myself to do anything when it’s warmer is just as hard."
    else:
        "I have been neglecting my duties as of late and I would love to get back to what I came here to do- teaching college girls and nothing else."

    scene black
    with dissolve2

    if bonus == True:
        "But what’s not hard is ignoring all of that and falling back into place."
        "I take a moment to dodge the shards of a shattered mirror falling from the sky disguised as snowflakes and, instead, let any chance of self-reflection be crushed beneath my feet."
        "After all, the school week is over."
        "Which means it’s time for me to return to the better part of my life."
        "The part where nothing can go wrong."
        "The part where I can do no wrong."
        "And so I make my way to a home away from home-"
    else:
        "Some other stuff happens and then I make it to the dorms."

    play sound "knock.mp3"

    "And find solace in one more place where I don’t have to dodge anything."

    i "Come in!"

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene dodgingsnowflakes1
    with dissolve2

    i "Uhh...surprise!"
    u "You know, I’ve been thinking. How did you even manage to make it this big? Like...where the heck did you have room to even build this?"
    s "Uhh...what is it?"

    scene dodgingsnowflakes2
    with dissolve

    i "Oh, you know. Just a...wardrobe...closet...thing..."
    s "Wow, how did you know that “wardrobe closet thing” was at the top of my Christmas list this year?"

    scene dodgingsnowflakes3
    with dissolve

    i "I know! I went totally overboard! But I felt weird about giving you two toys in a row when you’re an adult and...can probably benefit from additional storage space!"
    s "How am I even supposed to get this home?"
    u "I don’t know, but you better friggin’ figure it out because our room’s starting to get a little cramped."
    s "Starting?"

    scene dodgingsnowflakes4
    with dissolve

    i "I can...probably help carry it?"
    s "Sure. I’ll just carry a giant wardrobe across town with a girl who could probably get swept away by the wind at any given moment."
    u "How much does renting one of those moving van thingies cost? Maybe we could get one of those for a few hours."

    scene dodgingsnowflakes5
    with dissolve

    u "Oh! And then we could have a party at your place! And this time, we won’t let Noriko come so you can stay conscious for the whole thing!"
    i "I feel like I’m missing a very important detail here."
    s "Don’t worry about it, Io. And thank you for the...very large and random present."

    scene dodgingsnowflakes6
    with dissolve

    i "Do...you hate it?"
    s "I don’t hate it. I just have no idea where to put it. Or even what to put {i}in{/i} it."

    scene dodgingsnowflakes7
    with dissolve

    u "Don’t worry about that, Master! Every Ichimonji wardrobe is sized to perfectly fit Uta-chan for her new, traveling maid business!"
    u "Just bring me a drink of water and some pizza rolls every night and I can live in here for the rest of forever!"
    i "I don’t think Sensei wants to-"
    s "Sold. I’ll take ten."

    scene dodgingsnowflakes8
    with dissolve

    i "Ten?! "
    i "How am I going to get all of the materials for ten of these things? This wasn’t exactly easy to make."
    u "Shouldn’t you be a liiiiiittle more worried about where you’re gonna find nine other Utas?"

    scene dodgingsnowflakes9
    with dissolve

    i "Nah. I’ll just go back to our chat room thingy and see if there are any other girls with dying grandpas who can fit into small closets."
    i "That doesn’t sound that hard."
    u "Those poor grandpas..."
    s "Dying grandparents and chat rooms aside, I feel kind of bad now for not getting you anything. Especially when you made something as ridiculous as this."

    scene dodgingsnowflakes10
    with dissolve

    i "I don’t need anything from you, Sensei. Buying anything for me would just be a waste of money anyway. "
    s "It wouldn’t be a {i}waste{/i}, Io."
    i "No, no. It really would. Not just because I suck, but because all of the things I like can be found in dumpsters and discount warehouses and stuff. Material goods don’t really matter to me."
    s "That’s a weird thing for someone who makes material goods as a hobby to say."
    i "Okay, so maybe I didn’t word that correctly. But you should know by now that I am the human equivalent of a duffel bag full of contradictions."
    s "How can you have a human equivalent of an object that doesn’t actually exist?"

    scene dodgingsnowflakes11
    with dissolve

    i "Duffel bags are real, Sensei. Just because they’re full of something intangible doesn’t mean they don’t exist at all. It’s what’s outside that counts."
    s "I think that’s the opposite of how that phrase is supposed to work."

    scene dodgingsnowflakes12
    with dissolve

    i "Then...maybe the phrase needs to be changed?"
    s "I’m confused."
    i "In the future, if you ever want to give me a return present or anything like that, just give me a hug. I’ll always accept one of those from you."

    if bonus == False:
        s "=D !!!!!!!!!!!!!!!!!!!!!!!!"

    i "Which isn’t me insinuating that I want you to hug me right now. Even though I do. I just understand that you’re still probably put off by the fact that I made you something so large that-"
    u "Just fucking hug him, Io. "
    i "Can I? Please?"
    s "I don’t know. I still feel kind of put off by the fact that you made me something so large that-"

    scene dodgingsnowflakes13
    with dissolve

    u "Hug the Io, damn it!"
    u "Do you have any idea how much she busted her butt on this thing? The least you can do is give her some of that sweet, G-rated loving!"
    s "Okay, fine. Go."

    scene dodgingsnowflakes14
    with fade

    i "Woo! Hug-based victory! All of the calluses and splinters are suddenly worth it!"
    s "You should value your time and talent more. This sort of payment would never hold up in the business world."
    i "That might be true! But you know what else is true?"
    s "What, Io?"
    i "I like you."
    s "Yes, you’ve made that quite apparent."
    i "Let’s run away together. All three of us."

    scene dodgingsnowflakes15
    with dissolve

    u "Wait a sec, I’m coming too?"
    i "Of course you are. You’re my best friend. Do you have any idea how awesome it would be to leave everything behind {i}except{/i} for you two?"
    u "I..."
    i "..."

    "I obviously have no intention of doing any of this, but I guess it’s fine to let Io fantasize for a little while."
    "One hug in exchange for tens of hours of work isn’t really fair, so I’ll just consider this an added bonus that tips the scale a little further in my favor."

    scene dodgingsnowflakes16
    with dissolve

    u "Where...would we go?"
    s "Wait, are you actually considering this?"
    i "Anywhere and everywhere. Just the three of us. "
    u "That sounds...nice, but..."
    u "You know, I just can’t see myself having fun watching you two all...huggy all the time."

    if bonus == True:
        s "I am definitely not a “huggy” person."
    else:
        s "That is very unfortunate because I am all huggy all the time."

    i "You wanna join in? We’ve got room for one more."

    scene dodgingsnowflakes17
    with dissolve

    u "Oh, no...That’s your present. I didn’t get Sensei anything, so...I’d just be getting in the way."
    i "Suit yourself then. He’s really comfy. And suspiciously cold."
    s "I don’t see what’s suspicious about walking here in the snow, but I’m glad to hear that you’re comfortable."
    s "Now, if you could please let go, I’d like to make arrangements for how exactly I’m going to get this thing out of here..."

    scene dodgingsnowflakes14
    with dissolve

    i "You really don’t hate it, Sensei?"
    s "No. And I didn’t hate the robot either. Stop assuming I’m just going to hate everything that you do when history very much begs to differ."
    i "I make no promises."
    i "Oh! And, I forgot to ask earlier, but are you coming to the Christmas party tomorrow? Because you being there directly influences whether or not yours truly will be in attendance. "
    s "I will, but don’t take that as me agreeing to spend the entire party with you since I normally wind up getting pulled around at events like this."
    i "That’s fine. I don’t mind pulling a little bit. It’s good exercise. "
    s "Then I will see both you and Uta tomorrow."
    u "Yeah..."
    u "It should be fun."
    i "Do you want me to just keep the wardrobe closet thing right where it is until you can figure out how to get it out of here?"
    s "I mean...do you have other options for where you could put it?"
    i "No. I don’t know why I asked that. I’m an idiot. No wonder you won’t date me."

    scene black
    with dissolve2

    s "Okay, that’s enough hugging for tonight."
    i "I completely understand and thank you for managing to put up with it for so long."
    s "Right. Well, I’ll see you two tomorrow, I guess."
    i "Okay! Goodnight, Sensei! See you tomorrow!"
    u "Goodnight, Sensei."

    play sound "dooropen.mp3"

    "I make my way out of the dorm room and begin to flip through a mental list of contacts to determine who would best be able to help me with this."
    "Within a matter of seconds, I’m able to cut the list down to just Haruka and Maki since they’re the only people I know who can drive."
    "Well, Niki too, I guess- but she’s probably off being famous somewhere."
    "I’m not sure if either one of my choices has a vehicle large enough to fit my present but, at the same time, I-"

    stop music

    $ renpy.end_replay()
    $ christmastwo4 = True
    jump christmastwo5

label christmastwo5:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
scene ayaneofficebang24
    with dissolve

    ay "Hah...hah...fine! You want to...do this the...non-romantic way?! I can do that!"
    ay "I know what...my future husband likes!"
    s "Oh yeah? What’s that, Ayane?"

    scene ayaneofficebang25
    with dissolve

    ay "He likes...how it feels in my...tight...wet...pussy..."
    ay "He likes squeezing my ass and...ahh...digging his nails into it..."
    ay "And I...like it too...I want him to...squeeze harder...do me harder..."

    scene ayaneofficebang26
    with dissolve

    ay "He likes that I’m in high school...and that he can do me in my cute, new uniform."
    ay "Ah- I just felt it get harder. "
    ay "Is that what you want to hear more of [ayanemaster]? That I’m your student and...you have me bent over a table?..."
    ay "Is the door locked?...What would happen if someone came in?..."
    ay "Do you think I’m a bad girl...for wanting to be with my teacher like this?..."
    ay "For wanting him to fill me up?...Wanting him to...let it all out inside of me?"
    s "Ayane-"
    ay "Go ahead, [ayanemaster]...cum for me...cum {i}in{/i} me...cum for...a girl who’s cum for you...hundreds of times before..."
    ay "Let it out...love me harder...love my...tight...schoolgirl pussy..."

    scene ayaneofficebang27
    with dissolve

    ay "Ah! Yeah! Love me...right there...love me right there..."
    ay "Let’s...cum together, [ayanemaster]! I mean...let’s...do our homework! "
    ay "I’m...oh god...I don’t want to do it alone again...please, [ayanemaster]..."
    ay "Doing homework alone is...embarrassing!"
    ay "I can’t...hold it in anymore..."
    ay "Love me..."
    ay "Love me!"
    ay "Love me!!!"

    with sexfade
    with sexfade
    scene ayaneofficebang28
    with cumflash
    with hpunch

    ay "AAAaaaAAAaaaAaaahhh!!!!!~~~~~~~~~"

    "Ayane stops thrusting altogether and connects her ass with my waist, holding it there for the duration of my orgasm and making sure I give her every last drop."
    "Unfortunately, her body is still too small to hold everything, and some of my semen winds up dripping out of her and onto the table to meet with her own juices."
    "Her skin is moist, and before pulling myself out of her, I take another few seconds to indulge in it, softly gripping her flesh as if to say I’m not done with her yet."
    "Unfortunately, I am. At least for now."

    play sound "bell.mp3"

    s "..."
    ay "..."

    "Yup. Definitely done."

    scene ayaneofficebang29
    with dissolve

    ay "Heheh..."
    s "What? Why are you laughing?"
    ay "Because I’m having fun."
    ay "I like being like this with you."
    s "You mean with cum dripping out of you onto a table in my office?"
    ay "Yeah. Exactly like that. We should do this more often."
    s "Come visit me more often, then."
    ay "Maybe I will~"
    s "Really. Do it. I’m not kidding."
    ay "Wanna go again?"
    s "Did you not hear the bell just now?"
    ay "Bell?"
    s "The thing that signals when the next class starts. People are going to realize we’re gone."
    ay "Just tell them we went out to lunch or something. Nobody needs to know that we were having sensual, doggystyle sex in your office."
    ay "Or that I set the new orgasm world record."
    s "That definitely wasn’t the world record."

    scene ayaneofficebang30
    with dissolve

    ay "Then I will try harder next time!"

    scene black
    with dissolve2

    "And that’s how Ayane developed a new goal in life."

    $ renpy.end_replay()
    $ ayane_lust += 1
    $ ayanelust20 = True
    stop music fadeout 5.0

    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo4
...
```