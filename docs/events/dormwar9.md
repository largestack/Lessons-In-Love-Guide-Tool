# Why Now?
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar9&go=Go)


Part of event chain [What a Wonderful World](./ayanelust15.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwar9
* Group: Main
* Triggered by label: ayanelust15

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label dormwar9:
    scene frown
    with dissolve3
    play music "starvingtodeathoutofreachofthesun.mp3"

    "It’s easy to smile when you’re feeling sad, and it’s easy to frown when you’re feeling happy."
    "It’s actually rather easy to combine any two contradictory emotions and expressions if you put your mind to it."
    "The only issue is that our minds are so full of toxic sludge and faded photographs we call “memories,” for lack of a better term, to really give us the space we need to take control."
    "To dig our fingers straight through our skulls and start sloshing around beautiful brain matter as if it’s a bowl of ground beef that we’re mixing and preparing for dinner."
    "Why now?"

    if ayanelust15 == False:
        "Why, in the midst of what should be one of the happiest times I’ve had, does it suddenly feel impossible to control anything at all?"
        "My hands are no strangers to meat. "
        "I have done my fair share of sloshing."
    else:
        "Is it because I watched one more petal fall off of one of the tallest sunflowers I have seen just moments ago?"

        if bonus == True:
            "Is it because even when there was a girl in my arms, crying to the point of hyperventilation, I couldn’t help but focus on an innate desire to mop my cum off the floor so it does not stain the carpet?"

        "You do not understand. "
        "You really don’t."

    "Why now?"
    "I look in the mirror and attempt to contort my face into something unrecognizable, but what I see is no reflection of myself."
    "It’s a pair of disembodied hands, sifting through the hair of someone who does not exist."
    "They look soft."
    "They smell like cherry blossoms."

    play sound "static.mp3"
    scene smile with flash
    scene frown with flash
    scene smile with flash
    scene frown with flash
    scene smile with flash
    scene frown with flash
    scene handsareweird with flash
    stop sound

    "I place my hand against the mirror and hope to feel one of the two on the other side."
    "Ideally, I would like to feel both."
    "But I feel nothing."
    "I guess that isn’t much of a surprise though, considering that feeling nothing has essentially become the norm for me."
    "But maybe one day."

    if bonus == True:
        "Maybe one day, when either I get recycled into some other person’s body and have nothing else to do but crawl into the lives of another set of [young_girls]-"
        "Or when the world stops resetting (Doubtful, but you’d have to ask Maya)-"
    else:
        "Maybe one day, when autonomous driving becomes more commonplace or something like that."

    "Maybe then."

    play sound "glass.mp3"
    scene handsareweird2

    "I punch the mirror and cut my hand. Blood spills out all over the bathroom."
    "I run it under hot water for 23 seconds and discover that there is no cut and no blood."
    "There is nothing."

    scene black

    "I need to go for a walk."

    "………"
    "……"
    "…"

    scene likemotherlikedaughter1
    with dissolve2

    "I stumble upon Yuki after-"
    "Actually, I’m not really sure how long I’ve been out here."
    "Ten minutes? Thirty? An hour?"
    "Hell, maybe I’ve gone really overboard and I’ve been aimlessly walking around this area for years, always slightly out of reach of everyone."
    "Maybe I’m a missing person and Yuki is about to get a sweet reward."
    "I call out to her, as today is her lucky day."

    s "Yuki Yamaguchi."

    scene likemotherlikedaughter2
    with dissolve

    yu "Why the fuck are you using my full name all of a sudden?"
    yu "Actually, the hell are you even doing around here? Not a place I’ve ever seen you before."

    if bonus == True:
        s "I’m currently chaperoning twenty girls in a battle for my body."
    else:
        s "I’m the huggy boy. I go wherever there are hugs."

    yu "And I’m the richest girl in fucking Kumon-mi."
    s "That can’t be true because the richest girl in Kumon-mi is actually part of the twenty that-"

    scene likemotherlikedaughter3
    with dissolve

    yu "If you’re gonna flirt with me, can you at least do it in like a...less fucking weird way or something? Because I have no idea what’s going on."
    yu "And by the looks of it, neither do you."
    yu "You on something right now?"
    s "Me? Not that I’m aware of."
    s "Unless one of the other girls snuck in and-"

    if bonus == True:
        s "Actually, how long does being roofied last?"
        yu "Jesus, you’re the worst fucking chaperone in the world."
        s "No, not for them. For me. "
        yu "You roofied yourself? The fuck is your problem?"
        s "No, I just-"
    else:
        s "Actually, how long do sleeping potions last?"
        yu "Uhh...what?"

    s "Actually, forget all that. What are you doing out here?"
    yu "Fuck’s it look like I’m doing? I’m smoking."
    s "Yes, but it’s also the middle of the night. Shouldn’t you be at home or something?"
    yu "Mind your own fucking business. No point in asking me a question in return if you’re not even gonna answer mine."
    s "I really wasn’t kidding about the chaperone thing. "
    s "I’m pretty sure there’s like, a pillow fight or something going on as we speak."
    s "We’re at a hotel not far from here. I think."
    s "I may or may not be lost right now."

    scene likemotherlikedaughter4
    with dissolve

    yu "You’re a weird fucking guy."
    s "That is certainly one way to describe me."
    s "What about you, then? Have I proven myself worthy enough to ask you a question in return?"

    scene likemotherlikedaughter5
    with dissolve

    yu "Since you apparently {i}have{/i} to fucking know...I’m coming back from some fuckin’ NA thing."
    yu "Don’t really do shit like that often, but it’s not like I have anything else to do lately."

    if bonus == True:
        s "Do you...also want to chaperone twenty girls in their quest for my body?"
    else:
        s "Do you want to come back to the hotel with me and try to convince all of those bloodthirsty women that I should not be treated as some sort of prize?"

    scene likemotherlikedaughter6
    with dissolve

    yu "Ha! Yeah, because my track record of babysitting is one of the best around. Sure thing. "
    s "Yumi’s actually there, you know."

    scene likemotherlikedaughter7
    with dissolve

    if bonus == True:
        yu "This you finally admitting that you’re fucking my daughter?"
        s "What? No. But I guess I don’t blame you for interpreting it that way."
        yu "How else would I fuckin' interpret that?"
        yu "And what do you mean Yumi’s there? "
    else:
        yu "This you finally admitting that you’re hugging my daughter?"
        s "What? No. But I guess I don’t blame you for interpreting it that way."
        yu "But you're the huggy boy. You go where the hugs are."
        yu "And what do you mean Yumi’s there? "

    s "I mean that she is one of the twenty girls at the hotel right now."
    yu "{i}My{/i} Yumi is at a hotel with nineteen other girls? They’re not a biker gang, are they?"
    s "Do biker gangs paint each other’s nails and play truth or dare?"
    yu "Sometimes, sure. We had girls like that."
    s "Your backstory just got a lot more interesting then."

    scene likemotherlikedaughter8
    with dissolve

    yu "I obviously wasn’t one of ‘em. But yeah, there were definitely a bunch of girls who were into that feminine shit."
    yu "If they ain’t a fuckin’ biker gang or whatever, the hell’s goin’ on over there? It ain’t like a normal slumber party or some shit, is it?"
    s "It kind of is. "
    s "The second floor of their dorm just filled up, so all of the girls are holding one-on-one competitions to see who’s better at certain things."
    yu "Uh-huh. And what’s Yumi “competing” in? Girl’s got no talent at all. Just like her mom."
    yu "Well, except for that whole business management thing she’s got goin’ on now."
    s "She sells stolen TVs, Yuki. That’s hardly a business."
    yu "She have customers?"
    s "Well, selling them would imply that she does. But it can’t be very many and-"
    yu "Well then that’s a fuckin’ business. Now tell me, what’s she up to? What’s her contest?"
    s "Yumi’s contest is..."
    s "Well, let’s just say that all she needs to do in order to win is...cooperate."
    yu "So it’s like a fuckin’ teamwork thing or some shit?"
    s "Sure. Why not?"
    s "Also, she’s up against Io."

    scene likemotherlikedaughter9
    with dissolve

    yu "Wait, you pullin’ my leg right now?"
    yu "Two of them aren’t friends, are they?"
    s "They are quite the opposite. "
    s "In fact, neither of them really talk to anybody other than their roommates."
    yu "Wow."
    yu "Small fuckin’ world, huh?"
    yu "I obviously ain’t one to brag about my daughter and shit, but if that’s all the competition is, Yumi is going to win."
    yu "Not a doubt in my mind."
    s "Why do you say that?"

    scene likemotherlikedaughter10
    with dissolve

    yu "She ever say anything about when she was younger?"
    yu "Apart from all the shit about me, I mean."
    s "Not really. Yumi doesn’t open up much."
    yu "Course she doesn’t."
    yu "She liked playin’ a lot when she was little. "
    yu "Thing is, we didn’t really live in a place where it was okay for kids to hang around, so she didn’t see too many of ‘em and always had to play by herself."
    yu "Don’t know how much she’s changed since then, but I’d be willing to bet fucking money that she just wants to be included in something."
    s "If that’s the case, she should probably stop pushing people away when they try to include her."

    scene likemotherlikedaughter11
    with dissolve

    yu "Do you like dudes?"
    s "..."

    if bonus == True:
        s "...Yuki, what the fuck?"
    else:
        "I look away nervously."

    yu "Answer honestly. I don’t have a fuckin’ problem with it if you do."

    if bonus == True:
        s "I don't. And what does that even have to do with anything?"
        yu "Say that you {i}did{/i} like dudes. Just a big ole fuckin' cock jockey-"
        s "Yuki, what is happening right now?"
    else:
        "I look away even more nervously."

        s "L-L-L-L-L-L-L-LETSTALKABOUTSOMETHINGELSE!"

    yu "I’m not fuckin’ finished. Hold on a sec."

    if bonus == True:
        yu "Say that you {i}did{/i} actually like dudes, but everyone knew you as the womanizing daughter fucker you actually are."
    else:
        yu "Say that you {i}did{/i} actually like dudes, but everyone knew you as the womanizing daughter hugger you actually are."
        s "Hey, I may hug daughters, but I am NOT a womanizer."

    yu "Then one dude shows up to a party you’re at with a bunch of those daughters and is like, “Hey man. You down?”"
    yu "Would you be like “Yeah, let’s go,” or would you take a look at your fuckin’ surroundings and think that it might just be better to hide who you really are?"
    s "Now, I’m by no means a champion of morality, but it seems a little wrong to be comparing sexual preferences to your daughter not wanting to talk to people."

    if bonus == True:
        yu "Probably not “politically correct” or whatever bullshit kids are saying nowadays, but it sounds about right to me."
    else:
        yu "Probably not “politically correct” or whatever bullshit people are saying nowadays, but it sounds about right to me."

    yu "Point is, sometimes people don’t take what they actually want when it’s offered to ‘em...because there’s a lot more to it than that."
    yu "It’s one thing to want shit, but to want shit and not care about what other people think about you isn’t somethin’ most can do. "
    s "So, basically, Yumi won’t talk to any of the other girls because she’s already established herself as the “Girl who doesn’t talk to other girls?”"
    yu "Yeah. Pretty much sums up what I’m saying."

    if bonus == True:
        s "Teenagers are fucking exhausting."
    else:
        s "(Catchphrase)"

    yu "Is what it is, man."
    yu "She’ll probably start comin’ out of her shell in due time if she’s anything like she used to be way back when."
    yu "As for Io..."
    yu "I don’t know."
    s "They’re both enigmas."
    yu "Nah. They’re just [teenager]s."
    yu "Figured you’d have realized that by now."

    "Of course I’ve realized that..."
    "In fact, pretty much everything Yuki said is something I’ve already filtered through the sloshy brain meat inside of my skull. "
    "And I add “pretty much” to that because I don’t normally include the part with all of the homosexuality."
    "But yes, of course they’re not real enigmas."
    "Not most of them at least."
    "They’re just girls trying to figure out who they are and where they belong. "

    if bonus == True:
        "And I’m just a guy following closely behind them on some wooded trail, waiting for them to get so lost that I can do what I please to them without the fear of being discovered."
    else:
        "And I’m just a guy following closely behind them on some wooded trail, making sure they make it home without getting hurt."

    "Praise be."

    scene likemotherlikedaughter12
    with dissolve

    yu "Anyway, I should probably get going."
    yu "Have an actual fuckin’ “job interview” in the morning."
    s "You? Working?"
    yu "Crazy, right?"
    yu "Pay is basically shit, but it’s not like I’ve got any experience to my name or whatever."
    yu "Kinda just thankful somebody is willing to even interview me despite that."
    s "Am I allowed to ask what the job is or will you hit me?"
    yu "Why the fuck would I hit you for askin’ that? It’s fine."
    yu "Just some random ass bar. Not really anything to write home about."
    yu "Stopped in the other day and apparently it’s going under or some shit. Got to talkin’ with the owner and, thought...“You know what? Fuck it.”"
    yu "So...here’s hopin’ I don’t fuckin' ruin everything tomorrow."
    s "…"
    s "It really is a small world."

    scene likemotherlikedaughter11
    with dissolve

    yu "You know it."

    if bonus == True:
        yu "Have fun with your fuckin’ giant orgy or whatever. Make sure you wear a rubber when it’s my daughter’s turn."
    else:
        yu "Have fun with your contest or whatever. Tell Yumi I'm ready for a big hug whenever she is."

    s "You are such a horrible mother."
    yu "And you’re a fuckin’ horrible teacher, so I don’t wanna hear it."
    yu "I’ll catch you later."
    s "Yeah."
    s "Goodnight, Yuki."

    scene nightsky
    with dissolve

    "I slide my phone (Which is now on the brink of death) out of my pocket and quickly punch in the name of our hotel so I can get an idea of where to go in order to get back."
    "I’m able to do it seconds before the phone breathes its last electrical breath and find myself walking back amidst one of the quietest winter nights I’ve ever experienced moments later."
    "And to think that, just hours ago, things were so loud that I wasn’t sure if I’d ever be able to hear again."
    "I head back toward the origin of sound regardless."
    "For silence can be nice at times, but painful when you remember everything that needs to be missing in order to achieve it."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene likemotherlikedaughter13
    with dissolve

    no "Ooooooh, so you were out {i}here.{/i}"
    no "And to think that everyone assumed you’d just gone to sleep early."
    s "Weren’t you two in your pajamas...recently?"

    "I still have no idea how long it’s been that I’ve been out here as I didn’t even think about checking the time on my phone when I opened my GPS app."

    f "A few of us couldn’t sleep, so...we all decided to go for a walk. "
    s "All? There are only two of you."
    no "Otoha and Rin are on their way to the convenience store together to see if they sell Pokemon cards."
    s "That is both adorable and slightly depressing at the same time."
    no "Depressing because Otoha is a creature who is immune to romance and Rin is falling deeper into unrequited love with each passing moment?"
    s "I meant depressing because they’re too old to be playing with cards, but yes. That too."
    f "I...don’t think they’re too old for that..."
    f "It’s actually...a really common hobby for girls our age."

    if bonus == True:
        no "Futaba has sex dreams about Mr. Mime. True story."
    else:
        no "Futaba has dreams about Mr. Mime. True story."

    scene likemotherlikedaughter14
    with dissolve

    f "I do not! You’re the one who has dreams like that! Stop making me out to be the weird one!"
    no "Oh, please. It was {i}one{/i} dream. That hardly makes me weird."
    s "I have no idea who this Mr. Mime person is, but I’m interested in hearing about this dream."

    scene likemotherlikedaughter15
    with dissolve

    f "You really shouldn’t be. It’s...quite disturbing."

    no "I have no problem explaining the dream to you in vivid detail, but I would like something in return."
    s "And do you know what you would want?"
    no "Yes. I want to see your room."

    scene likemotherlikedaughter16
    with dissolve

    f "Wait, Nodoka. What are you doing?"
    no "I want to see if it’s true."
    s "See if what’s true?"
    f "She’s just...making things up. She does that because...she’s an experienced writer and-"
    no "More specifically, I want to see what you and my dear friend here would {i}get up{/i} to in said room assuming that I, Nodoka Nagasawa, was not present at all."

    scene likemotherlikedaughter14
    with dissolve

    f "Nodoka! Why?! "

    if bonus == False:
        s "Y-Yeah, Nodoka! It's not like the two of us would...h-h-hug or anything..."

    no "Futaba, my sweet girl. My sweet, sweet girl. My sweet, beautiful girl with gigantic breasts."

    if bonus == True:
        no "Do you not understand why I struggle to believe the news of your apparent...experiments with our dear teacher?"
        no "It was just the other day that we were frolicking through a field of flowers, holding hands and-"
        f "Even if it wasn’t true, why would you just bring it up like that?!"
        no "Because it’s funny {i}and{/i} sexual and those are two of my most important character traits."
        no "So either it’s not true and we all have a laugh about it, or it {i}is{/i} true and I get to watch my teacher copulate with my best friend. Win win."
        s "…"
    else:
        no "You do not need to hide your hugs from me."

    s "Futaba...did you tell Nodoka about us?"

    scene likemotherlikedaughter17
    with dissolve

    f "I...may have said...some things. "
    f "But I had no idea she was going to immediately blurt them out to you."
    no "I have only known about this for ten whole minutes, but they have been ten of the most exciting minutes of my life if any of it is true."
    no "I do acknowledge that this may still be some elaborate ploy to toy with me, but I am the official dorm wars knowledge champion until further notice, so I’m kind of a big deal."
    no "Not really one to be so easily {i}tricked{/i}, I mean."
    s "You’re not going to say anything about this to anyone else, are you?"

    scene likemotherlikedaughter18
    with dissolve

    no "Sensei, I’m going to let you in on a little secret."
    no "I kind of love the girl sitting next to me right now. And I would never do anything that I believe would even come close to hurting her."
    no "And, should I happen to hurt her accidentally, I would carve out my insides with a wakizashi."
    no "So, no. I’m not going to tell anyone else."

    scene likemotherlikedaughter19
    with dissolve

    no "Besides, this isn’t something I’d believe without seeing with my own eyes. "

    if bonus == True:
        no "Futaba is a delicate flower who will not do anything sexual until she is married, and I am sure this is all just a big, poorly executed prank."
    else:
        no "Futaba always tries to run away when {i}I{/i} hug her and I want to see if it's just a reflex of hers or more of a personal issue with me directly."

    no "Also, the girls in my room were so loud that it made reading near impossible. And if your room is any quieter, I’d like to utilize it for some good ole word absorption."
    f "…"
    s "…"
    s "And your thoughts on this, Futaba?"
    f "I think that she should stop calling reading “word absorption.”"
    s "You know what I’m talking about."

    scene likemotherlikedaughter20
    with dissolve

    f "I...am a little curious about your room."
    f "And going there doesn’t automatically mean that...you know."

    if bonus == True:
        s "I have no idea what you mean by that, Futaba. You and I have never done anything sexual before. Why would you lie about this to Nodoka?"
    else:
        s "NO, FUTABA. NO HUGS!"

    scene likemotherlikedaughter21
    with dissolve

    f "H-Hey! Now that she already knows, there’s really no point in-"

    if bonus == True:
        s "In fact, while I’m at it, I’ve never done anything sexual with anyone ever."
        s "I’m a total virgin who’s never even seen boobs before."
        s "Now...if only there were girls around who’d be willing to show me them..."
        no "Oh dear. Perhaps we {i}could{/i} find a janitor’s closet somewhere in the hotel..."
        f "No! We’re going to Sensei’s room now before anyone else hears us talking about this!"
    else:
        s "NOOOOOOOOOOO!!!!!!!"

    scene black
    with dissolve2

    "Futaba quickly stands up and grabs Nodoka by the wrist, dragging her up as well."
    "She must already know my room number as she immediately begins to lead the way there."
    "Nodoka looks back every few seconds to wink at me and...I really can’t tell if it’s because of the janitor’s closet thing, if she believes what I’ve done with Futaba, or if she {i}doesn’t{/i} believe anything at all."
    "It could really mean anything with that girl."

    play sound "dooropen.mp3"

    "Eventually, we make it to my door and I grab the key out of my pocket, insanely curious about whatever is about to happen."

    if futaba_lust >= 15 and nodokadorm5 == True:
        $ renpy.end_replay()
        $ dormwar9 = True
        stop music fadeout 5.0
        "………"
        "……"
        "…"
        jump futabalust15
    else:
        "Unfortunately, nothing exciting happens at all."
        "The two of them take a look around, say some things about how nice the furniture is, and then remove books from their respective bags and start reading them, paying no mind to me at all."
        "Things have quieted down, and I’m reminded once more of how much I hate silence sometimes."
        "And how I wish to fill the room with new, exciting noises."
        "Noises that could be heard all the way down the hall."
        "I lie on the bed and close my eyes, not minding whether or not I fall asleep with the local bookworms present."
        "..."
        "And that is exactly what happens."

        $ renpy.end_replay()
        $ dormwar9 = True
        $ futabalust15skip = True
        stop music fadeout 5.0

        "………"
        "……"
        "…"

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
        else:
            "ERROR ADVANCING TO SUNDAY"

        jump dormwar10

label dormwar10:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
ay "…"
    ki "…"
    s "…"

    "But it doesn’t look like I can get out of this without making a decision, so..."

    menu:
        "Kirin wins":
            $ kirinbjcontest = True
            $ dorm2warpoints += 1

            s "…"
            s "The winner of this contest is Kirin."

            scene ayanekirinfuntime33
            with dissolve2

            ay "Hahaha...of course it is..."
            ay "Of course I didn’t win when I...spent half of the contest crying..."
            ki "I..."
            ki "I actually won?"
            s "You won."
            ki "…"
            ki "Are you fucking serious right now?"
            s "...What?"
            ki "I forced Ayane to do this, tormented her the entire time, and you’re going to make me the winner on top of that and just...add fucking insult to injury?"
            ay "Sensei is...an unbiased judge...and you were the one who...technically ended things, so..."
            ki "I can’t fucking believe you."
            ki "I’m not even flattered. I’m just shocked that you could be {i}this{/i} heartless."
            ki "Do you even like Ayane?"
            s "Of course I do. I just think that in this particular contest, you-"
            ki "The contest was an excuse, you dick."
            ki "Like, I’m obviously still going to take the point because I want you in our room. But...wow."

        "Ayane wins":
            $ ayanebjcontest = True
            $ dorm1warpoints += 1

            s "The winner of this contest..."
            s "Is Ayane."

            scene ayanekirinfuntime35
            with dissolve

            ki "Hey, congrats. Good job following through with the whole thing and not hiding in the bathroom."
            ay "I’m...glad you chose me, but...I never really saw this as a contest in the first place."
            ki "Okay, yeah yeah. No one asked for a victory speech. Just take your dorm war points and go buy yourself a fucking cookie or something."
            s "Are you okay now, Ayane?"
            ay "Yes. Getting a point added to my team’s score in a friendly competition makes the repeated sexual blackmail so very worth it."
            ay "I am not okay. "
            ay "I’m not okay at all."
            ki "Such great sportsmanship. That’s a real martial artist for you."
            s "Kirin, just leave."
            ki "You guys going for a second round? Can I stay and watch?"
            s "Just go, Kirin. Really."
            ki "Fine. I guess this is enough to satisfy me."

    scene ayanekirinfuntime34
    with dissolve

    ay "So...does that mean this is finally all over?"
    ay "And you won’t...make us do things like this anymore?"
    ki "I don’t know. Maybe? Really depends on how I feel, I guess."
    ki "I’m kinda done with this now, though. So I’m going to clean my face up and hang out with Noriko or something."
    ay "And I’ll..."
    ay "I’d like to stay and talk with Sensei a little more."
    ki "Of course you would. "

    scene black
    with dissolve2

    play sound "dooropen.mp3"

    ki "Night, you two."
    ki "Your secret lives another day."

    "Ayane collapses into my arms the second Kirin leaves the room."
    "She cries for so long that my semen dries into her hair and she needs to take a shower to get it out."
    "And when she gets out of the shower, she cries some more."
    "And then she goes back to her room."
    "But somewhere in the middle of all of those things, she finds the time to reassure me that she’s going to be okay."
    "And that she doesn’t fault me at all for the things I did to her “friend” while she was away."
    "She walks over to the door."
    "She stands up tall and straightens out her clothes."
    "And then turns to me and smiles before leaving the room."

    $ ayane_lust += 3
    $ kirin_lust += 3
    $ renpy.end_replay()
    $ ayanelust15 = True
    stop music fadeout 7.0

    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
    "………"
    "……"
    "…"

    jump dormwar9
...
```