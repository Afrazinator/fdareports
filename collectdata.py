import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import nltk
from urllib.parse import urljoin
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import xlwt
import pandas as pd
from xlwt import Workbook


def divnamesCriterion(listofnames):
    if len(listofnames) == 0:
        return ""
    if len(listofnames) == 1:
        return listofnames[0]
    return max(listofnames)

def findPharmaNamedivs(pharmanames,text):
    ##This Usually returns a lot of names##
    listofnames = []
    for i in range(0, len(pharmanames)):
        if pharmanames[i].upper() in text.upper():
            listofnames.append(pharmanames[i])
    return listofnames

def findPharmaName(pharmanames, text):
    for i in range(0, len(pharmanames)):
        if pharmanames[i].upper() in text.upper():
            return pharmanames[i]
    return ""

def findPharmaNamebyfirstname(pharmanames,text):
    for i in range(0,len(pharmanames)):
        firstname = pharmanames[i].split(' ')
        firstname = firstname[0]
        if firstname.upper() in text.upper():
             return pharmanames[i]
    return "Not Found"
def extract_pharmaname_archived(drugname, text,approvalsentence):
    #------------Finding the name of the pharmaceutical from the text-------------
        if drugnameLong == True:
            drugstringCondition = drugstringCondition = 'The FDA granted approval of ' + drugname + ' to '
        else:
            drugstringCondition = 'The FDA granted approval of ' + ' '.join(drugname) + ' to '
        #print(drugname)
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
        try:
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
        except:
            pharmaname = [" "]
        #-------Exception handling when drug name not found----------
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = ' approval of ' + drugname + ' was granted to '
            else:
                drugstringCondition = ' approval of ' + ' '.join(drugname) + ' was granted to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'The FDA granted the approval of ' + drugname + ' to '
            else:
                drugstringCondition = 'The FDA granted the approval of ' + ' '.join(drugname) + ' to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'The FDA granted Priority Review of ' + drugname + ' to '
            else:
                drugstringCondition = 'The FDA granted Priority Review of ' + ' '.join(drugname) + ' to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = ' the approved generic version of ' + drugname + ' is '
            else:
                drugstringCondition = ' the approved generic version of ' + ' '.join(drugname) + ' is '
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = ' FDA granted approvals of ' + drugname + ' to '
            else:
                drugstringCondition = ' FDA granted approvals of ' + ' '.join(drugname) + ' to '
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'The sponsor of the approved generic version of ' + drugname + ' is '
            else:
                drugstringCondition = 'The sponsor of the approved generic version of ' + ' '.join(drugname) + ' is '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'Approval of ' + drugname + ' was granted to '
            else:
                drugstringCondition = 'Approval of ' + ' '.join(drugname) + ' was granted to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'Approval of ' + drugname + ' were granted to '
            else:
                drugstringCondition = 'Approval of ' + ' '.join(drugname) + ' were granted to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = ' approval of ' + drugname + ' was granted to '
            else:
                drugstringCondition = ' approval of ' + ' '.join(drugname) + ' was granted to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
            if pharmaname == []:
                if drugnameLong == True:
                    drugstringCondition = ' approval of the ' + drugname + ' was granted to '
                else:
                    drugstringCondition = ' approval of the ' + ' '.join(drugname) + ' was granted to '
                regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
                pharmanameCriterion = re.compile(regexCondition,re.M)
                pharmaname = pharmanameCriterion.findall(text)
                if len(pharmaname) > 1:
                    pharmaname = pharmanameCriterion.findall(approvalsentence)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'Approvals of ' + drugname + ' were granted to '
            else:
                drugstringCondition = 'Approvals of ' + ' '.join(drugname) + ' were granted to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
        if pharmaname == []:
            regexCondition = r'(?<=\.)(.*?)(?= holds the application )'
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
        #--------This code is exhaustive for multiple pharmaceuticals on the same drug---------
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'The FDA granted approvals for the generic versions of ' + drugname + ' to '
            else:
                drugstringCondition = 'The FDA granted approvals for the generic versions of ' + ' '.join(drugname) + ' to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\n|$)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = 'The FDA granted approvals for the ' + drugname + ' to '
            else:
                drugstringCondition = 'The FDA granted approvals for the ' + ' '.join(drugname) + ' to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\n|$)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)

def extract_drugname(text):
    #this code will definitely find the drug name, you need more control over sentence
    drugdiscoveryCriterion = re.compile(r'(?<=The FDA granted approval of )(.*?)(?= was | to )',re.M)
    drugname = drugdiscoveryCriterion.findall(text)

    #---Exception handling when drug name not found------
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<= the approval of )(.*?)(?= was | to )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<= granted Priority Review of )(.*?)(?= was | to )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<=The approval of )(.*?)(?= was | to )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<=Approval of )(.*?)(?= was | were | to )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<= holds the application for )(.*?)(?=\.)',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<= approved generic version of )(.*?)(?= is )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<= approvals for the generic version of )(.*?)(?= to )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        print(text)
        drugdiscoveryCriterion = re.compile(r'(?<= approvals of )(.*?)(?= to | were )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
        print(drugname)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<= approvals for the )(.*?)(?= to | were | \. )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r'(?<=The sponsor of the approved generic version of )(.*?)(?= is )',re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r"(?<= approval of the )(.*?)(?= was )",re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    if drugname == []:
        drugdiscoveryCriterion = re.compile(r"(?<= granted )(.*?)(?= to )",re.M)
        drugname = drugdiscoveryCriterion.findall(text)
    return drugname

def pharmanamebyRegex(text):
    #-------Exception handling when drug name not found----------
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = ' approval of ' + drugname + ' was granted to '
        else:
            drugstringCondition = ' approval of ' + ' '.join(drugname) + ' was granted to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'The FDA granted the approval of ' + drugname + ' to '
        else:
            drugstringCondition = 'The FDA granted the approval of ' + ' '.join(drugname) + ' to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'The FDA granted Priority Review of ' + drugname + ' to '
        else:
            drugstringCondition = 'The FDA granted Priority Review of ' + ' '.join(drugname) + ' to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = ' the approved generic version of ' + drugname + ' is '
        else:
            drugstringCondition = ' the approved generic version of ' + ' '.join(drugname) + ' is '
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = ' FDA granted approvals of ' + drugname + ' to '
        else:
            drugstringCondition = ' FDA granted approvals of ' + ' '.join(drugname) + ' to '
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'The sponsor of the approved generic version of ' + drugname + ' is '
        else:
            drugstringCondition = 'The sponsor of the approved generic version of ' + ' '.join(drugname) + ' is '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'Approval of ' + drugname + ' was granted to '
        else:
            drugstringCondition = 'Approval of ' + ' '.join(drugname) + ' was granted to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'Approval of ' + drugname + ' were granted to '
        else:
            drugstringCondition = 'Approval of ' + ' '.join(drugname) + ' were granted to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = ' approval of ' + drugname + ' was granted to '
        else:
            drugstringCondition = ' approval of ' + ' '.join(drugname) + ' was granted to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)
        if pharmaname == []:
            if drugnameLong == True:
                drugstringCondition = ' approval of the ' + drugname + ' was granted to '
            else:
                drugstringCondition = ' approval of the ' + ' '.join(drugname) + ' was granted to '
            regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
            pharmanameCriterion = re.compile(regexCondition,re.M)
            pharmaname = pharmanameCriterion.findall(text)
            if len(pharmaname) > 1:
                pharmaname = pharmanameCriterion.findall(approvalsentence)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'Approvals of ' + drugname + ' were granted to '
        else:
            drugstringCondition = 'Approvals of ' + ' '.join(drugname) + ' were granted to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=,|\.)'
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)
    if pharmaname == []:
        regexCondition = r'(?<=\.)(.*?)(?= holds the application )'
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)
    #--------This code is exhaustive for multiple pharmaceuticals on the same drug---------
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'The FDA granted approvals for the generic versions of ' + drugname + ' to '
        else:
            drugstringCondition = 'The FDA granted approvals for the generic versions of ' + ' '.join(drugname) + ' to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\n|$)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)
    if pharmaname == []:
        if drugnameLong == True:
            drugstringCondition = 'The FDA granted approvals for the ' + drugname + ' to '
        else:
            drugstringCondition = 'The FDA granted approvals for the ' + ' '.join(drugname) + ' to '
        regexCondition = r'(?<='+drugstringCondition+')(.*?)(?=\n|$)'
        pharmanameCriterion = re.compile(regexCondition,re.M)
        pharmaname = pharmanameCriterion.findall(text)
        if len(pharmaname) > 1:
            pharmaname = pharmanameCriterion.findall(approvalsentence)

def check_approval_sentence(text):
    if "approves" in text or "Approval" in text or "approve" in text or "approval" in text or "granted" in text or "distributed" in text or "marketed" in text or "manufactured" in text or "made" in text or "developed" in text:
        return True
    return False

def check_priority_review(text):
    if "Priority Review" in text:
        return True
    return False

def check_side_effects_sentence(text):
    if "side effects" in text or "adverse effects" in text or "Side effects" in text or "Adverse effects" in text or "adverse reactions" in text or "Adverse reactions" in text or "risk" in text or "adverse drug reactions" in text or "Adverse drug reactions" in text:
        return True
    return False

def lexicon_analysis(text):
    word_weight_dictionary = {"constipation": 2, "rash": 2,"anaemia": 3, "diarrhea":2, "dizziness": 2, "drowsiness":2, "headache": 2, "insomnia": 2,"nausea": 2, "vomiting": 2, "fatigue" : 2, "sleeping": 2,"pain": 4, "fever": 5,"hyperphosphatemia": 3,"hypophosphatemia": 3,"hepatotoxicity": 10, "suicidal": 10,"harm": 4, "death": 100 }
    stop_words=set(stopwords.words("english"))
    tokenized_word = word_tokenize(text)
    filtered_sent=[]
    for w in tokenized_word:
        if w not in stop_words and w.isalnum():
            filtered_sent.append(w)
    fdist = FreqDist(filtered_sent)
    word_list = fdist.most_common(600)
    dangerous = 0 #score of side effects
    for i in range(0,len(word_list)):
        for key,value in word_weight_dictionary.items():
            if word_list[i][0].lower() == key:
                dangerous += word_list[i][1]*value
    return dangerous

def clean_text(text):
    blankstr = ""
    for i in range(3,len(text)-2):
        blankstr += text[i].get_text()
    return blankstr

def clean_pharmaname(pharmaname):
    if len(pharmaname) > 1:
        pharmaname = pharmaname[len(pharmaname)-1]
    else:
        pharmanme = " ".join(pharmaname)
    return pharmaname

def check_drug_name(drugname):
    drugnameLong = False
    if len(drugname) > 1:
        drugnameLong = True
        drugname = drugname[len(drugname)-1]
    return drugname, drugnameLong

def extract_text_archived(soup, url,excel_data_pointer, workbook):
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.find_all('p')
    text_copy = text

    #----------------Lexicon Analysis------------------
    priorityReview = False
    dangerous = 0
    approvalsentence = ""
    for i in range(0,len(text_copy)):
        if check_side_effects_sentence(text_copy[i].get_text()):
            dangerous += lexicon_analysis(text_copy[i].get_text())
        if check_approval_sentence(text_copy[i].get_text()):
            approvalsentence = text_copy[i].get_text()
        if priorityReview == False:
            priorityReview = check_priority_review(text_copy[i].get_text())

    #find the date:
    date = ""
    try:
        date = soup.find("div", {"class": "release-date"}).find("div", {"class": "col-md-9"}).get_text()
    except:
        date_search = soup.find_all('strong')
        for i in range(0,len(date_search)):
            if date_search[i] == "<strong>For Immediate Release:</strong>" or date_search[i] == "<strong>For Immediate Release: </strong>":
                date = date_search[i].get_text()


    #-----Exception handling for the 2013-2014 data-------
    if date == "":
        #Clean out </br> tags
        for br in soup.find_all('br'):
            br.extract()
        try:
            date_search = soup.find_all("b")
            print(date_search)
            for i in range(0,len(date_search)):
                if date_search[i] == "<b>For Immediate Release:</b>" or date_search[i] == "<b>For Immediate Release: </b>":
                    date = date_search[i].get_text()
        except:
            pass
        try:
            date_search = soup.find_all("div")
            print("This is what happens when you get text" + date_search[i].get_text())
            for i in range(0,len(date_search)):
                if date_search[i] == "<b>For Immediate Release:</b>" or date_search[i] == "<b>For Immediate Release: </b>":
                    date = date_search[i].next_sibling



            if date == "":
                date_search = soup.find_all("div").find_all("strong")
                for i in range(0,len(date_search)):
                    if date_search[i] == "<strong>For Immediate Release:</strong>" or date_search[i] == "<strong>For Immediate Release: </strong>":
                        date = date_search[i].get_text()

        except:
            pass
    if str(date) == "\r\n\t\t\t\t\t\t10903 New Hampshire Avenue":
        date = ""
    if date == "":
        try:
            date_search = soup.find('strong')
            date = date_search.next_sibling
        except:
            pass
    if date == "":
        try:
            date_search = soup.find("div", {"class": "main"}).find_all("div")
            date_search = str(date_search)
            date_writtenCriterion = re.compile(r'(?<=<div>For Immediate Release: )(.*?)(?=</div>)',re.M)
            date = date_writtenCriterion.findall(date_search)
            date = date[0]
            date = str(date)
        except:
            date_search = ""

    if date == "":
        print(date_search)

    print("The date is " + str(date))
    text_copy = text
    print("The length of text copy is " + str(len(text_copy)))
    print("The formatted date is " + repr(str(date)))
    text = clean_text(text)

    #----------------Lexicon Analysis------------------
    dangerous = 0
    priorityReview = False
    for i in range(0,len(text_copy)):
        if check_side_effects_sentence(text_copy[i].get_text()):
            print(text_copy[i].get_text())
            dangerous += lexicon_analysis(text_copy[i].get_text())
            if priorityReview == False:
                priorityReview = check_priority_review(text_copy[i].get_text())

    print("priority review is " + str(priorityReview))

    drugname = extract_drugname(approvalsentence)
    #-----If Regex caught more than one sentence always make drugname the last one------
    drugnameLong = False
    drugname, drugnameLong = check_drug_name(drugname)


    #----New Pharmacy Name Idea------
    pharmaname = ""
    pharmaname = findPharmaName(df, approvalsentence)
    #-----If the approval sentence is wrong-----
    if pharmaname == "":
        while(pharmaname == ""):
            for i in range(0, len(text_copy)):
                if check_approval_sentence(text_copy[i].get_text()):
                    approvalsentence = text_copy[i].get_text()
                    pharmaname = findPharmaName(df, approvalsentence)

                    if pharmaname != "":
                        break
            pharmaname = "Not Found"
        for i in range(0, len(text_copy)):
            pharmaname = findPharmaName(df,text_copy[i].get_text())
        if pharmaname == "":
            pharmaname = "Not Found"
    if pharmaname == "Not Found":
        while(pharmaname == "Not Found"):
            for i in range(0, len(text_copy)):
                if check_approval_sentence(text_copy[i].get_text()):
                    approvalsentence = text_copy[i].get_text()
                    pharmaname = findPharmaNamebyfirstname(df, approvalsentence)
                    if pharmaname != "Not Found":
                        break
            pharmaname = "Not Found Again"
    #-----We finally hit a case where it wasn't in the paragraphs and is under div now!------
    if pharmaname == "Not Found Again":
        try:
            text_copy = soup.find_all('div')
        except:
            pass
        for i in range(0,len(text_copy)):
            if check_approval_sentence(text_copy[i].get_text()):
                approvalsentence = text_copy[i].get_text()
        #----New Pharmacy Name Idea------
        pharmaname = ""
        pharmaname = findPharmaNamedivs(df, approvalsentence)
        pharmaname = divnamesCriterion(pharmaname)
        #-----If the approval sentence is wrong-----
        if pharmaname == "":
            while(pharmaname == ""):
                for i in range(0, len(text_copy)):
                    if check_approval_sentence(text_copy[i].get_text()):
                        approvalsentence = text_copy[i].get_text()
                        pharmaname = findPharmaNamedivs(df, approvalsentence)
                        pharmaname = divnamesCriterion(pharmaname)
                        if pharmaname != "":
                            break
                pharmaname = "Not Found"
            for i in range(0, len(text_copy)):
                pharmaname = findPharmaNamedivs(df,text_copy[i].get_text())
                pharmaname = divnamesCriterion(pharmaname)
            if pharmaname == "":
                pharmaname = "Not Found"
        if pharmaname == "Not Found":
            while(pharmaname == "Not Found"):
                for i in range(0, len(text_copy)):
                    if check_approval_sentence(text_copy[i].get_text()):
                        approvalsentence = text_copy[i].get_text()
                        pharmaname = findPharmaNamebyfirstname(df, approvalsentence)
                        if pharmaname != "Not Found":
                            break
                pharmaname = "Not Found Again"
    #-----Debug Print Suite--------
    """
    print("The name of the drug is " + str(drugname))
    print("The name of the pharmacy is " + str(pharmaname))
    print("The date is " + str(date))
    """
    #-------Why certain pharmacy names are not found----------
    """
    if pharmaname == [] and drugname != []:
        print("The length of the whole HTML is: " + str(len(text_copy)))
        print(approvalsentence)
        print("Drugname: " + str(drugname))
        print(pharmanameCriterion)
        print(url)
        """
    #-----Add data to excel-------
    sheet.write(excel_data_pointer,0,pharmaname)
    sheet.write(excel_data_pointer,1,date)
    sheet.write(excel_data_pointer,2,dangerous)
    sheet.write(excel_data_pointer,3,url)
    sheet.write(excel_data_pointer,4,priorityReview)
    workbook.save('FDA.xls')


def extract_text(soup, url,excel_data_pointer, workbook, df):
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.find_all('p')
    #find the date:
    date = text[len(text)-2].get_text()
    text_copy = text

    text = clean_text(text)

    #----------------Lexicon Analysis------------------
    priorityReview = False
    dangerous = 0
    approvalsentence = ""
    for i in range(0,len(text_copy)):
        if check_side_effects_sentence(text_copy[i].get_text()):
            dangerous += lexicon_analysis(text_copy[i].get_text())
        if check_approval_sentence(text_copy[i].get_text()):
            approvalsentence = text_copy[i].get_text()
        if priorityReview == False:
            priorityReview = check_priority_review(text_copy[i].get_text())
    print(dangerous)
    print("priority review is " + str(priorityReview))

    #this code will definitely find the drug name, you need more control over sentence
    drugdiscoveryCriterion = re.compile(r'(?<=The FDA granted approval of )(.*?)(?= was | to )',re.M)
    drugname = drugdiscoveryCriterion.findall(text)

    #---Exception handling when drug name not found------
    drugname = extract_drugname(approvalsentence)


    #-----If Regex caught more than one sentence always make drugname the last one------
    drugnameLong = False
    drugname, drugnameLong = check_drug_name(drugname)
#------------Finding the name of the pharmaceutical from the text-------------

    #------New Logic for Pharmaname--------
    pharmaname = ""
    pharmaname = findPharmaName(df, approvalsentence)
    print("My pharmacy name is " + pharmaname)
    if pharmaname == "":
        print("We are on this index " + str(excel_data_pointer))
    #-----If the approval sentence is wrong-----
    if pharmaname == "":
        while(pharmaname == ""):
            for i in range(0, len(text_copy)):
                if check_approval_sentence(text_copy[i].get_text()):
                    approvalsentence = text_copy[i].get_text()
                    print(approvalsentence)
                    pharmaname = findPharmaName(df, approvalsentence)
                    if pharmaname != "":
                        break
            pharmaname = "Not Found"
    #-----Debug Print Suite--------
    """
    print("The name of the drug is " + str(drugname))
    print("The name of the pharmacy is " + str(pharmaname))
    print("The date is " + str(date))
    """
    #-------Why certain pharmacy names are not found----------
    if pharmaname == [] and drugname != []:
        print("The length of the whole HTML is: " + str(len(text_copy)))
        print(approvalsentence)
        print("Drugname: " + str(drugname))
        print(pharmanameCriterion)
        print(url)

    #-----Add data to excel-------
    sheet.write(excel_data_pointer,0,pharmaname)
    sheet.write(excel_data_pointer,1,date)
    sheet.write(excel_data_pointer,2,dangerous)
    sheet.write(excel_data_pointer,3,url)
    sheet.write(excel_data_pointer,4,priorityReview)
    workbook.save('FDA.xls')

def extract_archive_byURL(url,sheet,excel_data_pointer):
    print(url)
    archivepageURL = "https://wayback.archive-it.org"
    for i in range(1, 5):
        fdapage = requests.get(url+"?Page="+str(i))
        fdapage = fdapage.content
        soup = BeautifulSoup(fdapage,'html5lib')
        urls = soup.find_all('a',href=True)
        for i in range(0, len(urls)):
            if check_approval_sentence(urls[i].get_text()):
                print(urls[i].get_text())
                abs_url = archivepageURL+urls[i].get('href')
                print(abs_url)
                temppage = requests.get(abs_url)
                tempsoup = BeautifulSoup(temppage.content,'lxml')
                extract_text_archived(tempsoup,abs_url,excel_data_pointer,wb)
                excel_data_pointer += 1
                print(excel_data_pointer)

    return excel_data_pointer

#---------------In this portion of the script we will be going over URLS over a certain period------------
#Create Excel File
wb = Workbook()

sheet = wb.add_sheet('FDA Mined Data')

#Create column names
sheet.write(0,0,'Pharmacy Name')
sheet.write(0,1,'Date')
sheet.write(0,2,'Dangerous')
sheet.write(0,3,'URL')
sheet.write(0,4,'Priority Review')

#Gather all the urls
excel_data_pointer = 1

#-----Read the names of all the pharmaceutical companies--------
data = pd.read_excel("listofpharmacies.xls")
df = data['Pharmacy Name'].values.tolist()
print(df)

#----------------This is to gather 2018/2020 data---------------
for i in range(0,69):
    fdapage = requests.get("https://www.fda.gov/news-events/fda-newsroom/press-announcements?page=" + str(i))


    soup = BeautifulSoup(fdapage.content,'lxml')
    urls = set()

    for i in soup.find_all('a',href=re.compile(r'(?<=approves).*')):
        url = i.get('href')
        abs_url = urljoin(fdapage.url, url)
        if urls is not set():
            temppage = requests.get(abs_url)
            tempsoup = BeautifulSoup(temppage.content,'lxml')
            extract_text(tempsoup,abs_url,excel_data_pointer,wb,df)
            urls.add(abs_url)
            excel_data_pointer += 1


#-----TODO: Add a script on 2013-2017 data------------
url_2017 = "https://wayback.archive-it.org/7993/20190422152747/https://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/2017/default.htm"
#This part will extract 2013-2017 data
excel_data_pointer = extract_archive_byURL(url_2017,sheet,excel_data_pointer)
#This part will extract 2013-2016
url_2016 = "https://wayback.archive-it.org/7993/20170111002425/http://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/2016/default.htm"
url_2015 = "https://wayback.archive-it.org/7993/20170111002435/http://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/2015/default.htm"
url_2014 = "https://wayback.archive-it.org/7993/20170111002446/http://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/2014/default.htm"
url_2013 = "https://wayback.archive-it.org/7993/20170111002457/http://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/2013/default.htm"
excel_data_pointer = extract_archive_byURL(url_2016,sheet,excel_data_pointer)
excel_data_pointer = extract_archive_byURL(url_2015,sheet,excel_data_pointer)
excel_data_pointer = extract_archive_byURL(url_2014,sheet,excel_data_pointer)
excel_data_pointer = extract_archive_byURL(url_2013,sheet,excel_data_pointer)
#Extract the text in each URL and build the Text classification tool
