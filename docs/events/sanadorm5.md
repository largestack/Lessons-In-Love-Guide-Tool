# Recluse (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 5



## Next events

None

## Event properties

* Id: sanadorm5
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm
* Triggered by path: sanadorm->sanadorm5

## Official wiki page

[Recluse](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm5&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm5:
    play sound "knock.mp3"

    "I knock on the door and wait a moment to see if anyone responds."
    "Well, to see if {i}Sana{/i} responds."
    "If anyone other than her or Ayane answered, I'd probably just leave."

    if day == 4:
        "Actually, if Ayane answered, I'd probably leave as well considering that Ayane is right in front of me and that would mean there is a clone of her inside of the room."

    "Either way, no one does- but I’m suddenly compelled to knock again for reasons beyond my comprehension."

    play sound "knock.mp3"

    s "Hello? Is anyone in there?"
    sa "S..."
    sa "Sensei?..."
    s "Yup. Just dropping by to see how you're doing."
    sa "You're..."
    sa "Dropping by...my {i}room?...{/i}"

    "I guess I'm going to have to speak to Sana through the door until I can convince her to allow me inside of her room."

    s "Is that weird?"
    sa "I...uhh..."
    sa "Yes?..."
    sa "I don't...think it's normal for...teachers to come to their students' rooms..."
    s "Well, I'm here. So I guess this just means either I leave or we hang out."
    s "The choice is in your hands."
    sa "Uhh..."
    s "I'll understand if you don't want to, Sana. It's fine."
    sa "I...I didn’t say that, but..."
    s "If it makes you feel any better, I'm doing this for educational purposes."
    sa "What...sort of educational purposes...would that even-"
    s "It's part of that new strategy I was talking about in class. The one where we need to start being friendlier and less formal."
    sa "I don't know, Sensei...This still seems really weird..."
    s "I don't think so. It's just a totally normal and socially acceptable after-school self-invitation."
    sa "..."
    s "So, can I come in?"
    sa "I'm...starting to think you won't go away even if I say no..."
    s "That's a fair assumption."

    play sound "lock.mp3"

    "I hear the sound of the door unlocking and take that as my cue to make my way inside."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene smallredux1
    with dissolve2

    sa "G...Good evening..."
    s "Thanks for letting me in. I get that it probably feels a little weird."
    sa "It's...more than just...a {i}little...{/i}"
    sa "But...um...here we are..."
    sa "The place I...live..."
    s "I’m going to go out on a limb here and assume your side is on the right?"
    sa "Umm...yeah...If you’re looking at it...from your direction..."
    sa "If you...look at it from mine it’s...it's on the...left..."
    s "Thank you for explaining how directions work, Sana. I had forgotten."
    sa "You're..."
    sa "You're welcome..."
    s "…"
    sa "…"

    "This is even more awkward than I thought it would be."

    s "I'm going to go out on a {i}second{/i} limb here and assume you’ve also never been alone with a guy before, have you?"
    sa "R-Right..."
    sa "But you’re just my teacher so...I don’t...really look at you that way..."
    s "You don’t...view me as a male?"

    scene smallredux2
    with dissolve

    sa "Oh! N-No! That’s not what I meant! I obviously...know you're...uhh...It’s just that...umm..."

    scene smallredux3
    with dissolve

    sa "Hah..."
    sa "This is just...kind of embarrassing for me, so..."
    sa "I'm probably going to...say a lot of things that are...um..........bad."
    s "Noted."

    "Sana’s half of the dorm is more or less what I expected."
    "The only thing I'd say is different from my imagination is the lack of black, but I guess all the spider stickers make up for that."
    "Apart from that, everything seems mostly normal."
    "Bed? Check. Video game stuff? Check. Creepy stuffed animal facing the ceiling? Another check."
    "Considering that only one of those three things is worth talking about, though, I pretty much know where to move the conversation next."

    s "I didn’t know you were into games, Sana."

    scene smallredux4
    with dissolve

    sa "Oh! Y...Yes!"
    sa "I don’t...really go out much, so..."
    sa "I sort of...play games to pass the time..."
    s "Well, maybe we could play something together sometime? That might be a decent way to get to know each other."

    scene smallredux5
    with dissolve

    sa "You...play games, Sensei? You don’t think you’re...too old for that?"
    s "There’s no such thing as being ‘too old’ for video games, Sana. That's a myth."
    s "Also, don’t call me old."
    sa "Oh, I...I didn't mean it like that...I’m sorry..."
    sa "It’s just that...my mom is always telling me I should go out more, and...umm...experience the world, I think she said?..."
    sa "Which...isn't really possible since we can't leave Kumon-mi, so..."
    s "I think you should do whatever you like to do. Life quickly becomes miserable once you start worrying too much about other people."

    scene smallredux4
    with dissolve

    sa "Th-Thank you...Sensei...I...I completely agree..."
    sa "If you want...maybe we...{i}could{/i} play together sometime?..."
    s "Sounds good to me. What sorts of games are you into, exactly?"
    sa "Mostly RPGs...and simulation games..."
    sa "I play...um...visual novels too, but...I...prefer playing those alone, so..."
    s "Well, we can play whatever you choose. I can't remember the last time I played anything, though, so try not to beat me too badly."

    "I conveniently leave out the detail where I can't remember anything else either."

    sa "Heheh..."
    sa "I...make no promises..."

    scene black
    with dissolve2

    "Sana turns around and steps toward her bed, but I remain where I am since I can't imagine she's anything like her roommate in terms of her willingness to cozy up to an older man."
    "At least not yet. I have no idea how Sana will end up a little further down the line. But that line is so far away from the entrance to her dorm room that there's no point in even acknowledging it yet."

    scene sanaroom1
    with dissolve2

    sa "This...isn't as scary as I thought it was going to be..."
    sa "I'll admit that...I didn't really want to let you inside, but..."
    sa "You've been really nice so far, so...thank you..."

    "Sana begins to fiddle with a bow wrapped around the neck of an ugly stuffed animal- admitting things to {i}it{/i} since admitting them to {i}me{/i} would be much harder."

    s "There's no need to thank me. I'm sure I'll do plenty to upset or anger you in the future. It would just be rude to do that on my first trip here."

    scene sanaroom2
    with dissolve

    sa "Well...thank you so far, then..."
    sa "It might not sound like it, but..."
    sa "I...{i}do{/i} like talking to you, Sensei..."
    sa "Or...trying to, at least..."
    s "Don’t worry about the ‘trying’ part. Things will start coming out a lot more naturally in time."
    s "Just treat me like a friend until you’re more comfortable and I’m sure everything will be fine."

    scene sanaroom3
    with dissolve

    sa "R...Right...Yeah..."
    sa "Like a friend..."
    s "..."
    sa "..."
    sa "I’m sorry...I’m just having...um...a hard time...thinking of you as anything more than my teacher right now, but..."
    sa "But I'm sure that...will change eventually..."
    s "Good. Because a little piece of my heart broke off earlier when you said you didn’t even think of me as a {i}guy.{/i}"

    scene sanaroom4
    with dissolve

    sa "That!...Well!..."
    sa "..."
    sa "I said...I'm sorry! I...don't know what else you want!"
    s "All I want is to make you happy, Sana."
    sa "Then...don't bring up the...weird things I say on accident!"
    s "Say less weird things and that won't be a problem."
    sa "I..."

    scene sanaroom5
    with dissolve

    sa "I'll try..."
    sa "And...umm...I’ll...try my best to make you...a little happy too..."
    sa "As your...umm..."
    sa "As your...friend..."

    scene black
    with dissolve

    "Feeling like that's a good place to leave things for the night, I turn around and reach for the door, only to be stopped a split second later."

    scene smallredux5
    with dissolve

    sa "Huh?....Are you leaving already, Sensei?..."
    s "Yeah. I think we’ve made enough progress for the day."
    s "You helped me kill some time {i}and{/i} I got to see your room. Those are two solid victories."

    scene smallredux4
    with dissolve

    sa "Hahah...If you say so..."
    sa "Will you, umm...come back soon?..."
    sa "I'd...like to maybe...do this again sometime..."
    s "Of course."
    s "You can always come visit me too, you know. I'm normally in my office after school."
    sa "I’ll...try to remember that..."
    s "Sounds good. I’ll see you later, Sana. Thanks for letting me in."
    sa "Yeah..."
    sa "See you later...Sensei..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "I exit the room and start making my way back to the street. "
    "I figured it would take Sana a little longer to let me inside, but I guess my initial read on her wasn't as accurate as I thought."
    "Either way, I’m glad she’s finally starting to warm up to me."
    "Here's hoping that doesn't stop anytime soon."

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm5 = True

    "{i}Sana’s affection has increased to [sana_love]! You can now spend time with her in her room!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadorm10:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
...
```