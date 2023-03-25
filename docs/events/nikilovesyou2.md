# The End of the Tour (Niki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [What it Takes to Move Forward](./nikilovesyou1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: nikilovesyou2
* Group: Niki
* Triggered by label: nikilovesyou1
* Chain sources: nikilovesyou1
* Chain sources path: nikilovesyou1

## Official wiki page

[The End of the Tour](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikilovesyou2&go=Go) for more details.

## Event code

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
label nikilovesyou2:
    if _in_replay:
        play music "starvingtodeathoutofreachofthesun.mp3"

    scene memorylane1
    with fade

    ni "{i}Do{/i} you have anything to do with it? Because it seems to me like you keep selecting other heroines instead. "
    ni "Who knew the woes of the childhood friend route applied to real life as well?"
    s "You’re starting to sound like a certain Irish girl I know and I can’t say I’m a fan of it."
    ni "Just remember that if you {i}do{/i} continue rejecting my advances, there is an entire Facebook group of people willing to sleep with me. And most of them would probably pay."
    ni "{i}You{/i} get the first-love discount. That’s a once in a lifetime promotion, you know."
    s "Oh, I know. And I’ll be sure to capitalize on it once everything surrounding our relationship stops being so damn depressing."

    scene memorylane2
    with dissolve

    ni "Ugh. I really am going to make it to thirty after all."
    s "..."
    ni "..."

    "Another bout of a certain brand of silence, one that I am beginning to recognize like the back of my hand, carries across the outstretched horizon before planting itself firmly in my lap."
    "It curls up into a ball of intangible warmth and fills me with a dreadful nostalgia that I attempt to wish away by focusing on the head resting upon my shoulder."
    "I wonder if this warmth has invaded her as well — and if the thoughts inside her head at this very moment add up to more than just “I’m happy here.”"
    "Are you?"
    "Happiness is tricky — confusing. And people like me who have grown so disenchanted by the pursuit of it approach the word with extreme caution so as to not {i}think{/i} we’re happy when we’re not."
    "So many good things have happened to me lately."
    "And if that is any indication of what is yet to come, I’d be a fool to not admit I’m terrified as there must always be a balance."
    "What goes up must always come down —but that comes with a caveat."
    "There are things you’ll see and experience in life that will push you further down into the bottomless pit of existence than you’d ever fall on your own."
    "And while there may be people who notice you screaming and begging for help — who take it upon themselves to lend you a hand and attempt to pull you up, no one will ever pull you {i}out.{/i}"
    "In the end, you either drag them down with you or let go and hope they never meet the same fate."
    "It will always be easier to fall than it will be to climb. "
    "And when you’ve fallen as deep as I have, the last thing you possess is the willpower to fight back against fate."
    "So you fall...and fall...and fall forever-"

    ni "I love you so much."

    "And pray that the slowly vanishing light at the top of the well never fully disappears."

    s "..."
    ni "..."
    s "I...love you too, Niki."
    s "Thanks for trying to pull me out of my bottomless pit."

    scene memorylane3
    with dissolve

    ni "It’s that or I jump in there with you. Better to suffer together than to suffer alone, right?"
    s "You don’t deserve to suffer."
    ni "Neither do you."
    s "I do, though. I’m probably not the same person I was when I was with you. A lot has happened since then and I’ve done...a lot of horrible things."
    ni "You can always change."
    s "See, that’s the thing...I don’t {i}want{/i} to. And I have no idea what type of person I’d be if I {i}did.{/i}"
    s "I’ve become the worst parts of myself...I’ve accepted them. And getting rid of those traits would be more like me turning into a new person than turning over a new leaf."
    ni "Then, I hope that bottomless pit of yours is wide enough for two."

    scene memorylane4
    with dissolve

    s "Niki-"
    ni "No matter what you’ve done or what you’ll {i}do,{/i} I’ll be right there with you. "
    ni "You chose a really stubborn person to spend so much time with way back when. This is the result of that."
    ni "You’re too weak to function on your own. Plus, it’s not like I have to {i}agree{/i} with all of those “horrible things” you do, right?"
    ni "You need someone to call you out on your shit — and who better than the girl who’s dealt with more of it than anyone?"
    ni "You’re not like this because you’re a bad person, you’re like this because you never learned how to be a good one. "
    ni "{i}It’s not your fault.{/i}"

    scene memorylane5
    with dissolve

    s "That...doesn’t make it okay."
    ni "Never said it did...just that I’ll always be your home when you have nowhere else to go."
    s "..."
    ni "..."
    s "I wish I remembered more of our past together."
    s "I don’t understand why I ever would have left you behind."
    ni "You left me behind because you’re a selfish asshole who's never been able to grasp the fact that there are other people out there struggling as well."
    ni "But you’re back now. And that’s what matters most."
    ni "We’ll return your memories one way or another- even if I have to force them in myself."
    s "Yeah? And how would you do that?"
    ni "..."
    s "..."
    ni "You don’t have any other plans for the rest of the day, do you?"
    s "I don’t."
    ni "Then...lets go for a walk-"

    stop music
    scene memorylane6
    play sound "broken.mp3"

    ni "[[REDACTED ~ REPEATED USAGE OF A PROHIBITED WORD HAS RESULTED IN A FATAL ERROR]"

    scene black
    stop music

    "////////////////PLEASE NOTE THAT RESTARTING YOUR DEVICE BEFORE AN UPDATE IS COMPLETE MAY RESULT IN IRREPARABLE DAMAGE"
    "........."
    "........"
    "......."
    play sound "static.mp3"
    scene somethinglikethis with flash
    stop sound
    play music "glasswalker.mp3"

    "One's grand flights, one's Sunday baths,"
    "One's tootings at the weddings of the soul"
    "Occur as they occur. So bluish clouds"
    "Occurred above the empty house and the leaves"
    "Of the rhododendrons rattled their gold,"
    "As if someone lived there. Such floods of white"
    "Came bursting from the clouds. So the wind"
    "Threw its contorted strength around the sky."
    "[[BREAK]"
    "Could you have said the bluejay suddenly"
    "Would swoop to earth? It is a wheel, the rays"
    "Around the sun. The wheel survives the myths."
    "The fire eye in the clouds survives the gods."
    "To think of a dove with an eye of grenadine"
    "And pines that are cornets, so it occurs,"
    "And a little island full of geese and stars:"
    "It may be the ignorant man, alone,"
    "Has any chance to mate his life with life"
    "That is the sensual, pearly spuse, the life"
    "That is fluent in even the wintriest bronze. "

    play sound "static.mp3"
    scene ayhh12 with flash
    scene ayhh1 with flash
    scene ayhh3 with flash
    scene specialsky with flash
    stop sound

    "There is a disconnect between that which is real and that which is not — but that disconnection is not one to be perceived by man."
    "It is visible to only those with the eyes of God and those who, in the moments of utmost unholiness, spill liquid sacrament from their pores and tongue."
    "There is a trip to be traveled through unmapped parts of the world."
    "You will see things that happened and didn’t."
    "You will feel things you will never feel again."

    play sound "static.mp3"
    scene roofnoon with flash
    stop sound

    "{b}{size=+20}AND YOU WILL SAVOR THE SPLENDOR IN EVERY SECOND{/b}{/size}"

    play sound "static.mp3"
    scene roofday with flash
    scene roofnoon with flash
    scene roofday with flash
    scene roofnoon with flash
    scene roofday with flash
    scene roofnoon with flash
    scene memorylane7 with flash
    stop sound

    "A walk upon glass through a forest untouched brings us several steps closer to a dance with our mirrored selves."
    "As my eyes connect with a conveyor belt of shadows and familiar unfamiliar faces, it is my legs that wind up moving while the world around me does not."
    "If I could break myself in two and reform with wings I would — but as I’ve never learned to fly, I must grapple with an unbearable truth and squeeze the life from out its body."
    "This is then and this is now."
    "I remember how to make my heart move."

    ni "Do you remember where we are?"
    s "..."
    ni "Would it help if I gave you a hint?"
    s "I can’t really put my finger on it, but..."
    s "I know I’ve been here before."

    scene memorylane8
    with dissolve

    ni "We built a secret base here out of stuff we picked from trash cans."
    ni "We filled it with snacks from my pantry and pretended we were an underground crime-fighting organization."
    ni "Any time we heard a noise, we’d hide behind trees and wait for some evildoer to move through the woods, but no one ever came."
    ni "It was a huge waste of time looking back on things if you don’t count all of the comics we read here as “being productive” but holy shit were we always so excited to come."
    ni "Things stopped being as exciting once Noriko found out about it and we began spending less and less time here as the days went by."
    ni "As you can see, there’s nothing left now...but this place was once really important to us."

    scene memorylane9
    with dissolve

    ni "Ring any bells?"
    s "..."
    ni "Then..."
    ni "How about this-"

    play sound "static.mp3"
    scene memorylane10
    with flash
    stop sound

    ni "We spent a lot of time in the woods when we were younger...but I never really realized it until I stopped going outside."
    ni "This was another spot we loved. Not far from here, there was a hidden path that led to a circle of abandoned gassho houses we’d sneak into to make out."
    ni "It feels like just yesterday we were carving our names on that tree."
    ni "Sucks I wound up coming back to scribble yours out after you left me all alone."

    scene memorylane11
    with dissolve

    ni "Do you have your keys on you? Maybe we could make a new carving?"
    s "You’re still interested in things like that?"
    ni "Oh, come on. Don’t tell me you’re so dead inside that you’re against a little {i}vandalism{/i} now?"

    "My feet are cut deeper as the forest pulls us closer to its core."
    "And while images of the past break their legs trying to run through the four corners of my mind, I see nothing but an endless blur and {i}feel{/i} nothing but the blood soaking into my socks."
    "The one sense that does not deceive me is my hearing as I can faintly make out the sound of a pocket knife being plunged into the flesh of an ancient tree."
    "We’d peel away its skin and replace it with a dream — false hopes in the form of a relationship that would one day perish only to be resurrected by sheer coincidence years later."
    "The rest begins to flow back in."
    "How small her hands were back then."
    "The way her glasses would fog up when it got too hot."
    "Her long, pink hair that would stick to my clothing and get me into trouble with-"

    play sound "static.mp3"
    scene memorylane12
    with flash
    stop sound

    "No. "
    "Stop remembering."

    ni "[[REDACTED]?"
    se "Hmm...how come {i}we{/i} never carved our names into a tree? That would have been cute."
    s "..."
    se "Hellooooo? Anybody home? You can’t just pretend you don’t see me. I know you do."
    ni "Hey, what’s going on? Are you remembering something?"
    se "{i}Hah...{/i}obstinate as ever, I see. And Niki, wow! She’s so pretty now! I can’t help but feel a little jealous."
    se "Are you two together again?"
    se "Does she {i}fuck{/i} you like I did? "
    se "Who’s better, me or her? "
    se "Be honest. I won’t get mad."
    ni "Hey. Talk to me. What’s-"
    s "I remember this place."

    play sound "static.mp3"
    scene memorylane13
    with flash
    stop sound

    ni "What? You do?"
    s "Yeah. We would come here...and there was a...circle of houses and...we would make out..."
    ni "Yeah, but...you’re kind of just repeating what I said a couple minutes ago. Are you really sure you remember? "
    ni "Be honest. I won’t get mad."
    s "More..."
    s "I need to see more..."
    s "Take me somewhere else..."

    scene memorylane14
    with dissolve

    ni "Okay..."
    ni "We’ll go on an all-inclusive tour down memory lane..."
    ni "From where it all began..."

    play sound "static.mp3"
    scene 1 with flash
    scene 2 with flash
    scene 3 with flash
    scene 4 with flash
    scene 5 with flash
    scene 1 with flash
    scene 2 with flash
    scene 3 with flash
    scene 4 with flash
    scene 5 with flash
    scene memorylane15 with flash
    stop sound

    ni "To where it all ended."
    s "Huh?..."
    s "Where..."
    s "Where are we?..."
    ni "I think it’s better if you remember this one without any help."
    ni "This place had a much more profound impact on you than it did on me, after all."

    "Before this, there were other places."
    "A convenience store where we’d stop on the way to school."
    "An old bus stop where we’d wait for over an hour sometimes for a ride into the urban district."
    "An Italian restaurant we never went inside, but always talked about how it would be nice to be able to eat there one day."
    "A softball field."
    "A community pool."
    "The yard of an old house where a dog used to live."
    "It’s gone now and a new one has taken its place."
    "Each of these locations spurred something inside of me to begin moving again. And slowly but surely, the faded traces of what {i}should{/i} be mine have opened up to the idea of coming home."
    "So why has that all come screeching to a halt at the end of the tour?"
    "Why am I numb again {i}now?{/i}"
    "Was I just caught up in the moment earlier?...Piggybacking off of Niki’s nostalgia because I’m so desperate for my own?"

    play sound "static.mp3"
    scene memorylane16 with flash
    stop sound

    "Or am I just suppressing something?"

    ni "You jumped."
    ni "Do you remember?"
    s "I..."
    s "I don’t know..."
    ni "Take as much time as you need."
    ni "This is the hardest part of the trip after all. And I’ve already told you-"
    ni "I’ll return your memories even if I have to force them back in myself."

    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane15 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane21 with flash
    scene memorylane22 with flash
    scene memorylane17 with flash
    scene memorylane18 with flash
    scene memorylane19 with flash
    scene memorylane20 with flash
    scene memorylane21 with flash
    scene memorylane22 with flash
    scene memorylane23 with flash
    stop sound
    $ renpy.pause(5, hard=True)

    s "This..."
    s "This is where it happened..."
    ni "That’s right."
    ni "This is where your world was ripped away from you."

    play sound "static.mp3"
    scene imissyoumore with flash
    scene everythingg with flash
    scene memorylane24 with flash
    stop sound

    ni "You can’t only open yourself up to the good memories, you have to let the bad ones in too."
    ni "You’ll never move on if you just keep ignoring the things that make you hurt. You have to {i}work{/i} if you ever want to get better. Only then will you be able to look back on the past without breaking into a million pieces."
    ni "But I promise you, and I mean this with {i}all{/i} of my heart, I will be there {i}every...single...step{/i} of the way."
    ni "You’re not alone..."
    s "..."
    ni "{i}Look at me.{/i}"

    scene memorylane25
    with dissolve2

    ni "{i}You’re not alone.{/i}"
    ni "{i}Okay?{/i}"
    ni "No matter how horrible you become...or how much work it takes to get you through a single day without feeling sorry for yourself..."
    ni "I will be here. I’ve {i}always{/i} been here. "
    ni "You’re my best friend in the whole entire world...and I am so...{i}so{/i} sorry you had to go through what you did..."
    ni "But..."
    ni "I don’t want to watch you suffer anymore..."
    ni "I want my friend back..."
    s "..."
    ni "Will you please stop running? Both literally {i}and{/i} figuratively?"
    s "..."
    ni "Please?..."
    s "You really won’t leave?"
    ni "Of course not. Never."
    s "No matter what I become?"

    scene memorylane26
    with dissolve

    ni "No matter what you become."
    s "Why?..."
    ni "Because I’m a fucking idiot."
    ni "But I’m {i}your{/i} fucking idiot. And you’re my big, melancholic doofus. "
    ni "So let’s go be stupid together...far away from the places that make us hurt."
    ni "Let’s go somewhere quiet...and comfortable..."
    s "..."
    ni "{i}Let’s go home, Akira...{/i}"

    scene black
    with dissolve2

    "Akira..."
    "That’s...my name."
    "My name is Akira."
    "..."
    "I’m a good boy."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ nikilovesyou2 = True

    jump nikilovesyou3

label nikilovesyou3:
...
```

## Code that triggers this event

File: (install folder)\game\NikiEvents.rpy

Code:
```python
...
ni "You are..."
    ni "And still one step away from being snapped in half all these years later..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene nikitired9
    with dissolve2

    s "Where are we now?"
    ni "A hill."
    s "No deeper meaning to it this time? Not the hill where we first held hands or something to that effect?"
    ni "I think you fingered me here once. But other than that, I don’t think it’s particularly important. Nice view, though."
    s "Yeah...you can’t even see the wall from here."
    ni "Feels like it’s visible pretty much everywhere nowadays, doesn’t it? Makes you realize how trapped we are."
    s "I’m sure you have ways of getting out. You’re a famous pop-star and all. The world outside of Kumon-mi needs you."
    ni "There are other Niki Nakayamas in other parts of the world. I’m sure they’ll be fine. "
    ni "There’s somebody I’ve gotta stay here and look after anyway."
    s "You don’t {i}have{/i} to, Niki. I’ll get by on my-"
    ni "Hm? I’m talking about Noriko, obviously. You can go fuck yourself."
    s "Wow. Okay. Fuck you too, then."
    ni "Haha! I’m kidding, calm down. Noriko’s way more independent than you. She’ll be fine on her own."
    ni "I give her a lot of shit since she’s my sister, but I really do think she’ll wind up an amazing woman someday."
    s "I...think so too. She really amazes me sometimes."
    ni "I’d be surprised if she didn’t. She tries harder around you. Always has, always will. "
    ni "But I guess that’s to be expected when you’ve been filling the “cool older brother” role in her life ever since she was little. “Cool” being a word I’m using lightly, of course. {i}I{/i} don’t think you’re cool at all."
    s "Were we ever like that?"
    ni "Like what? Siblings?"
    s "Yeah."
    ni "Mmm...no. Not really."
    ni "There may have been a short period of time where I felt like an older sister to you, but it didn’t last long. Especially when I found out you were older than me."
    ni "We’ve always been close, though. Other people from the neighborhood would always tell me how weird it was when they’d see me walking around without you. Not sure if you ever got that."
    s "Not sure if I’d remember even if I did."
    ni "Yeah...there’s that too."
    s "..."
    ni "..."
    ni "You know, Noriko’s a lot older now. If you’re starting to feel a little differently about her-"
    s "Are we really doing this?"
    ni "Hold on. Let me finish."
    s "There’s no possible way that topic can end on a good note."
    ni "Why not? You’re not already messing around with her, are you?"
    s "Niki-"
    ni "Oh my God, relax! I’m kidding."
    ni "I’m just saying...she’s still in the process of learning how to see you as something other than a brother...but it’s okay if you start to see her as a woman, you know."
    ni "She’s not going to be a kid forever. She barely even copies me anymore. She’s her own person and deserves to be treated as more than my little sister."
    s "..."
    ni "I really love her. Like, a lot. "
    s "I can tell...I can’t wait to let her know you said that."
    ni "Please don’t. It’s still embarrassing even if it’s true. "
    s "Why bother telling me then? You know I’m just going to tease you about it."
    ni "{i}Because,{/i} {b}[[REDACTED ~ REPEATED USAGE OF PROHIBITED WORD]{/b}, you’re one of the few things in this world that can actually hurt her."
    ni "Even if she’s strong, she’s still growing. And since she’s in the process of finding herself, it means there are going to be a bunch of pieces scattered around that she needs to collect."
    ni "I’m sure some of those pieces are in your hands...and that’s why I feel like it’s my duty to tell you, as her sister and {i}not{/i} your psycho ex-girlfriend-"
    s "Don’t hurt her. Got it."
    ni "Not that. Well, yes that. But there’s something more as well."
    ni "{i}Help{/i} her. "
    ni "Even the most independent of us need a hand from time to time. Noriko’s amazing, but she’s no exception to that. And there are things you can do for her that I simply...can’t."
    ni "It sucks, but it’s the truth. "
    ni "The two of us have watched you forever. You’ve helped both of us learn all sorts of things about ourselves without even trying."
    ni "I’m old and decayed and set in my ways at this point, but she’s still young and full of life. And now that you’re back, she’s following your lead again."
    s "You’re 29, Niki. You’re not “decayed.”"
    ni "Maybe not {i}physically,{/i} but my brain is fried from having to balance all of this idol stuff with all of this {i}you{/i} stuff."
    s "Is my existence really causing you that much stress?"
    ni "Oh {i}fuck{/i} yeah. I found a grey hair last week and cried for twenty minutes. But that’s more on me than it is on you."
    ni "I just want you to be happy. That’s all. "
    ni "It doesn’t have to be {i}with me{/i} if you don’t want it to be."
    ni "I love you — and I don’t mean that in a romantic way this time. "
    ni "Please talk to me if there is ever anything you need. "
    s "Anything?"
    ni "If you ask me for a blowjob right now, I swear to God."
    s "I mean...if you’re offering..."
    ni "{b}[[REDACTED ~ FURTHER OFFENSES MAY RESULT IN UNEXPECTED SIDE EFFECTS. PROCEED WITH CAUTION.]...{/b}"
    s "I’m kidding."
    s "I’ll try and lean on you a little more, but don’t blame me if a lot of it sounds crazy because it most assuredly will."
    ni "I’ve been unhealthily obsessed with same boy for like two thirds of my life. I can handle crazy. "
    s "Well, I wouldn’t blame you if you couldn’t. A lot of what’s been happening to me lately isn’t really all that believable."
    ni "Only one way to find out, I guess."
    s "..."
    ni "..."
    ni "Thanks for calling me today. This is the most productive talk we’ve had ever since...you know."
    ni "Between all of the panic attacks and migraines you give me on a weekly basis, it’s easy to forget how nice the good times can feel."
    ni "And how so many of the best moments in my life have been little things like this — where the two of us just sit under a tree and...talk."
    s "..."
    ni "We’ve come a long way, haven’t we?"
    s "Seems like it."
    ni "Growing up kind of sucks, huh?"
    s "Everything sucks. Accepting that is the first step of obtaining true adulthood."
    ni "Said the perpetual manchild to the thirty-year old virgin."
    s "Hey, you’re not thirty yet. There’s still time."
    ni "Pfft. Yeah, sure. I’m starting to think I’ll die a virgin at this rate."
    s "Not if I have anything to do with it."

    $ renpy.end_replay()
    $ nikilovesyou1 = True

    jump nikilovesyou2
...
```