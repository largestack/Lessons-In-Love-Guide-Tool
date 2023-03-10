# One Man's Trash (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 20

* Event [Amongst Other Things](./iodorm15.md) (Io) is completed)



## Next events

None

## Event properties

* Id: bathhouse20
* Group: Io
* Triggered by label: bathhouse
* Triggered by branch label: bathhouse
* Triggered by path: bathhouse->bathhouse20

## Official wiki page

[One Man's Trash](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bathhouse20&go=Go) for more details.

## Event code

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse20:
    scene iopresent1
    with fade
    play music "io.mp3"

    i "Oh! Uhh, hi! How are you doing, Sensei?"
    s "I’m...good. "
    s "Why do you seem so surprised to see me?"
    i "Well, you never give me a warning when you’re coming, so I’m kind of always surprised to see you."
    s "Should I be informing you beforehand? Because that’s not really my style."
    i "No no no, it’s fine. I don’t mind at all."
    s "Right..."

    "I show up at the bathhouse (Which is apparently surprising) and immediately head over to the counter to talk to Io."
    "There are a good amount of people moving in and out of the lobby today, so I’m kind of wary about getting in the way."
    "But, at the same time, I’m a little {i}less{/i} wary because all of them are women who have, given the circumstances, probably pictured me naked for at least several seconds."
    "This somehow manages to calm me down."

    i "So...um..."

    scene iopresent2
    with dissolve

    i "So, we’ve got this new scented lotion that’s pretty cool, I guess."
    s "Amazing."
    s "Why are you being so weird?"
    i "Because I’m...always weird?"
    s "Medication again?"

    scene iopresent3
    with dissolve

    i "What? No. I haven’t taken anything today. I’m fine right now."
    s "So you’re just being weird out of habit and not because of an external force."
    i "Also not entirely true. You’re an external force and if I were to pretend you didn’t have at least a minor impact on how I’m acting, I’d be a liar."
    s "Are you..."
    s "Are you hiding something behind your back?"

    scene iopresent4
    with dissolve

    i "Nope!"
    s "What is it?"
    i "Nothing!"
    s "Hand it over, Io."
    i "What if it’s...something really gross? Like a bug?!"
    s "You didn’t take Uta’s pet beetle to work, did you?"
    i "That...depends on whether you’re interested in beetles or not!"
    s "Okay, so it’s not a beetle."
    i "It’s the...scented lotion! So boring, right?! "
    s "It better be something extremely embarrassing if you’re making this much of a big deal about it."

    scene iopresent5
    with dissolve

    i "Ugh...it is."
    i "The truth is, it’s...not really something I wanted to show you just yet. Which is why I was so taken aback when you came in."
    i "Like...another day or two and I would have been totally okay with showing you and-"
    i "Okay, maybe not {i}entirely{/i} okay. But I’d be at least kind of okay. Probably. Maybe."
    s "…"
    i "…"

    scene iopresent6
    with dissolve

    i "It’s just scented lotion. Forget everything else I’ve said up until this point."
    s "Correct me if I’m wrong, but I think a good reason this relationship has been as “successful” as it has been is because you don’t typically hide anything from me."
    i "That’s not true. I hid most of my medication stuff from you when I fell down the other day."
    s "But you also gave me the freedom to grab them and figure out what they were on my own."
    i "Yeah. But that’s just because it would have been light years easier to talk about it or explain things if I didn’t have to make the first step on my own."
    s "You really are a coward, aren’t you?"
    i "I'm absolutely worthless. "
    i "I’ll probably never do anything unless you force me to do it."
    i "Unless it’s like, asking you to go to an amusement park or something. That's something I can do on my own."
    i "Speaking of which, that sounds really good right about now."
    s "Why should I have to always make the first step to compensate for your issues?"
    i "Because if I make the first step, I’ll wind up accidentally tripping and destroying everything."
    s "And if I make the first step, I'll wind up pushing you over."

    scene iopresent7
    with dissolve

    i "Then it appears that neither of us will ever walk again."
    s "Io."

    scene iopresent8
    with dissolve

    i "Okay, fine! I’ll show you!"
    i "But...I should explain first!"

    scene iopresent9
    with dissolve

    i "A while ago..."
    i "In fact, I think it was the first time you ever came into my room...we talked about how...I like building stuff or making stuff and..."
    i "And that sometimes I make things like...toys or figures...or other things like that."
    s "Have you finally summoned the courage to actually start giving your creations away?"
    i "Uhh...not to random orphanages or...real kids or anything like that."
    i "But..."

    scene iopresent10
    with dissolve

    i "But I thought it might be nice if I could...give something to you, since..."
    i "You kind of took the first step back then in helping me realize I should just...go for it."
    i "And...you know, I thought it would be easier this way since it {i}is{/i} just you, but now I can’t help but feel like you’ll think it’s dumb and won’t want to talk to me anymore."
    s "If it's something you personally made, of course I wouldn't do something like that."
    s "A beetle, on the other hand..."

    scene iopresent11
    with dissolve

    i "Are you sure you want it? It’s like...not even done yet."
    i "Like, I was going to put the finishing touches on it while working tonight, so...it’s missing a few of the details and..."
    i "And you’re obviously too old for toys anyway."
    s "Who cares? Even if it’s something I have no use for, it’s something you made for me. "
    s "So, I obviously want to see it."
    i "Even if it sucks?"
    s "Even if it sucks."
    i "Even if {i}I{/i} suck?"
    s "Even {i}though{/i} you suck."
    i "And you’re not gonna just like...grab it and throw it on the ground or something, are you? Because I worked really hard on this one."
    s "That would be the actual meanest thing I could possibly do."
    i "It really would. And you’re not exactly a great person, so you can probably sense my hesitation."
    s "Your hesitation was apparent long before how “not great” I am started to weave its way into the conversation."
    s "Just show me. It’s no big deal."

    scene iopresent12
    with dissolve

    i "It is for me..."
    i "It’s like...giving you a little piece of me that you’ll take with you when you leave today."
    i "And so I’m worried not just about how much you’ll like it, but...what will happen to it."
    i "Is it just going to sit on a shelf and collect dust? "
    i "Will it be thrown into a box of a bunch of other things you feel bad about getting rid of because they’re not things you personally bought, but things that were given to you?"
    i "What if it breaks?"
    i "What if it breaks and you don’t want to tell me about it because it will look like you didn’t care for it as much as you should have, or..."
    i "I...I wouldn’t mind fixing it for you if it breaks. "
    i "I’m...really good at that kind of stuff after all."

    "In typical Io fashion, she’s trying to pull the plug at the last second."
    "The problem is that her paperthin arms, weakened by prescription drugs and apparent malnourishment, are too weak to get it all the way out of the socket."
    "She wants me to help her euthanize her worries because she, herself, is not strong enough to do so."
    "But pulling the plug should be a last ditch effort when all else fails, and she hasn’t failed yet."
    "At least not in my eyes."
    "I’m sure she’s failed in her own eyes time and time again. "
    "And I’m sure that every night when she pulls the blanket over her tiny frame, that is both the first and last thing she thinks of."

    s "I won’t break it, I won’t shove it into a box, and I won’t let it collect dust."
    s "I’m not displaying it on my desk at[school], though, because that would make me look immature and I’ve already cemented myself as the {i}cool{/i} guy."

    scene iopresent13
    with dissolve

    i "I wouldn’t expect you to do something like that anyway."
    i "In fact, I’d much rather you put it somewhere in your room so that I can kind of like...always be there, in a way."
    s "I really appreciate how you can still manage to be so cute despite being a tiny, green bundle of self-deprecation."
    i "And I really appreciate that you haven’t gotten tired of that yet."
    i "And..."
    i "Hopefully...giving this to you means that you never will..."

    scene iopresent14
    with dissolve

    "Io reveals the painted, wooden robot that she’d been concealing behind her back."
    "It’s quite similar to the one she showed me in her dorm room but, at least at first glance, it seems like there is a lot more work put into this version."
    "I’m not sure if she’s just getting better or if she only took extra care of this one because she intended to give it to me-"
    "But I want to believe it’s the latter."
    "In fact, it almost certainly is the latter."
    "Of course she’ll put extra care into something for me when she expects {i}me{/i} to be the person to ultimately save her from herself."
    "Or everything else."
    "To save her from a world she wants no part of, filled with people she wants no part of. "
    "But now I have a part of her."
    "Which is just one small step on the way to all of her."

    i "Are..."
    i "Are you going to...say something?..."
    s "I love it."

    scene iopresent15
    with dissolve

    i "You...you do?"
    s "I do."
    s "It’s obviously not something I can really {i}use{/i} because I am a grown man, but I’ll be happy to keep it in my room."
    i "And you’re not just saying that to make me happy, are you?"
    i "Actually, even if you {i}are{/i} just saying that to make me happy, it’s okay."
    i "I’m...I’m happy."
    i "It’s...the first thing I’ve ever really made {i}for{/i} someone and...I wish it would have been something a little more relevant to you as a person or...your interests, but..."

    scene iopresent16
    with dissolve

    i "I kind of just...think robots are really cute and stuff..."
    s "So, does it have a name?"

    scene iopresent17
    with dissolve

    i "Not yet."
    i "I was gonna give him one when I was like, {i}totally{/i} done. But, like I said...there are still a few more details to put in and..."
    i "And I think that {i}you{/i} should name him instead."
    i "It’s a boy robot, by the way."
    s "I didn’t realize robots had genders."
    i "This one does."
    s "Do you want to help me name him?"

    scene iopresent18
    with dissolve

    i "No...I want you to name him by yourself."
    i "I want you to give him a name that’s...important to you."
    i "It’s a lot easier to get attached to something if you get to give it a name, and...I think it would be really nice if you somehow got attached to this little guy."
    s "…"
    s "In that case..."

    $ robotname = renpy.input("What do you want to name your robot?")
    $ robotname = robotname.strip()

    s "I think I’ll call him-"

    scene iopresent19
    with dissolve

    i "I don’t have to know. "
    i "In fact, I don’t {i}want{/i} to know. Because then {i}I’ll{/i} get attached. And getting attached to a little part of myself sounds really exhausting."
    i "Honestly, I don’t understand how you can put up with {i}any{/i} part of me."
    s "The whole “being cute” thing really helps."

    scene iopresent20
    with dissolve

    i "Take care of Sensei for me...Okay, little guy?"
    i "When he’s sad...when he’s tired...when he’s angry..."
    i "Take all of the bad things that can happen to him and-"

    scene iopresent21
    with dissolve

    n "Sensei? What are you doing here?"
    i "Huh?"

    scene iopresent22
    with fade

    "Noriko and Kirin show up at the counter and the mood completely shifts."

    i "Umm...welcome to-"
    ki "Sensei, get this. Noriko and I were hanging out at my house when one of the pipes burst like {i}seconds{/i} before we were about to take a bath."
    ki "We were gonna just go back to the dorm and shower instead, but then we saw this place on the way back and..."

    if bonus == True:
        ki "Wait, are these baths co-ed? Do you want to get in with us?"
    else:
        ki "Wait, do you want to come back to the dorm with us afterward and watch the third season of Seinfeld?"
        s "Kirin stop."

    scene iopresent23
    with dissolve

    n "Hi, Io. I didn’t realize you worked here."
    i "Uhh...hey."
    s "It’s not co-ed. There’s a girls’ section. "
    s "I think it’s kind of busy right now, though."
    ki "Gotcha. Do you come here often or something?"
    s "More or less. "
    s "Io runs the place with her aunt, so it’s one of the only places I can really see her."
    n "Oooh, what’s that you’re holding? It’s cute."

    scene iopresent24
    with dissolve

    i "This is..."
    i "It’s...nothing..."
    ki "What even is that thing?"
    i "A...robot..."
    ki "Did you like, pick it out of a dumpster or something? It's kinda creepy looking."

    scene iopresent25
    with dissolve

    i "What?..."
    n "..."
    ki "Am I wrong?"
    s "Yes. It’s not creepy at all."
    ki "Do you actually like that kind of stuff, Sensei? "
    n "Wait..."
    n "Did you...{i}make{/i} that, Io?"
    i "I..."

    scene iopresent26
    with dissolve

    i "I found it in the trash."
    s "…"
    n "Really?...I kind of wanted one..."
    i "Bathhouse is...free tonight. Just go through the pink curtain."
    i "I’m...going to go on break..."

    scene black
    with dissolve

    "Io leaves [robotname] at the counter and quickly rushes to the front door without even grabbing her hoodie."
    "I follow closely behind her, trying to stop her from running away the same way she always does, but she immediately notices this and swings around."

    scene iopresent27
    with dissolve

    i "You don’t have to follow me."
    s "I know I don’t {i}have{/i} to. But I’m going to."
    i "Why? I’m probably just going to scream and cry and punch things."
    s "Because if I don’t come with you, you’ll wind up taking what Kirin said to heart despite it being obviously incorrect."

    scene iopresent28
    with dissolve

    i "It’s not {i}obviously{/i} incorrect. If that’s the impression she got, that’s the impression other people are going to get as well."
    i "I should have...practiced more and...gotten better before giving you anything."

    scene iopresent29
    with dissolve

    i "I should have been better..."
    s "Who cares what Kirin or “other people” think? You made it for me and I like it."
    s "I gave it a name and everything."
    i "I’ll make you a new one...with better materials and..."
    s "I don’t want a new one."
    i "…"
    s "So, where are we going?"
    i "You’re..."
    i "You’re still going to come with me?"
    s "Obviously."
    s "Just try and pick somewhere nearby. I wouldn’t recommend straying too far in the cold wearing just that."

    scene iopresent30
    with dissolve

    i "…"
    i "There’s a...bench I normally sit on during my lunch break..."
    i "It’s not far..."
    i "You really don’t have to come, though. It won’t be any fun."
    s "Then we’ll be bored and depressed together."
    i "Wouldn’t you rather be bored and depressed by yourself instead of bored and depressed with some random girl who’s just going to complain and make things sound worse than they actually are?"
    s "Not really, no."
    s "We’ve already uncovered that I mask my downsides by surrounding myself with other people."
    i "But there are two other girls who want your attention right behind you. They’re still looking this way."
    s "That's nice. But I'm looking forward right now."

    if bonus == True:
        i "You can probably see them naked if you stay here."
        s "I can see naked girls any time I want."
        i "Pervert."
        s "You’re wasting precious break time, Io."
        i "…"
        s "…"
    else:
        i "You can probably hug them if you stay here."
        s "I can hug girls any time I want, Io."

    scene black
    with dissolve2

    "Io turns around and leaves the bathhouse."
    "I follow behind her and-"

    s "Wait a second."
    i "...Huh?"
    i "What’s wrong?"
    s "I almost forgot something."

    $ renpy.end_replay()
    $ bathhouse20 = True
    $ io_love += 3

    "………"
    "……"
    "…"
    "{i}Io’s affection has increased to [io_love]!{/i}"

    jump bathhouse20part2

label bathhouse20part2:
...
```

## Code that triggers this event

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse:
    if io_love >= 0 and day247 == True and bathhouse1 == False:
        jump bathhouse1
    if io_love >= 5 and bathhouse1 == True and bathhouse5 == False:
        jump bathhouse5
    if io_love >= 10 and dormwar17 == True and bathhouse10 == False:
        jump bathhouse10
    if io_love >= 20 and iodorm15 == True and bathhouse20 == False:
        jump bathhouse20
...
```