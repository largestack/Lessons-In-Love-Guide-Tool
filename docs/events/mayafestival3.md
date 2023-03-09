# As The Sun Disappears
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayafestival3&go=Go)


Part of event chain [Three Halves Make a Whole](./mayafestival2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: mayafestival3
* Group: Maya
* Triggered by label: mayafestival2

## Event code
File: \game\MayaEvents.rpy
Code:
```python
...
label mayafestival3:
    scene clearnightsky
    with dissolve2
    play music "shrinemaiden.mp3"

    "Let me use this opportunity as the sun disappears to let you in on a little secret."
    "Sometimes, I can’t tell if I’m awake or not."
    "I can’t tell if what is happening is {i}actually{/i} happening or if it’s just more light filtering in through the glass."
    "I can’t tell what I should or shouldn’t believe."
    "Feel or think or say."
    "But I can tell you that I’m glad those moments come."
    "For, if they did not, I’d be the same as you- a disembodied soul floating carelessly through the ether."
    "Living life through the eyes of another because yours have already been taken away."
    "When you were still able to see, what would you wake up to?"
    "And if you could lower yourself into the ground, fully aware and fully conscious, what do you think you’d find?"
    "Darkness?"
    "Probably."
    "But what if it was something a little different?"
    "What if past the dirt and rubble and roots and all of those other things you’d normally find underground, there was something better?"
    "Something wonderful?"
    "Something {i}so{/i} wonderful that, the moment you feast your eyes upon it, you understand that it’s far too good to be true."
    "Maybe the reason I can’t ever tell if I’m awake or not has something to do with that."
    "Do you think we’ll ever see it?"
    "The thing beneath us."
    "The thing above."
    "Two sides of the same coin, cut in half and separated by more distance than one could travel in a lifetime."
    "That’s what we are."
    "It will take too long to become whole again, so we find comfort in quitting because at least that will give us the time to try something else."
    "We’ll always just be half of something, though."
    "How did we ever get this far apart?"
    "How did we separate in the first place?"
    "..."
    "Can I tell you another secret?"
    "..."
    "I’m scared."
    "But no one can ever know that."
    "No one in the middle, at least."
    "I’ll reconsider my position once it’s somewhere else."

    scene mayanightwalk1
    with dissolve2

    m "You know, this weird potato stick thing is actually really good. Perhaps you should just...randomly point at objects to make decisions more often?"
    m "Assuming that’s not how you’re already selecting new members for your harem, of course. "
    s "My decision making process is a little more complicated than that."
    m "I bet. You only have two hands. It sounds difficult pointing at everyone all at once."
    s "So, do you know where we’re headed?"

    scene mayanightwalk2
    with dissolve

    m "More or less. I admit it’s been quite a while since I’ve come here. "
    m "The novelty wears off once you’re forced to go alone over and over."
    s "I’m sure the other versions of me would have come as well if you had asked."
    m "I didn’t want them to."
    s "W-"
    m "Because they weren’t you."
    m "I’m surprised you even need to ask at this point, what with all of your alluding to my alleged {i}true feelings{/i} and whatnot."
    s "Can I take that as a confession?"
    m "No. But you may ask me again on my next birthday and see if the answer has changed."
    s "So another...what, two resets from now? Four?"
    s "There’s no way I’ll remember something that far off."
    m "Could be three. Maybe even one."
    m "We managed to sneak two Christmases into one winter, did we not?"
    s "You know we can spend more time together on days that aren’t your birthday, right?"

    scene mayanightwalk3
    with dissolve

    m "And then what?"
    s "What do you mean?"
    m "If I were to start spending more time with you, something I’ve made you extremely aware that I {i}don’t{/i} want to do in the past...what would happen next?"
    s "Well...we’d get closer."
    m "{i}Uh-huh.{/i} And then what?"
    s "Well, considering you already seem to know how quickly I move in relationships-"

    scene mayanightwalk4
    with dissolve

    m "No. That is absolutely not what I’m talking about."
    m "Do I really need to remind you why we can’t get closer anymore than I already have? Because it’s getting extremely repetitive and I’m {i}kind of{/i} good at dealing with repetition."
    s "It’s not fair that you have to live like this."

    scene mayanightwalk5
    with dissolve

    m "Hearing that from you just makes it worse."
    m "I suppose it is a little nice finally having company again, though."
    m "Now, if only we could predict the future..."
    s "Can I ask you something?"

    scene mayanightwalk6
    with dissolve

    m "I...suppose? You don’t normally ask for permission."
    s "What’s even the point of a “future” for you when you can’t seem to ever get what you want?"
    m "..."
    s "I guess what I’m asking is...if I really am the “real” me, but you can’t get any closer to me without the risk of destroying that..."
    s "What’s the point?"
    m "Well...why would an animal chase a carrot on a stick tied to its back?"
    m "Because it’s stupid and thinks that it might catch it one day."
    m "In my case, though, I’m even dumber than an animal. "
    m "There’s been a stick tied to my back for longer than I can remember and I’m {i}still{/i} chasing after it."
    m "I’m just moving a little slower than I used to while doing that."
    m "Am I ever going to catch it? Probably not. "
    m "But it feels like I’m getting a lot closer sometimes."

    scene mayanightwalk7
    with dissolve

    m "And it’s not like there’s anything else to do in this city."
    m "Anyway, please stop worrying about {i}why{/i} I do the things I do and instead try to accept them."
    m "There’s nothing you can actively do to help with my weird...cosmic curse thing or whatever it is that caused {i}me{/i} to persist but no one else."
    m "You can passively help, though. By just being around and not doing anything stupid."
    m "And occasionally buying me exorbitant amounts of food and allowing me to walk with you in my yukata."
    m "Just that every once in a while is enough for me to keep making it to the roof."
    s "I’m sorry."

    scene mayanightwalk8
    with dissolve

    m "Ew, no. Don’t apologize like that. It’s gross and weird. "
    m "Besides, it’s my fault for getting so attached to something I never should have."
    m "I can only imagine how fun and carefree my life in loops would be if I were even a mere fragment of the person you are."

    if bonus == True:
        m "But, no. I have to spend the rest of eternity convincing my best friend’s uncle to not breed with my friends while he sits back and has breakfast served to him in bed every morning."
        s "I normally go out into the kitchen."
    else:
        s "That's mean. Molding the minds of college students is a very hard job."

    scene mayanightwalk4
    with dissolve

    m "Oh, my apologies. Your life is clearly just as hard as mine then. How could I have been so blind?"
    s "Do you really think there’s a chance you might...“go away?”"

    scene mayanightwalk9
    with dissolve

    m "..."
    s "That’s been stuck in my head since you said it earlier."
    s "And, at the risk of sounding concerned, I’d really prefer that doesn’t happen."
    m "There is nothing wrong with a little concern every now and then."
    m "I have no idea what will or won’t happen. "
    m "I just know that things don’t tend to go well for me very often."
    m "It’s turned me into a bit of a pessimist over the years."
    s "Well, at the bare minimum, I hope I persist in the event that you wind up being reset."

    scene mayanightwalk10
    with dissolve

    m "As do I. "
    m "At least then you’ll know a sliver of what I’ve felt all this time."
    m "Only a sliver, though."
    m "I wouldn’t wish any more than that upon anyone."

    scene black
    with dissolve2

    "Maya and I continue down a gravel path, gradually moving further and further away from the festival. "
    "In fact, I imagine we’ve been moving away from it for quite some time now after getting caught up in conversation."
    "I don’t particularly mind, but I feel a little bad for Maya since I know she wanted to spend more time at the festival itself."
    "The moment I’m about to ask her if she wants to turn around, however-"
    "She stops dead in her tracks."
    "........."
    "......"
    "..."

    scene mayanightwalk11
    with dissolve2

    s "Is this the shrine you were talking about?"
    m "No..."
    m "I have no idea what this is."
    s "Weren’t you just saying a little while ago how you know every nook and cranny of Kumon-mi?"
    m "I’ve been wrong before."
    m "And I guess I’m wrong again now."
    s "Well, we were on our way to a shrine, weren’t we? Why not just go check out this one instead?"
    m "Is there even anyone inside? It seems extremely quiet for a shrine on New Year's."
    s "I doubt we’ll find out without going in."
    m "I don’t know. Something seems off."
    s "Are your supernatural powers tingling or something?"
    m "That’s not it."
    m "It just feels like this would be the two-panel shot at the end of a manga volume."
    s "I can’t imagine I’d make a very good manga protagonist."
    m "I would make up for it. Don’t worry."
    s "Are we going in then? Or does the manga end here?"
    m "I think we kind of {i}have{/i} to go in at this point. We’ve stood here for long enough that this is now an important story beat."
    s "Should I lead the way?"
    m "Probably. You {i}are{/i} the self-proclaimed protagonist after all."
    s "Do you want to hold hands on the way up the stairs?"
    m "Not particularly, no."
    s "Then I guess just..."
    s "Follow me."

    scene black
    with dissolve2

    "The further we ascend, the further the shrine seems to move away from us."
    "I’m sure it’s just an optical illusion or exhaustion kicking in, but it really does feel like something out of a book."
    "The blinding light exuding from the interior of the shrine doesn’t help either."
    "It’s so strong that I’m forced to cover my eyes."
    "I turn back for a brief moment to find Maya doing the same."

    play sound "static.mp3"
    scene mercy1 with flash
    scene mercy2 with flash
    scene mercy3 with flash
    scene mercy4 with flash
    scene mayanightwalk12 with flash
    stop sound

    "Then I turn back around and we’re already inside."

    play sound "static.mp3"
    scene mayanightwalk13 with flash
    stop sound

    "There’s a thing in front of us, pushed through another thing with some things above it."

    s "..."
    m "..."
    m "Well, that was anticlimactic."
    s "How is a shrine out of order, exactly?"
    m "How should I know?"
    s "I mean...you {i}are{/i} a shrine maiden."
    m "I’m only a shrine maiden out of necessity. And in my many, {i}many{/i} years of service, I have not once had to put an “Out of order” sign on anything."
    s "I’m beginning to understand why there’s not anyone here. "
    m "Perhaps “Out of order” simply means that this shrine was abandoned by its god?"
    s "Is that a thing that actually happens?"
    m "Probably. Gods are assholes."
    s "What kind of god do you think it was?"
    m "You know, I’m going to go out on a limb here and assume it was some sort of rabbit. Don’t ask me where I got that idea, though."
    s "So...are we still supposed to pray?"
    m "To what? It’s either abandoned or out of order and neither of those things makes me confident our prayers will be heard."
    s "What makes you so confident your normal prayers will be heard?"
    m "A depressing amount of willpower and a keen sense of intuition."

    scene black
    with dissolve2

    "We stare at the shrine for another moment. "
    "That moment is followed by several other moments."
    "It seems that neither one of us wants to look away for some reason, but it’s not one I can put my finger on."
    "Perhaps we’re just trying to make the best of a long journey to nowhere."
    "But, then again-"
    "That’s what we’re always doing."

    scene mayanightwalk14
    with dissolve2

    "Maya is the first to break free of the rabbit’s hold as she turns around and takes up her normal seiza position, facing the way we came in."
    "I follow her lead and sit beside her, albeit with posture much worse and a significant increase in disrespect."
    "This might come as a bit of a shock to you, but I don’t like places like this."
    "I don’t like religion in general. "
    "Or rather, I don’t like the people who devote themselves to someone or something just because they think they should."
    "I don’t like the immediate acceptance and refusal to question why the focus of their feverish passion doesn’t ever actually {i}do{/i} anything."
    "And yet every morning, I put on this blazer and make my way across town."
    "I take my place behind a podium in a building I should have never been allowed to set foot in."
    "And I revel in the fact that there are so many people exactly like that- focused on me instead of anything else."
    "No god deserves the praise they are given."
    "And neither will I until I do something worthy of obtaining it."
    "But {i}god{/i} will I drink it down anyway."

    s "Why did you become a shrine maiden in the first place, Maya?"
    s "And...how long have you been one?"
    m "Which of those two questions would you prefer I answer first?"
    s "Whichever one has a less convoluted answer."
    m "Sometime around middle school, then."
    m "The end of elementary, perhaps?"
    m "It’s not exactly easy to remember minor details like that from so long ago. But I know it was before [high_school]."
    m "As for {i}why{/i}..."

    scene mayanightwalk15
    with dissolve

    m "Let’s just say I liked the dress."
    s "I kind of want to know the real answer."
    s "If you’re still doing it after all this time, I imagine it must have been a lot more serious than just liking the dress."
    m "I’d quit if I could. Honestly."
    s "Why can’t you?"
    m "Why does it matter?"
    s "You could be using that time for something else."

    scene mayanightwalk16
    with dissolve

    m "Like what? Waiting for you to come knock on my door? Listening to Ayane sing Despacito or helping Ami brush her obnoxiously long hair?"
    m "The shrine is a reprieve from the parts of my life that I struggle with tolerating every hour of the day."
    m "And if it weren’t for the spiritual aspect of it, I’d find it quite nice as my own reclusive hang out spot."
    s "There are other hang out spots, though."
    m "But how many of them will allow me to keep doing what I’m doing?"
    m "I’ve toyed with the idea of leaving before. Especially when I was getting a new {i}you{/i} every four months or so."
    m "But I ultimately decided against it because, on the off chance that there is {i}something{/i} about being a shrine maiden allowing me to persist through each reset-"
    m "Well, I don’t want to risk severing that."
    s "What if severing that connection repairs everything, though?"
    m "What if it doesn’t?"
    m "Besides, there’s absolutely no way this world is convenient enough to just “get repaired” by something as inconsequential as me not sweeping a staircase for several hours each weekend."
    m "The shortened version is that I do not want to risk this world dramatically changing- even with how much I’ve grown to abhor the mundane aspects of it."
    m "If all I’m faced with is a minor inconvenience two days out of every week, I will face it head-on....over and over again until I can no longer stand up straight."
    s "You’re doing all of that for me?"
    m "No, you narcissistic asshole. I’m doing it for everyone. "
    m "I suppose your sliver of the pie chart is a little larger than the others, though. Why that is, I will never understand."
    s "I understand."

    scene mayanightwalk17
    with dissolve

    m "Don’t say it a-"
    s "Because you’re in love with me."
    m "...gain."
    s "{i}Why{/i} you’re in love with me is still far beyond my comprehension, though."
    m "That is literally the exact thing I was saying."
    s "Does {i}that{/i} count as a confession?"
    m "Do you feel your brain liquefying?"
    s "I don’t think so."
    m "Then no. Probably not."
    s "Maybe we can avoid the whole blackout thing if you just think up really creative ways to say it instead of being blunt about it."
    m "Or maybe we can keep doing exactly what we’ve been doing since you “woke up” and maintaining a healthy distance that doesn’t spiral into a never ending pool of regret for both of us?"
    m "I think that sounds fun. Let’s go with that option."
    s "You’re going to break one day and you know it."

    scene mayanightwalk18
    with dissolve

    m "I have no idea what you’re talking about."
    s "You really-"
    m "Stop it. Please."
    m "I’ve heard it enough today."
    s "..."
    m "..."

    scene mayanightwalk19
    with dissolve

    s "Sure."
    s "Did you want to maybe start heading back soon, though?"
    s "As much as I appreciate and understand your love for shrines now, I highly doubt you want to spend the entire night at one."
    m "Back home or back to the festival?"

    scene mayanightwalk20
    with dissolve

    s "Is the festival still going? It seems pretty late."
    m "It should be. We’re quite a way from the main area, but I imagine we would have still heard the fireworks if they were set off."
    m "We missed the ones on Christmas, so I’d like to see these if you’re okay with it."
    s "Why wouldn’t I be okay with it?"
    m "Sorry, you might be fine with it {i}now.{/i} But who knows what would happen if another pink-haired girl were to show up out of nowhere and profess her love to you while we’re on the way?"
    s "I’d have to tell her I’m already on a date tonight."
    m "This isn’t a date."
    s "..."
    m "What? It’s not."
    s "Sure, Maya."

    scene mayanightwalk21
    with dissolve

    m "It’s not!"
    s "Uh-huh. Whatever you say."
    s "I'm going to start heading over now."

    scene mayanightwalk22
    with dissolve
    stop music fadeout 8.0

    m "It’s not a date!"
    s "Can’t hear you. Walking away."
    m "I mean it!"

    scene mayanightwalk23
    with dissolve

    m "..."
    m "..."
    m "..."

    scene mayanightwalk24
    with dissolve

    m "Hah..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mayafestival3 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump mayafestival4

label mayafestival4:
...
```

## Code that triggers this event
File: \game\MayaEvents.rpy
Code:
```python
...
m "Am I? Because I’m pretty sure I’ve asked you to kill Noriko on several occasions and, if anything, I think I’d prefer to keep the squid alive if I had to choose between the two of them."
    s "I can’t wait until the day you two make up and start being friends. It’s going to be so sweet."

    scene mayafestival22
    with dissolve

    m "Ew, stop. At least wait until I finish eating to start saying stuff like that."
    s "Maya, there is so much food here that it is going to take you the rest of the festival to eat it all even {i}if{/i} you manage to eat at your normal breakneck pace."

    scene mayafestival23
    with dissolve

    m "Do not underestimate my love for food."
    m "Festivals are to me what the dorm rooms of [teenage]girls are to you- a place where I can be free. Where my hunger can never be sated."
    s "I don’t know. My hunger is normally sated after half an hour or so. Sometimes, even less."

    scene mayafestival24
    with dissolve

    m "Why do you say things like this to me?"
    s "Because I know you won’t think any less of me."
    m "I literally can {i}not{/i} think any less of you."
    s "Yeah, exactly."
    m "..."
    s "..."
    m "Itadakimasu."

    scene black
    with dissolve2

    "One by one, Maya tears into each plate and-"
    "Well, I guess {i}tear{/i} probably isn’t the right word since she somehow manages to look graceful even while consuming more than some villages do in an entire week."
    "But she eats everything without lessening her pace even once."
    "The sun begins to set as she does so, and the air begins to turn a bit colder- but that’s to be expected since it is {i}technically{/i} still winter."
    "Sure, the two of us were gifted a relatively warm day by Mother Nature, but only until it was time for her to go out and party with her other cougar friends."
    "As Maya eats, well, {i}everything-{/i} I slowly pick at a bowl of ramen that, at least to my unrefined palate, doesn’t compare much to what Tsuneyo makes."
    "But it’s warm enough to battle the encroaching cold and gives me something to do while waiting for the first stage of Maya’s favorite day of the year to end."
    "........."
    "......"
    "..."

    if amifingered == True:
        scene mayafestival25
        with dissolve2

        m "MMMMMM!!!!!~~~~"

        "Just as she said she would, Maya saves the watermelon for dessert."
        "And yes, she did finish {i}everything-{/i} including the remainder of my ramen which, despite my worsening hunger, I was not able to finish."
        "I recall her saying in the past that she doesn’t like being watched while she eats and, this isn’t me being weird or...fetishy, but I’m glad she seemingly abandoned that insecurity today."
        "There’s something oddly satisfying about seeing a girl so far detached from joy being enveloped by it that I can’t help but feel a little warmer inside."
        "Maybe that’s why I couldn’t finish my food."
        "I was already warm enough."

        s "Enjoying yourself?"

        scene mayafestival26
        with dissolve

        m "A bit."

        "Smile Count: 5"

        m "And you?"
        s "For now. I’m sure that will change once I look at my credit card statement."
        m "At least Ami will still have a home when your house is repossessed."
        s "So, what’s the next phase of your game plan now that you’ve eaten from roughly every stand at this festival?"
        m "Hmm..."
        m "Have you changed your stance on goldfish at all in the last hour or so?"
        s "I can’t say I have."
        m "Then I suppose it would be best to avoid Kingyo-Sukui. Or any other games for that matter since you’re horrible at them and I don’t want any of the prizes."
        s "Pretty sure that just leaves more food, then."
        m "Don’t forget what day it is. We still need to visit a shrine and pay our respects for the year or god might kill us. That seems like a thing he would do."
        s "God sounds like an asshole."
        m "You’re just realizing that now?"
        s "Nope. Just reinforcing the belief with some help from you."
        s "I guess we can get our fortunes while we’re there too. That seems like another...{i}festivaly{/i} thing to do."
        m "Not necessary."
        m "I draw the same one every time."

        scene black
        with dissolve2
        stop music fadeout 10.0

    "We collect our garbage, dropping everything off at a nearby receptacle."
    "The squid (Still alive, albeit just barely) is left there as well- clinging to life atop a stack of dirty plates."
    "It covers its body in a variety of sauces, seasoning itself before death, in a desperate attempt to seek out water and prolong its unappreciated existence."
    "Neither of us have the heart to kill it, but we have the heart to watch it die."
    "And that must count for something."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayafestival2 = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump mayafestival3
...
```