# Important Things (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 15

* Event [Back Out in the Heat](./amidorm15.md) (Ami) is completed)



## Next events

None

## Event properties

* Id: amisroom15
* Group: Ami
* Triggered by label: amisroom
* Triggered by branch label: amisroom
* Triggered by path: amisroom->amisroom15

## Official wiki page

[Important Things](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amisroom15&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom15:
    scene lr_day
    with dissolve
    play music "normalday.mp3"

    "I decide to spend the morning with Ami, and not just because I don’t feel like going anywhere else this time."
    "I admit that this seemingly small factor may sometimes play a large role in determining whether I spend time with her or not, but it’s not like I don’t want to see her or anything like that."

    if bonus == True:
        "Ami and I have gotten close enough that I have basically accepted her as family at this point."
    else:
        "Ami and I have gotten close enough that I basically consider her family at this point. Which she definitely is not."

    if bonus == True:
        if amifingered == True:
            "Just...family with the added bonus of providing sexual favors for one another every now and then."
            "But whatever. Sue us. It's not like no family has ever done this sort of stuff together before."
        else:
            "The only thing is...it’s kind of hard to avoid that she might be feeling a little more than that."
            "It’s weird...When I first woke up here, I had every intention of just using any chance I had to get physically closer with her."
            "But now look at me."
            "I’m about to walk into her room and I don’t even {i}almost{/i} have an erection."
            "In fact, if I didn’t spend half of every day perving out on other [teenage]girls, I might even consider myself starting to change."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "I make my way over to Ami’s door and, as is becoming customary, decide to push it open without knocking like the true gentleman I am."
    "........."
    "......"
    "..."

    scene amisroomonefive1
    with dissolve2

    a "Hmmm hmmm hmmm~"
    a "Hmmmmm hmm hmmmmm hmmm~"

    "Ami happily hums a song to herself while sorting through her manga collection."
    "I’m surprised to see that she’s already dressed for the day when weekend-Ami has become all but synonymous with lounging around the house in her pajamas and waiting for me to talk to her."

    s "Morning. What are you doing?"

    scene amisroomonefive2
    with dissolve

    a "Ah?!"
    a "What the heck, [amimaster]? Why are you just sneaking up on me like that?!"
    a "Even if I never get mad at you for not doing it, you should still remember to knock, you know?"
    s "I don’t remember how to knock."

    scene amisroomonefive3
    with dissolve

    a "You...don't remember how?..."
    s "Yeah. I don't think my hands work that way. You'll just have to deal with this from now on. Sorry."
    a "Can you at least try to remember when it comes to knocking on other girls' doors? Because I don't want you walking in on {i}them{/i} when they're vulnerable."
    s "But with you, it's fine?"

    scene amisroomonefive4
    with dissolve

    a "Mhm. With me it's fine. But I really wish you'd at least warn me before coming in so I don't have a heart attack next time I turn around and see you there."
    a "So, does you being here mean that...you maybe want to hang out with me? Cause I was just going to spend the morning reading, but-"
    s "What were you going to read?"

    scene amisroomonefive5
    with dissolve

    a "Uhh...nothing you’d be interested in. "
    s "Try me."
    a "Okay, well...the series I’ve been reading is about this one girl with magical powers and-"
    s "Yup. Not interested."

    scene amisroomonefive6
    with dissolve

    a "I'm honestly a little surprised you even made it that far."
    s "I’m just kidding. You can keep going with your description."

    scene amisroomonefive5
    with dissolve

    a "Okay...So, she’s got magical powers and she needs to save the world from all these villains that keep showing up. "
    a "But the thing is, the biggest villain of them all is actually her childhood friend and love interest."
    s "Wow. Do you immediately spoil major details like that for everyone who asks you about something you're reading? Or am I just the lucky one?"
    a "Is it really even a spoiler if I know for a fact that you're never going to read it?"

    scene amisroomonefive7
    with dissolve

    a "Besides, you really don’t need to ask me about stuff I know you’re not interested in, [amimaster]."
    a "The fact that you’re willing to {i}pretend{/i} to be interested is enough for me."

    if bonus == True:
        s "Pretending? Who’s pretending? For all you know, I could be a huge otaku who just keeps his hobbies a secret from everyone else."
    else:
        s "Pretending? Who’s pretending? I'm a cool boy who likes cool boy things."
        s "In fact, they used to call me Cooly McCoolguy when I was in college. That's just how cool I was."

    a "Lies. You can't earn the title of {i}otaku{/i} unless you annoy other people about your hobbies and try to force them into liking the things you like."
    s "I feel like that's not true. But anyway, did you want to do something today?"
    s "It’s been a little while since the two of us just spent the whole day hanging around the house, so I figured we could do that if you don't have any better ideas?"

    scene amisroomonefive8
    with dissolve

    a "Wait, the whole day day? You mean like...morning, afternoon, and night?"
    s "Yes, Ami. Those are the three key parts of the day."
    a "So...I get to spend the entire day with you?"
    s "You do."
    a "And you’re not gonna go anywhere else?"
    s "I’m not."
    a "And you’re going to hold my hand the whole time?"
    s "Do you really think I'd fall for that?"

    scene amisroomonefive9
    with dissolve

    a "Heheh...I thought I might be able to fit that in there without you noticing."
    s "Holding hands for an entire day sounds a little too cute for my liking. I'm not sure if my mind or body would even allow it. "
    a "Are hugs too cute for your liking as well? Because I haven't gotten one of those yet and I'm starting to think you woke up anti-Ami today."
    s "I have literally been in here for five minutes and, within that time, already devoted my entire day to you. What more do you want?"
    a "An amount of hugs that is...bigger than zero?"
    s "Pass."

    scene amisroomonefive10
    with dissolve

    a "What’s even the point of spending the whole day together if I'm not allowed to hug you?! What else do you wanna do, Sensei?! Talk about the economy?!"
    s "What? No. Why would you even assume that?"
    a "Because it's the most boring thing I can think of and you are clearly only here to play with my feelings by not hugging me!"
    s "How about we just watch TV or something? That’s a thing we can both enjoy, right?"
    s "And hey, if you let me choose what we watch, I think I can be kind enough to let you hug my arm for a few minutes at a time so long as you don't squeeze too tightly."
    a "I don’t need permission to hug my [uncle]’s arm!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    a "Hey! Where are you going?! You can't just leave like that without saying anything!"
    s "I'm going to the living room before I wind up being assaulted by a five-foot redhead."
    a "I’m five-foot-two! This is a thing you should know!"
    a "Pay more attention to me!"

    "I exit Ami’s room and take a seat on the couch, waiting for her to join me."
    "I obviously have no problem hugging her or holding her hand or any of the other annoyingly adorable things she’s somehow able to say without blushing in the comfort of our home-"
    "It’s just really fun to tease her."
    "And I intend to continue doing that for the rest of our time together."
    "………"
    "……"
    "…"

    scene amisroomonefive11
    with dissolve

    a "…"
    s "…"
    a "You don’t love me anymore."
    s "You got me. All of the love inside of me has faded into nothingness."
    a "That’s fine. I just won’t cook you dinner anymore."
    s "Nevermind. I love you again. Please don't stop cooking for me. I will die."

    scene amisroomonefive12
    with dissolve

    a "Yay! You told me you loved me and I didn't even have to ask!"
    s "Yup. That is definitely what happened."
    s "This means you'll keep making me dinner, right?"

    scene amisroomonefive13
    with dissolve

    a "Heheh...we’ll see. Dinner’s not until much later in the day, so you’re going to have to be extra nice to me if you want to eat."
    s "I’m a prisoner in my own home."
    a "That’s right. And I, Ami Arakawa, am the true protagonist of this story."
    s "Does that mean I’m your childhood friend-slash-villain of the story like in that manga you were talking about earlier?"

    scene amisroomonefive14
    with dissolve

    a "I wish...It would be so much easier if the two of us were childhood friends."

    if bonus == True:
        a "Why did you have to go and be born like a million years earlier than me? And also be related to my dad?"
        a "You’re just putting roadblocks all over this relationship, [amimaster]."
    else:
        a "Why did you have to go and be born with brown hair? My parents would never approve of this relationship if they were still alive."
        s "Is my hair really such a problem?"
        a "Between that and all of your incredibly unkind opinions on revolving doors, it's like you're intentionally just putting roadblocks all over this relationship."

    if amifingered == True:
        s "I don’t know. I kind of like you the way you are."

        scene amisroomonefive15
        with dissolve

        a "Huh?"
        s "Yeah. I don’t know if the two of us ever would have gotten close if it wasn’t for our relationship."
        a "Can you...tell me you like me the way I am again, please?"
        s "No. That was your one compliment for the morning. You’ll get another in the afternoon. Please look forward to it."

        scene amisroomonefive16
        with dissolve

        a "Guess I’ll take what I can get, then..."

        scene amisroomonefive17
        with dissolve

        a "Besides, I...also like the way things are now. And even though you’re a big dummy jerk-pants who won’t hold my hand, I know I can rely on you."

        if bonus == True:
            a "I’d still probably feel safe with you if we were the same age but...I don’t know."
            a "I..."
            a "I’m probably gonna start ranting about weird stuff if you don’t stop me."

        "I wait for a moment to see if Ami continues."

        a "Sensei, this is the point where you’re supposed to stop me."

        "Damn it."

        s "Fine. Stop."

    else:
        s "What am I putting roadblocks over exactly? We’re just [uncle] and [niece]. The way things are now is fine."

        if bonus == False:
            s "Besides, if they're going to call them {i}revolving{/i} doors, they should at least be ensuring that they revolve 100%% of the time and that I don't have to physically push them in order to get through."

        scene amisroomonefive17
        with dissolve

        a "Uhh...yeah. I know. I was just...making a joke or something."
        a "Of course I know that...all we are is [uncle] and [niece]..."
        a "And that's...probably all we'll ever be."

    "Ami reaches out and grabs the remote for the TV, switching it on and turning it to some early-morning kids anime."

    s "I'm fine with you putting on whatever, but I didn't think you'd just waive your right to hugging my arm in short bursts throughout the rest of the morning so easily."

    scene amisroomonefive18
    with dissolve

    a "You say that like you have any influence over when and where I hug you."
    a "Also, why would I give up control of the remote when you’d just put on something lame like the news?"
    s "When have I literally ever put on the news before?"
    a "You used to put the news on all the time to try and get me to go to sleep when I was younger."
    s "Did it work?"
    a "Yeah, cause the news is boring."
    s "Cool. Then let's put the news on. You've had a long day and deserve the rest."

    scene amisroomonefive18r
    with dissolve

    a "I've been awake for half an hour!"
    s "Wow, it's been that long already?"

    scene amisroomonefive19
    with hpunch

    a "That's it! I'm hugging you now and you can't do anything about it!"

    "Ami lunges at me and latches onto my arm, digging her fingers into my skin and squeezing me so hard that there's honestly a chance I could bruise from it."

    s "I guess I kind of asked for this by teasing you, didn't I?"

    scene amisroomonefive20
    with dissolve

    a "That's right. The meaner you are, the nicer I have to be to make up for it. Sorry not sorry."
    s "What exactly is “Sorry not sorry?”"
    a "A thing that you would know if you weren't a dinosaur."
    s "Me being a dinosaur implies that you're part-dinosaur, doesn't it?"
    a "Nuh-uh. I didn’t get the dino gene. I’m a purebred cute girl who must be protected."
    s "Protected from what? We’re the only two people in the house."

    scene amisroomonefive21
    stop music

    a "You don’t know that."
    s "…"
    a "…"
    s "…"
    a "…"
    s "…"

    scene amisroomonefive22
    play music "normalday.mp3"

    a "Just kidding! Hahahahaha..."
    s "…"

    scene amisroomonefive23
    with dissolve

    a "Oh! [amimaster]! I’ve actually seen this episode before!"
    a "This is the part where two childhood friends have to fight each other to prove who’s strongest!"
    s "What is it with anime and this childhood friend trope? How often do people even keep friends from their childhood around?"
    a "Shhh, don’t ask questions about anime! Just accept it! Now watch."

    "The TV begins to flash as one of two unbelievably muscular characters start...charging up or something like that."
    "I'm probably wrong due to being a {i}dinosaur,{/i} but it's at least worth a guess."

    scene amisroomonefive24
    with dissolve

    a "Guh...I can’t remember who wins this fight. I’m getting nervous."
    a "You don’t mind if I squeeze you a little harder, right? Cause I’m gonna do that."
    s "I do mind, actually. But I accept that I lack the power or the resolve to stop you."

    scene amisroomonefive25
    with dissolve

    a "Oh. Wait. I remember who wins now. It’s the protagonist."
    s "Are you just going to spoil everything today?"
    a "Watch this, [amimaster]. The guy with the black hair is going to have his arms ripped off."
    s "Is that really a thing they can put on TV so early? It’s like 9 AM. "
    a "They got rid of censorship laws here years ago, don’t you remember? You’re allowed to show anything you want on TV now as long as it’s not a penis."
    s "What’s with this bias against penises? That's just plain unfair."
    a "Stop talking about penises and focus. {i}Shit's about to get real.{/i}"
    s "…"

    "You know, if you asked me to make a list of all of the things that would ever be said to me-"
    "I don’t think that last thing would have made it on there."
    "…"
    "I stop talking about penises and focus because shit is about to get real."

    scene amisroomonefive26
    with dissolve

    a "YEAAAAH! FUCK HIM UP!"
    a "TEAR HIS STUPID FUCKING ARMS OFF!"
    s "I have learned today that I really don't like the person you become when you watch anime."
    s "I think you’re changing and it worries me."

    scene amisroomonefive27
    with dissolve

    a "Too bad, [amimaster]. Because we’re gonna watch this all day."
    s "..."
    a "..."
    s "Are you sure you don't want to put the news on?"

    scene black
    with dissolve2

    "Ami, once again, refuses to change the channel and the two of us spend almost the entire day sitting on the couch and watching anime."
    "And despite me not understanding literally anything that is going on at any point, it’s still kind of fun, I guess."
    "Sure, my arm may have fallen asleep two or three hundred times over the last couple hours alone, but that’s beside the point."
    "Eventually, the show’s marathon comes to an end and the two of us get up to stretch out our limbs."
    "I never understood how broken your body can feel after just sitting in one place for an extended period of time."

    scene importantredux1
    with dissolve2

    a "Sensei, do you want to go ahead and take a bath while I start making dinner?"
    s "Oh, sure. What are you going to make?"
    a "Hmm...would beef be okay? Or maybe hamburger steak?"
    a "I’m kind of in the mood for something hearty and I don’t think we have a lot of ingredients left for other stuff anyway."
    s "Works for me. You’re sure it’s okay if I go in first?"
    a "Of course. We skipped lunch today, so I know you’re probably excited to eat."
    a "Having dinner ready by the time you get out will be my special present in exchange for you spending the whole day with me today."

    "It’s moments like this that truly make me realize just how good I have it right now."
    "I’ve got a job I don't inherently hate."
    "A home."
    "And someone willing to look after me even when I don't deserve it."
    "Life can’t get any better than this, right?"
    "..."
    "Life can't get any better..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "…"
    "I open the bathroom door and begin to fill the tub with water."
    "I take my clothes off, leaving them on top of the sink in the corner of the room, and get in once it’s full."

    play sound "water1.mp3"

    "…"

    scene senseibath
    with dissolve
    stop music fadeout 15.0

    s "…"

    "I let the water soak into my skin and wash away the exhaustion that comes from watching shonen fight scenes all day. "
    "I’m glad that Ami and I got to spend a whole day together for a change."
    "More often than not, I find myself just moving from one place to the next without thinking much of it."
    "But every once in a while, it really is nice to slow things down."
    "I should do things like this more often."
    "Hell, maybe I should even quit teaching and just stay at home full-time. "
    "NEET-life sounds pretty good now that I have a [niece] who waits on my every beck and call."
    "But, then again...that would mean forcing Ami to work. And for the time being, I just can’t envision that."
    "Call me selfish, but..."
    "I'd like to keep her as my own for a little while longer."

    s "…"

    "Oh well. "
    "It is what it is. I guess."

    scene black
    with dissolve2

    "I close my eyes and give in to the comfort that comes with warm water and heated porcelain. "
    "And..."
    "Within a matter of minutes..."

    if amifingered == False:
        "I can feel myself dozing off."

        $ renpy.end_replay()
        $ ami_love += 1
        $ amisroom15 = True
        stop music fadeout 7.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        scene bedroom_night
        with dissolve

        "The stew Ami made wound up being absolutely delicious. "
        "The two of us cleaned out the entire pot and Ami went into a food-coma shortly after."
        "Left with nothing else to do for the night, I decide to go to sleep a little earlier than normal."

        scene black
        with dissolve2

        if day == 6:
            jump advancetosun
        else:
            jump advancetomon

    else:
        "........."
        "......"
        "..."
        play sound "slidedoor.mp3"

        s "...?"

label amisfirsttime:
    if bonus == True:
        jump amisfirsttimex
    else:
        scene black
        with dissolve

        "A ghost opens the door and I need to fight it off to protect my home."
        "I emerge victorious."
        "No ghost can defeat me."

        $ renpy.end_replay()
        $ ami_love += 1
        $ ami_virgin = False
        $ amisroom15 = True
        $ specialclassroom = True

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        if day == 6:
            jump advancetosun
        else:
            jump advancetomon

label amisroom20:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom:
    if ami_love >= 0 and firsttimeamisroom == False:
        jump firsttimeamisroom
    if ami_love >= 5 and amisroom5 == False:
        jump amisroom5
    if ami_love >= 10 and amisroom10 == False:
        jump amisroom10
    if ami_love >= 15 and amidorm15 == True and amisroom15 == False:
        jump amisroom15
...
```