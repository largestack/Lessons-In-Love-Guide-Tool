# Family Business
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimebar&go=Go)



## Event preconditions
✅Sana love greater than or equal to 0



## Next events
* [Sana: Nothing to Do](./sanafirsthall.md)

## Event properties
* ID: firsttimebar
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label firsttimebar:
    play music "calmbar.mp3" fadein 2.0
    scene firstbar1
    with dissolve

    "I decide to close out the night with a trip to the bar."
    "I’ve yet to have a drink since the whole reincarnation thing, and I’m sure Ami won’t mind if I stay out a little late every once in a while."

    s "..."

    "Look at me, thinking some teenage girl has some amount of influence over my behavior."
    "I must be getting soft."
    "The bar looks decently upscale for the area it’s in, but there aren’t any customers apart from a few old women smoking cigarettes in the corner."

    scene black
    with dissolve

    "I walk past them and take a seat at the bar, not noticing until now that the bartender looks exceedingly familiar..."

    scene firstbar2
    with dissolve

    sa "Uh..."
    s "...Sana?"
    sa "Um..."
    sa "Uh..."
    sa "H..."
    sa "Hello..."
    s "I had no idea you worked at a bar."

    scene firstbar3
    with dissolve

    sa "I...know it’s against the rules..."

    scene firstbar4
    with dissolve

    sa "Am I...going to get in trouble?..."
    s "With me? No. I’m not here to tell you how to live your life."
    s "Just try and keep it a secret from anyone more important than me and I'm sure you'll be fine."

    scene firstbar5
    with dissolve

    sa "You...really mean that?..."
    sa "Because...when you walked in, I-"
    s "I mean it. I {i}am{/i} a little surprised you work somewhere like this, though."

    scene firstbar6
    with dissolve

    sa "How come?"
    s "You just...don’t really seem like the bartender type, I guess?"
    sa "What is the...bartender type?..."
    s "Probably someone old enough to legally drink. But I'm sure you hear enough of that from your customers."

    scene firstbar7
    with dissolve

    sa "Umm...not really..."
    sa "Most of the people who come here have been coming here for years...so I've known them for a really long time..."
    s "How long have you been working here, exactly?"
    sa "I haven't been...{i}working{/i} here for long...but my mom lives upstairs, so...I...kind of grew up here...or something."
    s "You live above a bar? That's amazing."
    sa "Well...{i}I{/i} live in the dorms now, so..."
    s "Shame. Though, I guess that probably helps with you not becoming an alcoholic at an early age. Not that I imagine you drink much to begin with."
    sa "R-Right..."

    "Sana doesn’t seem much different than she does in class. She’s still just as quiet as ever."

    if bonus == True:
        "Well- scratch that. She {i}does{/i} seem different. But only in the fact that she is significantly more adorable in her work clothes than she is in her school uniform."
        "Which is a weird thing to admit since my attraction to school girls has been slapping me across the face ever since {i}waking up.{/i}"
        "Either way, I am now obligated to test the waters and compliment her appearance because that is just the type of guy I am."
    else:
        "I have also noticed that her clothes are the perfect size for her based on my years of experience in fashion design."

    s "Those clothes fit you well, Sana."
    sa "..."
    s "Sana?"
    sa "Oh...sorry...Thank you..."
    sa "It's just...they were my brother’s."
    s "Were? Does he not work here anymore?"

    scene firstbar8
    with dissolve

    sa "I..."
    sa "That's not...really something I want to talk about right now...if that's okay..."

    scene firstbar9
    with dissolve

    s "That's fine. I'm not going to push you out of your comfort zone until the second or third time we hang out after class..."
    sa "I...don't think that's...a thing we should do..."
    s "That aside, do you think you could pour me a drink? That's kind of the whole reason I'm here, after all."

    scene firstbar5
    with dissolve

    sa "You drink, Sensei?"
    s "What other reason would I have to come to a bar?"

    scene firstbar7
    with dissolve

    sa "Oh...yeah...hahah..."
    sa "R-Right..."

    scene firstbar9r
    with dissolve

    sa "Well, what can I get for you then?..."
    s "Just a beer, thanks. I'm not really a liquor person."

    scene firstbar10
    with dissolve

    sa "Okay...Coming right up."

    scene firstbarnone
    with dissolve

    "Sana moves to the opposite end of the bar and opens up a cooler that must be at least twenty years old."
    "She pushes aside a few half-empty syrup bottles and grabs me a can of some beer I don't recognize."

    scene firstbar10
    with dissolve

    sa "Um...here you go..."
    s "What is this exactly?"
    sa "It's...umm..."
    sa "You...{i}did{/i} say you wanted a beer...right?..."
    s "Yeah, I just don't recognize this kind."

    scene firstbar7
    with dissolve

    sa "We...only carry alcohol from the local brewery, so...I'm sorry if it's not to your liking..."
    s "There’s a brewery in Kumon-mi?"

    scene firstbar10
    with dissolve

    sa "If there wasn't...we'd have a problem..."
    s "Well hey, beer is beer and I got what I asked for."

    "Sana pulls the tab of the can open and slides it over to me as if she's doing it from muscle memory but, well, I guess that's to be expected given the environment she's apparently grown up in."
    "Assuming she's not done {i}growing up,{/i} that is."
    "It’s still strange seeing someone so [young]doing a job like this, though."

    s "So how long has your family been running this place, exactly?"

    scene firstbar7
    with dissolve

    sa "Since...way before I was born..."
    sa "My grandma and grandpa opened the bar a long time ago..."

    scene firstbar10
    with dissolve

    sa "My...mom told me it used to be really popular when she was a little girl..."

    scene firstbar11
    with dissolve

    sa "But...now, it's..."

    "Sana's eyes navigate to the corner of the room, where the group of old women sit."
    "Now that she's redirected her attention over there, I become acutely aware that they've been mysteriously quiet ever since I showed up."
    "They're old, though. They probably just ran out of energy or something. That seems like an old-person thing to do."

    s "So I guess this place is pretty much the shell of its former self then?"
    sa "Yeah..."
    sa "That's a...good way to describe it..."

    scene firstbar12
    with dissolve

    sa "You don't...think it's because of me...do you?..."
    s "I mean, I’ve only been here once, so I can’t say for sure...but I highly doubt that’s it."
    s "If anything, I’d think having a bartender as cute as you would reel even more customers in."

    scene firstbar3
    with dissolve

    sa "That’s...uhh..."
    s "You could probably work on your social skills a bit, though."

    scene firstbar2
    with dissolve

    sa "Huh?"
    s "What I mean is that {i}I{/i} know you’re naturally this quiet, but newer customers might not get that right away."

    scene firstbar7
    with dissolve

    sa "I was...kind of worried that might be the case..."

    scene firstbar9
    with dissolve

    sa "Sensei...do you know any tricks to...you know..."
    s "Get better at having conversations with strangers?"

    scene firstbar3
    with dissolve

    sa "Y-Yeah..."
    s "Hm...Not really."

    scene firstbar12r
    with dissolve

    sa "I see..."
    s "It’s just something you sort of have to do if you ever want to make it through life."
    s "Look at me- I don’t like talking to strangers 99%% of the time, but I still do it because that’s just how life works."
    s "You can’t just avoid everything forever. If life were that simple, we wouldn’t need jobs or[school] or anything like that."

    scene firstbar7
    with dissolve

    sa "I...guess you’re right."
    s "You seem to be talking to me just fine, though."

    scene firstbar9r
    with dissolve

    sa "Well...I’ve talked to you before, so..."
    s "Maybe we just need to talk a little more, then?"

    scene firstbar2
    with dissolve

    sa "Talk...more?..."
    s "By opening up more to me, you might get better at opening up to others. Right?"

    scene firstbar7
    with dissolve

    sa "Um...I don’t really know about that..."
    s "That settles it, then."

    scene firstbar4
    with dissolve

    sa "Wait, settles what?...I'm...suddenly confused..."
    s "I’m going to help teach you some social skills whenever I drop by the bar."

    "It's not like I plan on teaching her anything in school, so this is just my way to make up for that."

    scene firstbar7
    with dissolve

    sa "Sensei, I...don’t really have time for extra classes..."
    s "Is it really an extra class if you're on the clock for it?"
    sa "Is that...really okay, though?...Isn’t this place...a little far from your home?..."
    s "It’s not that bad. Plus, if it’s for you, I don’t mind at all."

    scene firstbar4
    with dissolve

    sa "You really mean that?...You’ll go out of your way for me?..."
    s "Of course. You’re one of my students. Plus, it will give you an incentive to reward me with free drinks and that is always a plus."

    scene firstbar13
    with dissolve

    sa "Heheh...well...we'll...have to see about that part..."
    sa "Because...I don't really think we're in the position right now to...be able to do that..."
    s "Well, lucky for you, I'm paying tonight."

    "I chug the remainder of my beer and slide the can back to Sana."

    sa "That's...not exactly {i}lucky{/i} for me...That's just...kind of how...buying things works..."
    s "Then you're lucky I decided to stop by here instead of some other bar."

    scene firstbar10
    with dissolve

    sa "Heheh...that, I...can't argue with..."
    sa "Are you ready for another?"
    s "I’m fine for tonight, actually. I think I’m going to head out."

    scene firstbar9
    with dissolve

    sa "O-Oh...I see..."
    s "I’ll be back soon, though. Just keep trying to improve on your own in the meantime."

    scene firstbar3
    with dissolve

    sa "I’ll try but...I’m pretty bad...I can't really promise that...there will be any progress..."
    s "Well, I'm passable. So I'm sure everything will all work out in the long run."

    scene firstbar10
    with dissolve

    sa "Okay...I trust you..."
    sa "Goodnight, Sensei...I’ll see you soon."
    s "I'm sure you will."
    s "Goodnight, Sana."

    scene black
    with dissolve2

    "I take a handful of coins out of my pocket and leave them on the counter without ever asking for a bill."
    "I'm sure it's a lot more than necessary, but it's not like I have anything I'm saving up for. And spending that money on Sana might be a good tool to get her to open up to me."
    "Is that technically a form of bribery? Sure. I guess you could say that."
    "But if there's anyone bribery works on, it's a family in financial turmoil."
    "I start my journey home with slightly lighter pockets, but a slightly more optimistic outlook for the future."
    "And that's a fair trade to me."

    $ renpy.end_replay()
    $ firsttimebar = True
    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar2to4:
    play music "calmbar.mp3" fadein 2.0
    scene firstbar10
    with dissolve

    "I decide to visit Sana at the bar again."
    "We work on the basics of public speaking but she shows little to no signs of improvement."
    "I might need to figure out an alternative method of teaching soon."
    "Even though she’s still hesitant to converse with others, I can feel the two of us becoming slightly closer..."

    scene black
    with dissolve

    $ sana_love += 1

    stop music fadeout 3.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar5:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
...
```