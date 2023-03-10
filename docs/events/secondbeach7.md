# Everything Ephemeral (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Taking the Reins](./kirinlust20.md)

## Event preconditions

* Kirin lust less than 20



## Next events

None

## Event properties

* Id: secondbeach7
* Group: Main
* Triggered by label: kirinlust20
* Chain sources: kirinlust20
* Chain sources path: kirinlust20

## Official wiki page

[Everything Ephemeral](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach7&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach7:
    "{i}Meanwhile...{/i}"

    scene utaiobeach1
    with dissolve2
    play music "justlights.mp3"

    "Two girls on a- "
    "Oh, fuck it. You get the point already."
    "The thing is, these two are a little different from the rest."
    "But how, you ask?"
    "Why, that would be a question to ask either of them. Not me."
    "I’m just a bystander."
    "A voice or a thought carried in on a snowflake, melting before I have the chance to kiss the ground."
    "Then, just as I’m about to get a taste of what it is to be real, I become ephemeral."
    "And I evaporate."
    "But that’s a good thing. "
    "Because it means I get to spend more time with you."

    u "It’s been a while since I’ve seen you with your hair down."
    i "Does it look weird?"
    u "‘Course not."
    u "Want me to teach you how to do my braid thingy so we can be twins?"
    i "I think I’d need to grow a few more sizes before we could really be called that, Uta."
    u "You’d have to put on a few pounds, too. I haven’t had my ribs showing like yours since back in elementary[school]."
    i "Heheh...you were even skinnier than me back then."
    u "Alas, what puberty does to a [young_girl]’s body."
    i "Or {i}doesn’t{/i} in my case."
    u "What’s the rush, girl? It’s not like we’re goin’ anywhere anytime soon."
    u "You’ve got all of [high_school] to worry about puttin’ some meat on those bones."

    scene utaiobeach2
    with fade

    i "I guess so."
    i "I mean, there are kind of...bigger things to worry about right now anyway."
    u "Have somethin’ on your mind? You know you can always talk to me if there’s somethin’ troublin’ ya."
    i "Yeah...I just..."
    i "I really like Sensei, Uta."
    u "…"

    scene utaiobeach3
    with dissolve

    u "Ah. "
    u "Yeah, I know you do."
    u "You two would be cute together."
    i "I don’t really think that “cute” is a term that either of us strive for."
    i "But things are a little less...horrible when I’m with him."
    i "Which probably makes me sound overly dependent and moronic given that I’ve known him for less than a[school] year, but you know how my brain works and blah blah blah Io stuff."
    i "I’m just kinda nervous, you know?"
    i "He’s so cool and I’m so...shitty. "
    i "I just wish there was something I could do to-"
    u "It might help to be a little less self-deprecating every now and then."

    scene utaiobeach4
    with dissolve

    i "Hm?"
    u "I...just mean that Sensei probably gets a little annoyed having to hear you always talking down about yourself!"
    i "I know what you mean, and I’m fully aware of that as well. You’re just not normally as direct when it comes to criticizing my flaws."

    scene utaiobeach5
    with dissolve

    u "No...I’m not, am I?"
    i "Uh-oh. Looks like Uta might {i}also{/i} need somebody to talk to."
    i "Is it time to relive one of our famous late night vents from the old chat room?"
    u "I don’t really want to get into anything that deep, Io. It’s still a vacation after all."
    u "And we’re not really the same people we were back then."
    i "Hmm..."

    scene utaiobeach6
    with dissolve

    i "I disagree."
    i "I think that, to some extent, people never really change."
    i "Sure, you can learn to handle some things differently...and learn to approach problems in more constructive ways."
    i "But we’re all still products of our upbringing and the experiences we had during the most impressionable times of our childhood."
    i "Which is part of why I’ll always think I’m worthless and why you’ll always-"
    u "I’m not really in the mood to be analyzed right now, Io."
    u "Besides...you wanted to talk about Sensei, didn’t you?"
    u "About how...cool he is or whatever it was you said?"
    i "He’s great."
    i "He listens to me and understands me."
    i "Or at least I think he understands me. I’m so all over the place that I don’t think anyone will ever be able to pick up on 100%% of my bullshit."
    i "And...I don’t know. I just feel like there’s this deep sort of connection there despite the two of us having never done anything to truly {i}connect{/i} with one another."
    i "And I guess...that last part is what I’m more worried about than anything."

    scene utaiobeach7
    with dissolve

    if bonus == True:
        u "Does that...mean what I think it means?"
        i "Probably."
        i "Sensei’s...kind of really perverted."
        i "And..."
        i "Well..."
    else:
        u "Are you...talking about him being the huggy boy?..."
        i "Yeah..."
        i "Like...how do I connect with the huggy boy? What if my hugs aren't up to his standards?"
        i "I can't do it, Uta."

    scene utaiobeach8
    with dissolve

    u "I get it."
    u "I understand you better than anyone, so I know that comin’ out and talkin’ about all that’s just gonna make both of us feel like puddles of...grossness."
    u "Remember what we learned back then- the best thing to do is face forward. Don’t let your stupid brain or the stupid world bring you down."

    scene utaiobeach9
    with dissolve

    i "This is starting to get into chat room territory after all."
    u "Specifically the fun times in the chat room. Without all the venting about our problems and more of all the stuff we planned on doing together once we finally met."
    i "Heheh...we still haven’t gone to a baseball game together."
    u "Or the zoo! "
    i "Or a professional wrestling match."
    u "Or another zoo!"

    scene utaiobeach10
    with dissolve

    i "Why did I ever think you were a boy when all you wanted to do was go to different zoos?"
    u "Idunno. I probably told you I had short hair or something back then and you just ran with it cause that’s what you wanted me to be."
    u "Also, boys can go to zoos, Io. For all we know, Sensei loves the zoo."

    scene utaiobeach11
    with dissolve

    i "Heheh...maybe he does."
    i "I think I still want to go alone with you before we let him tag along, though. We’ve kind of had plans for years already, so it wouldn’t be fair to make him the third wheel."
    u "That’s right! Hoes before bros!"
    i "Don’t call us that. It’s a derogatory term that reduces the two of us to mindless bimbos instead of the sweet, fun-loving girls we actually are."
    u "Uhh..."
    u "Sisters before misters?"
    i "Heheh...I like that one a lot more."

    scene utaiobeach1
    with fade

    i "Hey...Uta?"
    u "Yeah?"
    i "I’m kind of glad you convinced me to come along this weekend."
    i "Thank you."
    u "Don’t thank me yet. We still haven’t gotten to the sleepover part, and that’s probably gonna be harder than anything for you."
    u "I am glad you’re here, though."
    u "Even if you probably wouldn’t have come if it was just me and not Sensei."
    i "You say that, but here I am watching the sunset with you instead of going around and searching for him."
    u "What can I say? I’m just as popular with the ladies as I am with the men."
    i "You do get a surprising amount of female customers at the maid cafe."
    u "There are a surprising amount of females in Kumon-mi."
    i "Also a good point."
    i "Do you ever think about how life would be if it were the other way around? If it was all the women who disappeared instead?"
    u "I think I would be making significantly more money to spend on a variety of sugary cereals."
    i "You should probably learn to be a little more careful with your paychecks, Uta."
    u "I have a problem."
    u "I do think it’d be...different, though."
    u "I think a world like that would be a little better for you and...a heck of a lot worse for me."

    scene utaiobeach12
    with dissolve

    i "Probably. You’re definitely the type that guys tend to fawn over."
    u "I wouldn’t be worried about that part. If there’s anything I’m confident about that isn’t attached to my torso, it’s the ability to dodge boys. "
    u "What I’d be scared of would be the whole issue of...figuring out who I am."
    u "I’ve only been a “girly” girl for a really small part of my life. And it’s not like I figured out how to do that all on my own."
    u "I learned from other girls and stuff. Just saw what they were doing and...voila."
    u "But I like it. "
    u "I like this version of me."
    i "I like this version of you too."
    u "How much would you say you like it on a scale of one to Sensei?"
    i "Definitely Sensei. "

    if bonus == True:
        i "In fact, probably even more since I know you aren’t trying to get into my pants."

    scene utaiobeach13
    with dissolve

    if bonus == True:
        u "But Io, you aren’t {i}wearing{/i} pants right now. Does that mean it's okay?"
        i "You know, maybe I should knock you down to a nine or something instead?"
        ya "Sexual intercourse before marriage is a sin."
    else:
        u "Jerk. After all of the indirect kisses we have shared while sharing assorted beverages."
        i "You know, maybe I should knock you down to a nine or something instead?"
        ya "(Airplane noises)"

    ya "Your limbs will fall off and dissolve into the sand."
    u "…"
    i "…"
    u "Did you hear that just now?"

    scene utaiobeach14
    with dissolve

    i "Yup..."
    u "Oh! Yasuyasu’s here! What a...delightful surprise!"
    ya "Do not be delighted to be visited by a mere worm like me. I am simply scouring the sands in search of decaying plant matter to feast upon."
    u "Did uhh...did Noriko convince you to go vegetarian or something?"

    scene utaiobeach15
    with dissolve

    ya "I beg your pardon?"
    u "Umm...don’t worry about it. Just a little confused by the whole...plant matter thingy."
    u "You...wanna sit down with us maybe? We’re kinda just killin’ time before goin’ back to the room for dinner."
    ya "You’re inviting {i}me{/i} to sit with you? Is that really okay?"

    scene utaiobeach16
    with dissolve

    u "I mean...as long as Io is okay with it, I don’t really mind. It’ll definitely...liven up the conversation at least."
    i "Uhh..."
    i "I guess it’s okay?"
    i "I don’t really count Yasu as a human, so there’s not really anything for me to despise apart from the whole religious fanatic thing."
    ya "Do you dislike God, Io?"
    i "It’s not possible to dislike something that doesn’t actually exist."
    ya "But what if I can prove He does?"
    i "You can’t. Countless people have attempted to prove the existence of divine beings and each and every effort has been not only incredibly flawed, but-"

    scene utaiobeach17
    with dissolve

    u "I’m bored! Let’s talk about something that I can understand instead!"
    ya "I’d be more than willing to teach you if-"
    u "I’m good! "
    u "Plop that booty down right next to me and talk about something other than God for a change, Yasuyasu. "

    scene utaiobeach18
    with fade

    ya "Something...other than God?"
    ya "Do I know anything else?"
    u "You’ve gotta know {i}something{/i} else."
    u "Like...maybe some hobbies? Or a TV show you like that you never really get to talk about?"
    u "Me and Io watch a lot of TV together, so there’s a pretty good chance we’ve seen whatever you’re into."
    ya "I don’t watch TV. The frequency of the sound and color of the light causes my brain to shake in ways that make me feel a great deal of pain."
    u "Ooooooookay. Then how about food? Do you have a favorite?"
    ya "A favorite food..."

    scene utaiobeach19
    with dissolve

    ya "Strawberry daifuku."
    u "Ah! A real answer! And a really cute one at that!"
    i "That is...not the answer I was expecting."
    ya "What were you expecting, Io?"
    i "I don’t know...Maybe the...blood of angels or something?"
    ya "Why ever would I consume the life essence of what I aspire to become? That’s just silly."

    scene utaiobeach20
    with dissolve

    u "Yasuyasu, tell me somethin’ else you like. Another girly thing."
    u "Like...tell me how you feel about love!"
    ya "Love?"
    u "Yeah! Like...what kinda boys do you like? Or girls. We ain’t judgin’ here."
    ya "I’m not quite sure. "
    ya "I can’t say I’ve ever known someone long enough to feel an emotion as strong as that."
    u "Not even like a family member you joked about marrying or something? "
    ya "Family?"
    u "Yeah. Your mom must’ve told you about love at some point, right? "
    ya "I’m afraid I don’t have a mother."

    scene utaiobeach21
    with dissolve

    u "Oh...crap. I’m sorry."
    u "This is what I get for choosing two conversation topics in a row, isn’t it?"
    i "You’ve got Touka, though, right?"
    i "I’m sure that she’s probably asked you something similar in the past. You two are basically attached at the hip, aren't you?"
    ya "I suppose that Touka is like a mother to me."
    i "Not really what I was going for, but sure. Let’s run with that."

    scene utaiobeach22
    with dissolve

    ya "She is a good person."
    ya "Pure of heart and mind."

    if bonus == True:
        ya "A true virgin both physically and spiritually."
    else:
        ya "(Airplane noises)"

    i "Uta, change the topic again."
    u "Are you kidding? I wanna see where this goes."
    ya "A person like her would be better suited for this conversation."
    ya "She possesses both the freedom of thought and an unearthly desire to belong. To love and to be loved."
    ya "I possess none of that."
    ya "I am a vessel. Incapable of feeling or wanting those things."
    ya "Existing for the sole purpose of filling myself with light and pouring it over the heads of those willing to be drenched in His love."
    ya "Slipping silently into sermons, scalding each surrounding servant with seed stripped from sinful serpents."
    ya "Singeing the skin of those sleeping in shadows by singing the praises of the smile in the sky."
    ya "These are the reasons I exist."
    ya "Not to love. Not to feel. Not to want."
    ya "But to be. And become."
    ya "And to save. And to be saved."
    ya "All I want is for the world to smile together, all at once."
    ya "That is all He wants as well."
    ya "But there is so much darkness. "
    ya "And not just in the world itself, but in everyone."
    ya "In each of you."
    ya "It will swallow you whole, you know. "
    ya "Maybe not now. Maybe not tomorrow."
    ya "But there will come a time when you are forced to face what you fear the most."
    ya "And when that time comes, I will be right around the corner- with open arms and a sanctuary for you to lose yourself in when you think there’s nothing {i}left{/i} to lose."
    u "…"
    i "…"
    ya "…"

    scene utaiobeach23
    with dissolve

    ya "I’m sorry. What was the question again?"
    u "We..."
    u "We just wanted to know what you thought about love."
    ya "I see."
    u "…"
    i "…"
    ya "…"

    scene utaiobeach22
    with dissolve

    ya "I think love is lovely."

    scene black
    with dissolve2

    "Three girls in a line on the beach."
    "One callous-"
    "And two others."
    "But is there truly an issue with callousness in and of itself?"
    "And couldn’t such an adjective change based on your perception of it?"
    "If you want my opinion, the answer is yes."
    "My opinion is that everything can change. And that everyone’s thoughts can be changed if you try hard enough to actually change them."
    "And so I say to Io Ichimonji, the girl who thinks no one can change, that you are weak."
    "And I say to Uta Ushibori, the girl who doesn’t want to think at all, that you, too, are weak."
    "And to the girl {s}in the black dress{/s} in the[school] swimsuit-"
    "You are the weakest of all."
    "But for reasons quite different than that of the others."
    "The three girls run into the water and never return."
    "And I fall back into place in the midst of the water cycle, for the storm clouds have drifted slightly off course."
    "Everything is ephemeral."
    "Everything is falling."

    scene everythingg
    with dissolve4
    stop music
    play sound "static.mp3"
    scene everythingg2 with flash
    scene everythingg3 with flash
    scene everythingg4 with flash
    scene everythingg5 with flash
    scene everythingg6 with flash
    scene everythingg7 with flash
    scene everythingg8 with flash
    scene black
    stop sound

    $ renpy.end_replay()
    $ secondbeach7 = True

    "{i}Affection!{/i}"

    jump secondbeach8

label secondbeach8:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
"Cum outside":
            ki "Oh my god...oh my god...oh my fucking god...[kirinmaster]..."
            ki "Please...just...hurry the...fuck up already!"

            with sexfade
            with sexfade
            scene kirinnodoka32
            with cumflash
            with hpunch

            ki "AHH...AAHHHH! AAAAAAAAAAHHHHHHHHH!!!!!! FUUUUUCK!!!!!!!"

            "Kirin has just as violent of an orgasm as always as I pull out of her at the very last second and let loose an eruption of cum all over her body."

            scene kirinnodoka33
            with dissolve

            "She takes a few seconds after being drenched to lightly grind up against the underside of my shaft as she comes to terms with the fact that we’re done for now."

            ki "Hah...hah...hah..."
            ki "Woah..."
            ki "That was...a good one..."
            ki "Threesomes...are the best..."
            no "I’m not sure if I’d count this as a threesome, Kirin. I barely participated at all."
            no "The two of you performed wonderfully, though. Bravo."
            no "This will make an excellent erotic tale once I figure out what sort of relatives you two will be."
            ki "Hah...hah...relatives?..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene kirinnodoka34
    with dissolve

    ki "{i}*Ahem*{/i}"

    scene kirinnodoka35
    with dissolve

    ki "Nodoka."
    no "Kirin."
    ki "It has been a pleasure."
    no "An excellent start to the weekend, might I say."

    scene kirinnodoka36
    with dissolve

    ki "Sensei, thank you for fucking me and helping me get over how angry I was at my sister."
    s "Any time?..."
    ki "Anyway, I’m gonna go swimming now. Would you mind passing me my clothes? They’re right behind you."
    s "Oh...uhh...sure."

    play sound "slidedoor.mp3"
    scene kirinnodoka37
    with dissolve

    "Kirin quickly puts her clothes back on and leaves the room."
    "And, in other news-"
    "What?"

    no "Well, then."
    s "I can’t say that was a thing I expected to happen this weekend."
    no "Neither can I. Though, I did rather enjoy myself."
    s "You didn’t even do anything."
    no "You don’t always need to {i}do{/i} something to enjoy yourself, Sensei. Some people simply like observing."
    no "Now, if you’ll please excuse me, I’m going to go take a cold shower."

    play sound "slidedoor.mp3"
    scene kirinnodoka38
    with dissolve

    s "…"
    s "…"
    s "…"

    scene black
    with dissolve2

    "Being around [teenager]s is exhausting."

    $ renpy.end_replay()
    $ kirinlust20 = True
    $ kirin_lust += 1
    stop music fadeout 5.0

    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"

    play sound "phonebeep.wav"
    "{i}You've received a new picture message from Kirin!{/i}"

    "………"
    "……"
    "…"

    jump secondbeach7
...
```