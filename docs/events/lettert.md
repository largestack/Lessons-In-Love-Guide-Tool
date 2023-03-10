# The Letter 'T' (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: lettert
* Group: Happy scenes
* Triggered by label: doorknock
* Triggered by branch label: doorknock
* Triggered by path: doorknock->lettert

## Official wiki page

[The Letter 'T'](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=lettert&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label lettert:
    stop music
    scene black

    "………"
    "……"
    "…"

    scene lettert1
    with pixellate

    s "…"
    s "Huh..."
    s "Did I take a wrong turn somewhere?"
    s "This place doesn’t seem familiar at all..."

    "I can see several spotlights off in the distance, aimed at what looks like a giant letter T."
    "T is my least favorite letter in the alphabet."
    "Have I ever told you that?"
    "It seems rare that you can even form a sentence without one."
    "What a selfish letter T is."

    scene lettert2
    with pixellate

    "I take a step closer to get a better look at the worst letter in the alphabet."

    s "Is this...snow?"

    "I remove my hands from my pockets and hold them out. Several flakes fall into my palms,
    melting immediately upon contact."
    "It’s summer right now. Water shouldn't be able to freeze."

    six "You’ve been born twice and yet question the snow?"
    six "Curious."

    if roomwithtrack == True:
        s "What are you doing here?"
        six "Learning to spell."

        "The girl from the room with clocks speaks out to me from behind the letter T."
        "Her voice is easily recognizable, like nails on a chalkboard mixed with a dentist’s drill."
        "But it’s strangely calming for some reason I can’t figure out."

        six "Aren’t you going to come closer?"

        "She beckons me to the front of my least favorite letter."

    else:
        s "...Hello?"
        s "Who’s there?"
        six "Everyone and no one."
        six "The beginning and the end."
        six "Why don’t you take a look for yourself?"

        if bonus == True:
            six "{s}Step forward and taste me.{/s}"

    if bonus == True:
        jump lettertx
    else:
        scene black
        with dissolve

        s "No thank you."

        "Her weird voice makes me feel all creepy and I decide to just go home like I originally planned."
        "I miss out on some story content, but the world becomes a safer place because I didn't see any nudity and nudity is bad."

        $ renpy.end_replay()
        $ lettert = False
        $ letterttrack = True

        stop music fadeout 3.0

        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label ticktock:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
"..."
                                "There's no answer."
                                jump doorknock
                            else:
                                r "Uhhhhh...Look down here?"
                                s "Huh? Oh, damn. My bad."
                                jump rinhall
                        else:
                            play sound "knock.mp3"

                            s "Hey Rin, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock


                    "Futaba (Current Affection - [futaba_love])":
                        if futaba_love >= 5 and day != 2:
                            jump futabadorm
                        if day == 2:
                            play sound "knock.mp3"
                            s "Hey Futaba, are you in there?"
                            f "Umm...Sensei?...I'm right next to you..."
                            s "Huh? Oh, right. Sorry."
                            jump futabahall
                        else:
                            play sound "knock.mp3"

                            s "Hey Futaba, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock

                    "Go Back":
                        jump doorknock
        "Room 5 (Ami & Maya)":
            if roomwithclocks == True:
                jump roomwithclocks
            if ticktock == True:
                jump ticktock
            else:
                "Who do I want to talk to?"
                menu:
                    "Ami (Current Affection - [ami_love])":
                        if ami_love >= 5 and day != 5:
                            jump amidorm
                        if day == 5:
                            play sound "knock.mp3"

                            s "Hey, Ami. Are you in there?"
                            a "Huh? Sensei? I'm right over here."
                            a "Do you not recognize the back of your own [niece]'s head?..."
                            s "Woah. What are you doing there?"

                            jump amihall
                        else:
                            play sound "knock.mp3"

                            s "Hey, Ami. Are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock
                    "Maya (Current Affection - [maya_love])":
                        if maya_love >= 5 and day != 1:
                            jump mayadorm
                        if day == 1:
                            play sound "knock.mp3"

                            s "Hey, Maya. Are you in there?"
                            m "..."
                            s "..."
                            m "Is this really happening?"
                            s "Huh? Oh, hey. I didn't see you there."
                            jump mayahall
                        else:
                            play sound "knock.mp3"

                            s "Hey, Maya. Are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock

                    "Go Back":
                        jump doorknock
        "Go Back":
            if day == 1:
                jump mondaymenu
            if day == 2:
                jump tuesdaymenu
            if day == 3:
                jump wednesdaymenu
            if day == 4:
                jump thursdaymenu
            if day == 5:
                jump fridaymenu
            else:
                jump weekendmenu
        "Go Home":
            if lettert == True:
                jump lettert
...
```