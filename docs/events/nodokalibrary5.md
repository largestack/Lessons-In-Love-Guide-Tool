# Coloring Book (Nodoka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Nodoka love greater than or equal to 5

* Event [Cracks in the Armor](./nodokalibrary1.md) (Nodoka) is completed)

* Day of week is Saturday



## Next events

* [Nodoka: I See Everything](./nodokadorm5.md)

## Event properties

* Id: nodokalibrary5
* Group: Nodoka
* Triggered by label: nodokalibrary
* Triggered by branch label: saturdayafternoon
* Triggered by path: saturdayafternoon->nodokalibrary->nodokalibrary5

## Official wiki page

[Coloring Book](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nodokalibrary5&go=Go) for more details.

## Event code

File: (install folder)\game\NodokaEvents.rpy

Code:
```python
...
label nodokalibrary5:
    scene black
    with dissolve

    "………"
    "……"
    "…"

    play music "justlights.mp3"

    "{i}A fool sees not the same tree that a wise man sees.{/i}"
    "{i}He whose face gives no light, shall never become a star.{/i}"
    "{i}Eternity is in love with the productions of time.{/i}"
    "{i}The busy bee has no time for sorrow.{/i}"
    "{i}The hours of folly are measured by the clock, but of wisdom: no clock can measure.{/i}"
    "{i}- William Blake (1757 - Whenever he died)"
    "Some people have danced with tragedy while others do not know how to dance at all."
    "And somewhere between those two dancers, there is a place that resembles ours."
    "You likely won’t ever see it."
    "But some have."
    "And you likely won’t ever see them either."
    "Because their world faces a different direction than ours."
    "I hope you’re happy, wherever you are."
    "………"
    "……"
    "…"

    scene nodokasecondlib1
    with dissolve

    no "Good afternoon, Sensei. "
    no "Your timing is quite good today. I was just starting to get bored."
    s "Well you certainly look relaxed, if not anything else."
    no "This library has no couch, so I needed to create my own out of a metal chair and an annoyingly elevated desk."
    no "I give it a 5/10 for comfort and 7/10 for accessibility."
    s "Is this how bored you are? Resorting to rating the objects of the library?"
    no "Do you want to know {i}your{/i} rating?"
    s "I don't. I’m pretty sure it would make me self-conscious if it was low."
    no "Does my opinion matter that much to you?"
    s "It doesn’t...{i}not{/i} matter?"
    no "Interesting."
    no "So, how should the two of us kill time today without Futaba around to stare at?"
    s "We could just stare at each other, I guess."
    no "Or, alternatively, we could leave this place altogether and find something else to do."
    s "Are you allowed to leave right now? I thought you were taking over for Futaba?"
    no "Yes. I’m taking over for her volunteer position in a[school] library over the weekend, when barely anyone visits."
    no "I think I can get away with leaving a little early if I have prior engagements."
    s "It’s not really a prior engagement if we make it right now."
    no "No, but the books don’t know that."
    s "The books don’t know anything. They are books."

    scene nodokasecondlib2
    with dissolve

    no "Did you hear that, Hamlet? Sensei thinks you’re worthless."
    no "He bites his thumb at you."
    s "Hey. That line isn’t even from Hamlet."

    scene nodokasecondlib3
    with dissolve

    no "It’s not. But the phrase carries the same meaning and was completely comprehensible in context, correct?"
    s "Do you quarrel, Nodoka?"
    no "Quarrel, sir? No sir."
    s "..."
    no "..."
    s "As much as I'd like to continue, I don’t really remember anything else from that play. "
    no "That’s fine. I’m not much of an actor anyway."
    no "I don’t even really like plays. I’m just reading this because it was the first thing I picked up."
    no "This[school] is fine, but the library is small and its selection is entirely generic."
    no "My heart aches for all of those poor books stuck in that sink hole."
    no "Oh, here’s an idea. How would you like to venture to the ruins of my old[school] and throw yourself into an abyss?"
    s "I would not like to do that at all. It sounds horrible and dangerous."
    no "Then tie a rope around me and lower me down so I can at least pick up a few things I haven’t already read."

    if bonus == True:
        s "If I ever tie a rope around you, it will be for significantly less wholesome reasons."
    else:
        s "If I ever tie a rope around you, it will be because we are bungee jumping."

    scene nodokasecondlib4
    with dissolve

    if bonus == True:
        no "Bondage fan?"
        s "Not really, but pretty much everyone is fine with bondage if it’s just rope."
        s "I think."
        s "I don’t really know, actually."
        no "Handcuffs?"
        s "Sure. I know where to buy some, too."
        s "I’m pretty sure I wouldn’t be allowed to actually purchase them, though."
        no "Did you somehow manage to get yourself banned from a sex shop, Sensei? That’s so depressing."
        s "No. I just...know someone who works there."
        no "Someone I can meet?"
        s "Someone you’ve already met."
    else:
        no "I have always wanted to try that."
        s "Unfortunately, I already have a partner."

    no "Is it the tiny girl with the black hair who sits in the back of the classroom?"

    if bonus == True:
        s "Are you just {i}always{/i} going to guess Sana whenever I mention anything remotely sexual involving literally anyone?"
        no "I’m telling you, Sensei. She’s a freak. I can feel it."
    else:
        s "I do not know why you would assume that, but no. It is not Sana."
        no "She seems like she'd be a good bungee jumper."

    if sarasex == True:
        "Well she...definitely would not be the only one in her family like that."

        if bonus == False:
            "Sara loves bungee jumping."

    s "I...don’t think that’s true. But if that’s what you want to think, feel free."
    no "Speaking of “things that I think,” I’d like to reiterate and reintroduce the idea of us getting out of here."
    no "I haven’t seen a non-Sensei soul in hours. There is absolutely no downside to the two of us going on a little adventure."

    if bonus == True:
        s "An adventure to where? I’m fine with going out to lunch or something, but if you’re trying to drag me into a janitor’s closet..."
        s "Well, that’s even better."

        scene nodokasecondlib5
        with dissolve

        no "Hmm...no. Flirting is fun but I think we should limit things to just extremely suggestive talking for now."
        no "Just think of how great the payoff will be if we build up the tension a little more."
        s "And you were accusing {i}me{/i} of leading people on."

        scene nodokasecondlib6
        with dissolve

        no "Here, take a Nodoka point. Does that make you feel any better?"
        s "Just one? I thought they only came in multiples of fives?"
        no "They come in whatever amount I want them to come in. I’m in charge, remember?"
        s "That’s one hell of a double standard, Nodoka."
        no "I’m one hell of a girl, Sensei."
    else:
        s "I agree. It's really stuffy in here anyway and I need to keep my legs stretched for my potato sack race later."

    scene black
    with dissolve2

    "Nodoka grips her skirt as she moves her legs off of the desk and prevents me from being able to look up it because she is evil."
    "She puts Hamlet back on his shelf before the poison ever finds its way into his veins and he proceeds to live a long and happy life with Ophelia."
    "Until someone else decides to open the book, that is."
    "I can’t help but wonder how many other things there are in this world that are better left unfinished or unopened as we make our way out of the library and into the halls of the[school]."

    scene nodokasecondlib7
    with dissolve

    no "It feels like just the other day we were walking on the bridge like this."
    s "That kind of {i}was{/i} just the other day, though."
    no "I suppose that’s true."
    no "Has your opinion of me changed at all within that time frame?"
    s "I’m a little more worried about you as a person than I was back then."
    no "Worried? Why?"
    s "Well, maybe “worried” isn’t the right word. But I’m starting to think you’re capable of doing a lot more than you actually...want to do? Does that make sense?"
    no "Not really, no."
    s "Then let me try explaining it like this-"
    s "I think there are two Nodokas."

    if bonus == True:
        no "That would make an exciting threesome."
        s "It would, yes."
        s "But what I was getting at is that one of those Nodokas wants to be suggestive and flirty all day..."
        s "While the other one cares more about “tension” and...seemingly wants me to create the world’s largest consensual harem."
        no "You’re forgetting about the Nodoka who wants you all to herself."
        no "And the Nodoka who doesn’t want you at all."
    else:
        no "Oh god. Did they escape?"
        s "Wait, is there more than two?"
        no "More than I can even count."

    no "So many Nodokas, so little time."
    s "Which one is real, though?"
    no "All of them? None of them? Who knows?"
    s "I would imagine you do."

    scene nodokasecondlib8
    with dissolve

    no "Nope."
    no "I don’t really care to find out either."
    no "I just want to make memories while I still can."
    no "Good memories, bad memories, sad memories, passionate memories."
    no "Memories of anything and everything."
    no "If I feel every feeling the world has to offer, I’ll have an unlimited library of experiences to pull from and be inspired by."

    if bonus == True:
        no "And I’m not just talking about sexual stuff right now either."
        s "I...didn’t think you were."
        no "Okay, good."
        no "I did have a sex dream about you last night, though, just for the record."
        s "Wait, what?"

    scene nodokasecondlib9
    with dissolve

    no "The point is, you can’t figure out which Nodoka is the “real” Nodoka because she is all of those things."
    no "She’s just a girl. Not some genius or prodigy or anything like that."
    s "Don’t you have the highest test scores in all of Kumon-mi?"
    no "…"

    scene nodokasecondlib10
    with dissolve

    no "Okay, so maybe I {i}am{/i} a genius. But anyone can be a genius if they spend their entire life just...living other lives via literature."
    no "I said before that I’m not an actor, but one of the things I enjoy most of all is imagining how I would feel as someone else...Someone who isn't real."
    no "Or what I would do in their shoes, if only I could fit into them."

    if bonus == True:
        no "And yes, the answer to that question is typically declothing every female character and strapping them to sex machines-"
    else:
        no "Unfortunately, I have an invisible third foot and need to buy a very specific, special pair of shoes or I won't be able to walk at all."

    s "What?"

    scene nodokasecondlib11
    with dissolve

    if bonus == True:
        no "And yes, sometimes I must hook {i}myself{/i} up to those sex machines to truly understand what it means to feel-"
        s "{i}What?{/i}"
    else:
        no "I said that I have an invisible third foot and need to buy a very specific, special pair of shoes or I won't be able to walk at all."
        s "Oh, okay. I misheard you."

    scene nodokasecondlib12
    with dissolve

    no "But the second I close the book, I’m just Nodoka again."
    no "And everything turns gray."
    no "And I have to go out and find new colors to fill everything back in."
    no "Life would have been easier if I wasn’t printed as a picture book."
    s "…"
    no "…"
    no "The main reason so many people fall in love with fiction is because they’re searching for something they can’t obtain on their own."
    no "But there are also people who fall in love with it simply because there isn’t anything else to do."
    no "People who get so bored of not being able to feel anything that they allow themselves to fall into those who can."
    no "I kind of hate reading, actually."
    no "It’s time consuming...you can’t do it in the dark...and the memories you get out of it can barely be called memories at all since they aren’t your own."
    no "But the things I love about it always manage to outweigh those somehow."
    no "Even when I wish they wouldn’t."
    s "You don’t sound like a picture book at all, Nodoka."

    scene nodokasecondlib13
    with dissolve

    no "Huh?"
    s "You’re more like a...and forgive me in advance if this sounds childish-"
    s "But you’re more like a coloring book."
    s "A really advanced one with a lot of difficult drawings that...requires special attention and weird colors like chartreuse and mauve."
    s "And you’re just waiting to be filled in."
    no "…"

    scene nodokasecondlib14
    with dissolve2

    no "Oh..."
    no "It’s back."
    s "Hm? What is?"
    no "The color."
    no "It’s been gone for days."
    s "…"
    no "And there’s no chartreuse or mauve anywhere to be found..."

    scene nodokasecondlib15
    with dissolve

    no "Looks like you were wrong, Sensei."
    s "You just haven’t gotten to the page with all of the weird colors yet. You’re only in the beginning of the book."
    no "So the hardest is yet to come?"
    s "That depends. You’re not battling any really intense trauma or something, are you?"
    no "Is that really something you’re supposed to be asking someone?"
    s "Supposed to? No. Probably not."
    s "But I think we’re already at the level where we can start sharing things like that with one another."

    scene nodokasecondlib16
    with dissolve

    no "Hmm...I suppose we are."
    no "We’re out of the library now, but I think I’m going to carry on with my newfound hobby of rating things and give my personal trauma a solid 5/10."
    no "Nothing unmanageable, but nothing overwhelmingly tragic like witnessing a friend jump to her death or being mauled by a rhino."
    s "What kind of world do you live in where “being mauled by a rhino” is the second thing that comes to mind when measuring trauma?"
    no "One that’s sure to get a lot more colorful from this point on."

    scene nodokasecondlib17
    with dissolve

    no "Or not."
    no "For all we know, the two of us could grow to hate each other over something small like...taking the last piece of garlic bread."
    s "To prevent that hate from ever spawning, I hereby give you permanent permission to finish off any and all bread that we eat together in the future."
    no "Are you sure? Cause I really like bread and eating more of it all the time will make me fat."

    if bonus == True:
        no "I won’t be able to fit into the janitor’s closet anymore."
        s "We can just find a bigger closet, then."
        s "I’m not worried."
    else:
        s "You know, maybe we should just go on a diet instead."

    if bonus == True:
        scene nodokasecondlib18
        with dissolve

        no "Neither am I."
        no "If music be the food of love, play on."
        no "Here’s to the rest of our time together...which is sure to be full of confusion, misunderstandings, and handjobs in the locker room."
        s "I’ve never seen someone say “handjobs” with such a hopeful look on their face before."
        no "Then let us take this moment and lock it away in our collage of colors as just one of many memories the two of us will make together."
        no "Hooray for sinkholes."
        s "…"
        s "Yeah."
        s "Hooray for sinkholes."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ nodoka_love += 3
    $ nodokalibrary5 = True
    stop music fadeout 10.0

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label nodokadorm15:
...
```

## Code that triggers this event

File: (install folder)\game\NodokaEvents.rpy

Code:
```python
...
label nodokalibrary:
    if nodokablock == True:
        "I don't really think I want to see Nodoka right now..."
        jump satafternoonmenu
    if nodoka_love >= 0 and otohadorm1 == True and nodokalibrary1 == False:
        jump nodokalibrary1
    if nodoka_love >= 5 and nodokalibrary1 == True and day == 6 and nodokalibrary5 == False:
        jump nodokalibrary5
...
```