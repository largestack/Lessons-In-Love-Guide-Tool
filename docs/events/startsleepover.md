# A New You
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=startsleepover&go=Go)


Part of event chain [Every Day I Grow Some More](./start.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: startsleepover
* Group: Main
* Triggered by label: nextstartt

## Event code
File: \game\script.rpy
Code:
```python
...
label startsleepover:
    scene bathscenebutnomorebath1
    with dissolve2

    s "Uhh...Ami?"
    a "Yes, dearest uncle?"
    s "Would you mind...you know...reminding me what the name of the city we live in is?"

    scene bathscenebutnomorebath2
    with dissolve

    a "Jeez, even that's gone?"
    s "Just assume that {i}everything{/i} is already gone since it'll wind up saving the two of us a ton of time."
    a "Not {i}everything{/i} is gone, Sensei. I'm sure your love for me would remain no matter what sort of crazy thing happened to your brain."
    a "But, you're right. It's already kinda late out and I should be spending less time questioning you and more time helping you get back to normal."

    scene bathscenebutnomorebath3
    with dissolve

    a "So, allow me to {i}re-{/i}introduce you to Kumon-mi! A super normal town just outside of Tokyo."
    a "We’re not allowed to leave the city limits anymore because of the war, but-"
    s "Wait, war? What war?"

    scene bathscenebutnomorebath2
    with dissolve

    a "The same war we've been in for years now."
    a "Like 99%% of the men were drafted into the space army and are off fighting aliens right now or something."
    s "Is this...some sort of joke? Or..."
    a "Joke? No. It's super real."
    a "And you should be thankful you weren't one of the people who got drafted since you're a teacher and we need more people like you to make sure everyone in our class doesn't wind up like Miku."

    "I have no idea who that even is..."

    s "Is the war really in space, though?..."
    a "Of course. It's an important aspect of the plot that is going to be used as comedic relief in the future, so don't try and focus too much on it or you'll wind up getting distracted from everything else."
    s "Everything else meaning {i}what,{/i} exactly? Are there some other...weird rules about this place I need to be lectured on now?"

    scene bathscenebutnomorebath4
    with dissolve

    a "A few! But really, the hardest part of everything is that the girl-to-boy ratio is completely out of whack and I wouldn't be surprised if you go weeks or months without seeing other men sometimes!"
    s "I see no problem with this."

    scene bathscenebutnomorebath5
    with dissolve

    a "Well, you should. That's the part where you were supposed to say, “You're the only girl for me, Ami! I don't care about any of the other ones!”"
    s "Aren't we related?"

    scene bathscenebutnomorebath6
    with dissolve

    a "Enough about that, how 'bout we get back to some of those rules you were just talking about?"
    s "Are we really going to ignore the blatant incestuous undertones you-"
    a "Rule number one is keep your hands off all of your students! But that should probably be a rule that goes without saying since...you know."
    s "Is that, like...an Ami rule? Or is that an actual school rule?"
    a "I'm pretty sure it's a law. But it's also a school rule."

    scene bathscenebutnomorebath7
    with dissolve

    a "Technically, the rule only applies to school grounds, though...since no one can really keep track of what you do elsewhere."
    s "Right...and is there anything else I should be worried about?"

    scene bathscenebutnomorebath1
    with dissolve

    a "Probably! So just ask me whatever comes to mind and I'll help you out the best I can!"

label amiwhattodo:
    menu:
        "Tell me about my students":
            s "Can you tell me a little bit about my class?"
            a "You mean {i}remind{/i} you a little about your class?"
            s "Yeah...that. Sorry."
            a "Don't apologize to {i}me,{/i} Sensei. I'm used to dealing with you when you're at your worst. This sort of thing doesn't bother me at all."
            a "You're the only male teacher at an all-girls school...and there are ten total students you’re in charge of- including me!"
            a "Our school works a little different from the other high school in that we’re in your care for every class of the day."
            a "Sometimes, a student or two might not show up to class. A couple of them have cutting problems."
            a "I also think I heard something about more students joining later on in the year as well!"
            a "Sometimes, classes get a little crowded and people need to be moved around and stuff."
            a "Oh, in addition to being our teacher, you’re also our guidance counselor!"
            a "Some of the girls have issues they have a hard time discussing, so getting them to open up is part of your job."
            a "Since the semester has only just begun, some of them are still in the process of warming up to you."
            a "Oh! But then there are also some girls like Ayane and Maya who you've known for years since they come to our house to sleep over all the time."
            a "If you have any more specific questions about them, it would probably be better to check that weird book thingy you always keep lying around in your room."
            s "Book thingy?"
            a "I'm not really sure what it is since you won't let me look inside, but I'm pretty sure it's like...info on all of the students or something."
            a "Probably school related stuff since I know you'd never hide anything from me. Right, Sensei?"
            s "Uhh...yeah. Sure."
            a "Great!"
            a "So, any other questions?"

            jump amiwhattodo

        "Where are your parents?":
            s "What about your parents? Why aren't you staying with them instead of-"
            a "Ask something else."
            s "But-"
            a "{i}Ask something else.{/i}"

            jump amiwhattodo

        "What should I do?":
            s "So...what should I do?"

            scene bathscenebutnomorebath2
            with dissolve

            a "Hm? What do you mean?"
            s "Like...apart from teaching and...counseling or all of the other stuff my job requires me to do."
            s "I guess what I'm asking is...what is a normal day like for me?"

            scene bathscenebutnomorebath1
            with dissolve

            a "Oh, okay! Gotcha."
            a "I don't know. That's kind of a tough question."
            a "There's tons to do in Kumon-mi. And I'm sure you'll find plenty of ways to keep yourself entertained when you're not working or hanging out with me."
            s "You know, I kind of figured a girl your age would be a little more interested in spending time with her friends rather than her uncle."

            scene bathscenebutnomorebath8
            with dissolve

            a "I...can do both!"
            a "And I won't let you make me feel like a loser because I like being closer to someone with the same blood as me!"
            s "Having the same blood is just a pretty specific thing to look for in a companion is all."
            a "I just told you! I won't let you make me feel like a loser just because I like spending time with you!"
            s "And I won't try to do that anymore, I guess."
            s "Again, I'm just trying to figure out how to use what little free time I'll have and...no offense, but I'm sure not all of it will be spent on you."

            scene bathscenebutnomorebath2
            with dissolve

            a "You can't just say “No offense” right before saying something super offensive, Sensei. It doesn't work that way."

            scene bathscenebutnomorebath1
            with dissolve

            a "But I guess expecting you to speak normally is a little much to ask since everything else seems to be different about you today anyway!"
            a "So, is there anything else you want to know?"

            jump amiwhattodo

        "Tell me more about the war":
            s "Can you tell me more about that war you mentioned earlier?"
            a "Nope!"
            s "Oh."
            s "Oh, okay."
            a "Anything else you want to know?"

            jump amiwhattodo

        "Let's just move on":
            jump nextstart

label nextstart:
    s "I think I know everything I need to. Let's just go home and I'll...figure the rest out from there."
    a "Cool! In that case, I-"

    scene bathscenebutnomorebath9
    with dissolve

    a "Ah! Wait!"
    s "What? What's wrong?"
    a "What's {i}wrong-{/i} is that Maya has been sitting all by herself over there this entire time and we haven't even noticed her."
    a "Maya! We're coming to say hello whether you like it or not!"

    scene black
    with dissolve2

    "Ami charges away from me and I am stricken with the harsh realization that I might not be getting home as early as I was anticipating..."

    scene mayacg1
    with dissolve2

    m "..."

    "I stop caring about that the moment I see her friend, though."
    "If I'm remembering correctly, this is one of the girls that Ami claims I've known for years."
    "Hopefully, that means I've already got some decent footing with her and that my...romantic options are not limited solely to an extremely clingy family member."

    a "Hello! Earth to Maya! Ami and Sensei reporting in."
    s "Yes. Sensei. That is who I am."

    scene mayacg2
    with dissolve

    m "Hm?"

    "The girl suddenly looks up, ignoring Ami and locking eyes with me for an uncomfortably long time."
    "Well...in all actuality, it's probably only a few seconds. But her gaze is piercing enough to make it feel longer."

    m "…"
    s "…"
    m "…"
    s "…"
    m "Sorry, who did you say you were again?"
    s "...Sensei?"
    m "Is that so?"
    s "Uhh...yes?"

    scene mayacg3
    with dissolve

    a "Don’t mind him. He’s just tired from his nap. You saw him sleeping at the end of class, right?"

    scene mayacg4
    with dissolve

    m "Yes. Which, might I add, is a thing I'm {i}pretty{/i} sure teachers aren't supposed to be doing."
    s "You can talk to me directly, you know. You don't have to relay your problems with me to Ami."

    scene mayacg6
    with dissolve

    m "Pass."
    a "Don’t mind Maya. She can be a little...grumpy at times. I'm sure it's nothing personal."

    scene mayacg5
    with dissolve

    m "I wouldn't be {i}too{/i} sure if I were you."

    "Okay. Maybe knowing this girl for years is not quite enough to put me on good footing with her just yet."
    "For the time being, my options remain limited to just one."

    scene mayacg4
    with dissolve

    a "Oh, Maya. Are you still planning on coming over tomorrow night?"
    m "Are you sure you don't want to come to the dorm instead?"
    a "Are you only saying that because it's our turn to take out the trash?"
    m "Only? No. But I would be lying if I said that was not one of many factors contributing to how little I want to be in the same building as your uncle."
    a "You're in the same building as him every day, though."
    m "I know. It's horrible."

    scene mayacg5
    with dissolve

    a "Sensei! You're okay with Maya sleeping over tomorrow, right? Ayane is probably going to come too but she might have some stuff to do with Sana instead."
    a "I won't really know until tomorrow."
    s "Sure, yeah. Do whatever you want."

    "It's not like I'm going to complain about even {i}more{/i} attractive teenagers with preexisting ties to me being invited over to my house."
    "Unless this Ayane girl also feels the same way Maya does about me, which...would really call into question just who the previous Sensei was as a person."

    scene mayacg6
    with dissolve

    m "Please go straight to your room once you get home tomorrow and do not leave until {i}I{/i} leave. Can you do that?"
    s "Do you really dislike me that much?"
    m "I think {i}abhor{/i} is a better word, but yes."

    scene black
    with dissolve2

    "Ami and I don't stick around for much longer as Maya has to return to the dorm for...some reason she probably made up as an excuse to get away from me."
    "And while I'm still confused about why she's treating me with such disdain after barely saying anything to her, I'm not going to dwell on it for too long."
    "There are plenty of other girls I'm going to be meeting soon, and expecting all of them to like me right away would be..."
    "Well, let's just say it wouldn't be any fun at all."
    "This life is already proving to be full of conveniences and windows of opportunity that I would have expected to remain locked indefinitely given the type of person I am."
    "If {i}everything{/i} was like that and there were no windows I had to pry open myself-"
    "I can't imagine I'd be happy."
    "Conveniences are only blessings in small doses. Once they surround you, they become the norm and detach from any sort of {i}convenience{/i} at all."
    "I want something to chase after."
    "..."
    "And I have already found at least {i}one{/i} thing with a substantial head start."
    "........."
    "......"
    "..."

    scene bathscenebutnomorebath10
    with dissolve

    a "So, here we are! Home sweet home."
    s "Huh...It’s actually pretty nice in here."
    a "I’d hope so! You {i}do{/i} live here after all."
    s "I'm assuming you're the one who keeps things this...clean?"
    a "Mhm! So you don't have to worry about any of that stuff and can just relax whenever you're home. I'll take care of the rest."
    a "I {i}might{/i} ask you to take the trash out if the bags are too heavy, though."
    s "Oh, that reminds me-"
    s "Uhh...Maya said something about dorms, didn't she?"
    s "How come you're living here instead of over there? Isn't that where everyone else is?"

    scene black
    with dissolve2

    "Ami spins around and greets me with a stare that leads me to believe this isn't the first time she's been asked something like this."
    "I'm sure her apparent clinginess has something to do with it but, at the same time, it's not like the dorms would be {i}that{/i} far away, right?"
    "Is she really so dependent on me that she can't even {i}begin{/i} tearing herself away?"
    "Or..."
    "Is it maybe the other way around?"

    scene bathscenebutnomorebath11
    with dissolve2

    a "Are you trying to get rid of me now?"
    s "Of course not. I just figured that most girls your age would never turn down the opportunity to live with their friends."
    a "And I'm sure you know {i}all{/i} about what girls want...right, Sensei?"
    s "You still call me that even when we’re home?"
    a "Is that weird?"
    s "Kind of, yeah."
    a "Well, you better get used to it. Because I've been calling you that for so long that anything else would just make me feel...weird."

    scene bathscenebutnomorebath12
    with dissolve

    a "Besides! I think it makes things kinda fun! It's almost like we're role-playing or something! Just...we're playing our actual roles and not...creative ones."
    s "Well...whatever makes you happy, I guess."

    scene bathscenebutnomorebath13
    with dissolve

    a "Anyway, I'm gonna go get dressed and start preparing dinner. Is there anything you want to eat tonight or should I just...do whatever?"
    s "Just do whatever. I'm not really that picky."
    a "Works for me!"
    a "If your brain is still being weird, you should use this time to check out that book thingy I was telling you about earlier."
    a "Going to work tomorrow without any idea of who the other girls are could get really nasty really quickly. So, for your safety, take your time and try to {i}at least{/i} remember everybody's names."
    s "Sure. But, uhh..."
    a "What's wrong? Change of heart for dinner? You looking for something specific now?"
    s "No, I just..."
    s "Which door leads to my room again?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene bathscenebutnomorebath14
    with dissolve2

    "I step into my room after Ami points it out to me and am quickly greeted by the sight of a bedroom slightly less...mature than I was expecting."
    "If I'm a full-time teacher and homeowner, I think it's probably time to ditch the model kits and game consoles, but..."
    "Then again, I guess I shouldn't be bashing the previous owner of this body after they ever-so-kindly presented me with what tons of other men would deem as a perfect, dream scenario."
    "..."
    "Come to think of it..."
    "I wonder what happened to the old Sensei?"
    "Or, better yet-"
    "I wonder what happened to the old {i}me?{/i}"

    stop music
    play sound "static.mp3"
    scene whyme with flash
    scene whythesky with flash
    scene whygodwhy with flash
    scene bathscenebutnomorebath14 with flash
    stop sound
    play music "10c.mp3"

    "Probably nothing."

    scene bathscenebutnomorebath15
    with fade

    "The first thing I approach is a leatherback journal positioned on the center of a nearby coffee table."
    "Without even opening it, I already know this is the book Ami was talking about earlier."
    "Why it's just...sitting out here in the open if it supposedly contains classified information on my students- I have no idea."
    "But seeing as I was just talking to you about conveniences a moment ago, I don't think something like this is {i}too{/i} out of the ordinary."
    "Or...at least what ordinary is shaping out to be so far."

    scene black
    with dissolve2

    "I open the book and flip through a few pages of notes I don't want to be bothered with before reaching the section I'm looking for."
    "In addition to having a bit of information on all of the girls, it comes complete with their pictures as well."
    "Just one more convenience in the evergrowing and possibly infinite list of them, I guess."

    scene amiclass
    with dissolve2

    "{i}Ami Arakawa...{/i}"

    if bonus == True:
        "{i}Ami is an adorable and extremely cute girl that I’ve known since she was born.{/i}"
        "{i}We’ve always been close, but it wasn't until after the accident that we became what we are now.{/i}"

        play sound "static.mp3"
        scene amibreak1 with flash
        scene beforewefall2 with flash
        scene dust5 with flash
        scene bathscenebutnomorebath15 with flash
        stop sound

        "{i}Ami doesn't like talking about the accident.{/i}"
        "{i}Neither do I.{/i}"
        "{i}It should be avoided at all costs.{/i}"
    else:
        "A highly trained certified public accountant."
        "Her parents died or something and she lives here now."

    "…"

    "I guess this sort of doubles as...Sensei’s diary, or something?"
    "This definitely doesn't seem like just school-related information thus far, but..."
    "Why is a grown man keeping something like this in his room?"
    "It doesn't have something to do with the whole guidance counselor thing, does it?"

    scene mayaclass
    with fade

    "{i}Maya Makinami...{/i}"
    "{i}Maya is a strange girl who has never liked me and has always avoided me for seemingly no reason whatsoever.{/i}"
    "{i}She’s been coming to the house for several years now but, despite that, I know nothing about her and can't imagine I'll be finding anything out anytime soon.{/i}"
    "{i}All I know for sure is that she cares deeply for Ami and...is even more deeply troubled by my existence.{/i}"
    "{i}I should avoid her at all costs as well.{/i}"
    "Well, I guess that pretty much explains why I was treated the way I was earlier."
    "It's clear that Maya would agree with Sensei's final note in her entry, but..."
    "That doesn't stop me from wondering just what her deal is."

    scene ayaneclass
    with fade

    "{i}Ayane Amamiya...{/i}"
    "{i}Ayane is another one of Ami’s close friends that has been coming to the house for years now.{/i}"
    "{i}She is...surprisingly open. Annoyingly open, even.{/i}"
    "{i}Open to the point where if I don't stop her from sharing her feelings in public, it could get me into a lot of trouble.{/i}"
    "{i}She’s incredibly flirtatious and often wanders off to talk to me instead of Ami and Maya while hanging out at the house.{/i}"
    "{i}Her parents have made several large donations to the[school] and her father is one of the few males left in the city but, despite that, Ayane bears little attachment to him.{/i}"

    scene yumiclass
    with fade

    "{i}Yumi Yamaguchi...{/i}"
    "{i}Yumi is the obligatory class delinquent.{/i}"
    "{i}She doesn't particularly seem to show any interest in associating with the other girls apart from picking fights with them on a near daily basis.{/i}"
    "{i}The only one who seems to be an exception to that is Chika.{/i}"
    "{i}She's been known to hang around the local arcade with a crowd of slightly older guys who are most likely Yakuza, but has since stopped going- likely due to the draft.{/i}"
    "{i}Her attitude seems to be getting worse every day and even calling her into my office doesn't seem to work anymore.{/i}"

    scene chikaclass
    with fade

    "{i}Chika Chosokabe...{/i}"
    "{i}Unlike Yumi, Chika is actually quite popular with all of the girls and spends a lot of time getting to know them.{/i}"
    "{i}Despite her appearance, she's very bright and consistently ranks near the top of the class when she actually applies herself.{/i}"
    "{i}The big issue is getting her to apply herself since she skips homeroom frequently to use her phone in the bathroom.{/i}"
    "{i}Chika has a good heart, but is often too caught up in her own world to notice when the one around her is beginning to come undone.{/i}"

    scene makotoclass
    with fade

    "{i}Makoto Miyamura...{/i}"
    "{i}Makoto is the student council president, class representative, and self-proclaimed teacher’s assistant.{/i}"
    "{i}She seems to be almost immune to the opinions of others and has no problem sucking up to me at all times, likely due to admiration rather than an innate desire for a recommendation letter.{/i}"
    "{i}She’s the top student in her grade and has caused absolutely no problems whatsoever, often times keeping the entire class afloat when I am unable to.{/i}"
    "{i}Makoto's biggest flaw is that she goes above and beyond far too frequently, to the point where I believe it might be damaging to her.{/i}"

    scene futabaclass
    with fade

    "{i}Futaba Fukuyama...{/i}"
    "{i}Futaba is an extremely kindhearted girl, but greatly struggles with a variety of self-esteem issues and often elects to sit out of physical education as a result of them.{/i}"
    "{i}She is a constant target for Yumi's bullying, but is otherwise loved by the rest of the class and is always willing to lend an ear to anyone in need.{/i}"
    "{i}Futaba performs very well in Japanese Literature and spends most of her time reading, but she can get lost in daydreams at times and must be broken out of them.{/i}"
    "{i}In order for her to succeed, she will need to learn to love herself. Thankfully, she takes well to positive reinforcement and is significantly stronger than she looks.{/i}"

    scene mikuclass
    with fade

    "{i}Miku Maruyama...{/i}"
    "{i}Miku has a hard time figuring out when to stop talking. In fact, I don't think she has ever figured it out even once.{/i}"
    "{i}She has far too much energy for her own good and constantly needs to be reminded to either quiet down or stop running in circles around the classroom.{/i}"
    "{i}She excels in physical education and is arguably the strongest player on the school's soccer team.{/i}"
    "{i}When it comes to every other class or subject, however, she needs a significant amount of additional coaching.{/i}"
    "{i}Thankfully, she's very close with Makoto and seems to care deeply about keeping her happy.{/i}"

    scene rinclass
    with fade

    "{i}Rin Rokuhara...{/i}"
    "{i}Rin might look like the cool, calm, and collected type, but she has proven to be a bit unpredictable and far too excitable more times than I can count.{/i}"
    "{i}She goes through short periods of time where she doesn’t act like herself and has disappeared for days on several occasions.{/i}"
    "{i}She’s hesitant to come to me for counseling and seems like the type to ignore her problems rather than make a genuine effort to resolve them.{/i}"
    "{i}That aside, she's universally liked by everyone in the class and has never been known to cause problems for anyone other than herself.{/i}"

    scene sanaclass
    with fade

    "{i}Sana Sakakibara...{/i}"
    "{i}No one really knows anything about Sana other than Ayane.{/i}"
    "{i}She's extremely quiet and vehemently refuses to talk under almost all circumstances, but it's less because she doesn't want to and more because she can't.{/i}"
    "{i}It remains to be seen whether this is simply how she is or if there is something about her past that is causing her to be this way-{/i}"
    "{i}But without many opportunities to actually speak with her, I'm not sure if I'll ever really know anything or not.{/i}"

    scene bathscenebutnomorebath16
    with fade

    "So...that's my class, I guess."
    "It seems like there's a fair bit of diversity in terms of personalities, but I guess I won't be able to confirm anything for sure until I make it to school tomorrow, though."
    "A few of the girls seem like they might be a bit harder to {i}crack{/i} than the others, but...seeing as this is apparently my life now, I'm sure I'll have plenty of time."
    "The issue is just...figuring out who to talk to first."
    "Sure, Ami would likely be the easiest out of everyone- and the most accessible too."
    "The problem is that Ami seems almost {i}too{/i} accessible- to the point where, even now, I feel like she's hovering right over my shoulder."

    a "Do you remember everyone's names yet? Want me to quiz you?"

    scene bathscenebutnomorebath17
    with dissolve

    s "..."
    a "..."
    s "You're really quiet."
    a "Yeah. That's a special skill of mine."
    a "But in my defense, Sensei, I {i}did{/i} knock like three times before coming in here."
    a "And with how out of it you've been since we left school, I was worried your brain might have melted or something like that."
    a "You're lucky your loving niece was willing to come check on you rather than just calling an ambulance and letting them handle it."
    s "I'm flattered, really."

    scene bathscenebutnomorebath18
    with fade

    a "Dinner's in the oven right now, so you can go ahead and take a bath while it's cooking."
    a "I already warmed the water up for you...and I want to wait until right before I go to sleep to get in since that's what always makes my hair look best the next morning."
    s "Given how much of it you have, I'm sure it takes the entire night to dry as well."
    a "Yup! I'm pretty sure that if I put it into a ponytail while it's still wet and swing it really hard, I can probably kill someone."
    s "Great. I can't foresee a future in which that ever needs to happen, but I'm glad that you've found a way to weaponize your body so early in life."
    a "Sensei, you realize that every second you spend talking to me here is just making the bath cooler, right?"
    s "I know, I know. I'm going."
    s "But before I get in..."
    s "Thank you, Ami. For...answering all of my questions today and...just immediately accepting my existence."
    a "Saying it like that makes it sound like you didn't exist {i}until{/i} today, Sensei. And we both know that's not true at all."
    s "Yeah..."
    s "Yeah, I guess we do..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "The bath is perfectly warm once I get in...and dinner is perfectly cooked once I get out."
    "It's an amazing first day here in Kumon-mi."
    "But nothing this good can possibly last forever."
    "And I know that all of the conveniences being passed out like promotional tissues will soon become too much to bear."
    "There is no world so abundantly good...and I will not allow myself to be lured into believing such a world exists just because of a hot bath and a fresh plate of food."
    "Tonight, I will sleep."
    "And when I wake up-"
    "If I wake up in {i}this{/i} world-"
    "If none of this was a dream-"
    "I will start a new life."
    "And I will do my best to cherish it."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ clichebath = True
    $ ami_love += 1
    play sound "eggcrack.mp3"

    "{i}Congratulations! Ami’s affection has increased to 1!{/i}"
    "{i}In Lessons in Love, affection points are used to unlock the next step in each girl’s story.{/i}"
    "{i}Affection points may be gained through main story events and/or spending your free time with the girls.{/i}"
    "{i}Some events are locked to progress with certain characters, so make sure to level up all of them and not neglect anyone!{/i}"
    "{i}You can view your affection with the girls through the progress menu at the bottom of your screen. This will also show you how much content is available for each character.{/i}"
    "{i}For a more detailed look at each girl's content, you may view their character profiles. This is also where scene replays will be stored once you unlock them.{/i}"
    "{i}An event tracker for main events is accessible through the menu as well! And don't worry about skipping certain events if they aren't triggered in order.{/i}"
    "{i}Some events require very specific conditions to be met in order to trigger, so unless you see something crossed out in red, it is still obtainable.{/i}"
    "{i}Oh, and did I mention that all events are replayable by clicking their respective titles in the tracker? Because they are!{/i}"
    "{i}This will come in handy once I start showing you how much I hate you.{/i}"
    "{i}Anyway! This marks the end of Day 1!{/i}"
    "{i}Your true journey begins now!{/i}"
    "{i}Enjoy your stay in Kumon-mi!{/i}"
    "{i}And please accept this next scene as a token of my gratitude for spending time with me in here.{/i}"
    "………"
    "……"
    "…"

    $ totaldays += 1
    $ day += 1
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
        jump firstfriday
    else:
        jump firstfriday

label firstfriday:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```