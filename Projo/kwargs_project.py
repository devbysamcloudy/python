def save_user_data (name, **kwargs):
    print ("Name is", name)
    print("kwargs are", kwargs)
    for key in kwargs:
        print("The key is",key)
        value = kwargs[key]
        print("The value is", value)
        
save_user_data("John", favorite_color="blue", favorite_food="pizza", favorite_movie="Inception")
save_user_data(
    "Alice",
    age=30,
    city="New York",
    profession="Engineer",
    hobbies=[
    "reading",
    "hiking",
    "cooking"
        ],
        favorite_music="rock", 
        favorite_sport="tennis",
        favorite_book="To Kill a Mockingbird",
        favorite_tv_show="Breaking Bad",
        favorite_animal="dog",
        favorite_season="spring"
        )
def collect_user_info ():
    name = input("Enter your name: ")
    print("------------------------------------")
    print("You can fill out your bio")
    print("Enter category names")
    print("-------------------------------")
    user_data={}
    while True:
        category_name = input("Enter category name:")
        if category_name =="done":
            break
        category_description = input("Enter description:")
        user_data[category_name] = category_description
        #print(user_data)
        save_user_data(name, **user_data)

collect_user_info()
