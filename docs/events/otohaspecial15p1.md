# King Midas (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Otoha love greater than or equal to 15

* Event [How To Make Love Stay](./nikilovesyou3.md) (Niki) is completed)

* Day of week is Sunday

* Event [White People](./otohaspecial15p2.md) (Otoha) must not be completed)



## Next events

None

## Event properties

* Id: otohaspecial15p1
* Group: Otoha
* Triggered by label: dormweekend
* Triggered by branch label: dorms
* Triggered by path: dorm2weekend->dormweekend->otohaspecial15p1

## Official wiki page

[King Midas](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohaspecial15p1&go=Go) for more details.

## Event code

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohaspecial15p1:
    scene otohasnewhair1
    with fade

    if _in_replay:
        play music "sweetvermouth.mp3"

    "I make my way into the dorm and, before I even have the chance to knock on anyone’s door, I find Rin hesitantly standing outside of room eight. "

    play sound "glass.mp3"
    with hpunch

    "And I now understand why."

    s "Is Nodoka broken again?"
    r "It’s been going on for like five minutes. I just want to kiss my girlfriend. "
    s "Let's hope it ends soon because I want to watch you kiss your girlfriend."
    r "You might have to hide outside the door and just peek in. I’ll leave it cracked for you. Otoha doesn’t like being watched, I don’t think. Or, I don’t know. Maybe she does. But I’m too scared to ask right now."
    s "I’ll go fill up a bucket of water that we can dump on her or something."

    scene otohasnewhair2
    with dissolve

    r "Are you trying to tell me I can’t get my girlfriend wet?"
    s "I was talking about Nodoka. But I can grab a second bucket for Otoha if you aren’t feeling very confident in yourself. "
    r "Better to air on the side of caution. Grab three buckets just in case something goes wrong with me as well."
    s "On it."

    play sound "dooropen.mp3"
    scene otohasnewhair3
    with dissolve

    no "What’s this about buckets?"
    r "Woah. You look pretty good for someone who was having a manic breakdown like, five seconds ago."

    scene otohasnewhair4
    with dissolve

    no "Breakdown?"

    play sound "glass.mp3"
    with hpunch

    no "I’m afraid I have no idea what you’re talking about."
    r "Sensei...she’s got telekinesis now...don’t make any sudden movements."
    s "Is that...Otoha throwing shit around in there?"

    scene otohasnewhair3
    with dissolve

    no "There comes a time in the spring of youth when we must {i}all{/i} throw something against the wall. Natsume Soseki said that."
    s "No he didn’t. "

    play sound "glass.mp3"
    with hpunch

    no "Okay. Maybe he didn’t. But I did just now and, let's face it- he wasn't {i}that{/i} much better than me. "

    scene otohasnewhair5
    with dissolve

    r "That’s...Otoha doing that? Why? She seemed fine when we were texting a few hours ago."
    no "Oh. That was me. Surprise."
    r "But I...told you I love you."
    no "And I love you too, Rin. If it were not for your relationship with my roommate, I’d have my tongue so far up your-"
    r "Please don’t finish that sentence."
    s "Please finish that sentence. "
    no "...vagina that I would be able to lick your tonsils."
    r "Are you...an eldritch horror now?"
    no "You can call me Azathoth. Azzie for short. Now, I believe we were about to make out?"
    r "No...I {i}believe{/i} you were about to tell me what’s going on with my girlfriend."
    no "There’s nothing going on with your girlfriend."

    play sound "glass.mp3"
    with hpunch

    r "..."
    no "Okay. There may be something going on with your girlfriend."
    no "But it’s no more than a standard case of the plight of the artist."
    no "In times like these, it is best to leave people like Otoha alone until they finish what they started."
    s "Now, despite how much experience I’ve gained throughout the undisclosed amount of time I’ve been here, I am no expert when it comes to the woes of an ailing female."
    s "However...I have a hard time believing it’s best to leave Otoha to her own devices if she is currently breaking glass all over your bedroom."

    scene otohasnewhair6
    with dissolve

    no "I break glass all over my bedroom all the time and you never come to {i}my{/i} rescue. And to think that I’ve been looking up to you as a father figure this whole time."
    s "I {i}do{/i} come to your rescue. You’re just beyond saving."

    scene otohasnewhair7
    with dissolve

    no "Aww...Daddy..."
    r "I won’t stay long...I just want to check up on her and make sure she’s doing okay."

    scene otohasnewhair8
    with dissolve

    no "Okay. But it won’t be pretty and you can’t say I didn’t try to warn you."
    no "Now, if you two will please excuse me, I have several prior engagements to tend to."

    scene otohasnewhair9
    with dissolve

    no "Oh, and under no circumstance should you attempt to touch her. I made that same mistake once just to see what would happen and it did {i}not{/i} go very well."
    no "Have fun!"
    r "..."
    s "..."
    s "So, it looks like it wasn’t Nodoka after all. "
    r "I didn’t even realize Otoha had a side like this..."
    r "Is it really okay to go in there? Shouldn't we just...leave?"
    s "Well...was it good for you those times I walked in on you at {i}your{/i} darkest?"
    r "I don’t know. Maybe? But if I didn’t know about this side of her, it means she’s probably been keeping it a secret on purpose, right?"
    r "What if she doesn’t want me to see her like that?"
    s "Only one way to find out."
    r "..."
    s "..."

    scene black
    with dissolve2
    stop music fadeout 5.0
    play sound "dooropen.mp3"

    r "Yeah...I’m just here to check on her. And if she wants us to leave, we’ll leave. "
    r "It’s that simple..."

    play sound "static.mp3"
    scene otohasnewhair10 with flash
    stop sound
    play music "allofthesounds.mp3"

    "{s}Except it isn’t.{/s}"

    o "Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad.
    Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad. Nothing rhymes with sad."
    r "Uhh...Otoha?"

    scene otohasnewhair11
    with dissolve

    o "Otoha isn’t here. Go away."
    r "I just...wanted to see if you were doing okay. It was pretty loud out in the hall-"

    scene otohasnewhair12
    with hpunch

    o "{b}WHAT FUCKING PART OF “GO AWAY” DO YOU NOT UNDERSTAND?! I’M WORKING!{/b}"
    r "Y-Yeah! Okay...Okay. That’s fine."

    scene otohasnewhair13
    with dissolve

    o "Oh. Crescendo. I don’t need words to get it across if everything the words are built {i}around{/i} starts spinning. Spinning and climbing."
    o "I will reach the top one way or another. It doesn’t matter how it happens, it just matters that I get there. If I get there, things will be good again. I have to make them good. I have to be good."
    o "I’m amazing. A prodigy. Everything I touch turns to gold."
    o "King Midas! Metaphor! Speak through symbols when nothing else can show how you feel! I will be heard. You will hear me."
    r "Uh..."
    s "Are you ready to leave yet?"
    r "I don’t really know...my mind is telling me no, but-"
    s "But your body is telling you yes?"
    r "This really isn’t the time for early 90’s pop culture references, Sensei. And you know things are bad when even I’m saying that."
    s "I couldn’t help myself and I’m sorry."
    r "What I was saying is that my mind is telling me no, but my heart is telling me that Otoha might need me right now."

    scene otohasnewhair15
    with hpunch

    o "{b}OTOHA, THIS! OTOHA, THAT! CAN’T YOU SEE I DON’T NEED ANYONE?! I CAN FUNCTION ON MY OWN! NOW LET ME WRITE IN FUCKING PEACE!{/b}"
    s "I’m starting to think Nodoka was right. Which is annoying because she’s kind of always right and there’s no way things can stay that way forever."

    scene otohasnewhair16
    with dissolve

    o "That way forever...something-something...clever?...In the...something...December...something remember! That’s it! The bridge is finished! I’ll fill in the blanks later! I’m a genius."
    s "Maybe the bucket would have been a good idea after all?"
    r "Otoha...can you at least look at me? Your hair’s a mess. Do you need anything to eat? A...shower maybe?"
    o "There needs to be something else...something different...a cello? Theremin? Something that will pop! To draw attention away from the parts that aren’t meant to stick the way the chorus is."
    o "But it can’t be too distracting. If it’s too distracting, {i}nothing{/i} will stick. And if nothing sticks, everything falls. Everything falls but me. I stay on top. Where I belong."
    o "{i}Somewhere I belooooong.{/i} Fucking Linkin Park, man. So good. I bet they wouldn’t struggle with fucking {i}bullshit{/i} like this. I’m a fake. I’m pathetic. Fuck you, Otoha. Fuck you. Piece of shit. You’re disgusting."

    scene otohasnewhair17
    with dissolve

    r "Hey...I’ll run to the convenience store and grab you dinner or something. After that, I’ll be out of your hair. Okay? Is there anything you want?"
    o "Dadadadaaa......dada.......daaaaa.....fuck. No. Again. From the top. Dadadaaaa-"
    s "Rin, I don’t know if that’s a good-"

    scene otohasnewhair18
    with dissolve

    r "Otoha, look at me. You don’t have to be perfect all the time if it’s weighing on you. You could always-"

    stop music
    play sound "slap.mp3"
    scene otohasnewhair19
    with hpunch

    r "Ngh-!?"
    o "{b}I TOLD YOU TO GET THE FUCK AWAY FROM ME, YOU ANNOYING PIECE OF SHIT! I’M TRYING TO WORK!{/b}"
    s "Woah. You can’t just-"

    play sound "static.mp3"
    scene otohasnewhair20 with flash
    stop sound

    o "Ah! Oh my god! Rin! I didn’t mean that! Are you okay?!"
    r "You just..."
    r "You just {i}hit{/i} me..."
    o "It was an accident! You surprised me! I’m so so sorry! Really! I get...jumpy when people sneak up on me like that!"
    r "Yeah...Yeah, I understand..."
    r "I was warned to not touch you anyway and..."
    r "I kind of just forgot...in the heat of the moment..."

    scene black
    with dissolve2

    "I take a step back and let the two of them figure this out."
    "I have no place here anyway."
    "........."
    "......"
    "..."

    scene otohasnewhair21
    with dissolve2
    play music "pianomelancholy3.mp3"

    o "Does it hurt? Are you okay? We should put something cold on your cheek so it doesn’t swell up. Holy shit, I can’t believe I just did that. Oh my god. Oh my fucking god."
    r "I’m fine...it wasn’t that hard. You just surprised me, that’s all."
    o "Rin, I’m so sorry. Hit me back to make up for it. As many times you want. I deserve it."
    r "I’m not going to hit you, Otoha..."
    o "You should! I just hit you! You’re my precious girlfriend who I’d do anything for and I {i}hit{/i} you! "
    r "Well, now you’re just making me blush."
    o "I’m so sorry. What can I do to make it up to you? Name it. I’ll do anything you want. Anything at all."

    scene otohasnewhair22
    with dissolve

    r "Did you dye your hair back?"
    o "Huh?"
    r "Your highlights are gone. When did that happen?"
    o "Uh..."
    o "I don’t...I don’t really remember...but why is {i}that{/i} what-"

    scene otohasnewhair23
    with dissolve

    r "You look...kinda {i}hot{/i} like this."
    o "..."
    o "What?"

    scene otohasnewhair24
    with dissolve

    r "Oh! Sorry. Just...one surprise after the other today."
    r "Otoha, if you want to make it up to me, just take care of yourself."
    r "I’m no stranger to locking myself away until {i}I{/i} find what it takes to move forward again. So I get it. And I’m not trying to change you or anything."
    r "This is...a new side of you, yeah. And I’m not sure why you hid it from me, but...that doesn’t matter right now. "
    r "What matters is that you eat...and maybe get some sleep...and {i}then{/i} finish your work. I’m sure the song you’re writing isn’t going to just run away on you."
    o "..."
    r "Okay?"
    o "Why are you being so nice to me?"

    scene otohasnewhair25
    with dissolve

    r "Because I fuck up all the time...You’re allowed to make a few mistakes as well."
    r "Just don’t go cheating on me or anything."
    o "You really don’t want to hit me back?"
    r "And risk damaging that beautiful face? I’ll pass. "
    r "Plus, now that it’s behind us, I actually think getting slapped was kind of kinky. I think I might be into it."
    o "..."
    r "..."
    o "Rin, I’m so sorry. I really am. It’ll never happen again."
    r "I told you. It's fine."

    scene otohasnewhair26
    with dissolve

    r "Also, Sensei is here. Say hi."
    o "..."
    s "..."
    o "Hi..."
    s "Hey, Otoha. You look fucking miserable."
    o "I’ve...had better days..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohasnewhair27
    with dissolve

    o "So, uhh...you saw all that?"
    s "I did."
    o "And...what did you think?"
    s "I think that your girlfriend is a little too forgiving and that you have a lot of work to do if you’re going to make up for slapping her across the face when all she was doing was making sure you were okay."

    scene otohasnewhair28
    with dissolve

    o "You and I might not agree on much, but...I can’t argue with any of that."
    s "On a somewhat brighter note, I now believe that you may be able to dethrone your roommates across the hall in the race for “messiest dorm room” seeing as both you {i}and{/i} Nodoka are like this."
    o "In my defense, even though I probably shouldn’t be trying to defend anything right now...she is much worse than I am."
    s "I don’t know. She’s never hit an actual person before."

    scene otohasnewhair29
    with dissolve

    o "I meant, like...in terms of...actual destruction..."
    r "Can we maybe just forget about the slap for now and try to make things normal again? I’m really not that bothered by it."
    o "There’s no way I can just forget that..."

    scene otohasnewhair30
    with dissolve

    o "I’m so embarrassed...and disappointed in myself...and so, so fucking stupid. I seriously can’t believe that just happened."
    o "And on top of that, I look like a serial killer and haven’t changed my clothes since Friday. So yeah, life’s not really coming up Otoha right now."
    r "When did this start?...And, better question, what {i}is{/i} this?"
    o "I don’t know...fucking...this just happens when I get too many...feelings, sometimes."
    o "It’s like...all I can think of is trying to write them down accurately, but then nothing ever makes sense and it drives me insane and I’ve always just...locked myself up until it was over."
    o "Just...can’t really do that anymore now that I live in a dorm with nineteen other girls. One of which I’m dating."
    o "I’m sorry you had to see me like this. Both of you. I know it’s not pretty."
    s "Well...you seem a little better now. But maybe it’d be for the best if you took a little break from writing to just...cool down or something?"

    scene otohasnewhair31
    with dissolve

    o "Cool down?! Now?! But I’m so fucking close to-"
    r "Otoha."

    scene otohasnewhair32
    with dissolve

    o "Yeah...you’re right. Sorry. I’m still kind of...caught up in the...colors...Uhh...no...No, thats not the right way to word it. Uhh...fuck. Give me a second."

    scene otohasnewhair33
    with dissolve

    r "This new song you’re writing..."
    r "It’s not about me...is it?"

    scene otohasnewhair34
    with dissolve

    o "Uhh..."
    o "I don’t...I don’t really like talking about my songs until they’re done, so..."
    r "Will you let me hear it once it’s finished?"
    o "..."
    o "Y-Yeah. Totally. You can...hear it...when it’s done. That’s fine."
    r "I’m looking forward to it..."
    o "..."
    r "..."
    s "Well...I should probably leave you two alone now that Rin is no longer at risk of being mutilated by her lover."

    scene otohasnewhair35
    with dissolve

    r "I wouldn’t mind having a bodyguard for the rest of the night now that it looks like Otoha doesn’t need to be alone anymore."
    o "I’d still...kind of like to be alone..."

    scene otohasnewhair36
    with dissolve

    r "But it would make me {i}reeeeeeeally{/i} happy if we could all go to the cafe together. And I could definitely use the pick me up after all I’ve been through tonight."

    scene otohasnewhair37
    with dissolve

    o "That’s mean...you know I can’t say no to you right now."
    r "Just for a little while? I’ve wanted to see you all weekend and I’d hate for this to be the way that ended."
    o "Are you...okay with me looking like this, though? Because I don’t really think I can do my makeup right now. My hands are all {i}blah{/i} from writing and erasing things all day."

    scene otohasnewhair38
    with dissolve

    r "Leave it to me! Years of self-mutilation have made me into a wizard with makeup and I have been practicing to one day apply my girlfriend’s since elementary school!"
    s "Welp, once again, I’ll leave you to it and-"

    scene otohasnewhair39
    with dissolve

    r "Nonsense! You’re coming too!"
    s "{i}Why?{/i}"

    scene otohasnewhair40
    with dissolve

    r "Because I don’t want this to be {i}your{/i} final memory of the weekend either. Let’s just all have some fun the way we normally do and put all of this drama behind us. Cool?"
    r "Barring Futaba, all my favorite people are here with me right now. And nothing would make it easier to put this all behind us than overpriced, caffeinated beverages I will receive at a discounted rate."
    o "I can’t have dairy..."

    scene otohasnewhair41
    with dissolve

    r "Soy milk exists. Now stop trying to make up excuses and go sit on the bed so I can make you look presentable. "

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I wind up walking around the room as Rin “fixes” Otoha to collect the shards of broken glass from things  that she and Nodoka have decided weren’t important enough to preserve."
    "I can’t help but contort my worldview until pieces of Rin are scooped into my hands alongside the shards. "
    "Is {i}she{/i} worth preserving in the eyes of someone who nearly shattered her just moments ago?"
    "Or will she eventually slip through Otoha’s fingers as part of another unfortunate “accident?”"
    "That remains to be seen."
    "And hopefully next time, I won’t be around for it."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ otohaspecial15p1 = True

    jump otohaspecial15p2

label otohaspecial15p2:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormweekend:
        scene dorm
        with dissolve
        play music "sweetvermouth.mp3" fadein 2.0

        "I decide to pay a visit to the dorms."
        "This might be a good time to hang out with one of the girls."
        "It doesn't look like anyone is hanging out in the halls today."
        "What should I do?"

        menu weekendmenu:
            "Knock on a door":
                jump doorknock
            "Second Floor" if day154 == True:
                if otoha_love >= 15 and nikilovesyou3 == True and day == 7 and otohaspecial15p2 == False:
                    jump otohaspecial15p1
...
```