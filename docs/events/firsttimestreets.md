# Five Million Dollars (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 0



## Next events

* [Main: Not Even Me](./day21.md)

## Event properties

* Id: firsttimestreets
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets
* Triggered by path: streets->firsttimestreets

## Official wiki page

[Five Million Dollars](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimestreets&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label firsttimestreets:
    play music "streetnoise.mp3" fadein 3.0
    scene citystreets
    with dissolve

    "Not really knowing what else to do with this sudden abundance of free time, I decide to get a little more acquainted with the city."
    "I’m still getting used to this place, so I figure that the quicker I can actually figure out where I am, the quicker I can...I don't know. Do stuff?"
    "Plus, being out in the open gives me a better chance to run into someone than just sitting around in my room- and I believe that the easiest way to kill time is by distracting yourself with the presence of others."
    "Granted, that mindset gets a lot worse considering the only people I have any reason to spend time with right now are teenagers, but it doesn't really matter."
    "No one’s judging here. At least not to my knowledge."
    "And if I'm going to be making the most of my time in this...new world or whatever it is, dwelling on how anyone else feels will just hold me back."
    "If all of this is fake, I have nothing to fear."

    scene yumibridge1
    with fade

    "If all of this is fake, I am free to live as I please."
    "I walk up a flight of stairs onto a bridge overlooking the same part of town I have to go through in order to make it to school and take in the sights from a brand new perspective."
    "The light of the setting sun illuminates the body of a young girl and looks beautiful in the several seconds before she exercises {i}her{/i} free will to spit on a passing car."
    "She misses dramatically, but I'm sure she'll have many more chances."

    stop music fadeout 3.0

    q "{i}Hah...{/i}"

    "The mysterious girl lets out a sigh and stares off into the distance."
    "I wonder what it is that brought her here?"
    "I wonder why she isn't with anyone else?"

    q "..."

    "Something inside of me convinces me to call out."

    s "Hey."

    scene yumibridge2
    with dissolve
    play music "yumiska.mp3"

    y "The fuck do {i}you{/i} want?"

    "Apparently, that something is entirely unaware that not {i}everyone{/i} here unabashedly celebrates my existence."

    s "Nothing in particular. Just...looking around, I guess."

    scene yumibridge3
    with dissolve

    y "Uh-huh. Right."
    y "So you just happened to {i}look around{/i} exactly where I'm hanging out? Couldn't get on with your {i}adventure{/i} before annoying me first?"
    s "Apparently. But what's even more confusing than that is the abrupt appearance of ska music."

    scene yumibridge4
    with dissolve

    y "Ska...music? The fuck are you talking about?"
    y "This one of those fuckin' hidden camera shows or some shit? Cause I ain't cool with being filmed, dickweed."

    scene yumibridge2
    with dissolve

    y "The hell are you even sayin' hi to me for? What do you want?"
    s "Just thought you could use a little company if you're going to be hanging out up here. And since the two of us aren't doing anything-"
    y "What? You thought you'd just call out to a girl who's like a fifth of your age and that she'd get all excited to hang out with you or some shit?"
    y "Gimme a break. This ain't some fuckin' manga or whatever."
    s "First off, there is absolutely no way I'm even half as old as you think I am."
    s "And second, you should try to remember I'm responsible for your grades before you start doing things like insulting me and spitting on random cars."

    "I attempt to flex my newfound teacher muscle but, considering the type of girl Yumi appears to be, I doubt it will do anything."

    scene yumibridge5
    with dissolve

    y "Oh, suck my dick. You can't control where I spit. We ain't even in school right now. You've got no right to say shit like that to me."

    "Yup. Entirely ineffective."
    "Let's try a new strategy."

    s "You're just a lot cuter when you're not projectile-salivating on commuters."

    scene yumibridge6
    with dissolve

    y "Excuse me?! The fuck did you just say?!"
    y "I'll throw you off this bridge right now, fuckface!"

    "Strategy two is also a bust and I immediately question why I had to be reborn into a place like this instead of one where I am universally loved."

    s "If you want to try and lift me, go ahead. But I'm twice your size and I can't imagine you really want to touch me in the first place."
    y "Well...you're right about the touching part. But I ain't some dainty, little princess! I'm strong as shit!"
    s "I'm sure you are, Yumi. I'm very intimidated."
    y "I am! I ain't fuckin' around!"

    scene yumibridge7
    with dissolve

    if bonus == True:
        y "Wanna know what happened to the last guy who tried to fuck with me?"
        y "Kicked him so hard in the dick that I heard it fuckin' broke. You tryin' to be next?"
        s "I would prefer to keep my penis intact, thank you."
    else:
        y "This one time, I made this old man cry just by punching him."
        s "Why would you do that?"

    scene yumibridge2
    with dissolve

    if bonus == True:
        y "Say the word {i}penis{/i} around me again and I swear to fucking God I'll cut it off."
        s "You make even responding to you extremely difficult, you know."
    else:
        y "Because I am Yumi and punching old people is a character trait I have in the Patreon friendly version of the game."

    if totaldays > 21:
        "Does Yumi really have nothing better to do than just...hang out places like this during her free time?"
        "I mean...I'm doing the same right now. But still."
        "It was just the other day I found her in some random alley in the middle of the night. Now she's busy loitering here instead."
    else:
        "I still obviously don't know Yumi very well, but it's clear that she's not very fond of whoever inhabited this body last."
        "Frankly, it feels like even trying to get to know her at this point is a lost cause."

    s "So, is this just...where you hang out or something?"

    scene yumibridge8
    with dissolve

    y "If I say yes, are you going to fucking stalk me all the time? Cause I really don't wanna deal with that shit."
    s "Just...trying to learn more about one of my students."

    scene yumibridge4
    with dissolve

    y "Why? I barely even come to class."
    s "Hey, you don't have to come {i}at all{/i} if you don't want to. It doesn't make much of a difference to me."

    scene yumibridge9
    with dissolve

    y "Wait, what? You serious?"
    y "You ain't gonna, like...lecture me or some shit?"
    y "The fuck is goin' on with you today? This ain't normal."
    s "I guess you could say I've got a new lease on life. Come whenever you want or just...don't. It's up to you."
    s "I just want to know what you're busy doing when you're {i}not{/i} in school."

    scene yumibridge5
    with dissolve

    y "Well...nothing lately. Pretty much everybody I used to chill with is like, out in space or whatever now."

    "I assume she's talking about those Yakuza-looking guys my journal mentioned."

    y "We’d hang out at the arcade...shoot the shit...pick the locks on Pachinko machines for some free cash..."
    y "You know how it is."
    s "Wow, Pachinko machines. I can only imagine how feared you must be around here."

    scene yumibridge6
    with dissolve

    y "Yo! Cut it the fuck out! You don't know shit about what I've been through!"
    y "Can guarantee you the life I lead is a lot rougher than hangin’ out with your friggin’ {i}niece{/i} all day."

    scene yumibridge2
    with dissolve

    y "The hell is even up with that? You guys are way too fuckin' close for family."
    y "I bet she ain't even your real [niece] and is just some fuckin' mindslave you bought on the market or something."

    if bonus == True:
        s "I'm actually taking care of her because her parents died."
    else:
        s "She is a real accountant and has efficiently filed my taxes for years now."

    scene yumibridge5
    with dissolve

    y "...Yeah, well whatever. You’re still a fucking creep."
    s "You say that as if you're a completely respectable and normal person."

    scene yumibridge2
    with dissolve

    y "Least I don't spend my time borderline molesting girls on overpasses."
    s "I haven't even touched you."
    y "Awesome job. You want a fuckin' medal?"
    y "I ain't that abnormal, scumbag. I'm just not like the people you're used to bein' around."
    s "I'll say. You’re more aggressive than basically everyone else I know combined."
    y "So what? Like I said, you don’t know what I’ve been through."
    s "Probably on account of you refusing to tell me anything."

    scene yumibridge6
    with dissolve

    y "What, are you my dad now?! I don’t have to tell you shit!"

    "This really isn’t going anywhere..."

    scene yumibridge2
    with dissolve

    s "Listen, I’m not here to judge you or...try to discipline you or anything like that. I just thought-"

    scene yumibridge5
    with dissolve

    y "Thought what? We could be friends? Fat chance. I’d never willingly spend time with someone like you."
    s "Why, though? What did I ever do to you?"

    scene yumibridge2
    with dissolve

    y "The fuck do you mean {i}What did I ever do to you?!{/i}"
    y "You think I just up and forgot about all those fucking creepy ass detentions?! Get real!"

    "Detentions?"
    "Is she talking about something the old Sensei did?"

    s "Well, what can I do to make it up to you? I want to be on good terms."

    scene yumibridge5
    with dissolve

    y "I’ll need $5,000,000 in cash."
    s "US Dollars?"

    scene yumibridge2
    with dissolve

    y "There a problem with that?"
    s "No, hold on one sec."

    scene yumibridge9
    with dissolve

    y "Wait, do you really-"

    "I look through my wallet and pull out some cash."

    s "I have 600 yen."
    s "I know it's Japanese money, but-"

    scene yumibridge6
    with dissolve

    y "That’s not even close! Get the fuck out of here you creep!"
    s "Okay. I’ll just leave this here and-"

    if bonus == True:
        y "I SAID GO BEFORE I KICK YOU IN THE FUCKING BALLS!"
        s "Okay, okay. I’m leaving."
        s "But if you're not going to take my money-"

        scene yumibridge9
        with dissolve

        y "Wait, actually...no. Leave the money. I'm hungry."
        y "I ain't gonna just fuckin' forgive you or think you're cool or whatever, though."
        s "Then what exactly am I getting out of this deal?"
        y "The...opportunity to live another day?"
        s "..."
        y "..."
        s "Fair enough."

    else:
        y "I SAID GO BEFORE I HIDE CONDIMENTS IN YOUR POCKET."
        s "Okay, okay. I’m- wait, what?"
        y "YOU HEARD ME!"

    scene black
    with dissolve2

    "Yumi snatches the 600 yen out of my hands and storms away, leaving me alone on the bridge to soak up the remainder of the sunset and contemplate what my life has become."

    s "..."

    "As the day turns to night, I come to the depressing realization that this is very likely not the last time I'll wind up giving her money."

    $ renpy.end_replay()
    $ firsttimestreets = True
    $ yumi_love += 1

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdaynight

label streets2to4:
    play music "yumiska.mp3" fadein 3.0
    scene citystreets
    with dissolve

    "I decide to wander the streets again and wind up bumping into Yumi."
    "As always, she spends the bulk of our time berating me and throwing rocks at cars as they pass by."
    "Despite all of that, I still somehow feel closer to her."

    $ yumi_love += 1

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdaynight

label streets5:
...
```

## Code that triggers this event

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump satafternoonmenu
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
...
```