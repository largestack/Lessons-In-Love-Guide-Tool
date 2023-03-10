# Studious Teen Virgin (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Declaration of War](./makotoinvite1.md) (Makoto) is completed)

* Event [Quid Pro Quo](./makotolust5.md) (Makoto) is completed)

* Event [Slope Intercept Form](./day77.md) (Main) is completed)



## Next events

None

## Event properties

* Id: makotoinvite2
* Group: Makoto
* Triggered by label: makotoinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->makotoinvite->makotoinvite2

## Official wiki page

[Studious Teen Virgin](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotoinvite2&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label makotoinvite2:
    play sound "phonebeep.wav"

    "I decide to invite Makoto over and tap on her name in my phone."
    "Being that last time didn’t exactly go {i}well{/i}, I figure that I might need to do something about Ami if I want tonight to end in success."
    "But I need to at least figure out if Makoto is able to get out of work first."
    "………"
    "……"

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    mak "Hello? Sensei?"
    s "Hey. You wouldn’t happen to be free right now, would you?"
    mak "Umm...I {i}could{/i} be free, I suppose. My mom and I are both in the shop right now."
    s "Does she know that I'm the one calling you?"
    mak "No. She’s in the back room at the moment. She probably didn't even hear my phone ring."
    s "Cool. Tell her you need to study again or something."
    mak "Just to clarify, you {i}are{/i} inviting me over...Correct?"
    s "Correct."
    mak "Is your demon-spawn of a [niece] there right now?"
    s "She isn’t a demon-spawn...but probably. I’ll figure out a way to deal with her, though."
    mak "Good. Because I’d very much like to actually be {i}alone{/i} with you if we’re going to be in your house."
    s "Are you trying to seduce me over the phone?"
    mak "N-No! I just...you know! It’s {i}your{/i} house! "
    mak "I’m obviously going to...expect certain things if you invite me over."
    s "What are you expecting, Makoto?"

    play sound "phonebeep.wav"

    "Makoto hangs up the phone without responding to my question, which I’m assuming means that she is, in fact, going to come over."

    scene black
    with dissolve

    "I begin my trip home right away and type out a convincing text message to Ami about how I need her to go grocery shopping."
    "Being as dedicated to pleasing me as she is, I know that she’ll do virtually anything I ask."
    "Which is precisely why I come up with a list of imaginary ingredients for her to procure in order to extend the time Makoto and I will be together for."
    "I truly am a genius when I want to be."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"

    mak "Excuse me..."

    scene makotofirstinvlust1
    with dissolve
    play music "asobeatsex5.mp3" fadein 5.0

    s "Hey. How was your walk over?"
    mak "It would be a lot nicer if you were a normal adult and had a car to pick me up in."
    s "If I had a car to pick you up in, there wouldn’t be much of a reason for us to come {i}here{/i} in the first place."
    mak "I’m not sure what you mean by that, Sensei. Please clarify."

    if bonus == True:
        s "Oh, sure. I just meant that if I had a car, we could relieve our obvious sexual tension there instead of needing to come all the way here for it."
    else:
        s "If I had a car, I would never let anything come between you and me and the act of hugging."

    scene makotofirstinvlust2
    with dissolve

    mak "Uhh...I knew that’s what you were insinuating, but I thought you were at least going to be a little less...direct about it."
    s "No point. You’re smart enough to know that I wouldn’t get Ami out of here unless there was something I wanted from you."
    mak "{i}From{/i} me? Or {i}with{/i} me?"
    s "Whichever. It doesn’t really matter to me."

    scene makotofirstinvlust3
    with dissolve

    mak "Come on! At least be nice when you’re trying to hook up with me!"

    if bonus == True:
        s "But being nice is so exhausting. Do I really have to do that?"
        mak "Yes, you very much do. I have not yet provided consent and can leave at any moment."
    else:
        s "Woah, chill. I just want to hug."

    s "Aren’t you my classroom assistant or whatever? Do I really need consent from you?"

    if bonus == True:
        mak "Obviously. The student handbook says nothing about how classroom assistants are to perform sex acts on their teachers."
    else:
        mak "Obviously. The student handbook says nothing about how classroom assistants are to hug their teachers."

    s "If it doesn’t specifically say anything about that, doesn’t it mean it’s allowed to a certain extent?"

    scene makotofirstinvlust4
    with dissolve

    mak "Well, there is something in the generic section prohibiting physical relationships between teachers and students, so I’m pretty sure this would just fall under that."
    s "You’re such a buzzkill, Makoto."

    scene makotofirstinvlust5
    with dissolve

    mak "Of course I am. That’s my job."
    mak "If I don’t keep you in-line, who else will?"
    mak "And don’t say Ami because she doesn’t count as an actual human being."
    s "I think you two really need to resolve your differences."
    mak "It’s not our differences that make us adversaries- it’s our similarities."
    mak "She can sense how the relationship you and I have is special, and that makes her worried given that she has a different type of special relationship with you."

    if bonus == True:
        mak "Obviously, the one you two have is more of a familial relationship while the one you and I have is more..."
        mak "Intimate?"
        mak "Passionate?"
        s "Wow, nothing gets me in the mood quite like a lecture about the differences between my [niece] and you."
        mak "Well what else am I supposed to do? I don’t know which door leads to your bedroom yet."
        mak "And I can’t imagine you want me taking my clothes off in the living room. That would just be impolite."

        jump makotosecondinvx
    else:
        mak "Obviously, the one you two have is more of a...business relationship while the one you and I have is more..."
        s "Huggy?"
        mak "Sure. Huggy."
        s "Bring it in, Makoto."
        mak "Thanks. This will make me feel less bad about not being able to see my dad anymore."

        scene black
        with dissolve

        "A hug happens and Makoto cries a little."
        "I console her because I am a little nicer in this version of the game."

        $ renpy.end_replay()
        $ makoto_lust += 3
        $ makotoinvite2 = True
        stop music fadeout 10.0

        "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
        "{i}You can now choose between affection and hugging when inviting her over!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label makotoinviteaff:
    scene makotoinvitegen
    with fade

    "I decide to spend the night just hanging out with Makoto."
    "No sexual stuff involved. No teasing involved. Just-"
    "Well, actually, there is {i}some{/i} teasing involved. But it's all in good fun."
    "That's just the sort of dynamic the two of us have together."
    "I tease her. She blushes and yells at me. I pretend I don't feel anything at all for her. She pretends to think that as well."
    "But the moments we share like this, despite being few and far between, serve to contradict that."
    "Right now, in this very moment, it feels like she belongs here."
    "If only I could say the same for myself."

    scene black
    with dissolve

    "The world grows darker by the minute."
    "The house is consumed by the night."
    "Which, of course, means it's about time for Makoto to leave."
    "Ami should be getting home sometime soon anyway."
    "Makoto is reluctant to pack her things and go, but realizes that she must if the two of us are going to be able to spend more time together doing things like this."
    "It's okay, though."
    "I'm sure I'll see her again before long."

    $ makoto_love += 3
    stop music fadeout 5.0

    "{i}Makoto's affection has increased to [makoto_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotoinvitegrind:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump makotoinvitegrindx
    else:
        $ makoto_lust += 3
        stop music fadeout 5.0

        "{i}Makoto's lust has increased to [makoto_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label pornshop20:
...
```

## Code that triggers this event

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label makotoinvite:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump inviteover
    if makotoinvite1 == False:
        jump makotoinvite1
    if makotoinvite1 == True and makotoinvite2 == False:
        jump makotoinvite2
...
```