'''
this is the python script to enrich the user_info for high pagerank score users
input:  the csv of language_userrank (username, user_rank), input as Csharp.csv
output: store into csv of language_detail ('user_id', 'user_rank', 'user_type', 'githubage', 'user_followers',
       'user_following', 'repo_num', 'gist_num', 'location', 'company')
       output as userdetail_Csharp.csv
'''
#import libraries
import re
import pandas as pd
from github3 import login
from datetime import date
import pymysql.cursors


def get_user_details(gh, userid):
    '''
    import userid get the userpublic info via github3
    input: github3 login object, userid you want to know more(string)
    output: userid(string), user_type(string), github_age(int), followers_num(int),
            following_num(int), repo_num(int), gist_num(int),location(string), company(string)
    '''
    get_user = gh.user(userid)
    dict_info = get_user.as_dict()
    #get user type
    user_type = dict_info['type']
    #get create day
    github_age = date.today().year - int(dict_info['created_at'].split('-')[0]) +1
    #get followers number
    followers_num = int(dict_info['followers'])
    #get following number
    following_num = int(dict_info['following'])
    #get public repo number
    repo_num = int(dict_info['public_repos'])
    #get public gist number
    gist_num = int(dict_info['public_gists'])
    #location
    location = dict_info['location']
    #company
    company = dict_info['company']

    return userid, user_type, github_age, followers_num, following_num, repo_num, gist_num, location, company


def get_all_details(user_input,gh):
    '''
    input user_input(list): a list of github username (list)
          gh(class): github3 api object to fetch github user details
    output user_details_list(list): a list of github user user detail inform
    '''
    user_details_list = []
    for userid in user_input:
        try:
            userid, user_type, github_age, followers_num, following_num, repo_num, gist_num, location, company = get_user_details(gh, userid)
            user_details_list.append([userid, user_type, github_age, followers_num, following_num, repo_num, gist_num, location, company])
        except:
            #skip the users who no longer has this github account
            print('{} not found'.format(userid))
    return user_details_list


def save_to_dataframe(user_details_list):
    '''
    input user_details_list(list): a list of user detail list as ['user_id', 'user_rank', 'user_type', 'githubage', 'user_followers',
       'user_following', 'repo_num', 'gist_num', 'location', 'company']
    output: dataframe(pandas dataframe) : clean data in pandas dataframe format
    '''
    username_list = []
    userrank_list = []
    usertype_list = []
    githubage_list = []
    userfollowers_list = []
    userfollowing_list = []
    reponum_list = []
    gist_num_list = []
    location_list = []
    company_list = []
    count = 0
    for user_detail in user_details_list:
        username_list.append(user_detail[0])
        userrank_list.append(count + 1)
        usertype_list.append(user_detail[1])
        githubage_list.append(user_detail[2])
        userfollowers_list.append(user_detail[3])
        userfollowing_list.append(user_detail[4])
        reponum_list.append(user_detail[5])
        gist_num_list.append(user_detail[6])
        location_list.append(user_detail[7])
        company_list.append(user_detail[8])
        count = count+1

        user_data = {
            'user_id' :username_list,
            'user_rank' : userrank_list,
            'user_type': usertype_list,
            'githubage' : githubage_list,
            'user_followers': userfollowers_list,
            'user_following': userfollowing_list,
            'repo_num' : reponum_list,
            'gist_num': gist_num_list,
            'location': location_list,
            'company':company_list
            }
            dataframe = pd.DataFrame(user_data)
    return dataframe




#CHANGE BELOW
inputfile_location = 'location of input language_userrank files '
outputfile_location = 'location of output userdetail_language files '
#the github login object for github3.py api
gh = login('your github username', password='your github password')
#default value of top users to enrich user info
topN = 50
#CHANGE ABOVE

if __name__ == "__main__":
    #list of 11 languages we analysis
    inputfile_names = ['C','Cplus','Csharp','Go','Java','JavaScript','Perl','Python','Ruby','Shell', 'Scala']
    #loop over and send into the github3 api for user info enrichment
    for inputfile_name in inputfile_names:
        #construct the fullpath of inputfiles and outputfiles folder
        inputfile_fullpath  = inputfile_location + inputfile_name + '.csv'
        outputfile_fullpath =  outputfile_location +'userdetail_' + inputfile_name + '.csv'
        #readin the user_rank csv
        df = pd.read_csv(inputfile_fullpath, usecols=['user','rank'])
        #sort dataframe by the pagerank values
        df_sorted = df.sort_values(by=['rank'], ascending = False)
        #grab the top N user based on pagerank score
        user_input = df_sorted.user.tolist()[:topN]
        #get a list of user details by github3 api
        user_details_list = get_all_details(user_input, gh )
        #save the user info list to pandas dataframe
        dataframe = save_to_dataframe(user_details_list)
        #construct the filter to filter out no user
        is_user = dfObj['user_type'] == 'User'
        #filter out pagerank 0 following trap
        has_following = dfObj['user_following'] != 0
        #filter users who has more than 300 followers
        large_follow = dfObj['user_followers'] > 300
        #final df output
        df_final = dfObj[is_user & has_following & large_follow]
        #save final csv output to the pull path
        df_final.to_csv(outputfile_fullpath)
