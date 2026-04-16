#------Day 16: The Power of **kwargs---------#
#Real Life Use of *args (Unlimited Items) like WA groups
#2. Real Life Use of **kwargs (User Profiles & Settings) like Amazon ya Daraz jaisi shopping site
#*AI/ML*ya*Data Science* mein jayengi,th ap dekhengi ke bare bare libraries (jaise`scikit-learn`ya`pandas`)isi
#  tarah functions use krti hn taky wo flexible reh saken.
 
def user_profile(**details):
    for key, value in details.items():
        print(f"{key.title()}: {value}")

user_profile(name = "Ayesha", age = 20, city = "Sahiwal", course = "BSCS")                


#------Task: The Smart Bio-Data Maker---------#
def make_card(**info):
    print("\n ~.-----Digital Card-----.~")
    for key, value in info.items():
        print(f"{key.title()}: {value}")

make_card(name = "Ali", studentID = "BC230412539" , hobby = "coding", university = "VU")      


#------The "Master Level" — Mixing Everything!---------#
#---def func(name):, *args: def func(*names):, **kwargs: def func(**info):---
#-----The Ultimate Challenge — The Event Manager-----#
def manage_event(event_name, *guest_name, **more_details):
    print("\n ~.---It's Eid Milan Party---.~")
    print(event_name)
    for g in guest_name:
         print(f"Our guest is: {g}")
    for k, v in more_details.items():
         print(f"{k.title()}: {v}")

manage_event("Eid Milan Party", "Sana", "sara", "hina", venue = "Ayesha's house", timing = "10am" )

