# The Bending of Italics (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [A Thousand Truths](./beachmas8.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachmas9
* Group: Main
* Triggered by label: beachmas8
* Chain sources: beachmas8
* Chain sources path: beachmas8

## Official wiki page

[The Bending of Italics](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas9&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label beachmas9:
    scene clearnightsky
    with dissolve2
    stop music fadeout 15.0

    "{i}But further along the beach, things are not as simple and joyous.{/i}"
    "{i}Further along the beach is a man who struggles to grasp the concept of killing at all when the world around him is one giant fallacy.{/i}"
    "{i}Or is that just what he’s meant to think?{/i}"
    "{i}Is that just what you’re meant to think?{/i}"
    "{i}How can you kill what doesn’t exist? And what metaphorical line in the sand he kicks up as he walks must we cross over until we ask ourselves what is really important?{/i}"
    "{i}How much further down the beach do we need to walk until we reach the edge of the world?{/i}"
    "{i}And can we even reach it at all from here?{/i}"
    "{i}I see no walls...do you?{/i}"
    "{i}I see no barrier...{/i}"
    "{i}Do you?{/i}"

    play sound "static.mp3"
    scene tsuneyobeach1
    with flash
    stop sound
    play music "sensei.mp3"

    "I have no use for italics that bend my words into pretty shapes when the world itself is bending all of us every single second we spend inside of it."
    "We are the letters. "
    "Our role is to be manipulated. "
    "Italicized. Bolded. Highlighted."
    "Strewn together in different combinations until our presence means something."
    "But it won’t mean anything in the way you want it to."
    "So go on. "
    "Misinterpret it all again."
    "See the barrier as a different form of metaphor."
    "See the people you love as no more than code."
    "For I am tired of telling the truth to people who have no desire to {i}hear{/i} it."
    "I am tired of the rise and fall of the sun and the gods and the tide and all of the things you already had before I ever brought you here."
    "Before I showed you the {i}truth.{/i}"
    "You’ll never see anything if you keep walking down the shore with your eyes closed."
    "And the only reason you’re stuck here in the first place is because you think you’re somewhere you’re not."
    "The only barrier between us and freedom is one that you, yourself, have built."
    "Tear it down."
    "And for the first time in your life-"
    "{i}Listen to me.{/i}"
    "{i}Bend.{/i}"

    s "Tsuneyo? What are you doing out here all by yourself?"
    t "I am thinking."
    s "About...noodles, I’m assuming?"
    t "Amongst other things."
    s "Well...do you mind if I join you? "
    t "Do you mind if I refuse?"
    s "You haven’t refused any of the {i}other{/i} times I’ve dedicated to hanging out with you lately. So either something has happened for you to reevaluate the way you look at me or-"
    t "Or you’ve never understood the way I’ve looked at you at all."
    s "..."
    t "I know that I haven’t made that easy."
    t "I’ve never been truly {i}understood{/i} by anyone. Not even those like the Emerald Guardian or my father...the ones who care for me more than everyone else."
    t "It’s possible that my definition for what it means to be “understood” is strict in comparison to one we write in books. "
    t "But I don’t think it’s possible to ever understand anyone when we all do things that even {i}we{/i} don’t understand at times."
    t "Is it enough to only understand a fraction of someone?"
    t "What if the part you don’t understand is the most dangerous part of all? Is that not cause for concern? For fear?"
    s "You’re right to be afraid of me, you know."
    t "I’m not talking about you. I’m talking about myself."

    scene tsuneyobeach2
    with dissolve

    t "It appears that I have done something wrong. And yet...I can not seem to wrap my head around {i}why.{/i}"
    t "How am I to prevent myself from hurting more people I care about when I can not comprehend which of my actions will directly harm them?"
    t "Is this how you feel every morning when you wake up and leave your house to go prey upon the weak?"
    t "Am I just one more version of you? Destined to forever walk this beach alone in hopes that someone will find me and remind me that it’s {i}okay{/i} to hurt people so long as it’s done accidentally?"
    s "Tsuneyo-"
    t "The Guardian wants me to apologize to you."
    t "She wants me to apologize to the very man who betrayed her...and took advantage of her at her most vulnerable...all because she is afraid of losing him. "
    t "How am I supposed to understand that? How am I supposed to understand {i}anyone{/i} with such complex emotions? "
    t "How was I meant to prepare for this? What could I have done differently?"
    s "Nothing."

    scene tsuneyobeach3
    with dissolve

    t "..."
    s "There’s nothing you could have done differently."
    t "That’s where I keep landing as well."
    t "There’s nothing I can do. No way I can prevent additional harm when even attempting to prevent said harm can harm in its own way."
    t "What is this wretched cycle of pain? The one that destroys just so it can rebuild itself? The one that stretches wider than the ocean and taller than the sky?"
    s "It’s called life. And yeah, it kind of sucks the majority of the time. But what else are we going to do? "
    s "Just pretend everything is fine instead of trying to force yourself to understand anything. "
    s "Because if you’re going to stand out here and keep asking yourself rhetorical and borderline paradoxical questions about what you’re meant to do next, no one is ever going to see you again."
    t "I wonder what a world without me would look like. "
    t "I wonder if anything would change."
    s "I know one girl who would be very upset to hear you say things like that. And she’s the same one who sent me out here to come find you."

    scene tsuneyobeach4
    with dissolve

    t "It seems I have caused a great deal of trouble for both of you. And for that, I am sorry."
    t "But I will {i}not{/i} apologize for the things I said about you during the War of the Dorms."
    t "Not until you admit what you did to my friend. "
    s "And if I tell you {i}I don’t know{/i} what I did to your friend?"
    t "I’d tell you to stop pretending and actually {i}think.{/i}"
    t "If someone like me...someone who knew close to nothing before being tossed into this world, can form an opinion based on evidence...there is no way that {i}you{/i} can not."
    t "You’re either a coward...or you are lying to both of us. And only one of those things is unforgivable. "
    s "They’re both unforgiv-"

    scene tsuneyobeach5
    with dissolve

    t "There is nothing wrong with being afraid. If your cowardice comes at the cost of your humanity, that is a different story. But my friend adamantly believes that you did nothing wrong."
    t "And I simply can not believe her until {i}you{/i} reach that same conclusion instead of hiding from it like menma in a tangle of buckwheat. "

    scene black
    with dissolve2

    "I sit down just beyond the reach of the tide and wait for Tsuneyo to turn around and speak to me directly."
    "It takes another five minutes of complete silence before she does this. But I’m unsure if any of her anger has subsided as I can rarely ever tell what she’s feeling just by looking at her face."
    "She stares deeply into my eyes."
    "It feels as if she’s drilling holes into my pupils so deep that they’re going to penetrate the back of my skull and allow her to see right through me."
    "More than she already does."
    "Which is more than I ever thought she would."

    scene tsuneyobeach6
    with dissolve

    s "..."
    t "..."
    s "I don’t..."
    s "I don’t think what you did during the Dorm Wars was “wrong.”"

    scene tsuneyobeach7
    with dissolve

    t "You...don’t?"
    s "No. And I think you’re right to feel conflicted about all of this since sticking up for the people you love is always the morally correct thing to do."
    s "But moral correctness doesn’t have any sort of correlation to what the recipient of unwanted feelings will...well, {i}feel.{/i}"
    s "I don’t know if you were looking at us back then, but neither one of us could move. We were in shock."
    s "I guess we were just under the assumption that burying something meant it would stay underground. And neither of us thought we’d ever come face to face with it again."

    scene tsuneyobeach8
    with dissolve

    t "Should it have ever been buried in the first place, though? That is the question we must ask ourselves."
    t "Is ignoring such a serious matter truly what is best? Or should something be {i}done{/i} about it so nothing similar ever happens again?"
    s "What can be done?"
    t "That depends on what you did."
    s "Molly says I didn’t do anything."
    s "But what do you think I did?"

    scene tsuneyobeach9
    with dissolve

    t "I think you took something that didn’t belong to you."
    t "And I think you’re worried now because it’s burning holes in your pockets...but you’ve come too far since then and are now unable to return it."
    s "Things like that can never be returned in the first place."
    t "And that is why they are the worst to take."
    s "I can’t apologize for something I’ll never know if I actually did or not."
    t "Maybe so. But you can feel remorse."

    scene tsuneyobeach10
    with dissolve

    s "Do you think I haven’t? "
    s "Do you think I’m {i}proud{/i} of myself for this? Like it’s some sort of notch in my belt or a tally mark on a checklist?"
    s "At least Molly had someone like you to talk to after what happened while I had to lay in my bed night after night and {i}guess.{/i}"
    s "I know what it looked like. I’m not an idiot. But I don’t know for sure what {i}happened.{/i}"

    scene tsuneyobeach11
    with dissolve

    s "And I’m afraid of finding out."
    t "..."
    s "I {i}am{/i} a coward. It’s just like you said."
    s "But I wouldn’t do something like that to someone I care about."
    s "There’s no way I’d...do that to...someone...I care about..."
    t "..."
    s "..."

    scene tsuneyobeach12
    with dissolve

    t "I didn’t realize you were capable of showing such emotion."
    s "Yeah, well...you’re not really known for your expressions either."
    t "Thank you for saying that to me. Not the part about my expressionlessness, but the part where you admitted this was not just another lap around the noodle shop."
    t "The Guardian believes you may have been some sort of victim in whatever happened, just as she was."
    t "And while there is no way of ever knowing for sure as we can not undo the past, we can attempt to look forward."
    s "Not when certain people go digging up the past and throwing it back in our faces, we can’t."
    s "But..."
    s "I guess that was sort of necessary if we were ever going to get to where we are right now."
    t "I see now that I was blinded by my own perception of events. And that my ill will was only directed toward you as I had nowhere else to send it."
    s "How can you be so sure I’m not just a good actor? And that I’m lying to you right now to get you off of my case?"
    t "I can’t. And as I mentioned earlier, I can’t ever {i}understand{/i} you either. But I can {i}trust{/i} you — which is something Molly wants me to do."
    s "..."
    t "My father always told me that there are forces in this world that will compel us to act in ways we do not understand. "
    t "When I was younger, I would fall back on this every time I added an incorrect ingredient to a recipe or misjudged a portion size. "
    t "But it wasn’t until meeting you and everyone else that I understood his words stretched far beyond the reach of our restaurant. "
    t "I have a hard time remembering those words when things do not go the way they’re supposed to. And I imagine he’d be laughing right now if he could only see me."

    scene tsuneyobeach13
    with dissolve

    t "But he can not. And you {i}can.{/i}"
    t "So I ask you...do you truly care about us?"
    t "Or is the list of what you love still as empty as your eyes?"
    s "I care..."

    scene tsuneyobeach14
    with dissolve

    s "Just..."
    s "I don’t know if I care the way I’m supposed to. Or what the proper way to “care” even is."
    s "But I would never force that on anyone."
    s "At least..."
    s "Not...willingly..."

    scene tsuneyobeach15
    with dissolve

    t "Good. "
    t "But know that if you are lying to me about this...and you do go on to hurt someone in an unforgivable way...that I will not hesitate to introduce your organs to Gallow’s Edge."
    s "You’d be doing everyone a favor, that’s for sure."
    t "In that case, yes."
    t "But as it currently stands, you are the glue keeping many things in place. And a world without you would be sure to collapse within days."
    s "So I hear."
    t "Hearing and understanding are two different things."
    s "I’m like you — not good at “understanding.”"
    t "What I struggle to understand is people. What you struggle to understand is love."
    t "I can tell when someone cares about me, which is one of the many reasons I have not fallen for you the way the others have. I know that there is no real “love” there."
    t "You are the inverse. You can read everyone...and base each of your actions specifically on what you believe a person needs. "
    t "But you can not even understand the love from those closest to you...can you?"
    s "..."
    t "It would be interesting if we could trade places for a day."
    t "I could finally read rooms better."
    t "And you could feel like there’s some sort of purpose to all of this."
    s "I think you should head back to the inn, Tsuneyo. Molly’s going to get the wrong idea and think you hate her if you just keep avoiding her like this."
    s "But, then again, I have no idea what the hell has happened between you two over the last couple months, so...yeah."
    t "Strange. Neither can I."

    scene tsuneyobeach16
    with dissolve

    s "Hm?"
    t "Perhaps it has something to do with the humidity? Or how busy the shop has been as of late?"
    s "How would the humidity-"
    t "Regardless of the root cause, it is good knowing there is someone who feels the same way. As oftentimes, it seems that things are simply going around in circles."
    s "..."

    scene tsuneyobeach17
    with dissolve

    t "Will you not walk with me back to the inn? It is dangerous out here for a weak man like you, and I may be able to provide some sort of protective assistance. "
    s "Tsuneyo...what if I told you that time really {i}was{/i} moving around in circles? And that the way you feel isn’t necessarily wrong?"
    t "I’d say that you’re starting to sound more like my father. Regardless, if you do not need my protection, I will be on my way. My son is waiting."
    t "But thank you again for clearing up the current status of our relationship and where things stand between us. "
    t "I kindly hope for your continued support hereafter."
    s "Yeah..."

    scene black
    with dissolve2

    s "See you...later..."

    "I watch Tsuneyo for a full ten minutes until she disappears from my sight."
    "And it isn’t until she’s gone that I’m able to really grasp what she said about never being able to understand someone."
    "We all have patterns — things we do on a daily basis that help others predict our next actions or sentences."
    "And it’s funny. Based on dialogue and experience alone...she is perhaps the most predictable person in the entire class."

    s "..."

    "But every time her pattern breaks...she goes so far in another direction that it’s impossible to keep up."

    s "..."

    "I can’t help wanting to chase after her."
    "But it’s dangerous out here for someone as weak as me."
    "So I pick myself up off of the ground and set my sights on anyone weaker."
    "On anyone more predictable."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ beachmas9 = True
    stop music fadeout 7.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "........."
    "......"
    "..."

    jump beachmas10

label beachmas10:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
with dissolve

    to "I already said it! The regular one! Where the man is behind the girl and the girl’s hands are tied to something in front of her! Like a...pole or...something!"

    scene beachmastod23
    with fade

    ki "How fucked up does your algo have to be for something like that to be “regular?”"
    to "I seldom view such content! Forgive me for having more important things to do!"
    no "And sex servants. She never specifically denied the sex servants."
    to "I have no such thing!"

    scene beachmastod24
    with fade

    to "Ami! It is now your turn because everyone has decided to gang up on me and I am feeling very overwhelmed!"
    a "Don’t be! And excellent choice of position!"
    to "I would very much like to move past that right now! Truth or dare!"
    a "Let’s go with...truth!"
    ki "Ask her something lewd! Keep the ball rolling!"
    to "I would never-"
    ki "But it would make you {i}cooler...{/i}"
    to "Does...talking about such things truly make one cooler? I was under the impression it just made you a harlot."
    ki "Are you calling me a {i}harlot,{/i} Touka?"
    to "Are...Are you not? I thought that was your whole thing."
    mo "F’s in chat for Kirin. "
    a "Ask whatever you want, Touka. I don’t really care. "
    m "You probably should. Your interests aren’t exactly socially acceptable."
    a "They are in some countries."
    to "I will...remain true to myself and ask you something that is {i}not{/i} lewd as...imagining myself ever being like Kirin worries me greatly. "
    to "Ami...what is the...most absurd thing you would ever do for someone you love?"

    scene beachmastod25
    with dissolve

    a "The most...absurd thing...for someone I love?"
    to "R-Right! Where would you draw the line? Just how far would you go to prove yourself to the person you admire?"
    ki "His name is Sensei. You can call him Sensei."
    a "Hmm...I’ve never really thought about it before..."
    mo "I’m calling BS. I’ve had you pegged as the yandere from the start."
    to "What is a yandere, exactly?"
    m "Someone so attached to the object of their affection that they’re willing to kill anyone and everyone who gets in their way."
    to "Oh. Well of course Ami isn’t like that. She’s such a good girl. Just look at her, lost in thought about the man she loves. It’s adorable."
    no "It’s even more adorable when you remember they’re related."
    to "Ami, you’d never {i}kill{/i} for Sensei, would you?"

    scene beachmastod26
    with dissolve

    a "Oh, I {i}definitely{/i} would. I’m just trying to think of things that are {i}worse.{/i}"
    to "Than murder?!"
    mo "Boom! Called it! Never doubt Molly MacCormack’s ability to accurately categorize young girls into various tropes and groups! It is for this exact reason that I was put on this planet!"
    a "How long do you have to torture someone for it to be worse than murder?"
    to "This isn’t wholesome at all! Pick dare instead!"
    a "Is sensory deprivation cruel? Or is that kind of just a thing that nobody really cares about?"
    ay "When did you get like this?"

    scene beachmastod27
    with dissolve

    a "Like what?"
    ay "Like...Like that."
    a "Are you saying you {i}wouldn’t{/i} kill for Sensei?"
    ay "Uhh...I mean...I guess if I absolutely {i}had{/i} to. But-"

    scene beachmastod28
    with dissolve

    a "Well, I guess we know who loves him more then!"

    scene beachmastod29
    with fade

    a "Okey-dokey! Seeing as it’s my turn now and Kirin is the only one who hasn’t gotten a truth or a dare yet..."
    ki "Bring it on. And, just FYI, I won’t put up a fight like a certain {i}someone{/i} if you ask for my favorite sex position. I’ve got that drilled into the back of my-"
    a "Maya!"

    scene beachmastod30
    with dissolve

    ki "Seriously?! But you literally {i}just{/i} acknowledged how I haven’t gotten to go yet!"
    a "Yeah, but I wasn’t really interested in anything I could make you say or do and I want to hear Maya say more cute things about how much she loves me."
    m "Well, good luck as I mentioned earlier that I am a “dares only” girl and have little interest in whispering sweet nothings to you just because I am asked to."

    scene black
    with dissolve2

    a "Fine. Then I dare you to come over here and give me a hug because I love you."
    ay "Careful, Maya. You’ve been within ten feet of Sensei today so there’s a chance Ami might smell him on your skin and slit your throat when you’re not paying attention."
    m "If Ami truly wanted to kill me, I can guarantee you I would be dead already."
    a "Keep saying suspicious things like that and I might have to!~"

    "{i}No one chooses Kirin for the next fifteen minutes. And no one ever agrees to kiss her either.{/i}"
    "{i}Touka only chose dares from that point on.{/i}"
    "{i}And Ami manages to make it through the rest of the game without killing anyone.{/i}"

    $ renpy.end_replay()
    $ beachmas8 = True

    jump beachmas9
...
```