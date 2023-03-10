# Far From Fantasy (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 10

* Event [Imprinting](./ayanenew1.md) (Ayane) is completed)



## Next events

* [Ayane: Forever Yours](./ayanenew3.md)

## Event properties

* Id: ayanenew2
* Group: Ayane
* Triggered by label: dojo
* Triggered by branch label: dojo
* Triggered by path: dojo->ayanenew2

## Official wiki page

[Far From Fantasy](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanenew2&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label ayanenew2:
    scene ayanenewtwo1
    with fade
    play music "sakuya4.mp3"

    ay "Ahh! Seven losses in a row. I swear Miss Osaka, it’s like you’ve been doing this for your entire life or something."
    kin "I mean...yeah. If you were able to beat me at all, I’d probably just hang it up and open a flower shop or something."
    s "I somehow have a hard time picturing that."

    scene ayanenewtwo2
    with dissolve

    kin "Good. Keep me as far away from your fantasies as possible."

    "The three of us are relaxing in the dojo after a mildly eventful training session in which Ayane and I both gave it our all."

    kin "Oh, and if you go one more class without doing anything, I’m going to beat your ass without even giving you a warning first."

    "The three of us are relaxing in the dojo after a mildly eventful training session in which Ayane gave it her all."
    "Unfortunately, her all was not even close to enough and now she is extremely exhausted from overexerting herself- meaning her virginity will likely survive at least one more day while she recovers."
    "{i}If{/i} she recovers, that is. Because I’ve had this same exact inner monologue several times today, and each one has ended with another-"

    ay "One more round. I can do it this time. And...I won’t even make you give me a handicap again! That’s how confident I am!"

    scene ayanenewtwo3
    with dissolve

    kin "Fuck no. I’ve already spent pretty much the entire day with you. It’s not fair to the rest of the girls."
    kin "Besides, if I wind up hurting one of the richest girls in the entire city from pushing her too hard, your father will run this place into the ground."
    kin "I can’t afford a legal battle with...whatever the hell your dad’s name is."

    scene ayanenewtwo4
    with dissolve

    ay "Nice try, Miss Osaka. But I’ve already told you that Sensei is my dad."
    kin "That would be a little more believable if you stopped referring to him as “Sensei,” which, honestly, you shouldn’t be doing at all since {i}I{/i} am Sensei while we’re in here."
    s "What would I be called, then?"

    scene ayanenewtwo5
    with dissolve

    kin "Oh, I don’t know. Maybe your fucking {i}name?{/i}"
    ay "Can I ask you something, Miss Osaka?"

    scene ayanenewtwo6
    with dissolve

    kin "For the last time, no. I will not teach your chicken karate."
    ay "While I implore you to reconsider, that’s not what I was going to ask."
    ay "I just want to know why, if you know Sensei isn’t my real dad...you’re letting the two of us continue to show up together."
    kin "I care more about the fact that he does literally nothing here than the fact that he also happens to be your teacher."
    kin "If he even...is your teacher and that’s not just some weird pet name he’s making you refer to him as."
    s "What kind of person do you think I am?"

    scene ayanenewtwo7
    with dissolve

    kin "“Person” is generous. I don’t think you’ve earned the right to call yourself that yet."
    s "Okay, Ayane. It’s time to find a new instructor."
    kin "Good luck. Nobody in this city comes even close to the level I’m at. Which I guess {i}you{/i} don’t care about, but I’m sure Amamiya does."
    ay "To get back on track...he really {i}is{/i} my teacher. But we’ve also known each other for a really long time, so..."

    scene ayanenewtwo8
    with dissolve

    kin "I guess that kind of explains why you two act so “friendly” all the time, then."
    ay "Friendly? I mean...I don’t know if I’d call us {i}friends...{/i}"
    kin "There are definitely other words I’d use in place of that, but saying any of them out loud might make me throw up in my mouth and that would be...unprofessional or something."

    scene ayanenewtwo9
    with dissolve

    kin "To be frank, your entire relationship confuses the shit out of me. It’s just not really my place to get involved when, at least so far, it’s seemed {i}mostly{/i} innocent."
    kin "If Amamiya seemed genuinely creeped out or something, I’d be a lot more concerned. But, if anything, it kind of seems like {i}she’s{/i} the pursuer and not {i}Sensei{/i} over here."

    scene ayanenewtwo10
    with dissolve

    ay "That’s accurate. I’ve been pursuing Sensei for quite some time now as the two of us are destined to be together one day."
    kin "See, this is the kind of shit that I don’t want to hear because {i}now{/i} it’s a hell of a lot weirder."
    ay "The world needs to know."
    kin "Well, don’t lump me in with the rest of the world. I’m here to teach karate, not offer relationship counseling."
    s "Much like the flower shop job, you don’t really seem fit for that either."

    scene ayanenewtwo11
    with dissolve

    kin "Hey! I’ll have you know that I’ve been in a very successful relationship for quite some time now!"
    s "You mean with karate?"
    kin "No! I mean with a live, human being!"
    s "The fact that you had to specify “live” makes me a little wary of this alleged partner of yours."

    scene ayanenewtwo12
    with dissolve

    kin "Okay! Time for {i}your{/i} turn to spar, smartass."
    ay "I don’t think Sensei and I need counseling right now, but I’ll keep you in mind if we ever do, Miss Osaka."

    scene ayanenewtwo13
    with dissolve

    kin "Why? I literally just said that I’m not here to do stuff like that."
    ay "It’s just that you seem really happy most of the time, so I am assuming your relationship must be going pretty strong."

    scene ayanenewtwo14
    with dissolve

    kin "W-Well, it’s...I guess we {i}are{/i} pretty good together...but we’ve also known each other for a really long time and-"

    scene ayanenewtwo15
    with dissolve

    kin "Wait, why am I even talking about this with you two?!"
    ay "Because...we want to hear about your amazing and successful relationship?"
    kin "It’s amazing and successful! There you go! Conversation over!"

    scene ayanenewtwo16
    with dissolve

    kin "Now, pack your stuff and get ready to leave! We’ve only got ten minutes left of class and I still have to make up for all of the time everyone else lost during the seven ass-kickings I gave you."

    "So...the instructor is in a relationship."
    "I can’t say I saw that coming."
    "Which isn’t to say I don’t find her attractive or anything- she certainly has her own brand of...tomboyish charm."
    "She just doesn’t really seem like the type to fawn over someone based on first impressions alone."
    "But if every book on every shelf mirrored its cover, libraries would be a lot less exciting."
    "So I guess it’s good that people like her exist and remind us that not everything is always as it seems."

    ay "Sensei-"

    "Though, of course-"
    "Some things are."

    s "Yes, Ayane?"

    scene ayanenewtwo17
    with fade

    ay "Are you surprised to find out that Miss Osaka is dating somebody?"
    s "Yeah. It ruins my plan of asking her to marry me after beating her in a sparring match."
    ay "Normally, I’d worry after hearing something like that. But after going seven rounds with her today, I can pretty much confirm that there’s no reason to worry at all."
    s "Is she really that tough?"
    ay "Have you ever tried to punch a bird out of the sky before?"
    s "...No?"
    ay "Neither have I, but I imagine it’s kind of like that."
    ay "She’s super fast and pretty much impossible to hit. And when she hits {i}you,{/i} it’s way harder than you expect it to be."

    scene ayanenewtwo18
    with dissolve

    ay "I wonder if that’s what loving her is like as well?"
    s "I’m pretty sure that wasn’t meant to be a sexual innuendo, but I’m going to imagine it as one."
    ay "I mean, I guess that would be part of it. But yeah, I’m talking more along the lines of just...having something that {i}real,{/i} you know?"
    s "..."
    ay "Do you..."

    "Don’t ask it, Ayane."

    ay "Do you think..."
    ay "Do you think that we’ll ever have something like that?"
    s "..."
    ay "..."

    "Of course not."
    "All it would take is one look at us to know that something like that isn’t possible."
    "And, on the off chance it ever would be, it would take us years to get there."
    "Time is not known to be kind to the segmented nature of unblossomed, unrequited love."
    "And so there is no way that this girl and I will ever be happy together."
    "The same goes for everyone else who falls as deep into this hole as her."
    "I am not built for love-"
    "But I was built by someone somewhere."
    "So I will try on new goals as if they are outfits and peer into the glass, hoping that whatever is reflected back at me looks closer to something with purpose."
    "Or, at the very least-"
    "Something not far from fantasy."

    s "Ayane-"

    scene ayanenewtwo19
    with dissolve

    ay "On second thought...don’t answer that, Sensei."
    ay "It was a stupid question."
    s "It wasn’t a stupid question, it-"
    ay "No, it was."
    ay "And honestly, it’s stupid that I asked in the first place since I’ve known from the beginning that we could never have anything like that."
    ay "It’s one of the many unfortunate side effects of falling for someone the world doesn’t want you with."
    s "..."

    scene ayanenewtwo20
    with dissolve

    ay "But...I’m okay with that."
    ay "And sure, we might not ever have something {i}amazing and successful{/i} by everyday standards, but that doesn’t mean it won’t be amazing and successful {i}to us.{/i}"
    ay "Isn’t that what really matters? That we’re happy?"
    s "Do you actually think you’d be happy with me, Ayane?"

    scene ayanenewtwo21
    with dissolve

    ay "Yes."
    s "You didn’t even think-"
    ay "I don’t have to think, Sensei."
    ay "There are some things in life that you just know."
    ay "This is one of those things."

    scene ayanenewtwo22
    with dissolve

    ay "So, you can deny it all you want or think to yourself that there’s no real way for us to be happy, but I know that I’m happier than I’ve ever been just getting to say these things to you."
    ay "And I know that there’s next to nothing you can do to change that, whether you want to or not."

    scene ayanenewtwo23
    with dissolve

    ay "I’m kind of like a disease you’ll have to live with for the rest of your life."
    s "That is a significantly more grotesque note than I expected that mini-monologue to end on."
    ay "Same here, but I really couldn’t think of any other way to put it."
    ay "Things will never be normal between us. And very few people will ever accept it because its face value isn’t covered up by the masks they expect us to wear."
    ay "But one day, the two of us will be standing in front of a mirror together."
    ay "Your hands will either be on my shoulders or my belly {size=-15}assuming that I’m pregnant, which I probably will be-{/size}"
    ay "And what’s reflected back at us will be something with purpose. Something no one thought would ever work out."
    s "Ayane-"
    ay "I’ll make it work, Sensei."
    ay "I promise I’ll make it work."
    s "..."
    ay "..."

    scene black
    with dissolve2

    "I’m not sure how, but Ayane managed to tap into the same worries I had just moments ago when contemplating the unlikely future the two of us may have."
    "And while it would be easy to chalk that strain of hivemind up to the fact that she’s known me for years, I can’t help but feel like there’s a little more to it than that."
    "Love as pure as hers has no right to exist in the world-"
    "But neither do I."
    "And if the fact that I can wake up and step into a world that doesn’t want me is a symbol that things in life may happen without a reason, I have no right to say what can or can’t exist."
    "Not that I ever did in the first place, it’s just-"
    "I’m not built for love."
    "But that doesn’t mean no one else was."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanenew2 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label ayanenew3:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
    if ayane_love >= 10 and dojo10 == False:
        jump dojo10
    if ayane_love >= 10 and ayanenew1 == True and ayanenew2 == False:
        jump ayanenew2
...
```