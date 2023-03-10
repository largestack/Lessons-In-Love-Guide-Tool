# Butterfly Facts (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Girls in Spandex](./halloweentwo1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloweentwo2
* Group: Main
* Triggered by label: halloweentwo1
* Chain sources: halloweentwo1
* Chain sources path: halloweentwo1

## Official wiki page

[Butterfly Facts](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo2&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label halloweentwo2:
    scene halloweentwobar1
    with dissolve2
    play music "letsfuckingo.mp3"

    "I arrive at the bar with Sana to find the place already decked out in...well, not decorations, but whatever weird light bulbs Sara normally uses to make the color in here all pink and whatnot."
    "Apart from the lights, however, it doesn’t really appear that things have gotten underway as of yet."
    "I mean, there are no guests around- not even Maki and Haruka. And given that this place has been doing a little better than normal lately, that’s kind of disappointing."
    "I’m not really sure why I’m thinking so much about it, though, when I clearly have more important things to be doing. "
    "Like helping Sana get dressed."

    s "Do you require assistance?"
    sa "...I’m sorry?"
    s "Picking out clothes."

    if bonus == True:
        s "Or putting them on, I guess."
    else:
        s "Back in college, before I was the huggy boy, people used to call me {i}fashion man{/i}."
        s "Well...in between all of the other...horrible names they would call me..."

    sa "…"
    sa "No."
    sa "No, I think I’m okay..."

    "Fuck Halloween."

    sa "Everything I’m supposed to bring to the party is...pretty light...so you can just stay down here and wait for me to get back..."

    if bar50 == True and bonus == True:
        s "Are you sure you don’t need me to come up there and help with anything?"

        scene halloweentwobar2
        with dissolve

        sa "Uh...well..."
        sa "I kind of...yelled at you the last time we were up there together, so..."
        sa "I think it’s probably best if you just stay down here..."
        s "Yes. I can see how having me {i}closer{/i} to your mother is better at quelling your uncertainty about our relationship than having me in her room with you."
        sa "Well...it sounds weird when you put it like that..."
        s "Because it is weird. But if that’s what you want, it’s fine by me. "
        s "Could be good to catch up with her anyway."
        sa "Just...don’t catch up too much...hahah..."
        sa "Hah..."

        scene halloweentwobar3
        with dissolve

        s "…"

        "Well...that’s that, I guess."

    else:
        s "Are you sure? Even if there’s a lot, I wouldn’t mind helping out."
        s "I normally wouldn’t ever agree to doing something like this, but if that’s what it takes to get to the rest of the Halloween costumes sooner, so be it."

        scene halloweentwobar4
        with dissolve

        sa "You’re...really that excited to see what everyone else is dressed up as?"
        s "This day only comes once every year, Sana. Kind of."
        s "Basically, it’s an important day."
        sa "But...you didn’t even know what day it was until I-"
        s "But I do now, don’t I? Now, go get the decorations and raid your mom’s closet or whatever."
        s "I’ll just wait down here and talk to her in the meantime."
        sa "Oh...uh...okay..."
        sa "I’ll...be right back, I guess?..."

        scene halloweentwobar3
        with dissolve

        "Sana disappears up the stairs into the apartment half of the building, leaving me mostly alone in the bar with someone who may or may not already be drunk."
        "But, I guess there’s only one way to find out..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene halloweentwobar5
    with dissolve

    sar "Well, if it isn’t my favorite customer!"
    s "Hey, Sara. You’re looking mostly sober tonight."
    s "You too, Yuki."

    scene halloweentwobar6
    with dissolve

    sar "Hey! How come your voice sounded a lot more gentle when you said that to her? "
    s "Probably because Yuki’s sobriety is something we should be praising and yours is something we should be encouraging."
    yu "Thanks, man. Sara’s not that far gone yet, though. ‘Least not from what I’ve seen."
    sar "I’ll have you know I’ve been doing {i}much{/i} better lately when it comes to not drinking while the bar is open."
    sar "I wait until the doors are closed now."
    s "Well, that’s a step in the right direction, I guess."

    scene halloweentwobar7
    with dissolve

    sar "So, are you going to stay for the Halloween party again this year? Maki and Haruka are on their way over now."

    if bonus == True:
        sar "And, if the rumors I’ve heard are true, their costumes are even more...risque this year."
    else:
        sar "And, if the rumors I’ve heard are true, they're both dressed as the green M&M this year. It's sure to be a real blood bath when they realize they're the same character."

    s "Speaking of which, where’s yours? You seem like the type to pretty much always dress up for stuff like this."
    sar "Not tonight. "
    sar "Well...at least not until I know how business is going to be."
    sar "I’m sure we won’t be like, {i}actually{/i} busy or anything, but I still have Yuki and your friend from the last party coming to temp for the night while Sana is out being a [teenager]."
    sar "Basically, I am prepared to work if I have to. And since my feminine wiles don’t work as well on our female clientele, I don’t {i}have{/i} to get dressed up. I just want to."

    scene halloweentwobar8
    with dissolve

    sar "Besides, Yuki’s popular enough with the girls to make it so I barely even have to do anything."
    s "Yuki is? Really?"

    scene halloweentwobar9
    with dissolve

    yu "Yo. The fuck is that supposed to mean?"
    s "Hey, don’t ask me. You’re the one always calling yourself “not cute” or whatever."
    yu "Not my fault that a bunch of girls are just settlin’ for the closest thing to a dude they can get with all the real ones up in space or whatever the fuck is goin’ on."
    yu "I’d be willing to bet cash that any girl with short hair’s gettin’ the same fuckin’ treatment I am."

    scene halloweentwobar10
    with dissolve

    sar "Oh, stop. That uniform looks absolutely adorable on you. It’s no wonder so many girls are flocking to the place now."
    yu "Yeah, sure the fuckin’ fliers you’ve been handin’ out to everyone and their mothers have nothin’ to do with it."
    sar "Fliers mean nothing in the face of true beauty, Yuki. "
    yu "Guh."
    sar "…"
    yu "…"

    if bonus == True:
        s "Good. Now, kiss."
    else:
        s "Good. Now, hug."

    scene halloweentwobar11
    with dissolve

    sar "I suppose one wouldn’t hurt if that’s what you want to see, Sensei."
    yu "The fuck, dude?! No! Not only is she a chick, she’s my boss now!"

    if bonus == True:
        yu "‘Sides, what if people fuckin’ walk in or whatever? Can’t say I’d wanna spend my money at some place where the employees are fucking behind the counters."
    else:
        yu "‘Sides, what if people fuckin’ walk in or whatever? Can’t say I’d wanna spend my money at some place where the employees are hugging behind the counters."

    scene halloweentwobar12
    with dissolve

    if bonus == True:
        sar "I mean...I don’t think Sensei said anything about {i}fucking...{/i}but I’d be lying if I said I wasn’t at least a little curious..."
        yu "Oh, you’ve gotta be fucking kidding me. You too?"
        s "You’re just really popular now, Yuki. Embrace it."
    else:
        sar "Do itttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt~~~~"

    scene halloweentwobar13
    with dissolve

    yu "Hah...whatever. ‘Least I’m gettin’ paid."
    sar "I’m still waiting on an answer to whether or not you’re staying, Sensei. "

    if bonus == True:
        sar "I’m sure someone like you would be preeeetty popular around a bunch of sexually dissatisfied women. "
        sar "Assuming they show up, that is."
        s "As fond as I am of sexually dissatisfied women, I’m not sure if I’m able to hang around this time."
        s "Pretty sure the party for my class is basically underway already."

        "Not to mention I’d much prefer being in a room full of primarily virgins than one with a handful of women who have been around the block a few times."
        "Sue me."
    else:
        sar "I have so many more things I want to tell you about my dead son."
        s "Nope. I'm good. Bye, Sara."

    scene halloweentwobar14
    with dissolve

    sar "Are you really gonna say no to these cute little faces?"

    if bonus == True:
        sar "We need you, Sensei~"
        sar "We need you to save our bar...{i}and our bodies...{/i}"
        s "…"
        yu "I think I’m good, actually. Not in the best shape anymore, but don’t think I need {i}saving{/i} yet."

        scene halloweentwobar15
        with dissolve

        sar "Really? Because I’d think that if {i}anyone{/i} in this room needed saving, it would be you."
        yu "Dude, there are three people in this room. And you two are making it pretty clear you fuck like rabbits already, so..."

        if sarasex == True:
            scene halloweentwobar16
            with dissolve

            sar "Weeeeeell...I don’t know if {i}rabbits{/i} is the right word..."
            yu "Uh-huh. Sure, boss."
            yu "Now, can you let go of my chin? You’re startin’ to leave a mark."

        else:
            scene halloweentwobar17
            with dissolve

            sar "Oh...no."
            sar "Sensei and I are just friends, actually."
            sar "I just get a little flirty around him sometimes."
            yu "Really? Well, sure had me fooled."
    else:
        s "YUP. SEE YA."

    scene black
    with dissolve2

    if bonus == True:
        "Sara goes silent for a moment before finally removing her finger from Yuki’s chin."
        "Before the conversation is able to pick back up, however, the “friend of mine” that Sara alluded to earlier finally decides to walk in..."
    else:
        "I go to leave the bar, but I'm stopped when another familiar character that I have yet to hug walks in."

    scene halloweentwobar18
    with dissolve

    k "Hello, attractive bartender woman!"

    if bonus == True:
        k "I have returned to this building of female fornication for the purpose of pouring liquids into hollow glass cylinders and making people dizzy!"
    else:
        k "I have returned to this building for the purpose of pouring liquids into hollow glass cylinders and making people dizzy!"

    k "Please pay me in feathers!"
    yu "Wha-"
    s "Welcome back, Kaori."

    scene halloweentwobar19
    with dissolve

    k "Ah! Friend! You are here as well!"

    if bonus == True:
        k "Do you intend to fornicate with the bar lady or her handsome friend with sadbags under her eyes?"
    else:
        k "Do you intend to hug the bar lady or her handsome friend with sadbags under her eyes?"

    k "Please warn me beforehand if you do so I can look away and pretend to not hear anything!"

    scene black
    with dissolve

    "Kaori makes her way over to the bar and Yuki looks incredibly dumbfounded for some-"
    "Oh. Wait. "
    "Yeah, this is probably really weird for her considering the last conversation I had {i}about{/i} Kaori ended with me finding out she's related to Yumi."
    "And...if Kaori is related to Yumi, it’s probably safe to assume...yeah."

    scene halloweentwobar20
    with dissolve

    yu "…"
    k "…"
    s "Surprise."
    sar "Is something wrong, Yuki?"
    k "Bar lady, have you created a new policy in which customers order beverages from the opposite side of the large wooden rectangle?"
    sar "No, Kaori. Yuki is an employee here."
    k "I think it may be time to fire her, for she does not appear to be doing much of anything."
    yu "…"
    k "…"
    sar "…"
    s "Allow me to step in here and try to explain the situation just enough to not cause anyone’s brain to malfunction."
    s "Well, any more than it already malfunctions on a daily basis."
    s "Yuki actually knows Kaori."

    scene halloweentwobar21
    with dissolve

    k "Is this about the instant gram again?! I already took those pictures down! This should have erased the memory of everyone who saw them!"
    s "That’s not how memory or...any of that works, Kaori."
    sar "What do you mean Yuki knows her? From where?"
    s "Well..."
    yu "We’re related..."

    scene halloweentwobar22
    with dissolve

    sar "You’re what?! Really?"
    yu "She’s my niece."
    k "I believe the word is pronounced “nice.” And thank you, tired-looking woman."

    if bonus == True:
        s "Kaori, a niece is a sibling’s child. Like the red haired girl you’ve seen me with before."
    else:
        s "Kaori, a niece is a sibling’s child."

    scene halloweentwobar23
    with dissolve

    if bonus == True:
        k "But, Friend! I have seen you with so many girls that it is impossible to keep track of them all!"
        k "Besides, the hospital people told me everyone else was gone. I do not have what you humans would call a “family.”"
    else:
        k "But...the hospital people told me everyone else was gone. I do not have what you humans would call a “family.”"

    yu "You really don’t remember me? I used to pick you up and take you to hang out with Yumi when she was still all little and shit."

    scene halloweentwobar24
    with dissolve

    k "My memory became bad after the whapam, kaboom, shhhhhhhh. I don’t remember you at all."
    yu "Wow. Small fuckin' world."
    k "I do not see what the size of the world has to do with our relation, but “Earth” is actually very large. Bigger than three whole cheese wheels."
    sar "How long have you known about this?"
    s "Not long. I just found out recently and...I guess it slipped my mind until right now?"
    sa "Umm...Mom?..."

    scene halloweentwobar25
    with fade

    sar "…"
    sa "…"
    s "…"
    sar "Sana, dear. What in the world are you supposed to be?"
    sa "I..."
    sa "I don’t even know anymore..."
    s "That is certainly an...interesting choice for a costume."

    scene halloweentwobar26
    with dissolve

    sa "I thought there would be less...revealing choices available..."
    sar "I mean...it wasn’t really weird to wear more revealing clothing back then, right?"
    sar "We grew up around the same time, didn’t we? Back me up on this."
    s "Fishnets and tight jeans I can understand. It’s the gas mask, weird gloves, and crop top with the word “Fire” on it that I’m confused by."
    sar "I’m sure they...made sense at the time?"
    s "And you’re {i}not{/i} just into really weird shit?"

    scene halloweentwobar27
    with dissolve

    sar "Will you like me more if I am?"
    sa "Mom! Stop!"

    scene halloweentwobar28
    with dissolve

    sar "Sorry, sorry. I couldn’t help it, dear."
    sar "You look adorable as...whatever you are."
    sar "Did you find all the decorations you needed?"
    sa "Yeah, they’re near the door...Which means I’m ready to go whenever..."
    sa "We’re going to have to take the bus, too, so...we should probably start heading out as soon as possible."
    s "You guys should have just had the party here. That’s what we did for the dorm war and only a handful of you wound up getting intoxicated."
    sa "I will...relay that information to Ayane for next year’s party..."
    sar "Be safe, okay? If you’re going to drink, make sure Sensei is around to carry you to bed."
    sa "Sensei...please ignore her and just...come with me..."

    scene halloweentwobar29
    with dissolve

    s "Well, sorry I can’t stay, but...yeah."
    sar "It’s fine. I have a feeling we’ll be pretty busy tonight anyway, so having you around would just be a distraction for me."
    sar "We can have our own party some other time."
    sar "Have fun and look after Sana for me."
    sa "Mom...come on..."

    scene black
    with dissolve2

    "I follow Sana away from the bar and-"

    yu "Yo! Hold up a second."

    scene halloweentwobar30
    with dissolve

    s "What’s up? Mad at me for not confirming Kaori’s return as a zombie?"
    yu "Nah. That’s...weird as fuck, but...I’ve got the whole night to talk to her about it."
    yu "It’s just..."
    yu "Well, today’s Yumi’s birthday and shit."
    yu "And I know it’s not really your place to get involved any more than you already have, but..."
    s "You want me to say happy birthday for you?"

    scene halloweentwobar31
    with dissolve

    yu "Uh...yeah..."
    yu "If it’s not a problem, I mean."
    yu "And..."

    scene halloweentwobar32
    with dissolve

    yu "If you could maybe give her this, too..."
    yu "It’s not much, but...I don’t really have a lot I can spend and-"
    s "Sure thing."
    s "I’m not sure if she’ll accept it, but I’ll definitely give it to her if she shows up to the party tonight."
    yu "Thanks, man. Remind me to buy you ramen sometime when the power’s not getting all fucked at Tojo's anymore."
    s "Did it happen again after the last time?"
    yu "Just once more that I’ve noticed since then, but Tsu-chan still wouldn’t let me go near her dad."
    s "Huh. Weird."
    sa "Sensei? We...really need to go..."

    scene halloweentwobar33
    with dissolve

    yu "Oh, shit. My bad. I was-"

    scene halloweentwobar34
    with dissolve

    yu "The fuck are you supposed to be?"

    scene halloweentwobar35
    with fade

    sa "…"
    s "…"
    sa "Bad at Halloween..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    q "Excuse me!"

    scene halloweentwobar36
    with dissolve

    k "Ah! Customerburger!"
    k "I like your butterfly! "
    k "Did you know that the average lifespan for the red admiral butterfly is approximately ten months?!"
    sar "Kaori, what did I tell you about giving insect facts to the customers {i}before{/i} taking their orders?"
    q "Noooooo tell me more butterfly facts. I wanna know!"

    scene halloweentwobar37
    with dissolve

    k "Then...did you know there are over 24,000 species?! And that some of them can fly up to 12 miles per hour?!"

    scene halloweentwobar38
    with dissolve

    q "Ahh, yeah. That’s the stuff."
    q "Inject that lepidopterology right into my veins, baby."
    yu "Uhh...she botherin’ you? Cause if you’ve got somethin’ you wanna order-"

    scene halloweentwobar39
    with dissolve

    q "Not at all! I’ll take three of whatever your favorite thing on the menu is."
    yu "Aight. Three beers. Got it."
    sar "Yuki, come on! Upsell! Profits! Business lingo!"
    yu "What? She asked for my favorite thing on the menu."

    scene halloweentwobar40
    with dissolve

    if bonus == True:
        k "You are very pretty, Miss. Are you really having such trouble fornicating that you had to come here?"
    else:
        k "You are very pretty, Miss. Are you really having such trouble finding a hug partner that you had to come here?"

    q "Woah. The flier said “Halloween Party,” but I didn’t realize that’s the sorta thing I was getting myself into."
    q "Do you hit on everyone with butterfly related trivia or am I just lucky?"

    scene halloweentwobar41
    with dissolve

    k "Hitting {i}on!{/i} I know what that means now!"
    q "Hahahah! I love this place already!"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloweentwo2 = True

    jump halloweentwo3

label halloweentwo3:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
$ futaba_love += 5

            "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

            $ futabahalloween2win = True

        "Molly":
            s "Well, after careful, internal deliberation...the winner of this contest is Molly."

            scene secondhalloweenintro40
            with dissolve

            mo "Do...do my ears deceive me?!"
            mo "I did spend an absurd amount of money on this costume, but I still would have wagered that you’d pick someone else, Sir!"
            s "Maybe in some other timeline, I would have. But I think you look the “best” and, since I can only choose one...I guess it had to be you."
            mo "Really? Even though I annoy you?"
            mo "Even though we had a lengthy discussion recently about how I’ve all but given up on real human beings and that I will forever devote myself to dating games?"
            mo "You’re still going to choose me after all of those flags have already been raised?"

            scene secondhalloweenintro41
            with dissolve

            s "I guess so."
            s "Congratulations, Molly. You deserve it."
            mo "Th...Thank you, Sir!"
            mo "As previously mentioned in your warning about this choice...I will not forget this!"

            $ molly_love += 5

            "{i}Molly’s affection has increased to [molly_love]!{/i}"

            $ mollyhalloween2win = True

        "Sana":
            s "The winner of this contest is..."

            scene secondhalloweenintro42
            with dissolve

            s "Sana."
            a "…"
            sa "…"

            scene secondhalloweenintro43
            with dissolve

            sa "What?!"

            if sanafashion == False:
                s "You heard me, official Halloween costume winner."
            else:
                s "You heard me, two time fashion contest champion."

            sa "I wasn’t even competing in this one!"
            mo "Actually, Sana...you formally entered the competition when you stepped into the spotlight."
            mo "If you didn’t want to participate, you should have been more careful."
            ay "Congratulations, Sana! I would have picked you too."
            sa "I didn’t want to be picked! I don’t even have a costume yet!"
            s "You don’t need one. That’s how cute you are."
            a "Ugh...Sana being in this contest made it unfair to the rest of us..."

            scene secondhalloweenintro44
            with dissolve

            sa "I wasn’t in the contest! This is all a big misunderstanding!"

            $ sana_love += 5

            "{i}Sana’s affection has increased to [sana_love]!{/i}"

            $ sanahalloween2win = True

    scene black
    with dissolve2
    stop music fadeout 40.0

    "After I name the winner, it becomes clear that it’s time for all of the girls to start getting ready for tonight’s party."
    "Apparently, some of the others have already started heading over to the Amamiya mansion to help set things up."

    if bonus == True:
        "And fortunately, I wasn’t forced to go along with Makoto and participate in that stage of the party this year, saving me a fair amount of energy to use on more important matters- like sex."
        "Hopefully."
        "But, if that winds up not being the case, at least I’ll be a little less exhausted when I wind up having to deal with a drunken Molly or...anything else along those lines."

    "Regardless...I, too, begin to make my way out of[school] alongside everyone else."
    "But, just as I make it to the lockers, Sana approaches me for the second time today (A new all-time record) and asks me to accompany her to her mother’s bar and help bring over some decorations for the party."
    "And while this sounds {i}technically{/i} a little easier than the hours I spent setting things up with Makoto, I can’t help but be a little upset."
    "My short-lived desire to spend the moments before a party I just found out about in silence has, unfortunately, come to an end."
    "But..."
    "On the bright side, at least things at Sara’s were rather...{i}lively{/i} last Halloween."
    "If I’m going to be tagging along with Sana, I can at least hope for a repeat of that..."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloweentwo1 = True
    $ rinsad = False

    jump halloweentwo2
...
```