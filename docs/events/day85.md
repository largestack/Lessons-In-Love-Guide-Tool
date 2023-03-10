# Contractions (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 85

* Event [I See You](./streets10.md) (Yumi) is completed)



## Next events

* [Main: A Different View](./day121.md)
* [Main: Rumors](./day138.md)

## Event properties

* Id: day85
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day85

## Official wiki page

[Contractions](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day85&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day85:
    scene newyumiroof1
    with dissolve
    play music "10c.mp3"

    "School has ended for the day and I’m finally on my way home."
    "With another seemingly endless round of standardized tests around the corner and most of the girls off studying, my counseling hours have been cut back."
    "So, here I am with an abundance of free time and absolutely nothing to do with it."
    "And, if today is anything like most days before it, I imagine this is the part where someone walks up to me and starts a conversation before I’m able to decide anything for myself."

    scene newyumiroof2
    with dissolve

    y "Hey, douche monkey."
    s "Yumi, that’s not even a thing."
    y "Well, it is now."
    s "Great. Did you stop me just to say that?"

    scene newyumiroof3
    with dissolve

    y "Well...no."

    "Yumi goes quiet for a moment- which is a thing I don't normally get to think."
    "Her eyes scan the halls for several seconds before she finds it in herself to swallow her pride and open her mouth again, this time making my day even weirder than it has already become over the last ten seconds."

    y "I...actually need a favor."
    s "From me? That’s new."

    scene newyumiroof4
    with dissolve

    y "Trust me, I’m no happier about this than you are."
    y "I’ve been dreading having to do this all day...but at this rate, there’s no fuckin’ way I’m going to pass even {i}half{/i} the subjects on this stupid test thing."
    s "So...you want me to help you study?"

    scene newyumiroof5
    with dissolve

    y "D-Don’t say it out loud, you fucking dick! Someone might hear you!"
    s "You’re...afraid of someone hearing that you’re going to study?"
    y "I’m afraid of someone hearing me ask you for help!"

    if yumidorm10 == True:
        s "I’ve told you before it’s fine to ask for help. Don’t worry about it."
        s "I'm just a little surprised because this is the first time you've actually...you know, done that."

    else:
        s "Yeah, now that you say that, I think this is the first time you’ve ever
        asked me for...well, anything."

    scene newyumiroof6
    with dissolve

    y "And hopefully the last."
    y "This is the lowest point of my life and I’m only doing it because I have no other options."

    "I hate to think what’s in store for Yumi’s future if coming to {i}me{/i} is her best option. I’m sure Chika would be able to help her just fine."
    "And even though I've never really seen them speak before, I doubt Makoto would say no to someone asking for her help concerning all things education."

    s "I guess I'll just...go unlock the classroom then."

    scene newyumiroof2
    with dissolve

    y "Uhh...no. Is it cool if we go to the roof instead?"
    s "The roof?"
    y "It’s just...somebody might have left something in the classroom and if they come back for it, they might think I asked you for help or something..."
    s "But...you {i}did{/i} ask me for-"

    scene newyumiroof5
    with dissolve

    y "I fucking know! Stop reminding me! Now, are you going to come with me to the roof or not?!"
    s "How are we even going to get onto the roof? I don’t have a key."

    scene newyumiroof7
    with dissolve

    y "You’re the teacher and you don’t have a key? The fuck is that about?"
    s "Do they normally give every teacher a key to the roof? Because that seems like something I should have been informed of."

    scene newyumiroof3
    with dissolve

    y "Well...whatever. I’ve got one."
    s "Why?..."
    y "Because I’m a fucking delinquent, remember?"
    y "Just assume I stole it or some shit...I don’t care. Point is, I’ve got the key and I’m going to the roof, so if you want to actually do your job for once, follow me."

    scene newyumiroof1
    with dissolve

    "Yumi angrily storms up the stairs toward the roof and leaves me in the dust."
    "I take a quick look around to see if anyone has been watching us and, once I confirm that we’re in the clear, I follow her up..."

    scene black
    with dissolve2

    "………"
    "……"
    play sound "dooropen.mp3"
    "…"

    scene yumiroof1
    with dissolve

    "Yumi takes a seat on a nearby bench, removing a couple of books she had tucked inside of her blazer."
    "She lays them out in front of her and takes up a slightly messy seiza position in complete disregard for her skirt as she waits for me to join."

    y "…"
    s "…"
    y "I’m already having regrets about this."
    s "I haven’t even done anything."

    scene yumiroof2
    with dissolve

    y "Well, whatever. Just fucking teach me something already."
    s "Okay...What do you need help with, exactly?"
    y "Uh...Well, what’s going to be on the test?"
    s "You don’t even know that?"

    scene yumiroof3
    with dissolve

    y "How the hell {i}would{/i} I know?! I barely even come here!"
    s "Good point..."
    s "Then...I guess we can start with English?"

    scene yumiroof2
    with dissolve

    y "Sure. Whatever."

    "I figure I might as well coach Yumi on the one of the few subjects I’m relatively competent in."
    "It’s kind of hard when she doesn’t tell me what areas she doesn’t understand, though."

    y "Why the fuck do we need to learn English anyway? I’m not going to America any time soon."
    s "I don’t think anyone is going anywhere any time soon. We’re kind of stuck here."
    y "Exactly. They should just take English off the fucking curriculum or whatever it’s called then."
    s "I mean, basic English isn’t particularly hard once you get the gist of it. At least it makes a lot more sense than algebra."

    scene yumiroof4
    with dissolve

    y "For real, though. Like...all that shit about slopes that we had to learn a few weeks ago- the fuck even was that?"
    y "What do slopes have to do with me? We should be learning about, like...taxes or other useful shit that we can actually do something with."
    s "Right. And speaking of things you can do something with...English."

    scene yumiroof5
    with dissolve

    y "Shit. Yeah. My bad."
    y "Do your thing."

    "Instead of drawing attention to Yumi’s unexpected obedience, I decide to actually start doing the job I am paid to do."
    "She sits there silently, occasionally scribbling down notes in her notebook as I touch on ideas and topics she hasn’t heard before."
    "Her handwriting is sloppy, but it’s cute in its own way."

    scene yumiroof6
    with dissolve

    y "Wait...So what’s with all the different ways to spell “there?” I don’t get it."
    y "What’s wrong with just using the same one?"
    s "Think of it like kanji and how most of them can be read in a number of ways."
    s "Words like “there” and “your” change completely depending on the context of the sentence they're used in."
    s "What's even weirder is that there are situations where you sort of squish two words together to make alternate forms of those words- like “they're” and “you're.”"
    y "I get that. But is there, like...a trick to remembering them or something?"
    s "Uhh...probably? But not one that I know of."

    scene yumiroof7
    with dissolve

    y "What a stupid fucking language."
    s "Yeah, it’s pretty ridiculous most of the time. But if you ever want to get out of here, it’s probably best to at least learn a little bit."

    scene yumiroof6
    with dissolve

    y "You mean like, when they open the borders back up or some shit?"
    s "That’s right. You don’t intend to stay in Kumon-mi forever, do you?"

    scene yumiroof8
    with fade

    y "Huh...That’s not really something I’ve ever thought about before."
    s "Really? Why not?"
    y "I don’t know. It just...hasn’t occurred to me, I guess."

    scene yumiroof9
    with dissolve

    y "I’ve never left this city. Don’t even know what it’s like anywhere else."
    y "I don’t know if you come from anywhere different or...if you've ever gone anywhere else...but is it even worth it to leave?"
    s "Depends on what you’re looking for, I guess."
    y "And if we don’t know what we’re looking for? What then?"

    scene yumiroof10
    with dissolve

    y "Do we just, like...walk around and search for jobs or some shit? That sounds boring as fuck."
    s "I mean, it definitely sounds boring when you put it that way."

    "To be fair, I’m on Yumi’s side here."
    "Life is boring."
    "Well, old life was boring."
    "Or at least I think it was."
    "I'm sure I sound like a broken record, but I can't really remember."
    "But...this life?"
    "This one seems fine."
    "For now, at least."
    "Things can go wrong at any moment, though."
    "This is something I’ve learned."
    "One minute, you can be on top of the world-"
    "Then the next, your dog gets hit by a car. Or your grandfather goes into cardiac arrest and dies on the way to the hospital."
    "This world is filled with extremely specific yet entirely spontaneous tragedies like that."
    "But this isn’t something I need to teach Yumi."
    "This is something she’ll need to learn on her own."

    y "Uhh...You okay? You’re like, starin’ through me or some shit. It’s creepy."
    s "I’m fine. I was just thinking about life."

    scene yumiroof11
    with dissolve

    y "Well...don’t be getting all mushy about it. It’s my fault for askin’ somethin’ like that anyway."
    y "I couldn’t care less about leaving this place, to be honest."
    y "I don’t really care about anything. I just wanna eat good food, sleep late, and live forever."
    s "Well, one of those is clearly not possible, but I wish you the best of luck."

    scene yumiroof12
    with dissolve

    y "So, we done here?"
    s "I don’t know. You tell me."
    s "You said you needed help with everything but we’ve really only gone over English so far."
    y "Well, what else is on the stupid test thing? It can’t be more than like...English, Japanese, and math...right?"
    s "..."
    y "..."

    "I think to myself for a moment, searching deep in the back of my mind for any information pertaining to the next round of standardized tests."
    "I wind up with absolutely nothing."
    "Uh-oh."

    s "I...uhh..."
    y "..."
    s "..."
    y "You don't even fucking know, do you?"
    s "I don't."

    scene yumiroof13
    with dissolve

    y "Isn’t this your job? How the fuck do you expect to be a teacher if you don’t even know what you’re supposed to be teaching?"
    s "That’s a good question, Yumi."
    s "I don’t have an answer for it, but it’s a good question nonetheless."

    scene yumiroof14
    with dissolve

    y "Well, what the fuck am I supposed to do if we get to a part I don’t know?! Do you have, like...an answer sheet or something I could borrow?"
    s "…"
    y "Hello?! Anything going on in that disturbingly smooth brain of yours?!"
    s "Let’s just..."
    s "Let's see what else I can help you with..."

    scene black
    with dissolve2

    "Yumi and I skim through a few of her books and I do my best to glaze over every subject we come across."
    "Thankfully, Chika was kind enough to include a list of the subjects on the test in Yumi’s notebook without her knowledge- so at least we had that to go off of."
    "It wound up getting dark not much later."
    "I offered to walk Yumi back to the dorms but she refused."
    "In the end, I walked home alone while Ami yelled at me over the phone for not informing her of how late I’d be out."
    "So it goes, I guess."
    "..."
    "I wonder how much of today's lesson Yumi will remember?"
    "..."
    "I wonder if she really will be stuck here forever."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ day85 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label day89:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
...
```