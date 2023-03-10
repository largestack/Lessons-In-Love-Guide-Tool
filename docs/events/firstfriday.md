# Am I Awake? (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [A New You](./startsleepover.md)

## Event preconditions

* Day of week is Friday



## Next events

None

## Event properties

* Id: firstfriday
* Group: Main
* Triggered by label: nextstart
* Chain sources: startsleepover
* Chain sources path: startsleepover->amiwhattodo->amiwhattodo

## Official wiki page

[Am I Awake?](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firstfriday&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label firstfriday:

    if bonus == True:
        jump firstfridayx
    else:
        "..."
        "{i}Just kidding! This is a family friendly game without any adult content.{/i}"
        "………"
        "……"
        "…"
        "I have a completely normal dream about Ami."

    $ amiawake = True

label amiwakesupyeah:
    a "Hey, Sensei?"
    a "Senseiiiii?..."
    a "Earth to Sensei..."

    "A soft prodding at my cheek brings the world back into sight."

    scene amiwakeup1
    with dissolve2

    a "Morning!"
    a "How did you sleep?"
    s "Ami?..."

    "I take a moment to regain my senses and wipe away the sleep from my eyes."

    if bonus == True:
        s "How long have you been here?..."

        scene amiwakeup3
        with dissolve

        a "I just got here. Why?"
        s "I see..."
        a "Is...something wrong?"
        s "No, it's nothing. Forget I even said anything."

        scene amiwakeup2
        with dissolve

        a "Uhh, okay! Whatever you say."
        a "Hey, were you having a weird dream or something?"
        a "You were rolling around a lot when I first came into the room."
        s "Nope. Everything's totally normal here."
    else:
        s "Are taxes due yet?"
        a "Taxes? No. Not for a while. The year isn't over yet."
        a "Is that what you were dreaming about?"
        s "Yes. That would be a normal dream to have, and so that is what I dreamt."

    scene amiwakeup4
    with dissolve

    a "Well, whatever it was, you better hurry up and get ready."
    a "We need to leave in the next fifteen minutes if we’re going to make it to[school] on time."
    a "Your breakfast is on the table! I’m going to go do my makeup really quick."
    s "Okay, got it. Thanks."

    scene amiwakeup5
    with dissolve

    a "No problem."

    scene amiwakeupgone
    with dissolve

    play sound "dooropen.mp3"

    "Ami exits the room. I hear her door open and close just a few seconds later."

    if bonus == True:
        s "..."
        s "..."
        s "..."
        s "What the fuck was that dream?..."
    else:
        "As soon as I'm sure the coast is clear, I get up and excitedly prepare myself for the opportunity to better the knowledge of future generations."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

label thefirstclass:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
scene sanaclass
    with fade

    "{i}Sana Sakakibara...{/i}"
    "{i}No one really knows anything about Sana other than Ayane.{/i}"
    "{i}She's extremely quiet and vehemently refuses to talk under almost all circumstances, but it's less because she doesn't want to and more because she can't.{/i}"
    "{i}It remains to be seen whether this is simply how she is or if there is something about her past that is causing her to be this way-{/i}"
    "{i}But without many opportunities to actually speak with her, I'm not sure if I'll ever really know anything or not.{/i}"

    scene bathscenebutnomorebath16
    with fade

    "So...that's my class, I guess."
    "It seems like there's a fair bit of diversity in terms of personalities, but I guess I won't be able to confirm anything for sure until I make it to school tomorrow, though."
    "A few of the girls seem like they might be a bit harder to {i}crack{/i} than the others, but...seeing as this is apparently my life now, I'm sure I'll have plenty of time."
    "The issue is just...figuring out who to talk to first."
    "Sure, Ami would likely be the easiest out of everyone- and the most accessible too."
    "The problem is that Ami seems almost {i}too{/i} accessible- to the point where, even now, I feel like she's hovering right over my shoulder."

    a "Do you remember everyone's names yet? Want me to quiz you?"

    scene bathscenebutnomorebath17
    with dissolve

    s "..."
    a "..."
    s "You're really quiet."
    a "Yeah. That's a special skill of mine."
    a "But in my defense, Sensei, I {i}did{/i} knock like three times before coming in here."
    a "And with how out of it you've been since we left school, I was worried your brain might have melted or something like that."
    a "You're lucky your loving niece was willing to come check on you rather than just calling an ambulance and letting them handle it."
    s "I'm flattered, really."

    scene bathscenebutnomorebath18
    with fade

    a "Dinner's in the oven right now, so you can go ahead and take a bath while it's cooking."
    a "I already warmed the water up for you...and I want to wait until right before I go to sleep to get in since that's what always makes my hair look best the next morning."
    s "Given how much of it you have, I'm sure it takes the entire night to dry as well."
    a "Yup! I'm pretty sure that if I put it into a ponytail while it's still wet and swing it really hard, I can probably kill someone."
    s "Great. I can't foresee a future in which that ever needs to happen, but I'm glad that you've found a way to weaponize your body so early in life."
    a "Sensei, you realize that every second you spend talking to me here is just making the bath cooler, right?"
    s "I know, I know. I'm going."
    s "But before I get in..."
    s "Thank you, Ami. For...answering all of my questions today and...just immediately accepting my existence."
    a "Saying it like that makes it sound like you didn't exist {i}until{/i} today, Sensei. And we both know that's not true at all."
    s "Yeah..."
    s "Yeah, I guess we do..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "The bath is perfectly warm once I get in...and dinner is perfectly cooked once I get out."
    "It's an amazing first day here in Kumon-mi."
    "But nothing this good can possibly last forever."
    "And I know that all of the conveniences being passed out like promotional tissues will soon become too much to bear."
    "There is no world so abundantly good...and I will not allow myself to be lured into believing such a world exists just because of a hot bath and a fresh plate of food."
    "Tonight, I will sleep."
    "And when I wake up-"
    "If I wake up in {i}this{/i} world-"
    "If none of this was a dream-"
    "I will start a new life."
    "And I will do my best to cherish it."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ clichebath = True
    $ ami_love += 1
    play sound "eggcrack.mp3"

    "{i}Congratulations! Ami’s affection has increased to 1!{/i}"
    "{i}In Lessons in Love, affection points are used to unlock the next step in each girl’s story.{/i}"
    "{i}Affection points may be gained through main story events and/or spending your free time with the girls.{/i}"
    "{i}Some events are locked to progress with certain characters, so make sure to level up all of them and not neglect anyone!{/i}"
    "{i}You can view your affection with the girls through the progress menu at the bottom of your screen. This will also show you how much content is available for each character.{/i}"
    "{i}For a more detailed look at each girl's content, you may view their character profiles. This is also where scene replays will be stored once you unlock them.{/i}"
    "{i}An event tracker for main events is accessible through the menu as well! And don't worry about skipping certain events if they aren't triggered in order.{/i}"
    "{i}Some events require very specific conditions to be met in order to trigger, so unless you see something crossed out in red, it is still obtainable.{/i}"
    "{i}Oh, and did I mention that all events are replayable by clicking their respective titles in the tracker? Because they are!{/i}"
    "{i}This will come in handy once I start showing you how much I hate you.{/i}"
    "{i}Anyway! This marks the end of Day 1!{/i}"
    "{i}Your true journey begins now!{/i}"
    "{i}Enjoy your stay in Kumon-mi!{/i}"
    "{i}And please accept this next scene as a token of my gratitude for spending time with me in here.{/i}"
    "………"
    "……"
    "…"

    $ totaldays += 1
    $ day += 1
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
        jump firstfriday
    else:
        jump firstfriday
...
```