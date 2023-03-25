# Dear You (Niki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Sisters](./nikiinvite1.md) (Niki) is completed)

* Event [Loxosceles Reclusa](./norikodorm25.md) (Noriko) is completed)



## Next events

* [Main: Three Amigos](./christmastwo1.md)

## Event properties

* Id: nikiinvite2
* Group: Niki
* Triggered by label: nikiinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->nikiinvite->nikiinvite2

## Official wiki page

[Dear You](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikiinvite2&go=Go) for more details.

## Event code

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikiinvite2:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "And this time, I’m going to clarify that I am inviting her over to hang out with {i}me{/i} rather than my [niece]."
    "Granted, Ami should be off doing other stuff today anyway, so Niki wouldn’t even be able to ditch me if she wanted to."

    play sound "phonebeep.wav"

    ni "Am I bossy?"
    s "Hello, Niki."
    ni "Hi. Am I bossy?"
    s "Well, considering the last time you came over my house, you kicked me out...I’m going to say yes."
    ni "Damn it."

    if bonus == True:
        s "There was also that one time you stole my shirt and decided that it was yours. And when I asked for it back, you made me finger you."
        ni "I did not {i}make{/i} you do that! "
    else:
        s "There was also that one time you stole my shirt and decided that it was yours. And then when I wanted it back you made me take you to small claims court."
        ni "That last part never happened!"

    s "That’s not how I remember it. "
    ni "Shut the fuck up."
    s "See? You’re being bossy again right now. "
    ni "You fucking-"
    ni "I was talking about my vocal coach. She quit today because, apparently, I’m too bossy. "
    s "Aren’t you a vocal coach? Just teach yourself."
    ni "You’re a fucking idiot. I’m coming over."
    s "I’m getting mixed signals right now."
    ni "Well, we’ll fucking...unscramble them or whatever when I get there. Bye."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "Well, I forgot to have her confirm that she’s coming over for {i}me{/i}, but I guess that with Ami being gone, there’s no one else she {i}can{/i} be there for at the moment."
    "Unless, of course, she brings her sister again."

    if bonus == True:
        "Which, if that’s the case, it once again ignites the fire that is my passion to have sex with two Nakayamas at once."
        "Here’s hoping that fire burns bright tonight."
    else:
        "Which, if that’s the case, I hope I have enough time to clean up the house first."

    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene nikicouch1
    with dissolve
    play music "comfort.mp3"

    ni "Hi. Now, about me being bossy-"
    s "No Noriko tonight?"

    scene nikicouch2
    with dissolve

    ni "Excuse me? Am I not good enough for you anymore? You require the smaller version with shitty taste in fashion as an added bonus? Give me a fucking break."
    s "Jeez. If I had known you were in such a bad mood today, I wouldn’t have invited you over."
    ni "Oh please. I drove {i}myself{/i} here- and I probably would have done that whether you invited me or not."
    s "You have a car?"
    ni "I have three cars. I’m famous. "
    ni "Technically, I’m not the title holder of any of them. They belong to the agency. But they’re still {i}mine{/i}."
    s "Cool. This means I don’t have to take the bus anymore."

    scene nikicouch3
    with dissolve

    ni "Oh, so I’m your chauffeur now? Fantastic. What a huge step up from the most popular public figure to ever emerge from Kumon-mi."
    ni "Do you have Netflix?"
    s "Are you going to see if my [niece] wants to watch a movie?"
    ni "Is she here?"
    s "She is not."

    scene nikicouch4
    with dissolve

    ni "Good. I wanted to be alone. I missed you."
    s "And I thought {i}Yumi{/i} was tsundere."

    scene nikicouch5
    with dissolve

    ni "Who the fuck is Yumi?! Are you cheating on-"

    scene nikicouch6
    with dissolve

    ni "Oh. Right. We’re not dating anymore."
    s "Yeah. And it’s probably good that you remind yourself of that before you say anything else embarrassing."
    ni "Shut up. I hate you. Let’s watch a movie or something."
    s "Yes, dear. Let me just put on the kettle and check our joint bank account first."

    scene nikicouch7
    with dissolve

    ni "That’s not funny."
    s "Would it be funnier if we {i}were{/i} dating?"
    ni "Do you want to?"
    s "…"

    scene nikicouch6
    with dissolve

    ni "Just kidding. Where do you keep the remote?"
    s "…"

    scene black
    with dissolve2

    s "Right on the table..."

    "Girls are confusing."

    if bonus == True:
        "Especially girls that spend their entire life waiting on you despite you being a heaping pile of shit who takes advantage of girls while they sleep."
    else:
        "Especially ones like Niki who always steal clothing and then force you to rack up millions of yen in legal fees trying to get your stuff back."

    "Just kidding."

    if bonus == True:
        "I didn’t do anything."
        "I’ll never do anything."
        "…"
        "Not until I’m supposed to."

    play sound "static.mp3"
    scene nikil1 with flash
    scene nikil2 with flash
    scene nikil3 with flash
    scene nikil4 with flash
    scene nikil5 with flash
    scene nikicouch8 with flash
    stop sound

    "It feels a little different being alone with Niki than it does...pretty much anyone else."
    "You’re free to call it lingering history if you want, but there’s just something about her presence that makes me feel..."
    "“Safe” isn’t the right word."
    "Nor is “comfortable.”"
    "But I feel a little closer to existing than I normally do when I’m with her."
    "Then again, it could always be something a little more primitive than that."
    "I’ve heard in the past that the sense that will whack you over the head with nostalgia harder than anything else out there is scent."
    "Maybe it’s {i}that{/i} that’s causing me to feel the way I do?"
    "And while I can’t pinpoint {i}where{/i} I’ve felt this way before, I know I’ve felt it- which is more than I can say for most things or situations."
    "So as the two of us sit shoulder to shoulder on this couch, watching a series of moving pictures combining to tell a partially intelligible story, I think about the past."
    "Just, there’s nothing there."
    "I attempt to envision a younger version of Niki."
    "But again-"
    "There’s nothing there."
    "And it’s almost as if I never existed at all."
    "And that whatever scent brought on the prospect of me actually being {i}anywhere{/i} is all just a lie."
    "I should focus on the television."

    if bonus == True:
        ni "Oh. They’re having sex."
    else:
        ni "Oh. They’re hugging."

    ni "That means someone is going to die soon."
    ni "That’s like, rule number one of horror movies."
    s "…"

    scene nikicouch9
    with dissolve

    ni "Do you remember that time you came to sleep over and we stayed up all night, watching Friday the 13th under the covers?"
    s "What do you think, Niki?"

    scene nikicouch10
    with dissolve

    ni "Aww, really? That one’s gone too?"
    s "They’re all gone. There’s nothing there anymore."
    ni "Man. That was such an awesome night. It was like {i}right{/i} before we started dating and our hands kept touching and it was so sweet and awkward and now thinking about it makes me want to die."

    scene nikicouch11
    with dissolve

    ni "Not like, sad dying, though. Embarrassment dying. Like it’s just...really cringey and- oh. Yup. They’re definitely dead now."
    s "Your tangent made us miss the murder. Who knows when the next-"

    scene nikicouch12
    with dissolve

    if bonus == True:
        ni "Look. More people having sex. I bet they’re next."
    else:
        ni "Look. More people hugging. I bet they’re next."

    s "Wow. People who write horror are really just...not that impressive, are they?"
    ni "Not this kind, at least. But that’s what makes slashers fun. You always know what’s going to happen, so you never really get jump scared or anything."
    ni "Fucking jumpscares. Such a lazy form of horror, don’t you think?"

    play sound "imscared.mp3"
    scene tree3 with flash
    scene nikicouch12 with flash
    stop sound

    s "I agree wholeheartedly. But I’ve never really been a big fan of horror to begin with."
    ni "What are you talking about? Yes you have. You used to love this stuff."
    s "Oh. Well, not the version of me that I’m familiar with. But it’s not like my memories are that “full” yet. So who knows what’ll happen in the future?"
    ni "You’re weird. "
    s "That’s a fair assessment."

    "The two of us continue to sit there watching the movie and-"

    if bonus == True:
        jump nikicouchx
    else:
        "It's actually a pretty good movie."

        $ renpy.end_replay()
        $ nikiinvite2 = True
        $ niki_lust += 1
        stop music fadeout 5.0

        "{i}Niki’s lust has increased to [niki_lust]!{/i}"
        "{i}You can now invite her over after[school] and on weekends!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label nikilovesyou1:
...
```

## Code that triggers this event

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikiinvite:
    if nikiinvite1 == False:
        jump nikiinvite1
    if nikiinvite1 == True and nikiinvite2 == False:
        jump nikiinvite2
...
```