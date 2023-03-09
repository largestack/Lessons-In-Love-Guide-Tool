# A Hairline Fracture
Imani event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=imanidate5&go=Go)



## Event preconditions
✅Imani love greater than or equal to 5

❌Event "[Imani: Somewhere I Belong](./imanidate1.md)" is completed (event=imanidate1)

❌imaninumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: imanidate5
* Group: Imani
* Triggered by label: callimaninight
* Triggered by branch label: callnight

## Event code
File: \game\ImaniEvents.rpy
Code:
```python
...
label imanidate5:
    play sound "phonebeep.wav"

    "I tap on Imani’s name in my phone and wait for her to answer."
    "Despite the amount of time we’ve been spending together lately and the amount I have learned as a result of that, I don’t feel like things between us have really {i}changed{/i} at all."
    "So maybe today, something will happen to make me reevaluate that."

    play sound "phonebeep.wav"

    ima "Yoooo, Senpai! What’s going on?"

    "Or maybe nothing new will happen at all."

    s "Nothing much. What are you doing?"
    ima "Dying. What’s your address?"

    "Or...maybe something {i}will{/i} happen after all?"

    s "Why do you need my address?"
    ima "Because I’m coming over, obviously."
    s "I mean, I’m fine with that. But after hearing that you’re “dying” and how you immediately decided to come over without asking, I can’t help but be mildly concerned."
    ima "Be concerned on your own time, you’re wasting my minutes."
    s "Who doesn’t have unlimited phone time in this day and age?"
    ima "People like me who are still using prepaid plans. Now, address please. I’ll explain when I get there."
    s "Fine. See you soon, I guess."

    play sound "phonebeep.wav"
    stop music fadeout 10.0
    scene black
    with dissolve

    "I hang up the phone and send Imani my address."
    "Considering how far away she lives, I think I {i}should{/i} be able to make it back in time. But I have no idea what Ami is up to today, so..."
    "Well, I guess I’ll just have to wait and see if the day will end in tragedy, or if it will end with the defilement of my underling’s body."
    "Probably tragedy."
    "It’s almost always tragedy."
    "........."
    "......"
    "..."

    scene imanicomesover1
    with dissolve2
    play music "lifeismostlygood.mp3"

    ima "Pardon the intrusion. And thanks for having me over. You’re a real life saver."
    s "Uhh...why do you have so many bags?"
    ima "Because I live here now."
    s "That is not what we discussed over the phone."

    scene imanicomesover2
    with dissolve

    ima "It’s not?"
    s "All you told me is that you were running low on minutes and that you’d explain things when you got here. Not that you’d move in."
    ima "I don’t know, Senpai. I’m pretty sure I filled you in on all of the necessary details. But if you {i}really{/i} don’t want me to live here, I guess I can go home."
    s "Cool. See you later, then."

    scene imanicomesover3
    with dissolve

    ima "Fight for me, Senpai! Hold me tight and never let go! Don’t let me just walk out of your life that easy!"
    s "Imani, what’s really going on here?"

    scene imanicomesover4
    with dissolve

    ima "My AC unit busted and turned my apartment into a hotbox. "
    ima "I was actually already planning on calling you and asking if I could crash at your place for the night. But then {i}you{/i} called {i}me{/i} and I figured you’d have a harder time saying no if I was already here."
    s "If it’s just for tonight, why do you have three bags?"

    scene imanicomesover5
    with dissolve

    ima "In case you wanted me to stay longer. As it turns out, my cockroach buddy’s got a whole ass family, so I figured it might be cool to let them have the place for a few days."
    ima "Or for the indefinite future so I can become one of those people who overstays her welcome for so long that she just starts living here without ever having to sign a lease."
    s "If you can convince Ami, sure. You can move in."

    scene imanicomesover6
    with dissolve

    ima "Seriously?"
    s "That depends on if you’re actually serious."
    ima "I mean...I wouldn’t {i}not{/i} be serious about this if you were cool with it."
    ima "Not gonna lie, having an actual kitchen and an actual bathroom sounds a hell of a lot better than having to use the community ones at my apartment."
    ima "Fine. I accept. And for rent, I will let you choose between the 50,000 yen I’m paying for my current place or one sexual favor per week. No mouth. "
    s "No mouth, no deal. I’ll take the money. "

    scene imanicomesover7
    with dissolve

    ima "Understood. Pleasure doing business with you, Senpai. Assuming this isn’t just one big joke, of course. Which I kind of hope it isn’t, but will understand if it is."
    ima "Anyway, where can I put my stuff?"
    s "Wherever. I’ll make Ami take care of it once she gets back."

    scene black
    with dissolve2

    "Imani places all of her bags on the dining room table before returning to me, empty-handed and several minutes away from being forced to fight for her life."
    "Of course, I already know for a fact that she {i}won’t{/i} be living here any time soon, but I doubt one night will be a problem so long as she sleeps in the living room."
    "Either that or I get extremely lucky and Ami just doesn’t come home at all, leaving Imani the option of staying in my room instead- something with roughly a 50%% chance of success based on my calculations."

    scene imanicomesover8
    with dissolve2

    ima "No wonder you talked mad shit on my place, Senpai. Your house is actually pretty nice. Sweet neighborhood, too."
    ima "Can see myself settling down here fifteen years from now when we accidentally reunite at a local museum and decide to go out for one last drink. You know, for old time’s sake."
    ima "But then one drink would turn into ten and we’d wind up finally banging after all that time of {i}knowing{/i} we want to, but never following through with it because reasons."
    ima "Anyway, what’s for dinner? You cooking?"
    s "I don’t think you want to eat anything I make. "
    ima "Same. Guess we’re a takeout family now."
    s "If Ami comes home, I’m sure she’ll throw something together. I just can’t guarantee that your portion will be free of rat poison."
    ima "And if Ami {i}doesn’t{/i} come home?"
    s "We’ll probably order a pizza and continue not having sex for some reason."
    ima "Sounds like my kind of night."

    play sound "dooropen.mp3"
    scene imanicomesover9
    with dissolve

    a "I knew I sensed an intruder."
    ima "Welp, there that goes."
    ay "Imani? What are you doing here?"

    scene imanicomesover10
    with dissolve

    ima "I live here now. I’ll take my steak medium-rare, Ami. Thanks. "
    a "Sure, Miss Imai. Would you also like a side of {i}murder?{/i}"
    ay "Don’t be mean, Ami. She can give you detention. "
    s "Imani’s air conditioner broke. She’ll be staying here for the night."

    scene imanicomesover11
    with dissolve

    a "What?! But you already told me Ayane and Maya could sleep over!"
    s "I don't remember that at all."
    ima "Ooh! Slumber party! That sounds way more fun than not hooking up with your uncle!"

    scene imanicomesover12
    with dissolve

    a "You’re not invited! You can continue not hooking up with my uncle all by yourself in the corner of the room! "
    ima "She loves you so much. It’s adorable."
    s "Don’t piss her off {i}too{/i} much. Remember that she’s the one making your dinner."

    scene imanicomesover13
    with dissolve

    a "Tch! When did my precious house become a brothel?"
    ay "Where will Imani be sleeping? If there’s a lack of room for her, I wouldn’t mind volunteering to sleep with you, Sensei. "
    s "I think there’s plenty of room for her, but I’ll keep that in mind. "
    ima "I was probably just gonna crash on the couch. Joke’s aside, Sensei and I aren’t like that. You guys have nothing to worry about."
    ima "My place is just mad hot and I didn’t want to die. I’ll bounce as soon as the AC repair guy leaves."
    ima "Oh, and ignore all of the bags. I brought those just in case he wants to keep me for whatever reason. But now I just feel weird since my students are watching me."
    a "We are {i}Sensei’s{/i} students. You do not own the original Sensei Love Squad."
    m "Minus Maya. Not a member of the Love Squad. "

    "Lies."

    ay "Lies."

    "Thank you, Ayane."

    scene imanicomesover14
    with dissolve

    m "Hah..."
    ima "So...now what? Wanna play truth or dare again?"
    s "Depends. Which of the girls are you going to make out with this time?"
    ima "I guess that hinges on the dare."
    s "Truth or dare."
    ima "Truth."
    s "Not what I wanted."
    ima "I can not accept a dare in an environment like this. I am not you."
    ay "They’re playing games with each other...and excluding us. "
    ay "I don’t like this."
    a "Why do you think I never want anyone older to come here? It’s a slippery slope, Ayane. And right now, there’s nobody more...slippery than Miss Imai. How could I have been so blind?"
    m "Okay. I’m going to get changed now. I’m tired and haven’t worn this shirt in yet. It's uncomfortable."

    scene imanicomesover15
    with dissolve

    ay "I think it’s the bra. You’ve always worn those tank-top style ones and switching from that to an {i}actual{/i} bra is obviously going to- why are you looking at me like that?"
    m "I wonder."

    scene imanicomesover16
    with dissolve

    s "Ayane, truth or dare."
    ay "Dare!"
    s "Kiss Maya."

    scene imanicomesover17
    with dissolve

    ay "Your wish is my com- wait, where did she go?"

    scene imanicomesover18
    with dissolve

    ay "Maya, come back! Sensei wants us to kiss!"
    m "Don’t come anywhere near me!"
    a "I’m watching you, Miss Imai..."
    a "One wrong move and you will feel the wrath of Ami. A wrath that few have felt before..."

    scene black
    with dissolve2

    "The girls (Minus Imani) retreat into Ami’s room to get changed into their pajamas and formulate some sort of battle plan to kill my student teacher."
    "Thankfully (For her, not so much me), Imani takes the hint and distances herself, unpacking a few of her things before going into the bathroom to get out of her casual clothes. "

    scene nightsky
    with dissolve2

    "The next couple hours go by rather...naturally, believe it or not."
    "All four of the girls return around the same time and Ami and Ayane prepare dinner together while the rest of us sit on the couch and watch TV."
    "Imani gets to eat a hot meal free of poison and I get to somehow sit next to her without incurring the apparently rare “wrath of Ami” at any point."
    "Dinner is the closest we come, though...and once it’s over, she and the two girls who prepared dinner lay out a futon on the floor before sitting down on it and forgetting I even exist."

    scene imanicomesover19
    with dissolve2

    "I don’t have a problem with that, though. "
    "It’s better for all of us if everyone manages to get along. And I guess the amount of exposure the girls already have to Imani is enough to get them to feel more...comfortable around her."
    "In just a short time, she’s managed to win almost everyone over- and I think a lot of that is due to the fact that, unlike me, she’s able to care about them without ever getting anything in return. "
    "She may say things about how being around girls their age isn’t good for her psyche and that looming fear of mortality hidden in the back of our minds but, to be honest, she looks content when they’re around."
    "She’s good at what she does...good at being a teacher."
    "But the fact that she seems even more comfortable with {i}me{/i} makes me question exactly what type of person she is underneath it all."

    ay "College? That’s so cool. I think you’ll be a great professor. You always seem really smart whenever you start getting into it about things."
    ima "I’m still a ways off, but I’ll get there. Thanks for the blessing, Ayane. You were always my favorite."
    a "Hey."
    ima "You’re also my favorite, Ami."
    ima "Everybody’s my favorite. "
    ima "Well, except Kirin. She keeps trying to have sex with me and I don’t like it."

    if ayanelust10 == True:
        ay "Oh, don’t worry. She does that with everyone. Something is seriously fucked up with her brain and we all just have to fucking deal with it, I guess."

        scene imanicomesover20
        with dissolve

        ima "Uhh..."
        ima "Did something-"
        ay "Nope."
    else:
        ay "Sounds like Kirin, alright. "

    ay "But anyway, do you think you’ll at least finish the school year with us? Or should we try not getting {i}too{/i} attached?"

    scene imanicomesover21
    with dissolve

    ima "Attached to me already? Come on, I don’t deserve that. I’m just doing what any other teacher would do. Minus Sensei, of course. But he’s a special case."
    ay "Neither Ami nor I have any older women to look up to, really. And I don’t want to speak for her, but having you around makes us kind of...happy."
    a "I do like you, Miss Imai. I’m just not very good with...uhh...{i}change.{/i}"

    scene imanicomesover22
    with dissolve

    ima "Aww, you guys! You don’t have to go getting sentimental on me!"
    ima "I know doing that is a cornerstone of slumber parties and I’m not about to tell you to stop because hearing that was a major dopamine hit, but...{i}you guys!{/i}"
    ima "I like you too. And I’ll be happy to stay around as long as I can. But I can’t predict the future, and getting attached to {i}anything{/i} can be really dangerous."
    ima "Just be smart and don’t cry too much if I’m suddenly gone one day, okay?"

    scene imanicomesover23
    with fade

    m "I hope you’re happy, starting this festival of {i}feelings.{/i} Something we all know you don’t actually have."
    s "You’re one to talk. I don’t think either of us can really speak to what it’s like to openly discuss our emotions with others."

    scene imanicomesover24
    with dissolve

    m "Yes. Well, I suppose there’s a reason the two of us are standing off to the side while everyone else sits in a circle and carves out little pieces of their heart."
    s "Can’t really make a circle with three people."
    m "I suppose not. But you {i}can{/i} make a triangle, which bears its own form of significance in the fact that-"
    s "Oh no. We’re the philosophical group, aren’t we? And everyone else is part of the fun group."
    m "..."
    s "..."

    scene imanicomesover25
    with dissolve

    m "Philosophy can be fun..."
    m "It’s not my fault you suck at it."

    scene imanicomesover26
    with dissolve

    s "How do {i}you{/i} feel about Imani, Maya?"
    m "Me? In what way?"
    s "In general. Do you like her?"
    m "She’s...fine. "
    m "I have a hard time “liking” anyone. But is there a reason you’re suddenly asking {i}me?{/i} Why do my feelings in regard to someone else matter at all?"

    scene imanicomesover27
    with dissolve

    s "Just...thinking you guys might be better off with her as your full-time teacher rather than me."
    m "I see."

    scene imanicomesover28
    with dissolve

    m "Well, we definitely would. You’re the actual worst person for the job you wound up with."
    m "But I guess I can’t complain as I, too, wound up in a position I never asked for. Never fit. "
    m "Sometimes, life itself chooses what we’re meant to consume. And all we’re able to do is choke down what it serves us and pretend it’s what we wanted."
    m "For the rest of eternity...or until “eternity” breaks."
    s "Philosophy group rules. Who needs fun when we can create metaphors all night?"

    scene imanicomesover29
    with dissolve

    m "Even that is fun in its own way."
    ima "Uhh, Ami? Is it cool if I use your bath? I feel kind of gross from the air conditioning fiasco earlier and don’t think I’ll be able to sleep like this."
    ima "Was gonna try to tough it out because, you know, unfamiliar bath...but yeah. Don’t think that’s gonna be possible."
    a "Oh, sure. I can fill the tub for you right now."
    ima "It’s fine, it’s fine. You stay out here with Ayane. I’m sure I can figure out how a bath works."

    scene black
    with dissolve2

    ay "What if we all went in together? I kind of want to take a bath now too."
    a "This is something you should have said before we put on our pajamas. "
    ay "Sue me. I’m a free woman. I say things when I want."
    a "Also, all three of us? There’s no way we’d even fit."
    ay "But we do it with Maya all the time."
    a "I think Miss Imai is a little bigger than Maya."
    ima "Just a {i}little.{/i} But I’m not much of a “group bather” anyway, so I’ll be quick and then you guys can get in after me."
    ay "Are you sure? We could save time if we-"
    ima "I’ll be {i}super{/i} quick! Don’t even worry. It’ll be like I never even left in the first place!"
    ay "But-"
    a "Just let her go, Ayane. You’re in the swim club now. You’ll have plenty of opportunities to see her naked."
    ay "I just wanted to bond! "

    "........."
    "......"
    "..."
    "{i}The festivities continue on for the rest of the night.{/i}"

    $ renpy.end_replay()

    stop music
    play sound "static.mp3"
    scene imanicomesover30 with flash
    stop sound

    "{i}But for a brief moment, there is a fracture.{/i}"
    "{i}It goes unnoticed by the majority, but the part of the group that does recognize it sees nothing else until the night comes to an end.{/i}"

    scene black

    "{i}Until she closes her eyes and finds comfort in where she is and not who she is.{/i}"
    "{i}Until she wakes up the next day and leaves it all behind.{/i}"
    "{i}Oh, how easy it is to ignore our flaws when we cannot see them.{/i}"
    "{i}Oh, how easy it is to remember them once we can.{/i}"
    "{s}SLIP{/s} sleep"

    $ imani_love += 1
    $ imanidate5 = True

    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon
...
```

## Code that triggers this event
File: \game\ImaniEvents.rpy
Code:
```python
...
label callimaninight:
    if imani_love > 0 and wakanaspecial15 == True and imanidate1 == False:
        jump imanidate1
    if imani_love >= 5 and imanidate1 == True and imanidate5 == False:
        jump imanidate5
...
```