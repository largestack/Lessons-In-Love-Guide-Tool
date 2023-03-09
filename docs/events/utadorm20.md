# Blood Everywhere
Uta event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utadorm20&go=Go)


Part of event chain [Veins and the Circulatory System](./utamaid20.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Main: Food Groups](./day351.md)
* [Main: Good Morning](./secondbeach1.md)

## Event properties
* ID: utadorm20
* Group: Uta
* Triggered by label: utamaid20

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label utadorm20:
    play sound "dooropen.mp3"

    u "We’re hooooooome!"

    scene utacomeshome1
    with dissolve

    i "Oh, hey. It’s the only two people in Kumon-mi that I like, inconspicuously showing up at the dorm together just before midnight."
    s "Hey, Io. I’m surprised to see you still awake."

    scene utacomeshome2
    with dissolve

    "Uta tosses her hat and scarf onto an already large pile of clothes on the floor before taking her place next to Io. "

    u "Sensei and I did karaoke together!"
    u "Well, I did karaoke. "
    u "Sensei just stood there all night and watched me because he’s a creep."

    "She conveniently leaves out the part where we almost kissed."

    i "Did you have fun?"
    u "Lots."
    i "You should have invited me. I would have definitely come if it was just you two."
    s "Do you sing as well, Io?"

    scene utacomeshome3
    with dissolve

    i "Nope! I’m horrible. But I could have joined you in being creepy and just staring at Uta as she dances around in circles all night."
    s "What a surprise that you and I are on the same page once again."
    u "Yeah, yeah. Get a room."

    scene utacomeshome4
    with dissolve

    i "Maybe some other time. I actually have to run over to my aunt’s really quick because I just realized I left my phone over there."
    i "Can I trust you to take care of our teacher for the next thirty minutes or so without me?"
    u "I don’t know, Io. He’s always lookin’ at me with this weird fire in his eyes like he’s preparing to devour me whole."
    u "I’d feel a lot safer with your supervision."

    scene utacomeshome5
    with dissolve

    i "Sensei, will you be a good boy and promise to not devour Uta while I’m at my aunt’s house?"
    s "No. She is doomed."

    scene utacomeshome6
    with dissolve

    i "Welp, I’ve done all I can."
    u "Thank you for trying. If you are unable to find my body when you come home, please tell my parents I love them and my brother that he is an idiot."
    i "Will do."

    scene utacomeshome7
    with dissolve

    i "Um...if you’re gone by the time I get back...is it okay if I text you to say goodnight and stuff?"
    s "Sure. It’s already extremely late, so I imagine I'll be gone by then anyway."

    if bonus == True:
        s "I’m pretty sure Uta only invited me here to seduce me. And I doubt that will take long since I’m always staring at her with fire in my eyes or whatever it was she said."

    i "Okay! Yeah! I’ll...get going then!"
    i "See ya!"

    play sound "dooropen.mp3"
    scene utacomeshome8
    with dissolve

    "Io quickly puts her shoes on and darts out of the room, immediately thrusting Uta and I into yet another situation where we’re alone..."
    "Which, I’m pretty sure, is what she was inviting me here to get away from."

    if bonus == True:
        u "She didn’t even react to you saying I was gonna seduce you..."
        s "She either trusts you wholeheartedly or is completely open to the idea of you and I hooking up on your side of the room."

        scene utacomeshome9
        with dissolve

        u "Sorry, Sensei. You know the rule about my parents, and there’s no way I’d be able to call them this late without waking them up and getting them all grumpy."
        s "Then it appears we will have to continue awkwardly flirting with one another and pretending we never-"
        u "Yeah, yeah. A thing happened and now you think you’re a step closer to gettin’ your hands on the goods."

        scene utacomeshome10
        with dissolve

        u "Only problem is that the goods are out of stock and you’ve gotta wait for the store to replenish ‘em."
        s "Would you mind telling me when the next shipment is so I can mark my calendar?"
        u "Sorry, no. We closed for good and aren’t accepting deliveries anymore."
        s "I’m beginning to think your objective tonight was to just make me want you even more than I already do."

        scene utacomeshome11
        with dissolve

        u "I don’t really have objectives. I kinda just do what I do and hope nothing explodes as a result."
        u "I don’t have a problem with you wanting me and stuff, though. "
        u "So if tonight somehow made you want me more for...{i}reasons{/i}...that’s totally okay."

        scene utacomeshome12
        with dissolve

        u "Not that I think you’d be able to help yourself to begin with. I can basically buy a house with all of the money you’ve given me."
        s "Stop taking advantage of my heart. It’s not fair."
    else:
        s "You know, I think it's really unfair that Bojack Horseman was cancelled before everything was completely resolved."

    scene utacomeshome13
    with dissolve

    u "{size=-15}...What do you know about “fair?”{/size}"
    s "Hm? What was that?"

    scene utacomeshome14
    with dissolve

    u "I said...what do you know about chairs!"
    s "...Chairs?"
    u "Yeah! Cause...we should sit...and...since there’s no good place...how about the kotatsu?!"
    s "Do you actually think that was a good cover?"

    scene utacomeshome15
    with dissolve

    u "Don’t know! But I’m not about to wait around and find out! My feet are killin’ me."
    u "So either sit down or get the heck out, mister."

    if bonus == True:
        s "Can we not sit on the bed instead?"
        u "After what happened earlier? Heck no we can’t. I ain’t trying to lose my virginity in the thirty minute window of Io going to get her phone."
        u "What if she calls one of us right before it goes in and I get surprised and jump and then it splits me in half and there’s blood everywhere?"
        u "Does that sound fun to you?"
        s "I mean...up until the “blood everywhere” part..."

        scene utacomeshome16
        with dissolve

        u "Just sit down, you friggin’ horndog..."
    else:
        s "I understand. The last thing I would ever want is for you to feel physical pain. I will now sit down."

    scene black
    with dissolve

    "I take my shoes off and sit in the same spot where Io passed out on my lap the other day."
    "Uta does the same after grabbing a carton of strawberry milk out of Io’s mini fridge and, within a matter of seconds, things start going back to normal."

    scene utacomeshome17
    with dissolve

    "I guess “normal” is a pretty subjective term when it comes to my relationship with Uta, though, as I’m learning now that it hasn’t even really begun yet."
    "There’s clearly a lot that I don’t yet understand about her, and I feel like it wouldn’t be too much of a stretch to imagine that there’s a lot she doesn’t understand about herself yet either."
    "Granted, I could be completely wrong considering when I confronted her about her selflessness, she immediately refuted it."
    "Either way, the uncomfortable air blends in with the typical wood stain scented air of her dorm room and things, once again, move into an area of conversation we’re both more comfortable with."

    u "Io’s great, isn’t she?"

    "That area being talking about others instead of talking about ourselves."

    s "She said the same thing about you the other day."

    scene utacomeshome18
    with dissolve

    u "Oooooh...what else did she say? Anything juicy?"
    u "I’ve always been curious about what she says about me while I’m not around."
    u "Only issue is that she never talks to anybody, so this is the first chance I’ve had to find out."
    s "She said a few things. But the one that stuck out most to me is that you “got better.”"
    s "Whatever that means."

    scene utacomeshome19
    with dissolve

    u "...Oh."
    s "Should we deflect this conversation topic as well?"
    u "Yeah. My brain’s already overloaded from almost locking lips with you earlier and I’d rather not get into what that means right now."

    scene utacomeshome20
    with dissolve

    u "We can keep talking about Io, though! Just nothing bad, because she’s my BFF and I don’t wanna say mean stuff about her behind her back."
    s "Fine. But I’m going to let you lead the conversation since you’re the one who’s done nothing but show opposition to pretty much everything since we stepped into the karaoke booth."

    scene utacomeshome21
    with dissolve

    u "Done deal! Trust in Uta and you shall receive the best darn conversation you’ve had all night!"
    s "The competition is very weak, all things considered."
    u "Shush."
    u "So..."
    u "She hasn’t told me about it, but...based on the way she acted around you tonight, I bet that..."
    u "She told you she likes you."
    s "Perceptive."

    scene utacomeshome22
    with dissolve

    u "Did she give you the robot or did she chicken out? I think that one could have gone either way."
    s "The robot is now living on a table in my bedroom."
    u "Awwwwww, that’s so cute."
    u "She likes you a lot, you know. Which means you’re the first crush she’s ever had."
    u "Which means she’ll take it a bajillion times harder if you do anything to make her sad."
    s "Like kissing her best friend?"

    scene utacomeshome23
    with dissolve

    u "Guh. Well, at least we lasted a solid two minutes without bringin’ it up. But yes, like kissing her best friend."
    s "To move away from Io territory for a second...what about you, Uta?"

    scene utacomeshome24
    with dissolve

    u "Hm? What {i}about{/i} me?"
    s "Who was your first crush?"

    scene utacomeshome25
    with dissolve

    u "Hmm...good question. Who {i}was{/i} my first crush?..."
    u "…"
    s "…"
    u "…"
    s "…"
    u "Maybe Spongebob?"
    s "…"
    u "…"
    s "What?"

    scene utacomeshome24
    with dissolve

    u "You know. The cartoon sponge. Hangs out with a starfish."
    s "Your first crush was on a cartoon sponge?"
    u "Sure. He was cute."
    u "I never wanted to do him or anything cause I was just a little girl, but I used to talk about marryin’ him and stuff."
    s "You have come a very long way, Uta."

    scene utacomeshome26
    with dissolve

    u "I’ve had all kinds of crushes before."
    u "Cartoons. Boys. Girls."
    u "I even had a crush on Io for a little while."
    s "Excuse me?"
    u "Yup. You heard that right."
    s "Does...she know that?"

    scene utacomeshome27
    with dissolve

    u "No. And she’s never gonna find out because, if you tell her, you’ll never see another flavor beam for the rest of your life."
    s "Do you still feel that way?"
    u "Sensei, I mean it. Don’t even think about it."
    s "I’m not going to tell her. I’m just genuinely curious."

    scene utacomeshome28
    with dissolve

    u "No. I don’t feel that way anymore."
    u "It was only for a little while anyway. Like, barely even a couple weeks."
    u "I’ve just always had a hard time wrangling up my feelings and, before I know it, I wind up getting attached to stuff I don’t even have."
    u "It’s kinda pathetic, actually. And it’s made me do some really stupid stuff in the past."

    scene utacomeshome29
    with dissolve

    u "Buuuuuut that’s gettin’ a little too close to the “Uta doesn’t wanna talk about it right now” zone and I think it might be time for another topic change."
    s "What kind of stupid stuff?"

    scene utacomeshome24
    with dissolve

    if bonus == True:
        u "Sensei, I know you may be in love with me, but you really need to start payin’ attention to what I say and not just my boobs."
    else:
        u "Sensei, I know you may be in love with me, but you really need to start payin’ attention to what I say and not just my cute lil' face."

    s "I heard what you said, I’m just choosing to ignore it because I’m curious."
    u "Well that’s just plain rude and you’re a big ole jerk for doing that."
    s "Will you tell me eventually?"

    scene utacomeshome28
    with dissolve

    u "Yes. Whether I want to or not."
    u "It’ll slip out because, contrary to what Io may have said about me, I’m not “better.”"
    u "I just don’t say the same kinda stuff she says about herself because my brain is stupid and makes me think that anything that’s said out loud is real."
    s "So all of those smiles of yours are fake?"

    scene utacomeshome30
    with dissolve

    u "Course not. Just cause you’ve gone through some stuff in the past and can’t really get over it doesn’t mean that everything for the rest of forever is gonna be sad."
    u "I’m super happy now. And I’ve got a bajillion good things going for me."
    u "There’s just also some stuff I’ve gotta bury if I’m ever gonna move on."
    u "So maybe that does make me “better” if that’s the word Io is gonna use. But it’s not the one I would pick."
    u "Now, can we stop talkin’ about depressing stuff and go back to flirting? Even the whole near kiss thing was better than this."
    u "Also, you made me admit I had a crush on a sponge and now I’m mad at you."
    s "Can I tell Io about the sponge crush or is that off limits too?"
    u "Io knows about the sponge crush."
    s "And she still talks to you?"

    scene utacomeshome31
    with dissolve

    u "Are you gonna stop talking to me because I had a crush on a sponge?!"
    s "I can probably be convinced to keep associating with you."

    if bonus == True:
        u "Ah! I knew you’d break out the blackmail sooner or later! It was only a matter of time!"
        u "What do you want?! My first kiss? My first handie? My first child?"
        u "Tell me, Sensei! What must you take from me?!"
    else:
        u "What do you want?! Money?! A sandwich?!"

    s "Your phone number will suffice."

    scene utacomeshome24
    with dissolve

    u "Oh."
    u "That’s it?"

    if bonus == True:
        s "I’d also accept any of the three things you listed prior to my suggestion."
        u "No way. Not now that I know how easy it is to win you over."
        s "I forgot to add that I’ll also accept any sexy pictures you’d be willing to send me as a package deal with your phone number."
    else:
        s "I forgot to add that I’ll also accept any pictures of cats you'd be willing to send to me."

    scene utacomeshome32
    with dissolve

    u "That’s...not really something I can do..."
    s "That’s fine. I wasn’t trying to push-"
    u "No, like, I literally {i}can’t{/i} do that. There are parental locks on my phone and I can’t send picture messages."

    if bonus == True:
        s "…"
    else:
        s "Damn. A cat detection filter. How unfortunate."

    "I’m going to have to add somebody else onto my phone plan, aren’t I?"

    u "…"
    s "Just the number is fine, Uta."

    scene utacomeshome33
    with dissolve

    u "Done! Hand it over, Sensei."
    u "And get ready to be tossed into a group chat with me and Io so we all know what each other are doing every second of every day!"

    if bonus == True:
        s "I can guarantee that you do not want to know what I am doing for many seconds of many of those days."
    else:
        s "Okay, but please ignore all of the pictures of my accountant."

    u "..."
    s "..."
    u "How come you’ve always gotta ruin everything?"

    scene black
    with dissolve2

    "Uta gives me her phone number, which means I have now conquered the seventh dorm room."
    "And even though she is literally incapable of sending me picture messages, I’m glad to see that we’re at least {i}progressing{/i} in some way."
    "Or regressing, if her attitude toward what happened in the karaoke booth doesn’t change any time soon."
    "I’m not worried about that now, though."
    "I’ve learned a lot more about her today than any day before."
    "And even if there are parts of her that I won’t understand for months or years to come-"
    "I’m sure those months will be exciting."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm20 = True
    $ utanumber = True
    stop music fadeout 7.0

    "{i}Congratulations! You now have Uta’s phone number!{/i}"
    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm5:
...
```

## Code that triggers this event
File: \game\UtaEvents.rpy
Code:
```python
...
u "Bet you’re regretting missing that once in a lifetime opportunity, huh? We got really close to doing something really naughty. "
        s "I didn't realize it was up to me to make the first move there."
        s "Also, I don’t consider kissing “really naughty.”"
        u "That wasn’t just normal kiss territory. That was tonsil hockey territory. It was only gonna get crazier from there."
        s "I wish it did."
        u "Of course you wish it did. Uta-chan’s stolen your heart the way you’ve stolen a bunch of other people's."
        s "And I’m guessing those people are the ones you’re talking about when you say you “wanted to make the right move for everyone?”"
    else:
        u "I would have told everyone because I plan on sabotaging all of your hug-based relationships from this point on."
        s "Uta no."
        u "Sensei yes."
        s "With {i}everyone?{/i}"
        u "Everyone."
        s "Who does that entail?"

    scene utakaraoke27
    with dissolve

    u "Everyone means everyone."
    u "I’m glad you think I’m cute and that you wanna kiss me and stuff, but I’m really not as great as you think I am."
    s "What do you mean?"
    u "I mean that I’m really dumb and that I’d like to be forgiven for any dumb things I do around you."
    u "Like givin’ into that late night karaoke booth mood and gettin’ all up in your face."

    scene utakaraoke28
    with dissolve

    u "Or usin’ this opportunity to invite you back to my dorm room because it would be safer in there than it is in here."
    s "You are aware how that sounds, right?"
    s "Inviting someone back to your room after nearly making out with them can kind of only be interpreted one way."

    if bonus == False:
        s "It means you want to hug."

    u "{i}Sensei.{/i} I don’t care how much you want to make out with me or how you interpret my invitation. "
    u "It is now my duty as both your friend and your student to make up for invading your personal space and almost making you commit adultery. "

    if bonus == True:
        s "Are you sure you don’t want to just stay here and make out?"
    else:
        s "Are you sure you don't want to just stay here and do the hug thing without having to walk a bunch of miles?"

    scene utakaraoke27
    with dissolve

    u "Can you do me a favor and not bring that up anymore?"
    u "It really was just a spur of the moment thing. People do stuff like that all the time."
    u "It’s not like anything actually {i}happened{/i}. We just accidentally got our faces a little closer to each other than they’d ever been before."
    s "But what does that have to do with {i}everybody?{/i}"
    s "Because one of my least favorite qualities in people is selflessness. Think about yourself and what you want before worrying about how anyone else feels."
    u "No."
    s "No?"
    u "No. I don’t wanna."
    u "I’m happy the way I am."
    u "And that way involves lookin’ out for others."

    if bonus == True:
        u "So, sorry...but you’ll just have to keep wackin’ it to what the Uta in your imagination does and not worry about what the real Uta does."
        u "Cause the real Uta’s not gonna be ready for the stuff you wanna do with her for a long time. "
        u "Maybe not even ever."
        s "We’ll see about that."
    else:
        s "We should race go-karts sometime."

    scene utakaraoke29
    with dissolve

    u "Is that a challenge? "
    u "Are you still so excited about the dorm war that you need to start a {i}new{/i} contest just to keep the adrenaline up?"
    s "If that’s what you want to call it, sure."
    s "But I’m not going to let you forget that this happened and I am going to use it as a weapon against you whenever possible."
    u "Then I’ll just have to learn to deflect you even harder."
    u "Game on, Sensei. No one beats Uta."
    s "We’ll see about that..."

    scene black
    with dissolve2

    "Strangely enough, Uta doesn’t retract her dorm invite and, after checking out of the karaoke place, we begin to head over there."

    if bonus == True:
        "We’re both fully expecting Io to be around, though, so I’ve mostly given up on the prospect of pushing things any further with Uta for the time being."
        "It is really peculiar, though."
        "Maybe all of those deflections really aren’t deflections at all?"
        "Maybe Uta {i}does{/i} want something more with me but just...isn’t pursuing it for some reason."
        "It’s not because of Maya, is it? Or Io?"
        "…"
        "What did she mean by she’s not as great as I think she is?"
        "And why does that remind me of something Io said recently?..."

    $ renpy.end_replay()
    $ uta_love += 1
    $ utamaid20 = True

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    jump utadorm20
...
```