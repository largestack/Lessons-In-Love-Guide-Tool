# Flickering Spotlight (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kirin love greater than or equal to 15

* Event [Love, Dorms, and Other Things](./kirindorm10.md) (Kirin) is completed)



## Next events

* [Kirin: Enigmatology](./kirinsoccer20.md)

## Event properties

* Id: kirinsoccer15
* Group: Kirin
* Triggered by label: soccerfieldkirin
* Triggered by branch label: soccerfieldkirin
* Triggered by path: soccerfieldkirin->kirinsoccer15

## Official wiki page

[Flickering Spotlight](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinsoccer15&go=Go) for more details.

## Event code

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirinsoccer15:
    scene kirinsitups1
    with fade
    play music "highspeedprinter.mp3"

    "I head over to the gym to see how soccer practice is going."
    "Today, I am finally going to do my job as a coach and teach these girls the true meaning of sportsmanship."

    if bonus == True:
        "Just kidding."
        "I’m probably just going to stare at them and figure out why I have yet to open up a thigh massage stand in the corner of the room."
        "{i}That{/i} is the life I was destined to lead. Not this life of..."
        "Of..."

    s "Where even is everyone?"

    "I reach into my pocket for my phone to see if I’m here too late, but just as my fingers find their way into my pocket, a familiar voice cries out from the opposite side of the gym."

    mi "Sensei! Come quick! Kirin is dying!"
    s "That can’t be true when this background music is so upbeat. "
    ka "Background...music?..."

    if karinlied == False:
        scene kirinsitups2
        with dissolve
    else:
        scene kirinsitups3
        with dissolve

    "I make my way over to Miku and Karin to see what all this commotion about Kirin dying is."
    "But Kirin isn’t even here."
    "Oh no."
    "Was I too late?"

    s "Where will she be buried?"
    mi "Heck if I know. I say we just toss her into the nearest dumpster and set it out to sea."
    s "I can’t imagine it would get very far before sinking."
    mi "Then let’s just drop her out of an airplane and send her off with an even bigger splash."
    s "Miku, what is wrong with you?"
    mi "Pep talk! I’m tryin’ to whip her into shape."
    mi "If she thinks I’ll just get rid of her body when she dies, she’ll be more into...you know, not dying."
    s "I can’t wait to see this study posted in medical journals."
    ki "Can’t...go on!"

    "Another familiar voice wraps around my ankles and crawls its way up my body, slithering into my ears like some sort of miniature snake."
    "Basically, I hear Kirin."
    "That’s how a normal person would describe this."

    scene kirinsitups4
    with dissolve

    ki "Six-thousand-four...six-thousand...five!"
    mi "Woah! How’d she fit in an extra five-thousand-ninety in the time it took us to say hi to Sensei?!"
    mi "Kirin, stop! That’s enough!"
    ka "She’s just trying to make herself look cooler..."
    s "Congratulations on six-thousand sit-ups, Kirin. "
    s "Is this the same routine you used to get in shape for the beach?"

    scene kirinsitups5
    with dissolve

    ki "You mean when you...paid more attention to my sister than...you did to me?"
    s "I’m pretty sure all I did was compliment her."

    if bonus == True:
        s "If I remember correctly, I {i}definitely{/i} spent more time with you that weekend."
    else:
        s "I will compliment you as well if that is what you would like, Kirin."

    ki "Doesn’t matter if your...heart’s...not in it!"

    if bonus == True:
        s "Says the girl who willingly signed away any claim on my heart to her roommate."
        mi "Hm? What’s all this talk about hearts?"
    else:
        s "Says the girl who willingly signed away the right to ever enjoy a hug so her roommate could continue pursuing the elusive path of the huggy girl?"
        mi "Hm? What's all this about hugs?"

    mi "Kirin’s roommate's that creepy girl with the eyes that are all like “BA-BAM!” right?"

    if bonus == True:
        mi "You’re really gonna give your heart to somebody like that?"
    else:
        mi "You thinkin' about givin' your heart away to somebody like that, Sensei?"

    if karinlied == True:
        ka "Miku! Of course S...Sensei isn’t going to just...give his heart away..."
        ka "He’s going to wait for the right person to come along and...and..."
        ka "Ahhh, never mind! It’s too embarrassing to think about!"
    else:
        ka "…"
        mi "...Karin?"
        mi "Why are ya lookin’ all sad all of a sudden? You feelin’ okay?"
        ka "H...Huh?"
        ka "Oh. Yeah."
        ka "Yeah...I’m fine."
        s "…"

    scene kirinsitups6
    with dissolve

    ki "Hey...mind doing me a favor and...holding my legs still for a little while?"

    if bonus == True:
        s "I don’t think I have the willpower to do that in a safe-for-work way."
        ki "Then slide your head between 'em and let me squeeze it with my knees to stabilize myself."
        s "I have no idea how effective that will be, but it would be my pleasure."
        mi "Nobody is squeezing anybody’s head!"
    else:
        s "Sure thing, Kirin. That is a thing I can do because I do not look at you or any of the other girls as anything more than vessels waiting to be filled with knowledge."

        "I grab Kirin's ankles and she starts mimicking the theme song to the popular American sitcom, Seinfeld."

    mi "Kirin, if you’re not gonna take this seriously, I’m gonna have to figure out a way to {i}make{/i} you!"

    scene kirinsitups7
    with dissolve

    ki "I am...taking this seriously! Do you see how much I’m sweating?!"
    ki "It’s like...a fucking sauna in here! Isn’t a hundred enough?! That’s like...way above average!"
    mi "Karin and I both pumped out two-hundred without a problem at all."
    ki "You two are fucking mutants! I’m just a normal player! I’m not even that good!"
    mi "Sensei! Coach! Glasses!"
    s "Glasses is not one of my titles. "
    s "What do you want?"
    mi "We need ya to step in and motivate Kirin. "
    mi "Without your help, she’s gonna stay at the same level she is now for the rest of her life."
    mi "We’re reinventing her!"

    scene kirinsitups8
    with dissolve

    ki "I...ngh...don’t want to be reinvented..."
    ki "Just let me practice...how I want to practice..."
    ka "And how is that? By hanging out on your phone? Or spending the entire period talking to Sensei?"
    ka "We let you slack off every weekend. At least put some effort in today. "
    ka "We’re really trying to-"

    scene kirinsitups9
    with dissolve

    ki "SIX-THOUSAND-TWENTY!"
    ki "SIX-THOUSAND...TWENTY-ONE!"
    s "You’re still pretending you’re in the thousands? That’s just a waste of breath."
    ki "YOU’RE A...WASTE OF BREATH!"
    ki "SIX THOUSAND...TWENTY-TWO!"

    "I watch as Kirin repeatedly pulls her body up, struggling harder each and every time."
    "Miku and Karin pay close attention to her, calling her out whenever she doesn’t rise all the way."
    "It must feel horrible to be in her shoes right now."
    "Or, who knows? Maybe it feels good?"
    "She’s finally the center of attention for once- something even I understand she always wants to be."
    "But the attention isn’t exactly good this time."
    "The spotlight shining on her flickers."
    "It distracts her."
    "And, getting tired of the inconsistent light-"
    "She, too, burns out."

    scene black
    with dissolve

    ki "SIX THOUSAND...FORTY-NINE!"
    ki "I’m done! I can’t do any more!"
    mi "Ahhh no! That’s such a weird place to stop!"
    ka "Please do at least one more for all of our sakes."
    ki "No! That’s it! I’m done!"

    "Her arms go limp and her head falls down to rest in her hands."
    "She’s bright red and drenched in the efforts of her hard work."
    "I’m actually surprised that Miku and Karin were willing to push her this far when it’s clear that she’s at her breaking point."
    "But I guess it makes sense."
    "It’s not just routine. It’s punishment."
    "Like when a player makes a poor choice in a game and has to run extra laps at the next practice in order to make up for it."
    "Or other things that people who actually care about their jobs as team coaches force onto their players in the name of “improvement.”"
    "How much do you need to hurt someone in order to improve them?"

    ki "Hah...hah...hah..."
    ki "Sensei..."
    ki "Help me...up..."

    "Without looking toward Miku and Karin for approval (And also because I just feel bad for her in general) I reach down and grab Kirin’s hand, pulling her to her feet."
    "She winces in pain and clutches her stomach for a moment as she rises, but seems to be okay once she’s standing still."
    "………"
    "……"
    "…"

    scene kirinsitups10
    with dissolve

    ki "Hah...hah...hah..."
    ka "Do you think we might have...been a little too hard on her?"
    ka "She’s not looking so great right now..."
    mi "What are ya talkin’ about? She looks fine! Just a little red. But it’s a nice color for her!"
    ki "Kill...me..."
    ka "Kirin, maybe you should sit down for a second?"

    scene kirinsitups11
    with dissolve

    ki "I’m...fine! Just gotta...catch my breath!"
    s "Weren’t you just talking about how you wanted to call it quits like, a minute ago? "
    s "Maybe a break would-"

    scene kirinsitups12
    with dissolve

    ki "Oh, so now you’re on {i}their{/i} side as well? Figures."
    s "Why do there have to be sides? I just don’t want you pushing yourself too hard."

    scene kirinsitups13
    with dissolve

    ki "Yeah, well...it’s a little too late for that."
    ki "I feel like I fell in a lake."
    ki "But like, the lake was full of hot water that was also really sticky for some reason."
    ki "Probably pollution. "
    ki "Save the whales. Stop littering."

    scene kirinsitups14
    with dissolve

    mi "There are whales in lakes?!"
    mi "How do they fit?!"
    ka "Miku..."
    ka "I know your grades aren’t...the best. But please tell me that was a joke."

    scene kirinsitups15
    with dissolve

    mi "Sensei...How come you never teach us about whales? "
    s "Talk to Kirin. She’s the one who seems to care the most about them."

    scene kirinsitups16
    with dissolve

    mi "Kirin, how come you-"
    ki "I don’t give a shit about whales, Miku. I’m exhausted from doing six thousand sit-ups and am just talking out of my ass."
    ki "Is it cool if I go take a shower to cool down?"
    mi "Oh...uhh...well, we’re still in the middle of practice..."
    mi "But you {i}are{/i} kinda lookin’ a little worse for wear."
    mi "I guess it’s okay. But you’ve gotta come back as soon as you’re done for our practice game."
    ki "Yeah, yeah. Whatever."

    if bonus == True:
        ki "Can I take Sensei with me?"

        if karinlied == False:
            scene kirinsitups17
            with dissolve

            mi "Take him with you to...to the showers?! Why on earth would ya do that?!"
            ki "I’m not as flexible as you guys and can’t reach every part of my body."
            ki "I need his help getting all of the places I can’t get to myself."
        else:
            scene kirinsitups18
            with dissolve

            ka "Kirin! Again?"
            mi "Take him with you to...to the showers?! Why on earth would ya do that?!"
            ki "I’m not as flexible as you guys and can’t reach every part of my body."
            ki "I need his help getting all of the places I can’t get to myself."

        s "Well, if that’s what must be done-"

        scene kirinsitups19
        with dissolve

        mi "Keep it in your pants, Coach! I ain’t tryin’ to have a scandal on my soccer team until at least senior year!"
        mi "We’ve got stuff to focus on until then!"
        s "Hey, I’m just trying to look out for my players the only way I know how."
        mi "By bein’ a heckin’ perv and sneakin’ into the showers with ‘em?"
        s "Yes. Exactly that."
        s "So, now that we’ve all decided that this is okay-"
        mi "We have not decided that! I’m the captain and I say no!"
        ka "I..."
        ka "I also...say no..."
        ki "I say yes, which brings us to two against two."
        ki "The only possible solution is that we all just take a shower together."
        ki "Except for Karin. She can wait out here since she always takes too long."
    else:
        ki "Not sure if Karin was planning on coming or not, but I'd recommend that she stays out here."
        ki "She always uses too much water when she showers and it makes me worry about the future of the fish."

    scene kirinsitups20
    with dissolve

    ka "Wha- I do not! "
    ka "I take just as long as you do! "
    ki "Okay fine, but you also use twice the amount of shampoo."
    ka "I have twice the amount of hair!"
    mi "I..."

    if bonus == True:
        mi "Yeah, I don’t know if I want Sensei...seeing me...like that."

        scene kirinsitups21
        with dissolve

        ki "You {i}sure{/i} about that, Miku?"
        ki "Doesn’t it get your heart racing? Even just a little bit?"
        mi "Of course it does!"
        mi "I know firsthand how big his thing is because I sat on his lap during Halloween. And if I ever saw it up close I'd-"

        scene kirinsitups22
        with dissolve

        mi "Wait! I wasn’t supposed to say that!"
        mi "Makoto told me to never talk about it again!"
        ka "How...big...what is?"
        ka "His...bed?..."
        ki "Woah."
        mi "Kirin! Don’t tell Makoto I said that!"
        ka "Does he...maybe have a dog that’s...really big?"
        ka "But...why would Miku sit on a dog?"
        ka "Something isn’t...adding up..."

        scene kirinsitups23
        with dissolve

        ki "Did you like it?"
        mi "Wha-"
        mi "I mean...it was...fine!"
        mi "I try not to think about it!"
        ki "Because it gets you excited?"
        ki "My little Miku is growing up so quickly~"
    else:
        mi "Umm..."

    scene kirinsitups24
    with dissolve

    mi "Okay! Everybody into the showers except Sensei!"

    if bonus == True:
        mi "He should stay out here and think of Makoto’s naked body instead of ours!"
        mi "Bye, Sensei!"
        ki "Sorry~"
        ki "Can’t say I didn’t try."
        s "I feel like you had the chance to be a lot more persuasive than you actually were."
        ki "Or maybe {i}Miku{/i} was my target all along?"
        s "That’s-"
        mi "Bad! No!"
        mi "Everybody out! Practice is cancelled!"
        ka "A...chair?"
        ka "Those can get pretty big..."
        ka "That...yeah. That would make the most sense."
    else:
        s "That is fair. I will return home and shower in my own private shower, where no one can see me and I won't have to worry about accidentally bumping into any of you."

    scene black
    with dissolve2

    "In the end, the three of them disappear into the showers and I’m left out in the gym with all of the girls I don’t know the names of."
    "None of them really pay any mind to me, so I wind up deciding to get on with my day before Miku and the Kandas come back."
    "I think about apologizing to one of them through text for the disappearance, but-"
    "I’ve inadvertently stirred up enough trouble for the day and don’t want to make things any worse."
    "I’m sure they’ll understand."
    "I’m quite good at disappearing once things aren’t about me anymore."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirinsoccer15 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label kirinsoccer20:
...
```

## Code that triggers this event

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label soccerfieldkirin:
    if kirin_lust >= 5 and christmas7 == True and kirinlust5 == False:
        jump kirinlust5
    if kirin_love >= 15 and kirindorm10 == True and kirinsoccer15 == False:
        jump kirinsoccer15
...
```