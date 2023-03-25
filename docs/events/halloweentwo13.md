# Metal in Microwaves (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Gallows Edge](./halloweentwo12.md)

## Event preconditions

* bonus equal to False (unknown variable)



## Next events

* [Maki: Traveling Lube Dealer](./makiinvite1.md)
* [Maki: Special Occasions](./makiinvite2.md)
* [Maki: Baby Steps](./makiinv3.md)
* [Noriko: Fair & Square](./norikospecial20.md)

## Event properties

* Id: halloweentwo13
* Group: Main
* Triggered by label: halloweentwo12
* Chain sources: halloweentwo12
* Chain sources path: halloweentwo12

## Official wiki page

[Metal in Microwaves](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo13&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label halloweentwo13:
    play music "sensei.mp3"

    "What did you want to be when you were younger?"
    "I bet it was something silly, like an astronaut."
    "That didn’t turn out all too well, though...did it?"
    "Now, the days tick on like the smallest hand of an analog clock- passing over line after line because you’ve seen them so many times that they’re just not exciting enough to make you stop anymore."
    "Everything today is exactly the same as it was yesterday."
    "You wind yourself up and go around in circles."
    "You know you’re not heading anywhere in particular, but that’s never stopped you before."
    "Because you know deep within your heart that you determine how everything else moves."
    "If you don’t do your job, the more important cogs in the machine won’t be able to do theirs."
    "Move faster!"
    "Move quicker!"
    "The world stops existing the second you believe it to not exist!"
    "Don’t let all of it die!"
    "We’re all built around you!"
    "{i}It’s{/i} all built around you..."
    "Why, in this room full of things designed to make you happy, do you still struggle to find your place?"
    "Why do you refuse to grow?"
    "Why can you not sit back and accept that you are the king here?"
    "There is no god. There is no heaven. There is no hell."
    "There’s just this."
    "Love it."
    "Cherish it."
    "Embrace it."
    "For it is all you have now."
    "Those days when you were younger, when you were still unable to touch the tips of your fingers together as they curled around the pole of a stop sign..."
    "Those days are gone."
    "Now, your hands are bigger. Your body is stronger. "
    "It doesn’t grow much anymore, but your brain still does."
    "You know things now."
    "Not to touch the stove when it’s on."
    "Not to put metal in microwaves."
    "Not to pull on a cat’s tail."
    "Things you had to learn because that’s just how the world works."
    "…"
    "And now-"
    "You’re here again."
    "Hiding away in the darkest corners of your mind, distracting yourself with thoughts of better days, because you’re afraid of opening your eyes and seeing how terrible it’s all become."
    "You are no astronaut."
    "You’re just another piece in a much bigger puzzle."
    "It always comes back to puzzles, doesn’t it?"
    "I don’t want you here anymore."
    "Open your eyes."

    play sound "static.mp3"
    scene microwaves1
    with flash
    stop sound

    i "Oh, Sensei! "
    s "..."
    i "I heard from Uta that you ran off after Molly to try and make her less drunk or something. "
    i "How did that go?"
    s "I..."
    s "..."
    s "I don’t really know."
    i "Oh. Okay. Weird."
    i "I guess that’s kind of what it’s like dealing with drunk people sometimes, though."
    i "But, if it makes you feel any better, you can hang out with me now!"
    i "I figured I’d try and catch you after you were done saving Molly from self-destruction or whatever and...apologize for all of the weird stuff I was saying earlier."
    s "Everything you say is weird, Io. You don’t have to apologize for it."
    i "I...kinda do. "
    i "It’s ingrained into my personality at this point, and if I don’t apologize to the people I care about for everything I do, I believe they’ll get sick of me and stop caring entirely."
    i "Thankfully, that list of people is only two right now."
    i "And while I’d like to say this means I don’t have to apologize much, I fuck up very frequently and will apologize to both you and Uta until you’re...forced to..."
    i "…"
    i "What...happened?"

    play sound "static.mp3"
    scene microwaves2 with flash
    stop sound

    s "What do you mean?"
    i "I..."
    i "You look..."

    scene microwaves3
    with dissolve

    i "Different from how you normally look."
    i "So I figured I’d ask if something happened."
    s "Nothing happened."
    i "Yeah. Okay."

    scene microwaves4
    with dissolve

    i "Just forget it then! I mean, if you say it was nothing, it was definitely nothing. And I’m not going to make a big deal out of something that is literally {i}nothing{/i} you know? Hahah..."
    s "…"

    scene microwaves5
    with fade

    s "Hah..."
    i "…"
    i "Was it...something I said?"
    s "Not everything is about you, Io."
    s "In fact, {i}most{/i} things aren’t about you."
    s "So before you go and start over analyzing however I look or...how I’m acting right now, run that through your head a few times and see if it sticks."
    s "If not, it’s probably best to just leave me alone."
    s "I shouldn’t be here anyway."
    i "…"
    s "…"

    scene microwaves6
    with dissolve

    i "I like you."
    s "Yeah. You’ve said that before."
    i "I like you a lot."
    i "And I’m sure that no matter what that...thing that I’m not involved in is, I’ll still like you."
    i "I don’t expect that to make you smile or for you to just...get over it or anything, but I felt the urge to tell you again."
    s "I see."
    i "Do you want a hug?"

    scene microwaves7
    with dissolve

    s "Not right now."
    i "I’ll hug you in my mind instead."
    s "Do whatever you want. "
    i "Do you feel the mind-hug? I’m squeezing really hard."
    s "Sure. Whatever. "
    i "…"
    s "…"

    scene microwaves8
    with dissolve

    i "I won’t pretend to know what’s wrong, and I won’t ask you to tell me any secrets that you’re trying to keep hidden or something."
    i "One, because the burden of knowing would probably eat me up from the inside."
    i "And two, because I don’t expect you to always know what’s wrong with me either."
    i "We can keep being...eggshells around each other."
    s "Do you mean “walking on” eggshells?"
    i "No. I mean {i}being{/i} eggshells."
    i "The good parts of us have already been spilled out and used up by somebody else, and all that’s left is the useless white part."
    i "I’m crafty, though. And good with my hands. So if you let me hold you like I’d hold an egg, I can try to fix you up and make you look new again."
    i "Or, if that doesn’t work, decorate you and make you look better than ever before."

    scene microwaves9
    with dissolve

    i "But you’ll still always be empty inside."
    i "I can't change that part."
    s "…"
    i "…"
    i "I think it’s your turn to talk now."
    s "I don’t think I’m an...eggshell, Io."
    i "Why not?"
    s "Because “empty” isn’t the right word."
    s "There’s still something inside of me. I can feel it moving around."
    s "I just know it isn’t good. Or it’s not supposed to be there or...something."
    s "I don’t know. This analogy is annoying."
    i "Wanna crack yourself open and see if it’s a cool little worm or something?"

    scene microwaves10
    with dissolve

    s "How would I even-"
    i "By running away with me."
    s "…"
    i "We can go anywhere in Kumon-mi. And I won’t judge you if that...wiggly thing inside of you starts to come out."
    i "I’ll share it with you...since you’re already sharing some of what makes me want to curl up and wither away."
    i "Make your home inside of me, Sensei. "
    i "Let’s try our best to be happy together, because god knows we can’t do it on our own."

    scene microwaves11
    with dissolve

    s "There is no god."
    i "You’re right. There is no god."
    i "No god would make a world as cruel as this."
    s "Also, I’m not running away with you."
    i "Darn it."
    i "Guess I’ll have to wait until your next mini-bout of vulnerability to swoop in for the kill."
    ki "There you are!"

    scene microwaves12
    with fade

    ki "Guess what {i}I{/i} just did."
    s "Probably something evil or mischievous."

    scene microwaves13
    with dissolve

    ki "No, actually."
    ki "I just finished walking Noriko to the bus stop because {i}someone{/i} made her cry."
    ki "That someone is you. You are the someone."
    s "Thank you for clarifying. I was unaware."

    scene microwaves14
    with dissolve

    ki "Oh, the green girl is here too. Hi, green girl."
    i "It’s strange that you keep calling me that despite trying to talk to me on a weekly basis."
    i "You’d think that if you {i}really{/i} wanted to talk to me, you’d learn my name."
    ki "Do you know {i}my{/i} name?"
    i "Kirin."

    scene microwaves15
    with dissolve

    ki "Io."
    ki "See? I knew."
    i "Wow. Good job."
    ki "Are we officially friends now? "
    i "No. But we are officially acquaintances, which I suppose is more than nothing."
    ki "I will take what I can get."

    scene microwaves16
    with dissolve

    ki "What’s up {i}your{/i} ass? Don’t tell me the news about Noriko hit you that hard."
    ki "Actually, do tell me if that’s what it is. I’m sure she’d be happy to hear that you’re thinking about her in literally...any sense of the word."
    s "I’m just feeling a little out of it."

    scene microwaves17
    with dissolve

    ki "In what way?"
    ki "Were you drinking too? Because I literally told Molly to wait for me, and if you went off and took my place while I was being a good friend, I’m gonna be pissed off."
    s "Molly-"

    "Molly is drunk."
    "Molly is sad."

    s "…"
    s "Do you two want to go somewhere else?"

    scene microwaves18
    with dissolve

    ki "Like...away from the party? I literally {i}just{/i} got back. "

    if bonus == True:
        ki "{i}Plus{/i}, it is fucking freezing out there and my nipples are going to cut holes in my lingerie if they get any harder."
    else:
        ki "{i}Plus{/i}, it is fucking freezing out there."

    i "I’d be happy to go somewhere else with you, Sensei. I just don’t see the need for Kirin to come as well."

    scene microwaves19
    with dissolve

    if bonus == True:
        ki "Oh, you don’t? Well, that’s too bad. Because my nipples are magically soft now and there’s nothing you can say that’ll stop me from coming."
    else:
        ki "Oh, you don’t? Well, that’s too bad. Because I suddenly love the cold and I'm coming anyway."

    i "I’ve already annoyed Sensei enough tonight, so I’ll hold the rest of my arguments until you do something to piss me off."

    scene microwaves20
    with dissolve

    ki "So, where are we going?"
    ki "You had something in mind, right?"
    s "Not really."
    s "Just...anywhere, I guess."
    s "I need to walk."
    ki "Oooookay. Well are you going to at least say bye to everyone or-"
    s "I need to walk now."

    scene microwaves21
    with dissolve

    s "I...need to walk..."
    ki "Jesus, why is everyone but me being so fucking dramatic tonight?"
    i "…"

    scene microwaves22
    with dissolve

    i "Sensei! Wait for me!"
    ki "Oh, god damnit..."

    scene black
    with dissolve2

    "I walk."
    "I walk and I walk and I walk."
    "Io and Kirin are there too."
    "The three of us walk together."
    "We walk to all kinds of places."
    "A tree."
    "A bench."
    "A garbage can."
    "Another tree."
    "It is a fun and successful ending to the Halloween party."
    "I am glad that nothing bad happened tonight."
    "Nothing bad happened tonight."
    "I am a good person."
    "I receive several calls and text messages after I disappear."
    "I ignore them all but one."

    play sound "phonebeep.wav"

    mo "{i}Hhiy...is molly{/i}"
    mo "{i}I got youe number from Futa{/i}"
    mo "{i}Futa{/i}"
    mo "{i}lol autosuggest{/i}"

    "I don’t respond."
    "I don’t know what to say."

    mo "{i}Did yo leave???{/i}"
    s "…"
    mo "{i}Come back Sir{/i}"
    mo "{i}need to know whst happened{/i}"
    s "…"

    "I walk some more."
    "My phone stops vibrating."
    "I bring {s}Molly{/s} Kirin and Io back to the dorm."
    "Why am I thinking about Molly?"
    "I don’t want to think about {s}MOLLY{/s} anyone."
    "{s}I DON’T WANT TO THINK{/s}"
    "What did I want to be when I was younger?"
    "I escape again."
    "I run."
    "I walk."

    play sound "phonebeep.wav"

    "Phone beep again."
    "Remove."
    "Tap."

    s "…"

    stop music

    mo "{i}Was I a good protagonist?{/i}"

    $ mollynumber = True

    "{i}You have unlocked Molly’s phone number!{/i}"

    play sound "jackpot.mp3"
    scene halloweenyay
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    scene lavendermisc with flash
    scene tree3 with flash
    stop sound

    $ renpy.end_replay()
    $ halloweentwo13 = True

    $ totaldays += 1
    $ day = 6
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date
        jump saturdaymorning
    else:
        jump saturdaymorning

label goodboy:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
with dissolve2

    "………"
    "……"
    "…"

    scene whatwedo31
    with dissolve

    mo "Ngh..."
    mo "Thanks...for your help, Tsuneyo..."
    mo "Can’t imagine how that would’a gone if any’a the others found me."
    t "I am simply doing what I believed any good friend would do."
    t "You seem less disturbed by what happened than I thought you would be, though."
    t "I suppose that maybe the Herald was not lying when he decided to trust you over accepting a swift and mostly painless death."

    scene whatwedo32
    with dissolve

    mo "Ya t’reatened ta kill ‘im? Ain’t t’at a bit much?"
    t "If he had done something truly unforgivable, I don’t believe so."

    scene whatwedo33
    with dissolve

    mo "I’m...pretty sure it wasn’t anything like that..."
    mo "I can remember...talkin’ to him outside and then...comin’ in here..."
    mo "And my minds been all sorts’a screwed up lately. You know that."
    mo "Maybe it was me?"
    t "…"
    mo "Kinda wish I’d remembered what happened if that were the case, though."
    mo "'Ve'eard 'bout blackout drinkin' before, but never knew'it'd 'appen'tis quickly."
    t "You still lasted much longer than I would."
    mo "Yeah, well...you’re a special case."
    t "Do you really feel no pain at all, Emerald Guardian? Not even the slightest bit?"

    scene whatwedo34
    with dissolve

    mo "Not from anything I didn’t do to myself, I don’t think."
    mo "Just...not sure what to say to Sir now."
    t "You’re not mad about what he did to you?"

    scene whatwedo35
    with dissolve

    mo "Well’ats exactly th’problem."
    mo "I don’t wanna get mad too quickly if I played’a part in it."
    mo "S’a different story if’e just wanked one off while I was sleeping...but I feel like it’s more’ten that."
    mo "Or at least I hope it’s more."
    mo "Beatin’ off on a sleepin’ girl’s a pretty shite quality in a person."
    t "You think he might have beaten you?"

    scene whatwedo36
    with dissolve

    mo "No...Kendo Princess..."
    mo "I ‘tink it might’a been something sexual."
    t "I assumed that much, but I thought your heart was already possessed by the warlock Nithhala."
    t "Can multiple people hold dominion over the same organ at once?"
    mo "Yeah, but...I don’t know if I’d say that’s what’s goin’ on here."
    mo "I don’t wanna bog ya down by talkin’ about it when I know’it makes ya flustered, but I’ve talked to Sir about stuff like that recently."
    mo "And since I’ve already been playin’ around with the idea of maybe divin’ in’ta that sorta’ting...I just think this might be...my fault."

    scene whatwedo37
    with dissolve
    stop music fadeout 20.0

    t "I will respect your outlook. But I do not believe anything could possibly be your fault if you were not even conscious to be at fault {i}for{/i} it."
    mo "But what if I was’en then just...conked out? That’s why I’ve gotta talk to Sir."
    mo "But damn if I ain’t gonna be scarlet bringin' that up to’im."
    mo "You...wouldn’t happen ta know where he ran off to, would’ya?"
    t "Somewhere else."
    t "I asked him to leave this place at once."
    t "But he did not seem to be himself when he agreed, so it is possible he may have ignored that command entirely."
    mo "Ahh, shite."
    mo "It might be best to wait until another day then. Dad always said to not make important decisions while’yer on a tear."
    t "I did not notice any tears in your costume. Your father would be proud."
    mo "Hah..."
    mo "No’e wouldn’t, Kendo Princess."
    mo "No’e wouldn’t..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ halloweentwo12 = True
    $ mollysad = True

    "........."
    "........"
    "......."
    "......"
    "....."
    "...."
    "..."
    ".."
    "."

    jump halloweentwo13
...
```