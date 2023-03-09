# First Last Date
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar13&go=Go)


Part of event chain [Us](./dormwar12.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwar13
* Group: Main
* Triggered by label: dormwar12

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label dormwar13:
    scene toukadate1
    with dissolve2
    play music "love.mp3"

    mak "Makoto Miyamura here, coming to you live from Viale dei Giapponesi, one of the most prestigious and {i}extremely{/i} expensive restaurants in all of Kumon-mi."
    tb "What’s this? A pretend television show? How adorable."
    tk "Hello, world! Bow down before Tsukasa Tsukioka, future emperor of Japan!"

    scene toukadate2
    with dissolve

    mak "Tsubasa, thank you very much for joining me today."
    tb "Thank you for inviting me. It will be my daughter’s first ever date, and I need to be sure that my husband does not find out about it."
    mak "Does your husband not approve of your daughter “dating?”"
    tb "Oh, heavens no. He wants Touka to follow in the family’s footsteps and have an arranged marriage like we did."
    mak "And you {i}don’t{/i} support this?"
    tb "I just want my daughter to be happy and have the freedom she deserves. "
    tb "Which is also why we’ve rented out the entirety of the restaurant today."
    tk "Mother, can I go fire a chef?"

    scene toukadate3
    with dissolve

    tb "Not right now, dear."
    tk "Pleeeeeeeeeease?"
    tb "Tsukasa..."
    tk "Later?"
    tb "We’ll see."

    scene toukadate2
    with dissolve

    mak "So, Tsubasa, since you’ve rented out the entire restaurant, is it safe to assume that money will be the driving force behind what makes this date a success in your eyes?"
    tb "I’m sure it will play some role. But the true secret weapon is what’s on the inside."
    mak "Meaning you think Touka’s attitude and feelings toward Sensei will be what gets her the win today?"
    tb "Meaning she is wearing a dress that accentuates her natural beauty and that the atmosphere of the restaurant is unlike anything else I’ve ever seen."
    tb "But yes, she is also a lovely girl at heart as well."
    tb "I just hope that your teacher already being in a committed relationship does not cause the competition to be too one-sided."

    scene toukadate4
    with dissolve

    mak "Wait, what?"
    tk "Mother, when Touka gets married, can I have her second bedroom?"
    tb "Ask your father, Tsukasa."

    scene black
    with dissolve

    "I take a bus to the urban district after leaving Chika’s house to meet up with Touka."
    "I’ve already told Chika that she’s won the competition, so I imagine this “date” will be rather short."
    "Not that I imagine Touka would agree to going on a date with me at this point anyway, so she was probably just tossed into this contest against her will."
    "But hey, I’m totally fine with that as it means I’ll probably be able to eat a lot of expensive food or-"

    to "Finally!"

    scene toukadate5
    with dissolve

    to "Do you have any idea how long you’ve made me wait here?"
    to "I was beginning to think you weren’t going to show up at all."

    "…"
    "What was I saying about Chika again?"

    s "You look...very nice, Touka."
    to "And you look like you were never informed of this restaurant’s dress code."
    s "To be honest, it wouldn’t have changed much even if I was. I only own two outfits."

    scene toukadate6
    with dissolve

    to "Two?! Isn’t that remarkably low for even...lower middle class standards?"
    s "I’ve just never really needed any other clothes, I guess."

    scene toukadate7
    with dissolve

    to "I see."
    to "May I ask how your date with Chika went?"
    to "She seemed rather excited to have the...opportunity today."
    s "And you’re not?"
    to "Well...it’s not as if I {i}hate{/i} this."
    to "This is my favorite restaurant, after all."
    to "And...I’ve never been on a date before, so that much is exciting. "
    to "I just expected to feel a little more...nervous, I suppose."

    if bonus == True:
        s "Isn’t it good that you’re {i}not{/i} nervous? That just means you’re comfortable around me."
    else:
        s "You likely don't feel that way because I am a pure man with pure intentions who, after all of the teasing is said and done, really just wants to help you learn."

    scene toukadate8
    with dissolve

    to "I can assure you that is absolutely not the case. You make me feel less comfortable than anyone I have ever met before."
    to "It’s just that...this entire ordeal feels so...staged, don’t you think?"
    s "Well...it {i}is{/i} staged, isn’t it?"
    to "It is, yes. I didn’t even get to pick out my own clothes for the event."

    if bonus == True:
        s "Well tell whoever did that I am very thankful."
        to "Please keep in mind that I am still your {i}student{/i} at the end of the day...And that if anything were to happen between us, it would make the headlines of several newspapers."
        to "I am not trying to have both of our reputations ruined in one fell swoop."
        s "I don’t know. I feel like it might be kind of worth it..."
    else:
        s "Well tell whoever did that their taste is a bit outdated and that your dress is like three seasons too old."

    scene toukadate9
    with dissolve

    to "Can we just sit down? The two of us still standing here after introducing ourselves is likely making this date seem unsuccessful to our spectators."
    s "Spectators?"
    tb "Good luck, dear!"

    if bonus == True:
        tk "Ask him to teach you that game he played with the peasant girl! I still want to know!"
    else:
        tk "I'M GONNA RULE THE WORLD ONE DAY!!!!!!"

    tb "Tsukasa, please sit down. "
    to "I asked them not to come, but..."
    to "Well, you see how that ended up."
    s "I...certainly do."

    scene toukadate10
    with fade

    if bonus == True:
        "Touka and I sit down at the table and I quickly receive a reality check in that some [teenager]s grow up {i}way{/i} before others. "
        "I am going to have a very difficult time not staring at her tonight and I really wish her family was not here to observe that."
    else:
        "Touka and I sit down at the table and I have to fight off the urge to ask her if they sell chicken fingies here."

    to "This...dorm war..."
    s "What about it?"
    to "It’s...fun."
    to "Does your class do things like this often?"
    s "We’ve gone on trips to the beach and...had parties before. But there’s never been anything like this."
    s "Are you actually starting to get along with people now?"

    scene toukadate11
    with dissolve

    to "Slowly, but...I think so. "
    to "And I was a bit hesitant to accept {i}this{/i} particular challenge for that exact reason."
    s "Yeah, I was thinking you may have been forced into this somehow."
    to "I wasn’t {i}forced{/i}. You’re incorrigible, but I don’t despise you. "
    to "I just would have preferred something a bit more...girl-oriented so as to not paint yet another target on my back."
    to "Something like...the Nagasawa girl’s test of knowledge. Or the tomboyish girl...umm...Miku, I think? Her contest."
    s "You think you’d fare well in an athletics test?"
    to "You think I wouldn’t?"

    if bonus == True:
        s "I think there are two large obstacles that would prevent you from moving the same way someone like Miku does."
        to "Obstacles? There are very few obstacles for the Tsukioka family and-"
        to "Oh. I get it."
    else:
        s "I am on the fence. I feel as if your shoulders lack the typical aerodynamicism of many other women in your age group."
        to "You believe that to be an important element in determining one's success in athletics?"
        s "..."
        to "Why have you stopped responding."
        s "..."
        to "You're thinking about chicken fingers again, aren't you?"

    s "I’m glad I didn’t have to say anything."

    scene toukadate12
    with dissolve

    if bonus == True:
        to "I’m also quite glad you didn’t say anything. I am well aware of the hindrances my body may cause on occasion. "
    else:
        to "You and those darned fingies."
        to "How I've come to know you so well, so quickly...I will never understand."

    scene toukadate13
    with dissolve

    to "Like...right now, for example. You’re already starting to zone out, aren’t you?"
    s "..."
    s "Hm? What was that?"
    to "You are becoming more and more predictable with each passing day, Sensei."
    s "Before you know it, you’ll be opening your door before I even knock."
    to "I can’t imagine a day like that coming any time soon. "
    s "Yeah. Probably not until after our third date, I’d imagine."

    scene toukadate14
    with dissolve

    to "Hehe~ I was thinking more the...tenth or eleventh."
    s "Looks like we’ll be going on a lot of dates from now on, huh?"

    scene toukadate15
    with dissolve

    to "I can’t say I blame you for wanting to get closer to me, but I would like to remind you that this is not a real date and that I never would have agreed to go if it was."
    s "Never?"
    to "Probably never."
    s "That’s fine. I’ll just schedule a few more fake ones with your mom and see what else she’s willing to make you wear."

    scene toukadate16
    with dissolve

    to "Please don’t do that. I actually detest being fitted for new clothes, and she would never approve of me wearing the same thing to multiple outings."
    to "Besides, occasions like this are meant to be shared between either lovers or those with the potential to find love in one another."
    to "There is no reason for the two of us to do things like this together when the likelihood of us remaining in contact after I graduate is slim to none."
    s "Good thing you won’t be graduating any time soon."

    scene toukadate17
    with dissolve

    to "No...I suppose I won’t be. There are still several years left of [high_school]."

    "There are a lot more than just “several,” Touka..."

    to "It’s important to always look toward the future, though. Especially for someone like me, whose path is already laid out."
    to "So it would probably be best if we called this date our last."
    to "We can chat and make merry for the rest of the night, but once this is over, I’d like to go back to focusing on my studies."
    to "That {i}is{/i} why I came here after all. "
    s "Why you came and why you continue to come are two different things, though."
    s "You still show up to class every day and I haven’t done much to advance your studies yet, have I?"

    scene toukadate18
    with dissolve

    to "That is no fault of my own."
    s "But you still come."
    to "Because it is my duty to-"
    s "You come see me every morning. You even say hello to me as soon as you walk in."

    scene toukadate19
    with dissolve

    to "Because it would be impolite if I were to just walk by you without-"
    s "{i}I{/i} think you keep coming to class because you’re starting to like me."

    scene toukadate20
    with dissolve

    to "You-"
    to "Take that back! I am not!"
    to "You are...adequate as a teacher! But I still have yet to feel the full effect of your methods on my testing and-"
    s "You don’t...{i}love{/i} me, do you?"

    scene toukadate21
    with dissolve

    to "Mother! Some assistance, please?!"
    tb "You’re doing wonderfully, dear! He’ll be eating foie gras out of your palm within the hour."
    to "That is disgusting! Please come to the table and teach him how he should be-"
    s "Touka, hold on a second."

    scene toukadate22
    with dissolve

    to "...What?"
    to "You used my real name, so...it must be at least mildly important."
    s "First of all, I’m just messing with you. I know you don’t {i}love{/i} me."
    to "And?..."
    s "And...that’s why I already told Chika that this victory goes to her."
    to "…"
    s "…"

    scene toukadate23
    with dissolve

    to "Hah...you could have at least waited until we were finished with dinner to inform me of that."
    s "It’s just that-"
    to "Yes, yes. A fancy meal and a nice dress means nothing without actual romantic chemistry. "
    to "I am not {i}entirely{/i} naive, Sensei. I expected Chika to win from the moment this outing was decided."
    s "…"
    to "…"

    scene toukadate24
    with dissolve

    to "And yet...I came."
    to "Just like I do with class."

    scene toukadate25
    with dissolve

    to "You irritate me to no end."
    to "And yes, I may have tried to get you fired on several occasions now for completely disregarding your responsibilities-"
    to "But still, I show up every morning and greet you."
    to "It is not because I like you, though. "
    s "What is it then?"
    s "Is it actually-"
    to "If you say “love” I will snap my fingers and have my assassins jump right out from behind the bar."
    s "I knew I heard something back there..."
    to "The reason I continue to show up is that I need your help."

    if bonus == True:
        to "It wasn’t until I joined your class that I knew what it was like to be among other girls my age."
        to "And it wasn’t until I joined your class that I knew how it felt to look at myself in the mirror before going out to eat with a boy."
        to "I’ve had many firsts in such a short period of time, and it is all thanks to you."
        to "Well...maybe not {i}all{/i} thanks to you. But you have played somewhat of an important role in the matter."

        scene toukadate26
        with dissolve

        to "So I accept my defeat at the hands of Chika Chosokabe..."
        to "But I do ask that you continue to annoy me for a little while longer. "
        s "…"
        to "…"
        tb "Oh dear. I think I’m tearing up."
        tb "Tsukasa, darling. Could you fetch me a box of tissues from the kitchen?"
        tk "Yes, Mother. But there will be one less chef after I return. "
        tb "That’s fine...just...{i}*sniff*{/i}...hurry up."

    scene black
    with dissolve2

    if bonus == True:
        "The waitress arrives the moment we stop talking and takes our orders."
        "I try to order something myself but am unable to pronounce it properly, so Touka takes charge and says a bunch of stuff in what I’m pretty sure is Italian on my behalf."
        "We don’t talk much at all for the rest of the date, but it’s somehow not bad."
        "It doesn’t really feel like...anything, though."
        "Just another meeting at a table with a girl who is far too good for me."
    else:
        "Touka gently slides a briefcase across the table."

        s "..."
        to "Open the briefcase, Sensei."
        s "I'm scared. The last time someone slid a briefcase across the table to me, I opened it up and Jerry Seinfeld was smiling at me."
        to "I can guarantee you that will not be happening again today."

        "I nervously open the briefcase as Touka stares on, stonfaced."

        s "Ah!"
        to "What do you think?"
        s "There must be...twenty whole dollars in here..."
        to "And all you need to do in order to keep them..."
        to "{i}Is hug my mother...{/i}"
        s "Tsubasa?..."
        to "That's right."
        s "But...why?"
        to "She has never hugged a real man before. Just my father, who is a cyborg."
        s "...And if I refuse."

        "Touka reaches for the briefcase and I have to lunge forward and stop her."

        s "No! Wait!"
        to "Do you agree after all?"
        s "..."
        to "Do you have any idea how much gum you could buy with all of this money, Sensei?"
        s "Almost ten whole packs..."
        to "Tell me how much that is in sticks."
        s "So many sticks..."
        to "Roughly 150 sticks."
        s "SO MANY STICKS!"

        "Touka smiles at me and walks away from the table."

        to "I trust that you will do the right thing..."
        s "..."
        tb "{i}What did he say, Touka? Is he going to hug me?{/i}"
        to "Yes, mother. You will be hugged."
        to "Just...when you least expect it..."

    $ renpy.end_replay()
    $ dormwar13 = True
    stop music fadeout 5.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"
    "{i}Meanwhile...{/i}"

    jump dormwar14

label dormwar14:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
else:
        s "I'm the huggy boy."

    scene datewar19
    with dissolve

    c "H-Hey..."
    c "Wh-what’s this all of a sudden?"
    c "It’s...embarrassing when you just come out and say it out of nowhere like that."
    s "It’s what you were about to do, isn’t it?"
    c "Well..."

    if bonus == True:
        c "Maybe..."
    else:
        c "I was going to say I'm the huggy girl, but..."

    "Perhaps in another life, the three words she loves more than the world itself would not carry so much weight."
    "Perhaps in another life, I would be able to say them and mean them."
    "Or perhaps I wouldn’t."
    "It’s not really something that someone like me could ever know."
    "There’s no way to know anything in this world. Not when it continues to spin as quickly and change as rapidly as it does every single day."
    "But, for a brief moment in time, the spinning stops."
    "The changing stops."
    "And, in a time where I least expect it-"
    "Chika and I exist. "
    "Not just as people. Not just as a couple."
    "But as us."
    "I am me. She is her."
    "We are us."
    "That is all."

    s "…"
    c "…"

    "O, world."
    "Why must I destroy everything I touch?"

    s "You’re going to win this competition."

    scene datewar20
    with dissolve

    c "I mean...{i}obviously.{/i}"
    c "But we’ve barely even started, and to say that before Touka even goes..."
    c "Why now?"
    s "Because you deserve it."
    s "And I don’t deserve you."

    "It’s funny how the moments we least expect are the ones that always change us."
    "Which is not to say that I’ve changed."
    "I will hurt this girl more times than she can bear."
    "I will ruin everything."
    "I will destroy her world."
    "But I will not have wanted any of it."
    "I do not change."
    "But a part of me does."
    "Or did."
    "I don’t know."
    "But such is the art of never knowing."
    "Something that resembles love digs its jagged fingernails into my beating heart and sinks its teeth in once it's inside."
    "It’s not much."
    "But it’s enough for me to say it to her without feeling like a complete liar."
    "For the kind of love that Chika both has and wants is the kind that exists to be traded between two entities."
    "And that kind of love does not exist to me."
    "Nothing exists to me."
    "I wish it did."

    scene datewar21
    with dissolve

    ch "Chinami has returned!"
    ch "Please help yourselves to-"

    play sound "glass.mp3"
    scene datewar22
    with hpunch

    ch "…"
    s "…"
    c "…"
    ch "Chinami is in trouble, isn’t she?"

    scene black
    with dissolve2

    "Chika laughs it off and helps her sister clean up the mess."
    "It’s a horrible date."
    "I enjoy every second of it."

    $ renpy.end_replay()
    $ dormwar12 = True
    $ dorm1warpoints += 1
    stop music fadeout 8.0

    "………"
    "……"
    "…"

    jump dormwar13
...
```