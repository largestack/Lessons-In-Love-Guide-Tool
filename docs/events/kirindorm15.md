# Bye Bye, Boner (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kirin love greater than or equal to 15

* Event [Enigmatology](./kirinsoccer20.md) (Kirin) is completed)

* Day of week is not Wednesday



## Next events

* [Kirin: Terms & Conditions](./kirindorm20.md)

## Event properties

* Id: kirindorm15
* Group: Kirin
* Triggered by label: kirindorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->kirindorm->kirindorm15

## Official wiki page

[Bye Bye, Boner](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindorm15&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label kirindorm15:
    play sound "knock.mp3"
    stop music fadeout 10.0

    s "Hey, Kirin. Are you home right now?"

    "I knock on Kirin’s door, hoping to be able to spend some time alone with her tonight."
    "But, without knowing what Noriko is up to, it’s highly probable that that won’t be happening at all."
    "That’s not to say I don’t like Noriko either, it’s just-"
    "Kirin seems to function a little differently around me than she does with others."
    "Or, who knows? Maybe that’s just something I tell myself to feel special."

    ki "Yup! Feel free to let yourself in, Sensei. Door is always open to you."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "sleepystreets2.mp3"

    "I quickly open the door and let myself into the room."
    "The same fruity aroma that greeted me the last time I was here welcomes me with open arms once again."

    scene kirinkotatsu1
    with dissolve

    "And before long, I am facing two cute girls and an upside down house."

    ki "Excellent timing as always, Sensei."
    ki "Noriko and I were just about to watch a movie."
    n "Hey! Have you seen this one before, Sensei?"
    n "They play it on repeat in the old district all the time, but Kirin’s telling me she’s never seen it before."
    s "I can't be sure if I’ve seen it if I don’t even know what it’s called."
    s "The weird house certainly doesn’t look familiar to me."

    scene kirinkotatsu2
    with dissolve

    n "Huh...Now that I think about it, I don’t really know what the title is either. But it’s a super weird movie."
    n "You’ll probably like it."
    s "I get why Noriko wants to watch this, but I didn’t take you as the type to be into...abstract movies, Kirin."
    ki "I don’t really care. I just want to hang out under the kotatsu and unwind."
    ki "It’s been a pretty long day, to be honest."
    n "How come it's normal for me to do weird stuff but not normal for Kirin?"
    n "I'm not actually weird, am I?"
    ki "Want to maybe join us or something, Sensei?"
    ki "Not sure if you’re aware, but Noriko is kind of crazy about you, so there’s no chance she’d say no."

    if bonus == True:
        n "All I ask is that there’s no funny business under the table, including any conducted with me. "
        n "I just spent my entire last paycheck on this kotatsu and I don’t want it to get all gross after just a couple uses."

        scene kirinkotatsu3
        with dissolve

        ki "Think you can hold back for an hour or two? Or would you rather go bang on Ayane’s door for some “instant” satisfaction?"
        s "Stop saying questionable things in front of the girl with the pocket knife."
        n "Hm? Did Kirin say something questionable?"
        n "My hearing’s not great, so I probably didn’t catch it."
        s "Good."
        s "But yeah. I wouldn’t mind staying and hanging out here if that’s okay with you two."
    else:
        s "Sure, I'm down for some good clean fun."

    scene kirinkotatsu4
    with dissolve

    ki "Great! I call shotgun."
    n "Hey! I was about to call shotgun!"
    s "Am I a vehicle now?"

    if bonus == True:
        ki "Yup. Noriko and I are gonna ride you all the way to Mt. Fuji."
        n "Just not under the kotatsu."

    ki "Shotgun in this context means you have to sit next to me. "
    ki "Which you should {i}probably{/i} be thanking me for, since God only knows what would happen over on the crazy side."
    n "Nothing would happen! I don’t even normally bite!"
    s "Normally?..."

    scene kirinkotatsu5
    with dissolve

    n "There’s a time and a place for everything, Sensei~"
    s "You know, I could always just sit in the middle and not offend-"
    ki "Nope. I called shotgun. "
    ki "If you break shotgun rules, you have to spend the rest of your life cleaning our room."
    s "You intend to live here forever?"

    "Well, actually...it's not like there's really a choice."

    ki "Okay, whatever. You have to clean the room until we move out."
    s "Fine. Please forgive me for trying to make everyone happy."
    ki "Making everyone happy never works, Sensei. You’ve gotta pick one person and just focus everything you can on them."
    s "I have learned the hard way that you are very much incorrect."

    scene black
    with dissolve

    "Kirin twirls around and heads over to the side of the kotatsu opposite Noriko, gracefully sliding herself under the blanket while keeping it lifted up so I can get under as well."
    "I oblige, realizing halfway through entering that I forgot to take my shoes off."
    "I’m glad that Noriko’s love for me apparently surpasses her desire to keep the kotatsu clean, because this is something that I should very much be called out on right now."

    scene kirinkotatsu6
    with dissolve

    ki "Comfortable?"
    s "Kind of cramped. But I’m pretty large and this isn’t the biggest kotatsu in the world."

    scene kirinkotatsu7
    with dissolve

    n "Mmmm!"
    ki "...What?"
    n "I don’t like how close you two are."

    scene kirinkotatsu8
    with dissolve

    ki "Oh, come on. All we’re doing is sitting..."

    if bonus == True:
        ki "I agreed to not catch feelings or whatever, but I never said I’d stay six feet away from him for the rest of eternity."

    n "I know, but I’m still jealous!"
    n "And also a little excited because my feet are touching Sensei’s knees right now."

    scene kirinkotatsu9
    with dissolve

    ki "Those are {i}my{/i} knees."
    n "Oh my God, why are your knees so big?"

    scene kirinkotatsu10
    with hpunch

    ki "Wha- They’re not! They’re normal-sized knees!"
    n "Nuh-uh. I’ve got tiny knees. They’re like little golf balls that hold my legs together."
    ki "Have fun breaking your legs, then! That’s way too small!"
    n "Kirin, you really KNEEd to chill out right now. Other people might be sleeping."
    ki "..."
    s "..."
    n "Get it?! "
    n "Because, like-"
    n "Knees..."

    scene kirinkotatsu11
    with dissolve

    ki "Hah..."
    n "Oh, come on! That was good!"
    n "And what's with these weird matching expressions?!"
    n "Are you sure you're not in love?!"
    ki "Can we just watch your stupid upside down house movie now?"
    n "You mean the movie that’s been playing the entire time we’ve been talking?"
    n "I kinda just assumed you didn’t care since you weren’t paying any attention to it."

    scene kirinkotatsu12
    with dissolve

    ki "Oh. Would you look at that?"
    ki "It actually {i}is{/i} on."
    ki "I guess it wouldn't hurt to watch a little bit of it. Especially since you’ve seen it so many times."

    "The three of us direct our attention to the giant glowing rectangle in front of us."
    "Somehow or another, and please forgive me for not understanding the science, it channels electricity into moving images."
    "Moving images that...look awfully real for something that is apparently just a movie. "
    "There are five girls in a house together, gathered around a small kitchen table."
    "The windows around them are boarded and they’re eating a strange gray substance piled high on their plates."
    "No one is saying or doing anything."

    ki "…"
    s "…"
    n "…"
    ki "Noriko, what the fuck are we watching?"
    n "It’s an arthouse film! I think. I don’t know."
    n "It’s weird. I’ve actually never finished it. "
    n "Something always comes up in the middle and I have to leave."
    n "It’s like, a {i}really{/i} long movie."
    ki "Are you sure you’re not just falling asleep?"
    n "Of course I’m not falling asleep!"
    n "Probably. "
    n "I don’t know! Maybe! Just watch! Stuff is gonna happen soon."

    if bonus == True:
        jump kotatsux
    else:
        ki "No. I wanna watch the Bee Movie. Put the Bee Movie on."
        n "But you {i}always{/i} want to watch the Bee Movie."
        ki "We want the Bee Movie, we want the Bee Movie."
        n "Kirin, come-"
        s "We want the Bee Movie, we want the Bee Movie."
        n "..."
        ki "BEE MOVIE! BEE MOVIE! BEE MOVIE!"
        s "BEE MOVIE! BEE MOVIE! BEE MOVIE!"
        n "Jesus, fine. We can watch the fucking Bee Movie."

        scene black
        with dissolve

        "Kirin and I bust into a loud cheer that echos through the dorms."
        "Eventually, everyone shows up to investigate and we all wind up watching the Bee Movie together."
        "I love the Bee Movie."

        $ renpy.end_replay()
        $ kirindorm15 = True
        $ kirin_love += 1
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "………"
        "……"
        "…"


        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label kirindorm20:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label kirindorm:
    if kirin_love >= 10 and day271 == True and day != 3 and utadorm5 == True and iodorm5 == True and kirindorm10 == False:
        jump kirindorm10
    if kirin_love >= 15 and kirinsoccer20 == True and day != 3 and kirindorm15 == False:
        jump kirindorm15
...
```