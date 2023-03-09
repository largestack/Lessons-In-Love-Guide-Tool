# Another Man's Treasure
Io event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bathhouse20part2&go=Go)


Part of event chain [One Man's Trash](./bathhouse20.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Uta: Veins and the Circulatory System](./utamaid20.md)

## Event properties
* ID: bathhouse20part2
* Group: Io
* Triggered by label: bathhouse20

## Event code
File: \game\IoEvents.rpy
Code:
```python
...
label bathhouse20part2:
    if _in_replay:
        play music "io.mp3"

    scene clearnightsky
    with dissolve2

    "It’s dark by the time we go outside."
    "I didn’t realize how much time had passed...but I guess it always gets dark a little earlier in the winter."
    "Kumon-mi, despite being incredibly different from everywhere else in more ways than you can count, is no exception to that."
    "I silently follow Io as she rounds the corner and heads for whatever bench she normally spends her breaks on, noticing with each hundred feet or so that her disappointment is slowly fading."
    "Like she’s hitting a different stage of life each time she passes under a streetlight, each one bringing with it a brand new, but instinctively reserved outlook on life as we know it."
    "The word “caterpillar” comes to mind."
    "But it’s not the first time I’ve thought of her as something like that."
    "Something absolutely worthless, but with so much room to grow and so much left to give, if she ever elects to give anything to anyone."
    "Anyone other than me, I mean."
    "I’ve already managed to win her over simply by being in the right place at the right time."
    "But who’s to say that our encounter was the last place or the last time."
    "For all I know, someone else could swoop in and take her away the second they seem more valuable or even make {i}her{/i} seem more valuable."
    "The two of us have a lot in common."
    "We’ve accepted our worthlessness and rely on others to make up for what we can’t cultivate within ourselves."
    "Our blood is poisoned and our minds are tainted."
    "And while Io has an entire pharmacy’s worth of pills at her bedside to counteract this-"
    "I have these thoughts."
    "But that’s all I need."
    "Because everything is going to work out."
    "Because life will repeat itself and mistakes will correct themselves."
    "Either that or I disappear."
    "I can’t lose."
    "I’d definitely prefer not disappearing, though."
    "And for Io’s sake, temporary or not, I’m going to continue hoping that doesn’t happen."

    i "Here."

    scene iobench1
    with dissolve2

    "Io props herself onto the edge of a park bench, dragging her knees to her chest and shivering as a gust of wind comes to greet us."
    "I sit next to her and place my {s}unnamed{/s} wooden robot down on the opposite end."
    "A minute or two goes by without any dialogue...but this is fine."
    "I expected this."
    "Any minute now, she’ll revert back to her instinctive self-deprecation."

    i "I really suck, don’t I?"

    "See?"

    s "Why? Because you had a sensible reaction to someone insulting something you worked really hard on?"

    scene iobench2
    with dissolve

    i "Because I dragged you down with me."
    i "Those girls are going to remember this. "
    i "You're probably going to have to explain yourself to them now."
    i "All I did was create more problems for you."
    i "Which means I suck."
    s "I don’t see it as much of a problem. "

    if bonus == True:
        s "Noriko will probably get jealous and Kirin will probably just accuse me of sleeping with you or something."
    else:
        s "Noriko will probably get jealous and Kirin will probably just try to get me to watch Seinfeld or something."

    scene iobench3
    with dissolve

    i "Yeah..."
    i "Not going to lie, that sounds like a pretty big problem."
    s "I think it would be more of a problem for you than it would be for me. No one really thinks highly of me to begin with."
    i "I think highly of you."
    i "It’s not a problem for me since I don’t talk to any of them. They can think whatever they want."
    s "Yeah, I guess it’s kind of hard to be ostracized when you’re already a wallflower."

    scene iobench4
    with dissolve

    i "I suck at being a wallflower too. I couldn’t even win the wallflower contest thing for the dorm war."
    s "I’m pretty sure not winning makes you a {i}better{/i} wallflower."
    i "Hmm...maybe."
    i "Yumi seems to be actively hated, though. While everyone probably looks at me and thinks, “Oh, right. She’s in this class.”"
    i "So I guess I’m in my own category when you look at things that way."
    s "You’re definitely one of a kind. I’ll give you that."
    i "You know..."
    i "You know, I'm sorry for saying this again out of what seems like nowhere..."
    i "But I really think you should break up with that gyaru girl."
    s "The one that you’re well aware I’m not actually dating?"
    i "I’m not well aware of that. I still think it’s technically possible that you’re lying."
    s "Well, I’m not really sure what else I can do to prove to you that I’m not."
    i "You coooooould...start dating me instead?"
    i "I think that might help prove it."
    s "Two minutes ago, you were talking about how just following you would create problems for me...and now you’re suggesting we start dating."
    i "Because I know you won't want to."
    s "And you would?"
    s "I’ve gotta say, you don’t really seem like the type to start any sort of “official” relationship with anyone."

    scene iobench5
    with dissolve

    i "It’s not really something I’ve ever wanted...that’s true."
    i "But I think it would be kind of nice if it were you."
    s "…"
    i "It’d be really hard, though."
    s "Why’s that?"
    i "Because I’d cry a lot. "
    i "And probably freak out on you over a bunch of different things that aren’t your fault or that you can’t control."
    i "Oh, and I have lots of medications that you would probably have to help me pay for. "
    i "And I’d be up all hours of the night banging on stuff when I’m making shelves and dressers and other furniture for Uta."
    s "So we’re moving in together, too?"
    i "I move quickly."
    i "Well, that’s not entirely true."
    i "In some areas I move quickly. In other areas, I’d rather not move at all."
    s "Yeah, this relationship is already exhausting me and it doesn’t even exist."

    scene iobench6
    with dissolve

    i "Um..."
    i "Can I hold your hand?"
    s "Sure. But the second you start calling yourself my girlfriend, I am walking away."
    s "I can not make that same mistake twice."
    i "That was all rhetorical. I know I’m not your girlfriend. And I know I’ll probably never {i}be{/i} your girlfriend because there are a million better choices and-"

    scene iobench7
    with dissolve

    s "Just give me your hand already."
    i "Oh, yeah. Sure. Sorry."
    s "Don’t apologize. Just accept that this is a momentary sign of affection and that it does not mean we are formally dating."
    i "I accept your affection and henceforth agree to not enter into a relationship with you."

    scene iobench8
    with dissolve

    i "But if you change your mind...you can have me."
    s "What kind of “have” are we talking about here? Because that word carries some rather heavy connotations in my dictionary."

    if bonus == False:
        s "And before you misunderstand what I mean by that, I'm referring to hugs."

    i "It means that you get to inherit Io Ichimonji and her six billion pounds of baggage."
    i "And that you need to figure out what to do about it because she’s been trying for years and has solved absolutely nothing."
    s "This isn’t even high maintenance in the lowest way possible anymore. It’s just high maintenance. "
    i "True. But how many other girlfriends could you get right now that could build you a fence?"
    s "I’m sure that line would kill in a dating profile."
    i "Online dating is stupid. Whatever happened to traditional relationships that formed from just...people meeting each other out in public and stuff?"
    s "Half of them ended in divorce."
    i "Oh. Right. That’s a thing. "

    scene iobench9
    with dissolve

    i "Do you think I’m crazy, Sensei?"
    s "I think neurotic is probably a better word."
    i "I think that’s fair."
    i "I know better than anyone how much of a handful I can be."
    i "Thankfully, your hands are really big. And surprisingly soft."
    i "Have you been using our new scented lotion?"
    s "I’m surprised you can feel anything with the amount of callouses on your hands."

    scene iobench10
    with dissolve

    i "Hey! You already know I’m kind of self-conscious about that!"
    s "Does this mean I should let go?"
    i "No! I’ve never held hands with a boy before. I like it."
    s "Have you held hands with a girl?"

    scene iobench11
    with dissolve

    i "I mean...not that I can remember. But I’m sure I’ve held hands with Uta at least once."
    s "Are you two actually closer than you look?"
    i "Are you about to make this weird?"
    s "Making things weird is basically the only way I know how to function in extended conversations."

    if bonus == True:
        s "Why else would I bring up sex so much?"
        i "Because you're trying to groom everybody."

    scene iobench12
    with hpunch

    i "Ow! Hey! Why are you squeezing me?!"

    if bonus == True:
        s "Sorry. Just a reflex."
    else:
        s "This is exactly what I was talking about. I am so weird."

    scene iobench13
    with dissolve

    i "Geez..."
    i "To think a hand this soft could crush mine with almost zero effort..."
    s "I bet you wish you had one of your four boxcutters on you now, huh?"

    scene iobench14
    with dissolve

    i "As if I’d ever go out of my way to hurt you."
    s "If I was truly attempting to crush your appendages, I really hope you {i}would{/i} hurt me."
    i "If you ever try to crush any part of me, I'll probably deserve it."
    s "I don’t think there’s much a person can do to deserve something like that."
    i "I do."
    s "What a quick response."

    i "Quick and easy. "

    if bonus == True:
        s "Like sex."
    else:
        s "Like a Hot Pocket."

    i "You’re making things weird again."
    s "The conversation’s been going on for a while."
    i "Do you want it to stop? Are you already tired of me?"
    s "Not really. But I can’t imagine you’re allowed to stay on break for this long."
    i "Did you actually think this was my break and that I wasn't just running away because I was about to have a panic attack?"
    s "I mean...it could have been both."
    i "I guess it could have."
    i "I’m feeling a lot better now, though."
    i "And I’m sure it goes without saying, but I’m glad you followed me out. Even if it seemed like I might have been trying to push you away."
    i "That’s gonna happen a lot from now on, you know? Times where I say the opposite of how I feel because I’m scared or nervous."
    i "Are you okay with that?"
    s "It doesn’t sound like I have much of a choice."
    i "You do, though. You can abandon me whenever you want and I can’t do anything about it."
    i "I’m definitely at the point where that would really mess me up, though. So...sorry to put all of that pressure on you again."
    s "I’m getting used to it."
    i "Would you like a reward for all of your hard work?"
    s "I already got a robot."
    i "Would you like {i}another{/i} robot?"

    if bonus == True:
        s "How about an Io?"

        scene iobench15
        with dissolve

        i "You already have an Io."
        s "An Io I wouldn’t mind being closer with. "
        i "But you already said you don’t want to date me."
        s "And that’s not what I’m saying now..."
        i "Then...you..."

        scene iobench16
        with dissolve

        i "…"
        i "Oh..."
        i "I think I know what you’re saying, but..."
        s "I’m just messing around."
        i "Yeah. Yeah, I know."
        i "Sorry, it’s just..."
        i "I know it’s not much, but...you can at least hold my hand like this whenever you want..."
        i "Like, even if it’s in class or something. I’m okay with it."
        i "But...anything more right now is..."
        s "Why are you giving me a whole explanation? Just tell me to shut up if I say something you don’t like."
        i "You just...sounded really serious when you...insinuated that."
        i "And I don’t want you to get your hopes up and then get fed up with me if I take too long to do what you want and-"
        s "Shut up."

        scene iobench17
        with dissolve

        i "…"
        i "Okay."
        i "You wouldn’t want me anyway. I’m too scrawny and my hands are all hard. And I have stupid hair."
        s "Your hair isn’t stupid."
        i "You directly told me my hair was stupid once and I still haven’t lived it down."
        s "Stop taking all of my jokes so seriously."
        i "Stop saying everything with the exact same inflection then. It’s hard to keep up."
        s "Welcome to my life. Everything about you is hard to keep up with."
        s "Everyone and everything else, too."
        s "The world moves too quickly."
        i "And in other areas, it doesn’t move at all."
    else:
        s "Can you buy me new wheels for my skateboard? I am trying to look young again."
        i "Sure."

    scene iobench18
    with dissolve

    i "I like you, by the way."
    i "I’m sure I’ve made that pretty obvious. But I feel like now is a really good time to come out and just say it."
    s "I had a feeling."
    i "Like, a lot. "
    i "My heart is beating like crazy right now."
    i "It’s keeping me warm even though it’s like negative a million degrees outside."
    s "Why are you telling me this when you know I’m not going to date you?"
    i "Because now you’ll have no choice but to think about it."
    i "If I didn’t tell you, you’d probably walk home whispering some weird monologue to yourself about how {i}I’m{/i} lost or {i}you’re{/i} lost-"
    i "But now you’ll just think about my stupid hair and my garbage robot and how dating me would be harder than adopting six babies all at once."
    s "You really need to work on selling yourself a little better."
    i "Sorry. I only sell products I’d be fine with using myself."
    i "Have I mentioned our new scented lotion?"

    scene iobench19
    with hpunch

    i "Ah! You’re squeezing again!"
    s "You’ve said “scented lotion” way too many times today."
    i "At least...take a free sample!"
    s "Io..."
    i "Sensei! Stop!"

    scene black
    with dissolve2

    "The two of us head back to the bathhouse and I drop Io off without going inside."
    "There’s a distinct lack of inner monologue on my way home after that."
    "But there are plenty of thoughts about a girl with stupid hair."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse20part2 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ioarchery1:
...
```

## Code that triggers this event
File: \game\IoEvents.rpy
Code:
```python
...
i "What?..."
    n "..."
    ki "Am I wrong?"
    s "Yes. It’s not creepy at all."
    ki "Do you actually like that kind of stuff, Sensei? "
    n "Wait..."
    n "Did you...{i}make{/i} that, Io?"
    i "I..."

    scene iopresent26
    with dissolve

    i "I found it in the trash."
    s "…"
    n "Really?...I kind of wanted one..."
    i "Bathhouse is...free tonight. Just go through the pink curtain."
    i "I’m...going to go on break..."

    scene black
    with dissolve

    "Io leaves [robotname] at the counter and quickly rushes to the front door without even grabbing her hoodie."
    "I follow closely behind her, trying to stop her from running away the same way she always does, but she immediately notices this and swings around."

    scene iopresent27
    with dissolve

    i "You don’t have to follow me."
    s "I know I don’t {i}have{/i} to. But I’m going to."
    i "Why? I’m probably just going to scream and cry and punch things."
    s "Because if I don’t come with you, you’ll wind up taking what Kirin said to heart despite it being obviously incorrect."

    scene iopresent28
    with dissolve

    i "It’s not {i}obviously{/i} incorrect. If that’s the impression she got, that’s the impression other people are going to get as well."
    i "I should have...practiced more and...gotten better before giving you anything."

    scene iopresent29
    with dissolve

    i "I should have been better..."
    s "Who cares what Kirin or “other people” think? You made it for me and I like it."
    s "I gave it a name and everything."
    i "I’ll make you a new one...with better materials and..."
    s "I don’t want a new one."
    i "…"
    s "So, where are we going?"
    i "You’re..."
    i "You’re still going to come with me?"
    s "Obviously."
    s "Just try and pick somewhere nearby. I wouldn’t recommend straying too far in the cold wearing just that."

    scene iopresent30
    with dissolve

    i "…"
    i "There’s a...bench I normally sit on during my lunch break..."
    i "It’s not far..."
    i "You really don’t have to come, though. It won’t be any fun."
    s "Then we’ll be bored and depressed together."
    i "Wouldn’t you rather be bored and depressed by yourself instead of bored and depressed with some random girl who’s just going to complain and make things sound worse than they actually are?"
    s "Not really, no."
    s "We’ve already uncovered that I mask my downsides by surrounding myself with other people."
    i "But there are two other girls who want your attention right behind you. They’re still looking this way."
    s "That's nice. But I'm looking forward right now."

    if bonus == True:
        i "You can probably see them naked if you stay here."
        s "I can see naked girls any time I want."
        i "Pervert."
        s "You’re wasting precious break time, Io."
        i "…"
        s "…"
    else:
        i "You can probably hug them if you stay here."
        s "I can hug girls any time I want, Io."

    scene black
    with dissolve2

    "Io turns around and leaves the bathhouse."
    "I follow behind her and-"

    s "Wait a second."
    i "...Huh?"
    i "What’s wrong?"
    s "I almost forgot something."

    $ renpy.end_replay()
    $ bathhouse20 = True
    $ io_love += 3

    "………"
    "……"
    "…"
    "{i}Io’s affection has increased to [io_love]!{/i}"

    jump bathhouse20part2
...
```