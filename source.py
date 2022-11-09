def questions_for1():
    transport = input("Input type of transport ")
    adj = input("Input any adjective ")
    part_ofbody = input("Input a part of the body")
    adj2 = input("Input other ajcective ")
    verb = input("Input a verb ")
    num2 = input("Input number ")
    noun3 = input("Input noun again ")
    part_ofbody2 = input("Input another part of the body")
    noun4 = input("Input noun (this is the last time i promise) ")
    adj3 = input("Input another ajcective ")
    silly = input("Input a silly word ")


def dialog():
    num  = input("Input number ")
    measure_oftime = input("Input measure of time ")
    noun = input("Input any noun ")    
    color = input("Input some color ")
    noun2 = input("Input another noun ")


def templates(n):
    version_1 = f"""It was about {num} {measure_oftime} ago when I arrived at the hospital 
    in a {transport}.The hospital is a/an {adj} place, there are a lot of {adj2} {noun} here.
    There are nurses here who have {color} {part_ofbody}. If someone wants to come into 
    my room iI told them that they have to {verb} first. I've decorated my room with 
    {num2} {noun2}. Today i talked to a doctor and they were wearing a {noun3} on their 
    {part_ofbody2}. I heard that all doctors {verb} {noun4} every day for breakfast.
    The most {adj3} thing about being in the hospital is the {silly} {noun} !
    """

    version_2 = f"""This weekend I am going camping with {person_name}.I packed mylantern, 
    sleeping bag, andv{noun}. I am so {adj_feeling} to {verb} in a tent. I am 
    {adj_feeling2} we might see a/an {animal}. I heard that they're kind of dangerous. 
    While we're camping we are going to hike,fish and {verb2}. I have heard that 
    the {color} is great for {verb_ing}. Then we will {adverb_ly} hike through the 
    forest for {num} {measure_oftime}. If I see a {color} {animal} while hiking, I am 
    going to bring it home as a pet ! At night we will tell {num} {silly} stories and 
    roast {noun2} around the campfire !!
    """

    version_3 = f"""Dear {person_name}. I am writing to you from a {adj} castle in an 
    enchanted forest. I found myself here one day after ride on a {color} {animal} in {place}. 
    There are {adj2} {magic_crtrs} and {adj3} {magic_crtrs2} here! In the {room} there is
    a pool full of {noun}. I fall asleep each night on a {noun2} of {nouns} and dream of 
    {adj4} {nouns2}. It feels as though I have lived here for {num} {measure_oftime}. I hope 
    one day you can wisit, although the only way to get here now is {verb_ing} on a {adj5} {noun3}!!
    """

    if n == 1:
        return version_1
    elif n == 2:
        return version_2
    elif n == 3:
        return version_3
    else:
        return None