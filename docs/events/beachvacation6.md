# Three Girls in a Line on the Beach (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Behind a Bathroom, Under the Blazing Sun](./beachvacation5.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation6
* Group: Main
* Triggered by label: kirinbeachhjx
* Chain sources: beachvacation5
* Chain sources path: beachvacation5

## Official wiki page

[Three Girls in a Line on the Beach](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation6&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation6:
    scene yumisits1
    with dissolve
    play music "soda.mp3"

    r "…"
    f "…"
    r "She’s been sitting there for like an hour."
    f "Yeah...I feel kind of bad."

    scene yumisits2
    with dissolve

    r "Dude. You’re too nice. "
    r "Isn’t she a bitch to you like, literally every day ever? You shouldn’t feel bad just because she’s alone."

    scene yumisits3
    with dissolve

    f "I know...but imagine if that were me or you. "
    f "It probably took a lot of courage for her to even come here today. Especially since Chika isn’t here."

    scene yumisits4
    with dissolve

    r "Oh! Is Chika not here? I didn’t even notice. Hahahah!"
    f "That’s the same exact response you’ve had to that every single time it’s been brought up today."
    r "I mean, how weird would it be if I were to just...keep tabs on where Chika is at all times, right? Hahahah."
    r "That would be like, totally stalkerish. Who even is Chika? I’ve never heard that name before."
    f "Right..."

    scene yumisits5
    with dissolve

    if bonus == True:
        r "Well, uhh, anyway! Why don’t we get back to talking about that girl over there? The one with the surprisingly hot body that I’m totally not jealous of."
    else:
        r "Well, uhh, anyway! Why don’t we get back to talking about that girl over there? I'm pretty sure I saw her punching people at a nursing home the other day."

    f "Her name is Yumi...You know that..."
    r "Yeah, that girl. What do you wanna do?"

    scene yumisits6
    with dissolve

    f "What do you mean?"
    r "I mean, this is all on you. I’m just here for moral support."
    r "I thought you were gonna have one of those breakthrough things and approach her."
    r "That’s what it seemed like you were leading up to at least."

    scene yumisits7
    with dissolve

    f "Approach her and do what? The second I go over there she’ll just make some joke about...whales or something again..."
    r "Then fuckin’...kick some sand in her face and call her a loser or something. I don’t know."
    f "That doesn’t sound like moral support, Rin..."

    scene yumisits8
    with dissolve

    r "Well...then how about this? {i}Both{/i} of us will go over there and try talking to her normally. Like she’s any other girl in class."
    f "That has never worked before and I can’t imagine it working right now. But it’s a nice idea."

    scene yumisits9
    with dissolve

    r "Ugh, this is so stupid. Why does she have a problem with {i}you{/i} of all people?"
    r "You’re like the sweetest and nicest and cutest and smartest girl I know. And you’re always looking out for everybody."

    if bonus == True:
        r "And your boobs are like “BAM!”"
    else:
        r "And you are {i}so{/i} good at handling eggs."
        f "Why does everyone keep assuming-"

    scene yumisits10
    with dissolve

    r "Literally don’t get it at all."
    f "It’s because of my weight...She just...seems to have a problem with that for some reason."
    r "Well, that’s a stupid thing to take issue with. I think you’re adorable and I see you more than anyone, so that should mean something."

    scene yumisits11
    with dissolve

    f "It does mean something. Thanks."
    f "And for the record, I can’t imagine ever having any wingman other than you. So thanks for looking out for me all the time."
    r "Dude, duh. Thanks for looking out for {i}me{/i} all the time. I’m the loopy one. You’re just getting picked on by some girl with...self-esteem issues or something."

    scene yumisits12
    with dissolve

    r "Actually, now that I really think about it, what {i}is{/i} her deal anyway?"
    r "I don’t know, like...{i}anything{/i} about Yumi. Which is weird because I know like six million things about Chika."
    f "Chika? I thought you didn’t know anyone named Chika?"

    scene yumisits13
    with dissolve

    r "Wait, did I say Chika?! I meant...Chicken! I know a lot of...facts about chickens!"
    f "Name three..."
    r "Feathers! Wings! Beaks!"
    f "Those are just parts of the chicken, Rin. They aren’t really facts..."
    r "They are! Now let’s...go do the thing or whatever!"

    scene yumisits14
    with dissolve

    f "Hah..."
    f "Guess there’s no harm in trying again..."
    f "Here goes nothing."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yumisits15
    with dissolve

    "Three girls in a line on the beach."
    "One calm. One callous. One concerned."
    "And despite the girls having zero chemistry when inserted into the petri dish we call society, they do their best to emulate conversation as if they’re lifelong friends."
    "The only issue is that two of them {i}are{/i} while one has a hard time comprehending why she’s here in the first place."
    "But such is life."
    "No one knows why they’re here."
    "There are those who {i}think{/i} they know."
    "But they, too, are just specimens in petri dishes waiting for someone to come along and identify their purpose."
    "Oh, how disgusting it is to watch them squirm beneath the microscope."

    r "Yo! Mind if we join you?"
    y "Uhh, yeah. Kind of."
    y "What do you want?"
    r "Oh, nothing. Just wanted to sit by the water for a bit."

    scene yumisits16
    with dissolve

    y "You know there’s water fuckin’ everywhere, right? We’re at the beach."
    r "This isn’t the beach. This is a bathtub."
    y "..."
    r "..."

    scene yumisits17
    with dissolve

    y "Heh?"
    r "Sorry. It’s a thing. I swear."

    scene yumisits15
    with dissolve

    y "You’re fucking weird."
    r "What’s the problem with that?"
    r "Being weird is fun. You should try it sometime."
    y "Pass."
    y "Bad enough that I have to sit next to-"

    scene yumisits18
    with dissolve

    r "Oh! That reminds me! "
    r "I was wondering if maybe you’d want to come eat dinner with Futaba and me tonight?"
    y "What? Why?"
    r "Well...you know! Food! It’s a good way to bond with people or whatever."
    r "We were in class together in middle[school], weren’t we?"

    scene yumisits19
    with dissolve

    y "Surprised you remember. I barely showed up back then either."
    r "Yeah...Hey, that’s when you and Chika started hanging out, right?"
    y "...Oh, right. Forgot who I was talkin’ to for a sec."
    y "Listen, I don’t know where Chika is. You have her number, don’t you? Just fuckin’ text her."
    y "No point invitin’ me to hang out just to get info on her."

    scene yumisits20
    with dissolve

    r "That’s-"
    f "That’s not what Rin was trying to say..."
    y "Oh?"
    y "Then what {i}was{/i} she trying to say, fatass? Enlighten me."

    scene yumisits22
    with dissolve

    r "Hey! I don’t know what your deal is, but that’s my friend you’re talking-"
    f "It’s fine, Rin. Don’t worry about it."

    scene yumisits23
    with dissolve

    r "Ugh...whatever."
    f "We just...saw you sitting here alone and thought maybe you might be a little happier if you were hanging out with people."
    f "I know it’s hard to not have anyone you’re close to around and-"

    scene yumisits23
    with dissolve

    y "Oh, boo-fucking-hoo. It’s not like I’m sitting alone because I’m afraid of talking to anyone or some boring shit like that."
    y "I’m sitting alone because I like being alone. End of story."
    y "And now that you two showed up, my nice, quiet evening has been trashed and I’m going to go home pissed off."
    f "I...see..."

    scene yumisits24
    with dissolve

    y "So fucking annoying. I have no idea how Chika puts up with bein’ nice to people all the time and shit."
    y "All I want is for everybody to just stay out of my fucking business."
    y "It’s bad enough having to fuckin’ fend off the god damn teacher all the time, but now I have to deal with you dipshits as well? Fucking Christ."

    scene yumisits26
    with dissolve

    r "Why bring Sensei into this? He’s not even here right now."

    if bonus == True:
        y "Bullshit. Dude’s always lurkin’ in the background somewhere. He’s probably behind a tree jerking off to us right now."
    else:
        y "Probably too busy hugging his fucking accountant or something."

    f "Sensei isn’t like that, Yumi...He really does care about us."

    scene yumisits27
    with dissolve

    if bonus == True:
        y "Care?! You think that fucking pervert {i}cares{/i} about us? Jesus, you’re even dumber than I thought!"
        y "Just because he asks you to suck him off all the time doesn’t mean he fuckin' {i}cares{/i} about you! He’s using you!"
    else:
        y "Care?! You think that fucking bozo cares about us?! Jesus, you’re even dumber than I thought!"
        y "He just wants all of us to start some sort of traveling circus where we just juggle or...whatever else he's trying to get out of us!"

    scene yumisits28
    with dissolve

    if bonus == True:
        r "Woah! Slow down! Who said anything about sucking anyone off?!"
    else:
        r "Woah! Slow down! Who said anything about a traveling circus?!"

    r "Sensei is a good guy and wouldn’t ever force anyone to do anything they don’t want to!"
    y "Oh, if you only knew fucking half of it. "

    if bonus == True:
        y "And what’s with that shit about “not doing anything they don't want to do?” You think it makes it okay for a teacher to fuck his students as long as they’re okay with it?"

    scene yumisits29
    with dissolve

    r "Dude..."
    y "What?"
    r "What {i}happened{/i} to you?"
    y "The fuck are you talkin’ about?"
    r "I just don’t get how you can be so uptight all the time...We literally just came over here to ask if you wanted to eat with us."
    r "I’m not normally one to regret my decisions but...fuck, Yumi. You went and turned our nice gesture into a left field attack on our teacher."
    y "Hey, {i}you’re{/i} the ones who decided to come and talk to {i}me.{/i} Ain't my fault if you regret it."
    y "If you dislike it so much, why don’t the two of you fuck off and go eat or whatever instead of wasting your time inviting the class delinquent?"
    r "Oh, Hell no. We’re not going-"
    f "Let’s go, Rin."

    scene yumisits30
    with dissolve

    r "What?..."
    r "Really?..."
    r "After all that you just want to leave?"
    f "Yumi wants to be left alone, so we should leave her alone."
    f "It’s not our place to force her into doing anything she doesn’t want to do."
    y "Wish everyone would fuckin’ think that."

    scene black
    with dissolve2

    "Miscommunications."
    "Misunderstandings."
    "The circumstances and situations we find ourselves in often lead to nothing but anguish at the end of the day."
    "Forming bonds sounds more like a pipe dream when factoring in how they would impact others if we could only peer through the looking glass."
    "Three girls in a line on the beach."
    "Each involved in a different relationship with the same man."
    "Each with a different view of him."
    "How is it possible for three people to be so closely linked and yet so far apart?"
    "Such is the petri dish."
    "And such is life."
    "Perhaps we are not all meant to be happy."
    "And perhaps the girl in the middle of the line is meant to destroy herself in pursuit of what makes the other two whole."
    "{i}Praise be!{/i}"
    "{i}Not one god, but three!{/i}"
    "{i}The further we fall, the more we will see!{/i}"
    "{i}HOPE is the answer, but won’t be the key!{/i}"

    stop music
    $ renpy.end_replay()
    $ beachvacation6 = True
    $ trinity = True

    "The day drags on."

    play sound "static.mp3"
    scene whythesky
    with flash
    scene theend
    with flash

label beachvacation7:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
ki "I expected hot and sticky. There’s just more of it than I thought there’d be."
            s "That’s right. And now you have less than a minute to figure out a way to clean yourself up."
            ki "You mean you don’t want me saying hi to Ayane covered in your cum?"
            s "I absolutely do not."
            ki "But I worked so hard for it~"
            s "Kirin."
            ki "Okay! Fine, fine. I’ll go jump in the water."

            scene black
            with dissolve

            "Kirin lets go of my dick and promptly sprints over to the water to clean my semen off of her."
            "She jumps in before I’m able to warn her about exactly what happens when those two things mix."

            ki "Ah! What the fuck?! Why is it even worse now?!"
            ay "Oh! Kirin! There you are!"
            ay "Are we still going to the inn together?"
            ki "Uhhh...yeah! Just...give me a minute to cool off first! Hahahah~!"

            "I slide my swim trunks up and decide to head back before the two of them do."
            "My heart was beating so quickly toward the end of that that I’m pretty sure I need to take a nap or I’ll pass out and die."
            "But at least the girls will still be able to have some fun while I’m away."

            $ renpy.end_replay()
            $ kirin_love += 1
            $ beachvacation5 = True
            $ kirinbeachhj = True
            stop music fadeout 5.0

            "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
            "........."
            "......"
            "..."

        "Talk Kirin out of it":
            "Yeah...there’s no way I can do something like that in public. Not right now at least."
            "Kirin’s just...hormonal. She’d be better off masturbating in the bathroom than jerking me off behind it."

            s "Maybe some other time."

            scene kirinbeach13
            with dissolve

            ki "Wait..."
            ki "Are you for real?"
            ki "What the fuck is your problem?!"
            ki "What does everyone else have that I don’t?"
            ki "I’m literally ambushing you behind a bathroom because I’m so desperate for you to actually {i}want{/i} me and you’re going to say no?"
            ki "Do you even like girls? Are you gay or something?"
            s "That’s not what I’m saying..."
            s "I’d be more than happy going somewhere private and hooking up, but doing anything here is putting my entire life at risk."
            ki "Who the fuck cares about something as stupid as that?"
            ki "We’re supposed to be having fun. That’s what a fucking {i}vacation{/i} is."
            ki "Which means if a girl comes up to you and says “Hey, I’ll stroke your dick for literally nothing,” you agree."

            scene kirinbeach14
            with dissolve

            ki "But whatever. Fuck me, I guess. I’m not even in the mood to do it anymore anyway."
            ki "Go jerk yourself off or whatever. I’m gonna...go walk around the beach or something."
            ki "..."
            ki "And don’t come looking for me either. I want to be alone for a while."

            scene kirinbeach1
            with dissolve

            "Kirin storms off, ripping the leaves off a nearby bush and promptly throwing them onto the ground beneath her."
            "All I wanted was to try and do things a little more...safe. But it seems like I’ve wound up pissing her off instead."
            "…"

            s "Maybe I’ll go back to the inn and cool off for a bit?"

            "I mean, for all I know, that’s where Kirin is headed anyway."
            "…"

            s "Yeah. I’ll just do that for now."

            scene black
            with dissolve

            "I get myself together and begin to walk down the shoreline once more. "
            "The summer heat singes my uncovered skin as I step out of the comfort of the shade toward the chance to make things normal again."

            "{i}Uh-oh! It looks like Kirin is pissed off!{/i}"
            "{i}Hopefully she doesn’t cut off your penis in the middle of the night!{/i}"
            "{i}That would be horrible!{/i}"

            $ renpy.end_replay()
            $ beachvacation5 = True
            $ kirinbeachmad = True
            stop music fadeout 5.0

            "………"
            "……"
            "…"


    "{i}Meanwhile...not much further along the coast...{/i}"

    jump beachvacation6
...
```