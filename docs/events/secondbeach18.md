# All is Bright. All is Beautiful. (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Goodnight](./secondbeach17.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Rin: The Paragon of Not Worrying About Stuff](./cafe50.md)
* [Tsuneyo: Like Noodles in the Wind](./ramen25.md)
* [Tsuneyo: Unsleeping Aegis](./tsuneyodorm25.md)
* [Main: Girls in Spandex](./halloweentwo1.md)
* [Niki: Thousands, If Not Millions](./nikidate10.md)

## Event properties

* Id: secondbeach18
* Group: Main
* Triggered by label: goodnightp2
* Chain sources: secondbeach17
* Chain sources path: secondbeach17->secondbeach17

## Official wiki page

[All is Bright. All is Beautiful.](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach18&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach18:
    if _in_replay:
        play music "goodnight.mp3"

    $ totaldays += 1
    $ day = 1
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date

    scene endofsecondbeach1
    with dissolve3

    a "Guh. Bring back the sun. One day of summer weather isn’t enough. I want more."

    "Niki was gone when I woke up."
    "I imagine it was a side effect of regret or something along those lines."
    "I can’t imagine it’s very nice to wake up next to {i}me{/i} of all people- especially when I’ve hurt her as much as I have in the past."

    if bonus == True:
        "Nothing happened, in case you were wondering. "
        "I obviously {i}tried{/i} to make things happen, but she wasn’t having any of it."
        "I guess she just wanted the company."
        "She kept my t-shirt, though, which is a surprisingly ex-girlfriend thing to do."
        "But I’m sure I’ll be seeing her again as it was one of my extra thick ones and I need it in order to survive the winter."
    else:
        "She kept my t-shirt, though, which is a surprisingly ex-girlfriend thing to do."
        "But I’m sure I’ll be seeing her again as it was one of my extra thick ones and I need it in order to survive the winter."

    scene endofsecondbeach2
    with dissolve

    ay "You’re sure you have everything, Sensei? "
    s "I’m missing a shirt, but that much is out of my control. "
    s "I think I’m fine when it comes to everything else, though. I didn’t bring a lot."
    s "Would someone remind me again why we have to leave so early, though?"
    to "Because we have[school], of course."
    s "Would someone also remind me why Touka is here?"

    scene endofsecondbeach3
    with dissolve

    to "How rude. "
    to "But since you are so insistent on knowing-"
    s "I asked one time."
    to "{i}Since you are so insistent,{/i} it is because I am still waiting to be thanked for enabling this vacation."
    ay "You’re probably going to be waiting for a while, Touka. Sensei’s not very good at thanking people for the nice things they do for him."
    s "Lies. Thank you, Touka. I appreciate it."

    scene endofsecondbeach4
    with dissolve

    ay "Hey! I helped, too! Where’s my “Thanks, Ayane! I love you!?”"
    s "Somewhere else. I’ll give it to you later."
    to "Oh. Well...um...the pleasure has been all mine."

    scene endofsecondbeach5
    with dissolve

    ay "{i}And{/i} mine."
    ay "But yeah...mostly Touka’s, I guess. Even if we didn’t use half of the rooms we paid for."
    a "Now that you’re done praising the people that aren’t me, we should probably get going. You wouldn’t want to miss[school], would you?"
    s "Is that a real question? Of course I’d want to miss[school]. I hate[school]."
    s "I have to...do stuff there."
    a "Probably even more today than usual, too."
    s "Yeah. Mondays suck."

    scene endofsecondbeach6
    with dissolve

    ay "Wait...did you not hear?"
    s "Hear what? I’ve been awake for like twenty minutes and you four are the only girls I’ve seen."
    ay "Miss Watabe..."
    ay "Miss Watabe overdosed last night and had to be rushed to the hospital."
    s "What?"
    ay "Osako came bursting into our room asking for help in the middle of the night. I’m surprised you didn’t hear anything."
    s "Is she okay?"
    ay "Touka was able to arrange an ambulance right away and she’s stable {i}now{/i}...but she’s going to be taking off of[school] for a little while so she can recover."
    to "I’m sure you could have arranged for a transport just as quickly as me. I just happened to have a phone nearby."
    s "What was she on?"

    scene endofsecondbeach7
    with dissolve

    ay "Does that really matter? Because it’s not something I really think any of us should be asking."
    s "No, it doesn’t matter I guess. I’m just a little confused. "
    a "It could have been an accident..."
    a "I mean, it probably {i}was{/i} an accident."
    a "Miss Watabe is dark all the time, yeah. But...I don’t think she really means it when she says all that stuff about wanting to die."
    to "Perhaps we should make a “get well” card of some sort?"
    to "When I fell off my horse in elementary[school], my class got together and made a card like that for me."
    to "I thought it was very sweet."
    to "Until I found out that none of them wanted to sign it and that they only did it because the teachers asked them to and oh good now I’m feeling sad."

    scene endofsecondbeach8
    with dissolve

    ay "Whatever happened...I think we should just leave the two of them alone for a little while and let them work through it."
    ay "It’s not really our place to...get involved, I don’t think."
    a "But, umm..."
    a "On the bright side...Rin and Otoha are dating now?"
    s "Oh, right. I forgot Rin was going to confess last night."
    s "Otoha really said yes?"

    scene endofsecondbeach9
    with dissolve

    a "Yes, but...how did you know Rin was going to confess?"
    s "The same reason I know Touka sleeps on a vibrating love hotel bed. I’m popular."

    scene endofsecondbeach10
    with dissolve

    to "It...It is a normal, circular bed with rapid sleep technology! "
    a "Rapid what now?"
    to "And what does my bed have to do with those two forming a relationship with one another?!"
    s "Nothing, really. I just thought teasing you might cheer you up."
    to "It-"

    scene endofsecondbeach11
    with dissolve

    to "Wait...it actually kind of did."
    to "Huh."
    a "Either way! Looks like the harem is down two more girls and I am one step closer to...totally not marrying you because you’re my [uncle]! And that would be like, so weird, right?!"

    scene endofsecondbeach12
    with dissolve

    a "Unless..."
    s "…"
    ay "Aaaaaanyway, I’m cold. "

    if bonus == True:
        ay "And everybody else already went back to the dorms to shower and get ready for[school], so we might as well join them."
        s "In the shower? Good plan. Let’s head out, team."
    else:
        ay "And everybody else already went back to the dorms to get ready for[school], so we might as well join them."
        s "Good plan. Let’s head out, team."

    scene black
    with dissolve2

    if bonus == True:
        "As you may have guessed, I’m not able to shower with any of them."
        "But Touka is the only one who winds up heading back to the dorms anyway."
        "Ayane and Maya return to the house with Ami and me because that’s where they left all of their stuff."
        "And since they’re [teenage]girls and it isn’t weird for them to bathe together or whatever, they decide to just save time by {i}not{/i} adding an extra stop to the mix."
        "I’m sure they would have invited Touka as well if it weren’t for the fact that they’d have trouble fitting her breasts in the bath alongside them."
        "Sorry, Touka."

    "………"
    "……"
    "…"

    scene endofsecondbeach13
    with dissolve2

    ya "Touka?..."
    ya "Sensei?..."
    ya "Where did everyone go?..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene endofsecondbeach14
    with dissolve2

    "The same room as always. "
    "I wonder how many times it’s been now. And how many more mornings I’ll get to watch the light creep through the blinds."
    "I hope it really does last forever."
    "Because even if this world isn't something I understand...or something Maya understands..."
    "It’s my home now."
    "And sure, it can be pretty horrible at times with friends overdosing or having their hearts broken-"
    "Actually, correction. Rin didn’t have her heart broken this time. "
    "Good for her."
    "I can only imagine how Molly must be feeling, though."
    "I’ll have to check on her-"

    scene endofsecondbeach15
    with dissolve2

    "...soon."

    m "…"
    s "…"
    s "M-"
    m "Don’t speak."
    m "Just let me have this."
    m "Please."
    s "…"
    m "…"

    scene endofsecondbeach16
    with dissolve

    s "Okay."

    "Remember the other morning when I told you that I’d find myself losing battle after battle soon enough?"
    "Well-"
    "I managed to win one in the end."

    scene black
    with dissolve2

    "Maya leaves the room silently, without asking me to forget about this or...abstain from bringing it up to anyone else."
    "But I don’t think I will either way."
    "Just like I don’t think I’ll tell anyone about Niki showing up in my room last night to just...leave before sunrise without saying anything."
    "I have no reason to tell anyone at all about either of these things."
    "But it’s still only morning."
    "And even if everything is bright and beautiful now, it doesn’t mean it will be later."
    "The person I trust least of all is myself."
    "..."
    "I don’t deserve any of this."

    $ renpy.end_replay()
    $ secondbeach18 = True

    scene smileex
    with dissolve4
    $ renpy.pause(8, hard=True)
    stop music
    play sound "static.mp3"
    scene happy9 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene happy2 with flash
    scene happy9 with flash
    scene happy9 with flash
    scene happy2 with flash
    scene happy1 with flash
    scene happy2 with flash
    scene happy9 with flash
    stop sound

    jump afterschoolevent

label halloweentwo1:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
scene happy5 with flash
    scene happy6 with flash
    scene happy7 with flash
    scene goodnight35 with flash
    stop sound

    os "Babe? Sorry I’m back late, but the girls decided to just leave their bonfire thing burning."
    os "I’ll finish packing up all of your stuff out here, but if you could bring whatever we have in the bedroom out, it would be a big help."
    os "No idea why you always pack so much even when we know we’ll only be gone for a couple days...but this {i}is{/i} what I signed up for, I guess."
    os "…"
    os "…"
    os "…"

    scene goodnight36 with dissolve

    os "Wakana?"

    scene goodnight37
    with fade

    os "Is everything okay?"

    play sound "static.mp3"
    scene frown with flash
    scene smile with flash
    scene frown with flash
    stop sound

    "No."
    "It never is."
    "But we learn to accept this as life moves on because-"
    "Actually."
    "I don’t know."
    "Why {i}do{/i} we accept this?"

    play sound "static.mp3"
    scene goodnight38
    with flash
    stop sound

    "We all find ourselves back in bed each night, thanking God or a friend or a piece of media for being the drug we need to make it through the day."
    "But when there is so much happening behind the scenes, it’s easy to forget that there are people out there having a much harder time."
    "So we wait."
    "And we wait and we wait and we wait and we wait-"
    "For something to make us feel whole again."
    "Sometimes, you have to work for it."
    "But sometimes-"

    play sound "slidedoor.mp3"
    scene goodnight39 with dissolve

    "It comes to you instead."

    scene goodnight40
    with fade

    s "Niki?"
    ni "Can I stay here tonight?"
    s "I mean...sure."
    s "But don’t you-"
    ni "I just had a little more free time than I thought."
    ni "That’s all."
    s "…"

    scene black
    with dissolve2

    "Life is miserable."
    "But sometimes, it’s not."

    scene goodnight41
    with dissolve2

    ni "Are you okay?"
    s "Yeah."
    s "Just thinking."
    ni "About what?"
    s "I’m not really sure."
    ni "Fun."
    ni "Do you have a t-shirt I can borrow? I didn’t bring my bag."
    s "I mean, yeah...but..."
    s "This is a pretty dramatic departure from how we were this morning."
    s "And...every day before that."
    ni "Yeah."
    ni "..."
    ni "Yeah, I guess it is."

    scene black
    with dissolve2

    "Goodnight."

    $ renpy.end_replay()
    $ secondbeach17 = True

    "………"
    "……"
    "…"

    jump secondbeach18
...
```