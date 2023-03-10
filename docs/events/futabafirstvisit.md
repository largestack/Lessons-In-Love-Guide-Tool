# Under the Radar (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 5

* Event [Fan Fiction](./futabafall.md) (Futaba) is completed)



## Next events

None

## Event properties

* Id: futabafirstvisit
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm
* Triggered by path: futabadorm->futabafirstvisit

## Official wiki page

[Under the Radar](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabafirstvisit&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabafirstvisit:
    play sound "knock.mp3"

    "I knock on Futaba's door and wait for her to answer."
    "I figure with the amount of time I've spent at the library lately (As well as her not-so-hidden affinity for me), getting into her room shouldn't be all that hard."
    "But hey, she's a teenage girl and...girls can be territorial when it comes to their rooms or something. Probably."
    "I don't really know. Ami isn't like that at all, but Ami is also proving to be a...special sort of case thus far."

    f "Umm...hello?"
    s "Hey, Futaba, are you in there right now?"
    f "Sensei? I'm sorry, I had no idea you were coming. Is something wrong?"
    s "Nope. Just dropping by to see how you’re doing. Mind coming out for a second?"
    f "Of course! I'll be right out!"

    "I take a step back and wait for Futaba to- oh. Nevermind. She's already here."

    scene futabafirstdormredux1
    with dissolve

    f "Umm...hi. Is there...something I can do for you?"
    s "Yes, actually. Can I borrow 1000 yen?"
    f "I...suppose. But can I...ask why you need to borrow money from me?"
    s "Futaba, no. Don't just agree to lending me money like that. I was only messing around."

    scene futabafirstdormredux2
    with dissolve

    f "H-How was I supposed to know that? You've never visited me in my room before. I thought this might be some sort of emergency."
    s "The only emergency here is my boredom."
    s "Or something."
    f "..."
    s "Anyway, what are you up to?"

    scene futabafirstdormredux3
    with dissolve

    f "Just reading...like always."
    f "You're lucky you knocked at a good stopping point. Otherwise, I probably wouldn't have even answered..."
    s "You {i}did{/i} sound a little confused answering the door. Do you not normally get visitors or something?"

    scene futabafirstdormredux4
    with dissolve

    f "Not ones that knock, at least...Most people just walk in."
    s "Well, I'll make sure to follow proper protocol next time and just open the door without running it by you first."
    f "Please don't ever do that at any point ever. I would die."
    f "I'm more than happy to invite you in so long as I...actually know you're coming and-"
    s "Cool. Let me in, then."
    f "..."

    scene futabafirstdormredux2
    with dissolve

    f "Right now? Are you serious?"
    s "Sure. It's my duty as your teacher to make sure your...dorm room is conducive to proper...educational...learning stuff?"
    s "Does that sound like something a teacher would say?"
    f "That doesn't sound like something {i}anyone{/i} would say...why are you acting so strangely all of a sudden?"
    s "Is wanting to be alone with you inside of your room really that strange?"

    scene futabafirstdormredux5
    with dissolve

    f "Well...maybe {i}strange{/i} was the wrong word to use. It's just...entirely unexpected."
    f "But I guess if it's just to...make sure my room is conducive to proper...educational...learning stuff...it's okay?"
    f "There's not really...much to show you, though...so I doubt you'll have any fun."
    s "Just being with you is fun enough for me, Futaba."

    scene futabafirstdormredux6
    with dissolve

    f "Umm...this might be a bit of a silly question, but...this isn't some sort of prank, is it?"
    f "Did...someone put you up to this? Or...is there some sort of catch I don't know about yet?..."
    s "No. Why would you even assume that?"
    f "It's just that...this all seems a little too good to be true. That's all."

    scene futabafirstdormredux7
    with dissolve

    f "W-W-W-W-Which doesn't mean that I've actually ever thought about something like this happening, of course!"
    f "I just mean that in a...hypothetical situation where...I {i}had{/i} been dreaming about something like that...{i}then{/i} this would be too good to be true."
    f "But as it stands, it's just...it's just normal good."
    s "..."
    f "..."
    s "Futaba."

    scene futabafirstdormredux8
    with dissolve

    f "Yes, I'm sorry. Please follow me in, Sensei...but again, don't expect too much..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene futabafirstdormredux9
    with dissolve

    f "So, umm, here we are...my completely unexciting bedroom..."
    s "I'm going to go ahead and assume this the first time you’ve had a guy in your room?"

    scene futabafirstdormredux10
    with dissolve

    f "The only other {i}guy{/i} I know is my dad, so..."
    s "There's no way that is the only other male you know."

    scene futabafirstdormredux11
    with dissolve

    f "Boys, umm...weren't really interested in me in middle school...so I mostly just...flew under the radar."
    f "Way under the radar."
    f "And while I like attending an all-girls school for...completely unrelated reasons...it hasn’t really helped prepare me for situations like this..."
    s "No secret online boyfriends or anything either?"

    scene futabafirstdormredux12
    with dissolve

    f "Not that I'm aware of..."
    f "There was one...umm...person on a message board I used to visit, but...that was a...kind of...roleplaying thing, so..."

    scene futabafirstdormredux13
    with dissolve

    f "W-Why am I even telling you about that when you...obviously don't want to hear any of it."
    f "You’re just...here to look at the room...right, Sensei? For the...learning...education thing?"
    f "You probably don't even know what roleplay {i}is{/i} and...uhh..."
    s "..."
    f "..."

    scene futabafirstdormredux14
    with dissolve

    f "Can you please say something to prevent me from rambling and revealing any more embarrassing secrets?"
    s "I guess, but I was kind of interested in hearing where that was going."
    f "I don't even know...how I would have started in explaining it, so...it's probably best if we just move on and forget any of the last two minutes ever happened."

    "I scan Futaba’s side of the room and I'm not able to really learn anything new about her other than that she's a bit neater and more organized than Rin."
    "There’s a quote from Edgar Allan Poe on her dry erase board, which is...sort of surprising since she doesn't seem like the type to indulge in gothic poetry..."
    "But I guess I don't really seem like that type of person either and I don't have any problems with him."
    "Dying alone, drunk, and probably rabid is a pretty memorable way to go out, all things considered."

    scene futabafirstdormredux12
    with dissolve

    f "So, umm...this is where I do all of my school work and...all of my writing."
    f "When I'm...actually able to get any writing done, that is. Being creative is...kind of really hard and I wish I was better at it."
    s "Well, have you started writing anything for me yet? Because practicing is pretty much the only way you're going to get any better."

    scene futabafirstdormredux10
    with dissolve

    f "I have, but....it’s not very good."
    s "Can I see it? Or are you going to make me wait until it's more up to your standards?"

    scene futabafirstdormredux15
    with dissolve

    f "I-Ignoring how low my standards are...please wait a little longer!"
    f "I've...barely even started! I need more time to...build the world and...the characters and..."
    f "The plot..."
    s "..."
    f "..."
    s "How much have you gotten done, exactly?"
    f "The..."

    scene futabafirstdormredux16
    with dissolve

    f "The title?..."
    s "Wow."
    f "Being creative is...{i}really{/i} hard..."
    s "Hey, I told you before right? I’ll help you with whatever you need help with."
    f "I know, I know...It’s just really embarrassing."

    scene futabafirstdormredux15
    with dissolve

    f "Like...if it’s not good enough, I'm worried you’ll think I’m a loser and...want to give up on me or something."
    s "Futaba, you’re one of the brightest girls I know."

    "Probably."

    s "Plus, aren’t we supposed to be friends now? Or were you not paying attention in class when I said that?"

    scene futabafirstdormredux17
    with dissolve

    f "I was definitely paying attention!"
    f "I’m just still getting used to thinking of you as more than my teacher..."
    f "Up until recently, I...had no idea a friendship with you was even possible..."
    s "Is there...anything I can do to make the process a little easier?"
    f "To...make it easier?"
    s "Yeah. Like something {i}friends{/i} would do, but not a teacher and a student?"

    scene futabafirstdormredux13
    with dissolve

    f "Not...anything that wouldn't make me sound really weird for suggesting it..."
    s "Well, that certainly sounded suggestive. Are you flirting with me, Futaba?"

    scene futabafirstdormredux17
    with dissolve

    f "N-N-N-N-No! I would never suggest anything like that with you, Sensei!"
    s "Well, that just hurts."
    f "Not that I don't find you attractive! I do! It's just that I respect you as a teacher and would never want to jeopardize our relationship and...uhh..."
    f "Uhhh!"
    s "Deep breaths, Futaba. Now, what were you going to suggest we do in a completely platonic, non-flirtatious manner that will still somehow make you sound weird?"

    scene futabafirstdormredux13
    with dissolve

    f "Just that...we maybe...I don't know...{i}hug{/i} or something?"
    s "Oh. Easy."

    scene futabahug1
    with hpunch

    f "Ah! Sensei! W-W-W-what are you doing?"

    if bonus == True:
        s "You literally just suggested this."
        f "I didn't think you'd just grab me! I didn't even have time to prepare!"
        s "How do you prepare for a hug?..."
        f "I have no idea! My mind is going a million miles an hour right now."
        f "And I...I think something hard is pushing up against me?"
        s "That’s just the feeling of my desire for you to succeed."
    else:
        s "I’m giving you a hug. You're going to be getting a lot of these in the new and definitely improved Patreon version of the game."
        f "I...don't really mind, but..."
        f "It was just so sudden..."
        s "Kind of like the need to rework 1.2 million words of text and completely remove all innuendos and NSFW content because the context and societal critique of this game isn't easily apparent in the first 0.2%% of it."
        f "Yeah...that does sound pretty bad..."
        s "It's okay, Futaba. Because now I can fight ghosts and hide soup wherever I want."
        s "Also, I can finally share my love for clown costumes with everyone."

    scene futabahug2
    with dissolve

    f "Your {i}what?{/i}"
    s "Nevermind that. The point is, we're friends now and, according to you, friends hug each other."
    s "I don't really have any friends, so this is news to me."
    f "Please don't just casually say super depressing things like that. They'll confuse me even more."
    s "You're going to have to get used to that side of me, Futaba. It is never going away."
    f "This is...all happening so fast."
    s "I guess. But hey, you're not trying to pull away, so I must be doing something right."

    scene futabahug3
    with dissolve

    f "Well...That’s just..."
    s "Just what?"
    f "..."
    s "..."

    scene futabahug4
    with dissolve

    f "Ugh...you’re right. I honestly like this a lot..."
    s "I knew it. You {i}were{/i} flirting with me."

    scene futabahug5
    with dissolve

    f "No...I just like hugs."
    f "And I..."
    f "I also..."
    f "I also like-"

    scene futabahug7
    with vpunch

    stop music
    play sound "phonering.mp3"

    f "Ah-"
    s "..."
    f "..."
    s "Sorry. I should take this."
    f "..."

    scene black
    with dissolve

    play sound "phonebeep.wav"

    s "Hello?"
    a "Hi, Sensei!"
    s "Hey. Did you need something?"
    a "Hm? No. Not really."
    s "..."
    s "So..."
    a "So what?"
    s "{i}So why did you call?{/i}"
    a "Oh!"
    a "I just suddenly felt like you were about to do something that would make me sad. So I figured I'd let you hear my voice so you can remember I exist."
    s "..."
    a "Sensei? Are you still there?"
    s "I'll talk to you later, Ami."
    a "Wait! Don't-"

    play sound "phonebeep.wav"

    "..."

    scene futabafirstdormredux9
    with dissolve

    s "Sorry about that. It was just Ami being overbearing again."
    f "She...really likes you, doesn't she?"
    s "Yeah, well...I'm kind of all she has, so..."
    s "Anyway, should we get back to the hugging now?"

    scene futabafirstdormredux13
    with dissolve

    f "Oh, umm...I think we've...done enough of that for today..."
    f "I was actually just...thinking that I should probably...keep writing that story you asked me to write, so..."
    s "So you're kicking me out?"

    scene futabafirstdormredux9
    with dissolve

    f "Can we think of it as me...politely asking you to leave?..."
    s "I guess we can."
    s "But this is not the last you have hugged of me, Futaba."
    f "..."
    s "Now, goodbye."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I exit the room in dramatic fashion, leaving Futaba dumbfounded and impressed by my above average way with words."
    "On my way down the stairs, I silently curse at Ami to myself for ruining what could have been a huge step for Futaba and me."
    "But I immediately forgive her upon returning home and finding dinner waiting for me."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabafirstvisit = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "{i}You can now spend time with her in her room!{/i}"

    stop music fadeout 5.0

    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rinfirstvisit:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
...
```