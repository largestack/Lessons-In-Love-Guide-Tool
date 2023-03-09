# Beautiful Porn Salesman
Maki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makidate1&go=Go)



## Event preconditions
✅Maki love greater than or equal to 0

✅Event "[Molly: NTR & Pregnancy](./mollycafe1.md)" is completed (event=mollycafe1)

✅makinumber equal to True (unknown variable)



## Next events
* [Sana: Life is a Tomato](./bar25.md)
* [Makoto: Residual Sadness](./makotodorm20.md)
* [Maki: Maki Miyamura's Mom-Mode Mission](./makidate5.md)

## Event properties
* ID: makidate1
* Group: Maki
* Triggered by label: callmakinight
* Triggered by branch label: callnight

## Event code
File: \game\MakiEvents.rpy
Code:
```python
...
label makidate1:
    "Maybe I’ll give Makoto’s mother a call?"
    "Under most pretenses, I probably wouldn’t make my first call to someone I barely know just before nightfall, but she tends to work late anyway so maybe she’s used to it?"
    "Besides, Makoto is pretty much always at the shop anyway and this might give me a good opportunity to be alone with her."

    play sound "phonebeep.wav"

    "I tap on Maki’s name in my phone and listen to it ring a few times, hoping she picks up."
    "………"
    "……"

    play sound "phonebeep.wav"

    maki "Hello? "
    s "Hey, Maki? This is your daughter’s teacher."
    maki "Oh, hey!"
    maki "Normally, people introduce themselves by their name and not their job over the phone."

    "Normally, people {i}know{/i} their name to begin with."

    s "Sorry about that."
    maki "No need to apologize. I just don't know what to call you."
    s "Just Sensei is fine."
    maki "Hmm...Okay, okay. But if you get to go by your job, I want to as well."
    s "You want me to call you...porn salesman?"
    maki "Beautiful porn salesman preferably, but sure."
    s "I’ll see if I can remember that."
    maki "So what’s up? Why are you calling so late?"
    maki "Did something happen with Makoto?"
    s "Nothing in particular. I just wanted to see if you’d like to meet up for coffee or something."
    maki "...Coffee?"
    s "Yeah. It’s that brown stuff tired people drink."
    maki "Sensei, are you asking a married woman out on a date right now?"
    s "…"
    maki "…"
    s "Yes."
    s "Yes, I suppose I am."
    maki "Hah! Well at least you’re up front about it."
    maki "I can probably slip away for a little while if you want to meet up at Koi Cafe."
    s "Yeah, that works for me. I’ll start heading over now."
    maki "Same here. I’ll see you soon."

    play sound "phonebeep.wav"

    "Well...She just seems full of energy."
    "I have to admit, I saw that call ending a little differently once she brought out the “married woman” line."
    "But I guess it’s not really my place to question her relationship."
    "I’ll just head over to the cafe and wait for her to get there."

    scene black
    with dissolve
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    scene mollycafe1
    with dissolve
    play music "justbehappy.mp3" fadein 6.0

    mo "Welcome to Good Burger, home of the Good Burger. Can I take your order?"
    s "...What?"
    mo "It’s a thing. Don’t ask questions."
    s "Sure, Molly."
    s "Can I just get a black coffee? I’m meeting someone here in a few minutes."

    scene mollycafe18
    with dissolve

    mo "Meeting someone? Like...on a date thingy?"
    s "Uhh, I guess so."
    s "It’s just Makoto’s mom."
    mo "Makoto? Like, glasses Makoto? The Witch of the West Wind?"
    s "You gave her a nickname too?..."

    scene mollycafe1
    with dissolve

    mo "Of course! And I’ll do my best to not disrupt your date thingy!"
    mo "As a fellow degenerate, I know just how hard it can be finding love in this day and age. I’m cheering for you, Sir!"
    s "Really? I kind of saw this going a little differently."
    mo "No, no! Not at all! Go sit down in the corner! I’ll even bring over something special once she gets here."
    s "That’s really considerate of you, Molly. Thanks."

    scene makifirstdate1
    with fade

    "I take a seat near the back wall and wait for Maki to arrive. "
    "I wonder what sort of “special” thing Molly is going to bring over once the time comes?"
    "I hope it’s not anything explosive."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene makifirstdate2
    with dissolve

    if bonus == True:
        maki "Hey. Sorry it took me so long. Makoto had a question about blowjobs that I needed to answer."
    else:
        maki "Hey. Sorry it took me so long. I was continuously running into the wall in hopes that all of its atoms aligned at the perfect time, allowing me to pass through it."

    s "That’s probably the strangest intro to a date I’ve ever had the pleasure of hearing. "

    scene makifirstdate3
    with dissolve

    maki "Such is the life of the newly proclaimed “Beautiful Porn Salesman.”"
    s "Oh, right. I forgot that was your nickname now."
    maki "Don’t worry. So did I until five seconds ago."

    scene makifirstdate4
    with dissolve

    maki "Which is also right around the time that I became acutely aware that I’m still wearing my tracksuit."

    scene makifirstdate3
    with dissolve

    maki "You don’t mind, do you? "
    s "Not at all. If anything, I think it even accentuates your beauty."

    scene makifirstdate5
    with dissolve

    maki "Yeah, they {i}do{/i} look pretty nice in this, don’t they?"
    maki "Most people beat around the bush when they say that, though."

    scene makifirstdate6
    with dissolve

    maki "Heh. Bush."

    "Is Makoto really related to this woman?"

    scene makifirstdate2
    with dissolve

    maki "But anyway, thanks for calling me and blah blah blah. It’s not often I get out anymore, which I’m sure you’re able to tell by the get-up."

    scene makifirstdate7
    with dissolve

    maki "Oh how I have longed for the days to go out and enjoy my youth once again."
    maki "The life of a parent is truly a rough one."
    s "I can imagine. Makoto’s a good girl, though. At least she makes it easy on you."

    scene makifirstdate3
    with dissolve

    maki "She does now. But she was miserable as a kid. It was always “I want this. I want that. Buy me an encyclopedia.”"

    scene makifirstdate7
    with dissolve

    maki "I mean, really? What kind of five year old wants an encyclopedia for their birthday? Ask for a pony or something. Jeez."
    s "Wow. She was like that back then, too?"

    scene makifirstdate2
    with dissolve

    maki "Oh yeah. Big time. But hey, at least she’s consistent. Right?"
    maki "And she’s smarter than both her father and me now, so I can’t help but be proud of her."

    scene makifirstdate3
    with dissolve

    maki "High maintenance or not, she’ll always be my little girl."

    scene makifirstdate8
    with dissolve

    mo "…"
    maki "…"

    "Molly shows up at the table and places a normal cup of coffee in front of Maki."
    "How is this, in any way, special?"

    scene makifirstdate9
    with dissolve

    maki "That’s strange. I just felt the atmosphere in here change a little."
    maki "It feels...darker in some way."
    s "Well, that’s..."
    maki "…"
    mo "…"
    maki "Someone is giving me the death-stare, aren’t they?"
    s "Yeah. I think that might be my fault."
    mo "Clíodhna, beseech unto me a fraction of your beauty so that I may leave this harlot in the grimy waters of Glandore to {i}drown{/i}."

    scene makifirstdate10
    with dissolve

    maki "Uhh, hello there."
    s "Molly, please tell me that the coffee you brought to the table isn't poisoned."
    mo "What do you think you're doing here?"
    maki "Umm...Have I done something to offend you?"
    mo "State your name and occupation, harlot."
    maki "Maki Miyamura. Beautiful porn salesman."
    mo "And what exactly is it you intend to do with my master, {i}Maki Miyamura{/i}?"
    maki "Master?..."

    scene makifirstdate11
    with dissolve

    if bonus == True:
        maki "Isn’t she a little young?..."
        s "Not that kind of master, Maki..."

        "Though, I wouldn’t exactly complain if that were the case..."
    else:
        s "I am a ninja and I am teaching Molly how to be a ninja as well."
        maki "Wow, you're so cool."
        s "I know."

    scene makifirstdate12
    with dissolve

    maki "The two of us were just having some coffee. It’s an entirely wholesome meeting and you’re welcome to join us if you’d like."
    mo "I’m afraid I can not. Your aura is suffocating me. "

    scene makifirstdate11
    with dissolve

    maki "{i}I think this girl might like you.{/i}"
    s "I don’t think she’s into actual humans, to tell you the truth."

    scene makifirstdate13
    with dissolve

    if bonus == True:
        maki "Ahh...A hentai fan then?"

        scene makifirstdate14
        with dissolve

        mo "L-Leave my fetishes out of this, devil-woman!"
        maki "Tell me, child, what kind of hentai are you into? Vanilla? Tentacles? {i}NTR?{/i}"

        scene makifirstdate15
        with dissolve

        mo "I hate NTR! Don’t even get me started!"
        maki "Hmmm...I see, I see. So you approached this table because you’re afraid that I’m going to get to your {i}master{/i} before you. Is that it?"
    else:
        maki "Never fear. My husband also prefers other types of life forms. There is nothing wrong with it."

    scene makifirstdate16
    with dissolve

    mo "You have horrible taste in women, Sir."
    mo "This is clearly a succubus and you’ve just been lured into her trap. "
    mo "It is the only possible explanation."
    mo "But do not fear. I shall protect you."

    scene makifirstdate17
    with dissolve

    if bonus == True:
        maki "Though...I suppose I wouldn’t mind sharing him with you as long as he’s okay with it."
        s "Definitely okay with it."
        mo "Sh...Sharing...him?"

        scene makifirstdate18
        with dissolve

        maki "Of course, my dear. Real succubi like myself can thrive off the energy of both males and females alike."
        maki "Would you like me to show you how?..."

        scene makifirstdate19
        with dissolve

        mo "A threesome with Master and a succubus?..."
        mo "Perhaps...something like this would strengthen our bond?..."
        s "…"
        maki "…"

        scene makifirstdate18
        with dissolve

        mo "Will you leave us enough life essence to live our lives normally afterward? Or do you plan on taking everything?"
        maki "{i}Everything.{/i}"
        maki "But I’ll make it worth your while. I promise."
        s "Maki, it’s probably not healthy to go along with this. Molly tends to believe pretty much anything she-"
    else:
        maki "Hey, do you ever stare into the mirror for so long that it starts to look like all of your skin is detaching and floating somewhere else?"
        s "Maki, are you on drugs?"
        maki "What? Who is Maki? Where am I?"

    scene makifirstdate20
    with dissolve

    if bonus == True:
        mo "I’ll do it!"
        mo "I-I don’t know much about pleasing women...But I have played several yuri games and I’m sure I could figure it out!"
        maki "Leave the ‘pleasing’ to me, dear. You just sit back and relax..."
    else:
        maki "Are you my daughter?"
        mo "Ah!"
        s "Maki, stop. You are scaring the employees."
        maki "There is money for you in my purse."
        mo "Where...is your purse?"
        maki "Over there. Go get it."

    scene makifirstdate21
    with dissolve

    mo "AAAAHHH!"
    mo "I’LL BE RIGHT BACK!"

    scene makifirstdate22
    with dissolve

    if bonus == True:
        "Molly quickly sprints into the back room and I can hear a few things being knocked over in the process."
        "The poor girl is probably having a heart attack as we speak."
    else:
        "Molly nervously runs away and Maki refocuses her attention on me."

    scene makifirstdate23
    with fade

    s "You’re kind of terrifying."
    maki "Yeah. I kind of am."
    maki "Years and years of experience. I’m pretty good at figuring out what will set people off."

    scene makifirstdate25
    with dissolve

    if bonus == True:
        maki "I’m sure you know I don’t really plan on having a threesome with you two, though. Right?"
        s "..."

        "Damnit."

        maki "Heheh~ Sorry, Sensei. I don’t think my daughter would be very happy with me if I did that kind of stuff with one of her classmates."
        maki "Her {i}teacher{/i} on the other hand..."

        "Woah. Am I already in the clear?"
        "Was that husband thing from earlier just a bluff?"
    else:
        s "I feel like skirting the line betweeen dementia and drug addiction is enough to set most people off."
        maki "Yeah, well, I'm a free woman and I can do whatever I want."

    s "Not like it matters to me but...aren’t you married?"

    scene makifirstdate23
    with dissolve

    maki "I am. But it’s one of those “open relationship” deals. "

    if bonus == True:
        maki "I’m sure my husband is out there in space impregnating an alien-girl as we speak."
        s "Is that even possible?"
    else:
        maki "I’m sure my husband is out there in space hugging an alien-girl as we speak."
        s "Is that even possible? Have we confirmed that they have arms?"

    maki "I don’t know. But he’s a smart man. I’m sure he’ll find a way."
    maki "I hear the economy is pretty horrible in space, too. Child support will probably only be a few dollars a month."
    s "What is this conversation turning into?"

    scene makifirstdate25
    with dissolve

    maki "Hey, {i}you’re{/i} the one who brought up my marriage. I’m just trying to explain the situation to you."
    s "Does Makoto know about the situation?"

    scene makifirstdate24
    with dissolve

    maki "She...prefers not talking about things like that. "
    maki "And besides, even though it’s an open relationship, it’s not like I’m passing myself around. "

    scene makifirstdate25
    with dissolve

    maki "Believe it or not, I don’t really have many friends and-"
    s "Yeah, I believe that."

    scene makifirstdate26
    with dissolve

    maki "Wait, what? Why did you believe that so easily?"
    s "Just the vibe you give off. "
    s "It’s like a mix between shut-in, mega-deviant, and doting mother. It’s a strange combination and I can’t imagine it makes it easy to meet people or retain friendships."

    scene makifirstdate27
    with dissolve

    maki "Yup. Pretty much hit the nail on the head with that one."

    scene makifirstdate28
    with dissolve

    maki "It’s fine, though. If sexual feelings happen, they happen. I’m just not the type to go out and actively search for them with anyone."
    maki "Despite working in a porn shop, I could pretty much live without sex if I wanted to."

    scene makifirstdate25
    with dissolve

    maki "Obviously doesn’t mean I don’t enjoy it, though. "
    s "Well that’s...good news?"

    "I’m not really sure how to respond to Maki right now. "
    "This conversation is walking a fine line between serious and flirty, and it’s sort of putting me on the back foot."
    "But it’s not like I have a time limit or anything."
    "I’m sure if the two of us just keep hanging out like this, things are bound to happen eventually."
    "I just need to make sure Makoto doesn’t find out about it."

    scene makifirstdate28
    with dissolve

    maki "So, do you think the red-haired girl is doing okay?"
    maki "She’s been in the back for a while now."
    s "Molly? I’m sure she’s fine. Just a little worked up."

    scene makifirstdate25
    with dissolve

    maki "Sure you don’t want to go check on her?"
    s "There are several reasons that I don’t think that would be a good idea right now."
    s "Let’s just finish drinking our coffee and head out."
    maki "Hahah~ If that’s what you want, sure."

    scene black
    with dissolve2

    "And then, the two of us do just that."
    "We sit there like civilized adults, sipping coffee and talking about our respective outlooks and interests."
    "Maki talks much more than I do. "
    "I just relax and take in as much information as she’s willing to give me."
    "I’m sure it will come in handy eventually..."

    $ renpy.end_replay()
    $ maki_love += 1
    $ makidate1 = True
    stop music fadeout 5.0

    "{i}Maki’s affection has increased to [maki_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makidate5:
...
```

## Code that triggers this event
File: \game\MakiEvents.rpy
Code:
```python
...
label callmakinight:
    if makiblock == True:
        "I don't really think I should call Maki right now..."
        jump callnight
    if maki_love >= 0 and mollycafe1 == True and makidate1 == False:
        jump makidate1
...
```