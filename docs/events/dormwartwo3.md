# A Frame on a Shelf in a House (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Dorm War II: Pre-Game Show](./dormwartwo2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwartwo3
* Group: Main
* Triggered by label: dormwartwo2
* Chain sources: dormwartwo2
* Chain sources path: dormwartwo2

## Official wiki page

[A Frame on a Shelf in a House](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo3&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo3:
    scene sky
    with dissolve2
    play music "summerwind.mp3"

    "Some time later in some other place, something starts to happen."
    "It isn’t anything depressing, so there’s no need to worry the way you normally would. "
    "In fact, all things considered, it’s quite joyous and quite fun. For today, on this day so scarred by frequent let downs and misguided goals, we find ourselves on the precipice of reconciliation."
    "Not between two separate people, but between one girl and the two visions she has of herself."
    "But before we can get to that, we must cross a bridge."

    scene halloweenatchikas1
    with dissolve2

    "A bridge to a familiar apartment that, despite all expectations, has managed to cling to a sense of purity that many other locales have long since abandoned since you woke up."
    "Two girls sit in the bedroom, playing with toys and snacking on celery sticks- but there is a third entity right there with them."
    "It is not the type of entity you know or fear."
    "But it peers out from behind its glass in a 500 yen frame and longs to return to this world."
    "To pick up where it left off."

    play sound "dooropen.mp3"
    scene halloweenatchikas2
    with dissolve

    "But it takes solace in the fact that there is someone else now carrying that torch, and understands that any job left incomplete will surely be finished by someone else."
    "The final entity slips back into its frame."
    "Or was it ever there at all?"
    "The answer will change depending on who you ask."
    "But, if you ask me-"
    "It isn’t our body or our heart that makes us alive, but our ideals."
    "And if there’s ever anyone willing to adopt those once your physical self leaves the picture, you can find comfort in the fact that there will always be another frame on a shelf in a house somewhere."
    "And that you’ll still be able to live on even when your flesh has rotted off of your bones."

    c "Guess who’s back from school!"

    scene halloweenatchikas3
    with dissolve

    ch "Big sis Chika!"
    tk "Candy!"
    c "I see your priorities are the same as ever, Tsukasa."
    tk "Of course they are! Why would I ever care about {i}you{/i} when you hold what I have been waiting for since the moment I arrived!"
    ch "And just in time, too! If Chinami had to eat one more celery stick, she was going to run away from home!"

    scene halloweenatchikas4
    with dissolve

    c "Nuh-uh. Not if I have anything to do with it. Did you finish your homework for the day? Was Tsukasa able to help you?"
    ch "Mhm! Tsukasa knows all sorts of things that Papa probably doesn’t even know! Like how to read earnings reports and what asset liquidation means!"

    scene halloweenatchikas5
    with dissolve

    c "Huh? Did I print out the wrong vocabulary sheet or something? I don’t remember seeing anything about {i}asset liquidation.{/i}"
    tk "Your peasant vocabulary words will not prepare Chinami for the real world! If she is ever going to be a successful CEO, she needs to get ahead of the curve while she’s still young!"
    ch "That’s right! Big sis Chika...you’re fired! Now give Chinami her candy!"

    scene halloweenatchikas6
    with dissolve

    c "I’m starting to think you might not be a very good influence on my little sister."
    tk "Hey, {i}I’m{/i} not the one going around dressed like Clifford the Big Red Dog’s mistress. Now hand over the goods!"

    scene halloweenatchikas7
    with dissolve

    c "Nuh-uh. Not until you say the thing. You know how this works, don’t you?"
    tk "Of course I do! I’ve prepared all month for this!"
    tk "Treat!"
    c "I think you forgot a couple words, Tsukasa."
    tk "I’ve forgotten nothing. I know what I want and giving you options just lessens my chances of getting it."
    ch "That’s okay. Chinami will take the trick as payment for learning about asset liquidation."

    scene halloweenatchikas8
    with dissolve

    tk "Your sacrifice will not be forgotten, Chinami. Tsukasa will remember this."
    ch "As long as Chinami can have one piece with peanuts in-"
    c "No. "

    scene halloweenatchikas9
    with dissolve

    ch "Rats! Foiled again!"
    tk "Aren’t you allergic to peanuts? Why are you always trying to kill yourself? If you have thoughts like that, you should talk to someone."
    c "Okay, here. Take everything I’ve got. Just stop talking about sad stuff. You’re supposed to be having fun for the rest of the day now that your homework is done, not...whatever that was."

    scene halloweenatchikas7
    with dissolve

    tk "Finally! My treat!"
    ch "Chinami’s trick!"

    scene halloweenatchikas10
    with fade

    c "Yeah, yeah. Just don’t eat it all at once or you’ll get a tummy ache. "
    c "Oh! And make sure you throw away all of the wrappers because I am {i}not{/i} going to be a happy dog if we get ants again!"
    tk "I’ll have my newest butler come in and clean when he picks me up later!"

    play sound "dooropen.mp3"
    scene halloweenatchikas11
    with dissolve

    c "You should really just learn how to clean up after yourself, Tsukasa. You can’t lean on other people for the rest of forever."
    tk "You don’t even pay for your own phone bill! You have no right to tell me what I should or shouldn’t lean on others for!"
    c "That’s a completely different-"
    y "Yo."

    scene halloweenatchikas12
    with hpunch

    c "Guh! Jesus, when did you walk in? I didn’t even hear you and you weren’t supposed to be here for, like...another hour."
    y "Right before that brat started shit talking you in your own house."
    y "What happened to keepin’ the door locked? What if I was one of those homeless people coming to take all your shit?"

    scene halloweenatchikas13
    with dissolve

    c "Then you probably would have gotten distracted by my costume and given me enough time to chain you to the stove and call the cops."
    y "{i}That’s{/i} your costume?"
    c "Mhm. Is there a problem?"
    y "Yeah. Where’s the rest of it?"

    scene halloweenatchikas14
    with dissolve

    c "Dunno. Sensei’s bedroom floor, maybe?"
    y "..."
    c "..."

    scene halloweenatchikas15
    with dissolve

    c "Yumi?"
    y "Oh, sorry. Ain’t been gettin’ much sleep lately. "
    c "I bet. Having a king-size bed and a room all to yourself sounds like it can get pretty exhausting. I have no idea how you do it."
    y "{i}Did{/i} it. "
    c "Are you seriously trying to police my grammar despite having a total of like, four high school lessons under your belt?"
    y "No. I’m saying I moved out again. Ain’t crashin’ there anymore."

    scene halloweenatchikas16
    with dissolve

    c "Ah! Then...does that mean-"
    y "Yup. Got yourself a full time babysitter again. Hope you’re happy."
    c "I am! Super happy! This is the best news I’ve gotten in like, forever! "
    c "You do realize that {i}I’m{/i} the one who’s supposed to be getting {i}you{/i} a birthday present, right? Because you coming back is like, the second best present I could have ever gotten."
    y "The first being?"

    scene halloweenatchikas17
    with dissolve

    c "Front row Niki tickets. "
    y "Ain’t that Noriko girl related to her? Just get ‘em from her. Probably gets a crazy discount at the very least."
    c "They’re way too expensive to just come out and ask for, so I’ve been waiting for her to say something about it first and-"

    scene halloweenatchikas18
    with dissolve

    c "Wait. Fuck. I left your present at school."
    y "Hm? You got me a present? Why?"
    c "Uhh...because you’re my best friend? "
    y "Okay...but I ain’t ever gotten you anything for your birthday. "
    c "All that matters to me is your happiness."
    y "What size are your shoes again? Might be able to raise enough money to get you a pair by the end of next year."

    scene halloweenatchikas19
    with dissolve

    c "Happy birthday, Yumi. I’m glad you’re home."
    y "Yeah...whatever. Where’s the twerp? Haven’t seen her in a while and should probably apologize for leavin’ if I’m gonna be stayin’ here again."

    scene black
    with dissolve2

    c "Chinami! Look who decided to show up!"
    ch "Amazon Prime?!"
    c "Even better!"
    tk "Than Amazon Prime?! I don’t believe it! That’s-"
    tk "Oh. It’s just some girl. Boring."
    ch "Big sis Yumi! You’re still alive! This {i}is{/i} better than Amazon Prime!"
    tk "Ugh. You poor people are so uncivilized. I bet she doesn’t even have a Rolex."

    scene halloweenatchikas20
    with dissolve2

    "The house that had grown so lonely and so quiet these recent days was, once again, filled with noise as its third resident moved through the entryway for the first time in what felt like forever to everyone involved."
    "And while they are no family by traditional standards, the ways in which they care for one another make them just as viable as any household not disadvantaged by the shape and flavor of their DNA."
    "A picture in a frame on a shelf in a house gazes on with unblinking eyes, but everyone inside is too caught up in the moment to remember she’s there."
    "But that’s fine."
    "Because it’s moments like this that remind her she doesn’t need to be."
    "And the fact that there is still a family at all is everything she could have ever wanted if she was able to want in the first place."
    "Maybe she is. Maybe she isn’t."
    "The answer will change depending on who you ask."
    "So choose whichever one makes you the happiest and be sure to answer with that if {i}you’re{/i} the one who ever receives the question."

    c "So...remember that thing I texted you about earlier?"
    y "Wouldn’t be here right now if I didn’t. Shit woke me up from a nap, so it better be important."
    c "It is. I need your help with something."
    y "Like...{i}me?{/i} Or the Yakuza? Cause I ain’t really sure how Gary is gonna feel about lending you a hand after all that shit you said to him."
    c "First off, I mean {i}you.{/i} Second, fuck Gary. And third, can you agree to lend me a hand before I even tell you what it is?"
    y "Fuck no. We might be friends, but that doesn’t mean I’m just gonna blindly do whatever the fuck you need me to do. Gotta put myself first. You know that."

    scene halloweenatchikas21
    with dissolve

    c "I mean...{i}yeah.{/i} But given how opposed to it you were last year, I doubt you’re just going to flat out agree. And this might be a good chance to start getting back on everybody’s good side again."

    scene halloweenatchikas22
    with dissolve

    y "Hah...didn’t I already tell you I don’t really give a shit about bein’ on everybody’s good side? "
    y "My plan for droppin’ out still stands, you know. Just because I’m movin’ out of my dad’s place doesn’t mean I’m backtracking on {i}everything.{/i}"
    y "I’m just...reevaluating certain shit. Tryin’ to move {i}forward{/i} again so I don’t wind up like..."
    y "Well, like somebody really shitty."

    scene halloweenatchikas23
    with dissolve

    y "Also, what’s this shit about last year? All we did for Halloween last year was that fuckin’ party thing and I was only there for like, ten minutes."
    c "We decided to combine the Halloween party with the Dorm Wars this year. And with you being gone, it means that it’s nine against ten."

    scene halloweenatchikas24
    with dissolve

    y "Then take the one loss and make up for it in other contests or whatever. Don’t drag me into it."
    c "But I want to win Sensei! And I want people to like you again!"
    y "Nobody ever liked me, Chika."
    c "Okay, then I want people to be mildly conflicted in regard to your existence again! "
    c "Plus, Nodoka volunteered to go up against you and this might be a good way to kick her ass without {i}literally kicking her ass{/i} in front of everyone."

    scene halloweenatchikas25
    with dissolve

    y "Nah...There ain’t no way the others would be cool with that if everything I’ve heard from you is true. The fuck would they even want me there for?"
    c "Honestly? I think pretty much everybody is rooting for Nodoka to win to, like...try and give her some sort of revenge and make you look like an idiot or something."
    y "Ain’t really sellin’ me on this, you know. And I got no clue if I’d even be able to be {i}around{/i} her without trying to kill her again."

    scene halloweenatchikas26
    with dissolve

    c "But you’re better than that! I know you are. And if you really {i}are{/i} trying to move forward, wouldn’t it be good to, like...try and get revenge in a way that doesn’t lead to everyone fearing you?"
    y "Even if I do say yes and I {i}do{/i} win...the hell is that going to do for my reputation? Not like people are gonna forget I nearly gave her a concussion because I won some stupid contest."

    scene halloweenatchikas27
    with dissolve

    c "The second floor, probably not. They all seem pretty close with one another. "
    c "But if you {i}do{/i} win and bring the first floor one step closer to winning the whole Dorm War, I’m sure {i}some{/i} girls might appreciate it."
    y "Sounds to me like you’re just desperate to not go through the war thing with a one man handicap."
    c "Aren’t friends supposed to go to war for one another, though? I literally fought off the Yakuza for you."
    y "I {i}called off{/i} the Yakuza while you were fighting them."
    c "Sure, but we all know that I would have won in the end, right?"
    y "I don’t know, Chika...The fuck would I even be competing in?"
    c "Oh. Yeah, good question. I have no idea."

    scene halloweenatchikas28
    with dissolve

    c "Yeah, I’m not sure if your thingy was decided on yet. I left school before all of that stuff was distributed, so all I really know is my contest and what came before me."
    y "Can you, like...find out?"
    c "Sure. Come with me to the kitchen so I can get my phone. I’ll ask right now."
    y "Hah...fine. Whatever."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "phonebeep.wav"
    scene halloweenatchikas29
    with dissolve2

    c "There. Text sent. I’ve just gotta wait for Ayane to fill me in now."
    y "Listen, Chika...I ain’t tryin’ to get your hopes up and shit when this is obviously a thing you really care about..."
    y "But if this is something weird or...some shit I’m not comfortable with, I can’t guarantee I’ll be cool with...you know, {i}doing{/i} it."
    y "So if I do back down, it ain’t personal."
    c "I know. And I’m sure it’ll be fine. If worse comes to worst, I can probably convince Sensei and Imani to let me take your place as, like...a one time exception thing. "
    y "Cool...yeah. "

    play sound "phonebeep.wav"

    y "You’d probably be better off than me in the first place. Ain’t much I’m really {i}good{/i} at, you know?"

    scene halloweenatchikas30
    with dissolve

    c "Oh, stop. I’m sure you’ll be plenty good at..."
    c "At..."

    scene halloweenatchikas31
    with dissolve

    c "..."
    y "..."
    c "Good luck."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    "I collapse onto the bed, knowing full well that I’m going to be dragged out of it first thing in the morning so that nineteen (Or twenty) girls can fight over what to do with my body."
    "But between the scattered worries of what this could mean for both my physical safety and mental health, I thank whatever forces led me to this moment. "
    "Because if it were not for them, I’d likely still be so numb that I wouldn’t be able to feel things like this at all."
    "But that’s just a fleeting thought that serves to distract me from the sad truth that I’ll never know anything about myself at all."
    "And that everything I do is just served up on a platter by people I’m expected to trust."
    "What is real? "
    "What is not?"
    "These are the things I think of as I begin to fall asleep."

    stop music

    "But what I dream of is much darker."

    $ renpy.end_replay()
    $ dormwartwo3 = True

label dormwartwo4:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
scene anewinterview46
    with dissolve

    o "Don’t fucking joke about that. It’s not funny."
    c "I obviously wasn’t serious. Chill. "
    ay "Uhhh...okay! So, without sowing any more seeds of destruction, I’d like to wish the two of you the best of luck in your poll and urge you to keep campaigning as hard as you can!"

    scene anewinterview47
    with dissolve

    ay "And remember, folks! Be sure to vote! Wasting your vote is the same thing as wasting your voice, and you’d never want to throw that away, would you?!"
    ay "This is Ayane Amamiya, signing off! Back to you for the final interview, Molly!"

    scene anewinterview48
    with fade

    mo "Thanks, Ayane! And thank you Miku and Uta for joining me for the final interview of the-"
    mi "Ughhhhh! Whatever! This is like, so totally boring. Like, Dorm Wars? Seriously? Don’t you guys have any friends? Is this really what you do for fun?"
    u "The idea of “fun” does not exist. All we have is silence....shadows...the dark...and a mission. A mission to remain unseen. {i}Unheard.{/i} Unnoticed..."

    scene anewinterview49
    with dissolve

    mi "Tch. Ain’t “unnoticed” the same thing as “unheard” and “unseen?” That’s like, totally adorable. Look at you trying so hard to act cool. It’s hilarious. Can I take a pic? I’ll tag you. What’s your insta?"
    u "I do not understand the concepts of which you speak...nor the wretched scent of that perfume nor impractical accessories you don as if they are protection."
    mi "They {i}are{/i} protection, doll. They’re protecting me from looking so {i}stupid.{/i} Like, where did you even get that scarf? Goodwill?"
    mo "I have to say, this is going a lot better than I expected it to and I have to applaud both of you for both your fantastic costume design {i}and{/i} your commitment to your respective roles."

    scene anewinterview50
    with dissolve

    mo "It’s a risky move choosing to dress and act like a gyaru while we already have one in- uh-oh."
    u "Trouble approaches like morning dew. Quiet...but consistent. Reliable."

    scene anewinterview51
    with dissolve

    c "..."
    mi "..."
    mi "Uhhhh..."
    c "Miku..."
    mi "I...can totally, like...explain..."
    mi "This is-"

    scene anewinterview52
    with hpunch

    c "YOU ARE SO FREAKING PRECIOUS, OH MY GOD!"
    c "Where’d you get your top? And those bracelets? You have to show me. Just not today since I’ve got other stuff to do."

    scene anewinterview53
    with dissolve

    c "Oh! We should, like...totally go shopping together soon. I can show you all sorts of places with great stuff for mad cheap that-"
    mo "Chika, Miku’s disguise is simply a temporary item set that-"

    scene anewinterview54
    with hpunch

    c "Shut your fucking mouth, Molly! Let me talk to Miku alone! No one else ever dresses like me and I finally have someone to bond with even if it’s fake!"
    mi "Uhh...umm..."
    mak "Miku, you have a...tanning appointment in five minutes. Or something."

    scene anewinterview55
    with dissolve

    mi "R-Right! That, like...totes slipped my mind! Thankies, Makoto!"
    c "Wait! Come back! We weren’t done bonding! I love you!"
    u "Gone...like the color of the Chitose River in winter...waiting for its moment to return. But when? And who will be there to watch as the color returns?"

    scene anewinterview56
    with dissolve

    c "..."
    u "..."
    mo "..."

    scene anewinterview57
    with dissolve

    u "Wshhhh..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    mo "This concludes our second annual pre-war interviews! Thanks so much for watching and be sure to keep an eye out as the contests kick off first thing in the morning when I take on floor one’s Sana Sakakibara!"
    mo "Until then...Stay modest! Stay Molly!"
    mo "Seele out!"
    a "You know that’s not what that character is like at all, right?"
    mo "I actually haven’t even played the game yet."

    $ renpy.end_replay()
    $ dormwartwo2 = True

    "........."
    "......"
    "..."

    jump dormwartwo3
...
```