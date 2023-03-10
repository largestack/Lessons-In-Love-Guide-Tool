# Turn On The Lights (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 10

* Event [War's End](./dormwar17.md) (Main) is completed)



## Next events

* [Io: Amongst Other Things](./iodorm15.md)

## Event properties

* Id: bathhouse10
* Group: Io
* Triggered by label: bathhouse
* Triggered by branch label: bathhouse
* Triggered by path: bathhouse->bathhouse10

## Official wiki page

[Turn On The Lights](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bathhouse10&go=Go) for more details.

## Event code

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse10:
    scene bathhouseten1
    with fade
    play music "normalday.mp3"

    "I head over to the bathhouse to find Io and Yuki hanging out at the counter."
    "And, judging by Yuki’s skin being significantly less pale and lifeless than usual, I think it’s safe to assume that she is on her way out."
    "I apologize to Yuki inside of my head for making fun of her skin. I wish her the best in her journey back to health."

    if bonus == True:
        yu "Yo. Five minutes earlier and you would have gotten to see me nude."
        s "Damn it. I knew I should have run here."
    else:
        yu "Yo."

    i "Hey, Sensei. Welcome back."
    i "Yuki was just leaving."

    scene bathhouseten2
    with dissolve

    yu "Was I? Cause I’m pretty sure I was planning on making fun of you for losing to my daughter a little more."
    i "Nope! You were just leaving. Bye, Yuki."
    s "I take it this means you told her about the dorm war results?"

    scene bathhouseten3
    with dissolve

    yu "See? Told you Yumi was going to win if all that had to be done was cooperate or whatever."
    yu "Io’s less of a brat, but she’ll never cooperate with anyone or anything. Just the kind of girl she is."
    i "Yes. I am a pitiful isolationist. Why are we still talking about this?"
    yu "Cause I’ve gotta brag to your fuckin’ teacher on my way out."
    i "What will that accomplish, though? It's already over and done with."

    scene bathhouseten4
    with dissolve

    yu "It won’t {i}accomplish{/i} shit. It’s just fun."
    i "This is the last time I let you use my shampoo."
    i "Your bill is six million yen. Please leave the money on the counter and be on your way."
    yu "Nah, hold on a sec. Just cause I want to brag about how I was right doesn’t mean there’s no lesson on the way for you."
    i "Can we maybe leave the lessons to my teacher?"
    s "No. Go ahead, Yuki. I don’t particularly enjoy teaching anyway."
    yu "Then change your fucking career, dude."
    i "Ugh...what’s the “lesson” I have to learn today, Yuki? Just get it over with."

    scene bathhouseten5
    with dissolve

    yu "The lesson is that you’re completely fucked if you’re not even going to try and win winnable battles."
    yu "The hell is wrong with cooperating? What happened to all that shit about you being fake as hell or whatever it is you’re always saying?"
    yu "Wouldn't being fake mean sticking your neck out for your team even though you don’t want to?"
    i "You’re forgetting the very important detail of me also being a hypocrite. "
    i "So yes, I am incredibly fake in many respects. But I am fake on my own terms. Which means not getting involved with a bunch of sentient handbags."
    yu "Yumi might be a brat, but she ain’t a fuckin’ handbag."
    i "Yumi was on the other team. And she like, won by default or something. So it’s not like it was even a deserved win."
    i "Also, why are we still talking about this?"
    yu "Just fuckin’ shape up, kid. Ya ain’t gonna be happy if you’re so dead set on never doing anything for the rest of your life."
    i "Then I guess I’m never going to be happy. Thanks, Yuki."

    scene bathhouseten6
    with dissolve

    yu "Man, do you really deal with this shit every day?"
    s "Not really. In true Io fashion, she doesn’t really talk while she’s in[school]."
    yu "Beat. Just means she’s missin’ out on forging new friendships and all that."
    s "Yes. At this rate, Io will never have any bond as strong as the one between you and me, Yuki."

    scene bathhouseten7
    with dissolve

    i "I have Uta!"
    i "And besides, you two aren’t even that close!"
    yu "Sure we are. Your teacher and I chill all the time now. He practically has me on speed dial."
    i "Speed dial isn’t even a thing anymore! Probably."
    i "If it is, I have no idea how to use it."

    scene bathhouseten8
    with dissolve

    i "But that doesn’t matter! "
    i "You two can get as close as you want. I don’t care."
    i "But rubbing it in my face isn’t going to make me think, “Oh. Time to turn things around and be a normal member of society.”"
    yu "We can get as close as we want?"

    if bonus == True:
        i "I mean, I’d prefer that you didn’t because it would make things extremely awkward for me and I really don’t want to clean up whatever mess you would leave behind in the men’s bath-"
    else:
        i "Yeah. You can even...{i}hug{/i} if you want."

    scene bathhouseten9
    with dissolve

    yu "Uhh...okay. No need to get graphic. I obviously wasn’t being serious."

    "Damn it."

    i "But still...I don’t care. Do whatever."
    i "Also, the whole thing with the speed dial wasn’t even fair since Sensei doesn’t have my phone number yet."
    s "You know there’s a very easy way to change that, right?"

    scene bathhouseten10
    with dissolve

    yu "You really askin’ a [teenage]girl for her number right in front of me? "
    s "Yes, because you and I have an unbreakable bond and you will not judge me for it."
    yu "That was just...yeah, aight. Whatever."
    i "I’d be more than happy to give you my contact information. I was just under the impression you didn’t want me to have {i}yours{/i} since I would annoy you all the time."
    s "You already annoy me all the time. A little more won’t hurt."

    scene bathhouseten11
    with dissolve

    i "Really?!"
    s "Oh, wow. You're really that excited about this?"
    i "I am! Because now I can shove it in Yuki’s stupid face and start my own inseparable bond with you!"
    yu "The fuck just happened? We were teasing her like two seconds ago and now you guys are legit flirting."
    s "It’s not flirting. Io just really likes me for some reason."

    scene bathhouseten12
    with dissolve

    yu "Yeah...weird."
    yu "You ain’t hiding a dragon tattoo anywhere on your body, are you? Only time I’ve seen her get that excited is when she got to touch mine."
    s "No, but...I’ve also never looked at my back, so..."

    scene bathhouseten13
    with dissolve

    i "Want me to check for you?"
    i "My hands are cold and calloused and I can’t imagine they’ll feel very good if I touch you but, so long as you don’t turn around, it should be fine."

    if bonus == True:
        s "What’s wrong with turning around when you’ve seen my penis before?"

    scene bathhouseten14
    with dissolve

    yu "Okay, that’s enough for me."
    yu "Enjoy your new unbreakable bond or whatever. I’m gonna go load up on ramen and probably pass out on my bike."
    i "Night, Yuki. Thanks for inadvertently becoming the bridge Sensei and I needed to exchange contact information."
    yu "Kids are fuckin’ weird now."

    scene bathhouseten15
    with fade

    "Yuki leaves the store and I get a little closer to the counter."

    if bonus == True:
        s "So, about my penis."
        i "Weird segue."
        s "Does this bathhouse provide any sort of “extra services?” Because that's what you made it sound like just now."
        i "Nope. But I’m sure one of the imaginary old ladies playing mahjong in the back room that we don’t have would be happy to help you out for the right price."
        s "So that thing about your hands being cold and calloused or whatever-"
        i "Grave misinterpretation. I was just talking about washing your back."
        s "Well, it would certainly make sense why I’m not supposed to turn around then."
        i "Right."
    else:
        s "Do you guys sell M&M's here?"
        i "What? No."
        s "I really want them, though."
        i "..."
        s "Please?"

    i "Anyway, can I give you my number now?"

    if bonus == True:
        s "Oh, cool. We got over that misunderstanding a lot quicker than I thought we would."
        i "It comes with the job. Gotta be ready for stuff like that."
        i "Number?"
        s "…"

    s "Sure."

    scene black
    with dissolve
    stop music fadeout 10.0

    "I slide my phone across the counter to Io, who programs her number into it and sends herself a quick text message to-"

    s "Wait, why did you send a heart?"
    i "First emoji I saw. Definitely not going to look at it all the time and tell myself that you like me or anything."
    s "That’s a strangely specific and unwarranted thing to clarify."
    i "Yes. Yes it is."
    i "Now! Right this way, sir! I will show you to your bath!"

    $ ionumber = True

    "{i}Congratulations! You now have Io’s cell phone number!{/i}"

    "Io quickly pushes me through the curtain and into the men’s locker room, completely disregarding her responsibilities as an employee of this establishment."
    "I’m going to have to file a complaint."

    if bonus == True:
        scene bathhouseten16
        with dissolve2
        play music "io.mp3"

        s "This is strange behavior for someone who refused {i}additional{/i} service to me just seconds ago."
        i "Feel free to undress whenever you’d like."
        s "Are you actually going to wash my back?"
        i "Nah. We don’t do that here either."
        s "But you {i}do{/i} escort customers to the locker room and watch them get undressed."
        i "Only one customer has received this “escort” you speak of, and I wasn’t planning on watching you."
        i "I was just gonna close my eyes and talk to you while you relaxed or something."
        i "I don’t know. It seemed less weird in the lobby where the TV was on and everything wasn’t completely silent."
        i "Should I leave? "
        i "I should leave."
        i "I’m gonna leave."
        s "You don’t have to leave."
        s "Just think of it as...payback for you getting undressed in my hotel room or something."
        i "Except I was in wholesome onesie pajamas afterward and you’re going to be...not wearing those."
        s "It would be an extremely funny surprise if I was, though."
        i "No, it would be gross and weird. Save the cute pajamas for me."
        s "Io, please explain to me what’s happening right now."
        i "The bad parts of me are waging war with good parts of me. Which are waging war with my hormones. Which are, in turn, waging war with my greatest fears."
        i "Basically, I’m being Io again. Yay."
        i "I don’t know. This is weird."
        s "Am I taking a bath or am I not taking a bath?"
        i "I...guess that depends on if you want to take a bath?"
        s "I mean, that wasn’t the intention when I came here..."
        i "Am I forcing you into doing something you aren’t comfortable with?"
        s "Are you forcing {i}yourself{/i} into doing something you aren’t comfortable with?"
        i "I’m just trying to spend time with you in a way that won’t tire you out."
        i "I’m exhausting, right?"
        i "And I figure that if you’re warm and cozy and wet and stuff, you’ll be a little less annoyed by all of the talking I’m going to do."
        s "And you’re not just saying that to compensate for something you’re realizing now is flat out odd?"

        scene bathhouseten17
        with dissolve

        i "So it’s odd because it’s me."
        s "It’s odd in general."
        i "But it wasn’t odd when you came here with that blonde girl."
        s "Okay, valid point."
        i "I mean...it’s not like I’m going to be {i}in there{/i} with you, you know? I’ll be turned around, talking about...stuff."
        s "Which, in theory, we could have just done in the lobby."
        i "But I already said all that stuff about you being relaxed and warm. So isn’t that like, a preexisting counterpoint?"
        s "It sounds like more of an unplanned rationalization to me."

        scene bathhouseten18
        with dissolve

        i "Then it fits me perfectly!"
        s "Io-"

        scene bathhouseten19
        with dissolve

        i "The fact that you’re still talking makes this a million times worse than it would be if you just...did what you wanted rather than wait for me to do something."
        s "…"

        "She’s right."
        "That’s what I’m {i}supposed{/i} to do after all."
        "Why bother trying to fix situations that I did not personally break?"
        "I’m here at a bathhouse. Which means I should take a bath."
        "And if anyone is there to awkwardly try and hold a conversation with me as it happens, that’s on them."

        s "You’re weird."

        scene bathhouseten20
        with dissolve

        i "Yeah..."
        i "Yeah, this was a bad idea."
        s "Nah. Just close your eyes."
        i "…"
        s "…"

        scene bathhouseten21
        with dissolve

        i "…"
        s "…"

        scene black
        with dissolve2

        "Io does as she’s told and closes her eyes."
        "I take a moment to awkwardly remove my clothes several feet away from a cute [teenager], something I’ve done hundreds (If not thousands) of times in the past."
        "But something feels different about this time in particular."
        "Like it’s something that neither of us particularly {i}wants{/i} to do, but something we’re doing nonetheless."
        "I don’t even have an erection."
        "It’s just a bath."
        "That’s all it is."

    play sound "water1.mp3"

    "I get into the water and let my body soak in both chemicals and uncertainty."
    "And I hear a stool dragged across the stone floor just moments later."

    scene bathhouseten22
    with dissolve

    i "Is it hot enough?"
    s "It’s fine."
    i "Okay..."
    s "…"
    i "…"
    i "So, uhh...Yuki."
    s "Is that going to be our conversation topic for the night?"
    i "It’s just the first thing that came to mind."
    i "Well, the first thing actually worth talking about that came to mind. "
    i "There were a lot of other things that popped into my head beforehand, but they were all either stupid or pointless."
    s "So...Yuki, then."

    scene bathhouseten23
    with dissolve

    i "Her and Yumi..."
    i "Could you...tell me a little about them?"
    s "Why not ask her?"
    i "I’ve tried. But she always gets this look on her face that’s like a mix of...regretful and defeated."
    i "And I don’t want to make her talk about things that will obviously upset her."
    i "And...given Yumi’s general demeanor, I’m starting to think that maybe Yuki wasn’t really as great back then as she is now."
    s "She’s had her fair share of problems. They all make sense given the situation she was brought up in, though."
    i "I see..."
    i "And...do you think that situation justifies anything that she may have done?"
    s "Of course not. The justification of tragedies like that is an inevitable result of a seemingly infinite desire to be forgiven shared by nearly all humans."
    i "Yeah...Yeah, it is."
    i "What is it you want to be forgiven for, Sensei?"
    s "..."
    s "Everything, I guess."
    s "I just don’t want to put in the work required to actually {i}be{/i} forgiven."
    s "And you?"
    i "Everything, I guess."
    i "I’d just rather hide from all of it because it’s exhausting even confronting things you don’t like looking back on."
    s "Does it make you feel any less alone knowing you’re not the only one going through that?"
    i "No."
    i "But I like being alone."
    s "So do I."

    scene bathhouseten24
    with dissolve

    i "But...you spend virtually all of your time with other people. I barely ever even get to see you."
    s "Being with other people is easier."
    s "When you’re alone, it’s a lot harder to ignore the parts of yourself you want forgiveness for."
    i "I think this is where our paths start to change directions."
    i "When I’m alone, I can focus on whatever I want."
    i "I can build things. Or read. Or watch baseball."
    i "Or I guess text you now that I finally have your phone number."
    i "But when I’m with anyone else, it’s like I’m constantly being reminded of everything I hate about this world."
    i "And I understand that it’s irrational to live this way and that it will greatly increase the amount of stress I have and lead me to an early grave..."
    i "But there are some things that you can’t change. Or things you wouldn’t want to change."
    i "Like...you, for example."
    i "You’re just as fucked up as I am on the inside, but I’d hate for you to be anyone other than who you are."
    s "Or who you think I am. You barely know me, all things considered."
    i "I don’t need to know your story to know who you are. "
    i "So long as you can understand where I’m coming from and I can understand where {i}you’re{/i} coming from, we can be completely different from one another but still exactly the same."

    scene bathhouseten25
    with dissolve

    i "Uhh....Wait. That sounded better in my head."
    i "It's a little too contradictory to put it that way."
    i "But...you understand...right?"
    i "That...we don’t need to know everything about each other."
    s "Of course."
    s "But that will never mean we won’t {i}want{/i} to know."
    i "Yeah..."
    i "Umm...Sensei?"
    i "Is it..."
    i "Is it wrong for me to hope that Yuki and Yumi never patch things up with one another?"
    s "I mean...it’s not really your place to get involved."
    s "Are you afraid of losing Yuki or something?"
    i "No. It’s nothing like that."
    i "I just think I’d have a little more faith in myself if I got to watch others fail as well."
    i "There’s something incredibly vindicating about watching others struggle while you’re struggling yourself."
    i "It’s like turning off all of the lights and letting your eyes adjust."
    i "If you fill your world with sadness, you’ll get used to it and get better at accepting it."
    i "If everything is depressing to begin with, you can manage to find joy in even minor tragedies because, by comparison, they really aren’t as bad as they could be."
    i "I guess I just want more people to turn the lights off."
    i "And for me-"
    s "It’s like everyone is walking into your room and turning them on."

    scene bathhouseten26
    with dissolve

    i "…"
    s "…"
    i "I..."
    i "…"
    s "…"

    scene bathhouseten27
    with dissolve

    i "I..."
    i "Shouldn’t say what I was about to say yet."
    i "It’s too soon."
    s "...?"

    scene bathhouseten28
    with dissolve

    i "When the[school] year ends...do you want to go somewhere with me?"
    s "Where did you have in mind?"
    i "Somewhere far away. Like...maybe America or something?"
    s "We’re not allowed to leave Kumon-mi."
    i "Then...an amusement park?"
    s "What is it with you and amusement parks all of a sudden?"
    i "It could be anywhere."
    i "But...I want to be with you."
    s "Hmm..."
    s "I don’t know."

    if bonus == True:
        i "Why...not?"
        s "I’m not sure how I feel about being with a girl who can look at me while I’m naked and not actually do anything about it."
        i "But my hands are all cold and calloused."
        s "Still better than no hands at all."
    else:
        s "Sounds kind of inappropriate."

    i "…"
    s "…"

    scene bathhouseten29
    with dissolve

    i "Okay...that’s enough bathside talk for now."
    i "I’m gonna go back to watching the game. But you’re free to take as long as you want in here."

    if bonus == True:
        i "Also, if you hang around for a few more hours, you might get to see Uta’s boobs through the hole in the fence."
        s "There’s a hole in the fence? Where?"
        i "{i}It’s a mystery.{/i}"
        s "Io, you can’t just tell me something like that exists and then not help me."
        i "I’ll show you if you promise to run away with me one day."
        s "What kind of trade is that?"
        i "One where we both get something we want very badly."
        s "Ugh..."
        s "I’ll just find it myself."
        i "And I’ll keep slowly poisoning myself with unattainable desires."

    i "Enjoy your bath, Sensei."

    scene black
    with dissolve2

    "Io leaves and I suddenly feel a lot more alone than I thought I would."
    "Even the sound of the water is barely audible while I’m not moving around."
    "And since no one seems to be on the other side of the bath right now, I can’t even steal away the opposing share of ambiance."
    "I just soak."
    "In chemicals and uncertainty, I soak and wonder what it is that made Io the way she is."
    "If it was anything at all."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse10 = True
    stop music fadeout 7.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label bathhouse20:
...
```

## Code that triggers this event

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse:
    if io_love >= 0 and day247 == True and bathhouse1 == False:
        jump bathhouse1
    if io_love >= 5 and bathhouse1 == True and bathhouse5 == False:
        jump bathhouse5
    if io_love >= 10 and dormwar17 == True and bathhouse10 == False:
        jump bathhouse10
...
```