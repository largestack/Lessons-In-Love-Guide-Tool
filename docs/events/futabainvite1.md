# Sonnet 18 (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Futaba: Floral Aura](./futabainvite2.md)

## Event properties

* Id: futabainvite1
* Group: Futaba
* Triggered by label: futabainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->futabainvite->futabainvite1

## Official wiki page

[Sonnet 18](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabainvite1&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabainvite1:
    play sound "phonebeep.wav"

    "I tap on Futaba’s name in my phone and wait for her to answer."
    "This will be the first time I’ve ever tried inviting her over to the house and, if there’s anything I know about that girl by now, I’m pretty sure I’m about to give her a minor heart attack."

    if bonus == True:
        "But hey, if things are ever going to progress to the point where we can actually have sex, events like this are going to need to happen."
    else:
        "But hey, Futaba is part of my official hug club, so events like this are going to need to happen."

    "Plus, having to deal with a possessive and jealous redhead might be a good exercise in self-control and confidence for her."
    "All of us have something to gain out of this."
    "A notch in the belt for me, a new outlook on life for Futaba, and a new rival for Ami."
    "Everyone wins."
    "Except Ami, I guess."
    "But she loses virtually every time I invite someone new over."
    "Sorry, Ami."

    play sound "phonebeep.wav"

    f "Hello? [futabamaster]?"
    f "How are you doing?"
    s "I’m doing fine. Are you busy today?"
    f "Today? Umm...not really. Why?"
    s "I was wondering if you’d want to hang out at my place."
    f "Y-y-your...your house?!"
    f "But...it’s...so sudden! I mean...we haven’t even-"
    f "W-wait...this is...this is to study or something, right?"
    f "Yeah, of course it’s something like that."
    f "You live with Ami and have already...decided to not really {i}teach{/i} as much lately, so..."
    f "You probably just need someone to help her with English, right?"
    f "You definitely don’t want to just {i}hang out{/i} with me, hahahaha~"
    f "Right?..."
    s "I actually did, but the studying thing sounds like a good cover story."
    f "So...wait, what am I doing?"
    f "Do I need to bring my books?"
    s "Bring whatever you want. We’ll deal with it once you get there."
    f "Wait, [futabamaster]!"

    play sound "phonebeep.wav"

    "I hang up the phone and put it back into my pocket. "
    "I guess that call went more or less how I expected it to."

    scene black
    with dissolve
    stop music fadeout 10.0

    "All that matters is that Futaba agreed to show up. "
    "And it’s not like her coming over will be as rattling for Ami as someone like Chika since the two of them are already in a club together."
    "If anything, we can just fall back on the makeshift tutor idea Futaba was smart enough to come up with-"
    "Even if the manner in which she came up with it was the direct result of her poor confidence rearing its ugly head once more."
    "………"
    "……"
    "…"

    scene futabaamistudy1
    with dissolve
    play music "normalday.mp3" fadein 4.0

    f "Wow..."
    f "I can’t believe...I’m actually here..."
    f "I mean...I’ve stopped here once or twice before to lend Ami manga but...this feels so much different..."

    if bonus == True:
        s "I wonder if any of that has to do with how I’ve seen you naked and Ami hasn’t."
    else:
        s "I wonder if any of that has to do with how many times you and I have made card houses together."

    scene futabaamistudy2
    with dissolve

    if bonus == True:
        f "Umm...I’m sorry but, if anything, Ami has probably seen me without clothes on even more than you have..."
    else:
        f "Umm...I’m sorry but...Ami was my original card house partner long before you were, Sensei..."

    s "What?"
    s "Just what the hell is the relationship between you two?"
    f "We’re both girls and share the same locker room for PE..."

    if bonus == True:
        s "Oh right. The promised land that only I am unable to enter."
        f "R-Right..."
        f "But at this rate, you’ll probably find a way to get in eventually, so...yeah."
        s "One can only hope."

        scene futabaamistudy3
        with dissolve

        f "I’ll...put in a good word for you..."
        s "And I will continue to give you straight A’s in return."
        s "Let it be known that this is not a bribe and that I would have done that anyway."
        f "Of course you would have..."
    else:
        s "What the hell does that have to do with card houses?"

    scene futabaamistudy4
    with dissolve

    f "So, umm...I don’t know how serious you were about the studying thing so...I kind of just brought all of my books..."
    s "All of them? Aren’t there like, five?"
    f "There are a lot more than five books, [futabamaster]...and I’m pretty sure you know that."
    s "School has too many subjects."
    f "Yeah...I’m starting to see why you may have given up on teaching all of a sudden..."

    play sound "dooropen.mp3"
    scene futabaamistudy5
    with dissolve

    a "Oh, Futaba. What are you doing here?"
    a "Did I forget to give back some manga or something?"
    f "No...that’s not it."
    f "Sensei just thought it might be a good idea to have someone come and help you with...one of the more than five subjects at our[school]."

    scene futabaamistudy6
    with dissolve

    a "What? Why do you suddenly care about my education?"
    s "Because I am a good [uncle]."
    a "I thought you were gonna let me just steal all of the answers from you for the next couple years."
    s "For the rest of eternity, more likely."
    f "Uhh...[high_school] doesn’t last an eternity, Sensei..."
    s "Are you sure about that, Futaba?"
    f "...Yes?"

    scene futabaamistudy7
    with dissolve

    a "So, where did you want to start? There aren’t really any subjects I’m weak at, so pretty much anywhere would be fine."
    s "What is iambic pentameter, then? Go."

    scene futabaamistudy8
    with dissolve

    if bonus == True:
        a "Huh? No one my age would have any idea what that is."
    else:
        a "Huh? I'm an accountant, not an English major. Get off my back."

    s "Take a guess."
    a "I don’t know...some kind of medical thingy used to measure...blood?"
    s "That’s not even remotely close."
    f "I mean...some iambic pentameter is kind of like a heartbeat. So if you think of blood in that regard...it’s...almost a good guess?"

    scene futabaamistudy9
    with dissolve

    a "Why do you know that? And, better question, why does {i}Sensei{/i} know that?"
    a "He can’t even remember what days we’re supposed to take the garbage out. "
    a "I’ve had to start doing it since he always forgets."
    f "It...appears in a lot of Shakespeare’s work. And it’s easier for me to pay attention in class when we go over things I’m interested in."
    f "Well...when we {i}used to{/i} go over things, I guess..."
    a "Fine then...tell me more about this stupid pentagon thingy since I’m such an {i}idiot.{/i}"
    s "Pentameter."
    a "Shut up."
    f "It’s basically...a type of rhythm you can find in a poem."
    f "It’s a pattern of stressed and unstressed syllables that are measured out in fives."
    f "And some of the ones that directly alternate sound a lot like...heartbeats."
    f "Are you...familiar with Sonnet 18, Ami?"
    a "Uhh...I don’t think so..."
    a "I don’t need to learn the other seventeen first, do I? "

    scene futabaamistudy10
    with dissolve

    f "Hahah...of course not."
    f "Just...listen to me and see if you understand."

    scene futabaamistudy11
    with dissolve

    f "Shall {b}I{/b} com{b}pare{/b} thee {b}to{/b} a {b}su{/b}mmer’s {b}day{/b}?"
    f "Thou {b}art{/b} more {b}love{/b}ly {b}and{/b} more {b}tem{/b}per{b}ate{/b}-"
    f "Do you see what’s happening? How every other syllable is emphasized?"
    a "Yeah. It does sound kinda like a heartbeat when you do it like that."
    a "You remember all that off the top of your head, though?"

    scene futabaamistudy12
    with dissolve

    f "Mhm..."
    f "I have a lot of time to go over little things like that when I’m in the library. "
    f "And when you read something so many times, it starts to stick in your head."

    scene futabaamistudy13
    with dissolve

    f "Plus...that’s the sonnet Sensei used to teach me about the pentameter when I was struggling with it."

    "It’s good to see that whoever the old Sensei was had an appreciation for Shakespeare as well."
    "This is definitely a strange coincidence, though."
    "All I did was break out an advanced term that Ami wouldn’t know and the conversation quickly evolved into something of actual importance to Futaba."

    a "Really? All he ever taught me was how he likes his eggs cooked."
    s "Futaba is my new apprentice. You're in her hands from now on."
    s "Also, please don’t tell Makoto I said that. She’ll kill me."

    scene futabaamistudy14
    with dissolve

    f "Hahaha~ Of course, Sensei..."
    f "I’m kind of worried about what she’d do to me as well if she ever heard that."
    a "Hey...what did I tell you about using the M word in this house?"

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene futabaamistudy15
    with dissolve

    "Futaba, having just been declared my new apprentice, spends the evening alternating between tutoring Ami and trying to hold conversations with me."
    "It’s an incredibly normal feeling night, something I didn’t particularly expect when I decided I’d put the two of them in the same room."
    "Sure, they’re both members of the manga club and have spent many hours in the same room before-"
    "But I'm beginning to understand that some of the girls act differently when I’m around."
    "Just like how I act differently when I’m around some of them."
    "I’m glad this worked out, though."
    "Maybe Futaba can start coming here more often."

    f "Sensei, do you have any other good examples of iambic pentameter that I could give to Ami?"
    f "Things that would be easy for her to understand."
    a "I feel like I should be offended by that, but I still barely even understand what’s going on."
    s "Richard III...Winter of our discontent."

    scene futabaamistudy16
    with dissolve

    f "Ah! Another good one!"
    f "Listen closely, Ami. This one starts out like a song and then turns into a heartbeat."
    f "Think of the opening like a...short drumroll or something."
    f "{b}Now{/b} is the {b}win{/b}ter {b}of{/b} our {b}dis{/b}con{b}tent-{/b}"
    f "Made {b}glor{/b}ious {b}sum{/b}mer {b}by{/b} this {b}sun{/b} of {b}York{/b}."
    f "And {b}all{/b} the {b}clouds{/b} that {b}lour{/b}ed up{b}on{/b} our {b}house{/b}-"
    f "In {b}the{/b} deep {b}bo{/b}som {b}of{/b} the {b}o{/b}cean {b}bu{/b}ried."
    a "..."
    a "Yeah, I’m still confused. Maybe I’m just not good at poetry."
    f "There are very few people who are {i}good{/i} at poetry. But there are a lot of people who try to understand it."
    f "What I’m teaching you now is...less of a poetry lesson and more of a science lesson."
    f "It’s the science of what makes things sound the way they do. "
    f "Kind of like...how pop music is created for the sole purpose of getting stuck in your head."

    scene futabaamistudy18
    with dissolve

    a "Woah! I totally understand that part! "
    a "Sometimes, I’ll hear a song I don’t even know on the radio and it will get stuck in my head for pretty much the entire day. It’s crazy!"
    f "Exactly! Because it follows a pattern. Just like most of Shakespeare’s work does."
    a "That Shakespeare guy should have made a rap album. He sounds like he’d be really good at it if he stopped making up weird words all the time."

    scene futabaamistudy19
    with dissolve

    f "Well...umm...he’s...kind of responsible for a lot of the words that exist today, so..."
    f "If he stopped making them up it...probably wouldn’t have worked out as well for him..."
    a "Yeah, whatever. I still don’t really get it."

    scene futabaamistudy20
    with dissolve

    a "But it’s cool that you’re so smart when it comes to this kind of stuff, Futaba! I’m really impressed!"
    a "Sensei should just get rid of his current class-rep and give you the job instead."

    if bonus == True:
        a "At least I know you aren’t the type to perv out on him all the time."
    else:
        a "At least I know you won't hide soup cans everywhere like Makoto does."

    scene futabaamistudy21
    with dissolve

    f "Hahah...right..."
    a "Sensei, how does that sound?"
    s "It sounds like another thing that would get all of us killed if Makoto was here right now."
    a "Oh, stop. The only thing she’d defeat all of us in is like...a sudoku match or something."
    a "Futaba would be much better than her and we’re already friends."
    a "Don’t you want a class-rep who can help people actually learn instead of just yelling at them all the time?"
    a "Didn’t Futaba sound a lot like a teacher today?"
    s "Well, yeah...but-"
    f "I-I’m really only good at teaching subjects I like. Makoto’s a much better leader than I would ever be."
    f "So...I think she should still be the...important one."

    scene futabaamistudy22
    with dissolve

    a "Do you hear this, Sensei? Futaba is saying she isn’t important now!"
    a "Look what you’ve done!"
    f "I didn’t mean it like that..."
    f "I just think we should maybe...keep practicing instead of deciding who should replace Makoto..."

    scene black
    with dissolve2

    "We don’t hang out for much longer after that."
    "Ami gets up after expelling all of her learning-energy for the day and offers to make dinner for the three of us."
    "I guess Futaba feels like she’s overstayed her welcome as she denies the offer and decides to head home instead."
    "She texts me on her way back thanking me for inviting her over again and I contemplate whether or not I should apologize for just throwing her into the deep end with Ami."
    "I decide against it, though. "
    "I feel like this was a good first time for Futaba."
    "She didn’t have to deal with the nervousness that would be sure to come with us being alone in my room- and she even got to rant about one of the things she loves for a while."
    "All in all, I doubt today could have possibly gone any smoother."
    "I’ll have to invite her over again soon and see what happens next..."

    $ renpy.end_replay()
    $ futabainvite1 = True
    $ futaba_love += 3
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabainvite2:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabainvite:
    if futabainvite1 == False:
        jump futabainvite1
...
```