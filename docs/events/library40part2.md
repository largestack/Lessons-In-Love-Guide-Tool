# Without Running Away
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library40part2&go=Go)


Part of event chain [Shadowplay](./library40.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Futaba: Hall of Mirrors](./futabadorm45.md)

## Event properties
* ID: library40part2
* Group: Futaba
* Triggered by label: library40

## Event code
File: \game\FutabaEvents.rpy
Code:
```python
...
label library40part2:
    if _in_replay:
        play music "justlights.mp3"

    scene futabayumisnow1
    with dissolve2

    "There’s no shade anywhere."
    "Or at least not on the way home, there isn’t."
    "I’m sure there’s shade in some part of the world because...the world is big and whatnot."
    "But, by comparison, my world is rather small."
    "It’s small enough that, if I closed my eyes and didn’t mind wandering into traffic from time to time, I could probably learn to traverse it in complete darkness."
    "Not that I’d want to do that or anything, but I do think it would be nicer at times."
    "I’m sure Futaba would agree as well."
    "If everyone was blind and we all walked around with canes or seeing eye dogs, she’d never have to cope with the fact that her body isn’t what she wants it to be."
    "Think of all of the years in all of the loops where the first look on her face in the morning wasn’t one of disappointment or disgust."
    "And think of all the different iterations of me that have told her not to worry about it."
    "Think of all of the ones that did."
    "Think about me. Think about me. "
    "Think about me."
    "Think about me because it’s easier to resent someone {i}worthy{/i} of resentment than someone who doesn’t believe to be even worthy of themselves."
    "Someone who has harmed absolutely no one, yet feels the weight of the world on her shoulders with each passing moment as if she didn’t already believe she had enough “weight” in the first place."
    "Think of the me’s that told her she wasn’t good enough. Or the her’s that never tried turning things around. Think of how much it must have hurt."
    "Think of how everything hurts. "
    "And that even in this slightly more perfect rendition of a world we’ve been stuck in for {s}God{/s} god knows how long, there is still more pain than we can shovel into our pockets."
    "It tears through the fabric, like an improperly stored pocket knife- slicing our legs open and causing blood to slowly trickle down the insides of our pants."
    "This train of thought makes me think about Noriko."
    "Which leads me into a second train of thought about how I can’t even focus on what’s beside me without my mind wandering off and getting lost."
    "Without running away."
    "I run back."

    s "So...now what?"
    f "What do you mean?"
    s "I mean what do we do now that we’re not at[school]? "
    s "Did you want to get breakfast or something?"
    f "I...had a protein bar this morning."
    s "Oh. Well I guess I’ll just starve then."

    scene futabayumisnow2
    with dissolve

    f "We can still stop somewhere if you’d like. It’s...not like I have anything else to do now that I’m not in the library."
    s "It’s fine. I’m not really that hungry. I just didn’t really know what else to do."
    s "We can go back to your dorm, I guess."
    f "If it’s okay...I think I’d like to stay out here for a little while longer."
    s "Interested in joining the soccer team? We could go see what Miku is up to."

    scene futabayumisnow3
    with dissolve

    f "I think...just the gym is enough for now. "
    f "I should probably wait a little longer before trying to catch up to someone like Miku. "
    f "I’m not really much of a fan of sports in the first place."
    s "That’s fine. I’m not either, to be completely honest."

    scene futabayumisnow4
    with dissolve

    f "Aren’t you the coach of the soccer team, though?"
    s "Yes. But that position sort of came to me on its own and wasn’t something I went out of my way to acquire."
    f "That seems like a pretty serious thing to just...come to you out of nowhere."
    s "Well...wherever there are thighs...there will be me."
    s "It was probably just the universe doing me a favor."

    scene futabayumisnow5
    with dissolve

    f "I’m going to...do everyone a favor and just pretend I never heard that."

    if bonus == True:
        s "No. You {i}did{/i} hear it. I need you to etch this into your memory so you can expand your glossary of sex acts."
        f "I mean...there aren’t really any “sex acts” you can use your thighs for."
        s "Oh, Futaba. You still have so much to learn."

        scene futabayumisnow6
        with dissolve

        f "Wait...is there actually...something like that?"
        s "There is."
        f "But...how does..."
        s "Remember what we did in the nurse’s office? It’s just like that but...with your thighs."
        f "And that feels good?"
        s "I mean, I doubt it would feel good for you."
        f "That just sounds difficult."
        s "It sounds like good exercise to me."

        scene futabayumisnow7
        with dissolve

        f "Oh. So that’s where we’re going with this."
        s "I’m helping you become a better person."
        f "No. You’re just turned on."
        s "That’s a side effect. This is really just to make you happier when you wake up in the morning."
        f "There are a lot of easier ways to make me happier in the morning, Sensei."
        s "And how many of them involve my penis?"

        scene futabayumisnow8
        with dissolve

        f "Maybe like...three?"
        s "Can you name them?"
        f "Not really."
        s "Well then I guess you’ll just have to live your life in misery as I have no idea what else I can do for you."
        f "How many times do I have to tell you that you don’t have to do anything for me? Just let me handle this part of my life on my own."
        s "This makes it sound like you have a portable version of my penis."

        scene futabayumisnow9
        with dissolve

        f "Not everything is about your penis, Sensei!"
        s "You take that back right this instant, [young]lady."
        f "Are you my dad now?!"
        s "Do you normally talk about penises with your dad?"
    else:
        s "I'm sorry. That was uncalled for. I will do my best to refrain from bringing up legs for the indefinite future."

    scene futabayumisnow10
    with dissolve

    f "Hah...I should have stayed in the library..."
    s "Come to think of it, I’m pretty sure I overheard you saying something about your parents coming to visit when you were on the phone earlier."

    scene futabayumisnow4
    with dissolve

    f "Were you really listening for that long?"
    s "I was. And, sorry for asking but, is something like that even possible?"

    scene futabayumisnow11
    with dissolve

    f "I don’t really know...But it seems like that’s exactly the issue."
    f "They were under the impression that they’d be able to get a pass that would allow them to return since they were away on work, but it seems the process isn’t as easy as it sounds."
    s "This city gets more and more confusing with each passing day."
    f "You think so? It seems mostly normal to me."
    f "But...I’ve also never really lived anywhere else for more than a month or two, so I’m probably not the best judge of that."
    s "I just don’t get what the big deal is. "
    s "Like, why block off the city if-"

    scene futabayumisnow12
    with dissolve

    f "Wait...hold on a second."
    s "What’s wrong?"
    f "There’s...someone leaning up against the wall."
    s "Were we talking about something they shouldn’t be listening to?"
    f "No...it’s just..."
    f "Look."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene futabayumisnow13
    with dissolve

    "Futaba and I find Yumi with her back pressed against some sort of anime billboard and I think for a second about how she would look in cosplay."
    "Of course, I realize seconds later that I should probably be thinking about more important things."
    "Like how to explain why I’m out walking around with Futaba at this time of the morning."
    "Then again, I’ve also spent time in the city with Yumi and there’s nothing going on between {i}us{/i} so..."

    if bonus == True:
        "Well, except for that one thing."
        "But yeah, you get what I mean."

    f "Umm...G...Good morning, Yumi..."
    y "Don’t have to stop and fuckin’ greet me, you know. Not really in the mood to talk."
    s "Are you ever in the mood to talk?"
    y "Nope. Now get the fuck away from me. Too early for this shit."
    f "Umm...Sensei and I..."
    y "Don’t fucking care. You ain’t holdin’ hands or anything so I ain’t got a reason to get all pissed."
    y "Just take the fucking hint and keep walking. I’m not starting anything today."
    s "Are you okay?"

    scene futabayumisnow14
    with dissolve

    y "The fuck do you care? I am making this as easy as fuckin’ possible for you! Just leave me alone!"
    s "I just-"
    y "Again, don’t care! "
    y "I’m doin’ that whole “Ain’t got nothin’ nice to say, so don’t say anything” bit and you’re tryin’ to fuck me up!"
    y "Just go hang out or whatever! I’m stayin’ out of your way!"
    s "I’m shocked."
    y "Why?!"
    s "This just...might be the nicest thing I’ve ever seen you do."

    scene futabayumisnow15
    with dissolve

    if bonus == True:
        y "Suck my dick, you [niece]-fucking shitbag. "
    else:
        y "(Airplane noises)"

    f "That’s-"
    s "It’s fine. Baby steps, Futaba. Baby steps."
    s "She’ll get there."
    f "R-Right..."
    s "…"
    y "…"

    "The three of us stand there for a moment, causing the air to get noticeably less comfortable."
    "I start walking away to end the situation and get on with the day, but Futaba keeps her feet planted."
    "I’m not sure what it is she wants to accomplish by doing so, but-"

    f "Yumi..."
    f "Did...did you want to...hang out with us, maybe?"

    "Oh, okay. So that’s what’s going on here."
    "I stop myself from leaving and turn to see how the rest of this...exchange goes."

    scene futabayumisnow16
    with dissolve

    y "No. Get the fuck away from me."
    f "Okay, but...I think it...might be nice actually getting to spend time with you for once..."
    y "Why? All I do is make fun of you and shit. You some kind of masochist?"
    f "No, but...I just...have a hard time accepting that’s the real you."
    y "No idea what the fuck you’re talkin’ about, but the “real me” wants to be left alone. Now beat it before I punch your fucking teeth in."

    scene futabayumisnow17
    with dissolve

    f "Hehehe..."
    y "...The fuck you laughing at?"
    y "If this is some kind of...weird fucking test or something-"
    f "No no no...it’s nothing like that."
    f "I was just thinking that..."
    f "You look a lot like your mom when you start...being intimidating like that..."

    stop music fadeout 5.0
    scene futabayumisnow18
    with dissolve2

    "Uh-oh."
    "Bad move, Futaba."

    y "The fuck did you just say to me?"
    f "I...wait..."
    f "What did I do?"
    y "What the fuck did you just say to me? Say it again."
    y "I want to hear it."

    scene futabayumisnow19
    with dissolve

    f "I...I just thought..."
    s "Futaba, come on. Yumi’s not in the mood to talk right now."
    y "Oh no. I’m in the mood to talk now. I’d {i}love{/i} to talk, actually. "
    y "So go on. Tell me again."
    y "Who did I look like just now?"
    f "You..."
    f "You looked kind of like...your mom..."

    play sound "static.mp3"
    scene futabayumisnow20 with flash
    stop sound
    play music "thingsthathurt.mp3"

    "Yumi grabs Futaba by the shoulders and spins her around, throwing her up against the billboard that she’d been leaning on herself just seconds ago."
    "She rears back her fist and punches the wall, which allows me to breathe a sigh of relief on the way over as I thought she was about to kill a classmate."

    y "Listen here you fat, fucking bitch. I am {i}nothing{/i} like my mother. Nothing."
    y "Got it?"
    f "I...Yumi-"

    scene futabayumisnow21
    with dissolve

    y "Got it?!"
    f "Yes! I’m sorry!"
    y "You been pokin’ around for dirt on me or some shit?! So tired of me picking on you that you have to get involved in my fucking personal life?!"
    f "No! I just...met her and..."
    y "I don’t care what your fucking excuse is! You stay out of my shit and I’ll stay out of yours! "
    y "I told you to just fucking walk away, didn’t I?! I was gonna leave you alone!"
    y "But you must have seen that and decided, “Oh! Yumi looks vulnerable today! Time to hit her where it hurts!”"
    y "Is that right?! Is that what you're doing?!"
    y "Fuck you! Fuck you fuck you fuck you!"
    f "I...really didn’t mean to..."

    scene futabayumisnow22
    with dissolve

    s "Come on. That’s enough."
    y "No! It’s not fucking enough! Do you have any idea who that “mother” of mine actually is?!"
    f "I...didn’t even know it was your mom until a little while ago..."
    y "Of course you didn’t! Just a tiny, little mistake from a big, fucking girl!"
    y "Doesn’t even matter, right?! "
    y "Right?!"
    s "Yumi, let go. Futaba and I were leaving."

    scene futabayumisnow23
    with dissolve

    y "Yeah. Of {i}fucking{/i} course you were."
    y "You gonna go have a good time with the teacher, Futaba?"
    y "Gonna go feel better about yourself while he sits there and tells you your size doesn’t matter or some shit?"
    y "Gonna stuff your fucking face with junk food while looking down on people like me? People who never even got to know their parents?!"

    scene futabayumisnow24
    with dissolve

    y "No! Don’t close your fucking eyes, cunt!"
    y "Look at me and tell me again how acting intimidating makes me look like a fucking junkie who can’t even be bothered to take care of a little girl!"
    y "I should fucking kill you right here!"
    s "Yumi-"
    y "Never talk about my mother again! Got it?!"
    f "Yes! Yes! I won’t!"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene futabayumisnow25
    with dissolve

    y "Do you have something to do with this?"
    s "Yes."
    s "It’s my fault. Futaba doesn’t know anything about your relationship with your mother."
    y "Well she certainly knows something now."
    s "It’s all one big misunderstanding."
    y "Was it a misunderstanding when you told me you wouldn’t get involved anymore? "
    y "Am I too fucking dumb to understand what that means, Sensei?"
    s "Yumi-"
    y "I don’t know what the {i}fuck{/i} you are trying to do to me, but {i}stop{/i} getting involved with my family."
    y "Leave me alone. "
    y "And if you’re going to drag other people into it, at least drag in someone who will actually put up a fucking fight so I don’t feel like I’m about to strangle a defenseless little kid."
    s "I’m sorry. It was an accident."
    y "Yeah, and so was I. But I’m fucking here now. And I don’t need my teacher and his walking fucking morale booster to show up out of thin air and remind me of that."
    s "Yumi..."
    y "Just...leave me the fuck alone."

    scene black
    with dissolve

    "………"
    "……"
    "…"


    scene futabayumisnow26
    with dissolve

    s "Are you okay?"
    f "Yeah...but..."
    s "That was just a really bad coincidence. "
    s "I didn’t expect to run into Yumi without warning you to never bring up that...{i}subject{/i} around her."
    f "That...was a pretty important detail to leave out..."
    f "If you weren’t here, I..."
    s "If I wasn’t here, you never would have learned about Yumi’s mother in the first place."
    s "So let’s just call it a day and go back to the dorm. "
    s "I’m sure Yumi wants to forget this even more than the two of us do, so just don’t bring it up again and everything should be okay."
    f "You..."

    scene futabayumisnow27
    with dissolve

    f "You two must be...getting pretty close if you know things about Yumi’s family..."
    f "I thought Chika was the only one who...knew anything about that..."
    s "“Close” definitely isn’t the right word, but I don’t think now is the best time to really deep-dive into such a convoluted relationship."
    f "Yeah...probably not..."
    f "I’m sorry if I managed to...make it even more convoluted, though."
    f "She’s said a lot of mean things to me before, but...I’ve never really seen her get like that."
    s "And, if everything plays out the way it should, you never will again."
    s "Let’s go back for now, though. I’m sorry I didn’t warn you ahead of time."

    scene futabayumisnow28
    with dissolve

    f "It’s okay..."
    f "This is just what I get for...trying to be nice to someone who doesn’t want anything to do with me."

    scene black
    with dissolve2

    "Futaba and I head back to the dorm in almost complete silence."
    "We try making conversation about a few random things along the way, but nothing really sticks. "
    "The air is too uncomfortable and awkward after what we just experienced."
    "It’s strange how quickly things can fall apart just by being in the wrong place at the wrong time."
    "But it’s even crazier that, for some people, every place and every time is always wrong."
    "And there’s nothing we can really do about it."
    "We’ll just keep existing and keep hoping that tomorrow will be more convenient than today."
    "Sometimes it will be."
    "Other times, it would probably be better to not exist at all."

    $ renpy.end_replay()
    $ library40part2 = True
    $ futaba_love += 1
    stop music fadeout 6.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label futabanew1:
...
```

## Code that triggers this event
File: \game\FutabaEvents.rpy
Code:
```python
...
"There isn’t."
    "I am completely secure in everything."
    "My feet are planted so firmly to the ground that they would not even move in the event of an earthquake."
    "And if an earthquake were to come, and the ground beneath my legs would crack in cartoonish fashion, I would stare directly at it as my appendages are stretched so far apart that I'm torn in half."
    "There are people in this world who want to become better versions of themselves, and there are people who don’t."
    "But whatever those people decide to do is completely up to them."
    "My words don’t matter to Futaba, just as hers don’t matter to me."
    "We’ll keep existing and keep on fighting our own fights regardless of how much unnecessary support we pump into one another."

    if bonus == True:
        "Thankfully, support isn’t the only thing I have the privilege of pumping into her."

    s "Nah. I prefer to keep my problems to myself."
    f "Even after I just opened up about my biggest problem of all?"
    s "Is that really your biggest problem, Futaba?"

    scene futabaphonemom18
    with dissolve

    f "I...I think so?"
    s "You’re not worried about how each and every day we move one step closer to death? Or how the world is becoming less and less habitable with each passing moment?"
    f "I...don’t think I’m...supposed to start thinking about those things until after I graduate..."
    s "Since when do you do what you’re supposed to do? Stop wasting your time and fear them now."
    f "Sensei...you’ve given me a lot of...strange motivational speeches...but this one is just-"
    s "A joke."
    s "Kind of."
    s "Let’s just say I’m only half serious."
    s "If this bulimia issue is your biggest problem, I’m thankful you shared it with me."
    s "I didn’t know and I’m sorry you had to go through something like that."
    s "But there’s nothing I could share with you about myself that would make me feel any better or worse than I do right now."
    s "And there’s not much I know anyway."
    f "What do you mean by that?"
    s "I mean that this world is incredibly complicated."
    s "I can’t risk taking my feet off the ground or it will all just float away."

    if bonus == True:
        scene futabaphonemom19
        with dissolve

        f "I wouldn’t mind holding you down."
        s "I wouldn’t mind holding {i}you{/i} down either, but you want to be more comfortable with yourself first."
        f "Ha ha ha. It’s not like your...thing would fit inside of me anyway."
        s "We’ll never know unless we try."
        f "I can’t believe I agreed to skip out on the library to listen to my teacher make sex jokes all morning."
        s "It’s better than having the sex jokes happen {i}inside{/i} of the library, isn’t it?"
        f "Not...by much."

    "The shadows of the branches of a tree slaughtered by the harsh winter climate spread out and climb the walls of the[school] building, making it resemble some sort of spider web."
    "Shadows seem to be a recurring theme today."
    "Whether it be the shadows of the two of us or of the dying tree, it’s as evident as ever that there is a darker side to everything."
    "Futaba’s dark side managed to emerge today."
    "But instead of ignoring it like a normal person would, she parked it beside mine and reiterated that there is still joy to be found inside of darkness itself."
    "And that the darkest parts of me, which she will likely never come to know, somehow manage to help her feel less lonely."
    "And here, all I wish is to see a shadow as anything more than a shadow."
    "To see anything at all as more than exactly what it is."
    "To live without conflict because life itself is conflict enough."
    "But none of that is possible. Especially not with someone like this beside me."
    "She will follow me into the flames of hell and, instead of pushing her away, I will grab her wrist and pull her into them so I don’t have to die alone."
    "But she is weak and will die before me."
    "So I will die alone anyway."
    "Today is going to be a bad day."

    s "Okay, let’s go somewhere else."
    f "Yeah...I was wondering when you were going to say that."
    f "I like the[school] and everything, but...it’s not exactly fun just hanging out on the side of it. Even if it’s you I’m hanging out with."
    s "Yes, please continue to say nice things about me. It will soften the blow the next time you don’t let me watch you exercise."
    f "Oh, stop. You spent most of your energy on that...scary blonde woman anyway."
    s "Scary blonde- Oh, you mean Yumi’s mom."
    f "Yeah, Yumi’s-"

    scene futabaphonemom20
    with dissolve

    f "Wait, what? Huh?"
    f "That..."
    f "That woman was..."
    s "Anyway, time to go somewhere else."

    scene black
    with dissolve

    s "Kumon-mi awaits, Futaba."
    f "That...was Yumi’s mom?!"
    f "Wait! Sensei!"

    "I start walking away from Futaba, realizing that I have already said too much, and begin to head down the same path I take home every day."
    "I don’t have a specific destination in mind but, if I had to choose-"
    "I’d probably pick somewhere with a lot of shade."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ library40 = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump library40part2
...
```