# Friend Zone Fight! (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Alive & Active! All Out Athletics!](./dormwar4.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar5
* Group: Main
* Triggered by label: dormwar4
* Chain sources: dormwar4
* Chain sources path: dormwar4

## Official wiki page

[Friend Zone Fight!](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar5&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar5:
    scene friendzonefight1
    with dissolve
    play music "cafe.mp3"

    "I make my way into the cafe to find Ami and Maya and quickly approach-"

    scene friendzonefight2
    with dissolve

    h "..."
    s "..."

    "I make my way into the cafe and decide to talk to Haruka first since this is her business and I just walked in with over ten [teenage]girls."

    h "Well I guess this kind of explains why both Rin and Molly told me they needed off today."

    if bonus == True:
        s "The girls are having a battle to see who gets to sleep with me during the next beach trip."
    else:
        s "The girls are having a battle to see who likes me more."

    h "…"
    h "I’m sorry, what?"
    s "You heard me, Haruka."

    scene friendzonefight3
    with dissolve

    h "They’re going to at least buy stuff, though...right? Because if one or two girls want to just hang out here, it’s totally fine...but you guys are about to take up like half of the store."
    s "I don’t know. Probably?"
    s "Two of them are loaded, so they’ll probably wind up buying stuff."

    scene friendzonefight4
    with dissolve

    h "Cool. Well, as long as you don’t just sit around and make a mess of the place, that’s fine."
    h "Not gonna say no to a bunch of cute girls showing up and-"

    scene friendzonefight5
    with dissolve

    h "Hey, wait. Why is your entire class absolutely adorable? How’d you luck out like that?"
    s "Everyone I know is adorable, Haruka."

    "I wink at Haruka."

    h "…"
    h "No, like really though."

    "The wink doesn’t do much, apparently."

    scene friendzonefight6
    with dissolve

    r "Morning, Haruka! You sure look adorable today."
    s "I don’t think she’s in the mood for compliments. I just tried saying the same thing and she didn’t even have a response."
    h "Bold move to request off and then show up to work, Rin."
    r "I’m a bold girl."
    r "Besides, Otoha and me have to friend zone our teacher so that one of us can sleep with him over the summer."

    scene friendzonefight7
    with dissolve

    h "Wait...what? You have to friend zone him {i}so{/i} you can sleep with him?"
    h "Girls have really changed since I was in [high_school]."
    o "She means sleep in the same room."
    o "Whichever one of us holds off Sensei the longest gains a point for our team."

    if bonus == True:
        r "And whichever team has the most points by tomorrow night gets to tie him up and keep him in our room for the beach."
        s "Wait, I'm getting tied up?"
    else:
        r "And whichever team has the most points by tomorrow night gets to paint his nails and braid his hair!"
        s "Yay, I win either way."

    h "And what does the losing team get?"
    o "Nadda."

    scene friendzonefight8
    with dissolve

    h "Well then I suppose I’ll just have to keep my schedule open so the losing team doesn’t have to go empty handed."
    s "Smooth."
    h "I’m doing this for today’s youth, not myself."
    r "So, do you know how this is gonna work, Sensei?"
    s "Apparently, the two of you are going to try to not fall in love with me or something."
    r "Basically."
    r "You’re going to take turns spending time with both Otoha and me. And if you can manage to get one of us to flirt with you, that person loses."

    scene friendzonefight9
    with dissolve

    o "Technically, one of us can still lose even if we don’t flirt. But that will have to be decided by our totally unbiased roommates."
    s "And...how does that work, exactly? What do Futaba and Nodoka have to do with this?"
    r "Those two know us really well, so they’ll be able to tell when and if we start feelin’ something."
    r "It’s doubtful that either one of them will sell us out, so they’re kinda just there to make sure no one’s cheating or whatever."
    h "Really, why are you so lucky?"
    h "No one has ever had a contest over me before. Let alone one important enough to ditch work for."
    s "I’m not really sure if taking turns being rejected constitutes {i}lucky{/i}, but it’s not like every contest so far has been as anti-Sensei as this one."

    if rinbetrayed == False:
        r "Hey, I’m not anti-Sensei at all! If anything, I’m pro-Sensei! That dude’s the best."

    else:
        r "Yeah. Crazy how there are some girls out there who might be interested in {i}other{/i} people and are actually able to prevent mindlessly throwing themselves at you."
        s "Yeah...crazy."

    s "Either way, I guess we can get started whenever-"
    mi "Sensei! You haven’t congratulated me on my victory yet! Get over here, ya big doofus!"
    h "That girl with the giant jacket just called you a doofus."
    o "Are you just going to let her talk to you like that?"
    s "Absolutely not. I will put an end to this right now. "

    scene friendzonefight10
    with fade

    s "Who are you calling a-"
    s "Oh. Maki is here too. "
    maki "I’m Maki."
    maki "Is what my second daughter says true?"
    s "Second daughter?"
    mi "She’s obviously talkin’ about me. Go on and tell Maki about how I whooped Kirin’s butt so bad that she didn’t even come with us to the cafe."
    s "She didn’t?"
    mi "Nah. Said she had some stuff to do."
    mi "Now, tell her the story."
    mak "Or don’t tell her the story because it would be rude for us to brag about a victory so early on in the competition."

    scene friendzonefight11
    with dissolve

    maki "Or {i}do{/i} tell the story because I want to hear about Miku’s glorious victory."
    mi "See! Tell her I won and stuff!"
    s "Miku won and stuff."
    s "But it wasn’t entirely one sided. The other girl put up a fight. "
    maki "Whaaaaat? Miku absolutely destroyed the other girl and it wasn’t even close to a contest? That’s crazy."

    scene friendzonefight12
    with dissolve

    maki "Great job, second daughter. "
    mi "Thanks, Maki! Couldn’t have done it without your support!"
    s "Those two aren’t always like this, are they?"
    mak "They are, more or less. "
    mak "Miku and I have known each other for a long time, so naturally she’s already...acquainted with my mother."
    mak "Why are you still over here, though? It looks like Rin and Otoha have already set up and are patiently awaiting you."

    "I turn around to find the two of them at different tables across from one another, accompanied by none other than their respective roommates."
    "The thing is, I still don’t really know what I’m supposed to do."

    s "So...do I just like-"

    if bonus == True:
        mak "Just be yourself. You’re an incorrigible lust demon, so whatever you do is bound to be within the confines of what they expect from you."
        s "I am {i}not{/i} an incorrigible lust demon."
    else:
        mak "Just be yourself."
        mak "You're great and trusting and oh-so smart. Anyone would be lucky to even almost date you."
        s "Awww Makoto~"

    scene friendzonefight13
    with dissolve

    maki "Hey! Are you trying to say you have something against incorrigible lust demons?"

    if bonus == True:
        s "Nope. You’re great, Maki. Keep...being you."
        maki "I will! "
        maki "Now go over there and show those girls that they are too [young]for you! And that you would be much better off with a brand new fleshlight from my store!"
        mi "What's a fleshlight?"
        s "Yup. See ya."
    else:
        mak "NO, MOTHER. NO ONE SAID ANYTHING ABOUT THAT."
        s "You're scary sometimes, Maki."

    scene black
    with dissolve

    "I make my way through the store and over to Rin, who’s seated next to Futaba in the back of the cafe. "
    "I figure that it will be easier getting her to cave since I’ve known her for much longer."

    if rinbetrayed == True:
        "Granted, I’ve also absolutely shat all over her trust before. "
        "But even with that, I still feel closer to her than I do with Otoha."
        "Either way, I guess there’s no way to tell unless I try so..."
        "Here goes nothing."
    else:
        "That being said, there’s a much higher chance of me winning her over rather than Otoha."
        "Or...at least I think there is."
        "I guess there’s no way to tell unless I try, so..."
        "Here goes nothing."

    "………"
    "……"
    "…"

    scene friendzonefight14
    with dissolve

    s "Yo."
    r "Sorry, but I don’t want any."
    s "...Don’t want any what?"
    r "Any of {i}that ass{/i}. Now get out of here."
    s "…"
    f "I...am so sorry..."

    scene black
    with dissolve

    "I don’t want to deal with Rin right now, so I go talk to Otoha instead."

    scene friendzonefight15
    with dissolve

    o "Jesus, did you really strike out with Rin already? Or are you here to tell me I won?"
    s "I gave up on Rin for the time being. I’ll be back over there in a few minutes as long as you’re able to resist my overwhelming masculinity and mysterious aura."

    scene friendzonefight16
    with dissolve

    o "…"
    s "…"
    o "…"
    s "…"
    s "God damnit."

    scene black
    with dissolve

    "{i}Meanwhile...{/i}"

    scene friendzonefight17
    with dissolve

    u "Come on! All you have to do is...well, literally anything. "
    u "Just one time and I won’t bother you again for the rest of the tournament. "
    u "Don’t you want Sensei in our room for the beach thingie? "
    i "I don’t even know what “the beach thingie” is, but it very much sounds like a thing I don’t want to go to."
    u "Io! You can’t just keep avoiding everything ever."
    u "There are plenty of nice girls in the class who are more than willing to deal with...you."
    i "That’s great news. Then they won’t mind me wanting literally nothing to do with any of them. "
    i "I’m glad to have such an understanding group of girls in our class."

    scene friendzonefight18
    with dissolve

    u "Can you at least fake it or something? "
    i "Ew, fake it even more than I am by showing up?"
    i "You do realize this {i}is{/i} me faking it, right? I’d much rather be in bed right now."
    u "Io! I really wanna win this..."

    scene friendzonefight19
    with dissolve

    i "Well, good news! If you really want to sleep with Sensei, there are much easier ways of doing it!"
    i "Ways that don’t involve you trying to make me do things you know I don’t want to do!"
    u "That’s not why I want to win..."
    i "Oooooh, okay okay. You just want everyone to like you. Got it."

    scene friendzonefight20
    with dissolve

    u "Tch...whatever. I hate dealing with you when you’re like this."
    i "Hahahahah come on! I’m only like, half-kidding."
    i "But yeah, don't count on me cooperating in any way."

    scene friendzonefight21
    with fade

    if bonus == True:
        r "Hey, welcome back to the cool kids table. Does Otoha want your penis yet?"
    else:
        r "Hey, welcome back to the cool kids table. Does Otoha want to hug you yet?"

    s "Unfortunately, I don’t think so."

    if rinbetrayed == True:
        r "Wow. She already lasted longer than Chika did then. Good for her."
        f "I am...{i}really{/i} sorry..."
    else:
        r "Damn it. "
        r "Oh well. Just keep trying then, I guess."

    s "You know, I never realized how hard it is to flirt with someone when I am literally being forced to."
    r "That’s probs just cause you see me as a friend. "
    r "You can’t flirt with me because you don’t want to break our sweet bromance."
    s "A bromance implies that you’re a male."
    r "Homance, then. Homie romance."
    s "Homance makes it sound like you’re a slut."
    r "The hell do you want from me, man? Not my fault you’re not attracted to me."
    s "I am very much attracted to you, Rin."
    s "Also, sorry if that made this conversation weird, Futaba."
    f "It was...already weird, so..."
    r "If you’re so attracted to me, how come you’ve never asked for my number?"
    r "That’s like step one of picking people up- something I am obviously very experienced with."
    s "Oh. Because I already have it."
    r "…"

    scene friendzonefight22
    with dissolve

    r "Did you give Sensei my number?"
    f "Not...that I’m aware of."
    s "I got it from someone else."

    "Thanks, Haruka."

    scene friendzonefight23
    with dissolve

    r "That’s so weird!"
    s "I mean, it’s not like I went out of my way to get it or anything."
    r "No! It’s weird that you’ve never even sent me a “hey” or anything!"
    r "I was just joking at first, but I guess you really {i}aren’t{/i} attracted to me at all! "
    s "Well, are you attracted to me?"
    r "I can’t answer that question or I’ll probably lose!"
    s "I feel like even saying that should kind of count as a loss."

    scene friendzonefight24
    with dissolve

    f "As Rin’s lawyer, I’d like to ask you to please give us a moment to discuss...strategy with one another."
    f "It seems unfair that most of your time has been spent at this table so far."
    s "Fine. But only because I don’t want to get yelled at anymore."
    r "If this is because I wear basketball shorts to bed, I just want you to know they’re very comfortable and-"
    f "Rin...a moment, please."

    scene black
    with dissolve

    "{i}Meanwhile...{/i}"

    scene friendzonefight25
    with dissolve

    mo "…"
    h "You doing okay?"
    mo "Yeah."
    h "…"
    h "This is probably kind of hard for you to watch, isn’t it?"
    mo "…"
    mo "Yeah."
    h "..."
    h "Hey, want to go outside and talk for a little while?"
    h "Doesn't have to be about them or the contest or anything."
    h "Just...might be good to take your mind off of things."
    mo "..."
    h "..."

    scene friendzonefight26
    with dissolve

    mo "Yeah..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene friendzonefight27
    with dissolve

    ay "So, Touka, how are you adjusting to life outside of your...{i}bubble?{/i}"
    to "…"
    to "I don’t get it."
    to "Is that some sort of joke that commoners tell each other?"

    scene friendzonefight28
    with dissolve

    ay "Well...no. I meant like...cause our families both make bubble wrap."
    ay "And being in a bubble is another word for being sheltered and..."
    ay "The joke really isn’t as funny when I have to explain it..."

    scene friendzonefight29
    with dissolve

    to "Nonsense! I thought it was delightful. An excellent display of your sense of humor, Ayane."
    ay "I somehow feel even less funny after hearing that."

    scene friendzonefight30
    with dissolve

    to "To answer your question...life like this has been rather difficult to adapt to."
    to "Though, I’m sure you know this given that you had to adapt to it yourself. "
    to "I know firsthand how hard that can be now, and I really respect you for being able to fit in so seamlessly at this point."
    ay "Actually, it’s the other way around for me."
    ay "My family was pretty poor for a long time before my dad’s invention took off."
    ay "So if anything, I’d probably have a hard time getting used to that rich girl lifestyle you grew up with."

    scene friendzonefight31
    with dissolve

    to "Is that so?"
    ay "Yup! And, like I told you in class the other day, the whole rich person thing isn’t really my style."
    ay "I like it a lot living like this. "
    ay "I mean, I get to use my dad’s credit card to buy pretty much anything I want, so it’s not like I’m {i}not{/i} gonna take advantage of that-"
    ay "But still. I don’t think I’d {i}need{/i} it. "
    ay "And I’m sure that sooner or later, you won’t have to rely on wealth either."
    to "…"
    ay "…"
    to "Thank you, Ayane. I really appreciate that."
    to "Also, have you seen Yasu anywhere? She tends to wander off when I take my eyes off of her..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene friendzonefight16
    with dissolve

    o "Welcome back. I’m still not interested."
    s "Not even a little?"
    o "Can you score me front row seats to a Hikaru Utada concert?"
    s "I don’t even know who that is."
    o "Then no. Not interested."
    s "What if I told you that I’m not like everyone else who’s ever confessed to you?"
    o "Well, yeah. I don’t normally hang out with old people."
    s "I meant that I’m actually interesting."

    scene friendzonefight32
    with dissolve

    o "Pfft! Ahahahahaha! You! Interesting! Hahaha! "
    o "At least you’ve got a sense of humor!"
    s "…"
    o "Hahaha...hahah...hah..."

    scene friendzonefight33
    with dissolve

    o "You were being serious."
    s "I mean, I think I’m at least mildly interesting in the fact that I don’t really think the way anyone else does."
    o "Neither does Nodoka and you don’t see me hooking up with her every night."
    no "You know where to find me~"
    o "See? I can completely resist her and she’s a lot cuter than you are."
    o "Least when she’s not hopped up on caffeine."
    s "Well then how the hell am I supposed to end this tournament thing? "
    s "You’re completely uninterested and Rin apparently has a lawyer that is now going to prevent her from saying anything remotely incriminating."

    scene friendzonefight34
    with dissolve

    no "Oh. I didn’t realize Futaba and I were actually allowed to participate in that way."
    no "I was planning on spending the morning basking in the glorious scent of coffee, but now that I know Futaba is {i}getting involved{/i}, allow me to do the same."
    o "What are you talking about? I don’t really need help fending Sensei off."
    no "I know you don’t. But there’s an easy win condition for Sensei that could end this competition in the blink of an eye."
    no "He's likely just so smitten by all of us beautiful [young_girls] that he's yet to discern it."
    no "It would also elicit quite the reaction if he were to employ it, so I’d be happy to see him try."
    s "If you have some secret trick to picking up girls, please inform me. It would save me an extraordinary amount of time, all things considered."
    no "I can’t make anyone fall for you that won’t already fall for you of their own volition. "
    no "But, and don’t let this shock you too much, I am extremely in tune with the heart of the bisexual [adolescent] girl."
    no "If Rin doesn’t want {i}you{/i} which, to be fair, I think she may-"
    no "Promise her something she {i}does{/i} want."
    o "But...what she wants is-"

    scene friendzonefight35
    with dissolve

    o "Oh, hell no! That’s playing dirty! I can win without that!"

    if bonus == True:
        no "I can {i}guarantee{/i} you that simply offering up the chance to get naughty with both you {i}and{/i} Otoha is enough to end this contest right here and now. Scout’s honor."
    else:
        no "I can {i}guarantee{/i} you that simply offering up the chance of a group hug is enough to end this contest right here and now. Scout’s honor."

    o "Absolutely not! We don’t-"
    s "Say no more."

    scene black
    with dissolve

    o "Hey! Don’t make promises to her that you can’t keep!"

    if rinbetrayed == True:
        s "Been there, done that."
        s "I can’t imagine this time being any more catastrophic than the last."
        o "What does that even mean?!"
    else:
        s "Oh, I intend to keep this one. It just might take a long time to set into motion."
        o "Ew! No! Don't even joke about that!"

    "………"
    "……"
    "…"

    scene friendzonefight36
    with dissolve

    f "Well, Sensei...Rin and I talked it over and we’ll only be accepting certain conversation topics for the rest of the-"

    if bonus == True:
        s "Rin, Otoha says she wants to have a threesome with you and me."
    else:
        s "Rin, Otoha says it's time for a group hug."

    f "Oh, come on...Like we would fall for-"

    scene friendzonefight37
    with dissolve

    r "When and where?!"
    f "Rin...he’s not being serious. If she really said something like that, it would mean they already-"
    r "WHEN AND WHERE?!"
    s "Uhh...the dorms, as soon as we’re done here."
    r "Okay!"
    s "Okay?"
    r "Okay! Yes! This is the best possible scenario for me!"
    r "Well, the {i}best{/i} possible scenario would be if we swapped you for Kaori. "
    r "But I’m definitely attracted to you and probably wouldn’t mind as long as-"

    scene friendzonefight38
    with dissolve

    f "Rin! Come on!"
    r "What? You can come too if you want. I'm sure Sensei can figure something out."
    f "No! I mean you just lost us the game! You told Sensei he was attractive!"
    r "Game? What are you-"

    scene friendzonefight39
    with dissolve

    r "Ah!"
    r "You tricked me!"

    if bonus == True:
        r "My mind completely blanked the second I imagined Otoha naked!"
    else:
        r "My mind completely blanked the second I imagined wrapping my arms around Otoha!"

    o "I can hear you..."
    r "Thank God she can’t hear me from all the way over here!"
    f "Ugh...this was Nodoka’s idea, wasn’t it?"
    f "I should have seen this coming..."
    r "So...um..."
    r "It’s probably a silly question, but..."
    s "The answer is no. It's not actually happening. And I’m just as upset as you are."

    scene friendzonefight40
    with dissolve

    r "Ugh..."
    r "Maybe someday..."
    s "Maybe someday indeed..."

    scene black
    with dissolve2

    "I head over to Makoto to relay the results of the round to her, but she seems a bit distracted by some notebook in her hands."
    "As I'm trying to make out what it is, Makoto informs me that she's just getting into the zone because her contest with Nodoka is coming up next."
    "Nodoka, on the other hand, doesn’t seem the slightest bit fazed."
    "So either she’s entirely too confident or...just doesn’t care at all."
    "Actually, knowing Nodoka, it’s probably both."
    "Regardless, the massive group reforms apart from a few stragglers as we all begin to make our way over to the[school] library..."

    stop music fadeout 5.0
    $ renpy.end_replay()
    $ dorm2warpoints += 1
    $ dormwar5 = True

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

label dormwar6:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```