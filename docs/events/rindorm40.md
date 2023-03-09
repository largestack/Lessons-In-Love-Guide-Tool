# Semantics
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm40&go=Go)



## Event preconditions
✅Rin love greater than or equal to 40

✅Event "[Rin: Sketchy Basement](./cafe40.md)" is completed (event=cafe40)

✅Day of week is not Tuesday

❌Day of week is not Saturday

✅Day of week is not Sunday



## Next events
* [Rin: Debatably Bisexual Musicians](./cafe45.md)
* [Niki: Like it's Any Other Day](./nikidate5.md)

## Event properties
* ID: rindorm40
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm40:
    play sound "knock.mp3"

    "I knock on the door and wait for Rin to respond."
    "It isn’t until I bring my ear closer to the door, however, that I notice it’s a bit...louder than normal in there."
    "I wonder if something is going on?"

    r "One...sec!"
    r "Futaba...watch your hands!"
    f "But this is...the best way to do it..."
    r "But it’s...mine...I think I know...the best way!"

    play sound "knock.mp3"

    s "You can not make noises like that and expect me to not immediately come in."
    r "Just...hold on!"
    r "So close to being...finished!"
    s "What are you two doing in there?"
    f "Rin...were you...expecting Sensei?..."
    r "No, but...he can obviously join in..."
    r "He’ll be a...huge help...don’t you think?"
    s "Yes. I will help with anything. Just name it."
    f "Will he?...We’re basically done already..."
    r "Yeah...just..."
    r "...Ahhhh!"
    r "There..."
    r "Coming, Sensei!"

    scene black
    with dissolve
    play sound "lock.mp3"

    "Rin runs to the door and unlocks it, pulling it open and flagging me in."
    "I’m not exactly sure what sort of “activity” they need my help with but, as their teacher, it is my duty to-"

    scene rinfutabanewdorm1
    with dissolve

    r "Ta-da!"
    f "Umm...hey..."
    r "Sorry for the hold-up, Sensei. Futaba was helping me move my new bed into the corner. "
    s "You should be more specific when you’re letting out pained, exasperated yelps from behind a locked door."
    r "Or maybe {i}you{/i} should stop eavesdropping on people."
    s "I think it stopped being eavesdropping the moment I knocked."
    f "What exactly...did you think we were doing?"

    if bonus == True:
        r "Probably having sex."
    else:
        r "Probably rock climbing. That's what I would have assumed."

    scene rinfutabanewdorm2
    with dissolve

    f "With...each other?!"

    if bonus == False:
        r "Sure. Rock climbing is done in pairs all the time."

    s "I know how it sounds but I’m really not the only one at fault here."
    r "Liking the new set-up, Sensei?"
    r "We spent pretty much the whole evening putting everything together."
    s "It only took one evening? Even the floor is different."
    s "I feel like this should have taken a lot longer."
    r "Yeah, I don’t know. "
    r "I guess the maintenance crew handled swapping out the flooring while we were at[school] or something."
    r "I’m not arguing. I love the new look."

    scene rinfutabanewdorm3
    with dissolve

    f "It’s a little more...colorful than I was expecting. But it {i}is{/i} a nice change of pace."
    s "Why the need for the sudden renovation? Your room seemed fine."
    r "It {i}was{/i} fine, just a little out of date."
    r "All of the other rooms were actually renovated before ours."
    r "But right when it was our turn, they had to call everything off for financial reasons or something."
    r "Either way, we’re caught up now."
    r "And, look! I even got to keep my best friends!"
    s "Your...what?"

    scene rinfutabanewdorm4
    with fade

    "Rin hops onto her bed and quickly points to her shelf full of human skulls that somehow managed to survive the dorm renovation."

    r "These little dudes right here."
    s "I was finally starting to forget you even had those."
    r "You really think I could survive without these? Come on, man. You know me better than that."
    s "Do I really, though?"
    r "Hey, Sensei, want to hold one?"
    s "Not really?"
    r "What if I tell you one belonged to a [teenage]girl? That’ll get you going, right?"
    s "My appreciation for [teenage]girls doesn’t really persist through death, believe it or not."

    scene rinfutabanewdorm5
    with dissolve

    r "Well then you’re missing out."
    r "Death is when the {i}real{/i} fun starts..."

    scene rinfutabanewdorm6
    with dissolve

    s "Is she okay?"
    f "I...ask myself that all the time."
    f "She’s just...really attached to those skulls for some reason."
    r "Hey, I don’t judge you for being attached to your books."

    scene rinfutabanewdorm7
    with dissolve

    f "I don’t {i}kiss{/i} my books, though..."
    s "She {i}kisses{/i} them?"

    scene rinfutabanewdorm8
    with dissolve

    f "Just the one time..."
    f "I hope."
    s "Rin, do you-"
    r "No comment."
    s "That can’t be sanitary."
    r "More sanitary than Molly, probably. I’m still kind of reeling from that thing at the Christmas party."
    r "Like, for real. What made her think that was a cool thing to do?"

    if mollydorm20 == True:
        "I’m pretty sure I know {i}exactly{/i} why she did it..."

    scene rinfutabanewdorm9
    with dissolve

    f "Just because you don’t like her that way doesn’t make her unsanitary..."
    f "She’s just as sanitary as you and me. We literally shower together."

    if bonus == True:
        s "Yes. Talk more about this."
        s "Describe these showers in vivid detail."
        r "Futaba, put those things away. They’re getting our teacher riled up."
        f "Where would I even hide them?"

        "{i}In my hands.{/i}"
    else:
        s "That sounds like an entirely reasonable thing for college girls to do and isn't, in any way, something I am going to continue thinking about."

    scene rinfutabanewdorm10
    with dissolve

    r "Molly aside, welcome to the brand new Dorm #4, Sensei."
    r "I’m sure you’ll be spending a lot of time in here from now on, so get used to it."
    r "Well, at least until the[school] year ends and we’re forced to change rooms. "
    r "You can’t put in a good word for us to make sure we get this one again, can you?"
    r "I’ve only lived here for half an hour but I’m already pretty attached."
    f "We’ve lived here for a lot longer than half an hour..."
    f "The only thing different is the floor and some of the furniture."

    scene rinfutabanewdorm11
    with dissolve

    r "Speaking of brand new furniture, what do you think we should do with our table?"
    s "Can...tables do more than just be...tables?"
    r "A table can do anything it puts its mind to, Sensei."
    s "...What?"
    f "I think I’m fine with it just holding a vase for now..."
    r "Okay, but the second we need it for anything other than that, you can bet your big ole’ boobies that I’m dropkicking that vase all the way to North Dakota."
    s "Do you even know where North Dakota is, Rin?"

    scene rinfutabanewdorm12
    with dissolve

    r "Right above the south one, idiot."
    f "Rin drank four energy drinks while we were moving things around, so please forgive her for her...hyperness today."
    r "I thought all of the coffee I drink at work would have made me immune to caffeine but apparently I can still get some effects if I just overload on it."
    f "Uh-huh..."
    f "Tell him the other reason you’re acting hyper as well."
    s "Other reason?"

    scene rinfutabanewdorm13
    with dissolve

    r "Otoha and me are gonna go on a date soon!"
    r "Well, she didn’t call it a date. And neither did I."
    s "That is...exactly what you just called it."
    r "Semantics."
    s "Well, congratulations either way. It’s clear that this is the best thing that’s happened to you in quite some time."
    r "Probably ever."
    s "That would just be depressing."
    f "Have you two decided what you’re going to do yet?"

    scene rinfutabanewdorm14
    with dissolve

    r "We’re gonna go check out some arcade near her house that I looked up online."
    r "It’s supposed to be this cool kind of arcade thingy where they have shows and sell alcohol and stuff."

    if bonus == True:
        r "And sure, neither of us are old enough to drink, but they’ll still let us in. I checked that part out online, too."

    s "You put a lot of thought into this, haven’t you?"

    scene rinfutabanewdorm15
    with dissolve

    r "Despite never having a relationship with anyone and never even holding hands-"
    s "You had your first kiss before ever holding hands?"
    r "Please don’t remind me."
    r "But, as I was saying, despite all of that, Rin Rokuhara is a dating expert."
    r "I know all the spots, all the right things to say, and possess none of the courage required to actually capitalize on either of those things."
    f "She also wrote fan fiction for an anime series she likes and counts that as proper dating experience."
    r "That part could have been left out, but yes. Thank you, Futaba, for sharing one of my darkest secrets with Sensei."
    r "You’re lucky that I haven’t yet told him you wanted to marry your dad when you were little."

    scene rinfutabanewdorm16
    with dissolve

    f "Th-That’s a totally normal thing that a lot of little girls say!"
    r "Not me! I wanted to marry my {i}mom{/i}."
    f "How is that any better?!"
    r "It’s more progressive. I’m clearly a better person than you."
    s "Wait, just to clarify, Futaba {i}does{/i} know about your other “secret” right?"

    scene rinfutabanewdorm17
    with dissolve

    r "Oh, totally. It didn’t come out until the whole thing with Chika boiled over but she’s apparently known for a really long time."
    r "So I just stopped trying to hide it and now I have somebody to talk about girls with all day long."
    f "I’ll admit that it’s a little awkward since...{i}I’m{/i} not into girls, but...if Rin wants to vent, I’ll be here to listen."
    s "Same. Especially if you want to go into vivid detail about anything that happens with them."

    scene rinfutabanewdorm18
    with dissolve

    r "Boy, will I ever."
    f "You two are...kind of scary when you look at each other like that."

    if bonus == True:
        r "Don’t look down on us just because you’re too prude to talk about cool sex stuff."
        r "I bet you don’t even know how to do the sex, Futaba."
        s "That was a slightly compelling argument until you made it to that “do the sex” part."
        r "That’s what we’re calling it nowadays. Ask anyone."
    else:
        r "You should see us when we're shopping at flea markets for new hair products."
        r "Sensei gets this crazy look in his eyes like {i}I need shampooooooooooooooooooooooooo.{/i}"
        s "Why did you add so many o's"
        r "That's just how we're saying that word nowadays."

    scene rinfutabanewdorm19
    with dissolve

    f "We’re really not..."
    f "It’s just Rin."
    r "It’ll catch on. Watch."

    if bonus == True:
        s "So the gameplan is basically...meet up, cool arcade date, and then “doing the sex” with Otoha?"
    else:
        s "So the gameplan is basically...meet up, cool arcade date, and then hugging Otoha until she realizes she loves you?"

    scene rinfutabanewdorm20
    with dissolve

    r "Wait wait wait wait wait! I still haven’t even confirmed that she likes girls yet!"
    s "But you told me in the past that all girls kind of like girls."
    r "They do!"
    f "That is...not true..."

    scene rinfutabanewdorm21
    with dissolve

    r "Shut up and be supportive, so-called “best friend!”"
    f "S...Sorry..."

    scene rinfutabanewdorm20
    with dissolve

    r "But...yeah! There are a bunch of steps between going to an arcade and tying the lesbian tongue-knot."
    r "And one of those steps is confirming that the girl you’re trying to tie that knot with is actually into the same stuff that you are."

    "I hope she doesn’t mean skulls."

    s "You do know that “tying the knot” means getting married, right?"
    r "Obviously! That’s why I said “lesbian tongue knot!”"

    if bonus == True:
        s "That does sound a lot more interesting, I won’t lie."

    scene rinfutabanewdorm22
    with dissolve

    r "I’m super nervous, though, Sensei."

    if rinbetrayed == False:
        r "Like, what if it’s a repeat of the whole Chika situation and Otoha figures out that I think she’s cute and then never wants to see me again?"
        s "I mean...you haven’t known Otoha for nearly as long."
        s "So if something like that {i}does{/i} happen, do you really think it will hit you as hard?"
        r "Probably not, but that doesn’t mean I’m not still scared."
        s "Just don’t go confessing your love out of virtually nowhere and everything will be okay."
        r "It’s not love, obviously. But she’s so cool and I want her to like me and I can be kind of hard to like when I get all...Rin-ish."
    else:
        r "Like, what if it’s a repeat of the whole Chika situation? "

        scene rinfutabanewdorm23
        with dissolve

        r "I swear, if I find out you’ve been fucking around with {i}Otoha{/i} despite barely even knowing her, I will literally never talk to you again."
        s "I can assure you that has not happened."

        "Though, I can’t say I’d be entirely opposed if the opportunity arose..."

        f "Wait...what happened?"
        r "Nothing, Futaba. I’m just worried, that’s all."
        r "Things like this have a history of going kind of bad for me."
        s "And how long is that history, exactly? Just one time, right?"
        r "Yes it’s one time but that’s also a 100%% failure rate."
        r "Otoha’s so cool and...pretty and...I just want her to like me."
        r "But it’s probably really hard to like someone when they act all...Rin-ish."

    scene rinfutabanewdorm24
    with dissolve

    f "I...obviously can’t speak for Sensei, but..."
    f "I think how flustered you get is one of your cutest qualities..."
    f "And if there’s anyone who doesn’t appreciate that part of you, I don’t think I’d...sign off on them dating you."
    r "Are you sure you don’t like girls, Futaba? Cause I kinda wanna kiss you after hearing that."

    if bonus == True:
        s "You can kiss me if you want."

        if rinbetrayed == True:
            r "No thanks."
            s "Wow, not even a thought."
        else:
            r "No way. Futaba’s in the room. It would be weird with her watching."
            s "...Wait, so it would be okay if she wasn’t in the room?"

    f "Nobody is kissing anyone..."
    f "If you’re nervous about your date that...may or may not even be a date, you can talk to me about it."
    s "And if you have any questions about how to impress girls, I’d be willing to lend a hand as well."

    scene rinfutabanewdorm25
    with dissolve

    r "What? Since when do you know how to impress girls, Sensei?"
    f "His...writing skills are impressive at least..."
    f "Does Otoha like...writing?"
    s "There are other impressive things about me."
    s "Just...one of them isn’t legal to break out unless the circumstances are right."
    r "Circumstances? But what-"
    f "…"
    r "…"
    s "…"

    scene rinfutabanewdorm26
    with dissolve

    r "Ewwww..."
    r "What a weird time to brag..."
    f "Yeah...maybe it’s best if you...leave that part to me as well, Sensei..."

    scene black
    with dissolve2

    "I spend a little while longer hanging out with Rin and Futaba before the two of them decide it’s time to kick me out so they can lie down."
    "It only makes sense given how exhausted they must be from reorganizing things, but I also thought Rin’s energy drink high would have lasted a bit longer."
    "Either way, it’s clear that the conversation was going to continue to head into territory I probably wouldn’t be of any help for."

    if bonus == True:
        "And sure, it’s disheartening that, once again, Rin is starting to fall for someone with a vagina-"
        "But it’s not like I expect her to just change her primary preference overnight. "
        "No one can help who they fall for."
        "I just wish she didn’t fall so hard, so easily."
    else:
        "There are just certain things a teacher shouldn't be getting involved in and I hope Rin is able to solve all of her problems without sloping back into depression or exploding due to a surplus of love."

    $ renpy.end_replay()
    $ rindorm40 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm45:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
    if rin_love >= 20 and cafe20 == True and day50 == True and rindorm20 == False:
        jump rindorm20
    if rin_love >= 25 and rindorm20 == True and rindorm25 == False:
        jump rindorm25
    if rin_love >= 30 and day != 2 and cafe30 == True and rindorm30 == False:
        jump rindorm30
    if rin_love >= 35 and rindorm30 == True and rindorm35 == False:
        jump rindorm35
    if rin_love >= 40 and cafe40 == True and day != 2 and day != 6 and day != 7 and rindorm40 == False:
        jump rindorm40
...
```