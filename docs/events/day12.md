# Mitochondria (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 12



## Next events

None

## Event properties

* Id: day12
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day12

## Official wiki page

[Mitochondria](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day12&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day12:
    scene hall_noon
    with fade

    play music "10c.mp3" fadein 3.0

    "And so another day passes by without anything interesting happening."
    "You'd think that being reincarnated into a world where the only people I have to talk to are teenage girls would be a little more...I don't know, fun?"
    "But apparently, this world is going to be just as boring as the last."
    "Not like I {i}remember{/i} anything about the last, but..."
    "You get the point."
    "Originally, I was planning on getting some of my mandatory {i}counseling{/i} hours out of the way after school but, at the behest of Makoto, it seems everyone has been forced into studying instead of going home. "
    "As such, I am currently on my way to the library to personally assist her in tutoring the one girl who needs it more than anyone- Miku."
    "With standardized tests looming on the horizon and the future of the soccer team's ace hanging in the balance, it falls on one man (Me) to make sure everything turns out okay."
    "Thankfully, I have a foolproof strategy when it comes to situations as dire as this."

    scene libstudy1
    with fade

    mak "...and that’s why it’s called “pi.”"
    mi "I somehow feel even more lost now."

    "And that strategy is letting Makoto do everything while I sit back and watch."

    s "Hey, you two."

    scene libstudy2
    with dissolve

    mak "Oh, Sensei! Great timing!"
    mak "I was just telling Miku that “pi” is only called “pi” because it’s named after the Greek word ‘perimitros’ which translates to ‘perimeter.’"
    s "Awesome."
    s "And how are you holding up, Miku?"

    scene libstudy3
    with dissolve

    mi "I {i}thought{/i} I was doin’ okay! But then Makoto started sayin' all this stuff about pi and now I'm just hungry!"
    s "Just eat Makoto. She's rich in nutrients."

    scene libstudy4
    with dissolve

    mak "She is?!"
    mi "Hmm...You think so? Seems kinda {i}lean{/i} to me. Could probably do with a little more meat on her bones."
    mi "'Sides, Makoto uses coconut shampoo and I don't even like coconuts. I say we all just go get pie instead."
    mak "Can you do something about this before we start getting even {i}more{/i} sidetracked? There's no time to eat right now!"
    s "Don't worry, Makoto. I like coconuts and am not opposed to eating you."

    scene libstudy5
    with dissolve

    mak "Okay, ignore him. We have things to learn."
    s "Come on, relax. A minute or two of joking around won't kill you, will it?"

    scene libstudy6
    with dissolve

    mak "Sensei, it’s absolutely imperative that we teach Miku everything her brain can handle before the standardized tests begin."
    mi "Don't mean to interrupt, Makoto...but ya might be overestimatin' just how much my brain can handle."
    mi "I've been at my limit for a little while already..."
    s "Alternatively, what if we just...{i}don't{/i} do that?"
    mi "I think we should listen to the teacher, Makoto. He knows what he's doin'."
    mak "We can't just give up before we've even started, Sensei. Do you have any idea how horrible Miku is when it comes to science?"
    s "Well, which science are we talking about? Because some science is just flat out-"
    mak "Biology."
    s "Nevermind. It is absolutely imperative that we teach Miku about this subject."

    scene libstudy7
    with dissolve

    mi "You traitor! What happened to bein' on my side?!"
    mi "We were supposed to eat pie together! It wasn't meant to be like this!"
    s "Some things are just more important than pie, Miku."
    s "So, what are you struggling with when it comes to biology? The reproductive system? Mating habits?"

    scene libstudy8
    with dissolve

    mi "Umm..."
    mi "Well...actually..."
    mi "I was kinda hopin' that..."
    mi "Maybe...you could teach me a little about..."

    scene libstudy9
    with dissolve

    mi "Mitochondria?..."
    s "..."

    "Being a teacher sucks."

    s "Miku, why are you blushing? I could have sworn this conversation was going in a different direction."
    mi "Obviously cause I'm embarrassed about bein' all dumb and stuff."
    mi "Sensei...I'm really countin' on ya here."
    mi "Teach me everything there is to know about mitochondria."
    s "..."
    mi "..."
    mak "..."
    mak "Should I volunteer?"
    s "That would probably be for the best, yeah."

    scene libstudy10
    with dissolve

    mak "Ugh...fine."
    mak "Miku, listen closely. Because if I quiz you on this after I'm done speaking and you get all my questions right, we can go get pie."
    mak "But after that, it's right back to studying. Got it?"
    mi "Study now, pie later. Got it."
    mak "So, the mitochondria is a double-membrane-bound organelle found in eukaryotic organisms."
    mak "It aids in the biochemical process of energy production and respiration."
    s "Well said, Makoto. That sounds like something straight out of an Internet definition."
    mi "Wait...so are you sayin' this mitochondria things helps plants breathe and stuff?"
    mak "Not just plants, but animals and people as well."
    mak "Eukaryotic organisms contain cells with enclosed nuclei, so that means pretty much everything apart from bacteria and algae."
    mi "And, umm...what's a nuclei again?"
    mak "The plural form of nucleus. You remember what a nucleus is, right?"
    mi "Uhhhh...sure!"

    scene libstudy11
    with dissolve

    mak "Great! So, now that we’ve talked about {i}eukaryotic{/i} organisms, what comes next?"
    mi "Um...uhhh..."
    mi "{i}Unkaryotic{/i} organisms?"
    mak "Good guess, but no. What I’m talking about is-"
    s "Oh wow, would you look at the time?"
    s "I have suddenly become aware of a prior engagement. Farewell, students. Don't neglect your education."

    scene mitoredux1
    with fade

    mak "...and that’s why you need to- Wait, where did Sensei go?!"
    mi "Run, Sensei! Run! Save yourself!"

    "I believe I have about five seconds to get out of here before I am killed by the student council president."

    scene mitoredux2
    with dissolve

    c "Oh, look who it is! Sorry for not studying like Makoto asked us to. I just had to-"
    s "Shh. They’ll hear you."

    scene mitoredux3
    with dissolve

    c "Huh? Who will?"
    c "Are you being followed?"
    c "I have mace on my keychain. Do you need me to mace someone? Because I'll do it."
    s "I don't think that will be necessary. It's just Makoto I'm running from right now."
    c "Are you {i}sure{/i} you don't need the mace? Because Makoto can be pretty serious when it comes to studying and stuff."
    s "Is there any way you can save me {i}without{/i} macing her?"

    scene mitoredux4
    with dissolve

    c "{i}Without macing her...{/i}"
    c "Hmm..."
    s "Chika, we really don't have the time to-"

    scene mitoredux5
    with dissolve

    c "I've got it!"
    c "Come with me and don't ask any questions, okay?"

    scene black
    with dissolve2

    "Before I can respond, Chika grabs my hand and pulls me into a nearby room..."
    "........."
    "......"
    "..."

    scene mitoredux6
    with dissolve

    "She slams the door behind us, holding it closed so no one (At least no one weaker than her) will be able to come inside."
    "I'm a little surprised at how...assertive and daring this tactic is considering that if anyone saw us go in here together, it could start a whole slew of rumors."
    "But I'm not really about to argue with her logic right now as this is essentially a matter of life and death."

    c "Sorry if this makes you uncomfortable or whatever. But it's the best thing I could think of on short notice that didn't involve mace."

    if bonus == True:
        s "I am 99%% sure I am not allowed to be in here."
        c "I won't tell anyone if you don't. Besides, nobody ever comes here after school hours anyway."
    else:
        s "Please, take my lunch money and don't hurt me."

    c "Don't take that as a free pass to just come on in whenever you want, though. This is only okay because I'm here too."
    s "Does that really make it okay?"
    c "Hmm...I guess that depends on what happens next?"
    c "You wouldn't try to make a move on a girl who's in the process of saving your life, would you?"
    s "If anything, this feels like you making a move on me."

    scene mitoredux7
    with dissolve

    c "Wait, what? No. No, I was just-"
    c "It's not like that at all!"
    s "..."
    c "..."

    scene mitoredux8
    with dissolve

    c "Why are you just staying quiet?! It's really not like that!"
    c "I was trying to save you, remember?! {i}Save{/i} you!"
    s "..."
    c "Sensei!"

    scene black
    with dissolve2

    if bonus == True:
        "Chika and I hide out for a few more minutes before we decide it’s safe to leave."
        "Her face remains flushed the entire time."
    else:
        "Chika mugs me and gives me a swirly and I cry a lot."

    $ renpy.end_replay()
    $ chika_love += 1
    $ day12 = True
    stop music fadeout 5.0

    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschool

label day14:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

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
...
```