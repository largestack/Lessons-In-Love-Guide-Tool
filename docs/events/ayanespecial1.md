# Nevermind (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Price of Experience](./day344.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: ayanespecial1
* Group: Ayane
* Triggered by label: day344
* Chain sources: day344
* Chain sources path: day344

## Official wiki page

[Nevermind](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanespecial1&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label ayanespecial1:
    s "Hey."
    s "What’s up?"
    ay "Oh, you know. Just...Ayane stuff."
    ay "Are you...busy right now?"
    s "I’m just watching Tsuneyo cook."
    ay "Huh? Are you all the way in the old district right now?"
    s "Nope. I’m at my house- where {i}you{/i} would also be if you weren’t using your “secret girl powers” again."
    ay "Oooooh..."
    ay "Yeah. "
    ay "Yeah, I’m feeling fine."
    ay "But...I was actually wondering if you’d want to come meet up for a little while."
    s "So you don’t want to come here, but you want me to come to you?"
    ay "Right."
    s "Am I a delivery service now?"
    ay "Hahah...maybe. "
    ay "It really is only for a little while, though."

    "I sigh to myself and look over at Tsuneyo, who isn’t paying any attention to me at all."
    "I doubt I could get away from the house without things looking suspicious, but..."
    "It isn’t often that Ayane actually asks me to come meet up with her in the middle of the night."

    s "Are you at your dorm?"
    ay "Nope."
    ay "I’m at[school]."
    s "What? Why?"
    ay "Hahah..."
    ay "That’s the weird part. "
    ay "I don’t really know."
    ay "I just got this urge to come here all of a sudden."
    s "Well that’s not suspicious at all."
    s "I’ll start heading over now."
    ay "Thanks..."
    ay "It really shouldn’t take long. Just tell Ami that you’re running out to buy them snacks or something and I’m sure everything will be okay."
    s "I kind of already botched that idea earlier by telling them to eat whatever's in the house. "
    s "I’ll think of something, though."
    ay "Okay..."
    ay "I’ll be on the roof when you get here."
    s "The roof? Why?"
    ay "The sky is all...pretty again."
    ay "You’ll see when you get here...hahah."

    "Each time Ayane laughs, it feels as if she’s punctuating a sentence that she’s either resistant to utter or just doesn’t want to bother with at all."
    "It’s a strange type of laugh- nothing like the bright and jovial giggles I’ve grown accustomed to hearing from her."
    "It means she’s hiding something again."
    "I don’t want to make things sound like I’m some sort of magician who can just tell how people are feeling at all times-"
    "But it doesn’t require a magician to discern the most obvious of verbal tics."
    "I heard somewhere that tics can be treated with medication, though."
    "So I utilize and accept my newfound role as the sole proprietor of Kumon-mi’s latest delivery service and offer up myself to her."
    "She will be fixed in no time at all."

    s "Okay."
    s "I’ll see you soon."
    ay "I love you."
    s "…"
    ay "…"

    play sound "phonebeep.wav"

    "One of us hangs up."

    s "Tsuneyo-"
    t "Go."
    t "I will inform the Emerald Guardian and the others of your absence."
    t "Dinner will be on the stove when and if you return."
    s "If?"
    t "Tragedy could strike at any moment. You must always be prepared."
    s "...Right."
    s "Anyway, I guess I’ll see you later."
    t "Perhaps."
    t "Goodnight, Sensei."

    "………"
    "……"
    "…"

    scene clearnightsky
    with dissolve2
    play music "undersea.mp3"

    "I attempt to look up at the clouds once I make my way outside but see nothing at all."
    "Nothing apart from a few stray nebulas and the remnants of dead celestial bodies drifting haplessly through the air."
    "I, too, drift haplessly through the air."
    "I float through the streets of Kumon-mi, tapping my fingers against glass boxes encasing the bulbs of streetlights as if I were tapping extensions of a ceiling in the halls of an old[school]."
    "A[school] I would have attended before my (?)  body had grown to its current size."
    "A[school] where I would have learned who I am or what I am or where I am or how I am."
    "A[school]."

    if bonus == True:
        "School."
    else:
        "College."

    "That is where I’m heading."
    "I need to remind myself, as being this close to the sky is somehow distracting me from the order at hand here."
    "To meet with a girl who needs to see me now more than ever."

    if bonus == True:
        "I wonder if we will have sex."
        "I hope that we will have sex."
        "I am happy when I have sex."

    scene black
    with dissolve2

    "I close my eyes and allow my metaphorical wings to carry me the rest of the way."
    "What I mean by this is that I’ve walked the path so many times now that I don’t even need vision in order to make it there."

    play sound "thump.mp3"

    "Or at least that’s what I think until I walk face first into a dumpster."
    "From that point onward, I keep my eyes open-"
    "Proving once and for all that you can never see more with them closed."
    "………"
    "……"
    "…"

    scene nevermind1
    with dissolve

    if bonus == True:
        "Ayane Amamiya\nOccupation: Happy girl\nVaginal Depth: Medium-Shallow"
    else:
        "Ayane Amamiya\nOccupation: Happy girl\nFavorite Fruit: Bananas"

    "She sits on a bench with a scarf wrapped around her that she had to purchase for herself because a man whom she would give her life for bought her friends one instead of her."
    "All she wanted was to match."
    "Some nights, she lays awake in bed, pondering over things those friends may have said to him while she was not around."
    "She worries that both of them are more compatible with him than she is."
    "She worries the same thing for virtually everyone else that she encounters, for sometimes simply hearing that the person you love loves you back is not enough to convince you."
    "She claims to have the blood of a warrior, but she is really just O-."
    "Giving to everyone, receiving from no one. And destined to lurk somewhere in the background until it is her time to shine."
    "Occasionally, she will glance up at the sky, wondering how much longer it will take for her “future husband” to arrive."
    "Unbeknownst to her, he is floating through the streets below, colliding with trash receptacles and attempting to catch birds."
    "He catches none, but several land beside her as she waits."
    "And waits."
    "And waits."
    "All the while, it grows."

    scene black
    with dissolve2

    "I eventually arrive at the[school] and glance down at my phone to discover that it’s taken me relatively longer than normal to make it here."
    "I have several missed messages from Ayane, but see no purpose in responding to any of them as I’ll be seeing her any minute now."
    "I spread my arms out and part the[school] gates like Moses parting the Red Sea."
    "It’s incredibly effective because the gates were actually left open, and it enables me to feel much more important than I actually am for a brief moment in time."
    "I move through the[school]."
    "I make it to the roof."
    "I open the door."

    scene nevermind2
    with dissolve

    ay "Oh, good...I was starting to worry that maybe you were...abducted or kidnapped or something."
    s "I don’t really think it would count as “kidnapping” if someone my age was taken, so abducted works fine here."

    scene nevermind3
    with dissolve

    ay "Right, yeah. I should have just followed my gut."
    s "So, you really weren’t joking about the sky."
    ay "Crazy, right? It’s been like this pretty much every night lately."
    ay "Do you know if this means anything for the weather? Like, is winter going to end early or something?"
    s "Nah. The world is just coming to an end."

    scene nevermind4
    with dissolve

    ay "Well, if that is the case, I’m glad that I get to share my final moments with you."
    s "If you’d have actually come to the slumber party thing, we could have all weathered the apocalypse together."
    ay "But, Sensei, I don’t want to be around anyone else right now."
    ay "I wanted to lure you all the way over here so I could adultnap you and hide you in a secret passage underneath my house and be together forever."
    s "Okay, well, this has been fun. But I’ve got to head out."

    scene nevermind5
    with dissolve

    ay "Oh, stop. You know I’m only kidding."
    ay "If that were ever going to happen, I’d abduct Ami, Maya, and Sana too so all of us could live happily ever after in my secret underground bunker."
    s "Sounds to me like it would get pretty cramped in there rather quickly."

    scene nevermind6
    with dissolve

    ay "Probably, yeah..."

    if bonus == True:
        ay "And that would make it kinda hard to have “private time” together, so...maybe I’ll have to have Geoffrey construct additional bunkers or something like that?"
    else:
        ay "Hey...are you forklift certified?"

    s "Ayane."

    scene nevermind3
    with dissolve

    ay "Yeah?"
    s "You didn’t invite me here for construction tips, did you?"
    ay "I did not."
    s "Then what’s going on?"
    s "This isn’t like you."

    if bonus == True:
        ay "I’m a [teenage]girl, Sensei. My body is changing. And along with it, my interests, desires, and even my personality."
    else:
        ay "You know nothing, Jon Snow."

    s "I find that hard to believe."
    ay "How come?"
    s "Because a good chunk of your personality is rooted in how much you love me."
    ay "I can promise you that at least that much will never change."
    s "I don’t want any of you to change, though."

    scene nevermind7
    with dissolve

    ay "Huh?"
    s "Why is it surprising that I preferred the version of you that wasn’t using excuses to get out of everything?"
    ay "It’s not! I just..."
    ay "My heart skips a beat every time you look at me and say something like that."
    ay "So hearing it will probably always make me gasp."

    scene nevermind3
    with dissolve

    ay "I hope that’s okay."
    s "It’s fine."
    s "Now, tell me what this is really all about."
    ay "Aww, come on. Can’t I use stall tactics a little more before we start getting to the serious stuff?"
    s "Nope. I {s}flew{/s} walked all the way here for you and I expect there to be some actual substance tonight."

    scene nevermind8
    with dissolve

    ay "Even if it’s something you really don’t want to hear?"

    if bonus == True:
        s "If you pull the pregnancy trick on me again, I swear-"
        ay "Are you really that afraid of becoming a daddy?"
    else:
        s "If this is about bone necklaces, I swear-"
        ay "It is not, but would it really be bad if-"

    s "Yes. Now tell me what this is really about."
    ay "…"
    s "…"

    "I want to say something about how the wind assaults us on the rooftop-"
    "But it feels as if we’re already in space."
    "There is no wind anywhere. "
    "There is no sound anywhere."
    "There is nothing."

    ay "Can I have a hug?"
    s "…"
    s "You made me walk all the way over here for a hug?"
    ay "Do you have any idea how much I love your hugs?"
    s "Ugh, fine. Come here."

    scene nevermind9
    with dissolve

    ay "Heheh~ Yes, [ayanemaster]."

    scene black
    with dissolve2

    "I’ve noticed something about Ayane over the time we’ve spent together in this strange excuse for a world."
    "Nearly every time she wraps her arms around me, there’s always an extravagant build-up first."
    "Kind of like a dog who is obedient enough to stay off of the couch until invited onto it-"
    "But once it is, it leaps nearly ten feet in the air and crashes into the cushions with more vigor than a male rabbit during mating season."
    "I guess dogs can’t exactly jump ten feet, though."
    "That sounds more like a demon."
    "Either way, there’s no vigor at all in tonight’s embrace."
    "It’s more like wrapping my arms around a dying family pet that I’ll never get to hold again."
    "Its legs are shaking as it struggles to even stand up."
    "They snap- and all of the weight is forced onto me."
    "Everything always comes back to me."
    "I can’t stretch my arms around all of it."
    "………"
    "……"
    "…"

    scene nevermind10
    with dissolve

    ay "You’re warm."
    s "This is what you missed out on that night we went to the park with Sana."
    ay "That was really hard, you know?"
    ay "If it were up to me, we’d be like this every hour of every day."
    s "That would make it very hard to perform necessary daily functions."

    scene nevermind11
    with dissolve

    if bonus == True:
        ay "But you wouldn’t have to jerk off anymore."
        s "Also true."
        s "I guess there are pros and cons to everything."

    ay "I saw you once, you know."
    s "Saw me what?"

    if bonus == True:
        ay "Jerking off."
        s "What? When?"
        ay "A really long time ago. "
        ay "Ami and I both saw it because we went to your room to see if you’d make us a snack and then...surprise. Penis."
        s "Was that before or after I apparently caught you two kissing one another?"
    else:
        ay "Dancing."
        s "Was that before or after the world destroying robot thing?"

    scene nevermind12
    with dissolve

    ay "That..."
    ay "..."
    ay "That never actually...happened."
    ay "Well, apart from the Christmas party. But I was kinda just scrambling to keep things under wraps there and..."
    s "You made that up?"

    scene nevermind13
    with dissolve

    ay "…"
    ay "Yeah."
    s "Why?"
    ay "…"
    ay "You know..."
    ay "I’ve been getting the feeling lately that you’re kind of just...going along with a lot of stuff."
    ay "Like there’s part of you that’s just not really...there anymore."
    ay "And I’ve heard you joking about your memories in the past, but like...then I started wondering if it really {i}was{/i} a joke."
    ay "What if parts of your memories really {i}were{/i} gone and...weren’t coming back?"
    ay "What would that mean for me?"
    ay "When did the new memories start being recorded?"
    ay "Was it after I’d already fallen in love with you?"
    ay "And if so, how would that make me look?"
    ay "Needy?"
    ay "Desperate?"
    ay "Naive?"

    scene nevermind14
    with dissolve

    ay "So...yeah..."
    ay "I thought that maybe...if I could catch you going along with things that didn’t really happen...I’d know for sure."
    s "Ayane-"
    ay "It’s okay that you’re hiding things from me. I don’t need to know about them."
    ay "I just wanted to know how much of what we have is real and...how much I may have lost."
    s "You haven’t {i}lost{/i} anything."

    if bonus == True:
        s "Everything that’s happened since the moment we became...intimate has been all me."
    else:
        s "Everything that’s happened since the moment we started hugging each other has been not only consensual, but entirely of my own choosing. I regret nothing and you have no reason to believe any of it is not real."

    scene nevermind15
    with dissolve

    ay "Right, but..."
    ay "What about the moments that led us there?"
    ay "All of the...horrible feelings I felt...and all of the good things that came from meeting you and Ami..."
    s "They’ll come back."

    "Maybe."

    ay "And if they don’t?"
    s "If they don’t, they don’t."
    s "There’s nothing we can do about it."
    s "But I’m here now, so just focus on that."
    ay "…"
    s "…"

    scene nevermind16
    with dissolve

    ay "Okay."
    ay "There’s still...a lot more I want to talk about, though."
    ay "Well, I don’t {i}want{/i} to talk about it, but I kind of have to if things are ever going to change."
    s "Why do they have to change?"
    ay "Everything has to change. That’s how the world works."
    s "Change is so exhausting, though..."

    scene nevermind17
    with dissolve

    ay "I know it is...I agree..."
    ay "But...there is one change we kind of...have to acknowledge..."
    s "And what is that?"
    ay "Sensei..."
    ay "You know that Ami is...actually in love with you, right?"
    ay "Like, not just as a [niece]. As a girl."

    if bonus == True:
        s "…"
    else:
        s "Do accountants not count as girls?"

    ay "I...don’t even know why I’m asking. Of course you know. It would be impossible not to."
    ay "But, like...Ami is my best friend."
    ay "And...I also love you..."
    ay "And I’m fine with keeping that hidden from everyone else, but..."
    ay "I kind of...want to at least tell her that it's not really one-sided anymore."
    s "That’s a bad idea, Ayane."
    ay "Why?"
    s "Because Ami would literally kill you."
    ay "She wouldn’t {i}kill{/i} me."
    s "I wouldn’t be so sure of that."

    scene nevermind18
    with dissolve

    ay "I would."
    ay "We might get into little arguments and stuff, but she’s pretty much my sister."
    ay "And since I obviously know everything that’s going on with her, she should probably know everything that’s going on with me as well."
    ay "And that everything is you."
    s "This is a horrible idea, Ayane."
    ay "I’m sure it will be really awkward and confusing at first..."
    ay "But, in the long run, I think this is best for everyone."
    ay "I...don’t know if anything has actually {i}happened{/i} between you and Ami since you’re always so closed off and stuff...but I do know what’s happening on her side of things."
    ay "She’s getting very anxious and nervous with all of these new girls showing up. "
    ay "And I’m sure that the two of us getting closer every day doesn’t help that at all."

    if bonus == True:
        s "And you think her knowing that I’m fucking her best friend will?"

        scene nevermind19
        with dissolve

        ay "That’s not the part that’s important, Sensei. The important part is that our feelings for each other are specifically {i}more{/i} than just sex."
        ay "That’s what Ami’s afraid of- you leaving her."
        ay "It’s the same exact fear that I have."
        ay "Just...my fear has been getting a lot stronger lately."
        s "Because of Ami?"

        scene nevermind10
        with dissolve

        ay "…"
        ay "Because of a few things."
    else:
        s "She is just an accountant. Stop being dramatic."

    scene black
    with dissolve2

    "We break apart."
    "Not emotionally, but physically."
    "Emotionally, it’s hard to say if a strong enough bond has ever formed on my end at all."
    "Let’s, in typical “me” fashion, turn this into a strange anecdotal metaphor."
    "I am a half-finished statue based on the outer layer of a real human being."
    "The process of turning me into stone is my relationship with Ayane."
    "I am poised and ready for my body to be covered in a thick coat of cement."
    "But the artists have only made it up to my knees before running out of whatever cement is made of."
    "Is cement even made of anything?"
    "Is it just cement?"
    "I don’t know."
    "I once again distract myself from anything but the topic at hand because I am afraid of thinking."
    "I am afraid of all things."
    "I am afraid of nothing."
    "I grow wings and fly away."

    scene nevermind2
    with dissolve2

    ay "So...umm...remember how I said I might need some more attention soon?"
    s "Does this meeting not qualify as that? Because you’re already kind of acting out of the ordinary here."
    ay "No. I’m talking about the...you leaving me thing."
    s "If you’re really intending to break the silence of our relationship to Ami, we should worry more about you leaving {i}me{/i}."
    ay "The things I mentioned don’t all involve Ami, Sensei."
    s "Well, can we at least fully address that part first? Because I still don’t like the idea of you coming out about this."

    scene nevermind8
    with dissolve

    ay "Because you’re embarrassed of me?"
    s "What? No."
    ay "Because you don’t want to hurt Ami’s feelings?"
    s "That’s closer, but still...no."
    ay "Because you’re worried she’ll tell other people?"
    s "Ayane-"
    ay "Because you’re worried she’ll tell Maya?"
    s "What would Maya have to do with this?"
    ay "Remember the other day when I asked you about who you’d choose if all twenty of us were lined up in class and you were forced to pick one?"
    s "I remember it being a flawed hypothetical scenario based on several of the students’ attendance, but yes."
    ay "If that were true, and all of us really {i}were{/i} in the same room, I think your choice might actually surprise you."
    ay "That’s all I’m saying."
    s "You think I’d choose Maya in that situation?"
    ay "I just think you look a little differently at her than you do anyone else."
    ay "I don’t know what it means, but I’d be lying if I said it doesn’t bother me."
    s "And that’s another one of your worries?"
    ay "That’s another one of my worries."
    ay "I have a lot all of a sudden."
    ay "I’m even here actually talking to you about my feelings for once because I’m so overwhelmed right now that I think I might explode."
    s "You should have come to my house tonight."

    scene nevermind6
    with dissolve

    ay "I should have come to your house tonight."
    ay "I don’t belong up here."
    ay "I belong with everyone else...being loud and overly-expressive about the things I love most."

    scene nevermind2
    with dissolve

    ay "But, most of all...with you."
    ay "If the world really {i}was{/i} ending tonight, I’d be scared. But, in a way, I’d kind of also be a little happy."
    ay "Maybe the world ending would just mean that it starts all over again?"
    ay "A fresh start doesn't sound bad, does it?"
    ay "You'd have some of your memories back."
    ay "I'd have both of my parents."
    ay "And then one day, I’d bump into Ami and meet you."
    ay "And I’d fall in love all over again."

    scene nevermind5
    with dissolve

    if bonus == True:
        ay "And then I’d catch you jerking off again."
    else:
        ay "And then you would finally make a bone necklace with me."

    s "Why does that part have to come up now in the middle of a big, emotional moment?"

    scene nevermind2
    with dissolve

    ay "Neither of us are good at big, emotional moments."
    ay "Maybe I learned it from you, but I think it’s easier to just move onto things that aren’t painful to talk about most of the time."
    ay "Tonight is just...a special exception."
    s "I just want to know if there’s anything that can be done to make you-"

    scene nevermind3
    with dissolve

    ay "Ayane again?"
    s "…"
    s "Yeah."
    ay "I see, I see."
    ay "All you really have to do is love me."
    s "I can do that much."
    ay "And let me share those feelings with anyone that I think it’s safe to share them with."
    s "That one’s a little further off, but I could probably be swayed with a few more conversations."
    ay "And accept that sometimes, there will be parts of me you wish didn’t exist."
    s "Fine. Whatever."
    ay "And that sometimes, those parts might be hard to say out loud...so I’ll be forced to drop hint after hint after hint, hoping that you manage to understand what I’m trying to tell you."
    s "I get it. Yeah."
    ay "Do you, though?"
    s "Of course I do."
    ay "…"
    ay "{i}Do you, though?{/i}"
    s "Ayane...come on."

    scene nevermind9
    with dissolve

    ay "Heheheh~ "
    ay "It’s fine. It’s fine."
    ay "I kind of expected things to play out like this anyway."
    ay "It’s actually a pretty amazing quality being able to just effortlessly ignore the things you don’t want to acknowledge or hear."
    ay "I always have so much trouble with that."
    ay "Maybe one day, far off in the future, you can teach me how to be as intentionally dense as you."
    s "Are we done talking about serious stuff and just moving onto “insult Sensei time?”"
    ay "Is {i}that{/i} what time it is?"
    s "If you call it teacher time again, I’m leaving."
    ay "Already? But teacher time isn’t over yet."

    scene black
    with dissolve

    s "Okay. Goodnight, Ayane."

    "Sensing that things are going to end here within a matter of moments, I turn around and-"

    ay "Wait!"

    scene nevermind20
    with dissolve2

    s "What is it?"
    ay "I don’t want you to leave yet."
    s "Then come back with me."

    scene nevermind21
    with dissolve

    ay "I...don’t want to do that either."
    ay "I mean, I do..."
    ay "But if I come back to your house, I’ll wind up telling Ami about us...and you asked for at least a few more conversations to be persuaded."
    s "I can’t just spend the entire night here, though."
    s "There are other people waiting for me."

    scene nevermind22
    with dissolve

    ay "There are always other people waiting for you..."
    ay "And I’m okay with that. That’s just...the effect you have, I guess."
    ay "It happened to me so...of course it would happen to everyone else."
    ay "But right now, I...really need you to listen to me."
    ay "Sensei.."
    ay "Something..."
    ay "Something happened and..."
    ay "And it's something I really need your help with and..."
    s "…"
    ay "…"
    s "…"
    ay "…"
    s "I’m listening, Ayane."
    s "Whatever it is, I’m sure it won’t change anything between us."
    s "So, if that’s what you’re worried about-"

    scene nevermind23
    with dissolve

    ay "Nevermind."
    s "...What?"
    ay "Nevermind."
    ay "Don’t worry about it."
    ay "I can tell you some other time."
    s "Just tell me now. If there’s more to the reason you called me out here-"

    scene nevermind24
    with dissolve

    ay "I just wanted to look at the sky with you."
    ay "That’s all."
    ay "I’ll stop telling everyone I’m not feeling well for real this time."
    ay "And I’ll...keep doing my best."
    ay "Just...try to be there for me if I need you..."

    scene nevermind25
    with dissolve2

    ay "Okay?"
    s "…"
    ay "I love you..."
    ay "So...so much..."
    s "…"
    s "Ayane-"
    ay "I’ll head home in a little while. I promise."
    ay "I just want to be alone for a few minutes."
    s "…"
    s "Okay."
    s "I love you too."

    scene black
    with dissolve2

    "My wings retreat back into my flesh and I’m forced to walk down several flights of stairs with the image of a crying blonde girl etched into my mind."
    "I don’t know what it is Ayane was about to tell me at the end..."
    "But I’m sure that it will come up again in due time."
    "Either that or I’m just once again being “intentionally dense” or whatever it is she called me."
    "That doesn’t sound too far off."
    "I hope she’s okay, though."
    "I really do."
    "Just not enough to drop everything and be with her regardless of her plea for privacy."
    "Perhaps one day I’ll get there."
    "But for now-"

    s "…"

    "I slide my hands into my pockets for the millionth time and go back home."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanespecial1 = True
    stop music fadeout 10.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    jump thirdreset1

label ayanespecial2:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
s "Ehh, I’m fine standing here and watching. "
    s "I’ll view it as a sort of “Tojo Ramen on the go” special."

    scene mollyslumber18
    with dissolve

    t "It would be hard to profit off of such a venture."
    s "Well you’re free to move in and work in shifts with Ami to lighten a bit of the load on her."
    t "I can not abandon my father in his time of need."
    s "Oh, right. That’s a thing."
    t "He has been more active than normal lately."
    t "He’s still unable to get out of bed, but his smile has returned."
    t "If I were to leave him now to take up a job in an unknown man’s house, I imagine it would fade very quickly."
    s "I’m not “unknown.” I’m your teacher."
    t "That makes little difference to him. "
    t "He was kind enough to allow me out of the house after so many years. Asking him for more on top of that would make it seem like I am not grateful."
    s "You’re grateful to someone who kept you locked away for your entire life?"

    scene mollyslumber19
    with dissolve

    t "I am grateful to someone who taught me how to read and write."
    t "Who washed my hair when I was a child and bandaged my fingers when I cut myself in the kitchen."
    t "Who tenderly explained to me why our skin colors didn’t match and why people always looked surprised to find out I was his daughter."
    t "My father is a good man."
    t "I wish there were more people who would see him that way."

    "Tsuneyo pauses for a moment, likely waiting for me to say something."
    "Unfortunately, I don't have anything important or insightful to add, so I simply remain quiet and allow her to continue getting whatever point she's trying to make across."

    scene mollyslumber20
    with dissolve

    t "Sensei..."
    t "You love Ami, correct?"
    s "I mean...she {i}is{/i} my [niece]."
    t "If she was in danger and it was within your power to protect her...but it meant confining her to this very house...would you do it?"
    s "In danger from what exactly?"
    t "What is something you fear?"
    s "I don’t know...just make something up for me."
    t "Fine."
    t "Let’s say it’s spiders."
    t "An endless supply of them."
    t "Spiders that she’s highly allergic to. Ones that will kill her if they so much as sink their fangs into the pale skin of her beautiful legs."
    s "You really like her legs, don’t you?"
    t "They remind me of these carrots. Tender and soft."
    s "Are they...still good? Because you can throw them away if they’re not."
    t "They will suffice."
    t "But...if you could save your [niece] and preserve your love for her by confining her to this house, what would you do?"
    s "I..."
    s "I don’t know. That’s kind of a weird question."

    scene mollyslumber21
    with dissolve

    t "It is, isn’t it?"
    t "If I were Ami, I’d want to be saved."
    t "There’s nothing more important than preserving one’s own life."
    s "Not even noodles?"
    t "There is {i}almost{/i} nothing more important than preserving one’s own life."
    t "If protecting the person you love means sacrificing their freedom, all you need to do is teach them to feel free in captivity."
    t "I could have lived my entire life in Tojo Ramen without the desire to leave."

    scene mollyslumber22
    with dissolve

    t "But..."
    t "Sometimes, I’m glad I was able to."
    s "…"
    t "…"
    s "…"
    t "…"

    scene mollyslumber23
    with hpunch
    play music "phonering.mp3"

    s "Oh."
    t "Is that your ringtone?"
    s "What else would it be?"
    t "You have good taste in music. "
    s "That’s just-"
    s "You know what, nevermind. I’m gonna take this."
    s "I’ll be in the living room if you need anything."
    t "I understand. Though, I will be sad to hear the song end."
    s "I’m very sorry, Tsuneyo."

    scene black
    with dissolve
    stop music
    play sound "phonebeep.wav"

    s "Hello?"
    ay "Uhh..."
    ay "Hey."

    $ renpy.end_replay()
    $ day344 = True

    jump ayanespecial1
...
```