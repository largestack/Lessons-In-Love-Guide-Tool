# Japanese Summer (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Otoha love greater than or equal to 0

* Event [Conversations Outside of a Girls’ Dorm](./otohadorm1.md) (Otoha) is completed)

* Event [Uptown Girl](./saradate10.md) (Sara) is completed)



## Next events

* [Otoha: Locked In](./otohapark5.md)

## Event properties

* Id: otohapark1
* Group: Otoha
* Triggered by label: otohapark
* Triggered by branch label: saturdaymorning
* Triggered by path: saturdaymorning->otohapark->otohapark1

## Official wiki page

[Japanese Summer](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohapark1&go=Go) for more details.

## Event code

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohapark1:
    scene sky
    with dissolve
    play music "brighterdays.mp3" fadein 5.0

    "I step outside to find that the weather isn’t all that dreadful this morning."
    "I’m sure that will change as the day goes by because nothing good can ever persist for an entire 24 hours-"
    "But right now, things are looking up."
    "Including myself, of course, as the sun stings my eyes for staring at it longer than it wants me to."
    "Which is any amount of time."
    "But fuck it, if the sun wants to come out and say “What’s up? Here’s a little warmth,” in the middle of winter, the courteous thing for me to do is at least acknowledge him."
    "Or her."
    "Or they."
    "The sun can be whatever gender it wants to be and I won’t judge it for its decision."
    "I’m a good guy."

    scene otohapark1
    with dissolve

    "Oh right."
    "Otoha said something about coming to the park in the mornings. "
    "I guess it’s possible that I came here with that in mind, but..."
    "Well, I feel like I somehow would have wound up here regardless of whether or not she’d told me that."
    "It’s just that kind of day."

    s "Otoha? More like Yo-toha."
    s "What’s up?"

    scene otohapark2
    with dissolve

    o "…"
    s "Good morning."
    o "…"
    o "Did you really just greet me with “Yo-toha?”"
    s "No. That never happened."

    scene otohapark3
    with dissolve

    o "Yeah, I didn’t think so either. That would have been super lame."
    s "Almost as lame as hanging out in the park by yourself when there are tons of other girls who’d gladly come with you."

    scene otohapark4
    with dissolve

    o "Well, let’s see..."
    o "Nodoka hates mornings, Noriko hates mornings, and Rin works mornings."
    o "That’s pretty much everybody I’m close with so that leaves...me, myself and I. "
    o "It’s cool, though. I like having alone time and coming here by myself is a good way to relax. "
    o "Especially since it’s actually pretty nice out today."
    s "For now. I’m sure it’ll start snowing in like two hours or something."
    s "Kumon-mi’s weather patterns seem to fluctuate very dramatically from day to day."

    scene otohapark2
    with dissolve

    o "Guess we better make the best of it while we can then, huh?"
    o "Also, the weather really only gets weird during the winter. Every day in the summer is like, just hot and gross and stuff."
    s "Yup. That’s a Japanese summer for you. "
    o "Kinda pumped for the seasons to change again, honestly."
    o "Sure, it might get all humid and whatnot, but it’s a lot easier playing guitar with warm hands than cold ones."
    o "A lot less people come out to watch street performers in the winter too."
    o "Like, just take a look around you. We’re the only two people here and it's not even cold right now."
    s "Then I suppose you’ll just have to serenade me alone."

    scene otohapark5
    with dissolve

    o "Not only would that make me extremely uncomfortable, but I don’t even have my guitar with me."
    o "It wouldn’t be the first time I’ve had to figure out how to deal with just one dude watching me play while everyone passes by but...it’s definitely not something I want to get used to."
    s "Sure, but at least there would be a historically lower probability of him making a move on you than another girl."

    scene otohapark6
    with dissolve

    o "Wait, yeah. That’s a good point."
    o "I guess it's not creepy at all when you put it like that."
    s "No. It's definitely creepy."

    if bonus == True:
        s "Don’t let my bad advice lure you into a false sense of security unless I’m going to personally benefit from it."
    else:
        s "Please ignore anything I ever say to you that doesn't involve flower arranging. That's the only thing I'm really confident about."

    scene otohapark7
    with dissolve

    o "Roger. "
    o "Then, if you ever show up to find me playing by myself, just keep on walking and pretend you never even saw me."
    o "Only after dropping a 1,000 yen note in my guitar case, of course."
    s "How am I supposed to give you money {i}and{/i} pretend I don’t see you at the same time?"
    o "Maybe just accidentally drop it in one very specific location?"
    o "I don’t know man, you do you. A girl’s gotta earn some cash one way or another."
    o "And without a job, I’ve gotta rely on kind souls like you."
    s "Don’t call me a kind soul when I haven’t even tipped you yet."

    scene otohapark8
    with dissolve

    o "I’m just thanking you in advance since I know you’ll take good care of me."
    s "Well if you keep entrapping people like this, I’m sure you’ll be absolutely rolling in money in no time at all."

    scene otohapark2
    with dissolve

    o "Sure hope so."
    o "There would be some days in my old park where I’d be there for like ten hours and not even make 5,000 in total."
    s "Sounds to me like you should have found a different park."
    o "I don’t think it was the park’s fault. And I don’t want to sound cocky, but I don’t think it was mine either."
    o "It’s a lot busier on that side of town than this one. People just don’t really like giving out their money to street performers for whatever reason."
    o "Maybe if I grew up back when my mom did and people actually carried around cash, I would have had an easier time."
    o "She always made it sound so simple."
    s "Your mother was a performer too?"
    o "Once upon a time, yeah. She was in some girl band that toured Japan a few times but never really made it out of the country."
    o "Now she’s just a normal mom with a normal husband and a decently normal daughter."
    s "Didn’t you say something the other day about how she didn’t want you to be a musician, though?"
    o "Yeah, but like, I think it’s one of those things where you regret your own experiences and don’t want someone you care about to do the same thing or whatever."
    o "I don’t know. I don’t really get how old people think."
    o "Do you want to like...sit down, by the way? "
    o "It feels kind of weird carrying on an entire conversation with you just looming over me like some sort of statue."
    s "Oh. Yeah, sure."

    scene otohapark9
    with fade

    "Otoha slides over on the bench to make room for me, wrapping her arms around her legs in what could be interpreted as either a defensive stance or...just a comfortable one, I guess."
    "It’s strange how something as simple as folding your limbs a certain way can mean two completely different things. "

    o "So, speaking of how old people think-"
    s "Don’t do it, Otoha."
    o "Don’t do what?"
    s "Don’t call me old."
    o "Okay, I won’t."
    o "You’re definitely not young, though."
    s "Saying that is just as bad..."
    o "You’re...old by comparison?"
    s "I mean...that’s better. But..."

    scene otohapark10
    with dissolve

    o "I’m just kidding, Sensei. Well...kind of."
    o "You might {i}be{/i} old, but you act kind of like a...cool senpai or something."
    o "Not like the[school] prince or anything, but the broody guy that a really specific clique of girls all pine over."
    s "Right. But that’s only because the[school] prince position was taken over by you once you transferred in."

    scene otohapark11
    with dissolve

    o "That’s only true based on statistics! I’m clearly not princely at all!"
    s "Princess, then?"
    o "That’s just as embarrassing!"
    o "How do I become the dark and broody type like you?"
    s "Easy. Just give up on everything you’ve ever loved and surrender yourself to your impending demise."

    scene otohapark12
    with dissolve

    o "Woah. So lame."
    s "…"

    scene otohapark13
    with dissolve

    o "Pfft...{i}Just give up on everything you’ve ever loved. My name is Sensei and I’m the coolest guy in Kumon-mi.{/i}"
    s "…"
    s "You are making a mockery of my flawlessly flawed personality, Otoha."

    scene otohapark14
    with dissolve

    o "Only cause you’re making it so easy. You’ll never get a girlfriend if you keep acting like that, Sensei."
    s "I already told you I don’t want a girlfriend."
    o "Sure, but you’ll want one eventually."
    o "Like, you won’t just...go the rest of your life without one, right?"
    o "Have you ever even had an actual girlfriend before?"
    s "Yup. Just some idol chick. She’s famous now."
    o "Right, right. You dated a famous idol cause you’re the coolest guy in Kumon-mi."
    o "Which one? Anyone I would be familiar with?"
    s "Very much so."
    o "Oh yeah? Who? Let’s see if I-"
    s "I dated your vocal coach for five years."
    o "…"
    s "…"
    o "Who...do you think my vocal coach is?"
    o "I don’t...remember telling anyone about that."
    s "Niki Nakayama."
    o "…"
    s "She’s actually the one who told me she was coaching you. I’ve known for a little while now."
    o "…"
    s "…"
    o "And you just...decided not to say anything about it?"
    s "It never really came up in conversation."
    o "…"
    o "I don’t believe you."
    o "This is clearly a coordinated prank. Noriko probably heard about it from Niki and then...planned this with you or something."
    s "Call her."
    o "Like...right now?"
    s "Right now."
    o "But...she’s probably busy..."
    s "Call her and say nothing but “Sausage fest.”"
    o "I’m not going to call Niki and say “Sausage fest.” What does that even mean?"
    s "It’s her favorite dish and an inseparable bond the two of us share."
    o "…"
    s "…"
    o "Nah. This is a joke. I’m not falling for it."
    s "Why? Don’t think I’m cool enough?"
    o "Not that. It’s just..."

    if bonus == True:
        o "She’s...an adult."
    else:
        o "She’s...not an accountant."

    s "…"
    o "…"
    s "Okay. That’s fair."

    scene otohapark15
    with dissolve

    o "B-Besides! She’s said all kinds of messed up stuff about her ex before and you don’t really seem like that kind of guy!"
    o "Like yeah you’re...just as weird and stoic as she described, but I highly doubt you’d ever just up and ghost on someone who loves you as much as she loved him!"
    o "Like...don’t mention this to anyone, but she even said some stuff about how she almost killed herself this one time and like..."
    o "There’s no way...that person is..."

    scene otohapark16
    with dissolve

    o "It totally was you...wasn’t it?"
    s "I’m telling you, there are only two words you need to say to her that would answer every question you have right now."
    o "…"
    o "I’m not going to call Niki and say “Sausage fest.”"
    s "…"

    scene otohapark17
    with dissolve
    play sound "phonebeep.wav"

    s "You know, I really wish I didn’t have to keep doing this."
    o "Who...are you calling?"

    "I tap on Niki’s name and set my phone to speaker mode so Otoha can listen to her world shatter into a million pieces."
    "This will show her how cool I am."

    play sound "phonebeep.wav"

    ni "Yeah? What’s up?"

    scene otohapark18
    with dissolve

    s "Sausage fest."
    ni "What, like right now?"
    ni "Uhh...sure. I should have a little time before my lesson. I just have to get dressed."
    s "Actually, forget it. I changed my mind."
    ni "Already?..."
    s "Yup."
    ni "Well you better have a good excuse because I’m already halfway through taking my pajamas-"
    s "I’m actually with Otoha right now."
    ni "...What?"
    o "Hi, Niki..."
    ni "..."
    ni "[nikitemp]..."
    s "Yes?"
    ni "{i}Why{/i} are you with Otoha right now?"

    scene otohapark19
    with dissolve

    o "Your name is [nikitemp]?"
    s "We’re on a date. I was actually just calling you to brag about it."
    ni "Oh, no you are not! Put her on the phone right now!"

    if bonus == True:
        s "Sorry. About to do the sex to each other. Talk to you later."
    else:
        s "CHHHHHHHHH. Going through a tunnel. Talk to you later."

    scene otohapark20
    with dissolve

    ni "HOLD ON ONE SECOND, YOU FUCKING-"

    play sound "phonebeep.wav"

    "I hang up on Niki because I wear the pants in this relationship."
    "I lied about wishing I didn’t have to do this. It’s actually really fun."

    o "Why would you tell her that?!"

    if bonus == True:
        o "Niki and I have a good working relationship and the last thing I want is for her to think I’m sleeping with her ex!"
        o "This is going to be so awkward to have to explain!"
    else:
        o "Niki and I have a good working relationship and the last thing I want is for her to think I'm going through a tunnel!"
        o "You know how she feels about tunnels!"

    s "You brought this on yourself for not believing me."
    o "Don’t pin that on me! No one would ever believe something like that!"
    s "Then each and every one of them shall feel my wrath."
    s "Now, back to our date."
    o "No way! I’m supposed to meet her in less than two hours and now I have to call her and explain myself!"
    s "I see."
    s "Well, it was a nice and productive morning we had together, Otoha. Enjoy your vocal lesson."
    o "I’ll be lucky if I live through it at this rate! You know what she’s like when she gets mad!"
    s "You’re right. The only way out at this point is for us to kill ourselves together."
    o "Sensei! I’m being serious! Don’t mess this up for me!"

    scene otohapark21
    with dissolve

    s "…"
    o "...What?"
    s "I’m just..."
    s "I’m just glad you at least got to experience true freedom for a few days before the end..."

    scene black
    with dissolve2

    "Otoha’s phone goes off before she even has a chance to hop off of the bench. "
    "Without even saying goodbye to me, she answers it and frantically tries to explain that there was no date and that I was simply just trying to prove something."
    "Trying isn’t accurate anymore, though, as I’m clearly drowning in success right now."
    "…"
    "Maybe I should consider putting Niki on speed dial if I’m going to have to keep using her like this?"

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohapark1 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label otohapark5:
...
```

## Code that triggers this event

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohapark:
    if otoha_love >= 0 and otohadorm1 == True and saradate10 == True and otohapark1 == False:
        jump otohapark1
...
```