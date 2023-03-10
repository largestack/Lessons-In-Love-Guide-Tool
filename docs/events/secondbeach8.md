# The Legacy of Thaum Pt. III: Changeling (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Everything Ephemeral](./secondbeach7.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach8
* Group: Main
* Triggered by label: secondbeach7
* Chain sources: secondbeach7
* Chain sources path: secondbeach7

## Official wiki page

[The Legacy of Thaum Pt. III: Changeling](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach8&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach8:
    scene thirdthaum1
    play music "breeze.mp3"

    mo "Sisters! Brothers! "
    mo "The time has come for yet another installment in our violent and glorious campaign of...glorious violence!"
    m "Is it me or were some of us just referred to as “brothers?”"
    r "If we were boys, which one of us would have the biggest wiener? "
    ay "Tsuneyo. Hands down."
    m "I can see it."
    t "Blasphemy. I do not even like hot dogs."

    scene thirdthaum2
    with dissolve

    mo "Silence! All discussion pertaining to wieners will be kept to a minimum outside of in-character sexual exploits!"
    mo "We have a lot of ground to cover today and I will not allow the ramblings of the Kendo Princess and her metaphorical, sexual hot dog consume your attention in place of my...words!"
    t "The hot dog is a food item, Emerald Guardian. It is not sexual in nature."

    scene thirdthaum3
    with dissolve

    mo "{i}Ahem{/i}...Whatever the case, I would like to welcome our newest campaign member to the table..."

    scene thirdthaum4
    with hpunch

    mo "Ram! The changeling bard!"
    t "Yes. It is I. Ram, the changeling bard."
    f "Um...why “Ram?”"
    t "The Emerald Guardian said the name “Ramen” was too long for a changeling. This was the compromise we reached."
    mo "Ramen isn’t really a...name in general, so..."

    scene thirdthaum5
    with dissolve

    mo "You know what? That doesn’t matter right now! What matters is setting the stage for the session!"
    mo "Since Ram has not yet become an official member of the party and I’d feel bad about playing out most of the session without her, we’ll start our day off at a local tavern and maaaaaaybe introduce her there!"
    a "Should I hang out in the back? The last time we went to a tavern was kind of strange for me..."
    ay "Never fear, Arborea! Lidearel’s got your back!"
    ay "For a price..."
    mo "Silence!"

    scene thirdthaum1
    with dissolve

    mo "The smell of cheap wine and old ale assaults your senses as you push through the doors of the local tavern in Pyredale."
    mo "You know through the means of Urrheak’s divination that there exists a merchant in this town capable of providing {i}something{/i} that will aid you in your coming journey."
    mo "What that is or where the merchant is located remains to be seen, but a lingering feeling in the pit of the aarakocra’s...birdlike stomach tells you you’re on the right track."
    mo "But...just as the doors swing open, the merrymaking and music comes to a stop. "
    mo "All eyes turn to you, the band of mismatched individuals wandering into somewhere you clearly don’t belong...and you feel threatened."
    mo "But before you’re able to act in response to this, a large, cloaked man stands up from the bar and raises a hand in the air."

    scene thirdthaum6
    with dissolve

    mo "{i}Ahh. I was beginning to think you had no intention of showing up.{/i}"

    scene thirdthaum7
    with dissolve

    mo "His voice is deep. Deep enough that the bass crawls into your stomach and churns your insides. "
    mo "And even though he speaks in just one voice, you can feel as if there are many more...seemingly overlaying one another as if they’re a melody of barely intelligible, aberrant noises."

    scene thirdthaum6
    with dissolve

    mo "{i}All I want is to sleep....{/i}"
    r "Mood."
    mo "{i}All I want is to dream...{/i}"
    mo "{i}And yet I awaken.{/i}"
    mo "{i}Why?...{/i}"

    play sound "thump.mp3"
    scene thirdthaum8
    with hpunch

    mo "{i}Why?!{/i}"
    mo "He SLAMS his glass on the table, causing it to shatter and spill cheap ale all over the counter. But no one pays it any mind."
    mo "{i}Why do you make me wait?!{/i}"

    scene thirdthaum1
    with dissolve

    mo "…"
    r "Oh. Is he done?"
    mo "He is done. How do you respond?"

    scene thirdthaum9
    with dissolve

    r "Umm...uhh...{i}Hey...guy!{/i}"
    r "{i}It’s bad manners to go spilling your beer on...bars and stuff.{/i}"
    mo "The cloaked man does not respond. You can’t make out his face as it’s concealed by a hood, but you have a sinking feeling that he’s staring at someone."

    scene thirdthaum10
    with dissolve

    a "Oh no. It’s gonna be me again. I know it."
    a "We never even found out why that last person freaked out on me because she went and turned into a mushroom."
    a "Molly, I’m tired of fighting mushrooms. Is there some kind of roll I can do to make this...cloaked guy go away?"
    mo "I mean...you can try rolling for persuasion or intimidation or something...but I will tell you now that he is not going away."
    a "…"
    a "Then..."
    a "Then why would I roll?"

    scene thirdthaum11
    with dissolve

    ay "Sensing the hostility growing in the room, Lidearel reaches for her daggers...not unsheathing them, but making the cloaked guy know that she’s down to clown if he is."
    f "Xessaxia sees Lidearel readying for combat and reaches toward her quiver at the same time, stomping one of her hooves and wrapping her fingers around an arrow."

    scene thirdthaum12
    with hpunch

    sa "AAAAAAAAAAAAAAHHHHHHH!!!"

    scene thirdthaum13
    with dissolve

    sa "Zagull just yells."

    scene thirdthaum14
    with dissolve

    mo "Are you like...trying to communicate something with that yell? Or..."
    sa "Just..."
    sa "Just yelling..."
    mo "Right..."
    mo "Well, anyway...the man does not respond."

    scene thirdthaum15
    with dissolve

    mo "Instead, he lifts his hand once again and snaps his fingers."
    mo "You can feel the air in the room change in an instant."
    mo "But apart from the changing of the air, you can {i}also{/i} feel an increase in the amount of magic flowing into the room."
    mo "Then, right before your very eyes, the glass he had shattered just moments earlier begins to reform and refill with liquid."

    scene thirdthaum16
    with dissolve

    r "Nithhala takes one look at the glass as it’s filling up and decides to take a step forward."
    mo "Step forward and do what? If it’s just a step, he doesn’t react."
    r "I have darkvision, right? Can I use that to see inside of his hood."
    mo "That is not how darkvision works, Nithhala."
    r "Well then why the hell did I take it?"
    mo "You didn’t take it. It’s something you automatically have as a tiefling."
    r "I automatically have lungs and hands and stuff too but those aren’t written on my sheet. They’ve been a hell of a lot better than darkvision, I’ll tell you that much."
    mo "Is anyone {i}actually{/i} going to do something or do we want to use this time to complain about more of our racials?"

    scene thirdthaum17
    with dissolve

    m "Urrheak would like to do something."
    mo "And what would Urrheak like to do?"
    m "Urrheak gestures to his companions to stop reaching for their weapons and raises his...badass arm-wing things into the air."
    m "But he does it in a showy kind of way. Not an intimidating one."
    mo "Like a...mating dance?"
    t "Noodles, close your eyes."
    noodles "Caw!"
    m "Not really what I had in mind. But I’ll just speak to him as well. "
    m "Also, it's going to be in aarakocra and not common."
    mo "Sure. Go ahead."

    scene thirdthaum18
    with dissolve

    m "{i}We’re not here to fight...but we don’t know who you are either.{/i}"
    m "{i}If you’d be so kind as to introduce yourself to us, perhaps we can avoid bloodshed altogether and come to...some sort of understanding.{/i}"
    m "{i}My friends and I are looking for something to assist in the creation of a tunnel. A tunnel to-{/i}"

    scene thirdthaum19
    with dissolve

    mo "The man raises his hand in the air once more before Urrheak can finish his sentence. "
    a "Wait, if Urrheak was speaking aarakocra, how come I could understand it?"
    mo "Shut up, Ami. "
    mo "The man raises his hand in the air and looks into Urrheak’s eyes. And despite clearly not being a bird, he speaks in aarakocra back to him."
    mo "{i}One snap of the fingers...{/i}"
    mo "{i}One snap to rewrite tiny bits and pieces of history.{/i}"
    mo "{i}But perhaps you already know this, [young]one.{/i}"
    m "I’m not that young. I’m canonically-"
    mo "{i}You’re all [young]to me.{/i}"
    mo "{i}But that doesn’t mean we can’t reach some sort of understanding...{/i}"

    scene thirdthaum20
    with dissolve

    mo "He snaps his fingers again and disperses into thin air. But from out of the smoke emerges a lanky woman dressed as a clown."
    mo "Clasping a lute in her hands, she begins to play you all a song..."
    t "Yo yo yo. My name is Ram."
    t "I have two legs and I like ham."
    t "We’re in a tavern...at a place."
    t "I have two legs. I have a face."
    mo "She is not a very good bard."
    mo "But you still all get a point of inspiration because, for some strange reason, you like the song a lot and now Ram is a part of your party."
    t "Sup."

    scene thirdthaum21
    with dissolve

    ay "Wait, just like that?"
    ay "Lidearel isn’t going to accept that the weird cloak guy just vanished and got replaced by some girl dressed like a clown who can’t rap her way out of a paper bag."
    ay "And I’m allowed to say that because I finished second place in the first annual Super Mega Ultimate Dorm War."
    f "There were...only two contestants..."
    f "But...I agree. Xessaxia would also take issue with this."

    scene thirdthaum22
    with hpunch

    sa "AAAAAAAAHHHHH!!!!!"

    scene thirdthaum23
    with dissolve

    sa "Zagull yells again."
    ay "…"
    f "…"

    scene thirdthaum24
    with dissolve

    sa "…"
    sa "What?"

    scene thirdthaum25
    with dissolve

    mo "Hah..."
    mo "Of course you’re all free to ask Ram any questions you have. Tsuneyo and I spent a fair deal of time going over her backstory, so she’ll know the answers to mostly everything."
    mo "Though, it’s still up to her to decide whether or not she wants to share any of that information with you."
    r "Then, uhh..."
    r "{i}Where do you come from? And what happened to the hot guy in the cloak?{/i}"
    a "{i}Nithhala, you couldn’t even see his face.{/i}"
    r "{i}Oh right. Because darkvision SUCKS!{/i}"
    t "{i}I don’t know. I just woke up here.{/i}"
    ay "{i}That’s unacceptable and you know it!{/i}"

    scene thirdthaum26
    with dissolve

    t "{i}Sorry...but I really don’t know.{/i}"
    ay "{i}Fine...if you want to play things that way, then get ready to-{/i}"
    f "{i}Lidearel, wait!{/i}"
    f "{i}It’s highly probable that she really did wake up just now...{/i}"
    f "{i}We can’t factor out the possibility that she’s under some sort of spell or-{/i}"
    ay "{i}We don’t have time for this, X...Xesa...{/i}"
    ay "{i}Alicia!{/i}"
    f "{i}...{/i}"
    f "Xessaxia slaps Lidearel."

    scene thirdthaum27
    with dissolve

    mo "Roll to hit."
    ay "Hey, wait!"

    play sound "dice.wav"

    f "25."
    mo "Lidearel takes three points of damage."
    ay "Don’t I get an opportunity to counter this?!"

    play sound "slidedoor.mp3"
    scene thirdthaum28
    with fade

    r "Ah! Girl!"
    o "Uhh...excuse us."
    o "Noriko and I were just walking down the hall when we heard you guys in here and...it sounded like you were having a lot of fun."
    o "Are you playing D&D?"
    r "No!"
    r "Yes!"
    r "We’re playing a game! Games are fun!"
    r "Right, Sana?! Tell her games are fun!"
    sa "Games...are fun?"

    scene thirdthaum29
    with dissolve

    o "Are you going to be much longer?"
    o "I thought we could maybe hang out tonight if you’re not doing anything."
    r "HAHAH! GAMES ARE SO FUN! RIGHT, SANA?!"
    sa "Um...what?..."

    scene thirdthaum30
    with dissolve

    m "Move your feet."
    n "Hm?"

    scene thirdthaum31
    with dissolve
    stop music fadeout 60.0

    n "What was that, Maya? My hearing isn't that great."
    m "I said move your fucking feet. That’s my futon you’re stepping all over."
    a "Maya! She didn’t know. There’s no reason to freak out on her for it."
    t "Perhaps I should do my second rap to lighten the mood."
    t "My name is Ram and I’m here to say-"
    a "Not now, Tsuneyo."
    t "You’re right. We already have a point of the inspiration."

    scene thirdthaum32
    with dissolve

    n "Are you actually sleeping out here?"
    m "Of course I am. Where else would-"
    n "You know exactly where else you’d be sleeping."

    scene thirdthaum33
    with dissolve

    n "But, sure! I’ll get off of your futon."
    n "I was actually just about to leave anyway."
    o "You were?"
    n "I guess so."
    n "We can hang some other time, Otoha."

    play sound "slidedoor.mp3"
    scene thirdthaum34
    with fade

    r "Girl! Still here!"
    r "Can’t feel legs!"
    o "Umm...well, now that I am apparently all alone..."

    scene thirdthaum35
    with dissolve

    o "Can I play too?"
    r "You mean...play game?"
    o "I think so."
    r "Yes."
    r "You play game with Rin."
    o "Why are you suddenly a caveman?"
    r "Doesn’t matter!"
    r "Also, please forgive me for anything extremely embarrassing I say tonight! "
    o "I can play then?"
    o "It’ll be my first time, so I don’t really know-"

    play sound "static.mp3"
    scene thirdthaum36 with flash
    stop sound
    stop music

    mo "No."
    r "Wait...what? "
    r "Why not?"
    mo "Because it’s my campaign and I said no."
    mo "We’re already in the middle of a session. We don’t have time for a new player."
    r "But...Tsuneyo is new and-"

    play sound "static.mp3"
    scene thirdthaum37 with flash
    stop sound

    mo "I said no."
    mo "What part of that don’t you understand?"

    play sound "static.mp3"
    scene thirdthaum38 with flash
    stop sound
    play music "andlove.mp3"

    r "...Molly?"
    o "Oh. I'm...uhh...sorry?"
    o "I wasn't trying to get in the way."
    o "Like...I get it. It’s your game."
    o "My bad, Molly."
    r "Molly, what the hell?"
    mo "Anyway, what’s going to be your party’s next move? You could either try probing Ram for more information about where she came from or follow the trail of Urrheak’s divination-"
    r "No, hold on. Why can’t Otoha play?"
    mo "Does Otoha even like D&D?"
    o "I’ve...never played before."
    mo "See? It would be too much effort just working her in right now. "
    mo "Besides, we’re already a little behind schedule and-"
    r "You really can’t do this for me?"
    mo "For you?"
    r "Yeah..."
    r "I’m asking you as your {i}friend{/i} to do this {i}for me{/i}."
    mo "And I can’t ask you to drop it {i}for me?{/i}"

    scene thirdthaum39
    with dissolve

    o "Rin, it’s no big deal. I'll just watch."
    r "I just don’t get why {i}Molly{/i} can bring in a new player and I can’t."
    r "Especially when no one else would have a problem with it."
    sa "I’m...um..."
    sa "I’m fine with...waiting a little longer if Otoha wants to play..."
    f "We don’t have anywhere to be tomorrow...we could always stay up a little later?"
    a "Yeah! I’ll help you make her sheet if you think that’s what going to take the longest, Molly."
    m "Doesn’t Molly have several extra character sheets in her binder? Otoha could just use-"
    mo "No."

    scene thirdthaum40
    with dissolve

    o "…"
    r "Do you..."
    r "Molly, do you like...have some sort of problem with Otoha?"
    mo "Of course not. I just don’t want to sidetrack the game I spent hours and hours and hours working on to accommodate someone who’s only playing because {i}you’re{/i} here."

    scene thirdthaum41
    with dissolve

    r "What the hell is that supposed to mean?"
    mo "I said no and that’s final."
    mo "Now, we were just about to leave the tavern and-"
    r "We were {i}just about{/i} to help Otoha make a fucking-"

    play sound "static.mp3"
    scene thirdthaum42 with flash
    stop sound

    mo "We..."
    mo "We were not helping her do anything!"
    mo "We were going to go on a fun adventure as a party! "
    mo "I had tons of stuff lined up for tonight that I’d have to completely rebalance if we brought on {i}another{/i} extra person!"
    mo "Why is that so hard for you to understand?!"
    t "Emerald Guardian. I think you have popped one too many cooldowns."
    o "Did I like...do something to offend you, Molly?"

    scene thirdthaum43
    with dissolve

    mo "You..."
    mo "Hahaha..."
    mo "You don’t even know..."

    scene thirdthaum44
    with dissolve

    mo "You don’t even know what you did!"
    mo "You just wandered in here thinking...thinking that you own the place! And that everybody likes you!"
    mo "Well...you’re just..."
    mo "You’re not all that great! You’d never be able to set up a campaign like this! Create...branching paths and...innovative boss fights!"
    r "What are you doing?..."

    scene thirdthaum45
    with dissolve

    mo "And...and you can’t watch either! You got that?!"
    t "Balance in all things, Emerald Guardian. Remember your path."
    t "You are giving into the darkness."
    r "Molly..."
    r "Apologize."
    r "Right now."
    mo "For what?! Standing up for myself?! For...finally doing something for {i}me{/i}?!"
    mo "I’ve been looking forward to this {i}one thing{/i} for so long! I don’t want it to be ruined just cause..."

    scene thirdthaum46
    with dissolve

    mo "Just..."
    mo "Just cause..."

    scene thirdthaum47
    with dissolve

    mo "Just...cause..."
    o "…"
    mo "You’re not any better than me..."
    mo "You’re..."

    play sound "static.mp3"
    scene thirdthaum48
    with flash
    with hpunch
    stop sound

    mo "AAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!"

    play sound "static.mp3"
    scene thirdthaum49 with flash
    stop sound

    "Run away!"
    "Free yourself from discomfort by pretending it does not exist!"
    "Face your fears and brace for failure because, more times than not, things will turn out horrible!"
    "And when they turn out horrible, cry!"
    "Savor the warmth of your tears as they race down your cheeks, for their existence is the only warmth you deserve!"
    "Break yourself to build yourself back up!"
    "Do it over and over again!"
    "Run out of chances!"
    "Run out of everything!"
    "Run! Run! Run!"

    play sound "static.mp3"
    scene thirdthaum50 with flash
    stop sound

    r "Un-fucking-real."
    ay "I’m gonna go chase after her. I’ll be right back."

    play sound "slidedoor.mp3"

    f "Molly..."
    a "What...was that all about?"
    r "Who cares? If she’s going to be a bitch to people, she should get treated like a bitch back."
    r "Otoha did literally nothing wrong. All she did was ask to play and Molly decided to fucking explode."
    o "…"
    t "I have never witnessed her act in such a way before."
    a "Maya...did you want to chase after her as well?"
    m "…"
    m "No. "
    m "Whatever it is, I doubt there’s anything I can do about it."
    sa "I..."
    sa "I don’t even...really know what-"
    r "Don’t bother, Sana. "
    r "I highly doubt it’s anything worth actually chasing after her for."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ secondbeach8 = True

    "{i}Welcome to Lessons in Love!{/i}"

    if bonus == True:
        "{i}In Lessons in Love, you can trade in affection points for blowjobs.{/i}"
    else:
        "{i}In Lessons in Love, you can trade in affection points for hugs.{/i}"

    "{i}Also, girls cry a lot.{/i}"
    "{i}It’s really sad.{/i}"
    "{i}Let’s go help one feel better!{/i}"

    play sound "static.mp3"
    scene gamemenumin with flash
    stop sound

    "{i}Click the button to make Molly feel better!{/i}"

    menu:
        "Button":
            play sound "static.mp3"
            scene ayhh3 with flash
            scene ayhh14 with flash
            scene ayhh7 with flash
            scene ayhh1 with flash
            scene ayhh2 with flash
            scene mollybuthappier1 with flash
            stop sound

    "Lavender's blue, dilly, dilly "
    "Lavender's green "
    "When I am king, dilly, dilly "
    "You shall be queen"

    play sound "static.mp3"
    scene tree1 with flash
    scene tree2 with flash
    scene tree3 with flash
    scene treefall1 with flash
    scene mollybuthappier2 with flash
    stop sound

    "Who told you so, dilly, dilly "
    "Who told you so? "
    "'Twas my own heart, dilly, dilly "
    "That told me so."

    play sound "static.mp3"
    scene whygodwhy with flash
    scene whyme with flash
    scene whythesky with flash
    scene u with flash
    scene mollybuthappier3 with flash
    stop sound

    "Lavender's green, dilly, dilly "
    "Lavender's blue "
    "If you love me, dilly, dilly "
    "I will love you"

    "{i}Click the button once more!{/i}"

    menu:
        "Button":
            scene lessons
            stop music
            $ renpy.pause(10, hard=True)

            $ molly_love += 1

            "{i}Molly’s affection has increased to [molly_love]!{/i}"

            scene black

            "………"
            "……"
            "…"

            jump secondbeach9

label secondbeach9:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
u "Oh...crap. I’m sorry."
    u "This is what I get for choosing two conversation topics in a row, isn’t it?"
    i "You’ve got Touka, though, right?"
    i "I’m sure that she’s probably asked you something similar in the past. You two are basically attached at the hip, aren't you?"
    ya "I suppose that Touka is like a mother to me."
    i "Not really what I was going for, but sure. Let’s run with that."

    scene utaiobeach22
    with dissolve

    ya "She is a good person."
    ya "Pure of heart and mind."

    if bonus == True:
        ya "A true virgin both physically and spiritually."
    else:
        ya "(Airplane noises)"

    i "Uta, change the topic again."
    u "Are you kidding? I wanna see where this goes."
    ya "A person like her would be better suited for this conversation."
    ya "She possesses both the freedom of thought and an unearthly desire to belong. To love and to be loved."
    ya "I possess none of that."
    ya "I am a vessel. Incapable of feeling or wanting those things."
    ya "Existing for the sole purpose of filling myself with light and pouring it over the heads of those willing to be drenched in His love."
    ya "Slipping silently into sermons, scalding each surrounding servant with seed stripped from sinful serpents."
    ya "Singeing the skin of those sleeping in shadows by singing the praises of the smile in the sky."
    ya "These are the reasons I exist."
    ya "Not to love. Not to feel. Not to want."
    ya "But to be. And become."
    ya "And to save. And to be saved."
    ya "All I want is for the world to smile together, all at once."
    ya "That is all He wants as well."
    ya "But there is so much darkness. "
    ya "And not just in the world itself, but in everyone."
    ya "In each of you."
    ya "It will swallow you whole, you know. "
    ya "Maybe not now. Maybe not tomorrow."
    ya "But there will come a time when you are forced to face what you fear the most."
    ya "And when that time comes, I will be right around the corner- with open arms and a sanctuary for you to lose yourself in when you think there’s nothing {i}left{/i} to lose."
    u "…"
    i "…"
    ya "…"

    scene utaiobeach23
    with dissolve

    ya "I’m sorry. What was the question again?"
    u "We..."
    u "We just wanted to know what you thought about love."
    ya "I see."
    u "…"
    i "…"
    ya "…"

    scene utaiobeach22
    with dissolve

    ya "I think love is lovely."

    scene black
    with dissolve2

    "Three girls in a line on the beach."
    "One callous-"
    "And two others."
    "But is there truly an issue with callousness in and of itself?"
    "And couldn’t such an adjective change based on your perception of it?"
    "If you want my opinion, the answer is yes."
    "My opinion is that everything can change. And that everyone’s thoughts can be changed if you try hard enough to actually change them."
    "And so I say to Io Ichimonji, the girl who thinks no one can change, that you are weak."
    "And I say to Uta Ushibori, the girl who doesn’t want to think at all, that you, too, are weak."
    "And to the girl {s}in the black dress{/s} in the[school] swimsuit-"
    "You are the weakest of all."
    "But for reasons quite different than that of the others."
    "The three girls run into the water and never return."
    "And I fall back into place in the midst of the water cycle, for the storm clouds have drifted slightly off course."
    "Everything is ephemeral."
    "Everything is falling."

    scene everythingg
    with dissolve4
    stop music
    play sound "static.mp3"
    scene everythingg2 with flash
    scene everythingg3 with flash
    scene everythingg4 with flash
    scene everythingg5 with flash
    scene everythingg6 with flash
    scene everythingg7 with flash
    scene everythingg8 with flash
    scene black
    stop sound

    $ renpy.end_replay()
    $ secondbeach7 = True

    "{i}Affection!{/i}"

    jump secondbeach8
...
```