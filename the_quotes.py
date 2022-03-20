from datetime import datetime
import random

quotes = {
    0: ["If u wanna get something done right, do it yourself",
        "You're right, Elias, I'm not a Ghost... I'm the man that hunts them, and sends them back to the other side!",
        "Look at what you did. [Rorke kicks Hesh] You're good. You would have been a hell of a Ghost. But that's not gonna happen. There ain't gonna be any Ghosts... We're gonna destroy them together.",
        "Everyone breaks, Elias!",
        "Shit, son.",
        "You know our laws, son. You fail to protect your brothers...you join them in death.",
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
        "Kravchenko. When I sliced that bastard open, it saved everyone's ass. But he comes to first, BOOM! Welcome to the Hanoi Hilton. Six months later, they shipped me over to Da Nang. And this fucking place made the Hilton look good. We lost 17 in my group. By '72, it was just me. I was not gonna die in a FUCKING SWAMP!!",
        "FUUUUUUUCK!",
        "No, no, no, somethin's wrong. There's way too much activity.",
        "Thanks to your old man. He put it all on the line for me... for honor... and friendship."
        ],

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

    5: ["You tried to make me KILL MY OWN PRESIDENT!",
        "I'd given up hope of ever gettin' out. But Viktor Reznov found a way.",
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
        "I've destroyed your world piece by piece. It's only a matter of time until I find you.",
        "That was no message....this is a message."],

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
        "You must have a deathwish, soldier.",
        "Ahh... feeling a bit down lately, away from the fight. It's been a while since I've, had a good therapeutic bridge demolition.",
        "Don't see that everyday... You're alright, I suppose.",
        "I'm Captain Butcher of the SOE. Well, retired Captain Butcher these days. I was in charge of the SOE during the war. Ever heard of Vanguard?"]
        
}

gifs = {
    0: ["https://user-images.githubusercontent.com/65482473/145095893-faca1889-1dff-4d8e-bc1b-c5b43e7c0dff.gif",

    	"https://user-images.githubusercontent.com/65482473/145182543-51310f42-4e9f-4da1-8265-dcfed689e133.gif",

        "https://user-images.githubusercontent.com/65482473/145571417-44be4661-add9-474f-9e02-f9f7d0694bf6.gif",

        "https://user-images.githubusercontent.com/65482473/146401238-dbfab9d8-0103-4eed-a3ba-0a4b5e97225f.gif",

        "https://user-images.githubusercontent.com/65482473/145676647-caf58524-d42c-4b15-a30a-161882bbf491.gif",

        "https://user-images.githubusercontent.com/65482473/145708582-55728f4a-7a17-4d53-b868-a149626fa41b.gif",

        "https://user-images.githubusercontent.com/65482473/145710405-ccb1c679-7bd3-4ece-8a1c-f9490fc13ad1.gif",

        "https://user-images.githubusercontent.com/65482473/145710429-d716c076-e6de-446e-ab59-00f61b965278.gif",

        "https://user-images.githubusercontent.com/65482473/145710450-4aafda68-e046-4814-bd6c-3a73f6959b0e.gif"
        ],


    1: ["https://user-images.githubusercontent.com/65482473/153423543-58f8ef09-79db-4712-b62d-6279ad5116af.gif",

        "https://user-images.githubusercontent.com/65482473/153423700-d096930d-b353-42bc-a3c9-7238a7d4f7b9.gif",
        
        "https://user-images.githubusercontent.com/65482473/153423810-d2aeb2e4-8912-4f21-a2dc-d957951d4237.gif",
        
        "https://user-images.githubusercontent.com/65482473/153423922-20f9e239-303b-4821-8c31-887fb3c521cf.gif",
        
        "https://user-images.githubusercontent.com/65482473/153424059-238a14bd-8f4a-437c-9725-b6b5434febb0.gif",
        
        "https://user-images.githubusercontent.com/65482473/153424147-86838716-a813-4872-9064-a79ff0954e0d.gif",
        
        "https://user-images.githubusercontent.com/65482473/153424224-7399846c-8704-40aa-a28e-c800c95fa2e4.gif",
        
        "https://user-images.githubusercontent.com/65482473/153424459-aa4bf9d6-512c-479f-827e-ea15ce43f1b1.gif",
        
        "https://user-images.githubusercontent.com/65482473/153424540-e25ca93c-97d3-4e79-8d53-77a0b36dcd4b.gif",
        
        "https://user-images.githubusercontent.com/65482473/153424733-321e8137-1dbd-422b-a2b9-f9a04b664afe.gif",
        
        "https://user-images.githubusercontent.com/65482473/153600635-2c404723-88ed-4735-85bd-86f202209973.gif",
        
        "https://user-images.githubusercontent.com/65482473/153600698-4125ed95-01f6-4ed4-b0a3-862b8efae4ef.gif",
        
        "https://user-images.githubusercontent.com/65482473/153600776-00ef96d6-580e-4a32-89b2-b683ebc7b379.gif",
        
        "https://user-images.githubusercontent.com/65482473/153600836-c8eff82a-8bc6-4ff0-b71d-14cf7ae376ed.gif",
        
        "https://user-images.githubusercontent.com/65482473/153600905-fdae62f6-62de-4906-bc70-22ed182aa9fa.gif",
        
        "https://user-images.githubusercontent.com/65482473/153600963-4c7f540c-58a1-4008-9f5e-4b731f7ae0eb.gif",
        
        "https://user-images.githubusercontent.com/65482473/153601021-af144f8a-6252-44c1-8869-70c4ae432cac.gif"
        ],

    2:  ["https://user-images.githubusercontent.com/65482473/146401353-2d94815c-494b-4bdb-934e-14add2f68029.gif",
    
        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",
    
        "https://user-images.githubusercontent.com/65482473/146401535-faa0671a-9ecb-4c72-a79c-599b2226ac93.gif",
    
        "https://user-images.githubusercontent.com/65482473/146401438-422bb353-50e0-428a-ab36-ffe961848718.gif",
    
        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif"
        ],

    3:  [
        "https://user-images.githubusercontent.com/65482473/153222731-3b916d10-c5e7-4ace-80cc-90e195145100.gif",

        "https://user-images.githubusercontent.com/65482473/153222929-b45998ee-02cd-4158-b244-25f84b3df644.gif",

        "https://user-images.githubusercontent.com/65482473/153223057-6e9f23ab-3021-482f-a772-1af55c4a791e.gif",

        "https://user-images.githubusercontent.com/65482473/153223229-9bf8ea98-cab9-465b-a88e-875d9ea273b2.gif",

        "https://user-images.githubusercontent.com/65482473/153223303-c0e40d84-68e0-42c1-b4c0-8e8bdaad4141.gif",

        "https://user-images.githubusercontent.com/65482473/153223410-fb8fc82a-88f2-4fa3-9bd4-b789c29283d4.gif",

        "https://user-images.githubusercontent.com/65482473/153223861-45df2579-77f0-4869-9f81-5fd0c7022e1c.gif",

        "https://user-images.githubusercontent.com/65482473/153223945-04669174-0fe4-4463-9b45-7aa8f746b6fe.gif"
        ],

    4: [
        "https://user-images.githubusercontent.com/65482473/152934719-6af8ca19-2ae7-4659-8bfc-6b683daf4dc1.gif",

        "https://user-images.githubusercontent.com/65482473/152934643-9090bef3-70b1-41ba-be2f-0f33aae6078c.gif",

        "https://user-images.githubusercontent.com/65482473/152934372-2be1df7c-b905-43ea-a422-be2319c06999.gif",

        "https://user-images.githubusercontent.com/65482473/152934495-a704faa2-2d0b-45e1-a9b4-d0f1f0003f60.gif"
    ],

    5:  ["https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif"
        ],

    6:  [
        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif"
        ],

    7:  [
        "https://user-images.githubusercontent.com/65482473/154327695-8c785be0-78a0-41d2-8b77-074e5772cc47.gif",

        "https://user-images.githubusercontent.com/65482473/158032336-841824af-a086-4d1b-91f3-35bf5e7d4d36.gif",

        "https://user-images.githubusercontent.com/65482473/154327933-6a0d3189-dcc9-4523-8c36-aa89197a4a32.gif",

        "https://user-images.githubusercontent.com/65482473/154328046-5846b326-fa54-4abf-bc6c-55b2be04c7f1.gif",

        "https://user-images.githubusercontent.com/65482473/154328132-4c7d5320-70d8-40fa-a760-f6051e67e018.gif",

        "https://user-images.githubusercontent.com/65482473/154328247-d464bb67-3593-4bc4-b607-4a231e761f2a.gif",

        "https://user-images.githubusercontent.com/65482473/154328321-1e1e6767-0719-40d6-8f5f-1ee2067c9f5b.gif",

        "https://user-images.githubusercontent.com/65482473/154328417-46e1fad0-6961-4855-9e81-1dd34f4470de.gif",

        "https://user-images.githubusercontent.com/65482473/158032145-07d0ddd2-0977-434e-9925-52986d6504ab.gif",

        "https://user-images.githubusercontent.com/65482473/158031948-eace8299-05b2-4c0e-ae96-995f155807bc.gif",

        "https://user-images.githubusercontent.com/65482473/158031983-27491ada-438a-456a-b897-3d32e9af59ce.gif",

        "https://user-images.githubusercontent.com/65482473/158032002-342d2778-d25a-4bec-8dc4-bce93d1b1fca.gif",

        "https://user-images.githubusercontent.com/65482473/158032015-e753f65d-719b-4c09-8b79-6f39b3585473.gif",

        "https://user-images.githubusercontent.com/65482473/158032031-ad8d71a3-2113-4b23-8da5-4a37e1e7f1a1.gif",

        "https://user-images.githubusercontent.com/65482473/158032052-5f67c681-ad84-4269-b747-45d3ea59a46c.gif",

        "https://user-images.githubusercontent.com/65482473/158032072-404d8e20-5f87-49bb-80fe-eb21bc4bd1fb.gif",

        "https://user-images.githubusercontent.com/65482473/158032093-fba15726-164b-4652-a4ff-0e9c2258c9e4.gif",

        "https://user-images.githubusercontent.com/65482473/158032108-1b6e0b48-8ed2-42aa-8dd2-224e4b3bade9.gif",

        "https://user-images.githubusercontent.com/65482473/158032123-0b871135-3abf-4b68-a8a1-cd5f3c23156f.gif",

        "https://user-images.githubusercontent.com/65482473/158032165-2b092835-6398-422b-8da3-940275a14c49.gif",

        "https://user-images.githubusercontent.com/65482473/158032179-20e1e864-aa9c-4cf0-902f-280da9d4bc74.gif",

        "https://user-images.githubusercontent.com/65482473/158032204-82431528-d62d-4cfa-adec-4011f72f5379.gif",

        "https://user-images.githubusercontent.com/65482473/158032246-d8388213-b4b0-4e60-bac1-e958edf63991.gif",

        "https://user-images.githubusercontent.com/65482473/158032299-7aa05eca-7767-40f9-b674-8bfacc56692c.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif"
        ],

    8:  [
        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif"
        ],

    9:  [
        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif",

        "https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif"
        ],

}

"""
key = random.randint(0, len(quotes)-1)
value = random.randint(0, len(quotes[key])-1)

def choice():
    return quotes[key][value]

def choice_gif():
    return gifs[key][value]

print(f"key: {key}\n\nvalue: {value}\n\nlen(quotes[key]): {len(quotes[key])}\n\nlen(gifs[key]): {len(gifs[key])}\n\n\n")

assert len(quotes[key]) == len(gifs[key])
print("everything okay!!")
"""
the_date = int(datetime.now().strftime("%d"))
the_time = int(datetime.now().strftime("%H"))

key = ((the_date % len(quotes)) - 1)
if key == -1:
    key = 0

value = ((the_time % len(gifs[key])) - 1)
if value == -1:
    value = 0


def choice():
    return quotes[key][value]

def choice_gif():
    return gifs[key][value]

print(f"key: {key}\n\nvalue: {value}\n\nlen(quotes[key]): {len(quotes[key])}\n\nlen(gifs[key]): {len(gifs[key])}\n\n\n")

assert len(quotes[key]) == len(gifs[key])
print("everything okay!!")
