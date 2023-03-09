# Not Even Me
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day21&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 21

✅Event "[Yumi: Five Million Dollars](./firsttimestreets.md)" is completed (event=firsttimestreets)



## Next events
None

## Event properties
* ID: day21
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day21:
    scene yumialley0
    with pixellate
    play music "blueair.mp3"

    "It’s been nearly three weeks since I was reborn here."
    "Have I enjoyed my time?"
    "Absolutely."
    "I wouldn’t trade it for the world."
    "But still-"
    "Something seems off."

    s "..."

    "I’m leaving[school] later than normal today on account of some ‘end of term’ paperwork I needed to file in the staff room."
    "Still not fully understanding how to do my job, I wind up staying later than everyone else."
    "The halls are dead now, as I’m sure you can see."
    "There’s no one here."
    "No one at all."
    "{s}Not even me.{/s}"

    play sound "static.mp3"
    scene whereareyou with flash
    scene yumialley0 with flash
    stop sound

    "What am I doing?..."
    "Why am I doing it?..."
    "Where do I go?..."
    "When will I get there?..."
    "These questions spread throughout my mind like an invasive species, killing off everything but themselves in an attempt to take me over once and for all."
    "Fighting it just makes them mate faster- and soon enough, I can not take a single step without cracking an egg."

    play sound "eggcrack.mp3"

    "I walk regardless."
    "For if I don't, there are greater consequences than just spending the night in a place I almost spent the night in anyway."
    "No. If I stay here, I risk losing myself- or whatever faint traces of {i}me{/i} this body has managed to absorb during its brief vacation in an incorrect plane."

    play sound "eggcrack.mp3"

    "Another egg cracks."

    play sound "static.mp3"
    scene whereareyou with flash
    scene yumialley0 with flash
    stop sound

    "And another day ends."
    "But not before I get lost in quiet contemplation of what my goal here is."
    "And not before I give up on that and make a new one instead."
    "I want to make a mountain of sorts."
    "I want to stand atop a pile of used up teenagers, knowing that if I were to take a rest at the summit, the pile would move and a new peak would form."
    "From the top to the bottom- transference of power we {i}all{/i} can enjoy."
    "How long until the mountain forms?"
    "How long until we're all used up?"

    play sound "static.mp3"
    scene whereareyou with flash
    scene yumialley0r with flash
    stop sound

    "My feet move on their own and lead me down a path I can not normally see."
    "I can't say when my body successfully managed to escape the confines of the school, but I am somehow feeling {i}more{/i} confined now that I am on the outside."
    "I can see a place where the sidewalk ends- and a glowing passageway of TV static beckoning me forward."
    "It's like it's calling me to escape."
    "It's like it's trying to help me."
    "And yet-"
    "I can not find it within me to move my legs."
    "But that's fine, for there are few doors in life that only open once."
    "And even if this door disappears-"
    "I can tear down whatever wall I want and make a new one."
    "This place was built for {s}you{/s} me."
    "I can do whatever I want with it."
    "Everyone else is just furniture."
    "Everyone else is a part of the pile."

    av "Hey..."
    av "What are you doing?"

    "A voice calls out to me from a nearby alleyway."

    play sound "static.mp3"
    scene yumialley1 with flash
    stop sound

    "I chase after it and wind up in front of something beautiful-"
    "But only because I like the way its cracks look in the moonlight."

    s "I..."
    s "I'm not really sure."
    y "..."
    s "..."
    y "You're a fucking weirdo, dude."
    s "Well, what about you? What are {i}you{/i} doing out here this late?"
    s "Shouldn’t you be back at the dorms or something?"

    scene yumialley2
    with dissolve

    y "Shouldn't you be minding your own fucking business?"
    s "Hey, you're the one who called out to me."
    s "Did you get into a fight with Chika or something? Or are you just...being rebellious again?"
    y "I did not {i}get into a fight with Chika.{/i} And I can promise you I'm not fucking...being rebellious or whatever."
    y "But it ain't like I expect you to fuckin' understand me either, so...ain't no point in talkin' about it."
    s "Gotcha. Well, I doubt you’re looking to have a conversation or anything, so I guess I’ll just see you whenever you show up to school next."

    scene yumialley3
    with dissolve

    y "Hey...Wait up a sec."
    s "...?"
    y "You..."

    scene yumialley4
    with dissolve

    y "You’ve been acting really fucking weird lately."
    y "Like...even weirder than usual."
    s "I wasn’t aware that you were paying that much attention to me."

    scene yumialley5
    with dissolve

    y "Don’t flatter yourself, dickwad. I'm sure anybody with even half a brain has noticed by now. I'm probably just the only one with the balls to call you on it."
    y "Just last month, you were on my case pretty much every fucking day."
    y "Shit, dude. You even tracked me down at the arcade a few times and made it so I can't even chill {i}there{/i} anymore."
    y "Doin' annoying shit has never really been {i}above your paygrade{/i} or whatever. I get that."
    y "But now?"
    y "Now it's like you're backin' down on even trying to change me with all this {i}Oh, just be less of an asshole{/i} shit."
    y "The fuck is going on?"

    scene yumialley6
    with dissolve

    y "It’s, like...messing with my head now and shit."
    y "I don’t like it."
    y "Just go back to givin’ me normal detentions or whatever if it’ll stop you from wanderin' around like a lost puppy in the middle of the fucking night."
    s "Thanks, Yumi. But I think you might be misinterpreting something."

    scene yumialley7
    with dissolve

    y "Oh yeah? Like what?"
    s "I’m not going through some depressive slump because of my inability to control you."
    s "In fact, I’m not really going through a slump at all."
    s "I’m just...wondering what I’m doing here. That’s all."
    y "What you’re doing here? This one of those, like...philosophical questions or some shit?"
    s "Maybe. It's kind of hard to explain."

    scene yumialley4
    with dissolve

    y "Yeah, then don’t bother."
    y "We’re all doin’ the same thing anyway."
    y "Ain't nobody who just {i}gets{/i} what they're doing here. We're all just...trying to survive in our own ways and all that shit."
    y "Not gonna carry on with that thought, though, since all you'll hear is just some fucking...chance to get to know me or whatever."
    s "Wow. It's almost like you can read my mind."

    scene yumialley8
    with dissolve

    y "The fuck is your deal, dude?! I’m finally being serious about something, so the least you can do is try to be serious as well!"
    s "Sorry. I’m just...a little surprised."
    s "You always act like you're on top of the world, so it's weird thinking you might actually be somewhat vulnerable."

    scene yumialley4
    with dissolve

    y "I ain't {i}vulnerable...{/i}And just because I'm showin' a slightly different side of myself doesn't mean I like you all of a sudden."
    y "I still think you’re a fucking creep who spends way too much time around [teenage]girls."
    y "But...I guess you probably have your reasons."
    s "I mean, being a [high_school] teacher is probably the only acceptable reason for something like that, isn’t it?"
    y "I guess so. Still seems fucking weird, though. And not just in the gross, perverted way."
    y "It's like...the way you look at us is really...{i}off{/i} sometimes."
    y "It’s almost kinda like you’re tryin' to remember something."
    s "..."
    y "I don't know if there's anything more to it than just you wantin' to be young again or some shit, but..."

    scene yumialley3
    with dissolve

    y "Whatever it is, stop doing it."
    y "And also, the next time you’re out here this late, don’t expect me to call out to you again. Got it?"
    y "I just felt like bein’ nice today or whatever."
    s "You know, I’d appreciate it if you could do the same for your classmates every once in a while."

    scene yumialley4
    with dissolve

    y "Like I give a shit about them."
    s "Do you give a shit about {i}me?{/i}"

    scene yumialley8r
    with dissolve

    y "Wha- Fuck no, I don't!"
    y "I already told you I was just bein' nice today! Ain't anything more to it!"
    s "Can you maybe...feel like being nice around Futaba sometime soon? Because she's kind of terrified of you, Yumi."

    scene yumialley8
    with dissolve

    y "Fuck no. Futaba's gotta actually stand up for herself for once and stop lettin’ me walk all over her. She ain't earned the right to be {i}terrified{/i} yet."
    s "Standing up for yourself is easier said than done, you know. Some people just...can't really do that."

    scene yumialley4
    with dissolve

    y "Ain't ever been a problem for me..."

    "Yumi looks like she wants to say more, but cuts herself off and goes back to staring at the ground."
    "It’s strange how the first ‘normal’ conversation we’ve had is in an alleyway in the middle of the night-"
    "But I guess expecting anything about our relationship to be normal wouldn't really make any sense."


    y "..."
    s "..."
    s "Listen, I think you should probably head back to the dorms."
    s "I know you can hold your own, but it’s already dark out and we have class in the morning."
    y "Who says I'm coming to class in the morning?"
    s "I do. Because you are."
    s "Now, start heading back or I will drag you there myself."

    scene yumialley7
    with dissolve

    y "You lay one fucking finger on me and I swear to god I’ll chop your whole hand off."
    s "Then hurry up and get out of here before you are buried in legal fees and medical bills."
    y "..."
    s "..."

    scene yumialley9
    with dissolve

    y "Ugh...whatever."
    y "But I ain't doing this just because you told me to, got it?"
    y "I'm just tired as shit and it's been a long fuckin' day."
    s "Right, right..."
    s "I’ll see you in class tomorrow, Yumi."
    s "Have a good night."
    y "..."
    s "..."
    s "Yumi?"

    scene yumialley10
    with dissolve

    y "Just..."
    y "Just fuck off already, would you?"

    scene black
    with dissolve2

    "Yumi leaves the alleyway and I begin to head back home as well."
    "It's strange that I ran into her out here so late, but...I'm kind of glad that I did."
    "Not because I was able to remind her once more of how easily some people are impacted by her words-"

    stop music
    scene happy9
    $ yumi_love += 1

    "But because she was able to prevent me from walking toward the light."
    "{s}Congratulations!{/s}"
    "{s}You have unlocked a special event with {b}[redacted]{/b}!{/i}"
    "{s}There is something buried underneath your feet.{/s}"
    "{s}探してみませんか？{/s}"
    "{s}Yumi's affection has xxxxxxxxxxxxxxxxxxxx!{/s}"

    $ renpy.end_replay()
    $ roomwithclocks = True
    $ day21 = True

    jump endofweekday

label day24:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
...
```