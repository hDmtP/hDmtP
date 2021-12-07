import random

quotes = {
    0: ["If u wanna get something done right, do it yourself",
        "You're right, Elias, I'm not a Ghost... I'm the man that hunts them, and sends them back to the other side!",
        "Look at what you did. [Rorke kicks Hesh] You're good. You would have been a hell of a Ghost. But that's not gonna happen. There ain't gonna be any Ghosts... We're gonna destroy them together.", " Everyone breaks, Elias!",
        "Shit, son.", " You know our laws, son. You fail to protect your brothers...you join them in death.",
        "I am Gabriel Rorke. I have been trained by your Government to be a weapon. Trained to kill and destroy. All in the name of Liberty and Justice. Even surrender my very life in service to your country. But I am not one of you. The \"Just\" have turned their backs and become deaf to your cries. Who, then will show them justice? Who will show you the Liberty they have promised? The weapon they have created will be their undoing. But do not fear this. Do not fear me. It is only natural. Like the collapse of Rome, your cities will crumble and there will be great sorrow. But from the ashes of this diseased metropolis, a rebirth will occur. It will be paid for in blood and steel. Liberty must be restored. I am Gabriel Rorke, and I am here to show you the true meaning of justice.",
        "What's the matter? You look like you've just seen a ghost.",
        "Time to work, soldiers."],

    1: ["The healthy human mind doesn't wake up in the morning thinking that this is its last day on earth. But I think that's a luxury, not a curse. Knowing you're close to the end is a kind of freedom. Good time to take... inventory. Outgunned. Outnumbered. Out of our minds. On a suicide mission. But the sand and rocks here stained with thousands of years of warfare, they will remember us. For this. Because out of all our vast array of nightmares, this is the one we choose for ourselves. We go forward like a breath exhaled from the Earth. With vigor in our hearts and one goal in sight: We. Will. Kill him.",
        "Right… What the hell kind of name is Soap, eh? How'd a muppet like you pass Selection?",
        "The package is aboard a medium freighter. Estonian registration number 52775. There is a small crew and security detail onboard.",
        "Nikolai's in hell right now, we're gonna walk him out. We take care of our friends. Let's move.",
        "All right. Let's top these bastards before they kill the old man.",
        "Why'd you do it? Where did you get the bomb?",
        "Zakhaev's son, commander of the Ultranationalist forces in the field. Rotten apple doesn't fall far from the tree. The Loyalist, Kamarov, has got a location on the kid.",
        "They've started a bloody countdown! Zakhaev's gonna launch the remaining missiles!",
        "Well at least the world didn't end. Hit it.",
        "Roger that Soap. I've found Roach. He appears to be intact.",
        "Do NOT trust Shepherd- I say again, DO NOT TRUST SHEPHERD! Soap! GET DOWN!",
        "Makarov wouldn't let this travel lightly if it didn't serve a greater purpose, and chances are the bastard will be there personally to see things off. If he's back on the grid...then so are we",
        "Soap TRUSTED you. I thought I could too. So WHY, IN BLOODY HELL, DOES MAKAROV KNOW YOU?!",
        "We're gonna have one shot to grab the President before he gives up the launch codes and Makarov turns Europe into glass. Once we get boots on the ground, it's going to get lively down there.",
        "Prisoner 627. I'm coming for you, Makarov.",
        "My war ends with you.",
        "You wouldn't have to look far"],

    2: ["This is it... Ready to make history?",
        "No, no, no, somethin's wrong. There's way too much activity.",
        "FUUUUUUUCK!", "Kravchenko. When I sliced that bastard open, it saved everyone's ass. But he comes to first, BOOM! Welcome to the Hanoi Hilton. Six months later, they shipped me over to Da Nang. And this fucking place made the Hilton look good. We lost 17 in my group. By '72, it was just me. I was not gonna die in a FUCKING SWAMP!!",
        "Thanks to your old man. He put it all on the line for me... for honor... and friendship."],

    3: ["Come my friends. 'Tis not too late to seek a newer world.",
        "Martyr me...for Cordis Die.",
        "Victory is not measured by losses Farid( *shoots a chopper with FMJ* ), its measured by gains",
        "It matters not, I am one step ahead of him",
        "We will regroup at the citadel",
        "I DECIDE WHAT IS NECESSARY!",
        "Your life will be consumed by absolute losses, then and only then you will understand what you have done to me.",
        "You suffer with me!"],

    4: ["You did it, Mason! You did what I could not!",
        "The men and I had fought through the most bitter of winters on the Eastern Front, but we were no strangers to the cold. Even now, the blood in my veins chills when I think back to the events of that day... Far, far from home...",
        "Today, my comrades... Vorkuta... BURNS!!!",
        "Die like the RATS you are"],

    5: ["I'd given up hope of ever gettin' out. But Viktor Reznov found a way.",
        "It's Weaver. He's burnt.",
        "You should have stayed in Vorkuta.",
        "Woods! You look like hammered shit!",
        "How many times?! Steiner was at Rebirth Island! We had to kill Steiner!",
        "I remember...Ahhhh! Vorkuta...",
        "Where am I? Where's Reznov?",
        "My name is Viktor Reznov, and I will have my revenge!",
        "Your evil has claimed the lives of many good men! No longer!",
        "That young kid didn't make it....I swear to God that Woods was crying but he never let us see no tears.",
        "I keep hearing the fucking numbers!",
        "You will move without boundries. You will act above the law. You will use any means necessary to stop the wars that are hidden from the world. And if you succeed, you will do so, without any recognition. Because you do not exist.",
        "You tried to make me KILL MY OWN PRESIDENT!",
        "It's Uncle Woods, son. He'd do it for me.",
        "Turns out you're a lousy shot.",
        "I made the mistake of not confirming the kill five years ago at Baikonur.",
        "It's all in your mind, Woods."],

    6: ["Reznov's dead, Mason! Do you hear me!? HE'S DEAD!",
        "Jason Hudson, CIA. We're here to talk about your encounter with Russians in Laos. We got word a defector might be in play.",
        "Or you can give us what we want, and we guarantee your safety.",
        "Damn it! Why can't you remember!?",
        "Fuck! Okay...Me! Do it... DO IT!!!"],

    7: ["What happens here today will change the world forever. Nothing can stop this. Not even you.",
        "This deal will generate millions for our cause. Money can buy many things. Even power. The road to our future begins here, my friend.",
        "So Makarov is the prize.",
        "The American thought he could deceive us. When they find that body... all of Russia will cry for war.",
        "Russia will take all of Europe, even if it must stand upon a pile of ashes. I want the launch codes, Mr. President.",
        "Every man has his weakness. (to his men) Find the girl.",
        "Yuri, my friend. You never should have come here.",
        "Goodbye, Captain Price.",
        "С нами бог. Remember - no Russian.",
        "For Zakhaev." ,
        "That was no message....this is a message.",
        "Price, one day, you're going to find that cuts both ways.",
        "Shepherd is using Site Hotel Bravo. You know where it is. I'll see you in hell.",
        "Первый. Уничтожите вражескую надежду на победу. (First. Destroy the enemy's hope for victory.), Второй. Используйте все в своих интересах. (Second. Use everything to your advantage.), Третий. Используйте слабости противника. (Third. Take advantage of your enemy's weakness.), Четвёртый. Атакуйте с неожиданной стороны. (Fourth. Attack from the unexpected side.)",
        "It doesn't take the most powerful nations on Earth to create the next global conflict. Just the will of a single man.",
        "You think I am mad, but soon, you shall see, that every move, every strike, was meant to bring us to this.",
        "The symbols you have always looked to for strength, are smoldering in ruins. This is what your greed has brought you.",
        "All warfare is based on deception. For years, the West's hypocrisy has made the world a battlefield. The corrupt talk; while our brothers and sons spill their own blood. But deceit cuts both ways. The bigger the lie, the more likely people will believe it, and when a nation cries for vengeance, the lie spreads like a wildfire. The fire builds, devouring everything in its path. Our enemies believe that they alone dictate the course of history, but all it takes is the will of a single man.",
        "You know who I am? Then you know what I want.",
        "Captain Price - Ад ждет тебя. (Hell awaits you.)",
        "Today, we show the world our true strength. Perhaps it will give you some as well.",
        "Understand, Yuri: this is only the beginning.",
        "I see...this is what we are dealing with, brothers. A stubborn old man, hopelessly out of step with the changing world.You too, will change. Are you listening?",
        "Like it ended for Captain MacTavish? Tell me, Price. How long did it take him to die?",
        "I've destroyed your world piece by piece. It's only a matter of time until I find you."],

    8 : ["Today we reshape the world. Our motherland is lead by cowards and weaklings. In time, the Americans and their NATO puppets will bring the Soviet Union to its knees. We will break the stalemate, then burn them both to the ground. They sleep soundly at night, knowing they put on a good parade - but they lack the will to do what must be done. The superpowers will fall, victims of their own greed and corruption. We will rebuild Greater Russia from the ashes.",
        "Comrades, the United States and its allies have slowly consumed that which is dear to us. Our leaders continue to weaken under this threat. It is the MORAL duty of `Perseus` to act when they will not. Soon we will possess an American Nuclear Bomb, the key to unlock their entire Greenlight arsenal. Once we control the green light arsenal we will detonate them all from the safety of Solvetsky",
        "Come, there is still must to be done"],

    9: ["The name's Butcher, your new quartermaster for the duration of the Winter Siege",
        "First off, we've intercepted a shipment of Gewehr 43's. I'll give the Krauts one thing, they know how to make a sturdy bloody rifle.",
        "Then we have the Sten. This lightweight SMG is quite the little firecracker, just the ticket for the some close-quarters butchering.",
        "Lastly, the GPMG, a light machine gun that can drop an entire squad faster than you can blink, mate.",
        "Time to get down to business.",
        "Oi! Quit while you're still breathin'.",
        "Grab some supplies and get off to Paris. They need you there.",
        "Just when I thought I'd be gettin' back to the fight, you show up looking like a kid in a sweet shop. Take your pick and get a move on!",
        "Looking to uh, blow up a bridge? Take out a supply depot? Reclaim a city? I've got what you need.",
        "You must have a deathwish, soldier.", "Ahh... feeling a bit down lately, away from the fight. It's been a while since I've, had a good therapeutic bridge demolition.",
        "Don't see that everyday... You're alright, I suppose.",
        "I'm Captain Butcher of the SOE. Well, retired Captain Butcher these days. I was in charge of the SOE during the war. Ever heard of Vanguard?"]
        
}

def choice():
    keys = (list(quotes.keys()))

    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)
    random.shuffle(keys)

    ch = random.choice(keys)

    ch_ch = quotes[ch]
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)
    random.shuffle(ch_ch)

    ch_ch_ = random.choice(list(ch_ch))

    return ch_ch_
