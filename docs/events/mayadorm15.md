# Takoyaki (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 15

* Event [You and Me](./shrine15.md) (Maya) is completed)



## Next events

* [Main: Rewrite](./day102.md)
* [Maya: Nothing is Real](./shrine20.md)

## Event properties

* Id: mayadorm15
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm
* Triggered by path: mayadorm->mayadorm15

## Official wiki page

[Takoyaki](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm15&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm15:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Maya's door and wait for her to answer, figuring that the chance of her doing so is somewhere around 25%%."
    "That number greatly increases when I hear footsteps approaching just seconds later."

    scene takoyakiredux1
    with fade
    play sound "dooropen.mp3"

    m "What do you want?"
    s "Just to say hi."
    m "Hello."
    m "Goodbye."
    s "Wait. There's more."
    m "Is there? Or are you just pretending there is more because you don't want me to leave right away?"
    s "I guess it would be closer to the latter. But that doesn't mean there can't...{i}be{/i} more?"
    m "Can I help you with something? Or is listening to you mindlessly flounder just what I'll have to do for the rest of the night?"
    s "I don't think I need any help, no. But what about you?"
    s "Need me to, like...carry any boxes or something?"
    m "Is that something you would do right now if I asked you to?"
    s "I'd rather not, to be honest. I just don't know what else you normally do at night."
    m "I see. So you’re here to harass me and not assist me."
    s "Well, I wouldn’t say {i}harass{/i}..."
    m "Then what would you say? Annoy?"
    s "You know, I’m starting to get the feeling you don’t really like me all that much."

    scene takoyakiredux2
    with dissolve

    m "What would have possibly given you that idea?"
    s "A hunch, I guess. Combined with the fact that every time the two of us talk, you look like you're about to either vomit or fall asleep. Or both."
    m "You're disgusting."

    scene takoyakiredux3
    with dissolve

    m "But...perhaps there is something you could do for me after all."
    s "Does it involve a box?"
    m "No. But it involves following me roughly two miles west."
    s "That’s...a strange proposition."
    m "Is it?"
    s "Yes. And, if I didn't know any better, I'd say it might even sound like a date."
    m "If your idea of a {i}date{/i} is following someone for two miles in the dark, I hope that you never find love for the rest of your life."
    s "I won't, for my heart already belongs to you."

    scene takoyakiredux4
    with dissolve

    m "Ha ha ha. Hilarious."
    m "I take it you'll have no qualms with buying me dinner, then? Since your {i}heart belongs to me{/i} and all."
    s "Huh? I mean...I guess I can get you dinner. But why do we need to walk two miles away for it? There are plenty of closer places."

    scene takoyakiredux1
    stop music fadeout 10.0

    m "Is that a no? Because I am very hungry and don't have much money to spend right now."
    s "If I say no, what's the alternative? Panhandling?"
    m "I’m an incredibly attractive teenage girl. I'm sure there is {i}something{/i} I could be doing at this time of night to come up with the money."
    s "I...don't like the sound of that. So, sure. I'll buy your dinner tonight under the pretense that you never say anything like that again."
    m "Look at you, masking your jealousy as genuine worry. How adorable."

    scene takoyakiredux0
    with dissolve

    "Maya breaks eye contact with me and begins to head for the exit. The scent of watermelon shampoo drifts past me along with her body."

    m "Come. I would like to get there as soon as possible."

    scene black
    with dissolve2

    "I chase after the scent."
    "Down the stairs."
    "Out of the dorm."
    "Into the street."
    "........."
    "......"
    "..."

    scene takoyakiredux5
    with dissolve2
    play music "thesleepingcity.mp3"

    s "So...where are we going exactly?"
    m "Does it matter?"
    s "Kind of, yeah. I don’t want you dragging me to some weird cult meeting or something."
    m "I see."
    m "Then you should probably head back."
    m "I’m taking you to meet god."
    s "Uh..."
    m "That was a joke. Ha ha."
    m "You may laugh now. "
    s "You’re so fucking weird."

    scene takoyakiredux6
    with dissolve

    if bonus == True:
        m "You have no right to say that when you spend every waking moment stalking girls roughly ninety years younger than you."
        s "I feel like your estimation of my age goes up several years every time we talk."
    else:
        m "You have no right to say that when you can't even put your shirt on the right way."
        s "What are you talking about? Of course I- ah! What have I done?!"

    m "Poor you..."
    s "Just tell me where we’re going and I’ll be quiet the rest of the way. I promise."

    scene takoyakiredux5
    with dissolve

    m "As if I would believe that."
    s "..."
    m "..."
    s "..."

    scene takoyakiredux7
    with dissolve

    m "Takoyaki..."
    s "…"
    s "We’re walking two miles away for fried octopus balls?"
    m "I’m fine with going alone if you just give me the money."
    s "You know, you're lucky I'm such a generous guy or-"
    m "What happened to remaining silent after hearing the answer?"
    s "I didn't expect the answer to be something so...odd."
    m "What's so odd about takoyaki? It's an extremely common street food."
    s "Yes. So common that we can find it significantly closer than two miles away."
    m "And yet you're still following me instead of just handing over the money."
    s "..."
    m "..."
    m "It's not too late to back down, you know."
    m "It's not like either one of us is going to have a good time."
    s "Nah. I'm in it for the long haul at this point."
    m "I see..."

    scene takoyakiredux5
    with dissolve

    m "Then I suggest you remain quiet until we get there."
    m "I did as you asked, so now you must do as you were."
    s "..."
    m "..."
    s "Fine. Whatever. But don't come crying if you get bored along the way."

    scene black
    with dissolve2

    "I decide it's easier to remain silent than give up my money and wind up silently following Maya to wherever her...takoyaki-related destination is."
    "We walk closer together than we did when I carried her boxes."
    "The scent of shampoo returns each time a breeze kicks up and I conjure up the image of her with her hair pinned back in the bath to battle the awkward silence this night has thrown at me."
    "It’s colder than usual. Almost like it's not even summer anymore."
    "Part of me wonders if she would want to wear my jacket."
    "But then the other part of me realizes that she’d likely insult me for even offering her anything that has touched my skin."
    "And so we remain several feet apart."
    "And she remains cold."
    "........."
    "......"
    "..."

    scene takoyaki1
    with dissolve2

    "We show up at a two-window food stall situated in the middle of nowhere."
    "Well, I say the middle of nowhere, but it’s more like a suburban area I’ve never seen before."
    "How does Maya even know about a place like this?"
    "And what’s the point in coming all the way out here just for takoyaki when there were countless other places she could have gone?"
    "Common sense dictates that the reason would be one of two things-"
    "Either she prefers the taste of this specific takoyaki cart's food-"
    "Or it holds some sort of significance for her."

    scene takoyaki2
    with dissolve

    "The two of us walk up to the stall and I position myself away from the window to show I’m not interested in personally buying anything."
    "I’m simply here to pay for the dinner of my [niece]’s best friend- a totally normal scenario that I'm sure every uncle has to deal with several times a year."
    "Maya peers through the window and speaks to someone it appears she knows."

    scene takoyaki3
    with dissolve

    m "The usual, please."

    "An old man behind the counter nods, grunting to acknowledge her order."
    "He's one of very few men that I have actually seen around here, so I imagine he wasn't drafted due to either his age or...some sort of condition I'm not aware of."
    "He likely doesn’t have much time left anyway."
    "Better to die serving octopus than to die in space, I guess."

    scene takoyaki4
    with dissolve

    m "Do you want anything?"
    s "Wow, kind enough to let me buy things with my own money?"
    m "Is that a yes or a no? I need to know before he’s finished or he’ll get angry."

    "The old man lifts his head and his eyes meet mine."
    "I can already see a scowl beginning to form on his face, but he says nothing."
    "He just...stares at me."

    s "I’m fine. I’ll just pay for whatever you’re having."
    m "I see."
    m "Maybe another time, then."

    scene black
    with dissolve2

    "The man finishes Maya’s order and presents her with several trays of takoyaki."
    "I need to help carry them as her arms are too small to do it on her own."
    "The scent of watermelon shampoo is unfortunately consumed by one significantly more pungent."
    "........."
    "......"
    "..."

    scene takoyaki5
    with dissolve2

    s "…"
    m "…"
    s "Aren’t you going to eat?"
    m "It makes me uncomfortable with you just watching me like that."
    s "Is it because you eat at the speed of light and are afraid of somehow ruining your image in front of me?"
    m "I doubt there is {i}anything{/i} I could do to make you less attracted to me, but I would be a liar if I said I was not a little self-conscious."
    s "Are you? If I could eat the way you do, I'd be showing everyone."
    m "Wow. It’s almost as if we’re completely different people or something. Whoever could have predicted this?"
    s "I don’t appreciate the sarcasm, Maya. Especially right after I just bought you dinner."

    scene takoyaki6
    with dissolve

    m "Oh, you’re right. Thank you for buying all of this for me."
    s "Wait, are you actually thanking me? Because I was just messing around about the whole eating in front of me thing."
    s "I really don't care what you do or don't do with the food I bought you. It's yours to...eat or...throw or whatever."
    m "Do I look like the type of person to start throwing octopus balls around?"
    s "..."
    m "..."
    s "Maybe?"
    m "I am greatly offended by this."
    m "Thank you, though. Even if you are the worst person I have ever met, I'm grateful that you bought dinner for me."
    s "It's whatever. I’ve got some money to spare."
    s "It’s not like I’m constantly paying for takeout or anything since Ami is always cooking at home, so...it's really no big deal."

    scene takoyaki7
    with dissolve

    m "I see."
    m "Then...perhaps we might return here sometime."
    s "Are you...actually saying we should do this again? Because that really {i}does{/i} make it sound like a date this time."

    scene takoyaki6
    with dissolve

    m "I’m merely accepting my fate."
    s "This again?"
    m "Again?"
    s "Well...didn’t we just have a discussion about fate the other day at the shrine?"
    m "Ah, yes. When you decided to act out of character. I remember now."
    s "…"
    m "…"
    s "So...do you want to continue that discussion? Or..."
    m "No thank you."
    m "There is something else I would like to discuss, though."
    s "Well, that's new. It's not like you to actually {i}want{/i} to talk about something with me."
    m "It's less that I {i}want{/i} to and...more that I feel I {i}should.{/i}"
    m "Besides, do you really think I would have come all the way here with you if I did not have something to discuss?"
    s "That’s slightly offensive, but you've got a point."
    s "I’ll hear you out. Just try not getting {i}too{/i} weird this time."
    m "I will do my best, but I surely expect you to think I've failed immediately."
    s "What do you mean?"

    scene takoyaki8
    with fade

    "Maya stabs a toothpick into a piece of takoyaki and twirls it around to cool it off, causing some of the fish flakes to fly off and get carried away by the wind."

    m "You’re..."
    m "You're changing too quickly."
    s "Yeah, you've failed immediately. That's already a little too weird for me, but I'll continue to humor you."
    s "Changing how? What do you mean?"
    m "You’re doing things you’re not supposed to."
    s "Is this just another strange way of telling me to leave you alone? Because-"
    m "No."
    m "This is something much more serious than that."

    scene takoyaki9
    with dissolve

    m "Something...is going to happen very soon."
    m "Something that may...confuse you."
    s "Is it our next meeting? Because if so, I think you might be onto something."

    scene takoyaki10
    with dissolve

    m "I know it's hard for you, but please try to be serious for a moment."
    s "..."
    m "..."
    s "Okay...Sure."

    "I can feel my shoulders tense up a bit, but I'm not sure if it's due to her expression or the uncertainty of whatever she's about to tell me."
    "Either way, she's being more serious than normal and...it wouldn't be fair to just ignore that."

    scene takoyaki11
    with dissolve

    m "Something is...very different about you."
    m "And I’m not just talking about your rebirth. That’s old news as far as I'm concerned."
    m "We’ve already discussed how everything in the world is part of a cycle..."
    m "And how everything will end in the same place regardless of what you or I may want at that moment in time."
    m "But what do you think would happen if those cycles were to converge?"
    s "What? What do you mean by that?"
    m "I mean...Would you be able to handle the memories of hundreds of thousands of lifetimes if they were to all rush in at once?"

    scene takoyaki12
    with dissolve

    m "Or..."
    m "Would something like that break you?..."

    "Maya looks away in an expression even more unfamiliar than the one she gave me just moments ago."
    "This no longer sounds like just another one of her philosophical ramblings."
    "This sounds like a warning."

    s "…"
    m "…"
    s "Beats me, I guess."

    scene takoyaki13
    with dissolve

    m "Huh?"
    m "{i}Beats me?{/i} That's your response?"
    s "Was that...the wrong answer?"
    m "There is no {i}wrong{/i} answer. I just expected you to call me crazy or come up with some stupid joke, not shrug it off like it's some type of pointless {i}what-if.{/i}"
    m "I'm asking you this for a reason. Not just because I'm curious about your point of view."
    m "This really is serious. And it deserves a serious-"
    s "I am serious, though. Which is exactly why I'm not...making jokes or mocking you right now."
    s "What's a more reasonable response to someone being bombarded by the...memories of hundreds of thousands of lifetimes rushing in at once or...whatever it was you said?"
    s "That's not something a normal person would have an answer to off hand."
    s "If that happens, I'll just...deal with it, I guess."
    s "But...to more directly answer the second part of your question-"
    s "No."
    s "I don't think something like that would break me."
    m "I..."
    m "I can't bring myself to believe that."
    m "You don't know what it would be like. You have no idea what sort of effect that could have on a person."
    s "Hey. You asked and I answered. I didn't think we were going to be having a whole debate about this."
    m "..."
    s "..."

    scene takoyaki14
    with dissolve

    m "You...really are strange..."
    s "You’re one to talk."

    scene takoyaki15
    with dissolve

    m "Hah..."
    m "I guess that answer wasn’t {i}horrible{/i}, though..."
    m "We’ll just have to see how things play out from here."
    m "But...for your sake...I really hope you're right."
    s "You're actually caring about {i}my{/i} sake for once? I figured you'd be wishing for the exact opposite."
    m "Yes, well...that's because you don't understand me at all."
    s "You...definitely don't make it easy for me, at the very least."

    scene takoyaki16
    with dissolve

    m "No...I suppose I don't."

    scene black
    with dissolve2

    "The discussion quickly moves away from more serious topics after that."
    "Maya winds up biting the bullet and eating her takoyaki in front of me while I continue to look on as if her consumption of octopus is some new form of spectator sport."
    "She paces herself, though...proving once and for all that she really is still a [teenage]girl at the end of the day."
    "The two of us walk back to the dorm in silence after she finally finishes her dinner."
    "And while I say {i}silence{/i}, the true soundtrack of the trip home is the endless screaming of cicadas and the soft clopping of Maya's boots against the ground."
    "I can still smell the takoyaki."

    $ renpy.end_replay()
    $ mayadorm15 = True
    $ maya_love += 1
    stop music fadeout 10.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amifingerreplay:
        play sound "knock.mp3"
        "..."

        a "Wait! Hold on a sec!"

        "A moment of silence goes by before I hear some shuffling and then footsteps leading to the door."

        a "Okay! You can come in!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump amifingerreplayx
        else:
            $ ami_lust += 1
            stop music fadeout 4.0

            "{i}Ami's lust has increased to [ami_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label amihjreplay:
        play sound "knock.mp3"
        "..."

        a "Wait! Hold on a sec!"

        "A moment of silence goes by before I hear some shuffling and then footsteps leading to the door."

        a "Okay! You can come in!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump amihjreplayx
        else:
            $ ami_lust += 1
            stop music fadeout 4.0

            "{i}Ami's lust has increased to [ami_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label amidorm15:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
        if maya_love >= 15 and shrine15 == True and mayadorm15 == False:
            jump mayadorm15
...
```