# The VIP Treatment
Uta event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utadorm5&go=Go)



## Event preconditions
✅Uta love greater than or equal to 5

✅Event "[Uta: Love Me to Pieces](./utamaid5.md)" is completed (event=utamaid5)



## Next events
* [Kirin: Love, Dorms, and Other Things](./kirindorm10.md)
* [Uta: Shawshank Redemption](./utadorm10.md)

## Event properties
* ID: utadorm5
* Group: Uta
* Triggered by label: utadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label utadorm5:
    play sound "knock.mp3"

    "I knock on Uta’s door and wait for her to answer."

    if iodorm5 == False:
        "I haven’t been inside of her room yet, so I’m a little bit curious as to how things are set up in there."
        "Uta seems like the type to either keep things really neat or completely destroy everything in her path, so I’m interested in finding out which of the two is true."

    else:
        "The last time I was in here, it was with Io and..."
        "Well, let’s just say the room wasn’t exactly how I expected it to be."

    u "Ooh! My first visitor!"
    u "Who’s there?"
    u "You're not here to kill me, are you?"
    s "It’s me. Are you free right now?"
    u "Sensei? Yeah, sure! Come on in."
    u "I just cleaned up so you’re all good."

    if iodorm5 == False:
        "Oh, I guess she leans more toward the clean side after all."

    else:
        "Oh, good. I guess Io must have said something about my impression of the dorm when I went in there with her."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I try to push the door open but it gets stuck on something and I need to squeeze my way into the room instead of walking in like a normal human being."

    scene utafirstdorm1
    with dissolve

    s "…"
    s "{i}This{/i} is your idea of clean?"

    if iodorm5 == True:
        "It looks exactly the same as it did when I was in here with Io..."

    scene utafirstdorm2
    with dissolve

    u "Do you mean to tell me your room is cleaner than this, Sensei?"
    s "Yes. I do mean to tell you that."
    u "Wow, that’s actually really surprising. "
    u "I thought you’d be the type to leave things a total wreck."

    if bonus == True:
        u "Like a...naughty magazines and tissues all over the place kind of wreck."
        u "I’m sure you know what I’m talking about."
        s "Yeah, it doesn't exactly take a rocket scientist to figure it out."
        s "I remember when I used to be allowed to buy porn. Those were the good old days."

        "Damn you, Makoto."

        scene utafirstdorm3
        with dissolve

        u "How bad do you need to mess up to be banned from buying that kind of stuff?"
        s "Sometimes, you’re just in the wrong place at the wrong time."
        s "Which, coincidentally, is how I’m feeling in your room right now."
    else:
        s "What a rude assumption. I pride myself in how tidy my room is. And I only get a little help from Ami."

    scene utafirstdorm4
    with dissolve

    u "{i}Ahem...{/i}Are you even allowed in here in the first place, Sensei?"

    if bonus == True:
        u "I am a young, innocent girl and you are an older, stronger man who could take advantage of me at any moment."
        s "Where? I wouldn’t even have any room to do that if I tried."
    else:
        s "Yes. Now, clean."

    scene utafirstdorm5
    with dissolve

    u "At least acknowledge that I only recently moved in and that some of this is just temporary clutter!"
    s "I didn’t mean to insult you. I just figured things might be a little neater since you’re a {i}maid{/i} and all that."

    scene utafirstdorm6
    with dissolve

    u "Uta-chan is off tonight, Sensei. And she wouldn’t want to spend her free time being a maid in her very own room even if she weren’t."

    if bonus == True:
        u "However, if you act now, you can still hire Uta-chan’s exceptional maid services for your very own tissue-filled house."
        u "There is also a special VIP package available where Uta-chan will lay on your bed for two hours so your sheets will smell like her."
        s "And I’m assuming the catch is that I’m not allowed to lay with you?"
        u "Of course not. "
    else:
        u "However, if you act now, you can still hire Uta-chan’s exceptional maid services for your very own house!"
        u "There is also a special VIP package available where Uta-chan will lay on your bed for two hours so your sheets will smell like her."

    s "That just sounds like I’d be paying you to come to my house and take a nap."

    scene utafirstdorm7
    with dissolve

    if bonus == True:
        u "Exactly. But it’s one step closer toward your ultimate goal of getting freaky with Uta-chan so I figured you’d buy-in right away."
        s "Not if I have to pay. I already have Ami to-"
        u "To clean up all of the tissues?"
        s "…"
        s "To clean the entire house so I can continue laying around being useless."
        u "You sound more proud of that than you probably should be."
        s "And you sound a little too confident in the sales pitch for your napping-service."
    else:
        u "Exactly!"
        s "This is a bad deal."

    scene utafirstdorm8
    with dissolve

    u "That aside, do you really think it’s that bad in here? It wouldn’t make me happy if you thought I was lazy and whatnot."
    u "It doesn’t smell weird, too, does it?"
    s "The smell is fine."
    u "Cool cause I just spent way too much money on a bunch of essential oils from some flea market I went to with Io and I really needed to hear that it wasn’t a waste."
    s "It’s just really...unorganized. I guess that's a good word to use here."
    u "Well, we’ve got a lot of stuff and only a little room to put it all in."
    u "Like, how am I supposed to fit two whole wardrobes on my side of the dorm?"
    s "Those are both yours? I thought one was Io’s?"
    u "Nope, both mine."
    s "Then where do her clothes go?"
    u "Beats me. Maybe she’s hiding them all under the bed so no one can see them?"
    s "And why are your clothes all over the floor if you have two wardrobes?"

    scene utafirstdorm9
    with dissolve

    u "Are you only here to hurt me, Sensei?"
    u "After I opened my door {i}and{/i} my heart to you?"

    scene utafirstdorm2
    with dissolve

    u "Hey, wait a second, why did I open my door for you, anyway?"
    u "Isn’t it a little weird for us to be hanging out together like this?"
    u "I know that you’re in love with me and that it’s probably very hard to stay away, but you need to be careful or someone will think something of it."
    s "To be honest, you’ll probably see me around here a lot from now on."
    u "And that’s totally normal?"
    s "Normal for me, at least."
    u "I don’t really get it."
    u "Isn’t there some sort of security-person that should be keeping you away from all of us or can this[school] just not afford something like that?"
    s "I’m pretty sure it’s just more of the[school] not expecting someone like me to actually do something like this."
    u "Yeah, it’s definitely a little weird no matter how you look at it."

    scene utafirstdorm10
    with dissolve

    u "Well, like I said, I understand how hard it must be for you to stay away."
    u "So I will keep these late-night meetings a secret until further notice."
    u "I do have one condition, though."
    u "It's okay to stare at my clothes on the ground but if you start picking them up and sniffing them I will definitely be weirded out. Don’t do that."
    s "I can’t say that’s a thing I was planning on doing."

    scene utafirstdorm11
    with dissolve

    u "Well then okey-dokey, artichokey! We’ve got ourselves a secret!"
    s "Awesome. Not sure if I’d call it a secret, though, since I also hang out with the other girls in their rooms."
    u "Why would you let me set up a cute moment like that only to cut me down right after? Have you no shame, Sensei?"
    s "I really don’t."

    scene black
    with dissolve

    "Uta winks at me, but I’m pretty sure it’s a passive aggressive wink that she decided to break out in response to my sudden “betrayal.”"
    "Either way, it’s cute."
    "She spins around and her skirt flies up in the process, but she’s wearing leggings so I’m unable to catch a glimpse of anything interesting."
    "I follow behind her as she plops onto the bed stomach-first but, just as I’m about to take a seat beside her (Welcome or not), I notice something peculiar."

    scene utafirstdormleonard
    with dissolve

    s "…"
    s "What is this?"
    u "Hm?"
    u "Oh, that?"
    u "Leonard."
    s "A...stag beetle?"
    u "Rhinoceros beetle, technically."
    s "And where did you procure this creature?"
    u "Remember that flea market where I got all those essential oils?"
    s "You bought a rhinoceros beetle at a flea market?"
    u "Oh, no. But I found him on the way back and carried him home in my pocket."
    u "It’s freezing out. Poor little guy would have probably died if it weren’t for me."

    scene utafirstdorm13
    with dissolve

    u "Go on. Tell me how caring and adorable I am for taking in such a delicate lil’ guy."
    s "You picked up a bug off the ground and carried it home."
    u "I like to think I picked up sadness and taught it to smile."
    s "What does that even mean?"

    scene utafirstdorm14
    with dissolve

    u "It means Leonard is my buddy and if I was forced to choose between you and him-"
    u "I’d probably still choose you. But it would take a little bit of thought since he kinda depends on me and you have Ami."
    s "Oh, how’s she doing at the cafe, by the way?"
    u "Ami? She’s doing pretty good. She’s kind of already better in the kitchen than I am. "
    u "But since she’s got those twintails we’d be fools to not take advantage of ‘em."
    u "That hairstyle’s a hot commodity among the few men we actually get."
    s "She’s not actually trying to pull off a tsundere persona, is she?"
    s "She’s joked about that in the past but I’m not sure if it’s actually a thing she was going to follow through with or not."
    u "Oh, not at all. She’s a sweetheart. One of those clumsy types that always {i}almost{/i} trips when she’s carrying a tray but then somehow recovers at the last second."
    s "I’m pretty sure that’s just her being clumsy."
    u "Well, it’s cute. "
    u "She’s still got a bit to learn, though. Like, she’s got the “Master” thing down, but some people like being called other stuff and she’s still not comfortable with that."
    s "Other stuff? What kind of other stuff?"
    u "You know. Like “Prince” or “Oniichan.”"
    s "I don’t like the idea of either of you calling random guys “Oniichan.”"

    scene utafirstdorm15
    with dissolve

    u "Ohohoh~ Are you getting jealous, Oniichan? "
    u "You don’t want Uta-chan and your [niece] spending time with other boys?"
    s "Don’t tease me when I’m just trying to protect you."
    u "Protect us from what, Oniichan? Why do we need your protection?"
    u "You know I have an actual older brother, right? I call him Oniichan, too."
    u "Is he in trouble? "
    u "Are you gonna break into prison and beat him up?"
    s "No, I’m going to-"
    s "Wait, prison? What?"

    scene utafirstdorm16
    with dissolve

    u "He was dumb. Don’t worry about it."
    u "Fact is, though, long as the two of us are working somewhere like that, we’re gonna have to go a little out of our comfort zone."
    u "But who we are in there doesn’t mean anything if it’s not who we are on the outside."
    u "If I call somebody “Oniichan” or “Master” I’m really just trying to get into their pockets."
    s "That’s good to hear but, at the same time, you are really ruining the immersion for me right now."
    u "Never fear, Oniichan. Uta-chan’s off the clock right now and doesn’t mind being in character overtime for you~"
    u "Sure, you might’ve seemed like just another guy the first time you came into the cafe, but you’re more than that now."

    if bonus == True:
        u "You’re a special customer who needs {i}special{/i} service, if you know what I mean."
        s "Under normal pretenses, I feel like I would know that. But every time you say something suggestive, you immediately backpedal."
    else:
        u "Now, you're like...a really cool guy or something."
        s "Cool? You are being extremely suggestive right now, Uta."

    scene utafirstdorm17
    with dissolve

    u "Suggestive?! Sensei- me?! I have no idea what you’re talking about!"

    if bonus == True:
        u "To assume I’d {i}suggest{/i} something in my room while sprawled out on the bed with my little feet dangling in the air, you’re a real rascal!"
        u "Don’t get me wrong, I’m flattered you feel that way about me, but if I wanted to do any more I would have already tossed these clothes into the pile you’re standing on."
        s "Are you sure? Leonard is watching."
        u "He’s gonna have to grow up eventually! Better he learned from his parents than some video on the Internet!"
    else:
        s "Can I become the surrogate father of your rhinoceros beetle? We don't have to do anything."
        u "Sure."

    scene black
    with dissolve2

    "And that, kids, is how I became the adoptive father of a rhinoceros beetle."

    scene theend
    with dissolve2
    hide window
    $ renpy.pause(4, hard=True)

    $ renpy.end_replay()
    $ utadorm5 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utadorm10:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label utadorm:
    if uta_love >= 5 and utamaid5 == True and utadorm5 == False:
        jump utadorm5
...
```