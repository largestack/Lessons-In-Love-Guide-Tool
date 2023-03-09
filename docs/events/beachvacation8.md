# The Legacy of Thaum Pt. I
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation8&go=Go)


Part of event chain [The Moon is Beautiful](./beachvacation7.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachvacation8
* Group: Main
* Triggered by label: beachvacation7

## Event code
File: \game\script.rpy
Code:
```python
...
label beachvacation8:
    "{i}Roughly 30 minutes later...{/i}"

    scene beachdnd1
    with dissolve
    play music "breeze.mp3"

    mo "Finally! The time has come!"
    mo "For what seemed like millennia, I have awaited this moment. "
    mo "Through all of the pain I have endured...all of the harsh rays of the sun! I have finally returned to my element!"

    scene beachdnd2
    with dissolve

    r "You were outside for like half a day. Why are you being so dramatic about this?"
    sa "Maybe she’s just...really excited? "
    r "I mean, duhh, but like, this isn’t even the first time we’ve played. We’re just starting a new campaign and Molly’s treating it like the biggest moment in her life."
    mo "Ha ha ha! That is where you are mistaken, Nithhala!"
    r "You can call me Rin while we’re not playing, you know. That’s my actual name. Not sure if you realize that or not."
    mo "Silence, Nithhala!"

    scene beachdnd3
    with dissolve

    mo "Today {i}is{/i} the biggest moment of my life, for I have finally found a place to call my own!"
    mo "And I know what you may be thinking..."
    mo "“Molly! What about the manga club? What about all of the wonderful times we have shared in that small, enclosed space?!”"
    mo "And you would be right in asking that...but this is different! This is vacation!"
    mo "The chance to enjoy our youth! "
    mo "I’ve finally found a class who accepts me for who I am! So who would I be to treat this like just another day?!"

    scene beachdnd4
    with dissolve

    m "So inspirational. I can feel myself shivering in anticipation."
    ay "Do you want my hoodie, Maya? It might help with the whole shivering thing."

    scene beachdnd5
    with dissolve

    m "You’re just looking for an excuse to take your shirt off in front of Sensei."
    ay "I’m just trying to help out a friend in need! It’s totally different."

    scene beachdnd6
    with dissolve

    mo "Oh. Speaking of friends, has anyone seen Futaba anywhere? Wasn't she supposed to be joining us?"
    mo "I printed out her character sheet and everything."
    r "Oh she texted me. She’s not feeling well right now so she’s resting in the bedroom and can’t play tonight."
    mo "Wait, really? But it’s the start of the campaign. That’s a pretty big thing to miss."

    scene beachdnd7
    with dissolve

    r "You and me can figure out a way to write her in later on. Let’s just focus on getting this thing started so we’re not up until like 3 AM."
    r "We’re already still running on zero sleep, need I remind you."
    mo "Right, right. Well then! Let me just check my notes again and we’ll start in a second."

    scene beachdnd8
    with dissolve

    t "So much energy. So much passion."
    t "Dungeons and Dragons, which are fictional creatures in case you were wondering, is a truly wonderful game."
    s "They haven’t even started playing yet."
    t "I finally know what it means to be young."

    "Molly begins to flip through a few papers behind her weird folder-thing while Tsuneyo and I sit off on the side, trying to figure out what’s going on."
    "Apparently, Tsuneyo still needs to get a better grip on the basics before she’s allowed to play, so she’s being forced to watch this time."
    "Just how complicated can this sort of game be? It seems like there is an annoying amount of prep work involved."
    "Good for Molly for being able to keep all of this organized, I guess..."

    scene beachdnd9
    with dissolve

    a "Did you ever figure out what class you’re going to play? I remember you having a hard time last I checked."
    m "I’m playing a cleric this time."

    scene beachdnd10
    with dissolve

    a "A cleric? Why a cleric?"
    m "It’s just more suited to my strengths, I guess."
    m "What about you? Wizard again?"

    scene beachdnd11
    with dissolve

    a "What do you mean again?! I’ve only played a wizard one other time!"
    m "We’ve only played one other time."

    scene beachdnd12
    with dissolve

    ay "What are {i}you{/i} going to play, Sana? It’s your first time, right?"
    sa "Umm...Y-Yeah."
    sa "I’ve watched a few videos of other people playing so I get how it works, but it’s still kind of nerve-wracking actually playing for the first time..."

    scene beachdnd13
    with dissolve

    sa "I’m going to play an...umm..."
    sa "I'm going to play an orc barbarian."
    ay "…"
    sa "…"
    ay "Neat."
    ay "That’s..."
    ay "Yeah, okay."

    scene beachdnd12
    with dissolve

    sa "What about you?"

    scene beachdnd14
    with dissolve

    ay "I’m going to be a rogue. I’ve gotten pretty good at being sneaky lately, so I figure something like this might work out in my favor."
    sa "Sneaky?...What do you mean?"
    ay "I’ll tell you when you’re older, Sana."
    sa "You’re only a little older than me, though..."

    scene beachdnd15
    with dissolve

    r "You good over there, Molly? Need my help with anything?"
    r "I know you’re not great with numbers and all that jazz."
    mo "Silence! We will now begin!"
    mo "Friends of the manga club! Ayane and Sana! Feast your eyes upon me as I narrate the beginning of your adventure!"

    scene beachdnd16
    with dissolve

    mo "A thick fog crawls over the mountains and spreads through the forest, obscuring your vision as you slowly open your eyes."
    mo "A shrill scream from a creature you’ve never heard before rings out in the distance. "
    mo "As you struggle to regain your consciousness, you quickly realize that you’re surrounded by several people you’ve never seen before, in a land equally as unrecognizable."
    mo "The fog begins to lift as soon as the creature’s screams stop, leaving the six...Err, right. No Futaba."
    mo "Leaving the {i}five{/i} of you alone and confused."

    "Molly leans back on her cushion and waits for one of the other girls to say something."
    "And, in other news, I’m already lost."

    scene beachdnd8
    with dissolve

    t "Imagine waking up in a world where you know absolutely no one."
    t "How horrible that must be."
    s "...Right."
    t "I wonder if they’ll make it out alive?"
    s "Let’s hope so."

    scene beachdnd17
    with dissolve

    r "You said we’re in the forest, right?"
    mo "That’s right."
    r "How far into it can we see? "
    mo "Go ahead and roll for perception."

    play sound "dice.wav"
    scene beachdnd18
    with dissolve

    r "That’s...a five."
    mo "You see trees. That’s it."
    r "Wow I can feel myself getting stronger by the second."

    scene beachdnd19
    with dissolve

    ay "Lidearel unsheathes a pair of daggers from her belt and lunges toward the halfling also regaining her consciousness."
    m "I’m not playing a halfling anymore. I’m an aarakocra this time."

    scene beachdnd20
    with dissolve

    ay "What? Aren’t those the bird people? You’re playing a bird cleric? "
    m "I am."
    ay "Well...whatever. I’m lunging at you anyway."
    m" Uhh...okay?"

    scene beachdnd21
    with dissolve

    mo "So are you like...attacking her or?..."
    mo "What’s going on?"

    scene beachdnd19
    with dissolve

    ay "I stop directly in front of her."
    ay "{i}You...You have something to do with this, don’t you?{/i}"
    ay "{i}You look different from the rest of us..You’re much more...feathery...{/i}"
    ay "{i}Tell us where we are or I’ll cut your throat and sell your plumes to the nearest fletcher.{/i}"

    scene beachdnd22
    with dissolve

    m "{i}I’m just as lost as you. So I suggest you put your daggers down before you do something you regret.{/i}"

    scene beachdnd23
    with dissolve

    a "{i}E-Everybody just calm down! I know we might be scared...but there has to be an explanation for this!{/i}"
    a "{i}Let's just take a second and talk to each other before we do anything crazy...okay?{/i}"

    scene beachdnd24
    with dissolve

    m "Your acting has gotten better."
    a "Thanks. I’ve been practicing voices in my spare time."

    scene beachdnd25
    with dissolve

    sa "{i}And why...why would we do that?{/i}"
    sa "{i}There’s only one way to fix situations like this...and it involves draining every last drop of blood from whoever was stupid enough to bring us here...{/i}"

    scene beachdnd26
    with dissolve

    a "…"
    m "…"

    scene beachdnd27
    with dissolve

    mo "Before you can respond, another cry rings out and fills the area with fog once more."
    mo "But this time, as soon as the fog spreads through the forest and crosses your feet, the shaking of a nearby tree beckons your attention."

    r "What kind of tree is it?"

    scene beachdnd28
    with dissolve

    mo "Does...it matter?"
    r "It matters to me."
    mo "Uhh...okay. History check, I guess?"

    play sound "dice.wav"

    r "Five."
    mo "You don’t know what kind of tree it is."
    r "Ugh."

    scene beachdnd29
    with dissolve

    sa "{i}Heh...it looks like maybe I was too quick to judge...{/i}"
    sa "{i}Maybe the five of us have more in common than we thought?{/i}"

    scene beachdnd30
    with dissolve

    ay "I’m going to move closer to the shaking tree, keeping my daggers drawn."
    m "You’re a rogue. Why are you charging in before anyone else?"
    ay "It fits my character. "
    m "Oh. Okay. Fair enough."

    scene beachdnd27
    with dissolve

    mo "The shaking of the tree turns to more of a quake with each step you take closer to it. "
    mo "A scent exudes from the branches and finds its way into your nostrils. It’s a sort of fungus-like, putrid smell that you can’t help but shudder at."
    r "If only I knew what type of tree it was..."

    scene beachdnd31
    with dissolve

    a "{i}Wait! Lidearel! We don’t know what’s in there yet! It could be dangerous!{/i}"
    m "You don’t know her name yet."

    scene beachdnd32
    with dissolve

    a "Huh? Didn’t she say it when she was lunging at you?"
    m "That was out of character. Your character doesn’t know it yet."
    a "Oh, crap. You’re right. Sorry."

    scene beachdnd33
    with dissolve

    sa "{i}That smell...it reminds me of home...{/i}"
    sa "Zagull Throat Spear reaches for the greataxe strapped to his back and pulls it out as he moves toward where umm...where Ayane’s character went."

    scene beachdnd8
    with dissolve

    t "How exciting."
    t "What do you think is in the tree?"
    s "What, the fungus thing? Probably a mushroom monster or something."
    t "Those don’t exist. You’re an idiot."
    t "Pretty soon, you’re going to be saying stupid things like how dragons exist as well."
    s "Then what do {i}you{/i} think is in the tree, Tsuneyo?"
    t "Branches. Leaves. Tree things."
    t "Maybe even a bird."
    s "Then why is it shaking?"
    t "Wind."
    s "Are they going to fight wind?"
    t "They will certainly try."
    t "I can’t imagine it will be easy to hit."
    s "…"
    t "…"
    t "I’m going to go get a drink."

    scene beachdnd27
    with dissolve

    mo "As Zagull Throat Spear and Lidearel approach the tree, the shaking comes to an abrupt stop and the fog clears once again."
    mo "The forest is now dead quiet apart from the sounds of several chirping insects."
    mo "But, just as you begin to think you’re safe...the smell grows stronger."

    scene beachdnd34
    with dissolve

    r "Nothing’s popped out of the tree yet, though, right?"
    mo "Right."
    r "Okay. I’m going to approach the tree as well, but can I perception-check to see if I can spot whatever is inside of it?"
    mo "Mhm. Go ahead."

    scene beachdnd35
    with dissolve

    r "This is the one. I can feel it."
    sa "Good luck..."

    "Rin keeps the die in her hand for several seconds, shaking it up and down before-"

    scene beachdnd34
    with dissolve
    play sound "dice.wav"

    r "…"
    sa "…"
    mo "What is it?"
    r "A five."
    mo "You don’t see anything in the tree."

    scene beachdnd36
    with dissolve

    r "Ngh!"

    scene beachdnd27
    with dissolve

    mo "As Nithhala fails yet another tree-related roll, the branches shake one final time and out hop two creatures, one directly in front of Zagull and one in front of Lidearel."

    scene beachdnd37
    with dissolve

    ay "Do we know what kind of monsters they are from our old world or anything?"
    ay "I don’t know if you read my backstory but I used to live in the forest when I was a girl, so it would make sense for me to know it."
    mo "Yeah, you can go ahead and roll for history."

    scene beachdnd38
    with dissolve

    ay "Sweet..."

    "Ayane picks up a strangely shaped blue die and tosses it onto the table."

    play sound "dice.wav"
    scene beachdnd39
    with dissolve

    ay "That’s a 17."

    scene beachdnd40
    with dissolve

    mo "Thanks to years of struggling to grow up and foraging for food in the wilderness, you’re able to tell that the monsters in front of you are actually Violet Fungus."

    scene beachdnd41
    with dissolve

    ay "In a tree? Why?..."
    mo "It will make sense eventually."
    ay "Uhh, okay. If you say so."
    sa "{i}Mushrooms? I was just starting to get hungry!{/i}"

    scene beachdnd42
    with dissolve

    ay "{i}Wait! I recognize those mushrooms! You can’t eat them! They’re poisonous!{/i}"
    sa "{i}Step aside, elf. Poisonous is my middle name.{/i}"
    ay "You named your character Zagull Poisonous Throat Spear?!"
    sa "{i}I SAID MOVE ASIDE!{/I}"

    scene beachdnd43
    with dissolve

    s "I told you it was a mushroom monster."
    t "That’s cheating. You know more about the outside world than I do. "
    t "It’s an unfair advantage."

    scene beachdnd44
    with dissolve

    s "Whatever you say, Tsu-"
    t "...?"
    s "Is that a beer?"
    t "Is it?"

    scene beachdnd45
    with dissolve

    t "I just grabbed a can."
    t "I don’t think I’m allowed to drink this. My father said it’s bad for me."
    s "You’re allowed to do whatever you want. You’re on vacation."
    t "Hm..."
    t "I suppose you’re right."
    t "Perhaps just a taste will be okay."

    scene beachdnd46
    with dissolve

    t "{i}Sip...{/i}"
    s "…"

    scene beachdnd45
    with dissolve

    t "Delicious."
    s "…"
    t "…"
    s "…"
    t "…"

    scene beachdnd47
    with hpunch

    t "Zzzzzzzzzzzz..."
    s "I was wondering how that was going to turn out."

    scene beachdnd48
    with dissolve

    a "Did...Tsuneyo just fall asleep on my [uncle]?"
    m "I think she was drinking."
    a "I don’t know how I feel about this."
    m "I wouldn’t worry. She seems harmless enough."
    a "I sure hope so."

    scene beachdnd28
    with dissolve

    mo "Okay, you were getting ready to attack, weren’t you Sana? That’s what it sounded like but I just want to make sure."
    sa "Oh! Um...sorry...Yeah. I wanted to attack it..."
    mo "Okay. You and Ayane can roll for initiative."
    r "What about me? I went over to the tree as well."
    mo "You’re fighting too?"
    r "Yeah. It’s revenge for all of my failed rolls."
    mo "Then yeah. You three can roll for initiative. Vylhana and Urreahk didn’t approach so they’re out for right now."

    scene beachdnd32
    with dissolve

    a "Wait, what’s going on? I’m having a hard time focusing with Sensei just letting some girl who isn’t me sleep on his shoulder."
    m "The other three are fighting a mushroom."
    m "Well, two mushrooms. You and I aren’t in combat and they’re the first monsters of the game, so it’s pretty safe to say they’ll die before we even get there."
    a "Oh. Well umm, want to trade character sheets and look at each other's stuff in the meantime then?"
    m "I already read yours but you can read mine."
    a "When did you even do that?"
    m "Do you want my sheet or not?"
    a "Oh...uhh...yeah. Sure."

    scene beachdnd16
    with dissolve

    mo "Okay, what did you guys roll?"
    ay "19."
    sa "16."
    mo "…"
    r "…"
    mo "Rin?"
    r "5."
    mo "Okay. Well, we’ll start combat with Ayane then."

    scene beachdnd49
    with dissolve

    ay "Do I get my sneak attack bonus for this?"
    mo "Why would you get a sneak attack bonus? Both monsters are looking right at you."
    ay "Because I’m a rogue and-"
    mo "Overruled."
    ay "Ugh, fine. Then I guess I’ll just attack whichever one is closest to me with my daggers."

    scene beachdnd38
    with dissolve
    play sound "dice.wav"

    ay "..."

    scene beachdnd49
    with dissolve

    ay "Does a 9 hit?..."
    mo "It does."

    scene beachdnd38
    with dissolve
    play sound "dice.wav"

    ay "Okay, cool. Then that’s..."

    scene beachdnd49
    with dissolve

    ay "That's 7 points of damage."
    ay "And as a bonus action, I’ll use my two-weapon fighting and attack the same monster again."

    scene beachdnd38
    with dissolve
    play sound "dice.wav"

    ay "..."

    scene beachdnd49
    with dissolve

    ay "Does a 9 hit?"
    mo "Yes. Nothing has changed in the last five seconds, so a 9 still hits."
    ay "Awesome. Then that’s another..."

    scene beachdnd38
    with dissolve
    play sound "dice.wav"

    ay "That's another 4 points of damage."

    scene beachdnd40
    with dissolve

    mo "Okay! Mushroom numero uno is looking a little worse for wear, but still hanging on."
    mo "That means it’s Zagull’s turn."

    scene beachdnd49
    with dissolve

    sa "{i}Ha! As expected from a rogue. Two attacks and not a single kill. How sickening.{/i}"
    sa "{i}Allow me to show you how a true warrior fights!{/i}"

    scene beachdnd50
    with dissolve
    play sound "dice.wav"

    "Sana cocks her hand back and rolls her die with a level of aggression I’ve never seen out of her before. "
    "That aggression is succeeded, however, by a moment of cuteness that I can not comprehend but entirely appreciate."

    scene beachdnd51
    with dissolve

    sa "Ah! Natural-20!"
    mo "Ayyy! Zagull Throat Spear already making himself known as the MVP."
    sa "I did it!"
    mo "You did! I’m still going to need to know what your damage rolls add up to, though. "

    scene beachdnd52
    with dissolve

    sa "Oh! I’m so sorry. Umm...let’s see..."

    scene beachdnd50
    with dissolve
    play sound "dice.wav"

    sa "That’s umm...20 damage total."

    scene beachdnd40
    with dissolve

    mo "Mushroom numero dos has been vanquished! Which leaves us with the grand total of one mushroom, who gets to attack before Nithhala."
    r "Of course it does."
    mo "After watching his dear mushroom comrade fall at the hands of Zagull, the remaining weakened mushroom turns to look at the orc barbarian."
    mo "A single tear rolls down his cheek."
    a "Mushrooms can cry?..."
    m "No. But they also can’t hop out of trees or turn around either."

    scene beachdnd53
    with dissolve

    mo "Silence! I told you it will make sense later!"
    m "Sorry. I’ll shut up."

    scene beachdnd40
    with dissolve

    mo "As I was saying, a single tear rolls down the mushroom’s cheek and it begins to glow a more vibrant shade of purple."
    mo "You can tell that the scent is beginning to grow more pungent, as if it’s desperately crying out for help."
    mo "Or maybe even trying to protect itself and avenge its friend."
    a "Why is she making us feel bad for the mushroom?"
    m "Because-"

    scene beachdnd53
    with dissolve

    mo "I said silence!"

    scene beachdnd40
    with dissolve

    mo "The violet fungus takes one look at Zagull, which may very much be its last and uses “Rotting touch.”"

    scene beachdnd54
    with dissolve
    play sound "dice.wav"

    mo "Does a...13 hit?"
    sa "No. My AC is a little higher than that."
    mo "Wow. All that drama for nothing then."
    mo "I guess this brings us to Nithhala's redemption turn."

    scene beachdnd55
    with dissolve

    r "Excellent. You said the first mushroom was looking a little worse-for-wear, right?"
    mo "Correct. It’s also crying now as well."

    scene beachdnd56
    with dissolve

    r "Heh...Perfect. Then this is really the only roll that matters at the end of the day."
    r "Nithhala lifts her finger and points at the remaining monster. Her eyes narrow as she focuses everything she has on eliminating it."
    r "Then, after taking a deep breath, her eyes widen and she casts Eldritch Blast."

    play sound "dice.wav"

    r "..."

    scene beachdnd57
    with dissolve

    r "Oh, you’ve gotta be kidding me."
    r "A 6 doesn’t hit does it?"
    mo "Actually, it does."

    scene beachdnd58
    with dissolve

    r "Really?! Then-"
    mo "BUT-"
    r "...But what?"
    mo "Isn’t the attack modifier for Eldritch Blast a plus five? That would mean you rolled a natural-1."
    r "…"
    mo "…"

    scene beachdnd59
    with dissolve

    r "Don’t do this to me."
    mo "Your Eldritch Blast misses the mushroom and connects with a tree ten feet to the side of it."

    scene beachdnd60
    with dissolve

    r "This is still a victory in my book..."

    scene black
    with dissolve2

    "The battle ends on the next turn as Ayane’s character manages to slice the mushroom monster in half."
    "Shortly after that, the party reconciles and comes to the conclusion that all of them have been summoned here from different worlds."
    "Not knowing what else to do or where else to go, they decide to band together. "
    "But it’s around that time that I decide to leave. "
    "It’s clear that this sort of thing just...isn’t for me."
    "But then again, it doesn’t seem like many things are."
    "I’ll just focus on getting a good night’s sleep and wake up tomorrow feeling refreshed and ready to go."

    scene nightsky
    with dissolve

    "I think it’s pretty safe to say that this was a mostly-successful first day of vacation."
    "Sure, there were a few parts of it that went a little different than I expected-"
    "But overall, it was a great experience."
    "And I’m hoping that tomorrow, something even greater happens."

    $ renpy.end_replay()
    $ beachvacation8 = True
    $ ami_love += 1
    $ maya_love += 1
    $ ayane_love += 1
    $ sana_love += 1
    $ rin_love += 1
    $ molly_love += 1
    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Your affection with Ami, Maya, Ayane, Sana, Rin, Molly, and Tsuneyo has increased by 1 point each!{/i}"

    "………"
    "……"
    "…"

label beachvacation9:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```