# Something Out of a Nukige
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe10&go=Go)



## Event preconditions
✅Molly love greater than or equal to 10

✅Event "[Molly: Remnants of Forgotten Memes](./mollycafe5.md)" is completed (event=mollycafe5)

✅Event "[Molly: Torrent of Power](./mollydorm5.md)" is completed (event=mollydorm5)



## Next events
* [Molly: The Dark Entity](./mollydorm10.md)

## Event properties
* ID: mollycafe10
* Group: Molly
* Triggered by label: mollycafe
* Triggered by branch label: mollycafe

## Event code
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe10:
    scene mollycafe19
    with dissolve
    play music "cafe.mp3"

    mo "And that’s when I was like, “Watch your mouth, lich! You’re messin’ with the wrong priest!”"
    mo "And right before my holy nova went off, a swarm of adds spawned and aggro’ed straight to me so fast that the tank rage-quit on just our third wipe."
    mo "Some people just aren’t meant for progression raiding, you know?"
    s "No."

    "As you can see, I’m caught up in yet another “conversation” with Molly and beginning to question whether or not I will ever be able to talk about things {i}I{/i} like with her."

    if bonus == True:
        "Mind you, the list of things I like is limited to...cute girls, sex, food, and sleep...And maybe those aren’t really the best conversation pieces after all."
    else:
        "Like vanilla ice cream or donating money to various charities."

    mo "Oh well. That’s fine. You don’t really need to get it. I can fill you in on all of the stuff you don’t understand so that when you finally start your free trial, you’ll know the basics."
    s "The basics of what? I don’t have time for video games."

    scene mollycafe6
    with dissolve

    mo "Why do you have so much time to hang out with [teenage]girls but no time to play games?! That doesn’t make any sense!"
    s "I don’t have time to play games because I {i}have{/i} to hang out with [teenage]girls. It is my calling. "
    s "Just like how your calling is guarding emeralds or whatever it is you do."

    scene mollycafe14
    with dissolve

    mo "I don’t guard emeralds! I’m the Emerald Guardian! It is very different!"
    s "So like, you’re...made of emeralds? I’m not really sure what you’re trying to get at here."
    r "Jeez. Give the girl a break, man. She’s just trying to get you interested in her hobbies."
    s "…"

    scene mollysecondcafe1
    with fade

    "I turn around to find both Rin and Futaba waiting behind me in line. "
    "I didn’t even hear the two of them come in."
    "Probably on account of Molly’s obnoxiously loud voice, but still. "
    "If I were her, I’d probably make some comment about their skill in stealth or something along those lines, but I’m-"
    "Wait...why did that thought even occur to me? Have I really been spending so much time with Molly that this is just...the way I think now?"
    "What is happening to me?"

    s "How long have you two been standing there?"
    f "Since the part with the lich. So not that long at all."
    r "Yeah, it’s only been a few-"

    scene mollysecondcafe2
    with dissolve

    r "Hey, wait a minute! What are you doing here so late?!"
    r "You’re supposed to be {i}my{/i} guinea pig! Not Molly's!"
    r "Am I not good enough for you anymore?! Explain yourself, damn it!"
    f "Uh...umm..."
    s "It’s really not what it looks like. I-"

    scene mollysecondcafe3
    with dissolve

    r "Futaba, I’m being cheated on. Hold me."
    f "I’m...a little confused. But I don’t have a problem-"

    scene mollysecondcafe4
    with dissolve

    mo "Oh, such sorrow. Having your favorite customer stolen by a girl with minimal talent who put all of her points into charisma. "
    r "Why are you touching me? I asked for Futaba."
    mo "Because even if we are arch nemeses...I still love you."

    scene mollysecondcafe5
    with dissolve

    f "They’re always like this. Don’t pay it any mind. "
    f "Half of our club meetings are just the two of them arguing about things. I’m sure they’ll be back to normal in no time at all."
    s "You’re in the manga club too, Futaba?"

    scene mollysecondcafe6
    with dissolve

    mo "She’s not just in the club, she’s the vice president of it!"
    s "Wait, really? Who’s the president then?"
    mo "Yours truly!"
    s "Weren’t you just telling me the other day that it was hard for you to even be accepted into the club?"

    scene mollysecondcafe7
    with dissolve

    r "Wait, did you really say something like that? Why?"
    r "We wouldn’t have made you the new president if we didn’t accept you."
    mo "Well...I...uhh..."

    scene mollysecondcafe8
    with dissolve

    mo "Anyway! That's not what we're talking about right now!"
    mo "Sir, do you now understand just how powerful I truly am?! You should be thankful to have such a strong force on your side! Willing to fight tooth and nail for your honor!"
    s "I can assure you that any honor I may have had was lost long, long ago."
    mo "Then we must begin the side quest to track it down at once!"

    scene mollysecondcafe9
    with dissolve

    r "Uhh, can I order a drink or do I need to get back there and make it myself?"
    mo "What would you like to order, miss?"
    r "Quad grande upside down caramel macchiato. Extra caramel. "
    mo "…"
    mo "Black coffee?"

    scene mollysecondcafe10
    with dissolve

    r "Ugh. I’ll just do it."

    scene mollysecondcafe11
    with dissolve

    "Rin breaks free from Molly’s grasp and gets behind the counter to make whatever the hell she just said she wanted."

    mo "As you can see, Sir, I’m pretty horrible at my job."
    s "At least you’re aware of it."
    s "I’m not great at mine either, but it still seems to be working out somehow."
    mo "Aye. Because the two of us are cut from the same cloth! Two peas in a pod! Mercenaries selling ourselves to the highest bidder!"
    f "I’m glad to see the two of you are getting along so well despite only having just met each other recently."
    s "Is that what this is called? Getting along? Because Molly more or less just yells stuff at me every time the two of us are together."
    mo "I yell things at everyone. It is an endearing character trait. "
    s "You should try to be more like Futaba and never yell anything at anyone."

    scene mollysecondcafe12
    with dissolve

    mo "Ah! Oh no! It’s my worst nightmare come to life! "
    mo "You’re into the dandere type, aren’t you, Sir?!"
    s "The what?..."
    mo "Weebnote: Dandere characters are the super quiet, awkward ones with surprisingly cute sides that they break out just to get into your head!"
    mo "It's all a ploy! None of it is real!"
    mo "Fight the moe, Sir! Fight it!"

    if bonus == True:
        mo "All that stuff about them being freaks in the sack is purely fiction! Don't give in!"

        play sound "glass.mp3"
        scene mollysecondcafe12
        with hpunch

    r "Ah! Shit! I dropped my freakin'-"
    r "Molly, what the Hell are you talking about over there?! You know my hands stop working correctly when that sort of stuff comes up!"
    mo "I am sorry, but this is a major crisis! Sensei is about to leave us for Futaba!"
    s "That archetype sounds more like Sana than Futaba, to tell the truth."
    s "Futaba can be a little quiet at times but she’s not ever really {i}awkward.{/i} "

    scene mollysecondcafe13
    with dissolve

    f "I’m...only quiet in school, really..."
    s "That’s true, I guess. You’re actually quite talkative whenever we're in the library."
    s "Which is kind of...the opposite of how you’re supposed to be in the library, now that I think about it."
    mo "Oh! I’m glad the Supreme Overlord brought the library up cause I’ve been meaning to ask you if they have any of the resources I need for our one-shot thingy."
    s "One-shot thingy? What does that mean?"

    scene mollysecondcafe14
    with dissolve

    mo "Oh ho ho~ You want in, Sir? Why didn’t you just say so?"
    s "Probably because I still have no idea what you’re talking about."
    f "She’s talking about...Dungeons and Dragons..."
    f "Molly wants to play when we go on vacation since she can’t spend much time in the sun without getting burnt..."
    mo "Correct-a-mundo, Sword-dancer of the Seven Suns."
    s "Is that your nickname, Futaba? That’s the coolest one yet."

    scene mollysecondcafe15
    with dissolve

    f "You really...think so, Sensei?..."
    f "Hahaha...hah..."
    mo "You see, Sir...I’m gathering up able-bodied men and women to compete in a short-term campaign for one night only in whatever building you decide to keep us in!"
    s "Please don’t make it sound like I’m holding you captive."
    mo "We are {i}all{/i} but prisoners to the protagonist of the game. And that’s you, Sir. You’re the only male character around."
    s "Okay, fine. Whatever. But don’t make it sound like that to anyone who isn’t in the class."

    scene mollysecondcafe16
    with dissolve

    mo "Hehehe~ One male and so many females...all housed in close proximity to one another."
    mo "It’s like something straight out of a nukige."
    s "…"
    s "Can I get another weebnote, please?"

    scene mollysecondcafe17
    with dissolve

    if bonus == True:
        r "It means a game with a lot of sex."
    else:
        r "It means a game with a lot of hugging."

    s "Ahh. That explains why Molly is blushing so much right now."
    r "Futaba is too, I’d wager?"
    s "Yup. Both of them are."
    s "You are too, I think."
    r "Nah, this is just how my cheeks look."
    r "Three blushing girls would be overkill for one scene, dude. Don’t flatter yourself."
    s "Worth a shot."
    mo "A-Anyway! What I’m trying to ask is if you’d maybe want to get in on some of the action, Sir."

    if bonus == True:
        s "..."

        "Is she asking what I think she's asking?"

        s "Hell yeah. Of course I’d-"
    else:
        s "Hell yeah. I've always wanted to try my hand at a tabletop RPG. That sounds really nifty."

    scene mollysecondcafe18
    with dissolve

    if bonus == True:
        r "She means the campaign, Sensei. She’s not inviting you to an orgy."
        s "Oh."
        s "Well that’s significantly less exciting."
    else:
        r "She means the- wait. What?"
        r "I feel like this conversation used to be different."
        s "Shut up, Rin. Get excited."
        r "I mean...I {i}guess{/i} it's kind of exciting?"

    scene mollysecondcafe19
    with dissolve

    if bonus == True:
        mo "It’s plenty exciting! Some would even say it’s {i}more{/i} exciting than an orgy!"
        s "What sort of sad human being would ever say something like that?..."
        mo "I would!"
    else:
        mo "It’s plenty exciting! Some might even say that it's a smashing good time!"
        mo "And by some I mean Nigel Thornberry from the Wild Thornberries! Another character we are now able to reference in this game!"

    scene mollysecondcafe20
    with dissolve

    if bonus == True:
        mo "What would you even do in an orgy with so many people?...There would be like...twelve of us..."
        mo "Who would go first? Who would go last?"
        mo "Where would we put all of our clothes?"
        mo "Would we even {i}bring{/i} clothes?"
        mo "Can the male body even produce that much-"
        s "Okay, Molly. You asked too many questions and Rin is also blushing now. "
        s "Unless that is...also the natural color of her cheeks?"
        r "................................"
        s "Nope, definitely blushing."
        s "Anyway, I can’t say I know what’s going to happen on this “educational field trip,” but I’m almost positive there won’t be an orgy that large. Or even at all, for that matter."
    else:
        mo "Whatever happened to that show?"
        s "I can't say I know what's going to happen on this field trip or whatever, but I'm almost positive that we'll all make it back alive."

    scene mollysecondcafe21
    with dissolve

    f "Ummm...doesn't saying it that way...imply that...it’s possible?"

    "Again, I’ve literally watched this world be reset. Nothing is impossible in my head anymore."

    if bonus == True:
        s "Sure. I mean, who knows when some crazy virus will break out and cause all of the women everywhere to be overcome by lust?"
        s "Look, it's already claimed Rin."

        scene mollysecondcafe22
        with dissolve

        mo "Oh! I’ve played a game like that before!"
        r "{i}All{/i} of the women?..."
        s "You have strange taste in games, Molly."
        s "In fact, you have strange taste in everything."
        mo "My tastes are normal! I swear! I’ll even show you my homework folder to confirm this!"

        scene mollysecondcafe23
        with dissolve

        mo "Ah, wait! No! I should...probably check it first to make sure that all of the...uhh...more questionable material has been erased!"
        s "If you need to check the folder beforehand, I think that says more than enough about whatever {i}questionable content{/i} you're referencing."

        scene mollysecondcafe24
        with dissolve

        r "I mean...I guess {i}I{/i} could always...you know, give it a look...Since I’m an unaffiliated, unbiased party and everything."

        scene mollysecondcafe26
        with dissolve

        mo "Umm...orgy stuff aside, I do need to know if you’re gonna be joining us, Sir. "
    else:
        s "I mean...I guess we {i}could{/i} die. There's no good way of knowing in advance."

        scene mollysecondcafe26
        with dissolve

        mo "Um, all that aside, I do need to know if you’re gonna be joining us, Sir. "

    mo "I’m kind of neurotic when it comes to organizing stuff, believe it or not. So the sooner I know, the better."
    s "Oh. Uhh, well I don’t think I’ll play. But I wouldn’t mind watching you guys, I guess. "
    s "That would probably be fun in a really...different sort of way. "
    mo "Are you sure, Sir? It’s a load of fun. Two loads even. So many loads that you won’t even know where to put everything."
    r "So...many loads..."
    f "You word things very strangely sometimes, Molly..."
    s "She words things very strangely all the time."

    scene mollysecondcafe27
    with dissolve

    mo "And yet you still visit me at night!"
    f "Well...are you really sure he's here to see you and that...he didn’t just come for...a pastry or something?..."
    mo "Molly MacCormack is sweeter than any pastry, Sword-dancer. She is the main course and everyone else is just an appetizer."
    s "It's really impressive how you can be so weird {i}and{/i} conceited at once."

    scene mollysecondcafe29
    with dissolve

    mo "Why wouldn’t I be? Peak Molly-moments always happen when I’m surrounded by my friends! "
    mo "I’ve gotta hype myself up so I don’t fall behind them and wind up as nothing more than a girl passing by in the end credits."
    mo "The lead heroine always has to leave a lasting impression, Sir. Which is exactly why I need to remind you all the time about how awesome and powerful I am!"
    mo "And you’ll get to see that power in full-display come time for vacation! Even {i}if{/i} I need to hide my sensitive Irish skin from the sun during daylight!"
    s "I’m sure I will, Molly...I’m sure I will."

    scene black
    with dissolve2

    "The four of us hang out at the cafe for another hour or two until it comes time to close up shop."
    "I’m honestly surprised that Haruka trusts Molly enough to close this place on her own."
    "But I guess just being overly-spontaneous and hyper doesn’t make her a bad employee."
    "After all, when it came time for her to clean things up, she started focusing harder than I've ever seen her focus before."
    "It was actually a little impressive, to be honest."
    "But I guess it doesn't stay impressive for very long as I elect to leave in the middle of her cleaning spree."
    "At the end of the day, who wants to watch a girl clean up a restaurant when there’s an equally cute one waiting at home?"
    "And so I say goodbye to everyone, turning my back to them as I finally begin to make my way back to the residential district-"
    "Thinking about various combinations of orgies the whole way home."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe10 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe15:
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
...
```