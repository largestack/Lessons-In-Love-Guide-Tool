# Three Second Smile
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=streets5&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 5



## Next events
None

## Event properties
* ID: streets5
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets

## Event code
File: \game\YumiEvents.rpy
Code:
```python
...
label streets5:
    scene citynoon
    with dissolve
    play sound "streetnoise.mp3" fadein 3.0

    "Once again, I find myself aimlessly walking through the streets of Kumon-mi."
    "But, despite it being the middle of the day in what appears to be one of the more urban locales this city has to offer, things seem pretty calm."
    "I’m risking the chance of not seeing Yumi by trying out a different path today, but it's not like she's looking forward to seeing me anyway."
    "And hey, even if I don’t run into her, I’m sure I’ll be able to find something to do."
    "After all, Kumon-mi is-"

    y "Oh, God fucking damnit."

    scene streetsfive1
    with dissolve
    play music "yumiska.mp3" fadein 4.0
    stop sound fadeout 5.0

    s "Oh. Hey, Yumi."
    y "Don’t ‘Hey Yumi’ me. What the fuck are you doing here?"
    s "Am I...not allowed to walk around?"
    y "You can...walk as much as you fuckin' like. I just don't want you followin' me and shit."
    s "I have literally never seen you in this part of town. What makes you think I'd be following you?"
    y "Oh, I don't know. Maybe the fact that you chose the one fucking day I decided to go somewhere else to go exploring?"
    y "Only reason I came over here in the first place is because I was gettin’ tired of you showin’ up all the fuckin' time."
    y "You stalkin' me, asshole? Cause if you are, I swear to God I'll gut you like the fucking pig you are."

    "Note to self: Yumi apparently owns this city and I am not allowed to go anywhere anymore."

    s "Wow. What’s your problem today?"

    if day44 == True:
        scene streetsfive2
        with dissolve

        if bonus == True:
            y "Oh gee, I don’t know! Could it be that maybe I’m still a little pissed off about you sticking your fucking tongue down my throat?!"
            y "Do you think that could be it, Sensei?"
        else:
            y "Oh gee, I don’t know! Could it be that maybe I’m still a little pissed off about you fucking hugging me?"

        s "..."
        y "You just gonna stay silent now?!"
        s "To be fair, that's not really an easy thing to respond to."
        s "I told you I was sorry, Yumi."
        s "It's not like that was something I...anticipated doing."
        s "It just kind of happened."

        scene streetsfive3
        with dissolve

        y "Yeah. It sure fucking did."
        y "You know, maybe {i}less{/i} shit like that would happen if you didn’t get a fucking hard-on for every single [teenage]girl who makes eye contact with you?"
        s "It's going to be hard to put this behind us if you keep bringing it up, Yumi."
        y "Stop saying my fucking name. It's grossing me out."
        y "You wanna put shit behind us? I'll do you one better."
        y "How about we put {i}everything{/i} behind us and you go back to letting me kill time on my own? How does that sound?"
        s "Exceedingly difficult if we're going to keep bumping into each other like this."
        y "Maybe try bumping into a moving truck next time instead. Would save me a hell of a lot of a stress."

    else:
        y "What, I ain't allowed to be pissed off unless I've got a specific reason? Eat a dick. Some people are just angry, dude. Give me a fucking break."
        y "It’s shitty enough that I have to deal with you in[school]. I don’t want to be dealin’ with you on weekends, too."
        s "You barely come to[school], though."

        scene streetsfive3
        with dissolve

        y "Well maybe I’d start showin’ up more if my teacher wasn’t such a fucking douche."
        s "Since when does trying to stop someone from picking on other girls turn you into a douche?"

        scene streetsfive2
        with dissolve

        y "I don’t fuckin’ pick on anyone! That’s just how I talk!"
        s "Really? Cause this might sound a bit presumptuous, but it looks to me like you might just be trying to get attention."

        scene streetsfive3
        with dissolve

        if bonus == True:
            y "Pfft. If I wanted attention from you I’d just take my fucking shirt off or something."
        else:
            y "Pfft. If I wanted attention from you I’d just punch another old person or something."

        "To be fair, that would definitely work."
        "But that's not really what we're talking about here."

    s "..."

    scene streetsfive4
    with dissolve

    y "Hah..."

    "Yumi lets out a heavy sigh and slouches down against the phone booth she’s leaning on."
    "The glass is too thick to shatter from the pressure of her body against it, but a coffee cup positioned on top of a table falls off due to the phone booth suddenly being pushed backwards."
    "Its contents spill out all over the ground, drowning whatever insects made their home inside while coating the walls in a liquid that will remain unseen for what I imagine will be quite some time."
    "I feel a sudden compulsion to clean it."
    "I don't know why."

    s "..."
    y "..."
    y "You gone yet? Or am I going to open my eyes back up to just more disappointment?"
    s "Aren't you going to go pick up the trash you just knocked over?"

    scene streetsfive2
    with dissolve

    y "The fuck do you think, smartass?"
    y "Do I look like the kinda girl who’s gonna spend her free time mopping up some old ass drink off the inside of a phone booth?"
    y "Shit's probably been there for like a month. Ain't my problem."
    y "You fuckin’ clean it up if it bothers you that much."
    s "It...doesn’t. I was just trying to make a joke, I guess. I knew you weren't going to actually go out of your way to do something kind."

    scene streetsfive3
    with dissolve

    y "You call {i}that{/i} shit a joke? Try a lot fuckin' harder, dude. That wasn't even almost funny."
    s "You say that like you're some kind of comic genius or something."
    y "Maybe I am?"

    scene streetsfive4
    with dissolve

    if bonus == True:
        y "Here's a real joke for ya- What do you call a creepy dude who spends way too much time trying to get in the pants of every [teenager] he sees?"
    else:
        y "Sure. What do you call a teacher who's really bad at crossword puzzles?"

    s "Me."
    y "Wrong, it’s-"

    scene streetsfive5
    with dissolve

    y "Wait, did you really just fucking admit that? Are you insane?"
    s "I'm not admitting to anything. Your {i}jokes{/i} are just extremely predictable."
    y "Jesus Christ, you're fucking disgusting..."
    s "That may be true, but at least you wouldn't have to worry about me trying to get inside of {i}your{/i} pants if there was any merit to that jest."

    scene streetsfive1
    with dissolve

    y "Oh? And why is that? Am I not ‘cute’ enough or some shit?"
    y "You into the {i}girlier{/i} types? The ones who can't beat the living shit out of you?"

    if bonus == True:
        s "No. That's not it."
        s "You’re just not wearing pants."
        y "…"
        s "I can't get inside of them because they're not there."
        y "…"
        s "Because...you're wearing a skirt."
        s "Which technically isn't pants."
        y "…"
        s "There are just...no pants for me to try and get inside."
        y "…"
        s "…"
    else:
        s "No. Because I am actually a crossword puzzle expert."

    scene streetsfive6
    with dissolve

    y "Pfft..."
    y "..."
    s "..."

    scene streetsfive7
    with dissolve

    y "Funny shit."

    if bonus == True:
        s "You know, for a second I thought you might actually start laughing."
        y "As fucking if. Would have to be some sort of...shitty fucking alternate timeline or something for me to laugh at a shitty joke like that."
        s "You did kind of crack a smile, at least. Albeit for only like, three seconds."
    else:
        "I am so funny."

    y "Me? Nah. Didn't happen."
    s "I literally-"
    y "It didn't. Fucking. Happen."
    y "Got it?"
    s "Will you hit me if I say no?"
    y "I will fucking murder you if you say no."
    s "..."

    scene streetsfive4
    with dissolve

    y "So, now that we've reached an agreement-"

    scene streetsfive1
    with dissolve

    y "See ya."
    s "What? Already?"
    y "Yeah. This has already been like fifty times longer than I wanted to talk to you for."
    s "That statement implies that there is a measurable amount of desire you have to actually talk to me."
    y "It implies {i}shit.{/i} Now, get lost."
    s "I don't understand how you can be so rude to the only person who's ever made you smile before."

    scene streetsfive8
    with dissolve

    y "Oh, fuck off! That shit was barely even a smile! {i}Why{/i} would I smile?! "
    y "Your stupid ass {i}joke{/i} wasn’t even funny!"
    s "Really? But I explained it so many times and that makes every joke funnier."
    y "Just fucking drop it, okay?! It’ll never happen again!"
    y "And if anyone ever finds out that {i}you{/i} of all people got me to crack, I will literally never fucking live it down!"

    if bonus == True:
        y "So, again, tell anyone that I even {i}almost{/i} smiled and I swear on everything you love that I will rip your fucking balls off."

    s "Fine, Yumi. This momentous occasion can be our little secret."

    scene streetsfive9
    with dissolve

    y "Ahhhh!!! That somehow makes it sound even fucking worse!"

    if bonus == True:
        y "Just get the hell away from me, creep! Now! Before I...start screaming that you're trying to molest me or some shit!"
        s "There’s not only no one around, but we're both fully clothed and there is no way anyone would believe that."

        scene streetsfive8
        with dissolve

        y "So what?! At least if someone else comes, I won’t have to worry about some fucking tall, wonky-ass looking dickwad pushing me to the ground!"

    s "Okay, fine. I won't say anything."
    s "I wasn't really planning to anyway, but I'll go ahead and confirm that now before you pop a blood vessel trying to summon other people over here."
    s "If you think for a second that I'm not burning that image into my memory, though, you're dead wrong and now I'm just going to try and make you smile ten times more often."

    scene streetsfive9
    with dissolve

    y "AHHHHH!!! I FUCKING HATE YOU!!!"
    s "I know you do. You remind me every five lines of dialogue. Your entire personality is pretty much centered around hating me, isn’t it?"

    scene streetsfive3
    with dissolve

    y "Fuck off. I'm a human being just like everybody else. I've got tons of shit I'm dealin' with."
    y "But it’s not like someone as shitty and as {i}rude{/i} as me has any chance of redeeming herself, right?"
    y "I'm better off just stickin' to how I've always done things since that'll make shit easier for everyone involved."

    if bonus == True:
        s "That’s not true. I actually think you’d be pretty cute if you stopped spitting on cars from the top of an overpass and...threatening to rip my balls off."
    else:
        s "That’s not true. I think you’d be pretty cute if you stopped all of the spitting on cars and beating up old people."

    y "…"

    "Yumi doesn’t respond right away and, instead, focuses her gaze on a few cars off in the distance."
    "She's probably thinking about spitting on them."

    y "I think you're a fucking liar."
    y "But that's not something I'm gonna stand here and talk to you about when I've got other shit that takes priority."
    y "I’m tired..."
    y "I’m gonna get out of here."
    s "Do you want to head back together and-"
    y "Fuck no."
    y "And don't think about following me either."
    s "But-"
    y "Just leave me the fuck alone already."

    scene streetsfive10
    with dissolve

    "As expected, Yumi takes off down the street and aggressively tucks her hands into her skirt-pockets."
    "I watch from afar as she rounds the corner and disappears, heading off to somewhere she can feel alone without the prying gaze of a middle aged man chipping away at her walls."
    "I know that, before long, those chips will be large enough to see through."
    "But for now, I'll have to resign myself to just watching her walk away like this."
    "I'm sure there's plenty more of that in store for the future."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ streets5 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label streets10:
...
```

## Code that triggers this event
File: \game\YumiEvents.rpy
Code:
```python
...
label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump satafternoonmenu
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
    if yumi_love >= 5 and streets5 == False:
        jump streets5
...
```