# Veins and the Circulatory System (Uta)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Uta love greater than or equal to 20

* Event [Another Man's Treasure](./bathhouse20part2.md) (Io) is completed)

* Event [Facetime With My Mom](./utadorm15.md) (Uta) is completed)



## Next events

None

## Event properties

* Id: utamaid20
* Group: Uta
* Triggered by label: utamaid
* Triggered by branch label: utamaid
* Triggered by path: utamaid->utamaid20

## Official wiki page

[Veins and the Circulatory System](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utamaid20&go=Go) for more details.

## Event code

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid20:
    scene nightsky
    with dissolve2
    play music "justlights.mp3"

    "It’s cold."
    "But you’ve heard that before."
    "You’ve heard virtually everything before, haven’t you?"
    "One of the downsides of sharing your thoughts with people is that it’s very easy to lose track of who you’ve told what or how many times you’ve said {i}that.{/i}"
    "I think this to myself, for what may be the millionth time (Even I have lost count) and wonder who it is I’m referring to."
    "Who am I sharing these thoughts with?"
    "I look up at the stars and hope, for some reason, that it starts to snow."
    "Maybe it’s just because I’m looking for a change of scenery."
    "Or maybe it’s something a little more confusing in nature."
    "Like there’s something I associate the snow with that will subconsciously wipe away any and all of the lingering negativity coursing through my veins."
    "I think more about veins and the circulatory system. "
    "Of how our bodies are machines."

    if bonus == True:
        "Of how each and every part of us just naturally falls into place as the result of a man cumming inside of a woman."
        "And I realize that nothing in this world is really strange at all when entire existences and consciousnesses are being formed as the result of rough doggystyle sex in bathrooms."

    "I think more about veins and the circulatory system. "
    "Of how it’s all just a bunch of wires, not much different from what it would look like if you were to tear open one of your walls."
    "My mind races, but moves not even half as effectively as a horse who breaks its leg at the midpoint of a race and needs to be put down."
    "I think of splaying myself out on the concrete and letting someone put {i}me{/i} down while a group of children watch on in shock."
    "But I stop when I realize that I have so much left to live for. "
    "I stop when I realize I have not yet begun to live at all."

    s "…"
    s "…"
    s "…"
    u "Uhh..."
    u "You okay, Sensei?"

    scene utakaraoke1
    with dissolve2

    s "What?"
    u "You kinda just walked up to me and Osako and started lookin’ at the sky."
    u "Has Io been sneakin’ you some of her pills? Do we need to schedule an intervention?"
    s "I’m pretty sure I’m fine. What are you doing outside, though?"
    s "Aren’t you two supposed to be at work?"

    scene utakaraoke2
    with dissolve

    u "I already told you when you first showed up..."
    u "We close at 10:00 and it’s like 10:30 right now."
    s "When did it get so late? I feel like it was the afternoon just a few minutes ago."

    scene utakaraoke3
    with dissolve

    u "Ah! Dementia!"
    u "It’s grandpa Ushibori all over again!"
    u "Who am I, Sensei?! Tell me you remember me!"
    s "You are my girlfriend and personal maid."

    scene utakaraoke4
    with dissolve

    u "Phew...it looks like you're okay after all."
    os "Can you two take your flirting somewhere else? I’m starting to get a headache."
    u "Osako-chan is just sad that her girlfriend isn’t here to pick her up yet."
    s "Don’t worry, Osako. Uta and I will hang out with you and keep you safe until she gets here."
    os "You are...aware that I’m a fifth degree black belt, right? I could hold my own against basically everyone in this city."
    s "We will protect you. Don’t worry."

    scene utakaraoke5
    with dissolve

    os "You know, sometimes, I wish that rich girl {i}did{/i} buy the dojo."
    u "So, whatcha gonna do now that ya can’t be pampered by Uta-chan and stuff your face with cupcakes for the rest of the night?"
    s "Probably follow you around like some kind of stalker or something."

    scene utakaraoke6
    with dissolve

    u "Uhh...hahah..."

    if bonus == True:
        s "If you want the realistic answer, I’ll probably just go home and watch porn or something."
    else:
        s "If you want the realistic answer, I’ll probably just go home and cry myself to sleep."

    scene utakaraoke7
    with dissolve

    u "Here’s an idea! How about you come out with me instead?"

    if bonus == True:
        u "I obviously can’t do for you what those sexy porn ladies would do, but we can at least find our own non-sexual ways to have fun!"
        s "Non-sexual fun is an oxymoron."
    else:
        s "Why would I do that? Life is miserable and I just want to frown in isolation."

    u "Sounds to me like a certain somebody has never experienced karaoke before."
    s "Every experience I have with karaoke is bad."
    u "Well, looks like we’re gonna have to break the streak!"
    u "This is what I normally do after getting off work anyway. "
    s "You leave the maid cafe at 10:30 to go do karaoke by yourself?"
    u "I’m not always alone! Osako comes with me sometimes."
    s "Does she now?..."

    scene utakaraoke8
    with dissolve

    os "Don’t sound so surprised about it..."

    if bonus == True:
        u "Unfortunately, Osako-chan’s gotta get home and give her woman some of that sweet, sweet lovin’, so I was gonna go alone tonight."
        s "Have fun, Uta. I’m going to go back to Osako’s place and watch the whole loving thing."
    else:
        s "I am so surprised."

    if day333part2 == True and bonus == True:
        s "Which is more than she can say since she apparently likes being blindfolded and-"

    scene utakaraoke9
    with dissolve

    os "Excuse me?"

    if bonus == True:
        u "I guess I’ll tag along too. We can watch ‘em together as long as we stay on opposite sides of the room."
        s "Deal."
        os "Fuck off. We’re probably just going to watch a movie and fall asleep anyway."
        s "Don’t be like that. Wakana looks like she could use a good orgasm or two to be brought back to life."

        scene utakaraoke10
        with dissolve

        os "She’s plenty alive and plenty satisfied, thank you very much! "
        u "Sounds to me like Osako-chan could use a good rubdown herself, right Sensei?"
    else:
        s "You are weak and your arms are noodles."

    scene utakaraoke11
    with dissolve

    os "I...I’m going for a walk! "
    os "And if Wakana shows up, don’t you dare try hitching a ride back to our place or I’ll kick both of your asses!"
    s "Osako, really? Karate is supposed to be used for self-defense, not picking on people weaker than you."
    os "I’m...defending my honor. Now, goodbye."

    scene utakaraoke12
    with dissolve

    "Osako leaves and suddenly it’s just Uta and me."
    "She wastes no time in pressing the issue at hand, however, as we’re immediately discussing the probability of karaoke again."

    u "So, you gonna come with me? Or are you gonna let a defenseless lil’ girl like me wander around Kumon-mi all by herself?"
    s "You’ve already said that’s something you do all the time."
    u "Doesn’t mean I wouldn’t be happy to have a big strong man like yourself to protect my pint-size body from bein’ snatched up and thrown into a van."
    s "I’ll gladly accompany you. But know now that I’ll just be awkwardly staring at you as you sing for the entire night."
    u "You think I’m not used to you staring at me by now? Come on, Sensei. "
    u "You’ve barely taken your eyes off of me since I strolled into[school] that fateful winter day."
    u "You know, when you were hanging out with your girlfriend Maya at her locker."
    u "Actually, wanna invite her to karaoke with us?"

    if bonus == True:
        u "I’ll even sing some cute lil’ love songs to get you two in the mood!"
        s "If there is any song that will put Maya in “the mood,” I highly implore you teach it to me."
        u "That I can do, Sensei! But not if we’re out here."
        u "The karaoke place is on the way back to the dorm, so just stick with me and you’ll be learnin’ how to woo your lady in no time at all!"
    else:
        s "No. She's always mean to me and it makes me feel bad."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Uta begins to march away from the gate outside of the maid cafe and the two of us start heading over to the karaoke place."
    "I’m not sure if it will be the same one I’ve been to with Ami and the others before but, if it {i}is{/i}, I really hope Ayane isn’t there."
    "There’s only so much Despacito one person can take, and I have already greatly surpassed my lifetime allowance of it."
    "Uta and I remain close together, just an inch or two apart, as we wander down the streets."

    if bonus == True:
        "I think of veins and the circulatory system once again, but in an exponentially more suggestive way this time."
        "I can’t be blamed for this, though."
        "Karaoke this late at night with just one guy and one girl typically only means one thing."
        "And even though Uta may only be in this to sing and get some of the energy out of her system, I’m sure she knows how it’ll look too."
        "And yet we walk."

    "And, after ten minutes or so, we arrive at our destination..."
    "………"
    "……"
    "…"

    scene utakaraoke13
    with dissolve
    play music "utasings.mp3"

    if bonus == True:
        "I’m forcibly dragged into a private karaoke booth as soon as the two of us reach the place and, just as things start to look like they’re going to get exciting, Uta grabs a microphone and breaks out into song."
    else:
        "I’m forcibly dragged into a private karaoke booth as soon as the two of us reach the place. And just as I think we're about to hug, Uta grabs a microphone and breaks out into song."

    "I can already tell in just the several minutes we’ve been here that it’s something she’s done hundreds of times before."
    "Probably thousands if we’re taking the whole time loop thing into consideration and-"
    "Actually, that wouldn’t be right, would it?"
    "I know she worked at the maid cafe before transferring into [kumon_mi_high], but I highly doubt she was doing something like this before commuting all the way back across town."
    "Either way, I awkwardly stand around as she cycles through different pop songs and, of course, she also has somewhat of a dance routine for each one."
    "It’s a lot different than when Ami and the others come here but, even though her voice isn’t perfect, her energy and presence are mildly exhilarating. "
    "If I was into idols (Sorry, Niki) and other stuff like that, I’d probably find myself falling for her right about now."

    if bonus == True:
        "The only thing is, I’ve kind of already cemented Uta as an ideal woman in my eyes and I would not want to sleep with her any less even if she was absolutely horrible at singing and dancing."
        "Thankfully, she isn’t."
        "So...that’s just a plus I guess."

    scene utakaraoke14
    with fade

    "Every once in a while, she’ll make eye contact with me and try to get me excited, but..."
    "I am me. "

    if bonus == True:
        "And excitement is, unfortunately, not a trait I inherited from whoever it was that decided to have rough doggystyle sex and lay out the wires inside of my body."
        "I {i}am{/i} at least respectful enough to stand, though. "
        "Also, it gives me a better view of Uta because she tends to bounce a lot when she dances and...I’m sure you can guess what that means."
        "Sidenote: I really wish she wasn’t actually a prude and that she shared my same opinions on the idea of fun and its correlation to sexual contact."
        "But alas."
    else:
        "I am a sad boy."

    scene utakaraoke15
    with dissolve

    u "Sing with me, Sensei!"
    s "I don’t know this song."
    u "Who cares?! The words are right there on the screen!"
    s "I don’t sing."
    u "What if I let ya put your arm around me? That enough to get you to act happy?"
    s "Just have fun on your own and I’ll keep watching. "
    u "You’re not even looking, though!"
    s "If I look at you, I’ll have a harder time saying no."
    s "You’re annoyingly cute."

    scene utakaraoke16
    with dissolve

    u "Sing!"
    s "No."

    if bonus == True:
        "Uta grabs my chin and tilts my face toward her, making it incredibly hard to not grab her and not only ruin her song but break several of this establishment’s rules in the process."

    u "Sing!!"
    s "Why?"
    u "Because it’s fun!"
    u "You’ve gotta smile, Sensei!"
    s "I’m perfectly content with just watching."

    scene utakaraoke17
    with dissolve

    u "Sing, damn it!"
    s "Karaoke is bad."
    u "You will have fun with me and you will like it!"
    s "Stop it."

    scene utakaraoke18
    with dissolve

    u "AHHHHHH!"
    s "You’re messing up the song."
    u "You don’t care about the song! You don’t care about Uta-chan! You don’t care about anything!"
    s "Uta, I’m starting to lose balance."
    u "I’m starting to lose {i}patience!{/i} I’m on my fifth song and I haven’t even heard a peep outta you yet! "
    s "Uta-"

    scene utakaraoke19
    with dissolve

    u "How do you expect to ever marry me if you can’t even sing a little song?! It’s not that hard!"
    s "I am going to fall now."
    u "I’m 4’11! Are you really about to be taken down by a girl my size?!"
    s "Yup. Brace for impact."
    u "Sensei!"

    scene black
    with hpunch
    play sound "thump.mp3"

    "Now, I know what you’re thinking...and I’m sure it’s exactly how Uta put it."
    "And yes, I did get taken down by a girl 100lbs lighter and an entire foot shorter than me."
    "But A: My foot had gotten wrapped around a wire. And B: Why would I try and prevent this?"
    "Because now the two of us look like this."

    play sound "static.mp3"
    scene utakaraoke20 with flash
    stop sound
    play music "heartbeat.mp3"

    u "…"
    s "…"
    u "Um..."
    u "Hi..."
    s "Hey."
    s "Are you okay?"
    u "Me?"
    u "Yeah."
    u "I’m...fine."
    u "You kinda broke my fall."
    s "It appears that I did."
    u "Um..."
    u "Thanks for...protecting me?"
    s "No problem."
    s "I kind of warned you that this was about to happen, though."
    u "It wouldn’t have happened if you’d have just sung."
    s "All things considered, I’m kind of glad I didn’t."
    u "You’re...breakin’ a bunch of Uta-chan’s rules right now, Sensei."
    s "You’re the one on top of me."
    u "…"
    s "…"

    scene utakaraoke21
    with dissolve

    u "Huh. "
    u "I guess I am."
    s "…"
    u "…"
    s "And...you’re okay with that?"
    u "…"
    s "…"
    s "Uta?"

    scene utakaraoke22
    with hpunch
    stop music

    u "Ah! S-Sorry! I just..."
    u "The...blood rushed to my head from the fall!"
    u "I’ll get up!"

    scene black
    with dissolve2

    "Uta quickly hops off of me and pats herself down to straighten out her clothes."
    "The song that had been playing comes to an end and fills the room with silence."
    "Then, after a moment of respite for each of us, we quietly sit down on the couch and wait for the awkwardness to fade."

    scene utakaraoke23
    with dissolve2
    play music "thesleepingcity.mp3"

    s "…"
    u "…"
    s "So-"
    u "What’s that phrase about the elephant in the room again?"
    s "I believe that would be “the elephant in the room.”"
    u "We should probably talk about that."
    s "You mean how you got all red and looked like you were about to kiss me just now?"

    scene utakaraoke24
    with dissolve

    u "Uhh...yeah."
    u "You clearly didn’t buy the blood thing, so...I figure I’ve gotta explain myself or stuff will get weird."

    if bonus == True:
        s "Why didn't you just do it?"
    else:
        s "We should have just hugged instead."

    scene utakaraoke25
    with dissolve

    u "Sensei, I understand that you may be head over heels in love with me, but please don’t mistake my moment of confusion for the desire to smooch you."
    u "I just needed a second to figure out what the right move for everyone was."
    s "Everyone?"
    s "But we’re the only two people here. No one would have known if anything happened."

    scene utakaraoke26
    with dissolve

    if bonus == True:
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

label utaarchery1:
...
```

## Code that triggers this event

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid:
    if uta_love >= 0 and day247 == True and utamaid1 == False:
        jump utamaid1
    if uta_love >= 5 and utamaid1 == True and day > 5 and utamaid5 == False:
        jump utamaid5
    if uta_love >= 10 and dormwar17 == True and utamaid10 == False:
        jump utamaid10
    if uta_love >= 20 and bathhouse20part2 == True and utadorm15 == True and utamaid20 == False:
        jump utamaid20
...
```