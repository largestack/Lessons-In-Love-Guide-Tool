# Daytime Stalking Pass
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimesoccer&go=Go)



## Event preconditions
✅Miku love greater than or equal to 0

❌firsttimesoccerfield equal to False (unknown variable)



## Next events
None

## Event properties
* ID: firsttimesoccer
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield

## Event code
File: \game\MikuEvents.rpy
Code:
```python
...
label firsttimesoccer:
    scene sky
    with dissolve2
    play music "highspeedprinter.mp3"

    "You know, after being reborn into a world where I’m suddenly expected to fulfill the role of a teacher, I didn’t really expect to be using my {i}free time{/i} to hang out at school as well."
    "But here I am, drenched in sunlight and making my way over to the soccer field for reasons unbeknownst to even me."
    "I’m not sure what I expect to get out of this exactly, but I do know that at least one of my students is a member of the soccer team, so I'm {i}really{/i} hoping she’s there."
    "Otherwise, I’ll just wind up looking like some creepy older guy wandering around the premises."
    "Which, in all fairness I kind of am. "
    "It’s just significantly {i}less{/i} creepy if I know someone and can fall back on them."
    "Even if...the person I’d be falling on is a foot shorter than me and would likely snap in half from the pressure."

    scene mikunewsoccer1
    with fade

    "I manage to spot Miku gathering up some rogue soccer balls and shouting things to a group of girls who appear to be heading back to the gym."
    "Not knowing what else to do and still mildly worried about appearing as a stalker, I make my way over to her."

    s "Hey, Miku. Good morning."

    scene mikunewsoccer2
    with dissolve

    mi "Heya! Mornin’, Sensei!"

    scene mikunewsoccer3
    with dissolve

    mi "Wait, Sensei?! What are you doin’ over here?! You some kinda stalker now or somethin’?"

    "Damn it."

    s "No. In fact, I only approached you so I {i}wouldn’t{/i} look like some kind of stalker."
    mi "So...you’re stalkin’ me to...{i}not{/i} look like a stalker? I don’t get it."
    s "I’m not stalking anyone. I just happened to be in the area and thought I’d come say hi or something."

    scene mikunewsoccer4
    with dissolve

    mi "Works for me! I hereby grant you one Miku Maruyama “Daytime Stalking Pass!”"
    mi "In fact, take a whole box of ‘em! I give you permission to show up whenever ya want from this point on!"

    scene mikunewsoccer5
    with dissolve

    mi "How come ya gotta be at school on the weekend, though? Thought all you teachers were out doin’ math problems with each other or somethin’ on those days."
    s "Teachers have lives too, you know. "
    mi "Sure don’t look like it if you’re-"
    s "I’m just very good at my job. Can we stop talking about teaching now?"

    scene mikunewsoccer4
    with dissolve

    mi "Heck yeah we can! That kinda stuff always puts me to sleep anyway."
    mi "So, you lookin’ to learn about soccer or somethin’? Haven’t really seen ya drop by the field at all and I ain’t buyin’ that you’re just here to say hi."

    scene mikunewsoccer6
    with dissolve

    mi "Wait a sec! You ain’t here to become the new coach, are you?!"
    s "Coach? Absolutely not. I have zero interest in soccer and I {i}really{/i} am only here to say hi."

    scene mikunewsoccer7
    with dissolve

    mi "Guh."
    s "Guh?"

    scene mikunewsoccer8
    with dissolve

    mi "God! Can’t a girl say “Guh” around here without a teacher jumpin’ down her pants?!"
    s "I think you mean “throat” but please proceed."

    scene mikunewsoccer9
    with dissolve

    mi "Sorry for snappin’ at ya, Sensei. It’s just been all downhill since our last coach got knocked up and had to get put on baby-watch or whatever they call it."
    s "I believe that would be “maternity leave.”"
    mi "I don’t care what it’s called. All I know is that we’re startin’ to fall behind and we were {i}already{/i} havin’ a tough time trainin’ for nationals."
    s "Nationals? Are you guys really that good?"

    scene mikunewsoccer10
    with dissolve

    mi "Good? No way. "
    mi "A few of us are pretty awesome- me being one of ‘em of course. But a lot of the girls are like headless chickens out there, Sensei. It’s pure chaos."
    mi "I was kinda hopin’ this was gonna be like a sports anime and you were gonna show up and be all like “I used to play soccer before I stepped on a landmine” and then drop knowledge bombs on us."

    scene mikunewsoccer3
    with dissolve

    mi "Oh, crud! Sorry for wordin’ it like that. I’m sure it ain’t easy hearin’ the word “bomb” used so casually after the whole thing with your leg."
    s "Again, I know absolutely nothing about soccer and I am mostly confident that I have never stepped on a landmine."

    scene mikunewsoccer11
    with dissolve

    mi "Today just keeps gettin’ worse..."

    scene mikunewsoccer12
    with dissolve

    mi "Guess it wouldn’t change much even if I did get my sports anime wish, though. "
    mi "With the whole space war thing goin’ on, none of us are allowed outside of the barrier anyway."
    mi "With no teams from other prefectures to play, it’s kinda like the entire soccer team is just one giant, headless chicken."
    s "Do you know any other analogies or is that the only one?"

    scene mikunewsoccer10
    with dissolve

    mi "I don’t even know what an “analogy” is so that’s probably the only one."

    "I guess the journal thing in my room was right about Miku not being the brightest girl out there."
    "It wouldn’t be fair if she was gifted in both sports {i}and{/i} studies, though. It’s normally just one or the other for people."
    "Or neither, if you’re really unlucky."
    "But hey, at least Miku’s got {i}something.{/i}"

    s "I guess definitions aren’t really important as long as you’re not failing all of your tests. "
    mi "..."
    s "You’re failing all of your tests, aren’t you?"

    scene mikunewsoccer13
    with dissolve

    mi "You’re my teacher! Shouldn’t you know?! "
    mi "Makoto’s doin’ all she can to help me, but there’s only so much room in my brain for all that smart person stuff!"
    mi "I swear, I really don’t get why she wants to stay friends with me sometimes when I’ve got pretty much nothin’ I can do for her."
    s "You and Makoto are friends?"

    scene mikunewsoccer4
    with dissolve

    mi "Best friends, actually! Roommates too. We’re like two peas in a pod if the...pod only had two peas in it? How many peas are normally in a pod? "
    s "I have no idea, Miku."
    mi "Some kinda teacher you are. Not knowin’ about peas and showin’ up to soccer practice to stalk the star player."
    s "Hey, I have unlimited daytime stalking passes. I am allowed to be here."
    mi "Didn’t say ya weren’t. I think it’s great that ya wanna spend so much time around young girls. Means you’re still in touch with your youthful side."
    s "Yup. That is exactly what that means."
    mi "You like any kinda sports at all, Sensei? Baseball? Tennis? Hermit crab racing?"
    s "Not really. I’ve always- wait, what was that last one?"
    mi "Hm? Tennis?"
    s "No, the...actually, forget it. I don’t like any sports. "
    s "In fact...I don’t really like anything now that I actually think about it."

    scene mikunewsoccer3
    with dissolve

    mi "Well then how the heck do ya look all muscley and stuff? If ya didn’t just tell me you’re some kinda couch potato, I’d think you were workin’ out all day every day!"
    s "This is just how I am, I guess. I’m sure your looks wouldn’t change much either if you just...dropped out of the team or something."

    scene mikunewsoccer14
    with dissolve

    mi "Miku Maruyama droppin’ out of the soccer team? No way. There’s a better chance of you findin’ the guy responsible for blowin’ off your leg."
    mi "I love soccer. I love the rush. Runnin’ around with my friends...goin’ out to family restaurants after practice..."
    mi "Even cleanin’ up all the balls is kinda fun when ya get to do it with people ya like bein’ around."
    s "Well, I am very sorry for standing between you and your affinity for balls."

    scene mikunewsoccer15
    with dissolve

    mi "You ain’t standin’ between anythin’, Sensei! I like bein’ around you too!"
    mi "If I didn’t, I woulda asked you to leave a while ago."
    mi "Besides, the fact that you’re still here makes me confident that I can get ya to agree to bein’ our new coach!"
    s "No."

    scene mikunewsoccer13
    with dissolve

    mi "At least think about it, would ya?! If we don’t get a new coach by the end of the season, the school is gonna disband us!"
    s "Are they really?"
    mi "Well...they haven’t come out and said that! But that’s what would happen if this was a sports anime!"
    s "You really need to stop equating your real life sports club to the clubs in cartoons, Miku."
    s "Though...I definitely wouldn’t be surprised if your club {i}was{/i} disbanded for the reasons you mentioned."
    s "I’m sure there are like...health hazards or something if all of you are here over the weekend unsupervised."

    scene mikunewsoccer12
    with dissolve

    mi "It ain’t like we need supervision. Heck, it ain’t even like we need {i}coaching{/i} on account of the lack of teams for us to play against. "
    mi "We just need somebody who doesn’t mind occasionally bein’ around a bunch of girls in tight shorts to sign their name on a sheet of paper so we can keep doin’ what we love doin’."
    s "That really should have been your pitch from the get go. That sounds a lot more enticing."

    scene mikunewsoccer16
    with dissolve

    mi "Just wait ‘til ya see my vice captain. She’s got thighs so crazy they’ll give ya nightmares. Abs so hard they’ll...give ya nightmares too!"
    mi "What I’m gettin’ at is that you’re gonna have a bunch of nightmares, Sensei! So you better be prepared!"

    "As much as I like the idea of surrounding myself with other versions of Miku...I really don’t know if I’ll have the time to do this whole coaching thing."
    "There’s no way it will be as easy as just signing my name on a sheet of paper and staring at thighs."
    "Especially not when even keeping up with this conversation has been harder than normal for me."

    s "I...don’t know, Miku."

    scene mikunewsoccer4
    with dissolve

    mi "Then I’ll just have to keep botherin’ ya!"
    mi "You do plan on comin’ back, right? I’m sure I ain’t alone in thinkin’ that a boy bein’ around might help some of the girls kick it into overdrive, if you know what I’m sayin’."
    s "I want that to be a compliment, but I’m pretty sure it’s because almost all of the other men around here are gone."
    mi "That just means you’ve got more options to choose from! Tons of young, spunky soccer players- ripe for the pickin’!"
    s "For someone who loves being around her friends so much, you sure don’t seem to have a problem with handing them off to someone twice their age."

    scene mikunewsoccer17
    with dissolve

    mi "Think of ‘em as bargaining chips, Sensei. If you start dependin’ on ‘em and then I cut off your supply...you’ll {i}have{/i} to be our coach."
    mi "And that’s the bottom line, cause Miku Maruyama said so."
    s "Miku."

    scene mikunewsoccer7
    with dissolve

    mi "Guh. Don’t say it. It’s hard enough to stay motivated when all ya can do is run around in circles like some kinda-"
    s "If you mention headless chickens again, I am going to deflate every soccer ball on this field."

    scene mikunewsoccer13
    with dissolve

    mi "Hold on there, Bill Belichick! You think you can just walk onto {i}my{/i} soccer field and start touchin’ {i}my{/i} balls?! You ain’t earned the right!"
    s "That’s fine, because hearing you word it that way killed any desire I would have possibly had to do it anyway."

    scene mikunewsoccer17
    with dissolve

    mi "Mwahahah! Miku Maruyama wins again! A true champion of justice and soccer!"
    s "But not Nationals."
    mi "..."
    s "You know. Since you’ll never be able to make it, I mean."
    mi "..."
    s "..."

    scene mikunewsoccer18
    with dissolve

    mi "Gimme back that friggin’ day pass."

    scene black
    with dissolve2

    "Miku revokes my box of imaginary day passes, but that’s okay."
    "Because even if I have no intention of becoming the coach of this team, I still plan on showing up again."
    "Just like how I plan to learn more about Miku and ultimately use that as leverage to find my way into her extremely tight shorts."
    "That still seems miles away at this point, of course."
    "But something about seeing her sprint toward her goals makes me want to sprint toward mine..."
    "Even if they’re on the opposite side of the world."
    "As I turn around to leave the field, a ball crashes into my back with so much force that it almost knocks me over."
    "I think about glancing behind me to see whether or not this was intentional-"
    "But the sudden addition of Miku’s childish laughter blending in with the pre-existing medley of vigorous youth answers that question better than any glance possibly could."

    $ renpy.end_replay()
    $ firsttimesoccerfield = True
    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdayafternoon

label soccer2to4:
    play music "highspeedprinter.mp3" fadein 2.0
    scene soccerfield
    with dissolve

    "I walk over to the soccer field to see how Miku and the rest of the team are doing."
    "She notices me right away and runs up to me with the same level of excitement as always."

    if soccer20 == True:
        "I thought her enthusiasm might have died down a bit after I became the coach, but it's become easily apparent that this is not the case."
        "Regardless, I take a seat on the sidelines and watch as a group of attractive and fit [teenage]girls kick a ball around."
        "It's something I wouldn't mind watching all day, but eventually practice comes to an end and I need to find something else to do..."

    else:
        "Just like she does every time I'm here, Miku tries coaxing me into being the new coach."
        "Knowing absolutely nothing about soccer, I decline and Miku goes back to yelling
        at the rest of the girls to speed up."
        "I stay and watch for a little while before realizing that I probably
        look like a creep and decide to get on with the rest of my day..."

    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label soccer5:
...
```

## Code that triggers this event
File: \game\MikuEvents.rpy
Code:
```python
...
label soccerfield:
    if miku_love >= 0 and firsttimesoccerfield == False:
        jump firsttimesoccer
...
```