# Pool Party
Chinami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chinamidate15&go=Go)



## Event preconditions
✅Chinami love greater than or equal to 15

✅Event "[Main: Permission Slip](./day355.md)" is completed (event=day355)

✅chinaminumber equal to True (unknown variable)



## Next events
* [Chinami: Happy Hour](./chinamidate20.md)

## Event properties
* ID: chinamidate15
* Group: Chinami
* Triggered by label: callchinamimorning
* Triggered by branch label: callchinamimorning

## Event code
File: \game\ChinamiEvents.rpy
Code:
```python
...
label chinamidate15:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "………"
    "……"

    play sound "phonebeep.wav"

    c "Hihi! Chinami’s phone. This is Chinami’s secretary speaking."
    s "Chika?"
    s "Does this mean you’re not working at the mall anymore?"
    c "Heheh~ Of course I am. This is just an unpaid internship."
    c "So what’s up? Calling to check on my little sister?"
    s "Sure, let’s go with that."
    c "Well, you’re in luck! Cause we’re actually having ourselves a little pool party right now and Chinami would be suuuuuuper excited if you showed up!"
    s "How are you having a pool party without a pool?"
    c "We actually {i}do{/i} have a pool. It’s just one of those cheap, blow-up ones that we keep stashed away in the closet for most of the year."
    s "And...what better time to break it out than the middle of winter?"
    c "Right!"
    s "Chika, that was sarcasm."

    if bonus == True:
        c "Your face is sarcasm. Come get wet with my sister and me."
        s "Chika, please don’t add Chinami into sentences like that."
        c "Come stop me, then! "
    else:
        c "Be here in twenty minutes or I am going to burn the house down!"
        s "What? No. Chinami is in there."

    c "Bye bye, Sensei!"
    s "Chika-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "…"
    "Well, it looks like I am apparently starting today off with a...spontaneous pool party?"
    "I slide my phone into my pocket and begin to make my way over to the bus stop."
    "I feel as if just showing up to an event like this is going to require a fair amount of energy, so I should probably be conserving all I possibly can..."
    "………"
    "……"
    "…"

    scene chinamipoolparty1
    with dissolve
    play music "happyandplotting.mp3"

    c "Hey! Great timing. I just dried myself off."

    if bonus == True:
        s "How is that great? What happened to getting wet with you and your sister?"

        scene chinamipoolparty2
        with dissolve

        c "What happened to not wanting to drag the wizard into any of our silly euphemisms?"
        s "Touché. "
        s "You really didn’t have to go and do something like that, though."
        s "Don’t let me being here stop you from having fun."
    else:
        s "I am glad to see that the house remains unburnt."
        s "Is this pool party catered?"
        c "By {i}catered{/i} do you mean {i}awesome?{/i}"
        s "No. I want food."

    scene chinamipoolparty3
    with dissolve

    c "Ehh...I was starting to get kind of hungry anyway."
    c "Besides, Yumi is still in the pool with Chinami, so it’s not like she’s totally alone."
    s "Yumi...is in a kiddie pool?"
    c "Yumi is in a kiddie pool."

    scene black
    with dissolve

    s "Excuse me, Chika. I need to see this with my own eyes."

    if bonus == True:
        c "Heheh~ Don’t stare too hard when you’ve already got me, okay?"

    scene chinamipoolparty4
    with dissolve

    "I walk into the living room slash bedroom to find that Yumi is, indeed, in a kiddie pool."
    "And apparently having a pretty good time, too."

    ch "Thank you for all of the business tips, big sis Yumi! It makes Chinami very happy to learn about management from an experienced professional!"
    y "Hey, I ain’t {i}that{/i} experienced, twerp. Just know who you’re tryin’ to sell to and things’ll take care of themselves."
    ch "In that case, may I interest you in Chinami Corp's latest product? It’s just like a normal giraffe, but it has a jetpack and can shoot lasers out of its eyes."

    scene chinamipoolparty5
    with dissolve

    y "Heh. Will you take an IOU? I’m still kinda searchin’ for something a little more...predictable in the finance department."
    y "But I feel like I’ve been gettin’ pretty close lately and-"
    ch "Papa!"

    scene chinamipoolparty6
    with dissolve

    y "What? "
    y "What’d I tell you about payin’ attention to people when they’re talkin’ to you?"
    ch "Sorry, big sis Yumi! Chinami was just so excited to see her favorite man in the whole wide world!"

    scene chinamipoolparty7
    with dissolve

    y "The hell are you talkin’-"
    s "Hey. "
    s "Fancy meeting you here."

    scene chinamipoolparty8
    with dissolve

    y "Wha..."
    ch "Did big sis Chika tell you about the pool party, Papa? Or are you just here to pick up an order you placed on Chinamicorp.com?"
    y "This..."
    y "It’s...not what it looks like!"
    s "You’re not enjoying yourself and teaching Chinami about business inside of a kiddie pool in your best friend’s house?"

    scene chinamipoolparty9
    with dissolve

    y "I...I was makin’ sure the water wasn’t too hot for her! She’s got sensitive skin!"
    ch "Chinami’s skin isn’t very sensitive. Her mommy used to say it was strong and smooth just like {i}her{/i} mommy’s before she went to Heaven."
    y "Whatever! Now that I know it’s fine...my job here is done!"

    play sound "water1.mp3"
    scene chinamipoolparty10
    with dissolve

    ch "No! Come back! It’s not a family pool party unless we’re all here!"
    ch "Chinami finally found happiness!"
    c "Wait, Yumi. You’re not actually going out dressed like that, are you?"
    y "When the alternative is hangin’ around and being watched by that guy, heck yes I’m going out like this!"
    y "Just...tell me when he’s gone or something! I don’t know!"
    c "Yumi! Come on!"
    c "Sensei! Watch Chinami for a sec, please!"

    scene chinamipoolparty11
    with dissolve

    "I turn around to watch Chika quickly throw a hoodie on and chase Yumi out the door."
    "Then, within a matter of seconds, there are two pantless girls wandering around the old district of Kumon-mi."

    ch "Darn it. "
    s "It’s fine. We can have a pool party with just the two of us."
    ch "Yeah. But if either one of them catches a cold, they’ll have to quarantine themselves and Chinami will spend a few days alone."
    s "Oh."
    s "Well, worse comes to worst, you can come stay at my house for a few days."

    scene chinamipoolparty12
    with dissolve

    ch "Do you have a puppy?!"
    s "No. But I have a [niece] who kind of acts like one sometimes."
    ch "Is she fluffy?"
    s "Not really. No."

    scene chinamipoolparty13
    with dissolve

    ch "Chinami really wishes you had a puppy. That would give her the incentive she needs to come visit and avoid catching a cold from her dumbo sisters."
    s "Well that’s just too bad then because I don’t want a puppy. "

    scene chinamipoolparty14
    with dissolve

    ch "Hmph. I guess big sis Yumi was right after all and you really {i}don’t{/i} have a heart."
    s "Sure I do. It’s just not bogged down with the thoughts of love and puppies. It’s doing its job and delivering blood throughout the rest of my body."

    scene chinamipoolparty15
    with dissolve

    ch "Boooooring. Chinami wants to talk about dogs."
    s "This is the worst pool party I’ve ever been to."
    ch "Because Chinami is poor and can’t afford a real pool? "
    ch "Just wait until she’s a famous CEO princess with a hundred dogs that all hate you."

    scene black
    with dissolve
    play sound "water1.mp3"
    stop music fadeout 10.0

    "Despite wanting a hundred dogs to hate me or whatever ill will Chinami is suddenly wishing upon me, she scoots her way over to the edge of the pool and looks up at me."
    "I can already tell she’s switching modes once again- the same way I’ve seen her do a few times in the past."
    "I don’t want to say that she’s putting on an act or something- in fact, I’m almost positive she’s not."
    "But for someone like her, someone who’s able to understand and acknowledge exactly how she’s different from everyone else-"
    "There is always another mode."

    scene chinamipoolparty16
    with dissolve
    play music "starvingtodeathoutofreachofthesun.mp3"

    ch "Do you know why we’re having a pool party today?"
    s "No idea, actually."
    s "You should have all just gotten into the bath together if you were going to do something like this indoors."
    ch "Big sis Chika and big sis Yumi felt bad for Chinami because she can’t go to the beach with all of the other girls."
    ch "So they tried to bring the beach to her instead."
    ch "But Chinami wishes they could have brought their other friends here, too."
    ch "Chinami’s heard so much about them."
    s "Not from Yumi, I imagine. "
    s "She’s not exactly the most popular kid at[school]."
    ch "That’s because big sis Yumi is misunderstood."
    ch "But if Chinami were her age and got to go to[school] with everyone, she’d tell them that big sis Yumi isn’t scary at all."
    s "I’m sure your actual sister has tried that on multiple occasions. "
    s "Some people just aren’t really cut out for more than one or two interpersonal relationships, I guess."
    ch "Chinami doesn’t know what inner-personal means, but she’d like to try anyway."
    ch "Unfortunately, Chinami will probably never get to go to a real[school], so we’ll never find out."
    s "Giving up on your dreams of being a “normal girl” already?"

    scene chinamipoolparty17
    with dissolve

    ch "Chinami thinks that maybe some people just aren’t really cut out for being “normal girls” she guesses."
    ch "After Chinami’s new papa bought her a smartphone, she looked up all sorts of stuff about her condition."
    ch "She wasn’t very pleased with what she read."
    s "You should probably just be using your phone to murder pigs and leaving all of that sad stuff to medical professionals."
    s "The problem with the Internet and self diagnoses is that a person’s illness is never really as cut and dry as a list of symptoms on paper."
    s "In order to have whatever is wrong with you properly discovered, you need to gather the opinions of people who have spent their life training in the field and-"

    scene chinamipoolparty18
    with dissolve

    ch "Chinami is bored again. "
    ch "You’re not very good with girls, are you Papa?"
    s "Well...I don’t think I’m {i}bad{/i} with them."
    ch "Even though you have nothing you like to talk about and say all that boring stuff about doctors?"
    s "You know what? Why don’t we go back to talking about you?"
    ch "Is Papa afraid of doctor Chinami’s professional analysis? She has spent years training in the field."

    "I suppress the urge to hold Chinami’s head underwater and sigh to myself, knowing that she’s likely just trying to get a rise out of me at this point."
    "But even with the half-jokes about self diagnoses and her apparent side job as a medical professional, I really do feel for her."
    "I’ve never been good with empathy or sympathy or whatever {i}pathy{/i} the average person would exercise at a time like this-"
    "But I do wish things would have turned out a little bit different for her."
    "Not that things are “over” yet by any means."
    "But maybe some day this wizard will learn to use her powers to change herself and not just anyone she comes into contact with."
    "Perhaps she could even change me."

    s "Doubtful."
    ch "Doubtful?"
    s "Oh, sorry. Was just thinking out loud."
    ch "About what?"
    ch "Chinami wants to hear what you think about while you talk to her so she can be sure she didn’t make you feel bad."
    s "Chinami is in for a rude awakening then."
    s "You probably don’t realize this since you spend your entire life trapped inside of this house, but people very rarely say what they’re thinking in conversation."
    ch "Why?"
    s "Because we all have thoughts and parts of ourselves that we want to keep hidden."
    ch "Why?"
    s "Because people would realize how ugly we were if we actually expressed them."
    ch "Why?"
    s "Please don’t do this, Chinami."
    ch "Why?"

    if bonus == True:
        if ami_virgin == False:
            "I’ll be sure to cite things like this the next time Ayane or Ami tell me they want babies."
        else:
            "I’ll be sure to cite things like this the next time Ayane talks about having a baby."

    s "Are you just doing this to terrorize me?"

    scene chinamipoolparty19
    with dissolve

    ch "Yup."
    ch "Chinami realized she was annoying you, so she decided to distract you by annoying you in a different way."
    s "Chinami was not “annoying me.”"

    scene chinamipoolparty20
    with dissolve

    ch "Then how come your eyebrows looked like this?"
    s "I don’t know. Maybe I’m just not good at talking to you?"

    scene chinamipoolparty21
    with dissolve

    ch "That’s true. But we already figured that out when you wanted to talk about doctors and stuff."
    s "Well forgive me for wanting you to be a little more hopeful about your future."

    scene chinamipoolparty22
    with dissolve

    ch "Chinami..."
    ch "Chinami has no future."
    ch "Or at least not the kind of future her sisters and their future husband do."
    s "First off, you do have a future."
    s "Secondly, I can’t marry both of them. I’m pretty sure that sort of thing is illegal in Japan."

    scene chinamipoolparty23
    with dissolve

    ch "Does that mean you’ll marry {i}one{/i}?!"
    s "What? No."
    ch "Which one?!"
    ch "Big sis Chika would be a better wife but big sis Yumi’s body is more womanly."

    scene chinamipoolparty24
    with dissolve
    play sound "dooropen.mp3"

    ch "Ah! You’re not thinking of marrying Chinami, are you?!"
    c "Uhhhhh...excuse me?"

    scene chinamipoolparty25
    with dissolve

    ch "Yay! Big sis Chika is home!"
    s "Welcome back."
    s "I take it you weren’t able to track down Yumi?"
    c "Ugh, no. She’s annoyingly fast when she wants to be...and I didn’t want to run around barefoot."
    c "Would you mind explaining to me why you’re suddenly going to marry my little sister, though?"
    ch "Sorry for stealing your boyfriend, big sis! Chinami is just too darn cute."
    ch "She can't help it if things like this happen."
    s "Chika, it is not what it sounds like."
    s "I never agreed to any of this."
    s "She’s forcing it on me."
    c "She’s four feet tall. "
    s "But has the personality of a giant."
    ch "And the immune system of scrambled eggs!"
    c "Chinami! Stop that!"

    scene chinamipoolparty26
    with dissolve

    ch "Chinami is sorry. Please forgive her. "
    ch "And also make her lunch because she’s worked up an appetite from all of her swimming."

    scene black
    with dissolve2

    "Chika reluctantly agrees to her sister’s demands and winds up making lunch for all three of us."
    "We wind up eating together while the Chosokabes soak in their kiddie pool and I, being the anti-fun human being that I am, remain to the side of them."
    "Yumi never comes back and probably catches a cold or something. I don’t know."
    "Either way, it’s a little worrying to hear that Chinami now has access to a plethora of information that’ll likely exacerbate her already worrisome outlook on her condition."
    "But I think she’s counting herself out a little early, personally."
    "Is she weaker than everyone else? Sure."
    "I can’t recall {i}ever{/i} having to wear an animal mask in public while...that’s just a normal thing for her."
    "But she’s still alive."
    "She just needs to be a little careful."

    $ renpy.end_replay()
    $ chinamidate15 = True
    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label chinamidate20:
...
```

## Code that triggers this event
File: \game\ChinamiEvents.rpy
Code:
```python
...
label callchinamimorning:
    if chinami_love >= 0 and chinamidate1 == False:
        jump chinamidate1
    if chinami_love >= 10 and christmas7 == True and chinamidate10 == False:
        jump chinamidate10
    if chinami_love >= 15 and day355 == True and chinamidate15 == False:
        jump chinamidate15
...
```