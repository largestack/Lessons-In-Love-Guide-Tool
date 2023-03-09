# Apples to Apples
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=streets15&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 15

✅Event "[Yumi: Worse Comes to Worst](./yumidorm15.md)" is completed (event=yumidorm15)



## Next events
* [Main: On The Bright Side](./day126.md)
* [Main: A Proper Introduction](./day150.md)
* [Yumi: Token Tsundere](./streets20.md)

## Event properties
* ID: streets15
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets

## Event code
File: \game\YumiEvents.rpy
Code:
```python
...
label streets15:
    scene yumiapples1
    with dissolve2
    play music "normalday.mp3"

    "I scout the area for Yumi as I make my way down the streets of Kumon-mi."
    "The middle of the afternoon is the peak-time for foot traffic over the weekend, so things are surprisingly busy right now."
    "There are women walking dogs, children playing too close to the street...and I'm pretty sure I even saw a man or two at some point."
    "That's a big deal when you remember that nearly all of them are millions of miles away right now."
    "But Yumi is nowhere to be seen."
    "I wonder where she could be?..."

    scene yumiapples2
    with dissolve

    y "Yo..."
    s "If only there was some sort of clue as to where I could find her..."
    y "Hey. Captain Fuckwad. I’m right here. "
    y "The hell you just starin’ off into space for?"
    s "Oh, wow. What an incredibly convenient turn of events."
    s "Are you ready to get going?"

    scene yumiapples3
    with dissolve

    y "Get going? The fuck are you talkin’ about? I don’t remember makin’ any plans with you."
    s "Well, we didn’t really decide on a date, but I figured today might be a good chance to go scope out the cafe together."

    scene yumiapples4
    with dissolve

    y "Wait, today?! Why today?!"
    y "Don’t you need to like, get all dressed up and shit when you go job-hunting?"

    if bonus == True:
        s "Girls your age can normally get away with not doing that. Especially if it’s for something like a part time job as a barista."
    else:
        s "Eh. I'm sure you'll be fine."

    s "Besides, do you even have other clothes? That’s the only shirt I ever see you wear."

    scene yumiapples5
    with dissolve

    y "Of fucking course I have other clothes! I just like this shirt! You got a problem with that?!"
    s "No. I just don't think it's doing you any favors in the cuteness department."

    scene yumiapples6
    with dissolve

    y "Well, good. That department fuckin’ sucks."
    y "All those who spend hours every morning tryin’ to make themselves look pretty and shit are missin’ out on the joys of life."
    s "Right. Because when I think ‘Yumi’ the first thing that comes to mind is the endless pursuit of happiness."

    scene yumiapples7
    with dissolve

    y "Hey! You’re lucky I need money or I’d never agree to doing somethin’ as stupid as this!"
    s "There is nothing stupid about joining the workforce, Yumi. Just look at me- a semi-successful man of indeterminate age living his best life."

    scene yumiapples8
    with dissolve

    y "{i}Indeterminate age{/i} my ass. You're old as fuck."
    y "Just...bring me to the stupid cafe already. I don’t remember how to get there."
    s "Oh, cool. I was starting to think you were going to back down."
    y "Yeah, so was I..."

    scene yumiapples9
    with dissolve

    y "So, are we gonna fuckin’ get this over with or are you just going to keep standin’ there like one of those weird British guard dudes?"
    s "Fine, fine. Let’s go."
    s "If you try to run away, though, I’m grabbing you and dragging your body there myself."

    if bonus == True:
        y "Lay a finger on me and I swear to God you’ll live the rest of your life without a dick."
    else:
        y "Lay a finger on me and I swear to God you’ll live the rest of your life dead."
        s "Wait, what?"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene jobint1
    with dissolve

    "After a fair share of walking, the two of us arrive at the cafe."
    "I think Rin should still be working, so the best course of action is probably
    just asking her about any potential openings."

    scene jobint2
    with dissolve

    y "Uhh...I’m having second thoughts about this."
    y "Headphones is working right now. Won’t she think it’s weird if she sees the two of us together?"
    s "Probably. But we're already here, so there's no backing down now."
    s "It’s just Rin, though. I doubt she’d make a big deal out of something like that."
    y "Well...you know her better than I do, I guess."

    scene jobint3
    with dissolve

    y "Which is actually really fucking disturbing to say since I’m the same age as her and have known her at least twice as long."
    s "Uhh...Apples to apples, I guess?"

    scene jobint4
    with dissolve

    y "How does that dumb-ass phrase even apply here?!"
    s "It doesn’t. Just open the goddamn door, Yumi."
    s "Do it for the money. And the lunch. And m-"

    scene jobint5
    with dissolve

    y "If you tell me to do it for you I’m going to walk away right now."
    s "Do it for the money. And the lunch."
    y "…"
    y "Ugh...whatever..."

    scene black
    with dissolve2

    "Instead of moving toward the door, Yumi steps behind me and uses me as a sort of body-shield."
    "We’re walking into a cafe, not some sort of gang hideout, so I’m not sure what the big deal is."
    "But either way, I push aside the doors and the two of us make our way inside of the pleasantly air conditioned building."
    "For me, this is nothing but a welcome escape from the heat."
    "But for Yumi-"
    "This is a huge step toward the {i}her{/i} she's always dreamt of."
    "Or not and she's just desperate."
    "Either way, I'm glad to be inside again."

    scene jobint6
    with dissolve2

    r "Hey, Sensei! You don’t normally come in-"

    scene jobint7
    with dissolve

    r "This late..."
    y "Yo."

    "Rin’s enthusiasm immediately vanishes as soon as Yumi walks up to the counter with me."
    "I can only imagine how confusing that must be, especially with how Yumi and I rarely even talk at[school]."
    "Well, Yumi rarely talks to {i}anyone{/i} at[school] on account of not being there, but I digress."

    r "Oh. Uh...Hey, Yumi."
    y "Sup, Headphones."

    scene jobint8
    with dissolve

    r "Uhh...Sensei?"
    s "Yeah?"
    r "Would it be weird for me to ask exactly what's going on here?"
    s "I think it would be perfectly reasonable to ask that, Rin."
    r "Then, what exactly is going on here?"
    r "Since when do you and Yumi, like...go out for coffee?"
    s "It's our first date and she's very nervous. Please don't say anything that will embarrass her."

    scene jobint9
    with dissolve

    y "Yo! That ain't even close to bein' funny! Don't go sayin' shit like-"
    s "Yumi, quiet. Don't raise your voice like that in a place you're about to apply to."

    scene jobint10
    with dissolve

    r "Wait...apply? Are you looking for a job?"
    y "Oh. Uhh, yeah."
    y "I...kinda need the cash, so..."
    r "Okay, but...Why here of all places? I didn’t even know you liked coffee."
    y "I don’t."

    scene jobint11
    with dissolve

    r "Oh. Well, uhh...I guess there's technically no rule saying you {i}have{/i} to like coffee to work here, but..."
    r "..."
    r "Yeah. You know, I'm still not really getting why you chose here when that's...basically all we sell."
    s "I’ll take responsibility for that, Rin."
    s "We couldn't figure out where to go and this place was just the first one that came to mind."

    scene jobint12
    with dissolve

    r "Wait, so you two like, {i}planned{/i} this?"
    s "In a sense, yeah. I’m basically just going to take Yumi around and force her to apply to everywhere I can think of so that she doesn’t have to keep selling old TV’s until she dies."
    r "Uhh...Okay, well...first off, what?"
    r "And secondly-"

    scene jobint13
    with dissolve

    r "{i}What?{/i}"
    s "That’s a fair reaction. I can imagine it's probably really weird seeing the two of us together like this out of seemingly nowhere."
    y "Ain't just {i}seemingly{/i}. It's literally nowhere. I hate being around you, remember?"
    s "Again, yes. Thanks, Yumi."

    scene jobint12
    with dissolve

    r "{i}Weird{/i} would be an understatement, Sensei."
    r "You know that baby in a jar that Norman Reedus has to carry around in Death Stranding? This is like that, but somehow even weirder."
    s "Than a baby in a jar?"
    r "Than a baby in a jar."
    y "I'm gonna go ahead and interrupt whatever the fuck is happening here to remind you two that I'm here to make money."

    scene jobint14
    with dissolve

    r "Yeah, so, I’m not really sure if we’re hiring, but I can go grab my manager from the back if you wanna go take a seat near the door."
    y "Yeah, sure. Do I need to like, fill something out or whatever?"
    r "Nah. She’ll probs just wanna talk to you or something. She’s chill. Huge boobs, too."

    scene jobint15
    with dissolve

    y "Uhh...cool?"
    r "Frickin' {i}gigantic.{/i}"
    y "..."
    r "I just don’t want you to feel threatened by her womanly presence."
    y "...Yeah, I think I'll be okay."
    r "Anyway, hang tight for a sec. I'll go get her."

    scene jobint16
    with dissolve

    y "Why is everyone in our class so fucking weird?"
    s "Oh, come on. Rin isn’t that bad."
    y "Doesn’t she like, collect skulls and shit?"
    s "..."

    scene black
    with dissolve2

    s "Fair point."

    "I guess Yumi understands that she's about to be interviewed, so she walks directly past me and makes her way over to a chair in the corner of the room."
    "I try to follow her but she waves me off and I’m forced to go sit at a different table and wait for her to finish."
    "Thankfully, I’m able to grab a seat that makes it easy to listen in once Haruka comes out of her office..."

    scene jobint17
    with dissolve2

    "Haruka sits down beside Yumi after Rin points her out."
    "Yumi, who had been sitting straight up just moments ago, begins to noticeably lose her
    composure as soon as Haruka sits down."
    "Job interviews are always intimidating, but the first few are normally ten times worse."
    "Oh well. It’s out of my hands now."
    "From this point on, it's up to Yumi to either take her fate into her own two hands-"
    "Or let it slip through her fingers like an...old TV that's too heavy to carry or something."
    "It's not my best metaphor, but it's topical and gets the job done."
    "Unlike Yumi."
    "Who doesn't have a job."
    "Okay, I'm done now."

    h "So, you're Yumi Yamaguchi, right? Rin said you’re a classmate of hers."
    y "Oh, y-yeah! We’ve been in a few classes together, actually."
    y "Going back to like...middle[school], I think?"
    h "Oh, really? That's great."
    h "I'm not sure how much she's told you about this place, but pretty much all of our employees go to your school."
    h "And if you’re any bit as good as she is at this job, I can definitely see things working out for you here."
    y "I mean...yeah. I'll do what I can."
    h "Do you have any experience in customer service, Yumi?"

    scene jobint18
    with dissolve

    y "Um...Not really. Sorry..."

    scene jobint19
    with dissolve

    h "You don’t need to apologize. You’re still young. It’s perfectly fine if you haven’t had a job yet."
    h "I didn't have my first job until after high school, so you're already ahead of the me from back then and I like to think I turned out pretty okay."
    h "Crippling loneliness aside."
    y "...Uh."
    h "You know what? How about I ask you something else, instead?"

    scene jobint20
    with dissolve

    y "Oh, sure. Yeah. Ask whatever you want."
    h "Okay, so...how about a little work-related scenario?"
    h "I'll give you a situation that might arise while you’re at work, and you'll tell me what you’d do to remedy it."
    y "Got it."
    h "Great! So, imagine you’re ringing a customer up."
    y "Uh-huh."
    h "He buys a pastry for 100 yen and pays with a 500 yen coin."
    y "400 Yen."

    scene jobint21
    with dissolve

    h "Hold on, I’m not asking about the change."
    y "Oh, my bad. Go on."

    scene jobint20
    with dissolve

    h "After you hand the customer his change back, he looks at it and says that you’re short 100 yen."

    scene jobint22
    with dissolve

    y "Wait, so the dude pays with 500 yen and wants 500 yen back as his change?"
    y "Isn’t that one of those ‘confuse the cashier’ scams?"
    h "Exactly! I’m surprised that you know about something like that despite never working in retail."

    scene jobint23
    with dissolve

    y "Hahah, yeaaah...Weird..."

    "Something about that face tells me exactly why Yumi knows about things like that..."
    "Can’t say I’m all that surprised, though."

    h "So, what would you do in that situation?"

    scene jobint24
    with dissolve

    y "Oh, easy!"
    y "I’d punch his fucking teeth in."
    h "…"
    y "Ain’t no dude scamming any place I work for. Messin’ with the business is like messin’ with me."
    y "Oh, and if any blood got on the counter or something, I’d be sure to use bleach to make sure all of it gets out."
    y "A...clean workplace is a happy workplace or however it goes. Right?"
    h "…"
    y "…"

    scene jobint25
    with dissolve

    h "…"
    y "That was a good answer, right?"
    h "Mhm. Yup."
    h "In fact, I think I've actually heard all I need to hear."
    y "Woah! That was like, totally quick! Does this mean I have the job?!"

    scene jobint26
    with dissolve

    h "Um..."
    h "You know what? How about I call you and let you know?..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene jobint27
    with dissolve2

    y "Yo! Did you hear that? She said she’s going to call me!"
    s "Yes, Yumi. I heard."
    s "Loud and clear."
    y "Hey, do I still get lunch even though the job thing was successful on the first try?"
    s "Of course..."
    s "Please buy as much as you like in...{i}celebration{/i} of your first interview..."

    scene black
    with dissolve2

    "…"
    "Maybe taking her out job hunting before teaching her about appropriate social conduct wasn’t exactly the best idea?"
    "This...is my fault."
    "I will take the blame for this."
    "I’m sorry, Haruka."
    "I’m sorry, Yumi."
    "I’m sorry, everyone."

    $ renpy.end_replay()
    $ streets15 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label streets20:
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
...
```