# Pseudonym (Wakana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Wakana love greater than or equal to 15

* Event [The Road to Recovery](./yumiyukispecial1.md) (Main) is completed)

* wakananumber equal to True (unknown variable)



## Next events

* [Main: No Strings Attached](./imanispecial1.md)

## Event properties

* Id: wakanadate15
* Group: Wakana
* Triggered by label: callwakanamorning
* Triggered by branch label: callmorning
* Triggered by path: callmorning->callwakanamorning->wakanadate15

## Official wiki page

[Pseudonym](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=wakanadate15&go=Go) for more details.

## Event code

File: (install folder)\game\WakanaEvents.rpy

Code:
```python
...
label wakanadate15:
    play sound "phonebeep.wav"

    "I tap on Wakana’s name in my phone and wait for her to answer-"
    "Because, despite everything about her appearance screaming “I am going to stay in bed for the rest of forever,” she’s one of the only people I know who seems to always be doing something around this time."
    "So, based on prior experience, it’s probably safe to assume she’s either getting extra work done at school or...watching over the archery club (Again, at school.)"
    "You know, she should probably just move closer to the school if she’s going to be spending practically all of her time there."

    play sound "phonebeep.wav"
    play music "wewereangels.mp3"

    w "Good morning, Arakawa. What do you want?"
    s "Just wanted to see what my favorite goth was up to."
    w "If that section of your rolodex is comprised of more than just one person, please forward me their contact details. Talking to you and Imani is tiring. I need more people interested in incense."
    s "There’s always Nodoka."
    w "I said incense, not {i}incest.{/i}"
    s "Sorry. Only one of those words is in my dictionary."
    w "Then I believe it may be time for an upgrade. Fortunately for you, I’m currently surrounded by around a hundred of them. "
    w "I’ll make sure to grab one on the way out so your wealth of knowledge can expand beyond the reach of whatever it is you do to your niece in your spare time."
    s "You too? I feel like I can’t talk to anyone nowadays without them suggesting something going on between Ami and me."
    w "And whose fault is that, Arakawa? "
    s "Hers. Also, why not try spending a little time away from school every once in a while?"
    s "I get that you’re an intellectual and that libraries are like candy stores for you, but it’s still way too early in the morning to be going over there if you don’t {i}have{/i} to."
    w "Are you done?"
    s "I think so."
    w "Good. Then I guess this is the part where I tell you {i}I am not at school, you incorrigible half-wit.{/i} I’m at the {i}public{/i} library. And you just lost your chance to obtain a new dictionary for free. I hope you’re happy."
    s "What are you doing at the library?"
    w "Fucking reading, Arakawa. Do you even understand how libraries work?"
    s "But why {i}there?{/i} It’s nowhere near your apartment."
    w "Hah...I’m doing research. And quite disheartened by the fact that you now know I am in a library and you refuse to hang up the phone."
    s "You haven’t hung up either. I just want to know-"
    w "If there’s something you want to know, you know where to find me. I don’t have time to “shoot the breeze” with you like this. I have work to do."
    s "Waka-"

    play sound "phonebeep.wav"

    s "...na."

    scene black
    with dissolve2

    "Wakana hangs up the phone and I...guess I’m heading over to the public library to continue the conversation."
    "Not that I expect it to be exciting when she’s apparently just “researching” things, but at least deciding on this path for the day is easier than trying to uncover another one."
    "I throw on my clothes and head over to the bus stop, patting myself on the back for deciding to visit a real adult woman."
    "A real adult woman with no inclination to have sex with me, yes. But a real adult woman nonetheless."

    scene wakanalibrary1
    with dissolve2

    "It takes me a few minutes to find Wakana once I get to the library, but I manage to spot her during my second lap around the place in what should have {i}probably{/i} been the first section I checked."
    "I make my way through a narrow aisle walled by the names of dead poets and wind up in front of one still clinging to life by a few black threads dangling off the fingers of her gloves."

    w "Interesting. I didn’t think you were actually going to show up."
    s "We weren’t done “shooting the breeze” yet."
    w "Unfortunately for you, I don’t have time to do much “shooting” at all. This is proving to be a bit more difficult than I expected."
    s "What are you doing exactly? More...research or whatever?"

    scene wakanalibrary2
    with dissolve

    w "That is correct. Though, I suppose it’s less general research and more...brushing up on things I have forgotten."
    s "Care to explain?"

    scene wakanalibrary3
    with dissolve

    w "Not really, no."
    s "Wakana-"
    w "Fine. If you {i}must{/i} know, I have taken it upon myself to take on {i}even more{/i} work- as the work I had already was apparently not enough for my masochistic brain."
    s "I thought Osako was the masochist?"
    w "Physically, yes. But the amount of pain I insist on putting myself through makes me feel as if I am some sort of mental masochist."
    s "And this additional work is?"

    scene wakanalibrary4
    with dissolve

    w "I thought it might be fun to start an annual poetry contest for the girls at our school...as several of them have expressed interest in that sort of thing."
    w "But, me being me, simply agreeing to judge their work was not enough. "
    w "And so I find myself here, attempting to decipher several of the submitted works while brushing up on the fundamentals of what I’m trusted to be educating our students on."
    w "I’d say something along the lines of, “The life of a teacher, right?” But I know that you wouldn’t be able to relate and I don’t want to confuse that tiny, pea-shaped brain of yours."
    s "Interesting. I guess if anyone is going to judge something like that, it should be you."

    scene wakanalibrary5
    with dissolve

    w "I’d say you’re just as qualified, but I suppose actually {i}caring{/i} about the assignment is important too."
    s "Is there some sort of theme everyone has to use?"

    scene wakanalibrary6
    with dissolve

    w "Why? Are you thinking of entering?"
    s "Absolutely not. Just a little curious, that’s all."
    w "Worried you’ll lose to a bunch of teenagers? "
    s "You got me. That’s exactly it."

    scene wakanalibrary7
    with dissolve

    w "The theme is Kumon-mi. Though, I’d implore you to use a pseudonym if you actually intend to submit anything."
    w "How that would work if you actually {i}won,{/i} I have no clue. But I suppose that’s a bridge we don’t have to worry about crossing just yet."
    s "Would you actually let me enter? Doesn’t that seem a little unfair?"
    w "Perhaps. But I am rather curious about what sort of poem {i}you’d{/i} be able to write, Arakawa. "
    s "I doubt it would be anything good. There’s not much I really have to say about Kumon-mi other than it’s been really fucking hot lately."
    w "Several of your students seem to have quite a bit to say, on the other hand. I’ve gotten more submissions from your class than my own, and I even offered extra credit for writing something."
    s "From my class? Who?"

    scene wakanalibrary6
    with dissolve

    w "Would you like to read them together? You can...help me {i}judge{/i} them."
    s "The way you said “judge” there makes me worry they aren’t going to be any good."
    w "I wouldn’t worry too much. But I suppose I’ll let you get the final say. "

    scene black
    with dissolve2

    "Wakana bends down and removes a notebook from a large, purple bag. "
    "For anyone else, I’d use this opportunity to try and look up their skirt, but...yeah. "
    "Not really possible when the girl I’m with insists on wearing a dress that reaches the floor on a day where you could cook an {b}EGG{/b} by just cracking it open on the pavement."

    play sound "static.mp3"
    scene tree3 with flash
    scene wakanalibrary8 with flash
    stop sound

    w "So far, I’ve received submissions from a total of four of your girls. Though I believe there may be several others still working on theirs."
    w "It’s unfortunate that Miyamura won’t be participating. I feel like she’d be good at this. "
    s "She seems like more of an intellectual than an artist to me."
    w "Fair point. What we do have so far isn’t all that bad, however. Well, with the exception of one poem that I believe was created just to irritate me."
    s "Why? Does it talk about how life is awesome and totally worth living?"
    w "No. But it does mention an ungodly desire to strip the clothes from my body and “taste every inch of me,” but it’s disguised as a poem about dragonfruit. "
    w "I’d actually be quite impressed if I wasn’t so appalled by the subject matter- which has absolutely {i}nothing{/i} to do with Kumon-mi, by the way."
    s "Nodoka?"
    w "Who else would write a poem about tasting every inch of me?"
    s "Honestly? Probably a few more of my girls."

    scene wakanalibrary9
    with dissolve

    w "Really? Huh."
    w "And here I was beginning to think I had already lost my girlish charm."
    s "I’m not sure if your “girlish charm” is what they admire."

    scene wakanalibrary8
    with dissolve

    w "Regardless, that was Nagasawa’s disqualified submission. But the three that remain are much better. "
    w "This one comes from...Fukuyama."
    w "{i}The town that I grew up in;\nWhere I still grow today.{/i}"
    w "{i}Where skies are blue and grass is green and everything’s okay.{/i}"
    w "{i}The town where all my friends live;\nAnd where I fell in love.{/i}"
    w "{i}It may not be exciting, but it’s the only town I love.{/i}"
    s "She rhymed “love” with “love.”"
    w "She rhymed “love” with “love...”"
    w "And while that’s not unheard of and {i}could{/i} be intentional, I’m almost certain it was an accident and that she’s going to realize her mistake and try to correct it."
    w "Unfortunately, the rules state that as soon as something is submitted, you can’t get it back."
    s "Who’s next? There are two more, right?"
    w "Up next is...oh. The one I tried to pawn off on you only to find that she’s been “in love” with you since she was a child- Nakayama. How fun."
    w "{i}No blindeyes bloom on paths I walk, but I found a shepherd’s purse;{/i}"
    w "{i}With pockets full of buttercups, I returned it to the earth.{/i}"
    w "{i}Now in its place, a pasture- cross the homes of hyacinth.{/i}"
    w "{i}Near a suckling clover fountain and its bitter orange drip.{/i}"
    s "That one doesn’t seem to have anything to do with Kumon-mi either."

    scene wakanalibrary9
    with dissolve

    w "Ah, but that’s where you’re wrong."
    w "Nakayama comes from the old district, doesn’t she?"
    s "She does, but I don’t really understand how that’s relevant here."
    w "It’s a poem about the Hamori River...and all of the flowers that bloom there."
    w "I needed to do a little research to confirm, but I thought I understood it after my first read as Osako and I have walked along that path before. It’s beautiful."

    scene wakanalibrary10
    with dissolve

    w "Or {i}was.{/i} I hear that area’s all but abandoned now. Shame."
    w "It used to be so lively there."
    s "Huh..."
    s "I didn’t realize Noriko could write like that."

    scene wakanalibrary11
    with dissolve

    w "I agree. Her submission is probably my favorite of what I’ve received so far. But the biggest surprise of all is this next one."
    w "From Ami Arakawa..."
    w "{i}Summer. Winter. Paradox. No autumn, nor a spring;{/i}"
    w "{i}At night, I watch the sakura peel themselves off thick, red strings.{/i}"
    w "{i}Why can I see what isn’t there? Why can’t I feel the sting?{/i}"
    w "{i}Of the town that took the world away and the evil song it sings.{/i}"
    s "..."
    w "I don’t believe I’ve grasped the full meaning of the poem yet, but this...longing for pain and how it ties in with our missing seasons..."
    w "It reminds me of another poet I used to follow when I was younger."
    w "One that, if what I’ve heard is true...was also born and raised here."
    s "..."
    w "It’s impossible to tell for sure, though, as she always used a pseudonym."
    w "The girl who cannot breathe..."
    w "Infamous for her self-destructive thoughts on what it means to {i}be{/i} and the use of themes that most others would-"

    stop music
    play sound "thump.mp3"
    scene wakanalibrary12
    with hpunch

    "{i}Uh-oh!{/i}"
    "{i}It looks like you might have remembered something!{/i}"
    "{i}Remembering things is bad! Remember to remember that!{/i}"
    "{i}If you remember too much, you won’t be able to put your meat stick inside of tight meat holes anymore.{/i}"
    "{i}And that’s the point! Remember? Remember? Remember?{/i}"
    "{i}This is all just a game! It’s all part of a game!{/i}"
    "{i}It’s not real at all! Nothing is real! Nothing is real!{/i}"

    scene black

    "but if that’s true, why is everything so much bigger than you?"

    play sound "static.mp3"
    scene wakanalibrary12 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    w "Ara...kawa?..."
    s "Let’s get out of here."
    w "What?..."
    s "You. Me. Let’s leave."
    s "Do something else."
    s "Something better than this."
    s "Bigger."
    s "Let’s leave."
    w "Arakawa..."
    w "Your eyes..."
    s "Don’t look at me."

    scene wakanalibrary13
    with dissolve

    w "You’re making that quite hard with how close you’ve decided to come all of a sudden..."
    w "I’m flattered, really. Though, I’m not quite sure this is the type of relationship where you’re allowed to pin me against the wall and tell me to “get out of here” with you."
    w "Let alone in broad daylight...in the middle of a public library."

    scene wakanalibrary14
    with dissolve

    libp "Um...Miss, are you okay? Do you need me to...call for help?"
    w "Just a minor lover’s quarrel. Apologies for the commotion."
    libp "Oh...Okay..."
    libp "Well...uhh...I guess let me know if you need anything?..."
    w "Understood. Thank you very much."
    s "..."

    scene wakanalibrary15
    with dissolve

    w "..."
    s "..."
    w "..."
    s "..."
    w "..."
    s "..."
    w "If you have something to say, say it. This isn’t exactly a comfortable position for me."
    s "I can make it more comfortable if you want."
    w "Oh?"
    w "Is that what we’d do if I left with you?"
    s "..."
    w "Do you want to have sex with me, Arakawa?"
    w "Is {i}that{/i} why you’re cornering me like this?"
    s "..."
    w "Or is there perhaps another reason?"
    w "One you’re not telling me about, maybe?"
    s "You-"
    w "If you expect me to be afraid of you, it’s not going to happen. You look fucking pathetic right now."
    s "Don’t..."
    s "Don’t talk..."
    s "About..."
    s "..."
    w "Don’t talk about what? I don’t know what to do if-"

    scene wakanalibrary16
    with dissolve

    w "Wait..."
    w "Arakawa, what was the last thing I said before you decided to be a big, scary man and pin me to the wall?"
    s "..."
    w "Tell me."
    s "..."
    w "You can’t...can you?"
    w "You know-"
    s "I don’t know anything."
    w "Your eyes say otherwise."
    s "I told you to stop looking at them."

    scene wakanalibrary17
    with dissolve

    w "Fine. But if you seize this opportunity to stick your tongue down my throat, I have a hard time seeing how this friendship is going to work out."
    w "You can stay like this for as long as you need to...until you start to collect yourself, but..."

    scene wakanalibrary18
    with dissolve

    w "Just watch your fucking step, okay?"
    w "This little...{i}show{/i} you’re putting on right now? Not a fan."
    w "I doubt my {i}girlfriend{/i} would be much of a fan either."
    s "..."
    w "..."
    s "..."
    w "..."
    s "..."
    w "..."
    w "Arakawa..."
    s "What?..."

    scene wakanalibrary19
    with dissolve

    w "Just thought I’d say..."
    w "You’re a lot uglier up close."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "{i}The rest of the day disappears once you let her go...along with the three poems and the words uttered thereafter.{/i}"
    "{i}But you know they’re still in there somewhere.{/i}"
    "{i}Hiding somewhere you can’t see.{/i}"
    "{i}Waiting for the chance to suffocate you.{/i}"
    "{b}{i}You try to masturbate when you get into bed, but it doesn’t get hard.{/i}{/b}"

    $ renpy.end_replay()
    $ wakanadate15 = True

    "{i}Wakana’s affection does not rise.{/i}"
    "{i}But she saw who you really are today.{/i}"

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon

label wakanaspecial15:
...
```

## Code that triggers this event

File: (install folder)\game\WakanaEvents.rpy

Code:
```python
...
label callwakanamorning:
    if wakanadate1 == False:
        jump wakanadate1
    if secondbeach18 == True and christmastwo20 == False:
        "I should probably give Wakana a little space for now."
        jump callmorning
    if wakana_love >= 15 and yumiyukispecial1 == True and wakanadate15 == False:
        jump wakanadate15
...
```