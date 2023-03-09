# Ad Meliora
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanesanabeach2&go=Go)


Part of event chain [How the World Works](./ayanesanabeach1.md)

## Event preconditions
✅sarasex equal to True (unknown variable)



## Next events
None

## Event properties
* ID: ayanesanabeach2
* Group: Sana
* Triggered by label: ayanesanabeach1

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label ayanesanabeach2:
    scene sanaatthebeach1
    with dissolve2
    play music "sidecharacter.mp3"

    s "Yo."
    s "Figured I’d come say hi since you’ve been all by yourself this whole time."
    sa "..."
    s "..."
    s "Sana?"

    scene sanaatthebeach2
    with dissolve

    sa "Oh...yeah. Sorry. I just..."
    sa "I wasn’t expecting you, I guess."
    sa "I figured you’d be staying with Ayane until it came time for us to leave."
    s "And I figured you would have joined us at some point, but...here we are."
    sa "Here we are..."
    s "Is this really how you wanted to spend your day? Alone under a tree while Ayane and I hung out without you?"

    scene sanaatthebeach1
    with dissolve

    sa "It beats getting killed by the sun, at least. "
    sa "Besides, I’d just be getting in the way if I came and joined you two. Even if...it was supposed to just be Ayane and me today."
    s "Uh-oh. Did I interrupt your romantic getaway with your roommate?"

    scene sanaatthebeach3
    with dissolve

    sa "Mhm. Do you really think I’d ever wear something like this for {i}you?{/i}"
    s "Crazy. All this time and I had no idea you felt that way about her. Does Ayane know?"

    scene sanaatthebeach4
    with dissolve

    sa "Of course. She’s the one who invited me after all. "
    sa "But I suppose I’ll always be second to you, Sensei. If only she and I went back as far as you two. Maybe then I’d have a real chance."

    scene sanaatthebeach5
    with dissolve

    sa "But, that aside...I’m glad the sun is finally gone. At long last, I can feel my energy returning little by little. "
    sa "Kudos to me for managing to both stay out of harm’s way {i}and{/i} give you and Ayane all of the private time you needed."
    s "Kudos to you, indeed. But there’s no need to bring up Ayane anymore when it’s time for the two of {i}us{/i} to have some “private time” now."

    scene sanaatthebeach6
    with dissolve

    sa "And what would you like to do with that “private time” I wonder?"
    s "That entirely depends on how much I am allowed to do."
    sa "I don’t remember setting any guidelines or rules for you to follow."
    s "Maybe not directly. But you’ve inadvertently set a bunch of unspoken ones throughout the brief time we’ve known one another."
    sa "Have I? "
    s "You have."
    sa "Name one. "
    s "Remember that time you passed out because I held your hand while you weren't looking?"
    sa "Doesn’t ring a bell."
    s "Or all of those times you told me you only looked at me as a teacher?"
    sa "Are you something more than that?"
    s "You tell me. I have no idea what to make of this...weird mood you’re in right now."

    scene sanaatthebeach7
    with dissolve

    sa "Weird?..."
    s "Yeah. Did that swimsuit unlock some sort of secret power or something? Because you’ve seemed a lot less...Sana than normal tonight."

    scene sanaatthebeach8
    with dissolve

    sa "I’m...the same {i}Sana{/i} as always, though."
    sa "I guess I’m just a little excited that you decided to spend time with {i}me...{/i}that’s all."
    sa "That stuff about being worried about bothering you and Ayane...it’s all I could think of over here."
    sa "I wanted to see you. I wanted to see you {i}so{/i} badly. But you belong to her and I belong to-"
    s "I don’t belong to anyone."

    scene sanaatthebeach9
    with dissolve

    sa "Then..."
    sa "Why not belong to {i}me?{/i}"
    s "I’m sorry?"
    sa "Am I not good enough?"
    sa "Am I too small?"
    sa "Is someone like Ayane or my mom better suited to your interests?"
    s "What’s...going on with you right now?"
    sa "Maybe I’ve been drinking? I was just saying the other day that I talk too much when I drink, wasn’t I?"
    s "You were...but I don’t see any alcohol laying around. "
    sa "Heat stroke, then? That makes people act all sorts of weird, doesn’t it?"
    s "It does, but..."
    sa "Why does it even matter? It’s just the two of {i}us{/i} now...so you shouldn’t be worrying about something as silly as why I’m acting the way I am if the way I’m acting is {i}good.{/i}"
    sa "Enjoy the moment, Sensei. We don’t get many of them."

    scene sanaatthebeach10
    with dissolve

    sa "Though..."
    sa "I really wish we did."
    sa "I get lonely...just like every other girl."
    sa "There are things I want. Things I want that everyone else gets to have while I sit in the background. Unremarkable and exceedingly average."
    sa "I don’t want to be average anymore. I want to be fun. Exciting. Someone like Ayane or...or Rin."
    sa "People who can talk to you without getting nervous or scared or worried or-"
    s "But that’s not you."

    scene sanaatthebeach3
    with dissolve

    sa "What do you know about who I am? "
    s "Only what you’ve taught me over the last...five or six semesters. "
    sa "I can teach you more, you know."
    sa "There are tons of things about me I’m keeping locked away. And there are only so many places I can hide the key."
    s "You’re not going to question how we’ve been together for five or six semesters despite still being a first year?"

    scene sanaatthebeach11
    with dissolve

    sa "Oh! Uhh...has it been that many already? It feels like just yesterday we were meeting one another and-"
    s "Who are you?"

    scene sanaatthebeach12
    with dissolve

    sa "Sana Sakakibara...part time bartender and full time student. Resident of...dorm number two. Ayane’s best friend. A...member of the light music club. "
    sa "A girl who...really likes you and...is having a really hard time accepting that?"
    s "..."
    sa "..."
    s "..."
    sa "..."

    scene sanaatthebeach13
    with dissolve

    sa "Oh, God damn it."

    play sound "static.mp3"
    scene colorbars with flash
    scene happy1 with flash
    scene sanaatthebeach14 with flash
    stop sound

    q "You know, you’re a real buzzkill. A girl you’ve been chasing after to no avail for [totaldays] days is finally starting to open up to you and you go and do {i}this?{/i} "
    s "You..."
    s "You’re the girl from..."
    s "From..."
    s "Where do I know you from?"

    scene sanaatthebeach15
    with dissolve

    q "I’m surprised you know me {i}at all.{/i} Those memories aren’t supposed to stick. "
    s "What memories? How do you know what is and isn’t supposed to stick? And how were you Sana just now?"
    q "So many questions. You must be {i}really{/i} confused, huh?"
    s "Can you blame me? It’s not every day someone I know transforms into someone else."

    scene sanaatthebeach16
    with dissolve

    q "Hey, hey, hey! How can you be so sure of that? That Ami girl is {i}really{/i} suspicious at times, isn’t she?"
    q "And what about Niki? A convenient childhood friend slash ex-girlfriend who’s also an idol that never gave up on you after all of those years away? Get real."
    q "There’s tons of weird stuff that happens to you."
    q "If I were you and {i}I{/i} were going to go hunting for shapeshifters, those two are where I would start. Not the short, quiet girl with unsightly habits."
    s "Unsightly habits? What are-"

    scene sanaatthebeach17
    with dissolve

    q "But enough about that! Let’s talk about my amazing impression and how awesome I am! "
    q "Hooray! Clap clap clap clap clap."
    s "I don’t want it to sound like I’m encouraging this since I’d prefer if you stayed {i}out{/i} of my students’ bodies, but...you should probably talk a little slower the next time you slip into Sana’s."

    scene sanaatthebeach18
    with dissolve

    q "First off, rude."

    scene sanaatthebeach19
    with dissolve

    q "Second, I didn’t {i}slip{/i} into anyone’s body. I’ve been me the whole time. "
    q "You saw Sana because that’s what you wanted to see. And you stopped seeing her the moment you realized you were never seeing her at all."
    q "The human mind is interesting...how it can be tricked into seeing or feeling certain things that aren’t there. "

    scene sanaatthebeach20
    with dissolve

    q "But I guess that maybe I {i}do{/i} take a little advantage of that from time to time. "
    q "It’s not every day that I get to talk to somebody, you know. Gotta seize the opportunity when the opportunity arises."
    s "Can you tell me...literally anything of value? Who you are? Why you’re here? Where Sana is?"
    q "Sana’s just a little further down the shoreline. Good luck trying to talk to her right now, though. "
    q "As for the other two questions...I’m sorry, but I can’t answer them."
    s "Why not?"
    q "Because I can’t."
    s "That’s not a very good answer."
    q "Hey, I don’t make the rules. In fact, I rarely ever even follow them. Which I guess inadvertently answers question numero dos but, in case anyone asks, that was totally off the record."
    s "Any vague hints pertaining to {i}who{/i} you are?"
    q "Wanna take a guess?"
    s "..."
    q "..."
    s "Are you..."
    s "God?..."

    scene sanaatthebeach21
    with dissolve

    q "Woohoo! You got it-"

    scene sanaatthebeach22
    with dissolve

    q "Completely and utterly wrong. Not even close. 0/10."
    s "Well, then...do you have anything to do with the weird shit going on in this world? Assuming you {i}know{/i} about the weird shit going on in this world, that is."
    q "Again, that’s not really something I can answer. But you’ve gotta say, it’d be pretty gosh darn weird if I wasn’t {i}somehow{/i} involved, right?"
    q "Showing up out of nowhere...passing as a mimic...I wager I’m probably the most suspicious person you’ve ever met."
    s "I wouldn’t say you {i}passed,{/i} by the way. Your impression was still miles off. "
    s "But I guess expecting anyone to be able to understand Sana without putting in the effort to actually get to {i}know{/i} her is just...not likely."
    q "Are you insinuating something there, buddy?"
    s "Just that it’s a little rude to make up someone’s feelings."
    q "I wasn’t making them up. I was just..."

    scene sanaatthebeach23
    with dissolve

    q "...Appropriating them?"
    q "Channeling her energy?"
    s "Are you a psychic now, too?"

    scene sanaatthebeach24
    with dissolve

    q "Nope! And I’m very thankful for that as the idea of being able to read {i}your{/i} mind gives me the heebie-jeebies."
    s "I am also thankful that you can’t read my mind right about now."
    q "Keep it in your pants, chief. I’m not that kind of character. "
    s "Even though you were only a step or two away from seducing me using Sana’s appearance?"
    q "Hey, I obviously would have backed down before it went anywhere. I just wanted to see how long I could mess with you before you snapped out of it."
    s "Snapped out of what, exactly? "

    scene clearnightsky
    with fade

    q "Another one of your thingamajigs. "
    q "You walked off to find Sana and, somewhere along the way, your mind went blank."
    q "Thankfully, I was close by when it happened.  So I got to see the whole thing. "
    s "I’m...blacking out right now?"
    q "Mmm...not quite. In fact, I’m not really sure what’s going on- what with you vaguely remembering me and being able to hold an actual conversation in your current state."
    q "Maybe you’re just getting a little better at being crazy?"
    s "Wow. What a fun and useful skill to have. "
    q "Yeah. Not many practical uses for that, are there?"
    s "Why can’t {i}I{/i} transform into other people? I want that instead."
    q "You can!"
    q "You just do it in a different way than me."
    q "Think of how many yous there are. How many yous there have {i}been.{/i} Each one entirely different from the last. "
    q "And think of how many yous there could be at this current moment! Grooming teenage girls in parallel universes...plunging life itself into a lecherous, endless bout of chaos!"
    q "There are just so many possibilities!"

    scene sanaatthebeach25
    with dissolve2

    q "And yet you have found yourself in {i}this{/i} timeline...where everything is bad and good all at once."
    q "Where time moves both backward and forward simultaneously...just like {i}Ayane{/i} said."
    s "If that was even her speaking. I’m not sure who I can trust anymore knowing that you can just...become other people."
    q "Thankfully, that’s a worry you won’t have to live with for long since you will {i}probably{/i} forget me again after tonight."
    q "I’ll never turn into {i}her,{/i} though."
    q "And I know it’s pointless to say this since I literally {i}just{/i} told you you're going to forget, but...try and remember that."
    s "Why won't you turn into Ayane? "
    q "..."
    s "..."

    scene sanaatthebeach26
    with dissolve

    q "Don’t wanna. "
    q "Don’t like feeling what she feels."
    q "Also, don’t make it sound like doing what I did tonight is some sort of hobby for me. I normally just try on their clothes. Very rarely do I feel the need to step in and start playing charades. "
    s "Maybe...don’t do that at all anymore."
    q "Going to have a hard time looking at Sana now that you know how she really feels about you? Or is that something you’ve known all along?"

    scene sanaatthebeach27
    with dissolve

    s "I won’t know anything for sure until {i}she{/i} tells me. Hearing her feelings fall out of someone else’s throat just isn’t enough."
    q "But you have your suspicions, of course."
    s "Of course."
    s "Everyone loves me."
    s "They have to."
    q "Do they?"
    s "The world was made for me."
    q "Was it?"
    s "Yes."

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach28 with flash
    stop sound

    q "Is that what you really believe? Or is that what you {i}want{/i} to believe?"
    s "It’s the only thing that makes sense."
    q "You talk to birds. You are no authority on what does and doesn’t make sense."
    s "Are you?"

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach29 with flash
    stop sound

    q "No."
    q "In many respects, I’m just as lost as you are. "
    q "I just got a little lucky and skipped living through the whole “infinite high school” thing."
    s "You get used to it. I’m not really complaining. "
    q "Why would you? Your life is great."
    s "And yours isn’t?"
    q "..."
    s "..."
    q "It will be."
    q "Some day."

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach30 with flash
    stop sound

    s "I hope that day comes soon."
    s "You’re kind of annoying and I feel like you can definitely tell me more than what you actually have, but..."
    s "I don’t hate you or anything."
    q "I’m glad."
    q "I don’t hate you either."
    s "..."
    q "..."
    q "I think we have to say goodbye now."
    s "I see..."
    s "I’m not going to remember you...right?"
    q "Probably not."
    s "Then, for the sake of ending this extremely weird conversation on a good note...can you tell me your name?"
    q "..."
    s "..."
    q "Why don’t you give me one?"
    s "{i}Give{/i} you one?"
    s "I have no idea where I’d even start. "
    s "I don’t know anything about you other than the fact that you have nice eyes and...occasionally  someone {i}else’s{/i} eyes instead."
    q "Would you like a suggestion?"
    s "It would certainly be appreciated."
    q "Then..."

    scene black
    with dissolve2

    q "Name me after your favorite flower."

    stop music
    $ renpy.end_replay()
    $ ayanesanabeach2 = True

    scene youdiditlol
    $ renpy.pause(7, hard=True)

    jump ayanesanabeach3

label ayanesanabeach3:
...
```

## Code that triggers this event
File: \game\AyaneEvents.rpy
Code:
```python
...
s "At this rate, you’ll be telling all of us and we won’t even {i}need{/i} Maya anymore."
    ay "Maybe we don’t need her to begin with?"
    s "..."
    ay "Anyone can do the reset thingy, right? Not just her. "
    ay "If that’s the case..."
    ay "I think I want to try it next time. "
    ay "Do you think she’ll teach me how if I ask?"
    s "I can’t say for sure, but...probably not. "
    s "Maya doesn’t exactly like change."
    ay "I don’t think any of us do. I mean, if I {i}liked{/i} this, I wouldn’t be losing sleep over it. I wouldn’t feel like I’m the only one going insane for realizing things everyone around me just...ignores."
    s "You still have me. And despite your tendency to take pictures of me when I’m sleeping, I still think you’re surprisingly {i}sane.{/i}"
    ay "..."
    s "..."
    ay "I’ve got another question."
    s "I’m sure you have hundreds so just...ask me whenever you think of one instead of wasting words on warning me first."
    ay "I felt like this one deserved a warning due to its depressing nature."
    s "Uh-oh."

    scene ayanebeachtrip15
    with dissolve

    ay "So..."
    ay "Makoto’s dad..."
    s "..."
    ay "That...was the first time anything like that has ever happened before, right?"
    s "As far as I know, yes..."
    s "But Maya’s made it sound like other people have met similar fates in the past."
    ay "Did those people come back?"
    s "I’m pretty sure {i}we{/i} were among them, so...I’m going to say yes."
    ay "Does that mean Makoto’s dad might come back too?"
    s "..."
    ay "..."
    s "I hope so."
    ay "It’s so weird how time is moving both forward {i}and{/i} backward at the same time."
    ay "How people who should be gone wind up coming back...how our memories get reverted...and how new things are {i}still{/i} happening every day according to Maya."
    ay "How do we know that {i}this{/i} hasn’t ever even happened before? That we’ve never had this conversation?"
    s "We...don’t."
    ay "Exactly. We don’t."
    s "Aren’t you worried of knowing too much, though?"

    scene ayanebeachtrip16
    with dissolve

    ay "Should I be?"
    s "I know I am. But I’ve also been repeatedly told that finding out anything about my past might result in my brain imploding, so...yeah."
    ay "I guess it would be kind of hard to {i}not{/i} worry about something like that, yeah."
    s "What if we all have something like that? Key memories that whatever is controlling this world doesn’t want us to have back?"
    ay "You mean, like...God?"
    s "Is that something you believe in?"

    scene ayanebeachtrip17
    with dissolve

    ay "I did."
    ay "But now?"
    ay "I’m not so sure anymore."
    ay "If God is real, what is this supposed to be? "
    ay "A test?"
    ay "What are we supposed to gain from this...incomplete knowledge of how the world works when we can’t even share it with anyone else?"
    s "Beats me. But I’ll leave the critical thinking to you on account of the whole mind implosion thing."
    ay "That’s fine. I’m just thinking out loud at this point anyway."
    s "Look at you, learning to share your thoughts instead of keeping them all to yourself."

    scene ayanebeachtrip18
    with dissolve

    ay "Yes...look at me."
    s "..."
    ay "..."
    ay "No, seriously. Look at me. I bought this swimsuit with you in mind and you’ve done nothing but stare at the water for the last ten minutes."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Our talk about the inner workings of the world grinds to a halt as Ayane resets her mind (No pun intended) and refocuses on the real reason I think she came here today."
    "To get away from everything."
    "To take a break from this great new burden and remind herself that, beneath the mountain of troubles she’s taken it upon herself to excavate-"
    "She is still young."
    "That she still has the rest of her school life ahead of her and that she shouldn’t have to worry about caring for {i}me{/i} or {i}Maya{/i} when all that should matter to her is {i}herself.{/i}"
    "But that is just the type of person she is."
    "Someone with more love inside of her than she has ever been shown. "
    "Why?"
    "Why does she have no regard for the way {i}she{/i} feels?"
    "Why would she sacrifice this brief respite for the chance to reflect on how there is no respite for those like us at all?"
    "I don’t know."
    "And I will not find out today- for I leave her as soon as the sun sets."
    "And I make my way over to someone who was smart enough to avoid it in the first place."

    if sarasex == True:
        $ renpy.end_replay()
        $ ayanesanabeach1 = True
        $ ayane_love += 1

        "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
        "........."
        "......"
        "..."

        jump ayanesanabeach2
...
```