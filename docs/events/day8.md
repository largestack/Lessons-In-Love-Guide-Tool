# Delinquent (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 8



## Next events

None

## Event properties

* Id: day8
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day8

## Official wiki page

[Delinquent](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day8&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day8:
    scene yumioffice0
    with fade
    play music "phantomthief.mp3"

    "Earlier today, I decided to be a responsible teacher and asked Yumi to come to my office after school."
    "I have no idea whether or not she actually {i}will,{/i} but I figure that something like this is the least I can do to prevent her from...continuing to be an asshole, I guess?"
    "I'm still in the dark about what happened during gym class the other day, but I know that whatever it was seemed to really get to Futaba."
    "Worst case scenario, I could always give Yumi a formal detention or something like that, but...I'm pretty sure that would require me staying later as well."
    "And despite the seemingly endless supply of cute girls in this school, I still think I'd prefer to spend my time here {i}outside{/i} of this place..."

    play sound "dooropen.mp3"
    scene yumioffice1
    with dissolve

    y "I'm here. The fuck do you want?"
    s "You know you’re supposed to knock, right?"

    scene yumioffice2
    with dissolve

    y "And you know you’re lucky I even showed up for whatever this bullshit is, {i}right?{/i}"
    y "So why don't you save {i}both{/i} of us the time and just fucking get to it already? What do I have to do today?"
    s "Why do you have to be so hostile all the time? I didn't call you here for the sole purpose of pissing you off, you know."
    y "Yeah, no fucking shit you didn't."
    s "You know you can talk to me if something is wrong, right? You don't have to just take it out on everyone else."

    scene yumioffice3
    with dissolve

    y "Is this a fucking joke? Did you seriously just say that to me?"
    s "I...think so?"
    y "You think {i}I,{/i} Yumi Yamaguchi- the girl you fuck with more than {i}anybody,{/i} am going to just open up to you because you said it's {i}okay?{/i}"
    y "Suck my fucking dick, dude. No."
    y "Ain't a chance in hell that shit is gonna happen."

    "Yeah, that's more or less the response I expected."
    "She can't keep me in the dark forever, though...can she?"

    scene yumioffice3r
    with dissolve

    y "Hah...not sure where this sudden change of heart's comin' from or if this is just another one of your backwards-ass discipline tactics, but..."

    scene yumioffice4
    with dissolve

    y "Please, kindly fuck off."
    y "You hate me, I hate you. That’s how this shit goes. That's how this shit stays."
    y "If you want to keep me after for another fucking {i}detention,{/i} just say it. I ain't got time for you to talk in circles and shit."
    y "Just say it and I'll be on my way. Every second I spend with you in here brings me one step closer to puking all over your shitty carpet."

    "Wow, Yumi...might hate me even more than I thought she did?"
    "Just what was her impression of the last {i}me{/i} like?"

    s "I'm not going to give you detention, Yumi. I was thinking that maybe we could try something else."
    y "Something like {i}what?{/i} Because God only knows what kinda shit somebody like {i}you{/i} might have in mind."
    s "To be honest, I don't really have {i}anything{/i} in mind."

    "Nothing that I can seriously ask her to do, at least."

    if bonus == True:
        y "Oh, really? So you're {i}not{/i} thinking of some crazy perverted shit right now?"
        s "..."
        y "You are fucking pathetic."
    else:
        y "You’re not thinking of making me try to juggle and then laughing at me when I can't do it again, are you?"
        s "Woah, is that the secret truth about what happened in this office that will be alluded to for the next several years?"
        s "Who could have envisioned it would be something so silly?"

    s "Listen, the fact of the matter is that I can’t let you humiliate and berate the other girls whenever you want."

    scene yumioffice5
    with dissolve

    y "I wasn’t fuckin’ {i}'berating'{/i} anyone! Is this about that shit in gym yesterday?"
    y "What did that fat, fucking bitch say to you? Because I've got no problem marching over to her stupid ass dorky club and beating the living shit out of her right fucking now."
    s "See, that's exactly what I'm talking about. {i}That{/i} is berating someone."
    y "Don't expect me to know fuckin' stupid ass words like that, dick!"
    s "Yumi, what did Futaba ever do to you? Why do you have to treat her like this even when she {i}isn't{/i} around to hear it?"

    scene yumioffice6
    with dissolve

    y "Fuck if I know. She’s probably planning on stealing my lunch or some shit."

    scene yumioffice5
    with dissolve

    y "And, wait! Why the hell are you even on her side?!"

    if bonus == True:
        y "You into that BBW shit all of a sudden? You bein' nice to her just so you can fuck her and fulfill another creepy ass fetish of yours? "
        s "If I was, would it even make a difference?"
    else:
        y "Did she promise to give you a pack of gum or something?"
        s "Jesus, you have a problem with gum as well? Who hurt you?"
        y "My mom! But she doesn't show up until later!"
        s "Regardless, I like gum and I don't care what you think."

    scene yumioffice7
    with dissolve

    y "Yes! A fucking disgusting difference!"
    y "You're seriously attracted to {i}that?{/i} She's like what would happen if a fuckin' beached whale spent the night in a perfume factory and then fucked all the workers."
    y "You can't be fuckin' serious right now!"
    s "You know, if you're creative enough to come up with metaphors like that, you might actually have some promise as a writer one day."

    scene yumioffice8
    with dissolve

    y "Oh, fan-fucking-tastic. Here comes the part where you compliment {i}me{/i} because your fetish isn't {i}just{/i} overweight teenagers, it is literally {i}all{/i} of them."
    s "For someone who apparently hates me, you sure seem to care a lot about who I'm attracted to."
    y "I wouldn't care as much if I didn't have to see you every fuckin' day."
    s "I mean...you don't. Not as much as everyone else, at least."
    y "Gee, I wonder why."

    if bonus == False:
        "Wow. Yumi must really hate gum."

    scene yumioffice4
    with dissolve

    y "Listen, I'll stop talkin' shit about all your creepy ass fetishes so long as you promise to keep me out of 'em. Got it?"
    y "I’ve got shit I need to do and things I need to take care of."

    if bonus == True:
        y "And I can guarantee you that the {i}last{/i} thing I fuckin’ need is some cradle-robber breathing down my neck with his tiny little dick in his hand."
        s "And now you're berating my penis. Where does it end, Yumi? Where does it end?"
    else:
        y "Last thing I fuckin’ need is some gum liker talkin' about gum and shit."
        s "I see, I see."

        "I remove a handful of green apple Big League Chew from a tiny pouch and try to stealthily chew it without being detected."

    scene yumioffice9
    with dissolve

    y "It ends right fucking here!"

    if bonus == False:
        "I fail."

    y "You are fucking hopeless! And you are fucking disgusting!"

    if bonus == True:
        y "I swear, it's like you expect us all to just throw ourselves at you because you’re some sort of “man in power” or something!"
        y "Fuck that! No! I still can’t believe this place even hired someone like you!"

        "To be fair, they kind of didn’t..."

    s "Yumi..."

    scene yumioffice10
    with dissolve

    y "What? All out of shit to say? That's new."

    if bonus == True:
        s "No, I just...can’t really figure out how I’m supposed to talk to you."
        y "Yeah, well, that’s probably because you’re {i}not{/i} supposed to talk to me."
    else:
        s "Nn. Ma mouf isjuss fll."

    y "I hate this fucking[school]. I hate 99%% of the fucking girls in it. And I hate you, more than both of those other things combined."

    if bonus == True:
        y "And I ain't gonna stop making fun of Futaba just because you're trying to fuck her. "
        s "I don't have anything to do with why you should stop making fun of Futaba. You should stop making fun of Futaba because she hasn’t done anything wrong."
    else:
        s "Stp bng somean Ymi."

    scene yumioffice9
    with dissolve

    if bonus == True:
        y "You didn't even fucking deny that you’re trying to fuck her! You just deflected!"
        y "You’re lucky I’m not calling the fucking cops!"
        s "You do know that if you keep this up, you're just going to keep winding up in here, right?"

        scene yumioffice10r
        with dissolve

        y "..."
        s "You obviously don't want to be here since you have so much {i}shit to do,{/i} so just try and be less of a dick and you'll have more of that time to yourself and less of it hanging around me."
        y "Good, cause there are very few things in life that I hate more than being around you."
        s "I'm sure there are."
        y "So...am I free to go now or what?"

        "I probably shouldn’t let her leave just yet, but I honestly have no idea what else I can do at this point."
        "People like this are impossible to help because they don't want to {i}be{/i} helped."
        "Which, in turn, just makes everyone else suffer."
        "What I did here today won't help Futaba at all. It won't help {i}anyone{/i} at all. It was nothing more than a waste of time."
        "But..."
        "At least it allowed Yumi to vent a little. And, as a temporary optimist, I'm going to hope that prevents her from hurting anyone else for at least a day or two."
    else:
        y "Swallow your fucking gum, already!"
        s "*Gulp*"
        s "Ugh, why did I listen to you? That will stay in my digestive tract for years."
        y "Can I leave now?!"

    s "Yeah..."
    s "You can go."
    y "Cool. Bye."

    scene yumioffice0
    with dissolve
    play sound "dooropen.mp3"

    s "..."

    "And just like that, Yumi is gone."
    "It’s hard to believe that in a class as obedient and...{i}excitable{/i} as mine that there’s an outlier like her."
    "People don't become that way overnight."

    s "..."

    "Something must have happened to her."

    scene black
    with dissolve2

    "I leave my office and lock the door."
    "Before I know it, I’m on my way home."

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ day8 = True

    jump afterschoolevent

label day12:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
...
```