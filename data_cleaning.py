#Cleaning and Structuring the data: 
import json

#load the data
def load_data(file_name):
    with open(file_name,"r") as f:
        data=json.load(f)

    return data

data= load_data("store_data.json")
print(data)


def clean_data(data):
    text_to_num={"one":1,"two":2,"three":3,"four":4,"five":5}
    cleaned_data=[]
    unique_users=set()

    for user in data:
        #clean ratings from the data, problems like text to number, spaces etc
        raw_rating=str(user["rating"]).strip().lower()

        if raw_rating in text_to_num:
            raw_rating=text_to_num[raw_rating]

        user["rating"]=raw_rating

        #handling missing values
        raw_age=user.get("age")  #this .get function will give the null value if there isn't a data instead of error

        if raw_age == None:
            user["age"]=None

        #handling duplicate data
        if (user["name"].strip() in unique_users):
            continue

        unique_users.add(user["name"])
        cleaned_data.append(user)

    return cleaned_data


# to get meaningful insights from the data
def get_insights(data):

    #avg rating
    total_rating = 0

    for user in data:
        total_rating+=float((user["rating"]))

    print(f"the average rating = {total_rating/len(data)}")

    #percentage of user with poor ratings
    poor_ratings=0

    for user in data:
        if(float(user["rating"])<3):
            poor_ratings+=1

    print(f"percentahe of user with poor rating = {poor_ratings/len(data)*100}%")


get_insights(data)


# build a recomendation feature 
def get_recommendations(data):
    recommendations=[]

    for user in data:
        current_recom={}
        current_recom["name"]=user["name"]

        if (float(user["rating"])>=4):
            current_recom["brand"]="Apple"
        else:
            current_recom["brand"]="Samsung"
            
        recommendations.append(current_recom)

    return recommendations


get_recommendations(data)
