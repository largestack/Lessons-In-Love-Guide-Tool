# Pluto Was Never Really a Planet (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Lavender's Blue](./secondbeach14.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach15
* Group: Main
* Triggered by label: secondbeach14
* Chain sources: secondbeach14
* Chain sources path: secondbeach14

## Official wiki page

[Pluto Was Never Really a Planet](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach15&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach15:
    play sound "static.mp3"
    scene pluto1
    with flash
    stop sound

    "And so I shall whisk you away, on wings of misery and malice, to our next destination."

    if bonus == True:
        "A place with more water than the last, but immensely less sexual curiosity or desire to slide one’s fingers inside of a friend. "
    else:
        "A place with more water than the last, so make sure you bring a pool noodle and keep an eye on where the lifeguard is at all times."

    "It’s all fluid either way."
    "One example is just more literal than the other."

    s "I find myself in a place with a lower pixel count than normal."
    s "I narrate my thoughts because I am incapable of keeping them locked away."
    s "I am going to meet someone. "
    s "The night has come and I have accepted it."
    s "My shoes got wet around a mile back and are now irritating a blister I developed from walking in circles for too long."
    s "I wonder if I am bleeding."

    play sound "static.mp3"
    scene pluto2 with flash
    stop sound

    "I ʍoupǝɹ ᴉɟ I ɐɯ qlǝǝpᴉuƃ˙"

    "Narration slips back to where it’s supposed to be and I feel as if it had been all sorts of screwed up until just moments ago."
    "But that is fine, because I am on a mission."
    "A mission to meet a girl."
    "But which girl was it again?"

    play sound "static.mp3"
    scene pluto1 with flash
    stop sound

    "Someone wanted to talk to me about something."
    "I survey my surroundings."

    if bonus == True:
        "I ask them questions about who they will be voting for in the next gravure poll."
    else:
        "I ask them questions about who they will be voting for in the next content poll."

    "It is quite literally a survey."
    "To my dismay, however, none of them are willing to speak."
    "Low resolution boulders just aren’t the same as they used to be."
    "So I think of new resolutions. "
    "I remove a metaphorical pen from my real pocket and begin to draw."

    scene pluto3 with dissolve4

    "I don’t remember drawing ever being this hard."
    "But it’s not like I ever had the talent for this anyway. "
    "My hands tend to get bored a little too easily, and visual art is mundane. "
    "Which is one of the two important reasons I decided to start writing instead."
    "The second was buried many years ago."

    scene pluto4 with dissolve2

    "I begin to fill the scene with color, and it’s a little easier to do that than making the outline."
    "I use my spare time to doodle angry eyebrows and a frown over a set of rocks."
    "They’re angry because they can’t move and I can."
    "Fuck you, rocks."

    y "What in the absolute fuck are you doing right now?"

    play sound "static.mp3"
    scene pluto5 with flash
    stop sound

    s "Yumi! "
    y "...Yeah? The fuck do you have to yell it for?"
    s "I was just excited to see you."

    scene pluto6
    with dissolve

    y "Well...whatever. "
    y "Guess it only made sense that you wound up finding me. You always manage to do that somehow."

    "{s}CONNECTION RESTORED{/s}"

    s "Maybe you just suck at hiding?"
    y "Probably. Suck at pretty much everything else, so..."
    y "Congrats, I guess."
    s "So...you wanted to talk about something, right? "
    s "I don’t really remember how I got here, but I’m pretty sure I can remember that."

    scene pluto7
    with dissolve

    y "Shouldn’t you like...go to the doctor or some shit if your memory is that bad?"
    y "Sucks enough that you’re always fuckin’ turning into a zombie all the time. The least you could do is make sure it’s not fuckin’...terminal or whatever."
    s "I’ll be fine. Let’s just get this conversation out of the way so I can go do that sleepover thing or whatever it was I was supposed to do tonight."

    scene pluto8
    with dissolve

    if dormwarfloor1win == True:
        y "Ew, again? You literally just did that last night. Sleep in your own fucking room this time."

    else:
        y "What? Didn’t you do that last night?"
        y "In fact, I {i}know{/i} you did it last night because Chika wouldn’t shut the fuck up about it."

    s "I..."
    s "Yeah. I guess I did do that last night."
    s "Anyway, what’s-"

    play sound "static.mp3"
    scene pluto9 with flash
    stop sound

    "////////////////////////BUFFERING..."
    "////////////////////////…"
    "////////////////////////…"
    "////////////////////////…"
    "////////////////////////USER2 IS HAVING TROUBLE CONNECTING"
    "////////////////////////IT APPEARS THAT MORE THAN ONE USER MAY BE LOGGED IN AT THE SAME TIME"
    "////////////////////////PLEASE MAKE SURE ALL USERS ARE LOGGED OUT BEFORE TRYING AGAIN"

    s "I-"

    "////////////////////////PLEASE MAKE SURE ALL USERS ARE LOGGED OUT BEFORE TRYING AGAIN"

    y "Yo. Come...back or whatever. No use fuckin’ talkin’ to you about this shit if it’s not really {i}you{/i}."
    s "No, it’s me...everything just feels a little..."
    s "Wrong..."

    scene pluto10
    with dissolve

    y "That’s because everything is wrong. "
    y "You’re dreaming right now."
    y "And when you wake up, you’ll be right back in your bed."
    y "So why not use this opportunity to have a little fun?"
    s "Fun...how?"

    scene pluto11
    with dissolve

    if bonus == True:
        y "I guess we could like...make out or whatever."
    else:
        y "I guess we could like...hug or whatever."

    y "It’s a dream, so it’s okay."
    s "…"
    y "…"

    scene pluto12
    with dissolve

    if bonus == True:
        y "Making out isn't enough, huh?"
        y "Well...as long as it’s you...I wouldn’t mind-"
    else:
        y "Hugging isn't enough, huh?"

    play sound "static.mp3"
    scene pluto13 with flash
    stop sound

    y "…"
    s "…"
    y "Hey."
    s "Hi."

    scene frown
    stop music

    "you have strayed too far"
    "i will guide you back"

    s "What?"

    play sound "static.mp3"
    scene colorbars with flash
    scene contentwarning with flash
    scene lessons with flash
    scene everythingg with flash
    scene pluto14 with flash
    stop sound
    play music "sanctuary.mp3"

    "I make it to the water level."

    y "So, uhh...we’re not just gonna stand here all night, are we?"
    y "I figured if I managed to stay away from you for the rest of the trip that I could just dodge ever havin’ to talk about this, but you found me, so..."
    y "Yeah. "

    if bonus == True:
        s "You’re so wet right now."
    else:
        s "(Airplane noises)"

    y "…"
    s "…"

    scene pluto15
    with dissolve

    y "Actually...on second thought, I think I’m gonna go. Peace."

    play sound "static.mp3"
    scene pluto16 with flash
    stop sound

    s "Wait. No."
    s "I’m fine."
    s "Just...slap me if I start zoning out or something."

    scene pluto17
    with dissolve

    y "That’s a dangerous privilege to give me, dude. You won’t be able to feel your face for the next year."
    s "I kind of can’t feel it right now anyway, so it doesn’t really matter."
    s "Just tell me what this apparently super important thing you needed to come clean about is and we can get on with our respective nights."

    scene pluto18
    with dissolve

    y "It’s not really...{i}coming clean{/i}...it’s more just...trying to figure out what’s real and what’s not..."
    y "Which I’m sure sounds plenty fuckin’ weird to you, but...I don’t really know how else to word it."
    s "…"
    y "…"
    s "Did you want to-"
    y "Sit? Yeah. "
    y "Come with me."

    scene black
    with dissolve2

    "Yumi walks right past me and steps into the water to avoid having to move me out of the way."
    "I wonder if she’ll regret that decision over the next hour or two when it begins to irritate her blisters as well."
    "I’m sure there are quite a few of them, given how many circles she needs to go in just to survive."

    scene pluto19
    with dissolve2

    "We take our respective places on a rock not far from the natural archway we’d been positioned under just moments ago."
    "And, as expected, several moments of silence pass by before either of us attempt to speak."
    "Yumi opens her mouth as if she’s going to say something, but closes it several seconds later when she remembers that she’s not supposed to tell me anything ever."
    "I begin to wonder if this has something to do with my tendency to “lose myself” around her and then submit to the idea that I have no “self” and that those are just glimpses into another me."
    "Another me who, admittedly, struggles a bit more with rational thought-"
    "But sees the world in a light much different than anyone else."
    "Perhaps this is what it means to be a god."
    "Or simply what it means to be- because god (Or me) knows that the way I normally live is far from meaningful. "
    "Speak to me, delinquent angel."
    "Feed me your fears. Your concerns. And I will transform them into a means for you to escape the life you’ve grown to loathe."
    "I hate the water level."

    y "So, uhh...this job hunt sure is going great, isn’t it?"
    s "Is that actually what you were so afraid of talking about? Or is this just an excuse to stall?"
    y "I don’t fuckin’ do this often, okay? I’ve gotta like...warm up or some shit."
    s "You should have picked a better topic then, because your job hunt is going so poorly that I doubt we’d be able to squeeze even two minutes out of it."
    y "Is there, like...anywhere you think I should try next?"
    s "Not unless you’re okay with either wearing a maid costume or working alongside your mom."

    scene pluto20
    with dissolve

    y "Oh, fuck off. My mom hasn’t worked a fuckin’ day in her life. Ain’t nobody in their right mind gonna hire her."
    y "Fuck, dude. I’ve got a better shot at landing somethin’ than she does."
    s "She actually just started working at Sana’s mom’s bar a little while ago."

    scene pluto21
    with dissolve

    y "Wait, you for real? Why?"
    y "Even if they don’t talk anymore, she’s got a bottomless wallet in my dad since she scares the shit out of him. She doesn’t have to work."
    s "It’s not like I know {i}why{/i} she’s working. I just know she is."

    scene pluto22
    with dissolve

    y "I wanna say “good for her,” but frankly, I really don’t care."
    y "She can try to make up for walkin’ out on her daughter as much as she wants, but I’m not the type to forgive people that easily."
    s "I know that well from experience. "
    s "Not like I think you {i}should{/i} forgive me or anything after what I did to you..."
    s "But I know you’re not the type to really {i}want{/i} to do that in the first place because it makes it easier to shut people out."
    y "Don’t talk like you fuckin’ know me, dude. I don’t know what kinda shit you heard from my mom, but she doesn’t know me either. "
    s "Am I wrong?"

    if bonus == True:
        y "Doesn’t matter if you’re right or wrong. I just don’t want some douchebag pervert treating me like I’m some...friend or love interest or some shit."
    else:
        y "Doesn’t matter if you’re right or wrong. I just don’t want some douchebag hug addict treating me like I’m some...friend or love interest or some shit."

        "Little does Yumi know, I can quit hugs whenever I want."

    y "It’s shitty enough that you’re already cozying up to my fucking family."
    s "I mean, it’s not like I’m playing poker with your dad. I just hang out with your mom every once in a while."
    y "..."
    y "Is that really it?"
    s "Yeah. I have literally nothing to gain from lying to you about this."
    y "…"
    s "…"
    s "Now what? Would you prefer I told you I was dating her or something?"
    y "…"
    s "…"
    s "Yumi?"
    y "I saw you."
    s "Saw me what? I haven’t even touched her."
    y "Not with my mom."
    y "With...somebody else."
    s "…"

    scene pluto23
    with dissolve

    y "See...this is the part where shit is gonna get really weird. Because no matter how I fuckin’ talk about this, it’s gonna sound like I’m crazy."
    s "Well...the least I can do is pretend it’s not since you’re always snapping me out of mild hallucinations."
    s "You deserve to sound a little crazy after all you’ve done for me."

    scene pluto24
    with dissolve

    y "Thanks. But just the idea of {i}you{/i} havin’ to give me a fuckin’ free pass to not feel like I’m insane kinda sucks."
    s "Yeah, well...life kind of sucks. So it is what it is."
    y "You...uhh..."
    y "I don’t really remember when it was..."
    y "But a while ago, I was hangin’ out in some alleyway..."
    s "That could have been literally any night. That’s your favorite hobby."

    scene pluto25
    with dissolve

    y "Yo, fuck off. I’m trying to actually tell you something."
    s "My bad. I thought that was funny."

    scene pluto24
    with dissolve

    y "Well, it wasn’t."
    y "But...anyway, I was hangin’ out in some alley in the middle of the night when I heard a...familiar voice or whatever."
    y "So I obviously got up to like...just {i}make sure{/i} I wasn’t...mishearing it or some shit."
    s "Let me guess...that familiar voice belonged to me?"
    y "Yeah. Which isn’t weird by itself or whatever because like, you seem to basically {i}always{/i} be wandering around somewhere. "
    y "But...you weren’t alone that night."
    y "There was somebody else with you. And no, it wasn’t my fucking mom."

    if yumiknows == True:
        s "If this is about me “cheating on” Chika or whatever you’re going to accuse me of-"
        y "That’s not what I’m fucking talking about, asshole. Just...listen to me."

    else:
        s "I mean, you know pretty much everyone I know. So if you saw me with somebody else-"
        y "Just fucking listen to me for a second."

    y "It was...hard to tell with how dark it was and shit, so I can’t be sure that it was the same person, but..."
    y "Then I remember hearin’ something about...clouds that...sounded a lot like somethin’ I remember from when I was a kid..."

    scene pluto26
    with dissolve

    y "And then you...said a name."
    y "Kaori."
    s "...Okay? She’s a friend of mine. It’s not any more than that."
    s "I doubt she’d even be capable of anything more than friendship given her...eccentricity."
    y "No, dude. That..."
    y "I think that was my cousin."
    y "Did she have like, different colored eyes and shit?"
    s "Yeah. Have you really never seen her around before?"
    s "She works at virtually every restaurant in Kumon-mi...and was also a popular online model or something for a while."
    y "A: I don’t have enough money to go out to restaurants. And B: I only use my phone to make calls and shit."
    s "Either way, I can’t see why me hanging out with your cousin should be something you have to get all weird about bringing up."
    s "It’s just one of life’s many coincidences. "

    scene pluto27
    with dissolve

    y "Sure, yeah."
    y "It would’ve been all fine and dandy and totally normal except for the one minor detail that {i}I was pretty sure she was fucking dead.{/i}"
    s "…"
    s "Excuse me?"

    scene pluto28
    with dissolve

    y "I, like...didn’t have a lot of friends and shit when I was little."
    y "But she used to come over a couple times a month and keep me company while my mom was getting high."
    y "But...she suddenly stopped coming over one day. "
    y "I tried asking why, but all anyone ever told me was that she was involved in some accident and hooked up to machines and shit."
    y "And when I didn’t hear anything after a few years and stopped talkin’ to my family, I just assumed she never made it."
    s "…"
    s "I mean...she has said some stuff about being in the hospital. And the whole accident thing lines up with the weird onomatopoeia she used to describe what happened to her..."

    scene pluto27
    with dissolve

    y "Holy fuck...I had no idea."
    y "Has she said anything about like...family or whatever? What’s she like now?"
    s "Uhh..."
    s "That is...not an easy question to answer. Especially since I was pretty sure she was an alien until a few minutes ago."

    scene pluto30
    with dissolve

    y "Uhh...what?"
    s "Did she ever...speak strangely when you used to know her? Like...swapping out words for {i}other{/i} words and whatnot?"
    y "Not really. She was pretty normal apart from how she dressed and shit."
    s "Well, I hate to be the bearer of bad news, but she is very likely not the same person she used to be."
    s "She has a very particular...way of speaking now."
    s "Kind of like she’s relearning not only everything about communication, but life itself."
    s "Great work ethic, though. Maybe you finally have a path to employment after all."

    scene pluto31
    with dissolve

    y "Nah."
    y "If she’s that fucked up, there’s no sense in showin’ up and confusing her even more."
    y "It’s just nice knowin’ she didn’t wind up in the dirt."
    y "Fuck, dude. I could have sworn I was gonna leave this conversation feelin’ like some sort of maniac-"
    y "But to know that was actually her and not just some delusion is just..."
    y "Just fuckin’ wild."
    s "You don’t even want to meet her? Or...well, {i}re{/i}-meet her, I guess?"

    scene pluto32
    with dissolve

    y "Maybe some other time. Would probably wind up just makin’ me feel weird if I met her now and she was a totally different person. ‘Specially if it’s as bad as you make it sound."
    s "If that’s what you want..."
    y "Welp..."
    y "Guess that’s that, then."
    s "Are you done opening up already? Or do you want to talk more about past experiences from your childhood that helped turn you into the person you are today?"

    scene pluto33
    with dissolve

    y "Come on, man. This actually went kind of well. Don’t ruin it by makin’ me bring up a bunch of shit that has nothing to do with...anything. "
    s "But we’re on a roll. What if there are more acquaintances of mine that you’re related to? We should just get them all out of the way now."
    y "Nah. I said all I needed to say. "
    y "Just gonna go for a walk or some shit and try to...I don’t know- come to terms with this, I guess?"
    y "Fuckin’ weird thinking somebody's been dead for so long only to find out that they’re wandering around town talkin’ to your asshole teacher. "
    s "Yeah...I can only imagine how strange-"

    play sound "static.mp3"
    scene pluto34 with flash
    stop sound
    stop music

    s "That-"
    s "…"
    s "Yumi?"

    "Oh, how lovely it must be to have the world turned on its head."
    "To discover that the misery you’ve wrapped yourself in is nothing but a shroud of misunderstandings and pessimistic assumptions."
    "What else have you shed tears over that was not worth shedding anything at all?"
    "Have you bled yourself dry when you could have remained hydrated and healthy?"
    "Or, perhaps you enjoy the misery?"
    "Perhaps it is the feeling of helplessness that you can throw yourself into that gives your life meaning."
    "Because lack of meaning is meaning in itself."
    "And existing to be miserable gives you the only excuse you need to get yourself out of bed in the morning."
    "…"
    "Where did Yumi go, you ask?"
    "She left quite some time ago. "
    "But you’ve been here the whole time."
    "Watching minutes...hours tick by as you attempt to make sense of your existence through words on the screen."
    "Why does everything have to hurt so much?"
    "That’s simple-"
    "Because you want it to."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ secondbeach15 = True

    play sound "static.mp3"
    scene yayapoem1 with flash
    scene yayapoem2 with flash
    scene yayapoem3 with flash
    scene tryagain1 with flash
    stop sound

    jump secondbeach16

label secondbeach16:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
r "Because."
    r "You."
    r "Are."
    r "My."
    r "Friend."
    r "And if you want to {i}keep{/i} being my friend, you will get the fuck off of me right now."
    mo "But..."
    r "Molly. I don’t want to fucking hear it. "
    mo "But I..."
    r "I know what you’re going to say and...again...I don’t want to hear it."
    mo "…"

    play sound "static.mp3"
    scene lavendermisc
    with flash
    stop sound

    "Lavender's blue, dilly, dilly "
    "Lavender's green "
    "When I am king, dilly, dilly "
    "You shall be queen"
    "Who told you so, dilly, dilly "
    "Who told you so? "
    "'Twas my own heart, dilly, dilly "
    "That told me so."
    "Lavender's green, dilly, dilly "
    "Lavender's blue "
    "If you love me, dilly, dilly "
    "I will love you"

    scene black

    "A series of dots."

    scene lavender36
    with dissolve

    mo "Rin! I’m sorry! For yelling at Otoha and...and for tackling you!"
    mo "And for being an all around bad friend tonight! But...I can’t help it! "
    mo "I just want you to be happy! That’s all!"
    mo "I don’t want this to make things weird! I want to take it all back!"
    mo "I-"
    r "Chill."

    scene lavender37
    with dissolve

    r "I get it. "
    r "In fact, if there is literally {i}anything{/i} I get, it’s this exact thing."
    r "But..."

    scene lavender38
    with dissolve

    r "I don’t like you, Molly."
    r "And I {i}really{/i} don’t like how you acted tonight. It was fucking creepy and totally unlike you."

    scene lavender39
    with dissolve

    mo "I’m such an idiot...I’m such an idiot...I’m such an idiot..."
    r "Don’t...go beating yourself up about it..."
    r "You did a shitty thing, but...you’re a good friend when you’re not...jumping on me and shit."
    mo "I’m so sorry, Rin...I really am...Please please please please please don’t hate me..."

    scene lavender40
    with dissolve

    r "I won’t..."
    r "But...I think the two of us could probably use a little space for now..."
    mo "Oh my God...I’m sorry...I’m so, so sorry..."
    r "Yeah, you’ve mentioned that."
    r "Listen, I’m just gonna...go now. But it’ll be okay."
    r "I won’t tell anyone what happened and if anybody asks why we’re not talking or whatever, we can just...use the D&D thing as an excuse."
    r "Which...also makes a lot more sense now, by the way. So...sorry."
    r "That must have been a...really shitty position to be in."

    scene lavender41
    with dissolve

    mo "{i}*Sniff*{/i}"
    mo "Well...DMing is a tough job as-is, so..."
    r "…"
    mo "…"
    mo "Good luck, Rin..."
    r "Thanks..."
    r "Gonna need a...hell of a lot of it."

    scene black
    with dissolve2

    "Landing on the ground and not having your insides splattered all over the cement means that you can still pick yourself back up and start walking again."
    "Probably not right away because of all of the bone fragments that would need to be removed-"
    "And, who knows? Maybe you’ll need a new bionic leg or something like that."
    "But as long as you’re alive, you can keep on going."

    $ renpy.end_replay()
    $ secondbeach14 = True

    jump secondbeach15
...
```