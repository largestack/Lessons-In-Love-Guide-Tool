# Moe Fan Service (Tsuneyo)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Tsuneyo love greater than or equal to 15

* Event [Seeds](./ramen15.md) (Tsuneyo) is completed)

* Day of week is not Monday



## Next events

* [Tsuneyo: Fucking...Or What it Means to Live](./tsuneyodorm20.md)

## Event properties

* Id: tsuneyodorm15
* Group: Tsuneyo
* Triggered by label: tsuneyodorm
* Triggered by branch label: tsuneyodorm
* Triggered by path: tsuneyodorm->tsuneyodorm15

## Official wiki page

[Moe Fan Service](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyodorm15&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label tsuneyodorm15:
    play sound "knock.mp3"
    stop music fadeout 30.0

    t "Eep!"
    s "…"

    "Did my knocking scare Tsuneyo?"

    play sound "knock.mp3"

    t "Stop!"
    s "Tsuneyo, it’s just-"
    mo "Hold still, gosh darn it! It’s not even that tight!"
    mo "And Sir, since I know you’re out there, don’t be getting the wrong idea!"
    mo "I’m just helping Tsuneyo into a costume I made for her."
    mo "The door is open. Come tell us how it looks."

    if bonus == True:
        "Ahh, the perks of showing up at exactly the right moment."
        "I sigh to myself and hope that whatever costume Molly made for Tsuneyo this time is a bit more...revealing than the suit of samurai armor she wore to the Halloween party."
        "Don’t get me wrong, Tsuneyo was probably the cutest samurai I’ve laid my eyes on, but I’m pretty sure she’d also make a cute-"
        "Uhh, anything with less clothing than a samurai."
        "So most things."
    else:
        s "Okay, but please tell me if you feel uncomfortable at any point so I can be a good guy and leave."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the handle to be greeted by some anime theme I’m sure I’ve heard Ami playing around the house once or twice before."
    "I’m certain of this because I immediately feel upset with myself for singing along inside of my head."
    "I am supposed to be devoid of joy. I shall not be swayed by a cute pop song or-"

    scene tsuneyocos1
    with dissolve
    play music "oldweather.mp3"

    t "Help."
    s "…"

    "Okay, maybe I’ll allow myself to be a little swayed by Tsuneyo."

    t "The Emerald Guardian is trying to take me to Virginia."
    mo "So, honest thoughts, Sir?"
    mo "I’m thinking I should have used slightly darker fabric since this seems a little close to her skin tone, but it’s my first time making a costume from scratch for a girl of her color."
    mo "Also, I didn’t want to deviate too far from the character’s original costume, soooo...what do you think?"
    t "Do not answer the Guardian’s questions. I do not need to hear your thoughts."
    s "Why are you so afraid of hearing what I think? You look great."
    mo "Is that how you actually feel or are you just being nice? I kind of need to know if I have to change anything."
    t "He is clearly just being nice. My arms are too muscular and my chest too large to recreate this small magical girl."
    s "Is that really a problem?"
    s "I thought the whole thing with cosplay is that you want to put your own spin on characters."
    t "I have to spin now?"
    t "Why is this process so complicated?"
    mo "Not exactly, Sir. Most cosplayers try to get as close to the original characters as possible."
    mo "Sure, there are some who like putting their own spin on things, but this is not the case for Tsuneyo and me."

    scene tsuneyocos2
    with dissolve

    t "Fine! Spin me!"
    t "I am prepared!"
    mo "Not that kind of spinning, Kendo Princess."
    mo "What Sir is trying to say is that he thought you were making your own version of the character."
    mo "But that’s not-"

    scene tsuneyocos3
    with dissolve

    t "That sounds more fun than dressing as a character I don’t understand."
    t "Doesn’t it?"
    t "How would a normal [teenage]girl have fun in my shoes?"
    s "The only normal [teenage]girl I know would probably call this stupid and storm out to go eat ten pounds of takoyaki."
    t "Emerald Guardian, unhand me so I can go consume octopus balls like normal girls do."
    mo "But...my costume kind of hinges on the success of yours. We were going as a duo, remember?"
    mo "And...I worked really hard on this. "

    scene tsuneyocos4
    with dissolve

    t "What would a normal girl say now, Sir?"
    t "Should I fuck her?"

    scene tsuneyocos5
    with dissolve

    mo "...What?"
    s "Don’t worry, Molly. She doesn’t mean-"
    mo "Obviously it’s a reference to “fuck you,” Sir. I’m not an imbecile."

    "It's impressive how easily she understood that."

    mo "But why would Tsuneyo suddenly become so hostile?"

    scene tsuneyocos6
    with dissolve

    t "Perhaps it is what they call puberty?"
    t "I am becoming a woman and filled with so many hormones that I can’t help but fuck everyone and everything."
    s "You know...maybe it’s time we-"
    mo "Don’t even bother, Sir. It’s not worth it."
    mo "Let her find out from one of the other girls. This is out of our hands."
    mo "Besides, I kind of need to put the finishing touches on our costumes."
    s "What’s even the reason for this? Halloween just passed a few months ago."

    scene tsuneyocos7
    with dissolve

    t "Allow me to explain."
    t "The Emerald Guardian and I are lovers."
    mo "A less than exceptional start to your explanation, but I’d be lying if I said I wasn’t interested in hearing how the rest plays out."
    s "If you’re lovers, why won’t you let her take you to Virginia?"

    scene tsuneyocos8
    with dissolve

    t "Because I am not Tsuneyo...."
    t "I am Kyoko Sakura, a magical girl who is going to go on a boat ride with the Emerald Guardian’s character- a girl who I do not remember the name of."
    mo "Sayaka Miki. But, Kendo Princess, it’s important to note that when I reference “shipping” two characters I do not mean putting them on an actual ship."

    scene tsuneyocos9
    with dissolve

    t "Ah, so you intend to pack the characters. I forgot that the word “ship” could also be used that way. "
    mo "Closer, I suppose, but still not quite."
    s "What does any of that have to do with being in love?"

    scene tsuneyocos10
    with dissolve

    t "Your guess is as good as mine. I personally don’t feel like I’m ready for a relationship yet."
    mo "We’re doing a duo-cosplay and the characters we’re dressing as were {i}definitely{/i} in love but like, not canonically."
    mo "What I’m saying is they should have been."
    s "Oh, okay. So you don’t actually love Tsuneyo-"

    scene tsuneyocos11
    with dissolve

    t "You don’t?!"
    s "You’re just dressing her up as a girl who you believe is in love with the character that you’re dressing up as."

    scene tsuneyocos12
    with dissolve

    mo "Basically, yes."
    t "My heart is snapping like the neck of a chicken in the hands of my father."
    s "You’ll live, Tsuneyo. Everyone has their heart broken at least once."
    t "You are right. I am a strong woman who can sail on a boat with whoever she likes. "
    t "The only love I need is my love for-"
    s "Noodles, we know."
    t "…"
    s "…"
    t "Why have you not rescued me from the clutches of the Emerald Guardian yet?"

    scene tsuneyocos13
    with dissolve

    mo "Okay, I’ll be hitting the enrage timer any second if you don’t actually start helping me out, Kendo Princess."
    mo "How does everything feel? Itchy? Loose? Is it tight anywhere?"
    t "It’s tight everywhere. "
    t "Is it possible that you maybe have confused our chest-"

    if bonus == True:
        scene tsuneyocos14
        with dissolve

        t "Sizes?!"
        mo "I didn’t confuse anything."
        mo "I can obviously tell that you were fortunate enough to be born with additional stat points in the breast area, I just didn’t realize {i}how many{/i}."
        mo "Sir, you’re well versed in the breasts of [teenage]girls-"
        s "Why, yes I am. Thank you for noticing."
        mo "Go ahead and grab Tsuneyo’s other one."
        mo "Let me know if you think it’s actually too tight or if she should just suck it up and go as-is."
        s "Molly, remind me to thank you for this one day."
        mo "Just do it quickly, before she notices."

        "I take a step toward Tsuneyo and-"

        scene tsuneyocos15
        with dissolve

        t "Mmm!"
        s "…"

        "I take a step away from Tsuneyo and decide to not sexually assault her today."
        "Sorry, Molly."
        "And sorry, penis. I know you were looking forward to this more than anyone."

        scene tsuneyocos16
        with dissolve

        t "I think that I am supposed to be mad at you, but this does not feel nearly as bad as I expected it to."
        mo "Hmm...I guess I can see how this might be a little constraining for someone with your natural stat advantage."
        mo "I’ll make some adjustments so it will be more comfortable for you during the photoshoot."
        s "Photoshoot?"

        scene tsuneyocos17
        with dissolve

        mo "Oh, right. Tsuneyo never finished her explanation."
        mo "One of our latest projects in the manga club is doing a group cosplay shoot, and Tsuneyo is filling in for Rin as Kyoko."
        s "Why doesn’t Rin just do it?"
        mo "I’m not sure. But I don’t really have time to think about it since I still need to make the final adjustments for my costume as well."
        mo "Poor Futaba’s been waiting on the rest of us to finish since Halloween."
        s "Does this mean you’re joining the manga club, Tsuneyo?"
        t "…"
        s "Tsuneyo?"
        t "I am on strike from speaking until I receive my body back."
        t "It was only enjoyable for several seconds."
        t "Now I’m just angry and embarrassed."

        scene tsuneyocos18
        with dissolve

        mo "Go ndéana an diabhal dréimire de cnámh do dhroma ag piocadh úll i ngairdín Ifrinn!"
        s "What the fuck was that?"
        mo "Go stand in the corner, Kendo Princess."
        mo "I’ll just take some pictures and let you go back to dressing like a hooligan."
        t "And {i}you{/i} can go back to being pretty like the...pretty girl you are."
        s "Your insults could use a little work, Tsuneyo. But I applaud your effort."
    else:
        t "Ah!"
        s "Why did the screen suddenly go black? What is happening?"
        mo "Just more censorship, Sir. Gotta keep the folks at Patreon happy."
        s "I am missing out on vital information. Probably."
        t "I am missing out on vision."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene tsuneyocos19
    with dissolve

    mo "Last chance for any feedback, Sir. "
    mo "I hate to admit it, but you’ve been entirely unhelpful tonight."
    s "I don’t know. I feel kind of bad."
    s "It seems like Tsuneyo isn’t having a very good time."
    mo "Nonsense. She’s having the time of her life."
    t "It’s true. I’m finally experiencing what it means to be young."
    s "Then why do you look so mad?"
    t "Because the Emerald Guardian was extremely attractive in her costume and I look stupid."
    t "The manga club will never deem this a suitable cosplay if I don’t resemble Kyoko Sakura, professional sailor."

    scene tsuneyocos20
    with dissolve

    mo "Magical girl. Not a sailor, Kendo Princess. It’s not that kind of ship."
    mo "Also, the girls would never hold something like that against you."

    if bonus == True:
        t "Also I was groped. I think I am supposed to be mad about that."
        mo "That’s just a thing that’s going to happen if you’re going to dress up. I’m not fully accustomed to your...assets yet."

    s "Have you even seen yourself in the costume yet, Tsuneyo?"

    scene tsuneyocos21
    with dissolve

    t "Impossible. All I can see are my limbs."
    t "And they are large and unlike that of the Emerald Guardian, who has small, dainty, weak limbs."
    mo "Wow. Okay."
    s "Molly, just take a picture of Tsuneyo and show it to her."
    mo "An excellent decision, Sir! We’ll show the Kendo Princess how cute she is and it will immediately dispel any worries she has!"
    mo "An excellent plan. You truly are the Herald of the Adolescents."
    mo "Tsuneyo, pose!"

    scene tsuneyocos22
    with dissolve

    t "P-Pose how?"
    t "I don’t know any poses!"
    mo "Any pose! Make yourself look cool!"
    t "Uhh...uhhh!"

    scene tsuneyocos23
    with hpunch

    t "Pose!"
    mo "…"
    s "…"
    t "…"

    play sound "cameraflash.mp3"
    scene tsuneyocos23
    with flash

    mo "Welp, better than nothing."
    mo "Come see how you look."

    scene black
    with dissolve

    "…"

    scene tsuneyocos24
    with dissolve

    t "Ah..."
    mo "See? You don’t look stupid at all."
    t "You...made me look cute."
    t "Your powers truly {i}are{/i} real."
    mo "I’m offended that you ever doubted them."
    t "And that pose is so...brave."
    mo "…"
    mo "Sure, yes. Very brave. "

    scene tsuneyocos25
    with dissolve

    t "How did you know that this would work?"
    t "Can you predict the future?"
    s "No. I don’t have the same sort of...powers as Molly."
    s "I just figured that there was no way you’d still feel weird about yourself after seeing what you actually looked like."
    t "You believed in me?"
    s "Ehh, I wouldn’t say I {i}believed{/i} in you."
    s "I just spend pretty much every waking moment looking at [teenage]girls, so I like to think of myself as a good judge of them."

    if bonus == True:
        "I mean, I’m also lucky enough that literally everyone in my class is attractive, so that definitely helps with the, uhh...judgement."

    mo "And as someone who has spent just as long, if not longer, peering into the depths of her computer screen in search of the perfect waifu-"
    mo "I, too, know {i}moe{/i} when I see it, Tsuneyo."

    scene tsuneyocos26
    with dissolve

    t "Moe?..."
    mo "Uh-oh! Time for another weebnote!"
    mo "Moe’s a certain type of cuteness that transcends rational grading scales-"
    mo "A type of cuteness you can feel inside of your {i}bones{/i}."
    mo "Like when a girl in an anime gets really nervous on the first day of[school] and forgets how to write her name during her introduction..."
    mo "Or when a tsundere character finally cracks and says something nice to the protagonist."
    mo "It’s a certain type of cute that real humans could never hope to replicate. One that tells you anything and everything about a character from a single action."
    mo "And you, Kendo Princess-"
    mo "You embody moe."
    mo "...Sometimes."

    scene tsuneyocos27
    with dissolve

    t "I see."
    t "It appears that I prematurely judged myself without factoring in your abilities and knowledge."

    if bonus == True:
        t "I apologize for getting angry when you groped me. "
    else:
        t "I apologize for getting angry when you hugged me in the dark. "

    t "I understand now that it needed to be done."
    mo "I mean, I probably could have figured it out without doing that, but..."
    mo "Fan service. You know?"
    t "I do not. Please bestow unto me more of your wisdom, Emerald Guardian."
    mo "Well, Tsuneyo. Fan service is when-"

    scene black
    with dissolve2

    "I decide to head out while the two of them still have their eyes closed."
    "I’m not really in the mood to listen to more weebnotes and I’ve already gotten to see Tsuneyo in costume so..."
    "I guess I’ve accomplished pretty much everything I came in here to accomplish."
    "I’m a little surprised to hear Tsuneyo talk about being embarrassed or...whatever it was she felt, though."
    "It’s not often she lets her actual feelings slip out."
    "But I guess that all of us uncage our true selves from time to time."
    "And, a lot of the time, that kills us."
    "Or, in less drastic circumstances, makes us feel like shit."
    "But sometimes, like tonight in particular, it has the opposite effect."
    "And even though I didn’t stick around for the discussion of fan service, I feel like Tsuneyo gained a few points in...confidence or something."
    "Is confidence a stat in RPGs?"
    "Who even knows?"
    "I’m just going to go home and ask Molly to send me that picture of Tsuneyo."
    "I'm sure her weird pose won't get in the way of my...research."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm15 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm20:
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
    if tsuneyo_love >= 15 and ramen15 == True and day != 1 and tsuneyodorm15 == False:
        jump tsuneyodorm15
...
```