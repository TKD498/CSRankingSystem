import json
import datetime

file_path = 'github_mock.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
    length_of_user_commit_history = len(data)
    # Update code to grab user specific commit history!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
datetime_format = "%Y-%m-%dT%H:%M:%SZ"
most_recent_commit_date = data[0]['commit']["date"]
most_recent_commit_datetime_obj = datetime.datetime.strptime(most_recent_commit_date, datetime_format)
most_recent_commit_week = (datetime.date(most_recent_commit_datetime_obj.year, most_recent_commit_datetime_obj.month, most_recent_commit_datetime_obj.day).isocalendar().week)

today_date = datetime.datetime.now()
today_datetime_obj = datetime.datetime.strptime(most_recent_commit_date, datetime_format)
today_day_of_year = datetime.datetime.now().timetuple().tm_yday

def daily_commit_frequency():
    daily_streak = 0
    next_commit_date = data[0]['commit']["date"]
    commit_date = next_commit_date
    
    for i in range(0, length_of_user_commit_history - 1):
    
        #Check to make sure commit_date and nex_commit_date are different
        if next_commit_date == commit_date:
            next_commit_date = data[i + 1]['commit']["date"]

        #Make datetime objects for the different dates
        next_datetime_obj = datetime.datetime.strptime(next_commit_date, datetime_format)
        datetime_obj = datetime.datetime.strptime(commit_date, datetime_format)       

        if datetime_obj.year != next_datetime_obj.year:
            # It's been more than a year so no daily streak exists
            pass
        elif ((datetime_obj.day - next_datetime_obj.day) * -1) >= 2:
            # it has been more than a day so daily streak is broken
            pass
        elif ((datetime_obj.day - next_datetime_obj.day) * -1) == 1:
            # Daily streak exists! update daily streak
            daily_streak += 1
        commit_date = next_commit_date
        next_commit_date = data[i + 1]['commit']["date"]
        
        
    return daily_streak

def weekly_commit_frequency():
    weekly_streak = 0  
    
    for i in range(0, length_of_user_commit_history):
        commit_date = data[i]['commit']["date"]
        datetime_obj = datetime.datetime.strptime(commit_date, datetime_format)
        commit_week = (datetime.date(datetime_obj.year, datetime_obj.month, datetime_obj.day).isocalendar().week)
        
        if commit_week == most_recent_commit_week:
            weekly_streak += 1
            most_recent_commit_week -= 1
        elif (commit_week + 1) == (most_recent_commit_week):
            weekly_streak += 1
            most_recent_commit_week -= 1
        else:
            break
    
    return weekly_streak

# print(weekly_commit_frequency())
# print(daily_commit_frequency())

active_repos = {"user1": {
    "personal_repositories" : {
        "project1" : "active",
        "project2" : "not active",
        "project3" : "not active",
    }
}}


def active_independent_repositories():
    # Checks all of the users repos to see which ones they commited to in the last 30 days
    
    # Ideally this is in a database and that is what I'm checking against
    users_repositories = {}
    
    for i in range(0, length_of_user_commit_history):
        commit_date = data[i]['commit']["date"]
        datetime_obj = datetime.datetime.strptime(commit_date, datetime_format)
        commit_month = datetime_obj.month
        commit_date_day_of_year = datetime_obj.timetuple().tm_yday
        
        if data[i]['username'] == data[i]['commit']['repository']['owner']:
            users_repositories[f"{data[i]['commit']['repository']['name']}"] = "Not Active"

    # if users_repositories[]
        if (today_day_of_year - commit_date_day_of_year) > 30:
        # this logic doesn't work when we go into a new year, thats okay though
           pass
        
    #     if commit_month == today_datetime_obj.month:
    #         if data[i]['username'] == data[i]['commit']['repository']['owner']:
    #             users_repositories[f"{data[i]['commit']['repository']['name']}"] = "active"
                
    
    # if today_datetime_obj.month == most_recent_commit_datetime_obj.month:
    #     print("personal repo is active")
    print(users_repositories)
        

active_independent_repositories()

def pull_request_merges():
    pass

def github_points_awarded():
    pass

def calculate_github_rank():
    pass