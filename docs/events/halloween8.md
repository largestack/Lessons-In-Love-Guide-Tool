# Mechanical Bull (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Medical Assistance](./saralust10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween8
* Group: Main
* Triggered by label: saralust10skip
* Chain sources: saralust10
* Chain sources path: saralust10

## Official wiki page

[Mechanical Bull](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween8&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween8:
    $ totaldays += 1
    $ day = 7
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    "[totaldays] Days have passed..."

    mi "Psst..."
    mi "Sensei..."
    s "Hm?..."
    mi "Wake up..."

    if bonus == True:
        jump mikumountx
    else:
        s "Mm...five more minutes..."

        mi "Oh. Uhh...okay!"
        mi "Not really how this event's supposed to go, but it definitely helps me out a little."

        "I fall back asleep and wake up several minutes later, missing a lot of context."

label mikumount:
    scene mikumount22
    with dissolve

    "I get off the bed and stand before Mak-"

    mak "Actually, Sensei. Why don’t you take a seat?"

    if bonus == True:
        mak "I don’t think you’re, uhh, {i}ready{/i} to stand up just yet."
        s "Oh. Yeah, that makes sense."

        "I sit back down on the bed after Makoto makes me acutely aware that I have not yet “calmed down.”"
    else:
        s "Who are you and why are you in my room?"
        mak "I'm Makoto. Now shut up and listen."

    mak "Do you have any idea why I’m here?"

    if bonus == True:
        s "I imagine it’s because Miku was taking too long to wake me up."
        mi "Well I...got the job done, didn’t I?"
        mak "I mean why I’m at your house."
    else:
        s "To...hide soup?"
        mak "Guess again."

    s "Oh. I imagine it’s something involving the Halloween party based on the way you’re dressed."
    mak "Precisely. "
    mak "You are aware that the party tonight is at the Amamiya estate, correct?"
    s "I am aware, yes."
    mak "And have you been informed by any of the connected parties that your assistance is required to set the stage for the occasion?"
    s "Set the stage? You mean I actually have to help prepare?"
    s "Doesn’t Ayane’s family have like...servants or something they could use? "
    s "What about that Geoffrey guy?"
    mak "Geoffrey fell mysteriously ill last night. "
    mak "He is fine, but since this party is being held without Ayane’s father’s permission, the two of us have been chosen to get everything ready."
    mak "That includes shopping for food and drinks as well as managing the lighting and sound systems."
    s "Why do I have to be involved in this?"

    scene mikumount23
    with dissolve

    mak "Oh, that’s easy. Because you can carry more things than everyone else."
    mak "And also, you’re the only person coming to the party without a costume, so you need less time to prepare."

    if bonus == True:
        mak "Of course, there’s the time required for a certain part of you to...return to normal-"
        mak "But I trust that you and Miku were about to take care of that any minute, now weren’t you?"
    else:
        mak "Now, I suppose I'll let you and Miku get back to hugging or-"

    scene mikumount24
    with dissolve

    mi "Wha-"

    if bonus == True:
        mi "We were not! I told you I was just afraid of bein’ slapped in the face by it!"
    else:
        mi "I really wasn't doin' anything! I promise!"

    mak "You really expect me to believe that?"
    mi "Yes!"

    scene mikumount25
    with dissolve

    mak "Hah...well, whatever the case...just get dressed and get ready so the two of us can go on a little shopping trip. "
    mak "Everyone else is going to be heading to Ayane’s early and hanging out in her ballroom until then."
    mak "I believe the mansion has a separate section where we’ll be holding the party, so I’ll have her show us to it once we get there several hours from now."
    s "Why do you have to be so responsible all the time?"

    scene mikumount26
    with dissolve

    if bonus == True:
        mak "I need to be or, at this rate, you’ll wind up stealing everyone’s virginity and endangering your career."
        mi "I’m never gonna hear the end of this, am I..."
    else:
        mak "Because I am going to become the first female president."

    scene black
    with dissolve2

    if bonus == True:
        "What Makoto doesn’t realize is that stealing everyone's virginity is my exact mission."
        "But regardless, the two of them leave the room and I get changed, meeting back up with Makoto moments later."
    else:
        "Wow. I had no idea her mission was so serious."

    scene sky
    with dissolve

    "We spend the next few hours scavenging various grocery stores, picking up small things and party favors from all of them."
    "I figured that her attitude would get better throughout the day, but that is very much not the case. "

    if bonus == True:
        "Her resentment lingers and she has no trouble constantly reminding me of how innocent Miku is and how I’m just trying to corrupt her."
        "And while that isn’t {i}entirely{/i} incorrect, it’s not entirely correct either."
        "But of course, I know how it looked, so there’s no sense in arguing about it."
    else:
        "In fact, she tries to attack one of my pressure points in the produce section and I need to defend myself using the knowledge of pankration I gained from my time spent in Greece."

    scene black
    with dissolve

    "Eventually, the two of us make it to Ayane’s place and are immediately escorted through a large courtyard to a traditional Japanese-style dojo where the party will be taking place."
    "We spend the next few hours setting everything up without a single break before the “festivities” finally begin..."

    $ renpy.end_replay()
    $ halloween8 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    "………"
    "……"
    "…"

    "{i}Roughly thirty minutes later...{/i}"

label halloween9:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
scene saralustten14
    with dissolve

    sar "AHHH! AHHH! YES...YES!! FUCK! FUCK FUCK FUCK!"
    sar "OH MY...FUCKING GOD! "
    sar "I’M...GONNA CUM!..."
    sar "YES! YES BABY! RIGHT...FUCKING...THERE! "
    sar "AAAAAAAAAAH FUCK! "

    "Sara’s pussy clamps down on my cock as it becomes harder and harder for her to hold back a climax. "
    "I assume she’s trying to time it so that we finish together but, frankly, it’s more exciting for me to force it out of her before finishing myself."
    "Unfortunately, though-"
    "That doesn’t happen."
    "She arches her back one last time and the sight of her doing so as she holds back her legs is too much for me to bear."
    "I erupt."

    with sexfade
    with sexfade
    scene saralustten15
    with cumflash
    with hpunch

    sar "Aaaaaaaahhhhhhhnn~~~ Hah...hah...ahhhh!..."

    "Sara’s climax is less aggressive and more...intimate than I expected it to be given how loud she was just moments ago."
    "Instead of crying out in pleasure and shaking the house, she just lets out one long moan followed by a few scattered breaths and slides her hips forward."
    "I can feel her body trying to swallow every last drop of me as I fill her with cum."
    "It’s almost burning inside of her, but I can’t find it in myself to pull out just yet."

    sar "[saramaster]..."
    sar "I...umm..."
    sar "How did that...feel?"
    s "Amazing..."

    scene saralustten16
    with dissolve

    sar "Heh...right?"
    sar "I don’t even think I’m...drunk anymore..."
    sar "What was it like fucking a nurse?"
    s "What was it like being fucked {i}as{/i} a nurse?"
    sar "I honestly think I might have had more fun than you..."
    sar "Let’s do it again sometime~ I’ll save the costume."
    s "Would you even be able to return it after doing what we just did?"
    sar "Well...I mean...it’s not like you got anything on it, right?"
    sar "All of it went inside of me~ I can still feel it..."
    s "Yeah...So can I..."

    scene black
    with dissolve2

    "I pull myself out of Sara shortly after that and the two of us lie there for a few moments."
    "Maki winds up coming back into the room once she hears us finish and lays down right next to Sara before she can even fix her clothes."
    "My pants are already on when this happens, unfortunately, but I’m assuming Maki at least got a decent view of {i}me{/i} earlier."
    "I kind of wish she would have joined in, though."
    "But, no cats are allowed in the hospital, I guess..."
    "…"
    "The rest of the night passes by quickly. "
    "Sara and Maki both fall asleep right there on the bed and I wind up walking home very satisfied with myself."
    "And if tomorrow is anything like tonight was, I imagine I’ll be pretty satisfied in the near future as well."
    "I doubt any of my students will be sexy nurses or slutty cat girls but...hey, at least they’ll be wearing something a little different."
    "That’s more than enough for me."

    play sound "dooropen.mp3"

    s "…"

    "I don’t say anything when I walk back into the house."
    "It’s almost 3:00 AM at this point, so I don’t want to bother waking anyone up."
    "I wonder if Ayane ever tried coming to my room like she said she would?"
    "I did get a few texts from her over the course of the night but I’d completely forgotten I even had my phone with me until I was on the way back."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve
    stop music fadeout 5.0

    "I walk into my room and, of course, I don’t find anyone there."
    "It’s a lonely sight, but I know there are four girls just two rooms away. "
    "…"
    "I wonder if any of them are dreaming of me?"

    scene black
    with dissolve

    "I lie down on the bed and close my eyes. "
    "Tomorrow should be eventful, if not anything else."
    "…"
    "I’m looking forward to it."

    $ renpy.end_replay()
    $ sara_lust += 1
    $ saralust10 = True

    "{i}Sara’s lust has increased to [sara_lust]!{/i}"
    "………"
    "……"
    "…"

    jump halloween8
...
```