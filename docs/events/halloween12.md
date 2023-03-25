# The Depressing Implication of Goosebumps (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Wicked Witch of Kumon-mi](./halloween11.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween12
* Group: Main
* Triggered by label: halloween11
* Chain sources: halloween11
* Chain sources path: halloween11

## Official wiki page

[The Depressing Implication of Goosebumps](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween12&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween12:
    scene halloweentrio1
    with dissolve
    play music "soda.mp3" fadein 5.0

    c "…"

    "A girl stands alone, pressed up against a wall and dressed in significantly less clothing than she’s accustomed to."
    "Clothing that was meant to impress not only the man she adores but those around her."
    "Not in a cocky way, but in a way that says “I’m comfortable in my own skin.”"
    "As comfortable as one can be, that is."
    "Cold air finds its way out of brand new, industrial air conditioners that line the tops of walls in an otherwise ancient building."
    "That air reaches her legs and causes her to shiver."
    "She gets goosebumps."
    "She’s been extremely susceptible to those since she was a little girl."
    "Her mother was the same way."
    "Her sister, while less susceptible to them, was cursed with a slew of other issues."
    "The one pressed up against the wall wishes it were possible to trade places."
    "Getting goosebumps always makes her think of that."
    "But of course, that isn’t something worth telling anyone."
    "It’s not important at all."
    "Nothing’s important, is it?"

    scene halloweentrio2
    with dissolve

    "A second girl shows up. "
    "Her legs are cold as well."
    "But instead of letting her mind dwell on the depressing implication of goosebumps, she gets caught in thoughts of how fishnet stockings look best on girls with tanned skin."
    "It’s a thought much less personal than the girl on our right has, but it is a thought nonetheless."
    "That thought eventually transitions to how that girl must look underneath her costume, and the girl on our left attempts to break free from yet another sad delusion in the only way she knows how."

    scene halloweentrio3
    with dissolve

    r "Did you know, um...Pac-man was originally called Puck-man but..."
    r "They, umm...wound up changing the name because they realized it would be...too easy to vandalize..."
    c "…"
    c "Isn’t that from a movie?"
    r "…"
    r "Yes."
    r "Hi."

    scene halloweentrio4
    with dissolve

    c "Hey."
    c "Did you come over here because I looked lonely?"
    r "Whaaaaat? Noooo. Of course nooooot."
    r "I just happened to be in the area and...thought I’d drop by to say...you look really pretty tonight."

    scene halloweentrio5
    with dissolve

    if bonus == True:
        c "Oh my God, so do you. I’ve been staring at your thighs all night, I’m not even going to lie."
        r "That’s, umm..."
        r "{i}Do you want to touch them?{/i}"
    else:
        c "Oh my God, so do you. I’ve been staring at you all night. Not even gonna lie."
        r "{i}I have a picture of you that I keep under my pillow.{/i}"

    scene halloweentrio6
    with dissolve

    c "Hm? What was that last part? I couldn’t really hear you."

    if bonus == True:
        r "What? Huh? There was no last part. The conversation ended after you complimented my thighs."
    else:
        r "What? Huh? There was no last part."

    r "I didn’t even respond."

    scene halloweentrio7
    with dissolve

    c "Rin...relax. You don’t need to act so weird around me. "
    c "I’m glad you finally came to talk to me. I’ve been wondering when you were going to all night."
    r "You didn’t...notice me staring at you or anything, did you? Because I totally wasn’t."
    c "You totally were. We kept making eye contact for like, a split second before you'd turn away."
    r "That doesn’t sound like a thing I would do at all."

    scene halloweentrio8
    with dissolve

    c "That aside...are you having fun tonight?"
    r "I am, yeah...I kind of love Halloween."
    c "Yeah, I kinda figured as much with all the skulls you wear and stuff."
    r "You don’t really...seem to be having a good time, though."
    r "Could Yumi not make it? "
    r "You could have come...sat with us if you wanted."
    r "It’s just been Futaba and me for the most part."
    r "Molly pops in to say hi every few minutes but then just awkwardly walks away a few seconds later."
    c "Heh~ Thanks for the offer. I’ll keep that in mind for the rest of the night."
    c "Yumi’s actually on the way, though, so I think that might make things a little awkward for Futaba. Poor girl."

    scene halloweentrio9
    with dissolve

    r "Hey, you wouldn’t happen to know...{i}why{/i} Yumi is always that mean to her, would you?"
    r "I tried asking her on the beach and it didn’t really go well."
    c "I really wish I did. "
    c "Literally the only thing I can think of is that Futaba doesn’t really stand up for herself. "
    c "But that alone isn’t good enough reason to constantly bully somebody."
    c "Not like, there {i}is{/i} a good reason to do that or anything. I just don’t really understand Yumi sometimes."

    scene halloweentrio10
    with dissolve

    c "Did you know it’s her birthday tonight?"
    r "Yumi was...born on Halloween? That's so cool."
    c "That she was. Such a waste that she’s never even dressed up for it."
    r "So she’s coming to the party in her normal clothes? Like Sensei?"

    scene halloweentrio11
    with dissolve

    c "Pretty sure, yeah. "
    c "We better be careful or the two of them might bond over their shared interest in always being buzzkills."
    r "Yeah, right. Those two? They have just about as much of a chance as Maya and...literally anyone."
    c "I’ve never really talked to Maya before. Is she really that unapproachable?"
    r "She’s not unapproachable, she’s just...Maya."
    r "It’s hard to explain."

    scene halloweentrio12
    with dissolve

    "A third girl shows up at the party, several hours late, and takes a spot between the two star-crossed lovers."
    "She has no costume, nor intent to don one, but is instead dressed in clothes that her mother used to wear before walking out on her."
    "But even if the girl in the center can’t seem to get over that small yet significant part of her life, she still needs clothes."
    "Because she, too, gets goosebumps easily."

    c "Finally! I was wondering when the Hell you were going to show up."
    c "Also, where are your manners? You totally just stepped between Rin and me while we were in the middle of a conversation."
    c "I’m cool with you blowing {i}me{/i} off but at least say hi to her or something."

    scene halloweentrio13
    with dissolve

    y "Hey."
    r "...Hey."
    y "You look nice."

    scene halloweentrio14
    with dissolve

    r "U-Umm! Thanks..."

    scene halloweentrio15
    with dissolve

    y "..."
    c "...?"
    y "You look like a slut."
    c "..."
    y "..."

    scene halloweentrio16
    with dissolve

    c "Mm..."
    y "What?"
    c "Aren’t best friends supposed to like, you know, compliment each other instead of making them feel like trash?"
    y "…"
    y "Are they?"

    scene halloweentrio17
    with dissolve

    c "Hah..."
    c "Is Chinami asleep?"
    y "Yeah. "
    c "Did she remember your birthday at least?"
    y "She remembered that you told her to remember it."
    c "And I see that she didn’t remember to not tell you I told her that."
    y "Nope. "
    y "It’s whatever, though. It’s just a day and she’s just a kid."

    scene halloweentrio18
    with dissolve

    r "Happy birthday, Yumi."
    r "I’m sorry for getting all pissy with you on the beach."
    y "Thanks. And it’s whatever. I deserved it. I was a bitch that day."
    y "I mean, I’m a bitch most days, so it’s cool. "
    r "How old are you now, if you don’t mind me asking?"
    y "I’m-"

    scene halloweentrio19
    with dissolve

    c "Oh, before you answer that question, I was wondering if you saw Sensei on the way in."
    c "He’s been gone for a while now and I thought he might be out there."
    y "If you’re worried about where he is, why don’t you just go look for him?"

    if bonus == True:
        y "He’s probably fist deep inside of one of the other girls right now."
    else:
        y "He’s probably off hugging one of the other girls right now or some shit."

    scene halloweentrio20
    with dissolve

    if bonus == True:
        r "F-Fist?!"
    else:
        r "H-Huging?!"

    c "Bullshit."
    y "Think whatever the fuck you want to think. "
    y "Who else is missing right now? The rich girl? Class president?"

    scene halloweentrio21
    with dissolve

    r "Well...Yeah, Makoto’s been gone for a while, too. But I don’t think they left together, did they?"
    r "And even if they did, it’s Makoto. She’s probably just making him do...teacher stuff or something."
    c "The two of them basically set up the entire party, so they probably went to go get some more...drinks or something."
    y "Sure, whatever. Sorry for not telling you exactly what you wanted to hear. Please forgive me."

    scene halloweentrio22
    with dissolve

    c "Whatever. I’ll let it slide since today is your birthday."
    c "But no more saying mean things about the people I like."
    y "You fucking like everyone. You’ve gotta at least let me talk shit to somebody."
    c "I give you permission to talk shit to Chinami."

    scene halloweentrio23
    with dissolve

    y "Wha-"
    y "You know I can’t fucking do that!"
    c "That’s exactly why I gave you permission to do it."
    y "I don’t...need your fucking permission for anything! "
    c "Yes you do or I’ll take your phone away."

    scene halloweentrio24
    with dissolve

    r "Chinami is...Chika’s little sister, right?"
    r "Are you good with kids, Yumi?"
    y "Not especially. I just hang out at Chika’s place all the time and she’s always there so...we know each other."
    c "Yumi’s just being tsundere. She likes Chinami even more than she likes me."

    scene halloweentrio25
    with dissolve

    y "I just fuckin’ said it’s only cause I hang out at your place!"
    y "Just cause I won’t fuckin’ curse at a kid doesn’t mean I’m good with ‘em or like ‘em or anything! Give me a break!"
    r "I had no idea you had a cute side, Yumi."

    scene halloweentrio26
    with dissolve

    y "I don’t! The fuck is up with you two?!"
    y "I didn’t come all the way here just to get fuckin’ teased!"
    y "You have any idea how long that walk was?"

    scene halloweentrio27
    with dissolve

    c "Wait, you {i}walked{/i} here? Is that why it took you so long?"
    c "I left you money for the bus. What happened to it?"
    y "I used it for something else."
    y "Don’t sweat it. I’m here now and I’ll ride the bus home with you as long as you’re paying."

    scene halloweentrio28
    with dissolve

    r "Can I...ride back with you guys, too?"
    r "I mean, we literally live in the same building, so it would make sense."
    r "And Futaba is going to be staying at a friend’s place tonight, so it won’t be awkward or whatever."
    y "Do whatever the fuck you want. I don’t care."
    y "Just put a fuckin’ hoodie or something on so you’re not flashing everybody on the bus."

    scene halloweentrio29
    with dissolve

    y "Same goes for you."
    c "You mean you {i}don’t{/i} want to be sandwiched between two beautiful, barely-dressed girls like you are right now?"
    y "No. In fact, this feels really fucking weird for me."
    y "And it doesn’t help that you’ve both been staring at me pretty much this entire time."
    c "You look so cute in those clothes, though~"

    scene halloweentrio30
    with dissolve

    r "Agreed. And I’m kind of an expert when it comes to calling girls cute."
    r "Even if I have zero experience with both men and women."
    y "The fuck does that even mean?"
    r "It’s probably best for all of us if you don’t look into it."

    scene halloweentrio31
    with dissolve

    y "Ugh...fuck it. I’m just gonna go get some food."
    c "Noooo don’t leave us, we’ll miss you~"
    r "I already do miss you! In an extremely platonic way, though. Obviously."

    scene halloweentrio32
    with dissolve

    c "Hehe~"
    r "Hahah...hah..."
    c "You might be a natural when it comes to teasing Yumi. Well done, Rin."
    r "You might be a natural at being...beautiful and stuff."
    c "Is that your pickup line for tonight?"
    r "Depends. Did it work?"
    c "I’d offer to let you come feel my heartbeat and check but I’m pretty sure you’d rip my costume off."
    r "To be honest, I’d probably pass out the second I smelled your perfume."
    c "It’s rosewater, actually."
    r "And lemon. You forgot the lemon."

    scene halloweentrio33
    with dissolve

    c "Holy crap, how do you know that?"
    r "Oh! Umm, my sense of smell is just...really good! "
    r "I totally haven’t looked through your bag while you were in the shower or anything!"

    scene halloweentrio34
    with dissolve

    c "Oh my God...you’re hilarious."
    r "Hahah! Yeah! So funny!"
    r "I’m gonna go die now! See you later, Chika!"

    scene halloweentrio35
    with dissolve

    c "Pfft~"
    c "Why {i}me{/i} of all people?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ halloween12 = True

label halloween13:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
mak "I just can’t look down because seeing my own blood makes me nauseous."
    s "Yeah definitely don’t look down."
    mak "I’m trying...but it gets me really excited...thinking about how something that big...is fitting inside of me..."
    mak "This is...so much better than porn...isn’t it...Sensei?"
    mak "Now you can have...the real thing...instead of just...the girl that looked like me..in that DVD you stole..."
    s "I didn't {i}steal{/i} that DVD, Makoto."
    s "And I thought you said the girl didn’t look like you?"
    mak "She doesn’t..."

    scene makotohalloween31
    with dissolve

    "Makoto relaxes her body as her deep, pained breaths turned into ones that make it sound like she’s trying to calm herself down."
    "Of course, I’m sure that’s exactly what they are."
    "So I focus on her body and try to bring myself to climax to prevent further harm to her."

    mak "Ahh...ngh...[makotomaster]..."
    mak "I’m not...a virgin anymore..."
    mak "I’ve got...your cock inside of me..."
    mak "And you’re gonna...cum on me...any minute now..."
    mak "And then...no one is gonna...ngh...know about it..."
    mak "We’re so naughty...aren’t we?..."
    mak "Sneaking away at a party and...doing something like this..."
    mak "I’m glad it was me and not...somebody else..."
    s "Makoto..."

    scene makotohalloween32
    with dissolve

    mak "Gonna...cum...[makotomaster]?..."
    mak "Make sure you...pull out..."
    mak "You wouldn’t want to...have a baby with someone like me...would you?..."

    "I lock eyes with Makoto as a pressure builds up deep within me."
    "Feeling the outline of her hole rub against the tip of my cock, which is basically all I’ve been giving her for the last few minutes-"
    "I finally give in and pull out at the very last second..."

    with sexfade
    with sexfade
    scene makotohalloween33
    with cumflash
    with hpunch

    "Makoto does not climax along with me- and I don’t blame her."
    "I can’t imagine that she felt good at all during any of this."
    "There is no orgasmic final breath or back-arching to help her body catch all of my semen."
    "I just slide out of her and finish myself off all over her chest."

    scene makotohalloween34
    with dissolve

    mak "Hah...hah...hah..."
    mak "Ahh...mmn...are we...done?..."
    s "Do you not notice what you’re covered in right now?"
    mak "Still can’t...look down..."
    mak "Is it...cum?..."
    s "What else would it be?"
    mak "Blood..."
    mak "You...killed me...with your dick...Now...goodbye...forever..."
    s "You’re not dying, Makoto."

    scene makotohalloween35
    with dissolve

    mak "I know that, idiot..."
    mak "If anything...I feel...better than ever..."
    mak "We finally...did it..."
    mak "I’m finally...as close to you as I want to be..."
    mak "And I know...you can feel good...with my body..."
    s "Just {i}good{/i} is selling it short. That was pretty amazing, honestly."
    mak "Heheh~ I’m glad..."
    mak "When is it...supposed to stop hurting?..."
    mak "When can I...finish with you?"
    s "I mean, hopefully next time. "
    mak "Let’s practice soon...just to make sure..."
    s "Just focus on cleaning yourself up first before thinking about the next time we’re going to do this."

    scene black
    with dissolve2

    mak "Of course..."
    mak "Can you get me the box of tissues in the next room over?"
    s "How do you know there is a box of tissues there?"
    mak "I strategically placed it there earlier as part of my trap."
    s "..."
    s "That 'Wicked Witch of Kumon-mi' nickname really works for you, doesn’t it?"

    $ renpy.end_replay()
    $ makoto_virgin = False
    $ makoto_love += 5
    $ halloween11  = True
    stop music fadeout 6.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"
    "{i}While that was happening...{/i}"

    jump halloween12
...
```