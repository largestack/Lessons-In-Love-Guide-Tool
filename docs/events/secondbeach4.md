# TPK
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach4&go=Go)


Part of event chain [De-Briefing the Teacher](./secondbeach3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach4
* Group: Main
* Triggered by label: endofsecondbeach3

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach4:
    play sound "slidedoor.mp3"
    scene ocean
    with dissolve
    play music "samhain.mp3"

    "We make our way out of the inn and it quickly becomes evident that Otoha regrets not dressing appropriately for the occasion."
    "I think about letting her borrow my blazer, but then decide even offering it is pointless because, if it {i}really{/i} gets too cold for her, she can always zip her hoodie up."
    "Though, I really hope she doesn’t."
    "We walk in silence along the shoreline, trying to find somewhere to talk without anyone else seeing us, and I can’t help but find myself staring at her out of the corner of my eye."

    if bonus == True:
        "And either she’s okay with it or just doesn’t notice because, even though I’m barely being discreet about it, she doesn’t say anything."
    else:
        "I really hope I can look as cool as her one day."

    "I think more about what could have possibly prompted her to invite me out, knowing that she’s perhaps less interested in me than even someone like Yumi-"
    "And then I land on one thing and one thing only."
    "Rin."
    "How boring."
    "Which isn’t to say that Rin herself is boring. I like her a lot."
    "It’s just the idea of someone inviting me out to talk about romantic companionship (Or lack thereof) that doesn’t even involve me seems rather pointless in the long run."
    "But hey, people like to talk."
    "Otoha, if nothing else, is certainly a person."
    "A person who is likely going to try and figure out a way out of something bound to happen whether anyone wants it to or not-"
    "But a person nonetheless."

    if bonus == True:
        "And I have zero chance of sleeping with her in the future if I dismiss her over something as trivial as this."
        "If there is anything that walking alongside her on this beach has reinforced in my head, it is the desire to do just that."
        "But hey, maybe I’ll get really lucky and find out in this impromptu meeting that Otoha is just really horny and wants me to fuck her before anyone realizes we’re gone."
        "That would be the best case scenario."
        "Unfortunately, I don’t think I’ve encountered something that convenient since I first arrived in Kumon-mi."
        "Oh well."
        "I’ll just listen and hope that there’s something I can contribute to this conversation."
        "And store the sight of another sheltered girl’s fair skin in my mind to help me cum whenever I’m feeling lost or alone."

    o "This should be fine, right?"
    s "…"
    s "Yeah."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene otohabananaboat1
    with dissolve2

    s "Interesting choice of location."
    o "Why? Because it’s a boat shaped like a banana?"
    s "That’ll do it."
    o "It’s whatever."
    o "Not really sure what a random banana boat thing is doing in the middle of a circle of palm trees on the beach, but I was getting tired of walking, so..."
    s "Maybe it’s a cult ritual site of some sorts."
    s "Like one of you girls secretly worships a banana-shaped god and set up this boat as a means of contacting him."
    o "Maybe."
    o "Or maybe somebody just left it here."
    s "My idea was significantly more exciting."

    scene otohabananaboat2
    with dissolve

    o "More exciting, sure. A hell of a lot less plausible, though."
    s "Otoha...you didn’t call me out here to talk about bananas, did you? "

    scene otohabananaboat3
    with dissolve

    o "Of course not. I don’t even like bananas."
    s "Rin is going to be very happy when she hears that."

    scene otohabananaboat4
    with dissolve

    o "Dude."
    s "What?"
    s "You should be happy I made that joke. I saved you a segue. "

    scene otohabananaboat5
    with dissolve

    o "Hah...yeah. Yeah, you did."
    o "Figured you would have known that’s what this was about."
    s "What about her, though?"
    s "You two have a complicated relationship, so I figure it could be almost anything."

    scene otohabananaboat6
    with dissolve

    o "You think {i}we{/i} have a complicated relationship? Because, at least from my perspective, the one you guys have seems a lot more complicated than just two girls who hang out and talk about music."
    s "I think Rin sees a little more in you than just a musician friend, Otoha."

    scene otohabananaboat7
    with dissolve

    o "I obviously know that. But that’s all we are right now and that’s all we’ll be for a while."
    o "That’s not exactly what I’m thinking about right now, though."
    s "…"
    o "…"
    s "Are you going to tell me what you’re thinking? Or are we just going to hang out on a giant banana?"

    scene otohabananaboat8
    with fade

    o "Stop mentioning the banana."
    s "It is a hard aspect of this conversation to ignore."
    o "Then don’t mind if I ignore it and try to move things along because I am getting very cold."
    o "Have you like...talked to Rin at all today?"
    s "Today? No."
    o "Was she like...acting weird the last time you talked to her or anything?"
    s "Weird in what way?"

    scene otohabananaboat9
    with dissolve

    o "I don’t know."
    o "But she’s been acting a little different ever since she pulled you out of class the other day."
    o "Did you like...say anything to her or something?"
    s "At the risk of revealing too much information, do you mind if I ask {i}you{/i} why you think she’s acting weird? "
    o "…"
    s "…"

    scene otohabananaboat10
    with dissolve

    o "So, uhh..."
    o "She confessed to Chika or whatever during your last beach trip, right?"
    s "That was certainly a thing that happened."

    if rinbetrayed == True:
        o "But you and Chika were already, like...{i}together{/i} by then, right?"

        if bonus == True:
            o "Even though she asked you way in advance to give her a chance to...tell her how she felt."
            o "Or...feels?"
            o "I don’t know."
        else:
            s "If by {i}together{/i} you mean hugging, then yes."

        s "Do you think Rin still has feelings for Chika?"
        o "She liked her for years, dude. Am I insane for thinking that all of that would just vanish after spending a couple months hanging out with me?"
        o "She obviously likes me too, but with how weird she’s been acting lately, I can’t help but feel like she might be...having flashbacks or something to last time."

        scene otohabananaboat11
        with dissolve

        o "She’s not really easy to talk to when anything involving romance comes up."
        o "And I'm sure it's no surprise, but neither am I. I suck at it."
        o "But, not gonna lie, I think that a lot of her problem is a result of how you fucked her over back then."
        o "If someone I was close to betrayed me like that...I don’t even know what I’d do."
        s "I mean...it’s not like I did it for the sole purpose of hurting her."
        s "And since you apparently already know about my “involvement” with Chika, I shouldn’t have to explain {i}why{/i} I was with her."
        o "I’m not asking you to explain that. I’d prefer to stay as far out of your personal life as I can."
        o "All I want is to figure out what’s going on so I can...adjust accordingly."

    else:
        o "I...obviously already know that things with that didn’t really end well, but...is it weird for me to think there might still be something there?"
        o "Do you think that might be why she’s been acting weird lately?"
        o "Cause she’s having like...PTSD beach flashbacks or something?"
        s "Do you think that Rin still has feelings for Chika?"
        o "She liked her for years, dude. "
        o "I’m no expert on romance, but I don’t think that feelings like that just go away the second someone new shows up."
        o "Like...you two had a thing for a little while too, didn’t you?"
        s "I don’t know if I’d call it a “thing” when all we did was kiss."
        o "Normally, probably not."

        if bonus == True:
            o "But I think the fact that you’re twice her age kind of {i}makes{/i} it a thing. "
        else:
            o "But I think the fact that you’re the huggy boy kind of {i}makes{/i} it a thing. "

        o "If you had a normal friendship or student-teacher relationship or whatever, things like that wouldn’t happen."
        o "I guess what I’m getting at is that there are so many different reasons for her to be acting the way she is and I just...don’t understand any of them."
        o "And all I want is to figure out what’s going on so I can...adjust accordingly."

    s "Well, let me ask you this-"
    s "What if the reason Rin’s acting weird is because of you?"

    scene otohabananaboat12
    with dissolve

    o "I haven’t even done anything differently, though."
    o "In fact, I was kinda stoked to spend the weekend hanging out with her."
    o "Rin’s a really awesome and fun girl as long as you figure out how to tune out the...insane amount of hormones."
    s "I think the hormones are another thing about her that just makes her as...entertaining as she is."
    s "I have no idea how she still feels about Chika...and I’m probably even more confused about how she feels about me-"
    s "But I think the best thing you can do is ignore all of that and just think about how she feels about {i}you.{/i}"

    scene otohabananaboat13
    with dissolve

    o "It’s not that easy, dude."
    o "I’ve seen her scars. "
    o "I understand how much she must have been hurting to do something like that to herself."
    o "Being the current target for all of her affection...just makes it so that one wrong move on my part could get her to start doin' that shit again."
    o "It's so much pressure."
    o "Like...even if Rin feels a lot stronger about me than I do about her, I still care about her."
    o "She deserves happiness just as much as anybody else. "
    o "And it really fucks me up to see her upset."
    o "So, yeah...I kinda just...don’t really know what to do about it."
    o "She’s even like...avoiding me now. And that’s never happened before."
    o "Feels a lot like a...calm before the storm type of thing."
    s "And what do you think that storm will be, exactly?"
    o "…"
    s "…"
    o "I don’t know."
    o "I just hope it isn’t something that gets in the way of our friendship."

    "Ahh...there it is."
    "The semi-broodish resistance of a [teenage]girl pushing back a wave of feelings moving far too quickly for her to handle."
    "This type of thing is not uncommon in girls Otoha’s age- especially ones without any experience or even apparent interest in love or sex."
    "She just wants to enjoy her youth- and that is fine."
    "Unfortunately, it looks like someone may, once again, have to suffer as a result of that."
    "Maybe it would be best to let Rin know?"
    "Or, maybe-"
    "I should let her fail again."
    "Will that failure lead to her giving up on girls entirely?"
    "Will it land her one step closer to my door?"
    "Will she cry as she lays on my bed in defeat once again?"
    "Or will she accept her place in both my life and hers and just learn to let things go?"

    scene otohabananaboat14
    with dissolve

    o "Anyway, I guess I’ll leave you to your giant banana now."

    if bonus == True:
        o "I’m going to go put actual clothes back on and find out whether or not Nodoka lost her virginity to one of the girls who were arrested during our raid earlier."
        s "It’s honestly a miracle she still has it to begin with."
        o "I think that every single day."
        o "Thanks, though."
        o "And, if you see Rin, can you ask her to at least text me back?"
        s "Sure thing. "
        s "Have fun checking the virginity status of your roommate."
    else:
        s "Please don't. It has been speaking to me this entire time."
        s "The things it says...I can't even repeat them out loud. They horrify me."

    o "Have fun with the banana."

    if bonus == False:
        s "Otoha no"

    scene otohabananaboat15
    with fade

    "Otoha leaves and I wind up “having fun with the banana” for a minute or two."

    if bonus == True:
        "Please don’t interpret that the wrong way."
    else:
        "Except it's not fun at all. It's really scary and I'm probably going to have bad dreams now."

    "I’m really just sitting here thinking about, as Otoha put it, the calm before the storm."
    "I know we only have one other experience to work off of, but it feels like a beach trip without some form of tragedy would be no beach trip at all."

    scene otohabananaboat16
    with dissolve

    mo "…"
    s "Molly?"

    "Right on cue."

    mo "G...Greetings, Supreme Overlord."
    s "How long have you been there for?"
    mo "I was...in the middle of leveling up my stealth when...I saw you and Otoha walking, so..."
    s "So you followed us?"
    mo "...Yeah."
    s "How much did you hear?"
    mo "Not much, Sir. I had to stand rather far away to conceal my presence. "
    mo "I had every intention of leaving you behind and returning to the inn to complete my quest, but..."
    mo "I...I think I’m leveled up high enough to skip out on the XP for a little while longer."
    s "Does this mean it’s {i}our{/i} turn to talk now?"
    mo "May I sit?"
    s "As long as you’re okay with the seat being a giant banana."

    scene otohabananaboat17
    with fade

    "Molly takes a seat on the banana boat and peers up at the sun through the leaves of the palm trees."
    "As if the idea of the calm before the storm was not enough the first time it was brought up, she had to show up now of all times and remind me of just how much is at stake this weekend."

    if bonus == True:
        "Perhaps {i}everyone{/i} will be damaged beyond repair and I’ll be around to pick up the pieces?"
        "…"
        "Why does the thought of that not excite me even half as much as it should?"

    s "Molly-"
    mo "I’m already prepared for it, Sir."
    s "Prepared for what?"
    mo "TPK."
    mo "A total party kill, rather."
    mo "The only issue is that this druid is currently in between groups and running a party of one."
    mo "It’s a lonely campaign."
    mo "But...I’ll be able to start again on a new character soon enough."
    s "…"

    scene otohabananaboat18
    with dissolve2

    mo "I know it’s coming."
    mo "And I know things do not look good for the main heroine."
    mo "But...that’s just the thing with main heroines, Sir. "
    mo "Sometimes, our happiness is pushed back to the very end."
    mo "Perhaps that’s what’s happening this time. "
    mo "Or..."
    mo "Or perhaps I’m no main heroine at all?"

    scene otohabananaboat19
    with dissolve

    mo "Either way...I’m prepared."
    mo "I {i}have{/i} to be prepared."
    mo "If Rin thinks Otoha is the one who can make her happy...I’ll just have to make someone else happy."
    mo "I’ll..."

    scene otohabananaboat20
    with dissolve

    mo "I’ll..."
    s "…"
    mo "Damn it..."
    s "Would it make you feel better if we hugged on a banana boat?"

    scene otohabananaboat21
    with dissolve

    mo "Hahah..."
    mo "Maybe for a moment..."
    mo "I do...have to be getting back to the Kendo Princess, though. "
    mo "She’s embarking on a quest of her own right now that...may or may not have its own set of difficulties."
    s "A quest of her own?"

    scene black
    with dissolve2
    stop music fadeout 5.0

    $ renpy.end_replay()
    $ secondbeach4 = True

    "{i}Meanwhile...further down the shore...{/i}"
    "………"
    "……"
    "…"

    jump secondbeach5

label secondbeach5:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
scene secondbeachthree39
    with dissolve

    o "Well...you know. Beach."
    o "I kind of didn’t think I’d be wearing this at all with how cold it is, but I am apparently now a member of the yuri police and...this is the uniform or something."
    no "Looks like I’m going to need to search the room."

    if bonus == True:
        no "And also privately pat each one of you down."
        no "Except for Noriko. She’s too eager and it turns me off."
        n "And here I was ready to invite you to the futon snugglefest."

    no "Otoha. Hold down the living room. "
    no "I’m starting the search with their leader."
    o "Uh-huh. Right."

    scene black
    with dissolve

    mak "Nodoka! How many times do I have to tell you that I am not interested in women?!"

    if bonus == True:
        no "Apparently more because I do not believe you!"
    else:
        no "Being the chief of the yuri police doesn't mean that I am either!"
        no "Now, prepare yourselves for justice!"

    "Nodoka storms over to Makoto and does...Nodoka stuff."
    "But I use this opportunity to make my way over to Otoha and attempt to counteract the strangeness that has filled the room by talking to the most [[probably] normal person I know."

    scene secondbeachthree40
    with dissolve

    s "So..."
    o "…"
    s "I’ve always liked women in uniform."
    o "…"
    s "…"
    o "I’m gonna go ahead and forget you just said that, if that’s cool."
    s "I’m sorry. It was worth a shot."

    scene secondbeachthree41
    with dissolve

    o "I get it. I {i}did{/i} say it was my uniform, so I kinda set myself up for that one."
    s "I’m glad that we have reached an understanding so quickly."

    if bonus == True:
        o "Don’t really have a lot of time since I’m gonna get called on to pat somebody down any minute now."
        s "Doubtful. I imagine Nodoka would like to personally conduct her own strip searches of everyone in the room."
    else:
        s "Sometimes, I say things to try and make myself sound cool. But then I realize I'm not cool at all and just feel all embarrassed and stuff."
        s "Does that ever happen to you, Otoha?"

    scene secondbeachthree42
    with dissolve

    o "Yeah, probably."

    if bonus == True:
        o "That seems like..."
        o "...a thing she’d..."
    else:
        o "I'm kind of...naturally cool, though...so..."

    o "..."
    s "...?"

    scene secondbeachthree40
    with dissolve
    stop music fadeout 20.0

    o "Fuck it. Can you talk?"
    s "I’m talking right now."
    o "Privately. Before my...co-worker notices I’m gone."
    s "This is unusual."
    o "It won’t take long. Or at least I {i}hope{/i} it won’t take long. "
    o "Just...not really sure who else to talk to about this, so you’re gonna have to deal with it for a little while."
    o "Or you could just completely ignore me, forget I ever asked this, and I can figure shit out myself."
    s "No, I’ll come. Just...lead the way, I guess."
    o "I have literally never been here before and have no idea where I am going."
    s "Then just walk in a general direction and I’ll...walk behind you?"
    o "Or...next to me. Like a normal person."
    s "I guess that would be the normal thing to do, yeah."
    o "Yup."
    s "…"
    o "…"
    o "Okay. Gonna do that now."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ secondbeach3 = True
    jump secondbeach4
...
```