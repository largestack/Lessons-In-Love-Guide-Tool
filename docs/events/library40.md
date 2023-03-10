# Shadowplay (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 40

* Event [Skin](./futabadorm40.md) (Futaba) is completed)

* Event [Abyss](./yumicallnight35.md) (Yumi) is completed)

* Event [Clouds](./kaoridate15p3.md) (Kaori) is completed)



## Next events

None

## Event properties

* Id: library40
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library
* Triggered by path: library->library40

## Official wiki page

[Shadowplay](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library40&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library40:
    scene futabaphonemom1
    with dissolve2
    play music "justlights.mp3"

    "The morning starts off the same as any other."
    "I get out of bed."
    "I get dressed."
    "I leave the house."
    "And I decide to waste my day away with someone who did not ask for me, but will receive me nonetheless."
    "Someone who, just recently, made a minor decision to keep me at arm’s length in favor of temporary comfort, something I simultaneously admire and abhor."
    "I admire it because it shows that Futaba is becoming her own person."
    "That Kumon-mi is a giant eggshell and she’s finally starting to pip her way out of it."
    "But I abhor it because she is supposed to be imprinted on me."

    if bonus == True:
        "And also because I wanted to see those giant “assets” of hers in action as she ran on the treadmill."

    "Combine that with the fact that I’ve been standing here for roughly five minutes now without being noticed and..."
    "Yeah. Forgive me if I wind up harboring some unwarranted, internal resentment for at least a day or two."
    "Basically, everyone is free to do as they want. But everyone else is free to react to those decisions however {i}they{/i} want."
    "Am I making a bigger deal out of this than I should be considering it was just one thing that happened one time? "
    "Yes. Absolutely. There is no question about it."

    if bonus == True:
        "But if you think that is irrational, I implore you to reconsider how much I enjoy the female body and that this is nothing short of a traumatic experience for me."
        "Oh well, though."
        "I’ll just have her take her clothes off in private whenever she’s off the phone."
    else:
        "And so I will do my best to become a better person so this does not happen again in the future."

    f "...Yeah."
    f "No, I’m doing okay. How are you?"
    f "…"
    f "Still?"
    f "…"
    f "I thought you said it would be possible for you to come visit, though? Didn’t you just need some sort of pass?"
    f "…"

    scene futabaphonemom2
    with dissolve

    f "Oh, no. Not at all. I don’t need anything. "
    f "I’ve been saving basically everything you send me anyway since the dorm is free and-"
    f "...Yeah. I’m still with Rin."
    f "…"
    f "Yeah. She’s doing a lot better."
    f "Nodoka is actually here too now."
    f "…"
    f "Yes, she...is still Nodoka."
    f "…"
    f "My teacher?"
    f "He’s-"

    if bonus == True:
        s "Instructing you on how to properly pleasure a man."
    else:
        s "Giving you the good grades that you rightfully deserve."

    scene futabaphonemom3
    with dissolve

    f "HE’S FINE!"
    f "Mom, I’ve gotta go now. Someone just showed up to the library and-"
    f "Yes! I told you, I’m fine!"

    if bonus == True:
        s "Tell her about our “lessons.”"
    else:
        s "Tell her how much you are enjoying college and that everything is okay."

    f "Bye, Mom! Love you!"

    play sound "phonebeep.wav"
    scene futabaphonemom4
    with dissolve

    f "…"
    s "…"
    s "Good morning."
    f "Yes. Good morning."
    s "You should have let me talk to her."

    if bonus == True:
        f "I would have absolutely let you talk to her if the first thing out of your mouth wasn’t about our “lessons.”"
        s "I’m sorry, Futaba. I just can’t look at you without being overcome by lust and excitement."
        f "You can’t look at {i}anything{/i} without being overcome by those feelings..."
        s "And you are no exception to that."
    else:
        f "Maybe next time."

    s "Why were you talking to your mom?"

    scene futabaphonemom5
    with dissolve

    f "Why?"
    f "Because...she’s my mom."
    f "I don’t think I really need a reason other than that, do I?"
    s "I guess not. I’ve just never seen you talking to her before."
    f "Do you not talk to your parents often, Sensei?"
    s "I don’t have any parents."

    scene futabaphonemom6
    with dissolve

    f "Wait, you weren’t...adopted like Rin, were you?"

    if bonus == True:
        s "No. I just have zero recollection of my non-Ami family. So it’s essentially the same thing as not having parents."
        f "That’s...not exactly the same thing."
        f "They might be really worried about you."
        s "Or dead."
    else:
        s "Nah. I think I just kinda showed up one day."
        s "My background isn't ever really explained."

    scene futabaphonemom7
    with dissolve

    f "R-Right..."

    if bonus == True:
        f "Or dead..."

    s "Way I look at it is that I have no need for them, so them not existing isn’t really a big deal."
    s "I’m sure it saves me a lot of time too since I don’t have to talk to them on the phone while other people are waiting for me."
    f "Sensei, I’m not going to apologize for talking to my Mom instead of you."
    s "First the gym, now this?"
    s "Futaba...do you hate me?"

    scene futabaphonemom8
    with dissolve

    f "Of course not...you’re no less important to me at this point than Rin or Nodoka."
    f "Well, actually, you’re a little less important to me than them. But that’s only because I’ve known them for a lot longer and..."
    f "And I...still don’t totally understand what’s going on between us..."

    if bonus == True:
        s "If you take your clothes off, I’d be happy to remind you."
    else:
        s "Huh? Aren't we hug buddies?"

    scene futabaphonemom9
    with dissolve

    f "Uhh...no. I’m okay."

    scene black
    with dissolve

    "Futaba hates me now and our relationship is over."
    "I go home and spend the rest of the day wallowing in sadness and self-pity."

    f "Sensei...can you please open your eyes?"

    scene futabaphonemom9
    with dissolve

    s "Yes. But not because you asked me to. Because it is unsafe to keep them closed when there are wild animals out here that could tear me to shreds at any given moment."
    f "We live in suburban Japan...there isn’t any wild animal that is going to attack you out of nowhere like that."
    s "I’m keeping my eyes open just in case."
    f "R-Right..."

    scene futabaphonemom10
    with dissolve

    f "Umm...anyway...I’m kind of glad that you showed up this morning because I..."
    f "Wanted to tell you a little about how the other night went. Since I...made you leave and stuff."
    s "Sure. What’s there to say, though? "
    s "Figured you three just...did gym stuff for an hour or two and went back home."

    scene futabaphonemom11
    with dissolve

    f "That’s exactly right. We did gym stuff for an hour or two and then went back home."
    f "But...since it was just Rin and Nodoka...I was less worried about...looking like an idiot and..."
    f "I don’t know. I think I maybe even felt a little good afterwards."
    f "Obviously nothing has really changed yet since it was only one day, but...yeah."
    f "I wanted to let you know that...I didn’t just...cry the entire time after you left."
    f "I actually...followed through and tried to make myself better."

    if bookdate == True:
        scene futabaphonemom10
        with dissolve

        f "Do you...remember when the two of us went to the bookstore together?"
        f "And how I...kind of confessed my feelings for you?"
        s "It wasn’t “kind of.” You made it very apparent that you’re falling in love with me."
        f "And you made it very apparent that focusing on things like that isn’t productive if I can’t accept who I am first."
        f "The thing is, though...I don’t want to accept who I am. I want to be somebody else."
    else:
        s "What is “better,” though? What’s so hard about accepting who you are?"
        f "Who I am isn’t who I want to be. That’s the issue."

    scene futabaphonemom11
    with dissolve

    f "If I could wake up in the morning and see someone with Rin’s body...or Chika’s body...or basically anyone else’s body, I’d be a lot more comfortable stepping outside."
    f "But right now, it’s kind of like staring into an abyss. Or...TV static, I guess."
    f "It’s just one huge mess of spare parts that don’t fit together...but it’s still closer to some sort of...indiscernible blur than a monster."
    f "If you saw something like that, you’d try to tune it out too, right?..."
    f "I’m sure you’d do all sorts of...self-destructive things to hide the truth of how you feel, because that’s the easiest thing someone {i}can{/i} do."

    if bonus == True:
        play sound "static.mp3"
        scene imissyou12 with flash
        scene futabaphonemom11 with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown with flash
        scene futabaphonemom11 with flash
        stop sound

    f "The easiest routes always have downsides, though. They wouldn’t be easy if there wasn’t some sort of risk involved."

    play sound "static.mp3"
    scene imissyou19 with flash
    scene futabaphonemom11 with flash
    stop sound

    f "I...don’t know if you can really understand what I’m talking about since...you seem really comfortable with-"
    s "I know what you’re talking about."

    scene futabaphonemom12
    with dissolve

    f "You do?"
    s "Yes."
    s "I can’t really put my finger on how, but I do."
    s "I think we perceive self-destruction a little differently than one another, though."
    f "Why is that?"
    s "Well, you think it’s something that can be avoided and I think it’s an inevitable fate."
    s "We’re all going to self-destruct one way or another, so pushing it back with hard work and determination is just a waste of energy."

    scene futabaphonemom13
    with dissolve

    f "No..."
    f "You’re wrong about that."
    f "Because even if my destruction is inevitable, I want at least one day where I can see my shadow next to yours and not hate myself for the differences in them."
    f "So I can’t give up until I get at least one day like that."

    scene futabaphonemom11
    with dissolve

    f "Hopefully, it won’t end after just one day, though."
    f "To put it bluntly, I feel rather lonely whenever I see my shadow {i}without{/i} yours next to it."
    f "So you can be as negative and insightful as you want, but I’ve made my decision and I’m going to stick to it."
    f "There’s something I’ve been hiding from you, Sensei...one of the downsides from the easier path I took before deciding to {i}actually{/i} start trying again."
    s "And that downside is?"
    f "That downside {i}was{/i}. It’s not happening anymore."
    f "And I can’t guarantee it won’t ever happen again...but I can at least say I’ll try my best not to-"
    s "Just tell me what it is, Futaba."

    scene futabaphonemom14
    with dissolve

    f "An...eating disorder."
    f "And this isn’t me asking for sympathy. It’s me telling you because I’m tired of keeping it a secret from you for no good reason."
    f "But I’ve been making myself throw up to try and lose weight for a...pretty long time now."
    f "And that’s part of what my Mom and I were talking about today."
    f "She and my dad thought I’d stopped a long time ago, but..."
    f "Well, it’s a lot easier to lie to people when they’re not physically around."
    f "But...I came clean to her as well."

    if bonus == True:
        s "Suddenly, the timing of my sex joke seems a lot worse than it did at first."
    else:
        s "I interrupted such an important phone call? You should have slapped me."

    scene futabaphonemom9
    with dissolve

    if bonus == True:
        f "There...isn’t really any acceptable time for making a sex joke while a [teenage]girl is on the phone with her mom..."
    else:
        f "I will next time..."

    s "You’re okay now, though?"
    s "You’re not doing that whole...vomiting thing anymore?"

    scene futabaphonemom11
    with dissolve

    f "Right...so...if I...start gaining weight from...{i}not{/i} doing that-"
    s "I’ve already told you that I don’t care about-"
    f "You do, though. And it’s fine that you do."
    s "I don’t know how many times I have to say this, but nope. Don’t care at all."

    if bonus == True:
        f "Then...why haven’t we had sex yet?"
        s "Hey, I’m ready whenever you are. I’ve been holding off because you’re clearly uncomfortable with it."
    else:
        f "Then why has the amount of hugs we have on a weekly basis dwindled as of late?"
        s "Hey, I always accept more hugs. Do not blame me for the fact that you are slowly becoming anti-hug."

    scene futabaphonemom15
    with dissolve

    f "Hahaha! Yeah...Yeah, I guess that’s mostly on me..."

    if bonus == True:
        s "Not “mostly.” I will literally have sex with you right now. I don’t care."
    else:
        s "I will hug you right now. I don't even care."

    scene futabaphonemom16
    with dissolve

    f "Okay, so maybe you really {i}don’t{/i} care. But I still do."
    f "Even...being touched by you makes me feel...extremely self-conscious and...yeah."
    f "This isn’t really a thing I want to be talking about outside of the library, now that I think about it."
    s "Then take the day off and...let’s go for a walk or something."
    f "Sensei, I can’t just-"
    s "You’ve made it pretty apparent today that you can do whatever the hell you want."
    s "If you can decide to turn your life around and try to become a version of yourself you like more, I’m pretty sure you can survive a day away from your volunteer librarian position."
    f "…"
    s "Don’t just stand there while I’m taking revenge on you for kicking me out of the gym the other night."
    f "I’m not just standing here. I’m waiting for you to lead the way."
    s "Oh. I expected there to be some sort of verbal agreement."
    s "That’s normally how accepting invitations works."
    f "Since when do we do {i}anything{/i} how we’re supposed to be doing it?"

    if bonus == True:
        f "I’m a freshman and I gave you a boobjob in the nurse’s office."
    else:
        f "The last time we made macaroni and cheese, you used four whole sticks of butter."

    s "Yeah, that was awesome."
    f "It was...fine. But what I’m saying is that we’re so far removed from how things are {i}supposed{/i} to be done that we should just...follow our hearts."
    f "And today, like many other days, my heart wants me beside your shadow."

    scene black
    with dissolve2

    "I don’t find much of a point in responding to Futaba as she is clearly much more determined to speak today than I am."
    "My irrational rage aimed at her refusal to allow me to watch her gym routine has finally subsided, however, and the two of us are now on a journey to-"

    scene futabaphonemom17
    with dissolve

    f "The...other side of the[school]?"
    s "I didn’t know where else to go."
    f "You...were the one who invited me to walk around, though..."
    f "You didn’t even have a plan in store?"
    s "Every plan I’ve ever made has been significantly less wholesome than walking around town with a girl who just opened up about her insecurities to me."
    f "You’re more than welcome to...share a few insecurities of your own, Sensei."
    f "I’m sure there has to be something."

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

label library40part2:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
    if futaba_love >= 20 and library20 == False:
        jump library20
    if futaba_love >= 25 and futabanew3 == True and library20 == True and library25 == False:
        jump library25
    if futaba_love >= 30 and futabadorm25 == True and beachvacation16 == True and library25 == True and library30 == False:
        jump library30
    if futaba_love >= 35 and rindorm35 == True and futabadorm30 == True and library35 == False:
        jump library35
    if futaba_love >= 40 and futabadorm40 == True and yumicallnight35 == True and kaoridate15p3 == True and library40 == False:
        jump library40
...
```