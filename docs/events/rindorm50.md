# Technicolored Happiness Explosion (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 50

* Event [The Paragon of Not Worrying About Stuff](./cafe50.md) (Rin) is completed)

* Day of week is not Monday



## Next events

* [Molly: Resurrection Sickness](./mollycafe25.md)

## Event properties

* Id: rindorm50
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rindorm50

## Official wiki page

[Technicolored Happiness Explosion](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm50&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm50:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Rin’s door, but immediately upon ending my ritualistic five knocks, I notice an unusual noise coming from inside."
    "And, of course, due to the volume of that noise, she’s unable to hear me and let me in- banishing me to a night in the hall with nothing to do."
    "Defeated, I slide my hands into my pockets and head home."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Just kidding. "
    "I’ve never let a door stop me before and I don’t intend to start doing so now."

    scene rinotohaguitar1
    with dissolve
    play music "brighterdays.mp3"

    "Besides, the “unusual noise” was just these two lovebirds(?) playing guitar and ignoring my role as the person they are supposed to be falling in love with instead of one another."
    "Not that I want their “love” or anything."
    "Their bodies would suffice."
    "But alas. Lesbians."

    r "Yo! Here to jam with us, Sensei?"
    s "Sorry. I left my guitar at home."
    o "Wait...you don’t actually play, do you?"
    s "I do not. That was what those of us in show business call a “joke.”"
    o "Damn. For a split second, I thought you might actually be cool."
    s "Okay, Rin. You’ve had your fun. Time to break up with Otoha."

    scene rinotohaguitar2
    with dissolve

    r "I refuse! Have you {i}seen{/i} how cute she is in those pajamas?! Her thighs are like “BAM!”"
    r "Ain’t no way I’m giving that up, homie!"
    o "You know, I thought all of the commentary on my appearance might mellow out once we started dating...but I’m pretty sure it’s actually gone the complete opposite way."

    scene rinotohaguitar3
    with dissolve

    r "Am I really that bad?"
    o "I mean...I kinda knew what I was getting myself into."
    o "It would be nice if you’d wait a little longer before openly admitting to wanting to see how I look without my clothes on, though."
    s "Smooth, Rin."

    scene rinotohaguitar4
    with dissolve

    r "Wait, no! I definitely didn’t say that! Did I think it? Of course! But I’ve been getting a lot better at not screaming my thoughts out when Otoha is around!"
    s "Are you sure about that?"
    o "Just give it a rest, dude. Neither one of us is gonna change her. She’s too set in her ways."
    s "I am surprised you were willing to accept that part of her."

    scene rinotohaguitar5
    with dissolve

    r "Woah! Rude."
    o "Eh. It was bound to happen sooner or later."
    o "I’ll admit that it happened...a {i}lot{/i} sooner than I would have expected, but it’s not like I was ever gonna just reject her when she’s been pushier than anyone I’ve ever met."

    scene rinotohaguitar6
    with dissolve

    r "It looks like sometimes...all you need is a little persistence. "
    r "Or a lot of persistence. "
    r "And a group of friends who are willing to put up with your nonsense as you prepare yourself for imminent destruction only to be turned into like, the third happiest girl in[school]."
    s "Who are the first two?"

    scene rinotohaguitar7
    with dissolve

    r "Uta and Miku, obviously. I could get like ten girlfriends and still not be as energetic as either of them."
    o "Uhh...let’s try to stick to just one girlfriend for now, okay?"

    scene rinotohaguitar8
    with dissolve

    r "Yes, ma’am!"
    s "Wow. You two have barely even started dating and you’ve already got her wrapped around your finger."
    o "Yeah but, to be fair, she kind of wrapped herself around it before I even knew what was going on."
    s "Well, all things considered, you’re very cool about the whole thing. So thanks."

    scene rinotohaguitar9
    with dissolve

    o "Wait, why are you thanking me? That just makes it sound like I’m doing this as a favor to you. "
    o "You do know I actually...{i}do{/i} like Rin, right? Just...not as much as she likes me. Yet. I think."
    o "I don’t know. Just don’t thank me."

    if rinbetrayed == False:
        r "I’m pretty sure Sensei is just glad that I don’t have to keep bothering him with all of my obsessions and whatnot."
        s "I don’t mind your obsessions. I’m just happy you’re not about to explode anymore."
        r "If there’s anything you should know about girls like me, it's that we’re ready to explode at any given moment, Sensei."
        r "Just now, it will be a...technicolored happiness explosion. Or something."
        s "Right..."

    else:
        r "I’m pretty sure Sensei is just a little impressed because I managed to get a girlfriend he hasn’t already stuck his fingers inside."
        s "I don’t like how you can say that with a smile on your face."
        r "What can I say? It’s easy to fake a smile when you’ve already desensitized yourself to the feeling of betrayal."
        o "…"
        o "Yeah so...about...{i}not{/i} that."

    s "So, anyway, how come you’re willing to play guitar for Otoha and not me?"

    scene rinotohaguitar10
    with dissolve

    r "Uhhhhhhh...because girlfriend?"
    r "I’d jump off a bridge if Otoha asked me to."
    o "First off, no. Don’t do that."
    o "Second, have you really never heard her play before?"
    o "You’ve heard {i}me{/i} play before and I barely even know you."
    s "True. But Rin doesn’t really wander off to parks and play for tips."
    s "I just remember suggesting that she play for me sometime and...she’s yet to actually do it."

    scene rinotohaguitar11
    with dissolve

    r "Oh, yeah! I remember that! It was one of the first times you came to my room, I think."
    r "Wow, that feels like forever ago now."
    s "Nah. Just three school years."

    scene rinotohaguitar12
    with dissolve

    r "Three...school years..."

    if bonus == True:
        o "You weren’t her middle[school] teacher as well, were you?"
    else:
        o "You weren’t her high school teacher as well, were you?"

    s "Nope. Time is just a construct that we’re free to manipulate and measure however we want because it doesn’t actually exist and is entirely subjective."
    o "But..."
    o "But...we already came up with a way to measure it?"
    r "…"

    scene rinotohaguitar13
    with dissolve

    o "You doing okay over there?"
    r "…"
    o "Rin?"

    scene rinotohaguitar14
    with dissolve

    r "Oh! Yeah! Sorry. Just got lost in thought for a second."
    r "Time really does fly sometimes, huh?"
    o "It really does. Even I feel like I’ve known Sensei longer than I actually have, but...I guess that’s just part of being young?"
    s "Ahh, yes. "
    s "I, too, am young."

    scene rinotohaguitar15
    with dissolve

    o "Sure are, bud. Hang in there."
    r "We’re rooting for your health, Sensei."

    if bonus == True:
        s "Guys, I’m only thirty-one. That’s really not that old. "
        r "Nonsense. Thirty is when [young]people become old. "
        s "You’re going to change that number to forty when you’re in your twenties and you know it."
        r "No way, man. Otoha and I are gonna stay [young]forever. We refuse to grow up."
        r "Yolo and all that stuff. You know."
    else:
        s "Guys, I’m only 5000. That's not even that old."
        o "Uhh...it kind of is."

    "Welp, in a world full of shattered wishes, I guess one or two were bound to come true."
    "Because there’s definitely no way either of them is growing up anytime soon."
    "Well, at least not physically. "
    "I’m sure there’s still enough trauma to go around for both of them to get a little older in the vague sense of maturity."
    "But for now, I don’t see any harm in letting them enjoy their time together."

    scene rinotohaguitar16
    with dissolve

    o "Welp, I guess it’s time for me to get going."

    "Oh."
    "Or not."
    "It looks like I may have spoken too soon."

    r "Yeah...I guess so."
    r "Have fun talking to your mom. Tell her I said hi even though I’ve never met her before. I’m sure that won’t be weird or anything."
    o "It will. But okay."

    scene rinotohaguitar17
    with dissolve

    o "Night, man. "
    o "Try not to creep on Rin too much, okay? She’s taken now."

    if bonus == True:
        s "Isn’t everything I do creepy to you?"
        o "Kinda, yeah. But you know what I mean."
    else:
        s "Of course, Otoha. I respect you and you can trust me."

    scene rinotohaguitar18
    with dissolve
    play sound "dooropen.mp3"

    o "Goodnight again!"
    o "See you guys in[school]!"
    r "Night..."

    "Otoha disappears into the hall and Rin stays silent for a moment, likely wishing that she’d gotten to spend a little more time alone with her before I showed up."
    "But it looks like I get the pleasure of taking up the rest of her evening now, so at least I managed to come out on top in some form tonight."

    r "Do you ever just...look at something and think like, “Damn. You’re too good for this world.”"
    s "I’m looking at something just like that right now."

    scene rinotohaguitar19
    with dissolve

    r "Woah! Nice one, Sensei! You’ve got some game after all."
    r "Now, go use it on somebody who isn’t holding out hope that their girlfriend gives up on taking their relationship slow and bumps things up to the next level right away!"
    s "Still no progress on that end?"

    scene black
    with dissolve

    "I take a seat on the bed and Rin places her guitar on the floor, switching off the amplifier so that we are not destroyed by a wave of feedback."
    "Immediately, she turns to me and picks up right where we left off."

    scene rinotohaguitar20
    with dissolve

    r "No progress yet. But I’m probably just making myself sound a little more desperate than I actually am."
    r "I don’t mind waiting at all."
    r "Do I dislike it? Yuuuuuuuup. "
    r "But I’ve waited years to actually have a girlfriend and, now that I have one, I wanna do things right. You know?"
    s "Well, you clearly have more willpower than I do."

    if rinbetrayed == True:
        scene rinotohaguitar21
        with dissolve

        r "Gee, you think?"

        if bonus == True:
            r "Literally everyone in the world has more willpower than you if your response to a friend asking you to try and keep your hands off someone is to go and immediately finger them."
            s "It wasn’t immediate-"
        else:
            r "Literally everyone in the world has more willpower than you if your response to a friend asking you to try and keep your hands off someone is to go and immediately hug them."
            s "I am sorry. I just like hugs so much."
            s "It was a mistake."

        r "I don’t fucking care what it was. You promised me something and then proceeded to break that promise without even a second thought."
        r "You’re a shitty friend with zero willpower and it’s a miracle I managed to win over Otoha before you tried ruining that too."
        s "Can’t I just be happy for you this time?"
        r "I don’t know. {i}Can{/i} you?"
        s "I’m...going to try."
        r "Well...I hope you succeed."

    else:
        scene rinotohaguitar21
        with dissolve

        r "Yeah. I guess that isn’t really one of your strong suits."

        if bonus == True:
            r "But hey, you’ve never tried hooking up with me despite like six million opportunities, so that’s cool."
        else:
            r "But hey, it's not like we've ever hugged, right? And I know you've probably wanted to."

        s "I mean...we {i}did{/i} kiss once. "
        r "Yeah. We were right here when it happened. I remember it well."
        r "But that’s a thing of the past. And once Otoha is ready, I’m going to fill my mind with six million more kisses from her and try and push the one with you out."
        s "Woah. Rude. That seemed like a big moment for us."

        scene rinotohaguitar22
        with dissolve

        r "Because it {i}was.{/i}"
        r "But it’s not anymore. "
        r "And if we’re going to keep being friends...that’s something we should try our best to understand."
        s "…"
        r "…"

    scene rinotohaguitar23
    with dissolve

    r "Buuuuuuut...that’s enough of the serious stuff for now."

    scene rinotohaguitar24
    with dissolve

    r "Rin Rokuhara is in better shape than ever and ready for whatever curveballs life throws at her!"
    r "There’s absolutely nothing you can say that could bring me down right now! I’m on top of the world."
    s "Does Molly know yet?"
    r "…"
    s "…"

    scene rinotohaguitar25
    with dissolve

    r "Oh, god damnit. "
    s "I’m going to take that as a yes. "
    r "You knew, didn’t you?"
    s "Knew what? I have no idea where things stand with you two and have a history of revealing more than I should in situations like this."

    scene rinotohaguitar26
    with dissolve

    r "Hah..."
    r "Molly and I are taking a little break from each other right now."
    r "And since you brought her up specifically, I’m sure you know why."
    s "I see."
    r "Why didn’t you tell me? "
    s "I didn’t really think it was my place to get involved."
    r "But you’ve been getting involved in {i}my{/i} lovelife since day one."
    s "Correction: You have been dragging me into your lovelife since day one."
    r "Same difference, dude. It would have saved us a huge fight if you’d only let me know about how she felt beforehand."
    s "You’re not actually blaming {i}me{/i} for this, are you?"

    scene rinotohaguitar27
    with dissolve

    r "No...I’m not blaming anyone for anything."
    r "In hindsight, it was really fucking obvious and I feel like an idiot for not realizing it."
    r "But, like..."
    r "On the opposite of things, I could {i}not{/i} have made it {i}any more obvious{/i} that I don’t see Molly as someone I want to {i}be{/i} with."
    s "I guess you two are just good at...conveniently misunderstanding one another?"
    r "How hard is it to understand, “I don’t see you as anything more than a friend and I hate that you stole my first kiss from me?”"
    r "I’ve told Molly so many times that I don’t look at her that way...and then she goes and fucking tackles me to the ground when I’m {i}on my way to confess to another girl{/i} and tries to kiss me."
    r "What the fuck am I supposed to do, man? She intentionally threw me into a situation she knew I didn’t want to be in and expected me to just...accommodate her."
    r "Like...it sounds rude when I say it like this...but take a fucking hint. You know?"
    r "I get that you can’t help who you fall for and stuff...I fall easier than anyone."
    r "But if someone tells you waaaaay ahead of time, “I don’t want this,” you can {i}absolutely{/i} help trying to force it on them anyway."
    s "Just to be clear, I’m not trying to get involved in whatever is going on with you two. "
    r "Nothing. Nothing is going on. Because if anything {i}were{/i} to go on, I’d have to drag Otoha into it. And I don’t want to do that to her."
    s "That’s fine. I just like both you and Molly and wouldn’t want either of you to stay upset for longer than a necessary amount of time."

    scene rinotohaguitar28
    with dissolve

    r "What is the “necessary amount of time” we’re supposed to be upset for?"
    s "Any amount of time that doesn’t start negatively influencing the people around you."
    r "Boy, do I have bad news for you."
    s "Mental illnesses or whatever don’t count. That’s something you can’t help. "
    r "Yeah..."

    scene rinotohaguitar29
    with dissolve

    r "Yeah...speaking of that..."
    s "Uh-oh."
    r "You, like..."
    r "You have a hard time being happy sometimes too, right?"
    s "I try not to really think about it."
    r "It’s like..."
    r "It’s just weird."
    r "Because..."
    r "Because everything will be totally fine. And you’ll have literally no reason to {i}not{/i} be happy."
    r "And so you try to be. "
    r "You try really hard because that’s how you know you {i}want{/i} to feel. Or how you {i}should{/i} feel."
    r "But then-"
    r "All of a sudden-"

    scene black
    stop music

    r "It’s just nothing."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm50 = True

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm50special:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

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
    if rin_love >= 50 and cafe50 == True and day != 1 and rindorm50 == False:
        jump rindorm50
...
```