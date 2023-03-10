# A Short List (Tsuneyo)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Tsuneyo love greater than or equal to 10

* Event [Between the Slurps of Pork Broth](./ramen5.md) (Tsuneyo) is completed)

* Event [Drug Use & Jump-Rope](./tsuneyodorm5.md) (Tsuneyo) is completed)



## Next events

* [Tsuneyo: The Man Who Loves Nothing](./tsuneyodorm10.md)

## Event properties

* Id: ramen10
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop
* Triggered by path: ramenshop->ramen10

## Official wiki page

[A Short List](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen10&go=Go) for more details.

## Event code

File: (install folder)\game\TsuneyoEvents.rpy

Code:
```python
...
label ramen10:
    scene tsuneyokaori1
    with dissolve
    play music "kashiwagi.mp3"

    "I walk into the ramen shop to be met with an...unusual sight. "
    "It’s by no means uncommon to see other people here at this time of night. In fact, Tojo Ramen is actually surprisingly popular given its size and location. "
    "But...I can’t really say I expected to see {i}Kaori{/i} of all people here. Let alone a particularly angry looking Kaori."
    "Isn’t she normally working around this time?"
    "Just how many places can she be at once?"

    k "Why will you not listen to my proposal?! Do your human ears not function?! Is the spider to blame?!"
    t "We are not hiring, but thank you for your interest in Tojo Ramen. "
    t "Please do not come here anymore."
    k "May I at least speak with the human who owns this noodle building?!"
    t "He is sick and bedridden. He can barely speak."
    k "He does not need to speak! He just needs to listen!"
    s "Is there a problem here?..."

    scene tsuneyokaori2
    with dissolve

    t "Oh. Hello again."
    t "Welcome to Tojo Ramen."
    t "Please take your time looking over the menu and let me know if you have any questions."

    if kaoridate1 == True:
        k "Friend?! What are you doing here?!"
    else:
        k "Hamburger Man?! What are you doing here?!"

    t "Do you two know each other?"
    s "We do. In fact, I feel like I run into her pretty much everywhere I go."
    t "Do you know how to make her go away?"

    scene tsuneyokaori3
    with dissolve

    k "I have not yet even swallowed a single dough string!"
    t "She keeps calling my precious noodles dough strings."
    t "I am tempted to slap a bitch."

    scene tsuneyokaori4
    with dissolve

    "I move several steps closer to the two of them and take a seat at the counter next to Kaori."

    s "I see you learned another new phrase."
    t "Be quiet or I will slap you as well."
    t "My fury can not be quelled."
    s "Well at least you aren’t hiding a knife behind your back this time."
    t "…"
    s "…"

    scene tsuneyokaori5
    with dissolve

    t "…"
    s "Tsuneyo, don’t even think about it. Remember the tag line."

    scene tsuneyokaori4
    with dissolve

    t "Tojo Ramen. All of the flavor, none of the violence."
    s "There you go. I knew you had it in you."
    t "All I have in me is rage."
    t "And-"
    s "And noodles. Yes, I know."

    scene tsuneyokaori6
    with dissolve

    k "Make her hire me! Please!"
    s "Why? You have like seven jobs already."
    k "That is not even enough jobs to cover every day of the week!"
    s "...Yes it is?"
    k "I require additional occupations!"

    scene tsuneyokaori4
    with dissolve

    s "Hey, Tsuneyo?"

    scene tsuneyokaori7
    with dissolve

    t "Ah-"
    s "Will you give Kaori a job?"
    t "…"

    scene tsuneyokaori4
    with dissolve

    t "No."

    scene tsuneyokaori6
    with dissolve

    s "I have exhausted every possible effort."
    s "It looks like you’ll just need to find another job elsewhere."

    scene tsuneyokaori8
    with dissolve

    k "I will not forget this betrayal."
    s "Just be quiet and eat your dough-strings."
    t "You bastard. You will pay."
    k "You are both fortunate that my stomach is lonely and has not absorbed hot pork liquid in a very long time."
    t "That's it. I’m calling the police. "
    s "No one is calling the police."

    scene tsuneyokaori4
    with dissolve

    s "Tsuneyo, why don’t you take a break for a little while and sit with the two of us?"
    t "I am working."
    s "Right. Which is exactly why I said “Take a break.”"
    t "But you haven’t ordered anything yet. I will not be able to provide adequate service if you decide to do so while I am on the break you suggested."
    s "That’s fine. I'm not really hungry anyway. I just came here to talk to you for a bit."

    scene tsuneyokaori9
    with dissolve

    if bonus == True:
        k "Do not fall for his trap! This man sells girls your age on the black market!"
    else:
        k "Do not fall for his trap! This man sells girl like you on the black market!"

    s "Kaori, stop going on about that human trafficking thing. I told you it wasn’t true."
    k "No! I am very mad at you!"

    scene tsuneyokaori10
    with dissolve

    t "After all we’ve been through...you want to sell me?"
    s "Of course I don’t want to sell you..."
    s "Do you really believe this suspicious character over me?"
    t "I don’t know what to believe. Everyone is calling my noodles dough strings and it is pushing my mind into turmoil."
    s "Then how about you just take a seat and eat some noodles? That always helps, doesn’t it?"

    scene tsuneyokaori11
    with dissolve

    t "Ahh...noodles."
    s "There you go. Doesn’t that calm you down?"
    t "It does."
    t "I am very easily swayed. "

    if bonus == True:
        s "I’ll try to forget that when my motives become slightly more inappropriate."
    else:
        s "You should focus on improving that part of yourself, as it could be rather problematic in the future and could allow employers to walk all over you."

    t "Noodles..."

    scene tsuneyokaori12
    with dissolve

    k "What is this sorcery? All you did was tell her to think of dough strings and it is as if she's journeyed to another world."
    s "It’s not sorcery. I’ve just learned how to talk to her."
    t "Noodles..."
    s "That’s right, Tsuneyo. Noodles."
    t "Maybe I {i}will{/i} take a break..."
    t "Just for a bit."

    "Tsuneyo begins to make herself a bowl of ramen and appears to completely forget Kaori's existence for the time being."

    scene tsuneyokaori13
    with dissolve

    k "Why will you not partake in the consumption of a bowl of pork warmth?"
    k "Is it because you only eat hamburgers?"
    s "No, Kaori. I’m just not hungry. "

    if kaoridate1 == True:
        scene tsuneyokaori14

        k "Well, you may share mine if you change your mind."
        k "I am no longer mad at you. And we are friends now, so it is okay."
        s "Thank you, Kaori. That’s...very sweet of you. I’m really okay, though."
        k "You should consume more carbohydrates so you can run longer distances."
        s "That’s...not a thing I want to do."
        k "Share my dough strings. I can not finish them all."

    else:
        k "Is it because you think the dough strings look like worms?"
        s "...No?"
        k "I also think they look like worms. But I will gladly consume them and become stronger."
        s "You do that."

    scene tsuneyokaori15
    with dissolve

    t "I have returned. "

    "Tsuneyo plops a bowl of ramen onto the counter that is so large that I can feel the wood slant down a few centimeters due to the sudden increase in weight."

    s "Can you really eat all of that?..."
    t "Any less than this would not quiet the rage burning within me."
    s "You’re certainly fierce when you’re angry."
    t "Fuck you."
    s "Tsuneyo, just because you know that isn’t a curse anymore doesn’t mean that it’s okay to say it to your friends."
    t "You're not my friend. You aren't anything to me."
    s "What happened to that “After all we’ve been through” stuff from a few minutes ago?"
    t "I meant through all of the transactions. There have been several now."

    if kaoridate1 == True:
        k "Friend."
    else:
        k "Hamburger Man."

    s "Yes, Kaori?"
    k "You seem quite capable of holding conversations with strange individuals. "
    s "I can’t tell if you’re talking about yourself or Tsuneyo."
    t "I’m a perfectly normal, noodle-loving girl."
    k "Do you see? Is she not strange?"
    k "Perhaps it is for the best that I am not allowed to work in this building."
    k "I like other foods too much anyway. Like bratwurst! Or soda!"
    s "Soda isn’t a food, Kaori."

    scene tsuneyokaori16
    with dissolve

    k "Do not tell me how to live my life when you love {i}nothing{/i}."
    t "Go on, Sensei. Tell her you love noodles."
    t "Make me proud."
    s "Noodles are good, don’t get me wrong, but I don’t think I’d put them at the top of my list."

    scene tsuneyokaori17
    with dissolve

    t "You will regret these words."
    s "Okay, why do you both look like you’re about to kill me? I don't like this."
    t "Is this what “leading someone on” means? I read about this in a book once."
    k "If these so-called “noodles” are not included in your favorite human items, what are?"
    k "Is there nothing you find sacred in this world?"

    scene tsuneyokaori18
    with dissolve

    k "List the things you love!"
    s "…"

    "The things I love, huh?"
    "Well, we’ve already crossed off noodles. So that leaves what?"
    "I don’t love my job."
    "I don’t love Kumon-mi. "
    "I care a lot for some, if not all, of the girls I’ve met here...but is it really fair to call something as trivial as that {i}love?{/i}"
    "Even with everything I’ve gone through, I still feel like some sort of outsider when I’m told to list the things that are important to me."
    "In fact, there are so few of them that there's really no point in making a list at all."

    s "To be honest...I don’t think I love anything."

    scene tsuneyokaori19
    with dissolve

    k "Nothing?..."
    t "That’s good. It means there is still room in your heart to accept the one true savior."
    s "If you tell me that savior is noodles, I’m going to walk out of this restaurant right now."
    t "Perhaps it is best if I keep my mouth shut."
    k "You did not name a single furry creature in your list of beloved items. "
    k "You aren’t human at all, are you?"
    s "Shouldn’t we be the ones asking {i}you{/i} that?"
    k "I’m the most human person here. Neither of you voiced how you feel about animals. Humans are supposed to like animals."
    s "Tsuneyo loves animals."
    t "Do I?"
    s "For the sake of this conversation, yes."
    t "I see."
    t "I, Tsuneyo Tojo, love animals. Let this fact be known."

    scene tsuneyokaori20
    with dissolve

    k "At least you are not completely lost to the darkness, Pork Woman. There is hope for you yet."
    t "Pork Woman? "

    if kaoridate1 == True:
        s "That’s going to be your new nickname from now on. I can’t even remember how long I was stuck with Hamburger Man for."

    else:
        s "That’s going to be your new nickname from now on. I can’t even remember how long I’ve been Hamburger Man now."

    scene tsuneyokaori21
    with dissolve

    t "I don’t know how to feel about this."
    s "I’ve found that it’s just best to let it happen. "
    t "You should have let me stab her when I had the chance."

    scene tsuneyokaori22
    with dissolve

    k "I take back all of the mean things I said to you. I require your protection. "
    k "I have consumed too many dough-strings to be able to properly engage in combat with a girl as shapely and athletic and beautiful as her."

    scene tsuneyokaori23
    with dissolve

    t "Thank you. I think you are beautiful as well."
    k "Apology accepted."

    scene tsuneyokaori22
    with dissolve

    s "Kaori, that’s not the proper response to “Thank you.”"

    scene tsuneyokaori24
    with dissolve

    k "Your instructions are too vague! I can not correct myself if all you say is that I am wrong and do not provide a correct answer!"
    s "Just say “You’re welcome.”"
    k "Welcome where?!"
    s "Nowhere. It’s just a phrase."
    k "Welcome is a greeting! You are trying to trick me, aren’t you?!"
    k "I will not fall for this! I will not be a pawn in your game!"
    k "I am Kaori Kadowaki! The Queen of Spiders! The Mistress of the Dark! "
    t "And I am Tsuneyo Tojo, the quirky and fun-loving Flavor Samurai."
    s "You two should join forces and create the strangest crime fighting duo of all time."
    t "As long as I’m home before the moon comes out."
    s "That should be doable. Kaori works like eighteen jobs but you guys can probably find a time that’s good for both of you."

    scene tsuneyokaori25
    with dissolve

    k "What do you think you’re doing? I will not agree to work with someone who would not agree to work with {i}me{/i} under different circumstances."
    k "I was born to serve customers, not justice."
    t "I was born to serve-"
    s "Noodles. We know, Tsuneyo."

    scene tsuneyokaori26
    with dissolve

    t "Ah-"
    t "I’ve become predictable."
    s "You’ve been predictable since our second meeting. "

    scene tsuneyokaori25
    with dissolve

    t "Whatever you say, bro."
    k "Many years, I have lived. 154 Dog years to be exact. But never in my life have I been so out of place in one restaurant."
    k "This side of town is pure evil."

    scene tsuneyokaori27
    with dissolve

    k "I can feel it...deep inside of me- my organs wrapping around themselves."
    k "I should have thanked them more than once."

    scene tsuneyokaori28
    with dissolve

    k "I must go!"
    s "Kaori-"
    k "Good day, humans!"

    scene tsuneyokaori29
    with dissolve

    "Kaori quickly disappears out of the ramen shop, slamming the door behind her."
    "I wonder where she-"

    t "The..."
    t "The ramen..."
    t "It is nearly untouched..."
    t "Who..."
    t "Who could do such a thing?..."
    s "…"
    t "…"

    scene tsuneyokaori30
    with dissolve

    s "..."
    t "...?"
    s "Ugh, okay. Fine. I’ll eat it. "
    s "I should have figured something like this was going to happen anyway."

    scene tsuneyokaori31
    with dissolve

    t "Good."
    t "It appears that I will be able to sleep tonight after all."

    scene black
    with dissolve2

    "I scarf down the ramen as quickly as I can and decide to head back before it gets too late."
    "The walk home is surprisingly quiet."
    "I get lost along the way."
    "I should pay closer attention when moving around in the dark."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen10 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen15:
...
```

## Code that triggers this event

File: (install folder)\game\TsuneyoEvents.rpy

Code:
```python
...
label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
    if tsuneyo_love >= 5 and ramen1 == True and ramen5 == False:
        jump ramen5
    if tsuneyo_love >= 10 and ramen5 == True and tsuneyodorm5 == True and ramen10 == False:
        jump ramen10
...
```