# A Place Like This
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=streets25&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 25

✅Event "[Yumi: Great Expectations](./yumidorm20.md)" is completed (event=yumidorm20)



## Next events
* [Yumi: Caught in the Vortex](./yumidorm25.md)

## Event properties
* ID: streets25
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets

## Event code
File: \game\YumiEvents.rpy
Code:
```python
...
label streets25:
    scene yumiramenjob1
    with fade
    play music "soda.mp3"

    "I manage to find Yumi wandering around the city and somehow coax her into grabbing fate by the balls today."
    "After going back and forth for around twenty minutes or so, she finally caves and the two of us make our way to the old district to visit Tsuneyo."

    y "You sure you remember where this place is?"
    y "It’s like the middle of fuckin’ nowhere out here."
    s "I thought you spent a lot of time in this part of town?"
    y "Doesn’t mean I know where fuckin’ everything is, jackass."
    y "This place is confusing as shit to navigate sometimes."
    y "It’s easy to get lost. And it sucks when you do because of all the fuckin’ homeless people out here tryin’ to nab your spare change and shit."
    s "At least they haven’t bothered {i}us{/i} yet."
    y "Give it a minute or two, they’ll find you. Always fuckin’ do."

    "We make our way down the street toward Tojo Ramen."
    "Thankfully, I do remember the way on account of coming here to see Tsuneyo, but it seems like Yumi is genuine when she says she doesn’t know where it is."
    "She’s right in saying this part of town is easy to get lost in."
    "It feels almost like a labyrinth at times."
    "Abandoned building after abandoned building cloud the landscape while dwellings of impoverished living stack haphazardly on top of one another."
    "Every once in a while, a stray cat will run past us. Some of them even stop and rub up against Yumi."
    "She has no reaction."
    "She must truly be heartless."

    scene yumiramenjob2
    with dissolve

    y "Thanks for coming...I guess."
    y "Not because I’m nervous or anything. I just wouldn’t have been able to find the place on my own."
    s "Well, it’s not like you have an interview scheduled or anything."
    s "You could pretty much come here whenever you want. No one’s expecting you."
    y "Are you gonna fucking say “You’re welcome” or are you just gonna try and make me sound like an idiot?"
    y "Feel like every time I try and say somethin’ nice, you just throw it back in my face."
    s "To be fair, you’ve only said two or three nice things to me since we’ve met."
    y "Yeah but those might be the only two or three nice things you ever get out of me, so it’s probably best if you don’t fuckin’ toss ‘em aside so easily."
    s "You’re welcome, Yumi. I’m happy to have been of some sort of help to you today."
    s "Even if it is only as a GPS."

    scene yumiramenjob1
    with dissolve

    y "See? Was that so fucking hard?"

    "The walk continues."
    "We weave our way through the streets in the second half of town and manage to dodge enough panhandlers to finally come close to our destination."

    scene yumiramenjob3
    with dissolve

    y "So, I’m obviously not going to use your stupid strategy from the other night...but just for peace of mind, what was it again?"
    s "Just telling Tsuneyo how much you love noodles over and over."
    s "I honestly can’t imagine that {i}not{/i} working."

    scene yumiramenjob4
    with dissolve

    y "That’s so fucking weird...I don’t get it at all."
    s "Neither do I. But hey, at least she knows her interests."
    s "And besides, it’s a weird little shop in the middle of nowhere. If it had a normal interview process, it would lose its charm."

    scene yumiramenjob5
    with dissolve

    y "There’s no charm in a place like this."
    y "Just a bunch of fuck-ups and burnouts tryin’ to make it one more day without givin’ up on life."
    y "Thing about places like this is that if you spend too much time in ‘em, they wind up drainin’ you."
    y "You lose any sense of hope...give up on your dreams and think shit like, “Somethin’ {i}that{/i} good won’t ever happen to me.”"
    y "It eats away at you."
    y "And before you know it, you’re wakin’ up in an alley with a needle stickin’ out of your arm thinking, “How the fuck did it come to this?”"
    s "I’m hoping you’ve never woken up like that."

    scene yumiramenjob6
    with dissolve

    y "Me? Nahh."
    y "Drugs are cheap, so I probably could, though."
    y "Hell, probably still might if things never wind up gettin’ any better."
    y "But I’ve seen how that shit works firsthand and it’s not pretty. So I’ve somehow managed to avoid it one way or another."
    y "Nothing’s ever certain, though. Desperation can make people do crazy shit."
    y "So who knows? Maybe one day, the reason I won’t be in[school] might be a lot worse than just me not wantin’ to show up."
    s "…"

    "For what might be the first time ever, I actually understand where Yumi’s coming from."
    "I’m obviously a lot less experienced in the topic than she seems to be, but she’s smart enough to realize how dangerous a life like that is."
    "And yet she chooses to walk that path, surviving solely off of thievery and handouts from her best friend."
    "But it’s not like that makes her weak."
    "Those are just the circumstances she’s found herself in."
    "Good for her."

    s "I’m proud of you."
    s "I just want you to know that."

    scene yumiramenjob2
    with dissolve

    if bonus == True:
        y "Suck my dick, you fucking [rapist]."

    y "Don’t try to act like my dad just because I opened up for a second."
    y "It’s just...a long walk and I’m fuckin’ bored."
    y "Are we there yet?"
    s "…"
    s "Just a few more blocks."

    scene black
    with dissolve

    "And so we walk a few more blocks."
    "The scent of pork broth hits us from a quarter mile away, which is actually quite surprising given that Tojo Ramen doesn’t have any windows for the scent to leak out of."
    "I wonder why that is?"

    y "Wait. Stop..."

    scene yumiramenjob7
    with dissolve

    "Yumi comes to a sudden halt just as we’re about to round the final corner to Tojo Ramen."
    "In front of us is the same woman who I wound up buying dinner for the first time I ever went there."
    "And I’m assuming she’s the reason Yumi is suddenly hesitating."

    y "Uhh...Yeah, I don’t know if I’m feeling up to this today, dude."
    y "My stomach hurts and I think I’m just gonna head back to Chika’s place and crash."
    s "But it’s right around the corner. We’ve been walking for hours."
    s "At least give it a shot."
    y "Pass. I’ll give it a shot another day. I-"
    s "If it’s because you’re worried about that girl over there, I know from experience that she’s not as bad as she looks."

    scene yumiramenjob8
    with dissolve

    y "That’s my fucking mom, you idiot!"
    y "And what kind of experience do you have with her?!"
    s "..."
    s "{i}That{/i} is your mom?"
    y "Yes!"
    s "...I bought her dinner once."

    scene yumiramenjob9
    with dissolve

    y "Why did you buy dinner for my mom?!"
    s "I didn’t know she was your mom."
    y "We have the same fucking eyes!"
    y "Besides, she {i}is{/i} as bad as she looks! And I have a lot more experience with her than you do, I can tell you that."
    y "Who the fuck did you think I was talking about when I went on that rant about drugs and shit like ten minutes ago?"
    y "She’s a fucking psycho. And who the fuck knows what will happen if she sees me here?"

    scene yumiramenjob10
    with dissolve

    y "Ah-"

    "Yumi’s apparent mother suddenly shifts her eyes in our direction and causes Yumi to flinch in response."

    scene black
    with dissolve

    "She grabs my wrist and forcefully pulls me into an alleyway right beside us, throwing her body up against mine and bringing her voice to a whisper."

    scene yumiramenjob11
    with dissolve

    y "If you even {i}think{/i} about touching me right now, I will fucking kill you."
    s "You are aware that {i}you’re{/i} the one pinning {i}me{/i} to the wall, right?"
    y "Only because I have no idea what I’d fucking say to her and she was about to look this way."
    s "You smell nice."

    scene yumiramenjob12
    with dissolve

    y "Shut the fuck up! I do not!"
    s "How long do I need to shut up for?"
    s "As much as I’d like to spend the entire day in an alleyway with you, I feel like we’re going to need to come out sooner or later."

    scene yumiramenjob13
    with dissolve

    y "We need to...I don’t know...figure out a way to distract her or some shit."

    scene yumiramenjob14
    with dissolve

    y "You said the ramen place is right around the corner, right?"
    s "Right. You make the next right and it’s literally the only building there. It’s a dead end right after that."
    y "Then why don’t you...go and fucking talk to her for a minute or something?"
    y "Just long enough for me to sneak inside and talk to Noodles myself."
    s "Noodles is a bird. You have to-"

    scene yumiramenjob12
    with dissolve

    y "Can-it with the fucking bird! I mean Tsuneyo!"
    y "Just go distract my mom or something while I talk to her!"
    s "...Okay, deal."
    s "But if she makes me buy her dinner again, you’re having it taken out of your post-interview allowance."
    y "Fine! Whatever! Just go!"

    scene black
    with dissolve

    "Yumi makes an opening in the alleyway just large enough for me to pass through."
    "My body rubs up against hers and she twitches in response as I move back into the street and over toward her mother..."

    scene yumiramenjob15
    with dissolve

    q "Huh?..."
    q "Can I help you with-"
    q "Oh, wait a second. You’re that guy."

    scene yumiramenjob16
    with dissolve

    q "Here to buy me dinner again?"

    menu yumimomchoice:
        "I am here to distract you":
            s "I’m actually here to distract you."

            scene yumiramenjob17
            with dissolve

            q "Distract me? From what?"

            "Wait. Shit."
            "I’m clearly not very good at this."

            jump yumimomchoice

        "Want to make out?":
            s "I think I’m in love with you."

            scene yumiramenjob17
            with dissolve

            q "Love?"
            q "With me?"
            q "Are you out of your mind?"
            q "All we did was eat ramen."
            s "I think we need to kiss for a few minutes in order for me to figure out my true feelings."
            q "…"
            s "…"
            q "…"
            s "…"
            q "Well, it's cool that you're forward and shit. But I'm gonna have to pass."

            "Fuck."

            jump yumimomchoice

        "What are you up to?":
            s "Hey. Just saw you standing here so I thought I’d come and say hi."

    scene yumiramenjob18
    with dissolve

    q "Oh. Well, uhh...hey."
    q "I was probably going to get something to eat in a few minutes if you wanted to come."

    "A few minutes? Shit."
    "I need to figure out a way to buy more time."

    s "What were you planning on eating?"
    s "Pizza?"
    s "Mexican?"
    s "Udon?"
    q "Well, uhh...The ramen shop is literally right next to us and-"
    s "Italian?"
    s "Crepes?"
    s "American?"
    s "Dessert, maybe?"
    q "Ramen..."
    s "French creole?"
    s "Pancakes?"
    s "Salad?"
    s "Fried chicken?"

    scene yumiramenjob19
    with dissolve

    q "Is this some kind of prank or something? Because it’s really fucking weird if it is."

    scene black
    with dissolve

    "{i}Meanwhile...inside of Tojo Ramen...{/i}"

    scene yumiramenjob20
    with dissolve

    t "Good evening. Welcome to Tojo Ramen."
    t "Please take your time looking over the-"
    y "Actually, I’m not here to eat."
    t "…"
    t "Are you here to rob me?"
    y "What? No. I just-"

    scene yumiramenjob21
    with dissolve

    y "Listen...We’re in the same class and I really need a job."
    t "We are?"
    t "I’ve never seen you in[school] before."
    y "Yeah you have. We were next to each other in the hallway that one time."

    scene yumiramenjob22
    with dissolve

    y "But that’s beside the point."
    y "I’m not sure if you’re looking for any help around here or not, but I promise that if you give me a shot, I’ll work really hard."
    y "I might be a little rough around the edges and...I might not have the most experience, but I won’t let you down."

    if bonus == True:
        y "It’s just...kind of tough being self-sufficient at this age."
    else:
        y "It’s just...kind of tough being self-sufficient."

    y "Especially when no one wants to give you a chance."
    t "I’m sorry to hear that."
    t "We aren’t hiring, though."

    scene yumiramenjob23
    with dissolve

    y "Oh...Well, umm..."
    y "There’s...nothing I can do to change your mind?"
    y "Not even like, a free...apprenticeship or something?"
    t "Not at the moment. I apologize."
    y "…"
    t "…"

    scene yumiramenjob24
    with dissolve

    y "Hah..."

    scene yumiramenjob25
    with dissolve

    y "I love noodles."
    t "…"
    y "…"
    t "Okay. You have my attention."
    t "I suppose an apprenticeship would be okay."
    t "I do need to test your abilities beforehand, though."

    scene yumiramenjob26
    with dissolve

    y "Oh, yeah! Definitely!"
    y "Just tell me what you need me to do and I’ll try my best!"
    y "Like I said, I don’t have a lot of experience, but if it’s something like washing dishes or whatever, I can definitely figure it out."
    t "Then we will start with something simple."
    t "Any time someone enters the store, you must say, “Good evening. Welcome to Tojo Ramen.”"
    t "Please do that the next time someone walks in."

    scene yumiramenjob27
    with dissolve

    y "Easy."

    play sound "dooropen.mp3"

    t "Oh. Here comes someone now."
    t "Please repeat the words directly as I instructed."
    y "You got it!"
    y "Good evening! And welcome to-"

    scene yumiramenjob28
    with fade
    stop music fadeout 7.0

    y "..."
    y "Mom?"
    q "…"
    t "Close, but not quite."
    t "Perhaps it would be better if you worked somewhere else."
    q "Yumi?..."
    q "What are you doing here?..."
    q "Do you work here now?"
    y "No, I-"
    y "…"
    y "I was just leaving."

    scene yumiramenjob29
    with dissolve
    play sound "dooropen.mp3"

    "Yumi immediately leaves Tsuneyo’s side and walks right past her mother, barely acknowledging her along the way."

    q "…"

    scene yumiramenjob30
    with dissolve

    "Yumi’s mother remains silent for a moment before looking at me."
    "Even Tsuneyo seems to understand that something is going on since she’s yet to welcome me to the store."

    q "So that’s what you were trying to distract me from..."
    s "She didn’t seem like she wanted to see you."
    q "I don’t blame her..."
    q "The fuck are you supposed to be, though? Boyfriend?"
    q "You seem a little old."
    s "Her teacher. I’m helping her look for a job."

    if bonus == True:
        "I conveniently leave out the fact that I have forcefully made out with her daughter before."

    scene yumiramenjob31
    with dissolve

    q "A job, huh?..."
    q "Well...that’s good..."

    scene yumiramenjob30
    with dissolve

    q "Haven’t given you my name yet, have I?"
    s "You have not."
    yu "I’m Yuki. Yumi’s mother."
    yu "And you should probably chase after her now. She’s sensitive."
    s "Yeah. I’ll go find her."
    s "And I’ll see you some other time."

    scene yumiramenjob31
    with dissolve

    yu "Yup..."
    yu "See you around..."

    scene black
    with dissolve2

    "I’m not able to find Yumi after that."
    "Granted, I don’t look for very long."
    "While it would have been nice to find her, I can’t foresee anything good happening if I’m wandering around the second half of town in the dark."
    "I’m sure that wherever she went, though, she’s fine."
    "She probably just needs a little time to cool off."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets25 = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label streets30:
...
```

## Code that triggers this event
File: \game\YumiEvents.rpy
Code:
```python
...
label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump satafternoonmenu
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
    if yumi_love >= 5 and streets5 == False:
        jump streets5
    if yumi_love >= 10 and day44 == True and streets10 == False:
        jump streets10
    if yumi_love >= 15 and yumidorm15 == True and streets15 == False:
        jump streets15
    if yumi_love >= 20 and streets15 == True and ramen1 == True and streets20 == False:
        jump streets20
    if yumi_love >= 25 and yumidorm20 == True and streets25 == False:
        jump streets25
...
```