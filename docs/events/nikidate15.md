# Hotel Rooms (Niki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Niki love greater than or equal to 15

* Event [Thousands, If Not Millions](./nikidate10.md) (Niki) is completed)

* Day of week is Saturday

* nikinumber equal to True (unknown variable)



## Next events

* [Main: Girls in Spandex](./halloweentwo1.md)

## Event properties

* Id: nikidate15
* Group: Niki
* Triggered by label: callnikinight
* Triggered by branch label: callnight
* Triggered by path: callnight->callnikinight->nikidate15

## Official wiki page

[Hotel Rooms](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikidate15&go=Go) for more details.

## Event code

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikidate15:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "I know it’s a bit of a long shot trying to get her to hang out this late at night, so I am prepared for the worst."
    "Just...the “worst” in this case is simply calling someone else and seeing what they’re up to instead."
    "And, in the event that I am unable to go the rest of the night without the color pink, I’m pretty sure Noriko should be working. And she always accepts my presence."
    "I guess this scientifically proves which Nakayama likes me more."

    play sound "phonebeep.wav"

    q "Hello. Niki Nakayama’s phone. This is her manager."
    s "Weird. I could have sworn I dialed her cell number."
    q "You did. Which is why I answered with, “Hello. Niki Nakayama’s phone.”"
    s "You don’t sound like Niki at all."
    q "I’m- Are you even paying attention?"
    s "Do you have any idea who I am? "
    q "I believe your name was...[nikitemp]? "
    s "As much as I admire the tenacity in both of you still calling me that months later, can you put her on the line?"
    q "I’m afraid Niki is-"
    q "Oh. Wait. Hold, please."
    q "{i}Niki, you’re supposed to go on in five minutes. What are you doing here?{/i}"
    ni "{i}Phone. Now.{/i}"

    "I listen as Niki snatches her phone back and sends her manager away."
    "And, in other news, I think I’m higher on Niki’s priority list than her job now."
    "Probably."
    "Okay, maybe not {i}higher{/i}, but at least-"

    ni "Stop calling me at night. I’m famous."
    s "Are you? I had no idea."
    ni "Ha ha ha. Very funny."
    ni "If you can get to the urban district in five minutes, I’ll let you in for free."
    s "Sure, let me just teleport over there really quick."
    ni "Cool. Just say you’re there for me and they’ll let you in."
    s "It’s your concert. Literally everyone is there for you."
    ni "Jesus, why are you so difficult?"
    s "I’m not even doing anything this time."
    ni "Hah...listen- I have to go on stage now or thousands of people are going to be disappointed."
    ni "But if you want to make your way over to the urban district {i}after{/i} the concert, we can hang out in my hotel. "
    ni "I’m in the master suite at the...Grand Tsukioka...whatever or something?"
    s "I feel as if I’ve heard that name before..."
    ni "Grats. Bye, now."
    s "Wait."
    ni "What? What else could you possibly want?"
    s "Just wanted to say good luck."
    ni "Okay, but what do you {i}really{/i} want?"

    if bonus == True:
        s "To know if I should bring condoms or-"
    else:
        s "If I should bring your grandma's bones or-"

    play sound "phonebeep.wav"

    s "...not."

    scene black
    with dissolve

    "Jokes on her. I wasn’t going to bring them anyway."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene nikihotel1
    with dissolve2
    play music "love.mp3"

    "A few hours go by before I make it to the hotel which, as I've finally remembered, is owned by Toriko Tsukioka, a totally real student of mine."
    "Well, I guess it’s owned by her family, technically. But it wouldn’t surprise me if they’d just...give it to her or something if she asked nicely."
    "Oh yeah, and Niki is here too."
    "And...she’s..."

    s "...Is that my shirt?"
    ni "No. Your shirt had a smaller collar."
    ni "And I’d definitely never borrow it and stretch it out to turn it into a more comfortable pajama top."
    s "After all I’ve done for you..."

    scene nikihotel2
    with dissolve

    ni "Yeah. Thanks so much for all of those years of self-doubt. Appreciate it."
    s "It made you a better person, didn’t it?"
    s "Even if you’re looking a little...different now."

    scene nikihotel1
    with dissolve

    ni "Different for most people, sure. But this is the me you had the pleasure of looking at for pretty much half of your life. "
    ni "If anything, I’d think it would be weirder for you to look at the super...showy version."
    s "Ahh, so this is the {i}real{/i} Niki Nakayama."

    scene nikihotel3
    with dissolve

    ni "Yup. But if you take any pictures or say anything to anyone, I’ll chop your balls off."
    s "Afraid of people finding out you wear glasses?"
    ni "Only losers wear glasses. True story."
    s "I imagine tonight will be incredibly boring, then."

    scene nikihotel4
    with dissolve

    ni "I’m surprised you even came, to be honest. I could have sworn you’d be all like, “Ugh. Too much effort. I’ll just stay home.”"
    s "It’s the least I can do after, as you so aptly put it, “All those years of self-doubt.”"

    scene nikihotel5
    with dissolve

    ni "Woah. That was a really nice thing to say by your standards. I’m impressed."
    s "And {i}I’m{/i} impressed by how that shirt manages to stay on you despite being stretched to twice its original size."

    scene nikihotel6
    with dissolve

    if bonus == True:
        ni "Thanks. You know, it actually used to belong to this one guy I would always hook up with back when I was sexually active and less...sexually inactive."
        s "You’re not sexually active unless you’re actually having sex, Niki."
    else:
        ni "Thanks. Even though I won't be a wizard for another two years, I have already learned some of the powers."
        s "Wow."

    scene nikihotel7
    with dissolve

    if bonus == True:
        ni "Does hand stuff not count anymore? I remember that was kind of a big deal when we were growing up."
        s "Was it? Or were you just a nerd who didn’t understand what all of the cool kids were up to until a few years ago?"
    else:
        ni "Hey, is it just me or is your aura changing colors right now?"
        s "Here you go again with all of the annoying spiritual shit again. This is exactly why we broke up."

    scene nikihotel8
    with dissolve

    ni "Oh, yeah. Like you were one of those cool kids, Mr. I’mgoingtospendeverydayatmyneighbor’shouse."
    s "That is an incredibly long last name and sounds nothing like Arakawa."

    scene nikihotel7
    with dissolve

    ni "Oh, that reminds me. What’s a...Nakayarakawayama? "
    ni "Is that just our last names combined?"
    s "I am...assuming you heard that from Noriko."
    ni "In between declarations of how she was going to “steal you from me,” yes."
    ni "Of course, I had to inform her that you are not {i}mine{/i} to begin with."
    ni "And also that I would tell our parents if she even {i}tried{/i} stealing you from me."
    s "But...didn’t you just say-"
    ni "Do you wanna sit? My legs are a little tired on account of that whole “putting on a show for thousands of people” thing."

    if bonus == True:
        s "An idol in her pajamas, sitting on a bed with a known pervert? What would the news outlets say?"
    else:
        s "An idol in her pajamas, sitting on a bed with the one and only huggy boy? What would the news outlets say?"

    ni "Probably some stuff about how I’m a whore. And how I’m unfit to be a role model for [young_girls] and shouldn’t show my face in stadiums anymore."
    s "Woah."
    ni "Yeah. The idol industry’s rough. I had to fight off a PR nightmare once for just calling some actor cute."
    s "See, this is what you get for looking at someone other than me. "
    ni "You’re not even that cute anymore. The only thing you have going for you is your eyes."
    s "That’s not the {i}only{/i} thing I have going for me."
    ni "…"
    s "I’m referring to-"

    if bonus == True:
        ni "I know exactly what you’re referring to. Hand stuff, remember?"
        ni "If that whole thing about Tsukumogami is real, the old trash can in my room is going to come back and haunt me for all of the jizz-soaked tissues I tossed into it back in the day."
    else:
        ni "The decline of collective responsibility in American poltics?"

    s "Well, this conversation took a turn."

    scene black
    with dissolve2

    "Niki turns around and hops onto the bed, moving aside to allow me on as well. "
    "It’s a much nicer bed than the one we slept in at the beach, but that sort of thing is to be expected in a high class hotel room paid for by Niki’s agency."
    "I imagine she stays in places like this all the time."
    "…"
    "I wonder if she ever gets lonely sleeping in rooms like this without the comfort...or {i}dis{/i}comfort of an ex-boyfriend nearby."

    scene nikihotel9
    with dissolve

    s "…"
    ni "…"
    s "I still can’t believe you destroyed that shirt."
    ni "I still can’t believe you’re so upset about it."
    ni "If it will make you feel better, I’ll give you one of my old idol outfits to stretch out and wear around your house."
    s "I can’t imagine Ami would be very supportive of that new wardrobe choice."

    scene nikihotel10
    with dissolve

    ni "Well, then {i}she{/i} can have them."
    ni "She just needs to grow a little more first. She’s still kinda tiny for her age."
    s "Just don’t say that around her. She’ll cry."
    ni "I know, I know. Lots of girls are sensitive about their size."
    ni "She’s adorable, though. And, who knows? Maybe you’ll scar {i}her{/i} into becoming an idol as well?"
    s "Maybe it's not too late for me to become a producer instead of a teacher."

    scene nikihotel11
    with dissolve

    ni "Nah. You wouldn’t like being a part of this industry."
    ni "Too much...thinking on your feet and...reacting to stuff."
    ni "And, at the end of the day, even on days where you made thousands of people smile...things can still feel a little empty."
    ni "You can never form meaningful relationships with anyone because you belong to the people."
    s "Ah. So you {i}do{/i} get lonely, then."

    scene nikihotel12
    with dissolve

    ni "Hm?"
    s "In hotel rooms. "
    s "I was wondering how many times you must have sat in one of these by yourself. "
    ni "Oh, yeah. All the time."
    ni "It’s definitely lonely, but...not a {i}bad{/i} kind of lonely, you know?"
    ni "I really do like my job. And I like focusing on stuff relating to my job. "

    scene nikihotel13
    with dissolve

    ni "It helps...take my mind off of stuff."
    ni "Not that “stuff” is anything {i}bad{/i} anymore."
    ni "It’s just...stuff..."
    s "I see..."
    ni "Yeah..."
    s "…"
    ni "…"

    scene nikihotel14
    with dissolve

    ni "How about you? Do you ever get lonely? "
    ni "Probably not when you’re surrounded by a bunch of [teenage]girls, right?"
    s "I...guess not? I’m not really sure."
    s "Being around them does help me take my mind off “stuff” as well, though."
    s "And none of them steal my clothes, so it’s already better to hang out with them than it is with you."

    scene nikihotel15
    with dissolve

    ni "Well, gee. If I knew you were going to make such a fuss over it, I would have worn something else."
    s "It’s never too late, Niki. "
    ni "Wanna trade? I like the way the one you’re wearing now looks."
    s "Yeah, probably because you stole the only other one I had and turned it into a pajama tarp."
    ni "You want it back?"
    s "That is exactly what I have been saying since you took it. Yes."

    scene nikihotel16
    with dissolve

    ni "Then..."
    ni "How about you come and get it?"
    s "…"
    ni "…"

    scene nikihotel17
    with dissolve

    ni "Mm! Mnch...mlem...chu...nch...hah...ahh!"

    if bonus == True:
        jump nikihotelx
    else:
        ni "I wish...we were...hugging right now!"
        s "Me...too!"

        scene black
        with dissolve

        "Niki and I give into our unearthly desire to hug and, well, hug each other."
        "I let her keep my shirt because I know how much it means to her."
        "On the way home, I step in a puddle and have to walk home with a wet sock."
        "I didn't really have to tell you that, but I wanted to anyway."

        $ renpy.end_replay()
        $ niki_love += 1
        $ nikidate15 = True

        "{i}Niki’s affection has increased to [niki_love]!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label nikiinvite1:
...
```

## Code that triggers this event

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label callnikinight:
    if niki_love >= 5 and rindorm40 == True and nikidate1 == True and nikidate5 == False:
        jump nikidate5
    if niki_love >= 15 and nikidate10 == True and day == 6 and nikidate15 == False:
        jump nikidate15
...
```