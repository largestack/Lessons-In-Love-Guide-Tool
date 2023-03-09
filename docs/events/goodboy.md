# Good Boy
Happy scenes event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=goodboy&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: goodboy
* Group: Happy scenes
* Triggered by label: saturdayafternoon
* Triggered by branch label: saturdayafternoon

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label goodboy:
    scene black
    play sound "pop.mp3"
    stop music

    "Today, I am going to be a good boy."

    if bonus == True:
        scene sky

        "I buckle my belt and tie both my shoes, cause that’s what all the good boys do."
        "I put on my backpack and fasten my gloves, cause that is what a good boy does."
        "I shoveled the driveway and vacuumed the floor. I folded my laundry, I did all my chores."
        "I washed the whole house, I cleaned all our rooms. I took out the garbage, pulled hair off the brooms."
        "I fed both the dogs so they wouldn’t bark. Can I go outside now? I’ll be home before dark."
        "I’ll look both ways when I’m crossing the street. I’ll eat all my veggies and say no to sweets."
        "I’ll take off my pants, stay quiet for you. I won’t tell a soul. I promise it’s true."
        "I’m such a good boy, so why can’t I play? Why can’t I have friends? I’ll do what you say."
        "I’m such a good boy. Obedient too. So easy to touch, so easy to use."
        "So easy to break, yet you always play rough. I’m such a good boy. Can’t that be enough?"
        "I buckle my belt and tie both my shoes, cause that’s what all the good boys do."
        "I put on my backpack and keep my mouth shut. Then saunter to school with a pain in my gut."
        "Today, I am going to be a good boy."

    scene goodboyneg1
    play music "justbehappy.mp3"

    "Weather."
    "I take in the scenery as I make my way down the street and, strangely enough, the nice spring breeze actually cheers me up today."
    "Normally, the feeling of wind against my cheeks annoys me since I learned very early on in life that most diseases are transmitted through the air and, well, I’ve just always equated {i}more{/i} air to bad."
    "Today, I’m fine with taking my chances, though. "
    "Because today, I'm going on an {i}adventure.{/i}"
    "I heard through the grapevine that there’s a wonderful place nearby where dreams can become reality."
    "I’m not sure where I heard it but, then again, I’m not really known for my above average memory."
    "In fact, I’d probably forget to even eat if it weren’t for my wonderful [niece] Ami, who is always doing things to make me happy."
    "I am very glad that Ami exists because Ami is good."
    "Ami is so cute."
    "Sometimes, when I’m looking at Ami, I can even remember extra things."

    if bonus == True:
        "They normally vanish after a few seconds, though, because I would prefer to think of other things like sex or boobies."
        "Boobies are so great."

        s "I hope I see boobies today..."

    play sound "pop.mp3"
    scene goodboy0
    with hpunch

    a1 "Surprise!"
    s "Woah! What are you two doing here?"

    "The figure on the right and I do our celebratory dance together- the one we practiced in the corridors of [kumon_mi_high] before I encountered a talking net."

    a2 "We heard that you are going on an adventure!"
    a1 "Wonderful! Fantastic! Tell us more!"
    s "Hmm...Well, I don’t really have any major plans, but I was thinking of maybe taking a trip to somewhere I’m familiar with to find out if this new lease on life impacts how I see it!"
    a2 "Sounds to me like {i}somebody{/i} has been thinking about perception!"

    play sound "laugh2.mp3"

    s "Oh, you."

    "We dance again for good measure."

    stop sound

    a1 "Do you not think it is strange that the world appears so bright today?"
    a2 "That’s right! That’s right! What happened to the snow?"
    s "Hmm...that’s a good question. You know, I feel like somebody told me something about snow recently, but I can’t really remember who it was."
    a1 "Someone wonderful! Someone with eyes!"

    play sound "laugh3.mp3"

    s "Well, I’d sure hope so."

    stop sound

    a2 "It melts! Returns to the sky! Only to return when the world reverts!"
    a1 "But reverts to what?! And what is its rightful state?!"
    a2 "An excellent question! One we are too insignificant to answer!"
    s "I think you two are doing a bang-up job and should really start giving yourselves a little more credit."
    a1 "{s}ssssssssssssssssssssssssssssssssssss{/s}"
    a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"

    play sound "laugh1.mp3"

    s "I wouldn’t mind if that part stopped, though."

    stop sound

    a1 "Tell us, sinner! Who would you like to speak to?"
    s "You’ll let me choose?"
    a2 "Whoever you want! So long as we want them!"
    s "But how am I supposed to choose someone if I don’t know who you’re okay with me choosing?"
    a1 "Fall into your ideas!"
    a2 "Pick a name! Speak a name! Any name!"
    s "How about..."
    s "Maya?"
    a1 "Denied!"
    a2 "The one you speak of appears to be busy at the moment! Choose someone else! "
    a1 "We demand it! Command it!"
    s "You know, I think I’ll just let you guys choose for me."
    a2 "Excellent choice!"
    a1 "Splendid decision!"

    scene black
    with dissolve2

    "The two figures make their way over to me without walking. Their bodies glide, but not all parts of them move at the same time."
    "When all aspects are reunited, they hold their hands in the air."
    "I can feel the world around me grow hotter the higher their hands become, but I doubt that’s relevant information."

    a1 "This will hurt you! The pain will be great!"
    a2 "Your arms will bend back! Your body will ache! "
    s "Just do it already. "

    stop music

    "Without speaking any more words, the figures slip their hands inside of me."
    "They tug away at my organs as if they are levers, carefully selecting the coordinates of a certain place in a certain time."
    "I can only wonder what wonders await."

    play sound "static.mp3"
    scene happy9 with flash
    scene happy8 with flash
    scene happy9 with flash
    scene happy8 with flash
    scene happy9 with flash
    scene happy8 with flash
    scene goodboy1 with flash
    stop sound
    play music "maincharacter.mp3"

    "An unfamiliar hallway in a familiar plane of existence."
    "The scent of old textbooks lingers through the corridor like the ghosts of students past, stuck endlessly traversing the halls in hopes of uncovering some sort of escape route."
    "I recall a time when I was younger and cut my hand on the glass of a window that I attempted to climb out of."
    "I fell two stories and landed on my ankle in a way that made it incredibly difficult to walk for at least two weeks."
    "During that time, I grew closer to someone who would one day leave me."
    "Now, every time I look out a window-"
    "Or look down at my hands-"
    "Or look at anything, really-"
    "I have to remind myself to forget. "
    "I think that same reason is why the ghosts of this hall are stuck, looping around in circles for the rest of eternity."
    "But I think a lot of things-"
    "And I am seldom correct about any of them."
    "In fact, I don’t even believe in ghosts."
    "I just think the idea of this place being devoid of anything other than the scent of stale textbooks is far too lonely for even someone who’s already given up on the world."
    "So I will pretend."
    "I’ll pretend that this unfamiliar hallway is full of life-"
    "And as I make my way toward the end of it and back to the world that I call home-"
    "I will wave at every single spirit along the way."

    q "Hm? Who are you?"

    play sound "static.mp3"
    scene goodboy2 with flash
    stop sound

    "Someone appears, though I couldn’t tell you who."

    q "Are you a new teacher or something? "
    s "I..."
    s "Yeah."
    q "Well...what are you doing here now, then? School ended like five hours ago."
    s "If school ended five hours ago, what are {i}you{/i} doing here?"
    q "I don’t think there’s any rule that says I have to tell you that."
    s "And I don’t think there’s any rule that says I have to tell {i}you{/i} either."
    q "Well, then I guess we can both pretend we never saw each other and just completely forget that this encounter ever happened."

    if bonus == True:
        s "Or we can have sex."
    else:
        s "Or we can hug."

    "I decide to shoot my shot because this is obviously a delusion."

    q "You...do realize I’m a student, right?"
    s "Yeah. But that’s never really stopped me before."
    q "Ah. So you’re one of those."
    s "Are you one of those as well?"
    q "Sorry, but I already have a boyfriend. And the two of us are pretty serious, so...yeah."
    s "Oh well. Worth a shot."
    s "I guess if we’re not going to do anything, though, could you step out of the way so I can find my way out of this dream?"
    q "Dream?...Wait, are you hallucinating right now?"

    if bonus == True:
        q "Because if you’re just pretending to be insane so you can get away with asking me to screw you, I wasn’t really planning on telling anyone."
    else:
        q "Because if you’re just pretending to be insane so you can get away with asking me to hug you, I wasn’t really planning on telling anyone."

    q "People would probably just think I’m bragging or something anyway."
    s "Are you telling me that you’re actually real?"
    q "That’s what I’m telling you, yeah."
    s "And this...hallway? Or school, I guess?"
    q "[[REDACTED]."
    s "..."
    q "I figured you’d know that since you’re apparently a teacher here."

    if bonus == True:
        q "Unless that was a lie and you’re really just here to try and snatch up some schoolgirl for your own...personal use or something."

    s "You know what? I think I’m just going to keep exploring."
    q "Oh, okay. Have fun. "
    q "Can I ask you something before you go, though? From one totally random person who was never here to another."
    s "Sure. "
    q "Then..."
    q "Are you a good boy?"

    play sound "pop.mp3"
    scene goodboy3

    s "Wha-"

    "The girl pops."
    "Several feet behind her and in the center of the hall, a chair appears."
    "I’m competent enough right now to understand that this feels like something out of a horror movie, but it doesn’t change the fact that I feel compelled to sit down."
    "But I guess in a school with no one there, there’s not much else to do."
    "Even if I were to continue exploring, I doubt I’d find anything of value."
    "There might be an outdated encyclopedia or an old anatomical dummy still tucked away somewhere unseen, but I’m not sure how plausible it is to carry something back from a dream."
    "Nor am I even sure if this is a dream anymore to begin with based on the testimony of the girl who just popped."
    "Oh well."
    "I guess I’ll sit on the chair after all."
    "And if I pop, I pop."
    "At least then, I’ll know if any of this is actually happening."

    scene black
    with dissolve2

    "On my way to the chair, I hear another set of footsteps, but see no one at all."
    "As I sit down, the scent of cherry blossoms joins forces with that of the old books."
    "And while I don’t particularly dislike it-"
    "It makes me want to vomit."
    "I’m glad I decided to sit down, as I’m suddenly feeling very dizzy."
    "And as the acids in my stomach strap on their climbing gear and begin their ascent through my esophagus, I begin to realize that this is significantly more real than I want it to be."
    "I don’t want to adventure anymore."
    "I want to go home."

    scene goodboy4
    with dissolve2

    "Life is filled with treasures in every little thing. We just normally have to move a hideous looking rock or two before picking them out of the dirt."
    "But once we clean them off, killing away the bacteria and insects, we can watch in awe as they spring back to life in the palms of our hands."
    "Squirming around like little, glowing maggots- those treasures begin to take form. "
    "And while that form may appear like nothing more than another hideous rock to someone else, the fact that they sprung to life in {i}our{/i} hands makes us love them."

    s "..."

    "This chair is far more comfortable than I want it to be."

    av "{i}You’re such a good boy.{/i}"

    "One more thing I’ve found that I hate about this new environment is how, in its decay, the walls of this building have developed cracks."
    "Those cracks are able to mangle the sounds of wind, converting them from something I already dislike into something that makes me wish I’d never woken up this morning."
    "I know no one else is here, but I can’t shake the feeling that I’ve been being watched since I first heard footsteps."
    "Even now, the footsteps grow closer."
    "Louder."
    "They surround me- mixing with the wind as it once again assaults my skin."
    "And while my instinct is to cover my face to avoid disease, the parts of me that have grown tired of living a life of avoidance keep them strapped down."
    "The contaminated air finds its way into my lungs."
    "It becomes a part of me."
    "I am infected."

    play sound "static.mp3"
    scene goodboy5
    with flash
    stop sound

    "Sometimes, when I don’t have anything else to think about, I like to focus really hard and see if I can feel my blood move through my veins."
    "I don’t know why I felt compelled to tell you that, but you’re all I have to talk to in here."
    "And since you never say anything, I’m the one who needs to fill the void."
    "What is it that {i}you{/i} would like to talk about?"
    "You can choose any topic you like."
    "So long as it’s the topic I want you to choose."

    play sound "static.mp3"
    scene imissyoumore with flash
    scene help with flash
    scene imissyoumore with flash
    scene help with flash
    scene imissyoumore with flash
    scene help with flash
    scene goodboy6 with flash
    stop sound

    te "Let me see your hand."
    s "It’s fine..."
    te "And how about your ankle? Do you think you can walk?"
    s "I’m fine..."
    te "Reeeeeeally?"
    te "Don’t tell me you’re too embarrassed to accept a piggyback ride from your [[REDACTED]."
    s "You’re a girl. It’s not right for a girl to help a boy like that."
    s "I’m supposed to be strong."
    te "Heheh~"
    te "You’re such a good boy."
    s "Stop saying that..."
    te "Why? It’s true."
    te "You’re so much nicer than your big brother."
    te "Did I tell you what he did to me the other day?"
    s "Can we talk about something else?"
    te "Like what? Are you gonna brag to me about your {i}girlfriend{/i} again? Because I’m starting to think you might be {i}trying{/i} to make me jealous."
    s "She’s not my girlfriend..."
    te "Why not? She likes you, doesn’t she?"

    if bonus == True:
        s "..."
        te "{i}Do you jerk off to her?{/i}"
        s "Stop it! Seriously!"
        te "Hahaha! You so, totally do!"
    else:
        s "I'm just not ready for that kind of commitment."

    play sound "pop.mp3"
    scene goodboy7

    "A sudden popping noise drags me back to reality and I notice that I must have dozed off for a second."
    "It’s gotten a little darker since I last looked outside, so I’m pretty sure that I’ve been in...wherever this place is for at least a few hours."
    "And as much as I’d like to head home, I still don’t even know how to get out."
    "I’ve learned in the past that windows are unreliable, and every single staircase in this corridor has been blocked off by colossal mounds of dirt and rubble."
    "I’m not...going to die here, am I?"
    "Am I?"
    "Ami?"
    "I should text Ami."
    "Ami will know what to do."
    "Ami is so cute. Ami always helps me no matter what situation I’m in."
    "I can trust her."

    play sound "phonebeep.wav"
    scene black

    "I tap on Ami’s name in my phone and wait for her to answer."
    "........."
    "........"
    "......"
    "....."
    "...."
    "..."
    ".."
    "."
    ".."
    "..."
    "...."
    "....."
    "......"
    "......."
    "........"
    "........."

    play sound "pop.mp3"
    scene goodboy8
    stop music

    "{i}You did it!{/i}"

    if bonus == True:
        "{i}You made it through the event without molesting a girl!{/i}"
        "{i}All of that hard work and harsh training must have paid off!{/i}"
        "{i}For a limited time, please enjoy being a trophy!{/i}"
        "{i}Your limbs will return to normal the second we think they should.{/i}"
        "{i}But, in the meantime, please remember that bad things only happen to bad children!{/i}"
        "{i}And, so long as you be good, you’ll live a happy, carefree life! Where everyone loves you and {i}thinks you’re going to do great things.{/i}"
        "{i}Are you going to do great things? {/i}"
        "{i}You’re a good boy now, but how long will that last?{/i}"
        "{i}How long until you start wanting to do {i}bad{/i} things?{/i}"
        "{i}Bad things are bad! And good things are good!{/i}"
        "{i}So just do what you’re told and everything will turn out a-okay!{/i}"
        "{i}I love you so much.{/i}"
        "{i}If I didn’t, why would I do this?{/i}"
        "A hand reaches out and [[REDACTED] [[REDACTED] my [[REDACTED]."
        "I’m scared that I might [[REDACTED], but [[REDACTED] assures me that it’s totally normal if I do."
        "She [[REDACTED] my [[REDACTED] and some of the blood from my hand gets into her hair."
        "It’s hard to see because of the color, but that doesn’t stop me from trying to focus on it as she continues to [[REDACTED]."
        "Before long, we [[REDACTED]."
        "The cut on my hand opens back up."
        "I think it’s infected."

    scene black

    "///////////////////////////EVENT OVER"
    "........."
    "......"
    "..."

    if bonus == True:
        play sound "imscared.mp3"
        scene goodboy9
        play music "shiningstarvocals.mp3"
        $ renpy.pause(5, hard=True)
        scene goodboy10 with dissolve4
        $ renpy.pause(5, hard=True)
        scene goodboy11 with dissolve4
        $ renpy.pause(5, hard=True)
        scene goodboy12 with dissolve4
        $ renpy.pause(5, hard=True)
        stop music fadeout 9.0
        scene goodboy9 with dissolve4
        $ renpy.pause(5, hard=True)
        play sound "sponsor.mp3"
        scene goodboysponsors
        $ renpy.pause(6, hard=True)
        scene goodboy9 with dissolve2
        $ renpy.pause(3, hard=True)
        play sound "static.mp3"
        scene goodboy10 with flash
        stop sound
        play music "isingforyou.mp3"

        sev "Thank you for coming."
        sev "We have all been waiting with bated breath."
        s "What...is this?"
        s "Who are you?"
        sev "I am the host of today’s talk show event, and you are our very special guest."
        sev "I would like to thank you for coming and agreeing to pour your heart out onto the floor beneath us."

        "I stand at the edge of a stage I never wanted to set foot on, searching for shade to avoid having my skin singed by the spotlights spread out above me."
        "There is no audience, just a small camera crew and a blue sky spreading so far that it feels as if we’re suspended in mid air."

        sev "I would like to begin the show with this question first:"
        sev "How did you wind up here today?"
        s "I don’t want to be here."
        sev "If you don’t intend to answer the questions properly, we will have you removed from the show."
        s "Yes, please. That is what I want."
        sev "Are you sure about that?"
        s "What? Of course I'm-"

        play sound "pop.mp3"
        scene black

        s "I can’t see! What’s going on?"
        sev "I had your eyesight taken away."
        sev "You see, this is a very special program. And here, we’re allowed to do very special things."
        sev "Being removed from the show doesn’t mean you just get to go home, of course."
        sev "It means your entire existence is wiped clean."
        sev "And something like that would make {i}me{/i}, in particular, very {i}very{/i} sad."
        s "Okay, fine. I’ll do what you want. Just-"

        play sound "pop.mp3"
        scene goodboy9

        sev "Splendid."
        sev "So, how is it you ended up here today?"
        s "I have no idea. I was just...doing what I normally do and wound up here."
        sev "Were you?"
        s "Yes. I’m...pretty sure I was."
        sev "Hmm..."
        sev "Well, there’s no rule against {i}lying{/i}, so I suppose we can just move on to the next question."

        scene goodboy10
        with dissolve

        sev "You’re sitting at the computer with your friends and family in the room right behind you. They’re not paying much attention to what you’re doing."
        sev "Then, suddenly, you accidentally click on a pop up for a porn site and know that, within seconds, a video is going to play."
        sev "Your speakers are on full blast because it’s actually a Christmas party, and the Christmas music is about to be replaced with audible sex noises."
        sev "How do you handle the situation?"
        s "This is what you’re threatening to take my vision away for?"
        sev "I’m just trying to get to know you better."
        s "Whatever. I unplug the computer as quickly as I can."
        sev "Noooo, don’t do that. You’ll hurt it."
        s "I really don’t care."
        sev "Well, you should. Computers are important."
        sev "You’ll never know when one might come in handy."
        sev "In fact, you might owe a lot more to computers than you think!"
        s "Are you going to tell me how? Or am I just going to have to pretend to understand what you’re talking about?"
        sev "All I’m saying is that we don’t get to do this program very often and that you should maybe be a {i}little{/i} more cooperative if you want to be a return-guest."
        sev "But, with that, I will now turn things over to our senior correspondent, Moyo Makinamo."
        sev "Take it away, Moyo."

        scene goodboy14 with dissolve

        moyo " "
        s "..."
        moyo " "
        s "..."
        moyo " "

        play sound "moyo.mp3"
        scene goodboy15
        $ renpy.pause(2, hard=True)
        scene goodboy14
        stop sound

        sev "I couldn’t have said it better myself."

        "Before I can even think of a response to the ear piercing shriek I just heard, I find myself once again fighting back the urge to vomit, albeit with much less success this time."
        "Within seconds, I’m spewing a mixture of yellowish bile and what I think might be blood onto the tiled floor."

        sev "Don’t worry about cleaning that up, it will evaporate within seconds."
        sev "But, seeing as I forgot how Moyo is unable to speak without the vibrations of her voice causing the liquids in human innards to boil, let’s just move on to our third speaker."

        scene goodboy12
        with dissolve2

        sev "Chair, do you have anything you’d like to ask our guest?"
        chair "..."

        "I finish coughing up bile and look at the chair."
        "I know I’m being toyed with at this point, but there’s not really anything I can do about it without risking my eyesight and...whatever else these {i}people{/i} can take from me."

        sev "I see, I see."
        s "Would you mind translating for me?..."

        play sound "static.mp3"
        scene goodboy13 with flash
        stop sound

        sev "Translating what, exactly? It didn’t say anything."
        sev "In fact, Chair has yet to say {i}anything{/i} in any episode of this program. But we’re still holding out hope that it does one day."
        s "It might be time to find a replacement for that {i}speaker{/i} then."
        sev "We had a fourth, but she stopped coming for some reason."
        sev "I think she may have just gotten bored."
        sev "But anyway, we’re running out of time, so I’d like to ask you one final thing before we conclude today’s show."

        play sound "static.mp3"
        scene goodboy16 with flash
        stop sound

        sev "Our records show that, in addition to various illicit relationships with your students, you’re also engaging in a sexual relationship with a student’s mother."
        sev "Would you be willing to speak more about this relationship?"

        if sarasex == True and makisex == True:
            s "Which...one are you referring to?"
            sev "Unfortunately, the rules of our program prohibit me from releasing the name."
            s "Then...I don’t really think I have anything to say about it other than...they’re a consenting adult that wanted to have sex with me."

        else:
            s "Is this about Sara?"
            sev "Perhaps! Unfortunately, the rules of our program prohibit me from releasing any names."
            s "She’s...just a normal, single mom who runs a bar."
            sev "Normal? Are you willing to elaborate on this detail?"
            s "Well, maybe {i}normal{/i} isn’t the right word since she’s had her fair share of hardships."
            sev "I see here that she lost both a son {i}and{/i} her significant other. That sounds like a tough break."
            sev "Do you think she’s any happier now that she gets to experience the sensation of your oversized sex organ inside of her?"
            s "Excuse me?"
            sev "The desire to have sex without intent to procreate is one that has been ingrained in humans throughout their entire existence."
            sev "In fact, there are several species known with recorded evidence of recreational sex."
            sev "I am just attempting to understand if there is more to the relationship between you two than simply the compulsion to rub your genitals together."
            s "..."
            sev "..."
            s "I don’t know. Maybe?"

        scene goodboy17
        with fade

        sev "Great!"
        sev "Well, that pretty much wraps up today’s show."
        sev "I’d like to take another moment to thank our guest for sharing his thoughts with us- and our sponsors for keeping this show on the air for several million years now!"
        sev "We’ll see you again next winter with a lineup of new questions and, who knows? Maybe even a new speaker!"
        sev "But, until then-"
        sev "Stay beautiful-"
        sev "Stay happy-"
        sev "And stay good!"

        scene black
        with dissolve2

        "{i}This episode of “TV Show” was filmed in front of a live human.{/i}"
        "The world around me collapses into nothing."
        "On the way down, I see a barrage of memories disguised as sculptures."
        "But I know that once I hit the ground, I won’t remember any of them."
        "I won’t remember any of {i}this-{/i}"
        "And I’ll be forced to move on with my life like none of it ever happened."
        "I’ll go back to living in the shadows."

        stop music

        "I'll go back to being a good boy."

        $ renpy.end_replay()
        $ anewkey = False
        $ goodboy = True

        "........."
        "......"
        "..."

        "{i}I forget it all.{/i}"

        jump saturdaynight
    else:
        $ renpy.end_replay()
        $ anewkey = False
        $ goodboy = True

        jump saturdaynight

label christmastwo1:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label saturdayafternoon:

if totaldays >= 38 and firsttimepornshop == True and day36 == True and day38 == False:
    jump day38
else:
    "Now what should I do?"

    menu satafternoonmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Archery Range" if chapthreeactive == True:
                    jump tsuneyoarchery
                "City Streets" if firsttimeshrine == True:
                    jump streets
                "Shopping Mall" if firsttimeshrine == True:
                    jump mall
                "Shrine":
                    jump shrine
                "Dojo" if firsttimeshrine == True:
                    if osakodate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang Out With Ayane":
                                jump dojo
                            "Hang Out With Osako":
                                jump osakodojo
                    else:
                        jump dojo
                "Bathhouse" if day247 == True:
                    jump bathhouse
                "Library" if day288 == True:
                    if otohadorm1 == False:
                        "I should make sure Nodoka is settled into the dorm first before visiting her at the library."
                        jump satafternoonmenu
                    else:
                        jump nodokalibrary
                "Go Back":
                    jump satafternoonmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_afternoon

        "Call someone" if use_new_phone_ui == False:
            jump callafternoon

        "Wait until night" if firsttimeshrine == True:
            s "I'll just...walk around until it starts to get dark, I guess."

            scene black
            with dissolve
            stop music fadeout 3.0

            "I decide to wander around for a few hours."
            "........."
            "......"
            "..."

            jump saturdaynight

        "Wait until morning" if anewkey == True:
            jump goodboy
...
```