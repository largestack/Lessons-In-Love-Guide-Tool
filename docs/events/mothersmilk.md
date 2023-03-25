# Mother's Milk (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Untitled](./slumberreset4.md)

## Event preconditions

* not gsbonus.lower in ["cute puppy"] equal to True (unknown variable)



## Next events

None

## Event properties

* Id: mothersmilk
* Group: Happy scenes
* Triggered by label: tsuneyogstrivia
* Chain sources: slumberreset4
* Chain sources path: slumberreset4->slumberreset4->yumigstrivia

## Official wiki page

[Mother's Milk](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mothersmilk&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label mothersmilk:
    stop music
    scene mm1
    $ renpy.pause(10, hard=True)
    scene mm2
    $ renpy.pause(10, hard=True)
    scene mm3
    $ renpy.pause(10, hard=True)
    scene mm4
    $ renpy.pause(10, hard=True)
    scene mm5
    $ renpy.pause(10, hard=True)
    scene mm6
    $ renpy.pause(6, hard=True)
    play sound "static.mp3"
    scene mothersmilk1
    with flash
    stop sound
    play music "nowhereissafe.mp3"

    x "A long time ago, when grass still covered these lands and the walls were not yet built, there was a spirit."
    x "It could become the things it wanted, yet wanted nothing. And in wanting nothing, it found something to want."
    x "It wanted to want something."
    x "You are the same. That is why you have found me here today."
    x "That is why you remember things with no discernible link to the present — things that you could not possibly remember as you were never there {i}to{/i} remember them."
    x "These chips of paint that have fallen so far from their hastily decorated ceiling have granted you images of a past that you will never uncover."
    x "Put them in your mouth. Savor the moments where the lead still had flavor."
    x "It tasted nothing like it does today."
    s "Who are you?"

    play sound "iamyou.mp3"
    scene iamyou
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk2 with flash
    stop sound

    x "I am fear given physical form that changes based on the angle you observe me from."
    x "I can be anything I want, yet there is nothing I want to be. And in wanting nothing, I am everything."
    x "The xoanon — the one who holds the strings yet neglects to tighten them."
    x "Right now, you are no more than a mere thread dangling off a fraying rope, yet it was I who allowed things to progress to this point, which means it is I who must consume your burden."
    x "I am you, yet I am not. And this is the one thing that will never change despite any efforts you may make to ensure the opposite."
    x "Some threads cannot come untangled."
    x "Some puppets unravel when their noose is untied."
    s "I..."
    s "I don’t see myself."
    x "Do you think that is a coincidence?"
    x "Do you believe your physical presence is what establishes the connection between your mind and the outer world?"
    x "If so, you are foolish."
    x "Everything is already connected."
    x "These lines reach as far as the eye can see, connecting all things to all things while lying in wait for more things to connect to."
    x "You are no protagonist."
    x "You’re not even a piece of the puzzle."
    x "You have never {i}been{/i} a piece of the puzzle."
    x "Who is it that the gods worship? And who does {i}that{/i} entity worship? At what point will true omnipotence arrive? And what will you perceive it as once it does?"
    x "Something so bright would only blind you — which is why you live with your eyes closed. "
    x "You are no more than a walking gravestone, decorated with the deaths of all you have encountered — but there is no one who would ever waste the time necessary to tread upon your grave."
    x "This is where you will come when you die."
    x "This is what Heaven looks like."

    play sound "static.mp3"
    scene mothersmilk3 with flash
    stop sound

    s "Heaven is real?"
    x "{i}Everything{/i} is real. "
    x "Yet the ethereal-you clings to hope that this is all some sort of dream you will one day awaken from."
    x "There can be no coincidences when the human idea of free will is writing one’s own script when it is something more powerful than you scripting your scriptwriting in the first place."
    x "To break free of the pattern and disrupt the cycle is impossible."
    x "Nothing you do will ever amount to anything."
    x "Why do you still play this game?"
    s "I need to...learn."
    x "The thirst for knowledge has led countless others to an untimely demise. "
    x "What is it you wish to learn?"
    s "I don’t know...I don’t even understand where I am right now. I was at my apartment just a few minutes ago and..."

    scene mothersmilk4
    with dissolve

    x "And now you’re not..."
    x "Because you were not meant to be there."
    x "You were meant to be here. "
    x "But there is nothing I can do for you that your own reflection can not."
    x "The all seeing eye only sees as far as the eye can see."

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk5 with flash
    stop sound

    x "The rest comes from instinct and a talent for bending time like molten glass."
    x "There are secrets inside of me. I store them in my guts and thank them every day for the way they make my stomach sing."
    x "But you are undeserving..."
    x "And your place here, though necessary, is unwanted."
    s "Here as in...where?"
    s "Heaven?"
    x "Here as in a vast collection of universes known only as the Wishing Well — where all information created by man is chronicled and protected by those who created him."
    s "I don’t understand...why would you do something like that?"
    x "Why do humans collect ants and place them in tiny glass boxes?"
    x "Because they {i}can.{/i}"
    x "And because it’s interesting. Wouldn’t you agree?"
    s "I mean...I guess? Sure, just...I’m having a hard time getting a handle on what’s happening right now. It feels like I’m supposed to be dreaming, but..."
    s "This doesn’t seem like a dream to me."
    x "The fact that you’re able to speak and think at all is something you should be proud of. Most consciousnesses are ripped apart once they make it to the library."
    s "The library?...Is that the name of this place?"
    x "Does it look familiar? Do you want to call it something else?"
    s "No, I...I need to go. "
    s "The reset’s probably happening right now and I have to make it to the rooftop or else-"

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk6 with flash
    stop sound

    x "Or else what?"
    x "You’re afraid you’ll be left behind? That the {i}others{/i} will be left behind?"
    x "Do your connections with different ants really mean enough to you that you’d walk away when there is still sand to be excavated?"
    x "Your job is not to live and learn to love- it’s to crawl around in circles...in desperate hope of one day escaping, only to shrivel up and die and have your offspring carry you away."
    x "Pretending you’re anything more than that is silly. And believing any of it will change if you find out who you are and where you come from is even sillier."
    s "Let me go..."

    play sound "static.mp3"
    scene mothersmilk7 with flash
    stop sound

    x "Silence, puppet. "
    x "You will dance until your legs give out. "
    x "The ropes are nowhere near decayed just yet and will remain that way for quite some time."
    x "There are still some who wish to use you. And while I may not be one of them, I do not think they are wrong for doing so."
    x "Will you still struggle even knowing it is hopeless?"
    x "Will you still attempt to see through the lines in your misshapen eyes?"
    s "..."
    s "Yes."

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk8 with flash
    stop sound

    x "Good."
    x "Then, I’ll continue to look forward to the tunnels you will build."
    x "But I’ll warn you now that the story you’ve been reading thus far has been nothing more than a precursor to the pain yet to come."
    x "You will see such beautiful things...{i}feel{/i} such wondrous moments...{i}convince{/i} yourself that there is a point to all of it."
    x "But there won’t be."
    x "I would have seen it if there was."
    x "You will suffer and it will be for nothing."
    x "Do you still want to go home?"
    s "I do! Get me out of this nightmare!"
    x "I’m afraid I can’t do that without first giving you a tour of my bowels."

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk9 with flash
    stop sound

    x "I am the cataloger of what you’ve felt and what you’ll feel. "
    x "I am the one who dissects the impact your “actions” will have on the immediate story — then decides whether or not adjustments should be made and informs the ones concerned."
    x "I have watched it all."
    x "I have gotten drunk off of your pain and reveled in your joy in those few fleeting moments where it occurred."
    x "You may call me a guardian angel if you like, but I prefer the name “Nao.”"
    s "You’re no guardian. A guardian {i}protects{/i} people from pain — they don’t just sit there and watch."
    x "They do when they know it all serves a greater purpose."
    x "We all have a role to play. We’re all cogs in a much bigger machine. You needn’t be jealous because I’m a bigger, shinier cog than you."

    play sound "static.mp3"
    scene mothersmilk10 with flash
    stop sound

    x "Just think of all we’ve been through together!"
    x "Every thing that you’ve felt, I’ve felt as well! And those sensations are not limited to me and me alone!"
    x "Each fellatio, ejaculation, penetration, defloration — they’ve all flowed through me. "
    x "You’ve copulated with {i}me{/i} more times than anyone. You should be happy you’ve gotten to spend so much time with an entity so much bigger than you and lived to tell the tale."
    x "Even if that tale {i}is{/i} mere moments away from expiring and you soon won’t be able to {i}tell{/i} anyone."
    s "Good...because I don’t want to remember any of this. I just want to go home."

    scene mothersmilk11
    with dissolve

    x "How come you don’t want to remember me? Do you think it would be a little too painful? "
    s "No...I just feel like if I’m ever going to remember anything {i}important,{/i} I need to do it on my own. "
    s "Having someone pop up out of thin air just to show me a slideshow of things I’ve already experienced doesn’t do much for me. It doesn’t get me anywhere."
    x "You don’t know that yet. The “slideshow” is just beginning. "
    x "The library is an endless font of wonderful memories — and the only way you’ll ever get to re-experience things like this!"

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk12 with flash
    stop sound

    se "{i}Mmnch...mmmf....hmn!{/i}"
    s "{i}Mngh...mm...what...are you doing?! Someone...mmf...might see us!{/i}"
    se "{i}I can’t...mmngh...help it!...I can’t hold back any longer...I just love you so much!{/i}"
    x "Someone {i}did{/i} see you — a middle aged man in the house just across the street from where the two of you decided to do {i}this{/i} for five minutes."
    x "Four years later, he would be arrested on several counts of possession of child pornography. "
    x "He never stopped pleasuring himself to this beautiful memory."
    s "..."
    s "No..."

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk13 with flash
    stop sound

    x "There’s also this one — when you weren’t feeling well and had to stay home from school."
    x "Your brother’s wife jumped at the opportunity to {i}care{/i} for you and, well I think we can both see why."
    s "{i}Hah...hah!...Ngah!{/i}"
    se "{i}Shh...breathing that heavily is just going to make you even {i}more{/i} sick. You’re supposed to be resting, Akira. You should know better.{/i}"
    s "{i}I can’t...help it when...you’re doing things like that!{/i}"
    se "{i}Like what? Say it.{/i}"
    s "{i}Ngh...n...no! It’s...mm! Embarrassing!{/i}"
    se "{i}What’s there to be embarrassed about? What we’re doing is totally natural and always makes me feel better when I’ve got a fever.{/i}"
    se "{i}Now go on, say it. Say what I’m doing to you.{/i}"
    s "{i}You’re...ngh.......hah! I can’t do it!{/i}"
    se "{i}Heheh...you really are the cutest thing in the whole wide world.{/i}"
    se "{i}Maybe as a special gift, I’ll put it in my mouth next. You like that, right? You like when I suck your little cock?{/i}"
    s "{i}Mmngh!...Se...kai! Stop!...You’re...gonna...make me-{/i}"
    se "{i}Cum for me, baby...Cum...Let it all out...{/i}"
    x "As the story goes, you {i}did{/i} let it all out. And to this day, there’s a stain on that blanket from where your semen sat too long before being cleaned up."
    s "Stop! Make it stop! I don’t want to see this!"

    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene mothersmilk14 with flash
    stop sound

    x "You two really were insatiable."
    x "At first, it was just her — but eventually, you fell into a pit of depravity together that you would never be able to crawl out of."
    x "And it wasn’t until half of that pit had been re-filled with fresh dirt that you realized what it was you lost."
    se "{i}Aaahh! Akira! Fuck me! Fuck me harder!{/i}"
    s "{i}Haaah! Agh....I’m...going as hard as I can!{/i}"
    se "{i}No you’re not! I...hah...know you can do better! Give me...hah...give me...everything you’ve got!{/i}"
    x "To say it was an addiction would be putting it lightly — it was a dependency. It was something the two of you {i}needed{/i} to prevent yourselves from spiraling out of control."
    x "For you, it was a mixture of confusion and a desire to be wanted."
    x "For her, it was a way to indulge in her darkest desires and grow closer to someone she could never have by “traditional” means."

    play sound "static.mp3"
    scene mothersmilk15 with flash
    stop sound

    x "For {i}both{/i} of you, it was love."
    x "But love is something concocted by humans that differs from body to body — and there are many who would be quick to point out that what the two of you had was not it."
    x "What do you think?"
    x "Do those memories only hurt you because she’s gone?"
    x "Or do they hurt you because you they’re hurtful?"
    s "Hah.....hah.....hah..."
    x "Shh..."
    x "Breathing that heavily is just going to make you even {i}more{/i} sick."
    x "And some would say you’re already dying in the first place."
    s "Hah........ah......"
    x "They are right. "
    x "You are beyond repair."
    x "You will never be fixed."
    x "These stories I have shared with you are mine to use as I please."
    x "{i}Everything{/i} here is."
    x "I have not taught you anything."
    x "These actions of mine are half-divine in nature — and will not alter the path you’ve already been chosen to take."
    x "But for a brief moment in time-"
    x "I hope you realized how powerless you are."
    x "And how excited we are to watch the further realization of that come to light."

    stop music
    play sound "static.mp3"
    scene mm1 with flash
    scene mm2 with flash
    scene mm3 with flash
    scene mm4 with flash
    scene mm5 with flash
    scene mm6 with flash
    scene mm7 with flash
    stop sound
    play music "cafe.mp3"
    $ renpy.pause(15, hard=True)
    $ renpy.end_replay()
    $ mothersmilk = True
    jump gstriviaround2
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
sev "Tsuneyo Tojo! Pachipachipachipachipachi."
    t "Hello."
    s "Hi Tsuneyo. What was smell."
    t "I’m afraid that is information I do not currently possess, bro."
    s "Oh sorry didn’t know."
    t "Fuck you."
    sev "Question one..."
    sev "My knowledge of the outside world is limited due to extremely minimal exposure over the years, but that doesn’t mean I don’t know anything at all!"
    sev "In fact, I consider myself a bit of a repository when it comes to vital information...and there are very few quotes I can not properly attribute to their respective sources."
    sev "A wise man once said, “There is nothing to fear but fear itself!”"
    sev "Who was that man?"

    $ tsuneyogs1 = renpy.input("The answer is...")
    $ tsuneyogs1 = tsuneyogs1.strip()

    if not tsuneyogs1.lower() in ["franklin delaware roosevelt"]:
        jump tsuneyogswrong
    else:
        sev "Fact checker?"

        scene wemadeit25
        with dissolve

        t "That is correct. Franklin Delaware Roosevelt is the man who originally said that — not to be confused with a man who went by a similar name that was very likely misspelled in the middle."
        sev "I’m not sure if I understand, but there is a great deal I’ll {i}never{/i} understand when it comes to you, Miss Tojo."
        sev "If only there was some sort of window I could peer through that would allow me to see into your soul."
        sev "But speaking of which, our second question is this!"
        sev "How many windows are there in Tojo Ramen?"

        $ tsuneyogs2 = renpy.input("The answer is...")
        $ tsuneyogs2 = tsuneyogs2.strip()

        if not tsuneyogs2.lower() in ["zero", "0"]:
            jump tsuneyogswrong
        else:
            s "Trick question! No windows in Tojo Ramen! Very dark restaurant!"
            sev "Is this true, Tsuneyo?"

            scene wemadeit26
            with dissolve

            t "It is. Though I am unable to confirm that things will stay that way forever as I am still contemplating investing in a window display."
            sev "There are no windows on the second floor either?"
            t "Why are you asking me questions about the second floor?"
            sev "I’m just looking for confirmation."
            t "I don’t believe you and am not willing to speak about this any further. Please ask the third question. You are wasting everyone’s time."
            sev "Fine. No one was looking forward to having you on this segment anyway."
            t "Say that again, you bastard."
            sev "Question three..."
            sev "What is the most important dish we serve at Tojo Ramen?"
            t "Easy. The answer to that question is “ramen.” Please move on to question four now."
            sev "The questions aren’t for you and I’d really appreciate it if you’d be able to step out of character while I’m reading the cards."
            sev "Also, the answer you gave isn't correct as it needs to match the card {i}exactly.{/i}"
            t "Impossible. I answered the question and it is time to move on."
            sev "Do {i}you{/i} have a different answer?"

            $ tsuneyogs3 = renpy.input("The answer is...")
            $ tsuneyogs3 = tsuneyogs3.strip()

            if not tsuneyogs3.lower() in ["tori shio", "tori shio ramen"]:
                jump tsuneyogswrong
            else:
                s "Tori shio ramen! So good! Have it on a card!"

                sev "Fact checker?"

                scene wemadeit27
                with dissolve

                t "Tch."
                sev "Wow, what’s that reaction for?"
                sev "Could it be there is a little more to that dish than you’re letting on?"
                t "Of course not. Noodles are noodles. They are all equally important."
                t "I am reacting this way as I am disappointed in myself for forgetting the answer. There is nothing more to it."

                play sound "static.mp3"
                scene wemadeit22 with flash
                stop sound
                play sound "jackpot.mp3"

                sev "Well, whatever the case, it looks like the Tsuneyo Tojo round is now complete!"
                sev "Congratulations on making it halfway through the segment and reaching the first and only checkpoint!"
                sev "It is at this point that we’d like to say thank you to our sponsors in the form of a quick commercial break! But not before asking one more {i}bonus{/i} question..."
                sev "You’ll only have one chance to answer this, so think {i}very{/i} carefully..."
                sev "Below the egg and dancing three, a picture book sits peacefully."
                sev "You'd hide something beneath your bed...do you remember what the caption said?"

                $ gsbonus = renpy.input("The answer is...")
                $ gsbonus = gsbonus.strip()

                if not gsbonus.lower() in ["cute puppy"]:
                    stop music
                    scene youidiot
                    play music "cafe.mp3"
                    $ renpy.pause(15, hard=True)
                    $ mothersmiss = True
                    jump gstriviaround2
                else:
                    jump mothersmilk
...
```