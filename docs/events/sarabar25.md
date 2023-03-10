# Tell Me When (Sara)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sara love greater than or equal to 25

* Event [A Thing of the Past](./yukidate10p2.md) (Yuki) is completed)



## Next events

None

## Event properties

* Id: sarabar25
* Group: Sara
* Triggered by label: sarasbar
* Triggered by branch label: sarasbar
* Triggered by path: sarasbar->sarabar25

## Official wiki page

[Tell Me When](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sarabar25&go=Go) for more details.

## Event code

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarabar25:
    scene barnight
    with dissolve2
    play music "sidecharacter.mp3"

    "I make my way to the bar."
    "No one is there."
    "Though, I imagine that’s on account of the sign on the door saying they’re closed for the night."
    "I’m not sure why Sara chose {i}now{/i} to take a night off when she’s finally [[kind of] on the cusp of turning things around for the place."
    "But I guess I’m not one to spend too much time questioning her decisions when she’s made so many poor ones in the past that they’re starting to lose their novelty."
    "Regardless, I doubt she’s far."

    if bonus == True:
        "In fact, knowing her, she’s probably upstairs getting drunk...or masturbating to pictures of me as we speak."
    else:
        "In fact, knowing her, she’s probably upstairs getting drunk...or looking at pictures of me as we speak."

    "I’m not sure where she’d get any, considering I don’t think I’ve posed for a photo even once since waking up here-"
    "But Ayane’s sure had no problem procuring images of me, so maybe Sara just bought them from her?"
    "I don’t know. "
    "I’m done standing around down here, though. "
    "If I’m going to come all the way over to a failing bar in the middle of the night, I’m at least going to get something out of it."

    if sarasex == True and bonus == True:
        "And whether that be a blowjob or just some quality time with a friendly neighborhood MILF, I’m sure that whatever happens will be, at the bare minimum, worth walking a few miles."
    else:
        "And whether that be a free beer or just some quality time with a “friend,” I’m sure that whatever happens will be, at the bare minimum, worth walking a few miles."

    scene black
    with dissolve

    "The stairs creak the same way they always do, as I’m sure it’s been decades since this building has received any sort of renovation."
    "And I’m sure it’ll be a few decades more until it {i}is{/i} renovated (If Sara even still owns it by then)."
    "But stairs aren’t all that important."
    "You can let them rot and decay and still manage to make your way up just by stepping around all of the soft spots. "
    "The worst case scenario is that your leg will bust through an old plank and maybe tear some skin off or rip your pants in the process-"
    "But you’ll still get to where you’re trying to go."
    "Until you don’t, that is."
    "But I don’t know why I’m telling you this."
    "I ascend."

    scene saranewapt1
    with dissolve2

    "I walk into Sara’s place to find that she must have taken the liberty of redecorating recently. "
    "There’s some sort of movie on her television (Which also looks rather new), but I can’t be bothered to figure out what it is since I’m too busy taking in the rest of the sights. "
    "It’s warm inside- much warmer than in the corridor that carried me here. "
    "And the residual scent of old alcohol and vomit has been replaced by a sweeter smell of cinnamon and...some other indiscernible spice."
    "Sara locks eyes with me, not feeling the need to say hello as, apparently, I’m just welcome to intrude on her privacy whenever I want now-"
    "But Sana doesn’t react. Or perhaps it’s more like she doesn’t notice."
    "She just keeps her eyes centered on the movie that I can’t be bothered to watch and attempts to either fade into obscurity or simply just enjoy some rare time alone with her mother."
    "I don’t think I should be here right now."

    sar "Oh, good. I was worried that I was going to have to get up."
    sar "Can you pour me another glass of wine? There’s an open bottle on the counter over there."
    sar "Also, any compliments regarding my super awesome interior design skills are welcome. "
    sar "I was in the mood for a little spring cleaning earlier and, well, one thing led to a whole bunch of other things that led to this place looking almost brand new."
    sa "We don’t...even {i}get{/i} Spring here, though..."
    s "If I didn’t know better, I’d think you just bought a whole new place."
    sar "Less talking, more pouring. "
    sar "I know you’re not much of a wine guy, but feel free to help yourself to some as well. You know, as thanks for your service and whatnot."

    scene saranewapt2
    with fade

    s "Better idea- how about I just block your view of the TV instead?"
    sar "All those discounted drinks and exceptional service and {i}this{/i} is how you repay me? "
    sar "Oh well. I can just {i}not{/i} drink. "
    s "Or, you know, help yourself instead of relying on someone else to do your bidding."

    scene saranewapt3
    with dissolve

    sar "But if I get up, there’s a chance you’ll steal my seat and ruin our wonderful and extremely overdue mother-daughter night."
    sa "You know this...couch can fit a lot more than just the two of us...right?"

    scene saranewapt4
    with dissolve

    sar "But then I’ll be further away from you and won’t be able to constantly admire how adorable you’ve become!"
    sa "Umm...Sensei...I’m...pretty sure the sign downstairs said that we were closed..."
    s "Yeah, I know."
    sa "..."
    sa "So...you came in anyway?..."
    sa "And then...proceeded to...just come upstairs?..."
    s "I didn’t think that sign applied to me since I’m basically just another employee here at this point."

    scene saranewapt5
    with dissolve

    sar "What kind of employee won’t allow their boss to drink on the job?! Or wipe down tables?! Or restock the cooler?! Or do literally anything ever?!"
    s "The same kind who’s apparently intruding on what’s supposed to be an...important night, I think?"

    scene saranewapt6
    with dissolve

    sar "Yeah. But if anyone was going to intrude, I’m glad it was you."
    sar "Especially since I’d say you’re closer to being Sana’s dad than an employee of the Sakaki-bar-a at this point."
    sa "Can you...please stop saying that every time we’re in the same room together?..."
    sar "But if I keep saying it over and over again, Sensei will eventually start believing it and we’ll finally have a full family again."

    scene saranewapt7
    with dissolve

    sar "You could finally know what it’s like to have a male authority figure in your life, Sana!"
    sa "I don’t even have a...female authority figure in my life..."
    s "I can not allow this conversation to proceed without informing you that no amount of words will make me just suddenly believe I’m a member of this family."

    scene saranewapt8
    with dissolve

    sar "I wouldn’t be so sure if I was you. For all we know, some stuff could happen out of nowhere that makes you change your mind entirely."
    s "Doubtful."
    sar "I’m just saying, it wouldn’t be the first time a teacher fell victim to my feminine wiles. It’s not like there’s no precedent for this."
    sar "Just give me a little warning in advance if you decide to leave me for someone else so I can actually try and prepare this time and not have to raise Sana on my own."
    sa "..."
    s "I’m pretty sure Sana’s able to raise herself at this point."
    s "Well, apart from the whole still being terrified of talking to other people part."

    scene saranewapt9
    with dissolve

    sa "Hey! I’ve gotten a lot better since you started helping me!"
    s "True. But that doesn’t change the fact that you’re still exponentially worse than virtually everyone other than like...Yasu and {i}maybe{/i} Tsuneyo."
    sar "You {i}have{/i} improved a lot, Sana. Which means that Sensei has already done a lot more for you than your real father ever did."

    scene saranewapt10
    with dissolve

    sa "Why do you have to keep comparing the two of them?...Why can’t Sensei just be Sensei?"
    s "I would also like to remain Sensei if that is at all possible."
    sar "I’m not trying to compare them. I’m just saying that-"

    scene saranewapt11
    with dissolve

    sar "Well, a family of two can feel pretty lonely at times."
    sar "I love spending time with just us, but I miss the feeling of there being more sometimes."
    sar "And Sensei’s the closest we’ve had to..."

    scene saranewapt12
    with dissolve

    sar "A...male family member since-"
    sa "Since my dad left, I know."
    sar "..."
    sa "I just...don’t think it’s right to drag him into that without...considering how he feels first..."

    "You know, this might be presumptuous of me, but I’m pretty sure Sara wasn’t alluding to Sana’s father just now."
    "Which, of course, would mean that her daughter was going out on a limb to protect her- the same way I’m sure she’s done plenty of times in the past."
    "The two of them can’t keep running forever, though."
    "There has to come a day, for {i}Sara{/i} especially, when the two of them accept what they went through and finally stop putting bandages over a gash that obviously needs stitches."
    "The probability of that wound getting infected grows greater every day, and there’d be no point in meetings like this at all if one of them had that infection spread to their heart or their brain or something."
    "I’m not a doctor. I don’t really know where infections spread to- or even how they start in the first place."
    "I just know how easy it is for them to fester."
    "I know a little too well."

    sar "Yeah."
    sar "Since your dad left."

    scene saranewapt13
    with dissolve

    sar "You know, he was a real jerk! Like, it’s one thing to knock up a teenage girl, but to {i}abandon{/i} her and force her to be a single parent before she can even legally rent a car?"

    sar "What the fuck is that?!"
    sa "Do you...even know how to drive?"
    sar "No! But still! "

    scene saranewapt14
    with dissolve

    sar "Ugh. And he was so great at first, too."
    sar "Well, great is probably being a little too generous. But I {i}genuinely{/i} thought he was right for me and that all of the suspicions I had over the years were just me being paranoid."
    s "Wait a second, you suspected he was seeing other people and {i}still{/i} managed to...get as far into the relationship as you did?"

    scene saranewapt15
    with dissolve

    sar "Yeah. But you’ve gotta remember- I wasn’t really in the greatest place when I was in high school."
    sar "I thought that being paranoid and...not feeling confident about anything was just how teenage girls were {i}supposed{/i} to feel back then."
    sar "And when you’re that age and dating an adult, those feelings wind up getting even bigger than how they started out."

    scene saranewapt16
    with dissolve

    sar "Of course, he’d always assure me that I was the only one who mattered to him and that he’d never think of seeing someone else-"
    sar "But I’m sure that’s exactly what he told the other girl! Or...girls."
    sar "I don’t even know if it was just one person or not."

    if bonus == True:
        sar "Hell, for all I know, he could have been screwing his entire class back then."
        sar "Sorry for the language, Sana. Your mother’s getting pissed off."

    s "Wow. This guy sounds like a real scumbag."

    if bonus == True:
        "He also sounds like me."
        "But I guess those two things are close to interchangeable at this point."

    scene saranewapt17
    with dissolve

    sar "You know...I kind of wonder what he’s up to sometimes."
    sar "Not because I want to see him or anything, I just want to know whether or not he’s happy with the mess he made of his life."
    sar "And also because I’d want to point out to whatever girl, {i}or girls{/i}, that he wound up with that he’s an unfaithful jackass who walked out on the cutest daughter in the world...as well as her super cool mom."
    sa "Um...th...thank you?..."

    scene saranewapt18
    with dissolve

    sar "Don’t mention it, sweetie."
    sar "I love you. And I just want you to have the best life possible. And I..."
    sar "Well...Sometimes, I don’t think I’m able to give you that sort of life on my own."
    sa "Um...that’s...uhh..."

    scene saranewapt19
    with dissolve

    sar "But I guess I can’t just rope Sensei into being your new dad if that’s not something he already wants."
    sar "But that’s still not going to stop me from looking at him as the closest thing we have to another family member right now."
    s "Really? {i}I’m{/i} the closest thing? Because you’ve known Haruka and Maki significantly longer than you’ve known me."

    scene saranewapt20
    with dissolve

    sar "True. But my daughter doesn’t like either of them even half as much as she likes you."
    sa "M-Mom!"
    sar "And, between the three of us, I don’t like either of them as much as I like you either."

    if sarasex == True:
        "I would sure hope not."

    sar "Does it really matter how long I’ve known you? Am I not allowed to like you as much as I do until a certain date and time?"
    sar "Because if that’s the case, tell me when and I’ll mark it on my calendar right now. I’m serious."
    sa "S-Stop saying embarrassing stuff like that! It’s weird and neither of us like it!"
    s "I mean, I didn’t say-"
    sa "It’s weird and none of us like it!"

    scene saranewapt21
    with dissolve

    sar "Okay, you go. It’s your turn to say embarrassing stuff to Sensei so he’s forced to choose which one of us he wants to be closer to."
    sa "I think I’d rather just...not say anything..."
    s "And I think I’d rather never be forced into making a choice as horrible as that."
    s "I will gladly accept both of you, but keep you far enough away that you can not, officially or {i}un{/i}officially, indoctrinate me into the Sakakibara family."
    s "I refuse to be a part of a dynasty as bad at naming things as you two."

    scene saranewapt22
    with dissolve

    sa "I didn’t...really have anything to do with naming the bar..."
    sa "But...thank you for...staying away..."
    sar "Leave my bar alone. What did it ever do to you besides give you a place to spend your nights instead of at home with your [niece]?"
    s "It also refused to serve me tonight, but I guess I’m willing to overlook that on account of you two playing catch-up or whatever."

    scene saranewapt23
    with dissolve

    sa "Well...we {i}were{/i} playing catch-up...but I think I only have a little while left until I have to go back to the dorms..."
    sar "That’s right. You only had until the end of the movie, didn’t you?"
    sar "What happens if we rewind it? I have the cool kind of cable now where you can actually do that. "
    sar "Would that mean we can just keep sending you back in time until you don’t have to leave anymore?"
    sa "No, Mom...that’s...not what it would mean..."
    s "My bad for showing up and throwing a wrench in your plans. Just leave a note for me next time if you don’t want me coming up."
    sa "I...kind of thought the “We’re closed” sign was...that note..."

    scene saranewapt24
    with dissolve

    sar "It’s fine. "
    sar "Sure, Sana and I don’t really get many chances to spend time alone outside of the bar anymore..."
    sar "But I’m hoping that might be able to change some day..."
    sar "Business has been picking back up and, who knows? Maybe in a few months, I’ll be able to hire {i}another{/i} new employee so Sana and I take some time off together?"
    s "Just hire Kaori full time. I’m beginning to think there are ten or eleven of her that just share the same stream of consciousness."
    s "There is no other way she’d be able to be in so many places at once, so I think that might actually be what’s going on."
    sar "She’s actually still working for a competitor several nights out of the week, so she can’t be here full-time. But I’d be open to it if she ever leaves that place."
    s "Well, hopefully if you’re lucky, it will be swallowed by a sinkhole and things will just automatically get better for you."
    s "It happened for me, to some extent, so it’s not impossible."
    s "Though I guess “better” would be up for debate depending on exactly what you’re trying to get out of-"
    sa "Shh..."
    sa "They're about to...blow up the Death Star..."
    s "..."
    sar "..."

    scene black
    with dissolve2

    "Sara and I humor Sana and decide to stay quiet for the rest of the movie. "

    if bar50 == True:
        "It doesn’t last much longer and, once it’s over, Sana gathers her things and turns to look at me before heading to the door."

        sa "Umm...S-Sensei?..."
        s "Yeah? What’s up?"
        sa "Can I...umm..."
        sa "Can I talk to you for a minute?..."
        sa "In...private?..."
        s "Oh, yeah. Sure."

        "Sara pretends to not hear this and, very surprisingly, actually gives her daughter a little bit of privacy for once."
        "As such, I follow Sana to the foyer to see what it is she wants to talk to me about."
        "........."
        "......"
        "..."

        scene saranewapt25
        with dissolve2

        "The two of us stand there for a moment in what isn’t {i}technically{/i} silence due to the background noise of the television- but it sure as Hell feels like it."
        "I’m not the one who summoned this meeting, though, so I’ll be damned if I’m the one to break the silence."
        "Go on, Sana."
        "Air out your worries to me so that I may either discard them as I see fit-"
        "Or give you a shoulder to lean your head on (Likely with the help of a stepping stool)."

        sa "I...um..."
        sa "So...do you remember the...last time the two of us were up here together?..."

        if bonus == True:
            s "Obviously. You freaking out on me isn’t something that’s particularly easy to forget."

            scene saranewapt26
            with dissolve

            sa "I..."
            sa "I asked my mom about...what I found..."
            s "..."
            s "The sex toy? Or the things you yelled at me for?"

            scene saranewapt27
            with dissolve

            sa "O-Obviously the...things I yelled at you for!"
            s "Got it."
            s "Then what?"

            scene saranewapt28
            with dissolve

            sa "Well..."
            sa "She...told me they...weren’t yours..."
            sa "And then she...threw them all away because she said they were old and..."
            sa "Umm...did you know that...that those things can...expire?..."
            s "Yes, and I feel very bad for anyone who holds on to them so long that they actually do."
            sa "Y-Yeah...so..."
            sa "I’m...sorry again for...accusing you of...something you probably didn’t do..."
            s "Probably? So I’m still not off the hook yet?"

            scene saranewapt29
            with dissolve

            "Sana looks at me and goes quiet."
            "Quieter than she normally is, I mean."
            "And, strangely enough, the volume of the TV dies down at this exact moment, {i}actually{/i} sending the two of us into true silence for a few seconds."
            "Within these few seconds, Sana bares her heart to me."

            sa "You’ll never be off the hook, Sensei."
            sa "Not until my mom cuts the line."
            sa "And even then, you’ll have to swim away with it dangling off of your lip, hanging there until the day you die."
            s "..."
            sa "I have to leave now."
            sa "And..."
            sa "And I want you to come with me."
            sa "But you won’t, will you?"
            s "..."
            sa "..."
            sa "I..."

            scene saranewapt30
            with dissolve

            sa "I’m fine with not having a dad, you know."

            play sound "dooropen.mp3"
            scene saranewapt31
            with dissolve

            s "..."

            "And just like that, Sana leaves."

            scene black
            with dissolve2

            "It’s a strange note to part on, but I think I understand what she means."
            "And it’s not all that different from what she’s been slowly but surely trying to help me understand for a while now."
            "She has no intention of ever accepting the life her mother wants for her. Or, for {i}us{/i}, rather."
            "I’m not sure when I started being included, but it’s pretty much inevitable that it’ll just keep going on forever at this point."
            "Sana doesn’t want me to be here right now-"
            "But she knows that it’s not her place to drag me along with her."
            "And so she’s trusting me, something I wouldn’t recommend to anyone, to not do something that will hurt her."
            "Or-"
            "At least that’s how I’m interpreting it."
            "But, for all I know-"
            "I could very well be wrong."
            "And I could very well hurt her even when I do everything in my power to avoid that."
            "That’s...just the way things are sometimes."

            $ renpy.end_replay()
            $ sana_love += 1
            $ sarabar25 = True

            "{i}Sana’s affection has increased to [sana_love]!{/i}"
            "........."
            "......"
            "..."

            jump sarabar25p2
        else:
            s "You mean when you got into a fight with your mother's dresser?"
            sa "I think...I think it wants a rematch..."
            s "Are you ready? Have you been training?"
            sa "That's...kind of what I need your help for."
            sa "Can you send me...um...videos of people you think are really strong when you get home tonight?..."
            s "Of course, Sana. Good luck with your battle."
            sa "Th-Thanks..."
            sa "Also...try not to hug my mom tonight..."
            s "I will only hug her if she wants me to."
            sa "Ugh..."

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ sana_love += 1
            $ sarabar25 = True

            "{i}Sana’s affection has increased to [sana_love]!{/i}"
            "........."
            "......"
            "..."

    else:
        "It doesn’t last much longer and, once it’s over, Sana gathers her things and heads for the door."
        "She looks back at me and, strangely enough, in the one second of eye contact that I make with her, it seems like she’s telling me that she trusts me."
        "I’m sure it’s not easy for her to just leave me alone with her mother when she’s fully aware of her feelings for me-"
        "But it’s something she elects to do regardless."
        "I’m not sure what I did to deserve this, but I’m not about to make a break for the door to see if she’s really okay with leaving two adults alone in a dark room together."
        "And hey, maybe it’s something even less exciting?"

        if bonus == True:
            "Maybe trust has nothing to do with it and Sana just has absolutely no romantic or sexual feelings for me, making this just an average, everyday goodbye."
        else:
            "Maybe trust has nothing to do with it and Sana just has absolutely no feelings for me whatsoever?"

        "And, if that’s the case-"
        "So long, Sana."
        "Have a safe trip home- and don’t think too much about whatever you expect to happen in this room."
        "I’m sure that whatever comes next will be something you didn’t really want to be here for anyway."

        $ renpy.end_replay()
        $ sarabar25 = True

        "........."
        "......"
        "..."

        jump sarabar25p2

label sarabar25p2:
...
```

## Code that triggers this event

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarasbar:
    if sara_lust >= 5 and sarasex == True and saralust5 == False:
        jump saralust5
    if sara_love >= 20 and sarasex == True and day271 == True and sanadorm40 == True and sarabar20 == False:
        jump sarabar20
    if sara_love >= 25 and yukidate10p2 == True and sarabar25 == False:
        jump sarabar25
...
```