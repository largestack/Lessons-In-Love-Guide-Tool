# Unnamed Wooden Robots (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 5

* Event [The Girl with the Dragon Tattoo](./bathhouse5.md) (Io) is completed)



## Next events

* [Kirin: Love, Dorms, and Other Things](./kirindorm10.md)
* [Io: Paperthin](./iodorm10.md)

## Event properties

* Id: iodorm5
* Group: Io
* Triggered by label: iodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->iodorm->iodorm5

## Official wiki page

[Unnamed Wooden Robots](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=iodorm5&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm5:
    play sound "knock.mp3"

    "I knock on Io’s door and wait for her to answer."

    if utadorm5 == True:
        "It won’t be my first time being in there since I’ve already come to visit Uta before but..."
        "Well, I guess it will be interesting hearing Io’s take on the, uhh, {i}condition{/i} of the room."

    else:
        "I’ve yet to spend any time in there since her and Uta moved in and I’m really curious about what they’ve done with the place."
        "If I’m remembering correctly, it’s the first time either of them have lived in a dorm, so I’m sure they’ve put their own personal touches on it in some way already."

    s "…"

    "No one answers."
    "I guess I could have expected as much since this is Io we’re talking about and Uta would have just walked in..."
    "But I guess there’s always the possibility that she just isn’t at home right now."
    "Maybe I should call out to her so she knows I’m not some big, bad girl who’s come to...girl-up the place or something."

    play sound "knock.mp3"

    s "Io, it’s me. Are you around right now?"
    i "Oh, shoot."
    i "Yeah! Come in, Sensei. I thought you were somebody else."

    "Figures."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if utadorm5 == False:
        "I push the door open and notice a massive amount of clutter before it even opens all the way."

    else:
        "I push the door open to find that it’s in exactly the same state as it was the first time I came here."

    "I ask myself if it’s really fulfilling to live this way-"
    "But then I remember that it isn’t fulfilling to live at all and decide to move past it."

    scene iofirstdorm1
    with dissolve

    i "Hey."
    i "Come to give me a housewarming present or something?"
    s "Will you accept my presence as the...present?"
    i "Idunno. Can you do anything cool?"
    s "I made french toast this one time. That’s pretty cool, right?"
    i "It’s...normal."
    i "If you’re not bringing me a housewarming gift, what are you doing over here?"
    s "Just here to see you, I guess. Figured you might be bored or something."

    scene iofirstdorm2
    with dissolve

    i "We’re allowed to hang out in my room? "
    s "Probably not but that’s never stopped me before."
    i "Wow. You really do run a strange operation, huh?"
    s "I’m either the best or the worst teacher in the world depending on how you look at things."

    scene iofirstdorm3
    with dissolve

    i "Sorry the place is such a mess but, in my defense, most of this is on Uta."
    i "I’m just kinda stashing all of my stuff from my aunt’s house here so I can fool around in my spare time."
    i "And I’m pretty sure Uta is stashing every single item she’s ever laid her hands on. Pretty different approach if you ask me."

    scene iofirstdorm4
    with dissolve

    i "But hey, as long as you’re not uncomfortable surrounded by all this junk, I’m more than happy to have you."
    i "Can’t even remember the last time I hung out with anyone who wasn’t a part-time maid."
    s "I’m sure I’ll be coming here pretty regularly, so it's best you get used to it. "
    s "There is one thing that’s bothering me, though."
    i "Is it the cat on top of the wardrobe?"
    s "It is."
    i "You’re not allergic, are you?"
    s "I’m not. But I don’t particularly like animals."
    i "Ah. Well he’s dead anyway so you don’t have to really worry about either of those things."
    i "Or at least I don’t think you do? I’m not sure how taxidermied animals work for people with allergies."
    s "So that was {i}your{/i} cat and not Uta's, I’m guessing?"

    scene iofirstdorm5
    with dissolve

    i "Sir Meowington the Fourth."
    s "What happened to the first three?"
    i "The same thing that happened to the fourth. They died."
    s "You know, I was expecting a little more information there. But your simplistic way of looking at things has saved us a potentially awkward conversation."

    scene iofirstdorm6
    with dissolve

    i "You’re welcome."
    i "No sense in going into detail about stuff that’s just gonna bring you down, you know?"
    i "Gotta focus on the good stuff."
    s "Pretty positive outlook today, Io."
    i "Right?"
    i "Guess I’m in a good mood since my favorite teacher came to visit me."
    s "That’s quite flattering but I’m also your {i}only{/i} teacher, so..."
    i "Yeah but you’d still be my favorite even if I had other ones cause you won’t call on me to answer questions and stuff."
    s "I’d need to give out questions in order to do that in the first place, so yeah. You don’t have to worry about that."

    scene black
    with dissolve

    "Io moves a few steps to the side and takes a seat on an old-looking computer chair."
    "She also grabs a boxcutter off of her desk and begins to twirl it around with her fingers."

    scene iofirstdorm7
    with dissolve

    i "So, now what? Wanna play a game or something?"
    s "Saying that while twirling a boxcutter doesn’t exactly make me want to play anything you might be into."
    i "Oh, this thing? It’s kinda dull. You don’t have to worry about it."
    s "It looks incredibly sharp."
    i "Scared of sharp stuff, Sensei?"
    s "I want to throw it out there that that is a perfectly reasonable thing to be afraid of."

    scene iofirstdorm8
    with dissolve

    i "Relax. It’s just a tool. I’ve got tons of stuff way more dangerous than this lying around the room."

    scene iofirstdorm9
    with dissolve

    i "As long as you watch your step and make sure the area is clear before you sit down, you’re totally safe."
    i "I stepped on a nail once at my aunt’s place and you wouldn’t believe how-"
    s "Whatever you think I wouldn’t believe, I can probably assure you I would."
    i "What, I can’t even tell my nail story?"
    s "You can not."
    s "Instead, why not tell me more about this infatuation with tools? Like, why a boxcutter?"

    scene iofirstdorm10
    with dissolve

    i "We talked about my hobbies for like two hours at the bathhouse the other day. I like making things, remember?"
    i "The boxcutter is just for cutting boxes, though."

    scene iofirstdorm9
    with dissolve

    i "Unless you make me mad. Then it will be for cutting Senseis."
    s "..."

    scene iofirstdorm11
    with dissolve

    i "Um...That was a joke. "
    i "I wouldn’t actually hurt you, you know."
    i "I’m surprisingly non-confrontational for someone always talking down on other people."
    i "I’d probably just stop talking to you or...punch the wall or something if you ever made me that mad. "
    s "Can you at least put the boxcutter down, Io?"

    scene iofirstdorm12
    with dissolve

    i "No. I need something to fidget with or I'll start getting uncomfortable."
    i "Its the first time I've ever had a boy in my room. Please don't hold my discomfort against me."

    "Io begins quickly sliding the blade up and down with the little knob thing on the handle."
    "I’m sure there’s a special name for it but I have no idea what it's called so you’re going to have to deal with “knob thing” until I find out."

    scene iofirstdorm13
    with dissolve

    i "So, Sensei, is there anything you want me to try making you? "
    i "I just finished that second wardrobe a little while ago and I’m kinda out of big projects for now."
    s "Second wardrobe? Like, the one in this room?"
    i "Obviously. What other wardrobe would I be talking about?"
    s "You made those? They look professional."
    i "The one on the right has one leg that’s a little shorter than the others so it would never actually be able to ship or anything, but thanks."
    i "It’s really nice making stuff like that- stuff that can be used immediately."
    i "Sometimes, you’ll go out of your way to make something for somebody and they’ll act like they love it, but never actually use or find a use for it."
    i "It really sucks when stuff like that happens."

    scene iofirstdorm14
    with dissolve

    i "So I only make things that I know other people need or that I can use myself now."
    s "Well, the second I need a carpenter, I know who to come to."

    scene iofirstdorm13
    with dissolve

    i "Heheh~ Part carpenter, part floor scrubber. "
    i "Not exactly a glamorous life I’m leading, is it?"
    s "No, but it fits you."
    i "I know that's probably supposed to be a compliment but it makes me feel kind of gross."
    s "I just mean that I admire how you do the things you want to do without letting societal norms get in your way."
    i "I think it’s closer to me just avoiding ever figuring out what those societal norms are, but yeah. I’m gonna do what I want to do."

    scene iofirstdorm15
    with dissolve

    i "Which is why I’m more than happy to take up your time when there are plenty of other girls hoping you’ll knock on {i}their{/i} doors instead of mine."
    i "I win, even if it’s only for tonight."

    scene iofirstdorm14
    with dissolve

    i "So, if there’s anything I can make to show you that I’m worth your time, feel free to let me know."
    i "If not, I’ll probably just wind up making a third wardrobe and the room will look like even more of a trainwreck."
    i "It {i}would{/i} be nice having somewhere to put {i}my{/i} clothes, though."

    "Something Io said jumped out at me there."
    "“To show you that I’m worth your time,” is a phrase that, when isolated, looks remarkably self-deprecating."
    "And when paired with her tendencies to call herself trash or whatever it is she’s spouted before, it makes sense."
    "But the issue with dissecting small parts of dialogue like that and using them to assign attributes to people is that sometimes people deviate."
    "Maybe her offer to create something for me is less self-deprecation and more just the desire to please?"
    "I should ask her."

    s "Do you really think you’re not worth my time?"

    scene iofirstdorm16
    with dissolve

    i "Hm? What do you mean?"
    s "You offered to make me something to show me that you're worth it. What did you mean by that?"
    i "Hey. Speaking unfiltered thoughts is my job. You’re supposed to be the sponge."
    s "Sometimes, you’ve gotta wring the sponge out to make room for more liquid."
    i "This is a really weird analogy. I’m getting uncomfortable."
    s "Yeah, that sounded better in my head."
    s "I’m just trying to figure out more about you in the least intrusive way possible, I guess."

    scene iofirstdorm17
    with dissolve

    i "That’s a good strategy. "
    i "To clarify, I {i}can’t{/i} exactly think I’m not worth your time because I don’t quite know what your time is worth."
    i "But Henry David Thoreau once said-"

    scene iofirstdorm18
    with dissolve

    i "{i}Be not simply good; be good for something.{/i}"
    i "And so it’s important that we all make some sort of impact in the lives of others."
    i "If I can create something that changes your life, or even your daily ritual, I will be able to make a difference...albeit a relatively minuscule one."
    i "I’ll move one step closer to “good for something” rather than just a slowly dying flesh-compound who spends her nights picking splinters out of her fingertips."

    scene iofirstdorm19
    with dissolve

    i "You feel me?"
    s "I feel like I understand you less and more at the same time."
    i "Heheh~ Let me show you something else and probably confuse you even more, then."

    scene black
    with dissolve

    "Io gets off the chair and walks over to a small shelf full of miscellaneous objects near the door."
    "She moves aside a few books, knocking what sounds like loose change onto the floor, before returning and brandishing a strange looking figure before me."

    scene iofirstdorm20
    with dissolve2

    i "Did you have any toys you played with as a kid, Sensei?"
    i "Do you even remember things from back then?"
    s "…"
    i "You don’t, do you?"
    i "You know, many popular psychologists say that memory loss can be the result of repeated trauma."
    i "Of course, this isn’t me insinuating that that's what’s going on for you, but it {i}is{/i} a thing that happens."
    i "Without getting more off the rails, the point I’m trying to land at is that the first few years of your life are irrefutably the most important."
    i "A lot of kids these days would look at something like this little guy and think, “What am I supposed to do with it?”"
    i "“How can I have fun with this?”"

    scene iofirstdorm21
    with dissolve

    i "But then, there are a handful of kids without anything."
    i "A handful of kids who would take something like this in their tiny, little hands and give it a name."
    i "Give it value."
    s "Were you one of those k-"
    i "I’m one of them now, Sensei."

    scene iofirstdorm20
    with dissolve

    i "This isn’t something I leaned on when I was growing up or anything like that."
    i "It’s something I {i}made{/i}. "
    i "Something that {i}could{/i} be that much-needed solace for someone in dire straits."
    i "But instead of being in anyone else’s hands, it’s collecting dust on a shelf in my room alongside several others just like it."
    s "Why, though?"
    s "Why not give it away if you think it can help someone?"
    i "Why?"

    scene iofirstdorm22
    with dissolve

    i "Because I’m all talk."
    i "Because it’s easy for me to start things but near impossible for me to finish them."

    scene iofirstdorm23
    with dissolve

    i "I’m bad at seeing things through to the end."
    i "I couldn’t even finish my introduction in class the right way."
    i "And yeah, I’m still impressionable...but the only impressions I’ve gotten the last few years are that I need to hurry up and find my place in the world."

    scene iofirstdorm24
    with dissolve

    i "Who knows?"
    i "Maybe I'm just struggling to give this little guy away because he reminds me of myself?"
    i "Collecting dust somewhere and too empty to actually make anyone happy."
    i "The only difference is that {i}I{/i} actually have a name. "
    s "And that he’s made out of wood."

    scene iofirstdorm25
    with dissolve

    i "Heh...Yeah. I guess there’s more than just one key difference if you want to state the obvious."
    i "I’m a lot taller than him too. And a little better at talking to people."
    s "Jokes aside, if you need something or someone to lean on, I’m sure both Uta and myself would be viable candidates."
    s "I also wouldn’t mind helping you find a use for your apparent collection of unnamed wooden robots."
    i "I’ve got the numbers for two nearby orphanages saved in my phone if you want them."
    i "I figured I could donate a lot of the stuff I make to charities but then I look at it all and second-guess myself."
    i "Funny, huh? "
    i "I went as far as mentioning that things like this could save lives or whatever but I don’t even believe it myself."
    i "They’re just...wooden blocks at the end of the day."
    s "You prepared {i}that{/i} much and still didn’t finish the job? Just donate them, Io."

    scene iofirstdorm26
    with dissolve

    i "I’ve got a problem, okay? "
    i "I want to make a difference but I’m too scared to actually do it. "
    s "Well, at least you understand your fatal flaw. That’s more than most people can say."

    scene iofirstdorm27
    with dissolve

    i "…"
    i "Fatal flaw, huh?"
    i "If only it were just one."

    scene black
    with dissolve2

    "Io shows me a few other toys she’s made for the purpose of making other people happy and I’m extremely impressed by the level of detail in some of them."
    "She's right about one thing, at the very least."
    "Objects like this aren’t really appreciated by kids anymore."
    "Which is extremely depressing given how much thought I know Io has put into making them."
    "But they serve no purpose collecting dust in an overly-cluttered dorm room."
    "They’d be better anywhere else-"
    "Just like many of us."
    "The only issue is getting them there."
    "…"
    "Io starts dozing off an hour or two later and I decide to leave and let her get her rest."
    "She thanks me a bunch of times for “putting up with her” and, once again, displays another weakness of hers."
    "I think I’m beginning to understand just how many of those there may be."
    "At the same time, though, it’s admirable how much effort she’s putting into living up to her ideals."
    "It’s rare to find someone so strong and weak at the same time."
    "I just hope that both extremes wind up cancelling each other out so that she, one day, finds a trace of normalcy in this shithole we call life."

    $ renpy.end_replay()
    $ io_love += 1
    $ iodorm5 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm10:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm:
    if io_love >= 5 and bathhouse5 == True and iodorm5 == False:
        jump iodorm5
...
```