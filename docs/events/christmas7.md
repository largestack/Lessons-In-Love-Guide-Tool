# Fireworks, Chicken, and the Innate Fear of Death (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Selfless](./futabalust10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Ami: Living](./amiinvite1.md)
* [Ami: Rising to the Challenge](./amiinvite2.md)
* [Ami: Best Friends Forever](./amiinvite3.md)
* [Ayane: Hail Mary](./ayaneinvite1.md)
* [Ayane: One of Many Rooms](./ayaneinvite2.md)
* [Sana: Purest Intentions](./bar35.md)
* [Makoto: Semblance of a Soul](./makotolust10.md)
* [Futaba: Sonnet 18](./futabainvite1.md)
* [Futaba: Floral Aura](./futabainvite2.md)
* [Futaba: Too Blind To See](./futabainvite3.md)
* [Rin: Sketchy Basement](./cafe40.md)
* [Molly: Onward to Valhalla](./mollycafe15.md)
* [Molly: Unpaid Promotion](./mollydorm15.md)
* [Tsuneyo: Seeds](./ramen15.md)
* [Haruka: Shades of Green](./harukainvite1.md)
* [Haruka: Roses](./harukainvite2.md)
* [Haruka: Unfiltered Tap Water](./harukainvite3.md)
* [Maki: A Fair Trade](./makidate10.md)
* [Kirin: Full Blossom](./kirinlust5.md)
* [Kirin: Too Much, All at Once](./kirininvite1.md)
* [Kirin: No Extortion Necessary](./kirininvite2.md)
* [Chinami: Giant Pool of Jell-O](./chinamidate10.md)
* [Main: Suicide Pact](./day237.md)

## Event properties

* Id: christmas7
* Group: Main
* Triggered by label: futabalust10
* Chain sources: futabalust10
* Chain sources path: futabalust10

## Official wiki page

[Fireworks, Chicken, and the Innate Fear of Death](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas7&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label christmas7:
    scene lastchristmas1
    with dissolve
    play music "stpartynight.mp3" fadein 7.0

    t "I come bearing news."
    s "What kind of news? What’s going on?"
    t "We are under attack."
    s "Excuse me?"
    t "The sky is exploding."
    t "There are so many bright colors."
    t "I wanted to tell you I love you before we die."
    s "Those are called fireworks and they’re used to celebrate holidays. We’re not going to die."
    t "Oh."
    t "Well this is awkward."
    s "You don’t...actually love me. Right?"
    t "Is love the feeling you get when you want to feed someone noodles until they grow large and powerful?"
    s "In your case? Probably."
    t "Then I am in love with the whole class."
    t "How will I ever fund this wedding?"
    s "Is there any other reason you came up here? Or was it really just to seek shelter from some harmless, brightly colored lights?"
    t "I was told to bring you downstairs."
    t "I had assumed it was because someone wanted you dead, but I no longer think this on account of the fireworks."
    s "Well thank you for coming up to execute me."
    t "Merry Christmas. Now die."
    s "Yeah, I’m going to have to pass."

    scene lastchristmas2
    with dissolve

    t "A joke. "
    t "It’s okay if you stay alive."
    s "That might be the nicest thing you’ve ever said to me."
    s "You’re even smiling and everything."
    t "My face feels strange."
    t "Is this what they call Christmas Spirit?"
    s "Nope. Like I said, that’s a smile. "
    s "You should do it more often. You look cute when you’re actually emoting."

    scene lastchristmas3
    with dissolve

    if bonus == True:
        t "This is the first holiday I have ever spent with girls my age plus one older man."
    else:
        t "This is the first holiday I have ever spent with actual friends."

    t "It was so enjoyable that I will not smile again until next Christmas."
    t "I must preserve these feelings as if they were pickled garlic."
    s "Weird metaphor but sure, do whatever you want."
    s "Are you coming back downstairs with me?"

    scene lastchristmas4
    with dissolve

    t "To the war-zone?"
    s "Again, it’s not a war-zone."
    t "Are we not currently engaged in a space war?"
    t "How can you be sure the explosions are not coming from that?"
    s "Because this happens several times every year. It’s a celebration."

    scene lastchristmas5
    with dissolve

    t "War is no reason to celebrate, bro."
    t "Something bad is going to happen and you will be too busy using all of your smiles to prepare for it."
    s "Don’t say ominous things like “Something bad is going to happen.” Do you know how many red flags it raises when someone like you does that?"

    scene lastchristmas1
    with dissolve

    t "I don’t have a flag."
    s "…"
    t "That was-"
    s "A joke, I know. It wasn’t a good one."
    t "Well they can’t all be award-winners, you bastard."
    s "One would be nice."
    t "Knock-knock."
    s "What?"

    scene lastchristmas6
    with dissolve

    t "Mn..."
    t "I was prepared for you to say “Who’s there?”"
    t "The Emerald Guardian did not train me on what to say in the event of an emergency like this."
    s "I’m going downstairs now, Tsuneyo. "

    if futabalust10 == True:
        "I turn to the bathroom and shout at the door, wondering if Futaba will be finished cleaning {i}me{/i} off of her clothes any time soon."
    else:
        "I turn to the bathroom and shout at the door, wondering if Futaba will be finished any time soon."

    s "I’ll be outside whenever you finish in there."
    f "Oh...okay! Just give me a...few more minutes."
    t "Sensei, you have not heard the rest of my joke."
    t "Please finish this job so that I may rest in peace."
    s "Will finishing the joke kill you?"
    t "No, but it is sure to kill you."
    t "With humor."
    s "…"
    t "…"
    s "Who’s there?"

    scene lastchristmas1
    with dissolve

    t "Tsuneyo Tojo, soup warrior."
    s "…"
    t "…"
    s "That’s it? That’s the joke?"
    t "Unexpected, wasn’t it?"
    t "It is what the Emerald Guardian calls an “anti-joke.” "
    t "I am so bad at being funny that I must now be purposely {i}not{/i} funny when using comedy."
    t "This is what my life has become."
    s "Can I leave now?"
    t "No."
    s "Why?"
    t "The war. And other things."
    s "I’ll be fine..."
    t "Okay, but don’t come crying to me when you die."
    s "I will be sure not to..."

    scene black
    with dissolve2

    "I need to step around Tsuneyo, who adamantly refuses to move for some reason."
    "I’m not sure why she was being so weird, but-"
    "Wait, what am I talking about? She’s always weird. This is no different from talking to a bird or...pulling a knife on me in a restaurant."
    "If anything, being afraid of fireworks is even...{i}less{/i} weird."
    "I mean, look at Miku. She’s probably tucked away in some private room right now having her head rubbed by her best friend."
    "Maybe Futaba will be generous enough to rub Tsuneyo’s head when she comes out of the bathroom."
    "That might be beneficial for all of us."
    "………"
    "……"
    "…"
    "I walk out to find the charred bodies of all of my students, burnt to a crisp from space-explosions that found their way to Kumon-mi."
    "I pray for each and every one of them and then toss their bodies into the ocean."
    "They decompose and feed a grand total of 6,743 fish over the course of their time in the water."
    "The fish are then captured and eaten by humans."
    "Then eventually wind up back in the ground and grow into beautiful, tall trees."

    scene lastchristmas7
    with dissolve

    "Just kidding."
    "I walk past Rin and Maya and make my way over to Ami, who starts frantically waving at me the second the stray light of the fireworks hits my slightly-thicker winter shirt."

    a "Yay! You made it!"
    s "I was only like, two minutes away. Of course I made it."
    a "Why didn’t you come out as soon as we heard the first bang? You love fireworks."
    a "We always used to watch them together at all the festivals and stuff. Remember how you’d always let me sit on your shoulders?"
    s "Do you want to sit on my shoulders now? Is that what’s going on?"
    a "Yes please!"
    s "No."
    a "Why? Literally no one will care."
    s "I can name at least eleven other girls who probably would."

    scene lastchristmas8
    with dissolve

    a "But I’m the {i}main{/i} girl. Even if hearing that would break Molly’s little Irish heart into like seven trillion pieces."
    s "Where is Molly anyway?"
    a "Oh, she got really upset when Rin yelled at her and stormed off to go play games in the bathroom."
    a "That’s just what she does when she gets all sad and stuff. "
    a "I wish that worked for me. I just cry and eat instant noodles until I feel better."
    s "Yeah, that’s a much more adult way of handling your problems. "
    s "How is Rin taking it?"
    a "Rin? She’s fine. I think she was just surprised."
    a "Also, Ayane is dead now. I murdered her and dumped her body behind the hotel."
    a "Please don’t go looking for her."
    s "That’s a pretty intense reaction to just a kiss- especially with someone you’ve kissed before."

    scene lastchristmas9
    with dissolve

    a "This again?! I thought I just misheard you before."
    a "I have no idea what you’re talking about. Why would Ayane and me have ever done something like that?"
    s "Wait, are you being serious?"
    a "Of course. When have I ever lied to you?"
    s "Who knows? For all I know you could be lying right now."
    a "I’m not smart enough to lie in advance about stuff like that."

    "Would Ayane really lie about something as...specific and strange as that?"
    "Why?"
    "I mean, it’s definitely possible Ami just...isn’t remembering this."
    "The two of them were a lot younger after all."
    "And I remember literally nothing about my childhood, so..."
    "I guess the only way to ever find out would be to go back in time."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene lastchristmas10
    with dissolve

    m "You’ve seemed quite wrapped up in your phone all night."
    m "Is everything okay?"
    r "Oh, totally. I’m just talking to a friend or whatever."
    r "It’s that beginning part of the friendship where if you stop texting each other for like two minutes, the other one starts getting crazy anxiety and thinking you hate them."
    m "That does not sound like a normal friendship. "
    m "You know it very well could just be you who feels that way, right?"

    scene lastchristmas11
    with dissolve

    r "Is that code for that I’m probably coming on too strong and am going to ruin everything?"
    r "Oh God, she hates me doesn’t she?"
    r "She’s only pretending to like me to get me to go away."
    m "That...also doesn’t make sense."
    m "I just don’t think you should spend your entire Christmas on your phone when you have plenty of other friends here."

    scene lastchristmas12
    with dissolve

    r "Woah! Maya-advice!"
    r "Is this what it feels like to be Sensei?"

    if bonus == True:
        m "I don’t know. Do you suddenly have the urge to [molest] the entirety of our class?"
    else:
        m "I don't know. Are you currently repressing any memories of a romantic relationship with me?"

    r "…"
    m "…"

    scene lastchristmas13
    with dissolve

    r "…"
    m "…"
    m "Hah..."

    scene lastchristmas14
    with fade

    a "Oh, Sensei."
    a "I know you’re not the one who paid for it or set it up or...probably even enjoyed it at all in any way-"
    a "But thanks for spending Christmas with me like this."

    "The sound of the fireworks slowly begins to die out."
    "The night is coming to an end."

    a "It was really nice being able to share such a special day with all of my friends and..."

    scene lastchristmas15
    with dissolve

    a "And the one person I care about more than anything else in the world..."
    a "Every Christmas we spend together, it’s like...just a huge reminder of how important you are to me."

    scene lastchristmas16
    with dissolve

    r "Hm? A call?"
    a "And I know that probably makes it sound like you aren’t {i}usually{/i} important to me, but that’s definitely, {i}definitely{/i} not the case."

    play sound "phonebeep.wav"
    scene lastchristmas17
    with dissolve

    r "Hello?"
    a "So...if it’s not much of a bother...I’d like to maybe...have an extra Christmas with you or something?"
    a "One with just the two of us, where I...won’t have to kiss Ayane and stuff..."

    scene lastchristmas18
    with dissolve

    a "And...and we could watch movies and bake cookies! And cuddle under the blanket!"
    a "And...eat other stuff! And spend lots of time together! And-"

    scene lastchristmas19
    with hpunch
    stop music

    r "WHAT?! NO WAY!"
    a "Huh?"
    a "What’s going on over there?"
    r "Yeah, yeah. Definitely. "
    r "I’m glad you’re okay. "
    r "…"
    r "Uh-huh."
    r "…"
    r "Gotcha."
    r "I’ll talk to you soon."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    play sound "phonebeep.wav"

    scene lastchristmas20
    with dissolve

    m "Is everything okay?"
    r "Dude..."
    r "My friend’s[school] just..."
    r "Collapsed."
    m "...Pardon?"
    r "Apparently there was a huge sinkhole that just swallowed the whole thing up."
    r "They can’t even see the bottom so they have no idea how far down it goes."

    scene lastchristmas21
    with dissolve2

    m "…"
    m "What?"
    r "Yeah..."
    r "It’s winter break so no one was hurt or anything, but that’s still...so fucking crazy."
    r "Like, what if that was our[school]? Or what if we were in it?"
    m "When did this happen?"
    r "A little while ago, I guess. I don’t know. I’ve known just as long as you."

    scene lastchristmas22
    with dissolve

    r "Hah...I’m just glad everyone’s okay..."
    r "That’s so scary, dude. "
    r "You never know when shit like that is just going to happen."
    m "…"
    r "…"
    m "It’s not supposed to."

    scene lastchristmas23
    with fade

    ki "Huh..."
    ki "So it’s actually true."
    ki "Literally no one hurt, though? Isn’t that a little too convenient?"
    y "A[school] blowin’ up in general sounds a little too convenient. I call next."

    scene lastchristmas24
    with fade

    a "Sensei...Uta goes to that[school]."
    a "Do you think she’s okay?"
    s "It was kind of hard to hear from over here but didn’t Rin say nobody was hurt?"
    s "I’m sure Uta is fine."

    "Sounds like a royal pain having to deal with something that serious, though."

    if bonus == True:
        "My heart goes out to any fellow teacher who will now have a significantly more difficult time seducing his students."

    "But it is what it is, I guess."

    scene lastchristmas25
    with dissolve

    m "I’m going home early."
    a "But...it’s Christmas."
    m "Yup."
    a "You’re not worried about Uta, too, are you? Because I’m kind of-"
    m "Goodnight."

    scene black
    with dissolve2

    "I watch Maya walk out into the street. "
    "And then I watch the glow from her cell-phone as she wakes it from sleep-mode slowly blend in with the dark."

    scene lastchristmas26
    with dissolve

    r "Oh, Sensei. Hey."
    s "Hey. Are you okay? "
    r "Me? Yeah, I’m fine. Just thinking about how easy it would be for any of us to die at any moment."
    s "So the usual?"
    r "Pretty much, yeah."
    ay "What’s the matter? I heard a commotion from around the corner but I have no idea what’s going on."
    s "Some other[school] collapsed or something."

    scene lastchristmas27
    with dissolve

    ay "Oh my God...Is everyone okay?"
    sa "Rin...are you-"
    r "Yeah, totally cool. No worries at all."
    mo "And, umm, I know you’re probably still mad at me, but if there’s anything I can do to help, just-"
    r "Again, I’m fine. You guys are blowing this out of proportion."
    r "Yeah, it’s scary. But it’s just a[school]. You’re all acting like my friend died or something."

    scene lastchristmas28
    with dissolve

    sa "Maybe...um...since the fireworks are over..."
    sa "We can start packing up and...go back to the dorms..."
    s "No one was staying over tonight? Don’t you guys have the room until tomorrow?"
    r "Futaba and I were going to stay."
    r "Molly was too but now I’m kind of afraid she’s going to [rape] me."

    scene lastchristmas29
    with dissolve

    mo "I’m not a [rapist]! Just a girl who listens to what fate wishes of her!"
    r "I’m kidding, Molly. It’s fine. "
    r "Let’s all just start packing up and whoever stays behind, stays behind."

    scene black
    with dissolve2

    "And so the night comes to a close without anyone enduring emotional trauma."
    "Sure, I’m positive there are some people several miles away right now who really aren’t feeling great thanks to some recent developments but-"
    "At least everyone I know is safe."
    "Or at least I hope they are."

    if chikalust10 == True and futabalust10 == True and bonus == True:
        "Chika and Futaba both sort of disappeared as soon as I got sexual with them."

    "I wonder if this is some sort of omen? Or maybe a curse?"
    "Either one seems possible- especially since there are no miracles on Christmas."
    "Just fireworks, chicken, and the innate fear of death."
    "………"
    "……"
    "…"
    "{i}Congratulations on completing the special Christmas update!{/i}"
    "{i}Things will now return to normal!{/i}"
    "{i}Well, mostly.{/i}"
    "{i}Please continue to enjoy your stay in Kumon-mi!{/i}"

    $ renpy.end_replay()
    $ christmas7 = True
    jump endofsat



    # This ends the game.

    return
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
"Futaba uses two fingers to slide her panties to the side."
    "I watch them sink into her skin as she pulls them upward, using her thumb to graze the tip of my cock and starts spreading precum around."
    "I start fondling her a bit more aggressively but there’s not much of a change in reaction. "

    f "You can just relax, [futabamaster]. Let me take care of you again."
    f "Think of it as a Christmas present."
    s "Don’t I have to get you something in return, then?"

    scene futabalustten22
    with dissolve

    f "You can {i}get me something{/i} another time. We need to hurry up."
    f "I gave you what you wanted so hurry up and look down at me, okay?"

    scene futabalustten23
    with dissolve

    f "It’s kind of...unfortunate that...you’re going to wind up getting it on my underwear, though..."
    f "I just bought these..."
    f "It’ll come out in the wash but...it seems rude to them to have something that lewd happen just a few hours after putting them on for the first time."
    s "Futaba, focus."
    f "Right, sorry."
    f "Ngh...mmm...mm...[futabamaster]..."
    s "Are you not going to touch yourself?"
    f "Nope...just going to...keep doing this..."
    f "You’re going to...have to live with it..."
    s "Hey, suit yourself. Just thought it might make you a little more comfortable."
    f "There is no situation...where that would...make me {i}more{/i} comfortable..."
    f "Now...hurry up and..."

    "Futaba slides her hips further along the table, pressing my cock against the skin of her stomach."
    "Just like her hands, it’s freezing cold."
    "But it’s not an unpleasant sort of freezing. "
    "It works for this very specific scenario quite nicely."

    scene futabalustten24
    with dissolve

    f "Five-"
    s "What? Five what?"
    f "Time limits excite you. Don’t they? Four-"
    s "I never confirmed that. That’s a thing you just made up a few minutes ago."
    f "No. I can feel it. You’re about to finish. Three-"
    s "Don’t act like you know my body better than-"
    f "Two~"
    s "Futaba-"

    scene futabalustten25
    with dissolve

    f "Zero!"

    with sexfade
    with sexfade
    scene futabalustten26
    with cumflash
    with hpunch

    s "…"
    f "See? I told you it was about to happen."
    s "What happened to one? I didn’t have time to prepare."
    f "You had four full seconds to prepare. And all of the time before that."
    f "What would one more second have done?"
    s "Well I guess we’ll never know, will we?"
    f "Heheh...I guess not."
    f "Now, if you’ll please excuse me, I need to go get this stuff off of me."

    scene black
    with dissolve2

    "Futaba hops off the table and grabs her pants off the ground, walking into the bathroom just moments before-"

    play sound "knock.mp3"

    t "Please help. I must open this door to complete the quest assigned to me. "
    t "I saw the others use a card to open the door, but the only card I have is for the library and it won’t work."
    t "Probably because this isn’t a library."
    t "I feel like a fool."
    t "Please help."
    s "Tsuneyo, do you need help?"
    t "…"
    t "Yes."

    play sound "lock.mp3"
    stop music fadeout 10.0

    "I make my way to the door and let Tsuneyo in, hoping Futaba heard the exchange so she doesn’t walk back out half-naked or something along those lines."
    "Not that that’s a thing I’d expect her to do either way, but still."

    $ renpy.end_replay()
    $ futabalust10 = True
    $ futaba_lust += 1

    "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
    "………"
    "……"
    "…"

    jump christmas7
...
```