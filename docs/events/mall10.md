# Behind The Curtain (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chika love greater than or equal to 10



## Next events

* [Chika: Side Event](./chikadorm10.md)

## Event properties

* Id: mall10
* Group: Chika
* Triggered by label: mall
* Triggered by branch label: mall
* Triggered by path: mall->mall10

## Official wiki page

[Behind The Curtain](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mall10&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall10:
    scene mall2
    with dissolve
    play music "mall.mp3"

    "I show up at the mall a little later than usual after getting caught up in traffic."
    "Chika’s break should have already ended by now, so I guess I’ll wind up hanging out with her at her work again today."
    "Not like that’s a problem, though."
    "In fact, it might be {i}good{/i} that I showed up late because it increases the chances of her taking her clothes off for me."
    "Obviously, she'd be putting on {i}different{/i} clothes and not letting me watch the act of doing so- but either way. She is taking off her clothes for me."
    "And that is all I need to know."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene mallfive1
    with dissolve2

    c "Heya! Welcome-"
    c "Ah! Sensei!"

    scene mallfive2
    with dissolve

    c "Great timing. I was just thinking about you."
    s "You mean you aren’t {i}always{/i} thinking about me? Bummer."

    scene mallfive3
    with dissolve

    c "Cut me some slack, Sensei! If I spent literally {i}all day{/i} thinking about you, I’d forget to come to work and lose my job and it would be like, a whole thing."
    c "Besides, there's no way you think about me even half as much as I think about you."

    "Sure I do. I just can't talk about the majority of those thoughts out loud."

    s "I suppose that you dedicating any amount of time to me is more than enough, but I still implore you to try and fit more in whenever possible."

    scene mallfive9
    with dissolve

    c "I'll see if I can pull some strings and make that happen."
    c "So, you ready?"
    s "Ready for what?"
    c "Seeing me try some stuff on, dummy! That's why you came, isn't it?"
    s "I mean...that wasn't the {i}only{/i} reason."
    c "Well, I'm ready whenever you are."

    scene mallfive4
    with dissolve

    c "Plus, I found a dress that I might actually look good in, so..."
    s "Do you need any help putting it on?"

    scene mallfive9
    with dissolve

    c "Mmm...no. I think I can handle that part myself. You can follow me over to the dressing room, though."
    c "And if there’s anything you wanna try on, just let me know. Maybe I can judge you after you do me?"
    s "You can do me whenever you want, Chika."

    scene mallfive2
    with dissolve

    c "Thanks! Just follow me to the-"

    scene mallfive8
    with dissolve

    c "Wait! No! I said a weird thing again! I didn't mean it like that!"
    s "So...we're {i}not{/i} going to do each other?"
    c "Not yet!"
    s "But doesn't that imply-"
    c "Nope!"
    s "..."
    c "Anyway! Time to get dressed!"

    scene black
    with dissolve2

    "Chika awkwardly shuffles her way over to a separate part of the store, straightening out her skirt and shaking off whatever nerves started acting up as a result of her inappropriate wording just now."
    "I have to do the same, but it's less {i}awkward{/i} and I can't imagine it looking even half as attractive."
    "Either way, she stops in front of the dressing rooms before turning to face me."

    scene mallten1
    with dissolve2

    c "Okay, so. Disclaimer-"
    c "I’ve already told you that dresses aren’t my thing...so even if I said that I like this one...please don’t expect too much."
    s "Deal."
    c "Great. Disclaimer part two-"
    c "Make sure you wait until I’m done getting dressed to actually come in."

    scene mallten2
    with dissolve

    s "I liked the first disclaimer more."
    c "I bet you did, Sensei."
    c "And remember- I’m still {i}technically{/i} at work, even if there aren’t any customers right now."
    s "I hope there's not a third disclaimer stating that I need to help any of them while you're getting changed."
    c "..."
    s "Chika, I don't know how-"

    scene mallten3
    with dissolve

    c "Then, I guess all we can do is hope that nobody comes in!"
    c "But yeah! Other than that, just don’t make fun of me when I look like a fish out of water and we'll be all good!"
    s "Sounds easy enough. Apart from the idea of helping customers, I mean."
    c "Great! Then, hang out here for a couple minutes while I get dressed and...I'll see you soon."
    s "Sure thing. Let me know if your bra gets stuck and you need help getting it off."
    c "One of the hooks is already broken, so I doubt that'll be a problem. But thanks for the offer."

    scene black
    with dissolve2
    stop music fadeout 25.0

    if bonus == True:
        "Chika disappears into the dressing room and I can hear her clothes beginning to fall to the floor moments later."
        "It takes every ounce of self-control I have to not sneak in there, but I respect Chika's wishes and remain outside."
        "I'm sure a day will come when I don't have to do that anymore but, for now, the best way for me to get closer to her is to respect the very few boundaries she actually establishes."
        "I know that, at the end of the day, she is taking her clothes off for me right now."
        "So I justify my wait by reiterating that single thought over and over in my head until the time finally comes to-"
    else:
        "Chika disappears into the dressing room and I wait outside like the respectable man I am."

    c "Sensei! I'm...suddenly having second thoughts about this."

    "The time comes sooner than expected."

    s "What? Why?"
    c "Because I look like a freaking idiot."
    s "Chika-"
    c "Fine! Fine..."
    c "You can come in, just..."
    c "I'm sorry in advance for the disappointment..."

    scene black
    with dissolve2

    "I follow the sound of Chika's voice, slightly muffled by a thick red curtain-"

    scene mallten4
    with dissolve2
    play music "love.mp3"

    "And stumble upon a wonderful sight."

    c "Yeahhh, so...I kinda thought I’d look a little cuter than this...but it’s whatever, I guess."
    c "Dresses just aren’t my thing. I promise I’ll wear something more exciting next time."

    if bonus == True:
        c "Maybe not something as exciting as {i}lingerie{/i}, but..."
    else:
        c "I know that this probably isn't that great compared to a clown costume, but..."

    s "Don’t say that. Just because it's different from how you normally look doesn't mean it's {i}bad.{/i}"
    c "It doesn't mean it's {i}good{/i} either, though..."
    c "Like...how do you really think I look like dressed in stuff like this, Sensei? Be honest."

    menu:
        "I think you look beautiful":
            s "I think you’re beautiful, Chika."
            c "Yeah, that’s what I-"

            scene mallten10
            with dissolve

            c "Wait, what? Who? Me?"
            c "What did you just say?"
            s "I said I think you look beautiful."
            c "Yeah, but like...sarcastically, right? Like what you {i}really{/i} think is that I resemble an out-of-place[teen]on her way to Easter breakfast with her grandparents."
            s "I would...never think something that specific. I just genuinely think you look great."
            c "You...You know that I’ll still like you even if you tell me the truth, right? You don't have to be nice 100%% of the time."
            s "I am telling you the truth."

            if bonus == True:
                c "And you know I’ll still eventually do the lingerie thing even if you don’t compliment literally everything I ever wear, right?"
                s "Just accept the compliment, Chika."

                scene mallten11
                with dissolve

                c "Ahhhhh! I wanna! It’s just super embarrassing and I didn’t expect you to say anything good!"
                c "Maybe you just...need to take a closer look or something?! I don't know!"
                c "You wear glasses so your eyes are probably bad and-"
                s "Fine. "

                scene mallten12
                with hpunch
                play sound "thump.mp3"

                s "Nope. Still beautiful."
                c "Oh my God. A real kabedon. Am I dreaming?"
                s "What?"
                c "Nothing. Don't stop."
                s "Uhh...I don't really know what else there is to say other than you still look great."
                c "You’re not even looking at the dress anymore."
                s "Yeah. There's something else I like looking at a little more."
                c "Oh my fucking God, my hot teacher is kabedoning me. I'm in an anime. This isn't real."

                "Chika presses her back against the mirror not to get away, but to make herself more comfortable."
                "She's obviously surprised by me suddenly closing the distance like this...but she {i}was{/i} the one who suggested it, so..."

                scene mallten13
                with dissolve

                c "…"
                s "…"
                c "Your..."
                c "Has anyone ever told you how pretty your eyes are?..."
                c "And like, not even just that...you're straight up {i}really{/i} attractive up close..."
                s "I'll make sure to get as close as I can when I flirt from now on, then."
                c "Do you...really not have a girlfriend?"
                s "I already told you. I’m preoccupied with a bunch of [teenager]s instead."
                c "Sorry, I just..."
                c "My heart’s beating out of control right now and it’s kinda hard to remember stuff."
                s "Is it?"
                c "Uh-huh..."
                s "And why is that, Chika?"

                scene mallten14
                with dissolve

                c "Oh, I don't know, Sensei! Why do you think?!"
                s "Is that sass I hear right now?"

                scene mallten15
                with dissolve

                c "Are you gonna give me detention if I say yes?"
                s "I am now. Please drop by my office after[school] as soon as possible."
                c "What are you gonna make me do, Sensei?"
                s "I guess we’ll find out soon enough, won’t we?"
                c "Is it wrong for me to be a little excited?"
                s "Do you want the real answer or the hotter one?"
                c "Gimme the hotter one."
                s "Then, no."
                c "I've never had a detention before, Sensei. You might have to give me directions."

                "This is so much better than lingerie."

                scene mallten16
                with dissolve

                "I bring my hand to Chika’s face, not knowing exactly how she'll react but, as you can see, it works out pretty favorably."

                c "About time."
                s "Am I moving too slow for you?"
                c "Yes."

                scene mallten17
                with dissolve

                c "Ahm~"

                "Oh."
                "Oh, okay."

                c "Mnh...mmm..."
                s "..."

                scene mallten18
                with dissolve
                stop music fadeout 15.0

                c "Mnch...mmm..."

                "In a welcome turn of events, Chika slowly and gently wraps her tongue around my thumb, sensually taking as much of it into her mouth as she can."
                "To say I'm shocked is a bit of an understatement, but she's been more or less full of surprises thus far and the idea of her being into things like {i}this{/i} isn't too absurd."
                "And again, this is so much better than lingerie."

                c "Mm...mm...you like that, Sensei?..."
                c "This is...amf...what you wanted...right?..."
                s "..."
                c "..."

                scene mallten19
                with hpunch
                play music "mall.mp3"

                c "Oh my God. Please tell me I didn't just {i}dramatically{/i} misread the situation."
                c "Cause I really thought that was where we were going with that and-"
                s "No, it's just...I'm a little surprised."
                s "I thought you were innocent, is all."
                c "I am innocent!"
                s "The saliva all over my thumb begs to differ."
                c "That's...I don't know, Sensei! It seemed like the right thing to do at the time!"
                c "I just got worried that you were talking about an {i}actual{/i} detention when you stopped talking and just let me keep going and...and..."

                scene mallten20
                with dissolve

                c "And your thumbs are big! You should...apologize! For...for having such..."
                c "Such...large..."
                s "..."
                c "..."
                c "I'm going back to work now!"

                scene black
                with dissolve2

                "Chika storms out of the dressing room and, once I follow her out, she begs me for the next ten minutes to forget any of that ever happened."
                "Well, not {i}any{/i} of it- but the part where she started fellating my finger."
                "Regardless, it’s clear now that there’s at least some form of chemistry between us."
                "What that chemistry {i}is{/i} remains to be determined."
                "But once it reaches its full potential-"
                "I can see Chika becoming someone I'll never forget."
                "........."
                "......"
                "..."
                "Oh, and also, she is good with her tongue."

                $ renpy.end_replay()
                $ chikadetention = True
                $ mall10 = True
                $ chika_love += 1
                stop music fadeout 5.0

                "{i}Chika’s affection has increased to [chika_love]!{/i}"
                "........."
                "......"
                "..."

                jump saturdaynight
            else:
                c "Even though I'm not a clown?"
                s "Even though you're not a clown."

                scene black
                with dissolve2

                "Somehow, nothing else happens in that dressing room."
                "The two of us just stared at each other for what felt like hours and then left as if nothing had ever happened in the first place."
                "But it’s clear now that there’s chemistry between us, and I’ll be damned if I don’t capitalize on that as soon as possible..."

                $ renpy.end_replay()
                $ chikadetention = True
                $ mall10 = True
                $ chika_love += 1
                stop music fadeout 5.0

                "{i}Chika’s affection has increased to [chika_love]!{/i}"
                "........."
                "......"
                "..."

                jump saturdaynight

        "I think you look fine":
            s "I think you look fine."
            s "Sure, it’s not as fitting as your normal clothes, but you’re still adorable."

            scene mallten5
            with dissolve

            c "Guh...Maybe if I started, like...styling my hair differently, I could pull stuff like this off?"
            c "I’m sure makeup plays some part in it too, but that's like, a crazy amount of work."

            scene mallten6
            with dissolve

            c "Sorry for subjecting you to this, Sensei. Just can't help but feel like I should maybe try and change up my image every once in a while."
            s "What are you apologizing for? I don't see anything wrong with your normal style."
            c "I don't know. It's just that the whole gyaru thing attracts some unwanted attention at times."

            scene mallten7
            with dissolve

            c "Plus, you hanging around with a girl who looks like I do might...send some bad signals out or something."
            s "Dress however you want to dress, Chika. Don't tailor your style to fit me or anyone else."
            s "If you like it, wear it. That's really all there is to it."

            scene mallten8
            with dissolve

            c "Yeah...Yeah, that's a good point."
            c "As long as you don’t think I look weird or whatever, I’ll probs just keep dressing how I have been."
            c "It would suck having to buy a whole new wardrobe anyway..."
            s "At least if you start saving now, you might be able to afford something here by the time you retire."

            scene mallten9
            with dissolve

            c "Hahah! Yeah...maybe."

            scene mallten7
            with dissolve

            c "Well, uhh...I guess I should probably be getting back to doing my job or whatever now."
            c "You’re sure no one saw you follow me in here, right?"
            s "I...don’t remember checking, actually."

            scene mallten8
            with dissolve

            c "Oh well. We've been slow all day anyway, so I doubt there were any customers while we were in here."
            c "Just...you go out first and I'm sure everything will be alright. I still need to put my regular clothes back on anyway."

            if bonus == True:
                s "It's fine. I'll stay for that part. I want to understand your process."
            else:
                s "But you haven't turned into a clown yet. Is that-"

            scene mallten9
            with dissolve

            c "You will most certainly not stay for that part, Sensei."
            s "Well, you can't blame me for trying."

            scene black
            with dissolve2

            "I exit the dressing room and Chika comes out a minute or two later."
            "We chat for a little while longer before her boss calls and she needs to go over some inventory stuff with her."
            "As such, I exit the store and am once again subjected to aimlessly wandering the streets of Kumon-mi..."

            $ renpy.end_replay()
            $ mall10 = True
            $ chika_love += 1
            stop music fadeout 5.0

            "{i}Chika’s affection has increased to [chika_love]!{/i}"
            "………"
            "……"
            "…"

            jump saturdaynight

label mall15:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall:
    if chika_love >= 0 and firsttimemall == False:
        jump firsttimemall
    if chika_love >= 5 and mall5 == False:
        jump mall5
    if chika_love >= 10 and mall10 == False:
        jump mall10
...
```