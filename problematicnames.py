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

COUNTER = 0

def divnamesCriterion(listofnames):
    if len(listofnames) == 0:
        return ""
    if len(listofnames) == 1:
        return listofnames[0]
    return max(listofnames)

def check_approval_sentence(text):
    if "approves" in text or "Approval" in text or "approve" in text or "approval" in text or "granted" in text or "distributed" in text or "marketed" in text or "manufactured" in text or "made" in text or "developed" in text:
        return True
    return False

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
        lastname = pharmanames[i].split()
        if lastname[len(lastname)-1] == "CO":
            lastname[len(lastname)-1] = "Corporation"
        if lastname[len(lastname)-1] == "LTD":
            lastname[len(lastname)-1] = "Limited"
        if lastname[len(lastname)-1] == "PHARMA":
            lastname[len(lastname)-1] = "Pharmaceuticals"
        lastname = " ".join(lastname)
        if lastname.upper() in text.upper():
            return pharmanames[i]
    return "Not Found"

def extract_data(df,url):
    global COUNTER
    # get text
    temppage = requests.get(url)
    soup = BeautifulSoup(temppage.content,'lxml')
    text = soup.find_all('p')
    text_copy = text
    approvalsentence = ""

    for i in range(0,len(text_copy)):
        if check_approval_sentence(text_copy[i].get_text()):
            approvalsentence = text_copy[i].get_text()
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

    COUNTER += 1
    print("Count is " + str(COUNTER))
    print("My pharmacy name is " + pharmaname)
    print("URL is " + url)

data = pd.read_excel("listofpharmacies.xls")
df = data['Pharmacy Name'].values.tolist()
data = pd.read_excel("problematicpharmanames.xlsx")
df2 = data['URL'].values.tolist()
for i in range(0, len(df2)):
    extract_data(df,df2[i])
