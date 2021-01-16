from .models import *

personalityArtist = [
    ["아이유", "박혜원", "스탠딩에그", "장덕철", "이하이",
        "허각", "거미", "백예린", "임영웅", "벤",
        "폴킴", "양다일", "기리보이", "악동뮤지션", "폴킴",
        "볼빨간사춘기", "백지영", "청하", "크러쉬", "케이윌",
        "먼데이키즈", "김필", "박진영", "바이브", "창모",
        "지코", "제니", "에픽하이", "다비치", "윤하",
        "임창정", "레드벨벳", "에이핑크", "제시", "선미",
        "박봄", "노을", "마크툽", "오마이걸", "엠씨더맥스",
        "태연", "박효신"],
    ["엔플라잉", "악동뮤지션", "케이윌", "스탠딩에그", "백예린",
        "벤", "이하이", "하현우", "허각", "엑소",
        "폴킴", "볼빨간사춘기", "백지영", "청하", "크러쉬",
        "헤이즈", "먼데이키즈", "김필", "박진영", "바이브",
        "에픽하이", "방탄소년단", "트와이스", "제니", "잔나비",
        "박혜원", "노을", "엠씨더맥스", "박효신", "아이유",
        "임영웅", "장덕철", "양다일", "기리보이", "펀치",
        "거미", "오마이걸", "다비치", "마마무", "윤하",
        "임창정", "블랙핑크", "있지", "에이핑크", "아이즈원",
        "트와이스", "청하", "송민호", "마크툽", "태연"],
    ["아이유", "백지영", "장덕철", "이하이", "백예린",
        "박혜원", "스탠딩에그", "임영웅", "벤", "양다일",
        "기리보이", "악동뮤지션", "폴킴", "볼빨간사춘기", "청하",
        "크러쉬", "케이윌", "헤이즈", "창모", "지코",
        "제니", "에픽하이", "장범준", "잔나비", "김필",
        "규현", "바이브", "임창정", "10cm", "레드벨벳",
        "에이핑크", "제시", "선미", "박봄", "노을",
        "마크툽", "오마이걸", "엠씨더맥스", "거미", "태연",
        "허각", "박효신"],
    ["아이유", "거미", "박혜원", "장덕철", "스탠딩에그",
        "임영웅", "벤", "양다일", "기리보이", "다비치",
        "윤하", "임창정", "백예린", "하현우", "엔플라잉",
        "에픽하이", "레드벨벳", "에이핑크", "제시", "선미",
        "박봄", "노을", "마크툽", "오마이걸", "엠씨더맥스",
        "태연", "허각", "박효신", "이하이"],
    ["스탠딩에그", "허각", "장덕철", "이하이", "벤",
        "양다일", "기리보이", "아이유", "백예린", "박혜원",
        "악동뮤지션", "폴킴", "볼빨간사춘기", "백지영", "청하",
        "크러쉬", "케이윌", "헤이즈", "임영웅", "먼데이키즈",
        "김필", "박진영", "바이브", "하현우", "엔플라잉",
        "에픽하이", "노을", "마크툽", "오마이걸", "엠씨더맥스",
        "거미", "태연", "박효신"],
    ["마마무", "(여자)아이들", "김필", "바이브", "악동뮤지션",
        "폴킴", "볼빨간사춘기", "백지영", "청하", "크러쉬",
        "케이윌", "헤이즈", "이하이", "스탠딩에그", "먼데이키즈",
        "박진영", "허각", "장범준", "백지영", "잔나비",
        "규현", "임창정", "10cm", "아이유", "레드벨벳",
        "에이핑크", "제시", "선미", "박봄"],
    ["백지영", "크러쉬", "헤이즈", "이하이", "기리보이",
        "장덕철", "폴킴", "임영웅", "규현", "양다일",
        "엑소", "방탄소년단", "오마이걸", "블랙핑크", "악동뮤지션",
        "볼빨간사춘기", "청하", "케이윌", "창모", "지코",
        "송민호", "레드벨벳", "제시", "아이유", "백예린",
        "박혜원", "스탠딩에그", "벤", "마마무", "있지",
        "에이핑크", "아이즈원", "트와이스", "청하", "송민호",
        "노을", "마크툽", "엠씨더맥스", "거미", "태연",
        "허각", "박효신", "다비치", "송하예", "윤하",
        "멜로망스", "트와이스", "제니", "태연", "선미"],
    ["하현우", "엔플라잉", "에픽하이", "스탠딩에그", "먼데이키즈",
        "김필", "박진영", "바이브", "허각"],
    ["하현우", "장범준", "마크툽", "볼빨간사춘기", "송하예",
        "멜로망스", "펀치", "10cm", "엔플라잉", "에픽하이"],
    ["방탄소년단", "태연", "선미", "창모", "지코",
        "크러쉬", "송민호", "헤이즈", "기리보이", "마마무",
        "(여자)아이들", "장범준", "백지영", "잔나비", "김필",
        "규현", "바이브", "임창정", "10cm", "아이유",
        "레드벨벳", "에이핑크", "제시", "선미", "박봄"],
    ["하현우", "엔플라잉", "에픽하이"],
    ["마마무", "오마이걸", "블랙핑크", "있지", "에이핑크",
        "아이즈원", "트와이스", "청하", "송민호", "엑소",
        "장범준", "마크툽", "볼빨간사춘기", "송하예", "멜로망스",
        "펀치", "10cm"],
    ["아이유", "레드벨벳", "에이핑크", "제시", "선미",
        "박봄"],
    ["엔플라잉", "펀치", "송하예", "멜로망스", "하현우",
        "에픽하이", "폴킴", "다비치", "임영웅", "규현",
        "윤하", "양다일", "노을", "악동뮤지션", "백예린",
        "엠씨더맥스", "벤", "케이윌", "박효신", "잔나비",
        "창모", "지코", "크러쉬", "송민호", "헤이즈",
        "기리보이", "레드벨벳", "블랙핑크", "제시", "장범준",
        "마크툽", "볼빨간사춘기", "10cm"],
    ["노을", "악동뮤지션", "백예린", "엠씨더맥스", "벤",
        "케이윌", "박효신", "펀치", "스탠딩에그", "먼데이키즈",
        "김필", "박진영", "바이브", "허각"],
    ["임영웅", "규현", "양다일", "방탄소년단", "장덕철",
        "폴킴", "다비치", "송하예", "윤하", "멜로망스",
        "트와이스", "제니", "엑소", "태연", "선미",
        "아이유", "백예린", "잔나비", "김필", "바이브",
        "임창정", "10cm", "노을", "마크툽", "오마이걸",
        "엠씨더맥스", "거미", "태연", "허각", "박효신",
        "이하이"]
]



highSelfEsteem = 0
ideal = 0
active = 0
patient = 0
comfortable = 0
hardworking = 0
extrovert = 0
realistic = 0



def estimateArtist():
    global personalityArtist
    
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    personalityList = [highSelfEsteem, ideal, active, patient, comfortable, hardworking, extrovert, realistic, -highSelfEsteem, -ideal, -active, -patient, -comfortable, -hardworking, -extrovert, -realistic]

    firstPersonality = personalityList.index(max(personalityList))
    personalityList[firstPersonality] = -999
    secondPersonality = personalityList.index(max(personalityList))
    personalityList[secondPersonality] = -999
    thirdPersonality = personalityList.index(max(personalityList))
    personalityList[thirdPersonality] = -999

    personalitySet = set(personalityArtist[firstPersonality]) & set(personalityArtist[secondPersonality]) & set(personalityArtist[thirdPersonality])
    result = list(personalitySet)

    if len(result) != 0:
        return result

    return ["iu"]

def questionCalc():
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()

def question1():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_1 = Answer.objects.filter(question_number = 1)[0].answer
    if answer_1 == 1:
        highSelfEsteem -= 3
        ideal += 2
        active -= 1
        patient += 1
        comfortable -= 1
        hardworking += 0
        extrovert -= 3
        realistic -= 1
    elif answer_1 == 2:
        highSelfEsteem -= 2
        ideal += 2
        active += 0
        patient += 1
        comfortable -= 1
        hardworking += 0
        extrovert -= 2
        realistic -= 1
    elif answer_1 == 3:
        highSelfEsteem += 0
        ideal += 1
        active += 0
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert -= 1
        realistic += 0
    elif answer_1 == 4:
        highSelfEsteem += 2
        ideal += 0
        active += 1
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 0
        realistic += 1
    elif answer_1 == 5:
        highSelfEsteem += 4
        ideal -= 1
        active += 2
        patient -= 2
        comfortable += 0
        hardworking += 0
        extrovert += 2
        realistic += 2

def question2():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_2 = Answer.objects.filter(question_number = 2)[0].answer
    if answer_2 == 1:
        highSelfEsteem += 0
        ideal -= 5
        active += 3
        patient -= 1
        comfortable += 3
        hardworking += 0
        extrovert += 2
        realistic += 3
    elif answer_2 == 2:
        highSelfEsteem += 0
        ideal -= 3
        active += 3
        patient += 0
        comfortable += 2
        hardworking += 0
        extrovert += 2
        realistic += 3
    elif answer_2 == 3:
        highSelfEsteem += 0
        ideal += 0
        active += 1
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 0
        realistic += 0
    elif answer_2 == 4:
        highSelfEsteem += 1
        ideal += 2
        active += 0
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 0
        realistic += 0
    elif answer_2 == 5:
        highSelfEsteem += 2
        ideal += 3
        active -= 2
        patient += 1
        comfortable += 0
        hardworking += 1
        extrovert -= 1
        realistic -= 2

def question3():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_3 = Answer.objects.filter(question_number = 3)[0].answer
    if answer_3 == 1:
        highSelfEsteem += 5
        ideal += 5
        active += 3
        patient -= 3
        comfortable -= 3
        hardworking -= 1
        extrovert += 2
        realistic -= 3
    elif answer_3 == 2:
        highSelfEsteem += 3
        ideal += 4
        active += 2
        patient -= 1
        comfortable -= 2
        hardworking -= 1
        extrovert += 2
        realistic -= 2
    elif answer_3 == 3:
        highSelfEsteem += 1
        ideal += 2
        active += 1
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 0
        realistic += 0
    elif answer_3 == 4:
        highSelfEsteem += 0
        ideal += 0
        active += 0
        patient += 1
        comfortable += 1
        hardworking += 1
        extrovert += 0
        realistic += 1
    elif answer_3 == 5:
        highSelfEsteem -= 2
        ideal -= 2
        active -= 2
        patient += 2
        comfortable += 2
        hardworking += 1
        extrovert -= 1
        realistic += 4

def question4():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_4 = Answer.objects.filter(question_number = 4)[0].answer
    if answer_4 == 1:
        highSelfEsteem += -2
        ideal += 3
        active += -4
        patient += 3
        comfortable += 4
        hardworking += 2
        extrovert += -5
        realistic += 0
    elif answer_4 == 2:
        highSelfEsteem += -1
        ideal += 3
        active += -2
        patient += 1
        comfortable += 2
        hardworking += 1
        extrovert += -3
        realistic += 0
    elif answer_4 == 3:
        highSelfEsteem += 1
        ideal += 1
        active += 1
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 1
        realistic += 0
    elif answer_4 == 4:
        highSelfEsteem += 3
        ideal += 0
        active += 3
        patient += -1
        comfortable += 0
        hardworking += 0
        extrovert += 4
        realistic += 1
    elif answer_4 == 5:
        highSelfEsteem += 5
        ideal += -2
        active += 5
        patient += -2
        comfortable += -2
        hardworking += 0
        extrovert += 5
        realistic += 2

def question5():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_5 = Answer.objects.filter(question_number = 5)[0].answer
    if answer_5 == 1:
        highSelfEsteem += -2
        ideal += 3
        active += -4
        patient += 4
        comfortable += 4
        hardworking += 2
        extrovert += -3
        realistic += 5
    elif answer_5 == 2:
        highSelfEsteem += -1
        ideal += 3
        active += -2
        patient += 2
        comfortable += 2
        hardworking += 1
        extrovert += -2
        realistic += 3
    elif answer_5 == 3:
        highSelfEsteem += 1
        ideal += 1
        active += 1
        patient += -1
        comfortable += 0
        hardworking += 0
        extrovert += 1
        realistic += 0
    elif answer_5 == 4:
        highSelfEsteem += 3
        ideal += 0
        active += 3
        patient += -3
        comfortable += -2
        hardworking += 0
        extrovert += 2
        realistic += -2
    elif answer_5 == 5:
        highSelfEsteem += 5
        ideal += -2
        active += 5
        patient += -5
        comfortable += -4
        hardworking += 0
        extrovert += 3
        realistic += -3

def question6():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_6 = Answer.objects.filter(question_number = 6)[0].answer
    if answer_6 == 1:
        highSelfEsteem += -4
        ideal += -3
        active += -4
        patient += -3
        comfortable += -5
        hardworking += 3
        extrovert += -2
        realistic += -3
    elif answer_6 == 2:
        highSelfEsteem += -3
        ideal += -2
        active += -3
        patient += -2
        comfortable += -4
        hardworking += 3
        extrovert += -1
        realistic += -2
    elif answer_6 == 3:
        highSelfEsteem += -1
        ideal += -1
        active += -1
        patient += 0
        comfortable += -2
        hardworking += 1
        extrovert += 0
        realistic += 0
    elif answer_6 == 4:
        highSelfEsteem += 3
        ideal += 0
        active += 1
        patient += 1
        comfortable += 2
        hardworking += 0
        extrovert += 1
        realistic += 1
    elif answer_6 == 5:
        highSelfEsteem += 5
        ideal += 0
        active += 3
        patient += 2
        comfortable += 5
        hardworking += 0
        extrovert += 2
        realistic += 4

def question7():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_7 = Answer.objects.filter(question_number = 7)[0].answer
    if answer_7 == 1:
        highSelfEsteem += -1
        ideal += -3
        active += -4
        patient += 3
        comfortable += 5
        hardworking += -4
        extrovert += -3
        realistic += -3
    elif answer_7 == 2:
        highSelfEsteem += 0
        ideal += -2
        active += -3
        patient += 2
        comfortable += 4
        hardworking += -3
        extrovert += -1
        realistic += -1
    elif answer_7 == 3:
        highSelfEsteem += 0
        ideal += 0
        active += -1
        patient += 0
        comfortable += 1
        hardworking += -1
        extrovert += 0
        realistic += 0
    elif answer_7 == 4:
        highSelfEsteem += 1
        ideal += 0
        active += 1
        patient += 0
        comfortable += 0
        hardworking += 2
        extrovert += 0
        realistic += 2
    elif answer_7 == 5:
        highSelfEsteem += 2
        ideal += 1
        active += 2
        patient += -1
        comfortable += -2
        hardworking += 4
        extrovert += 2
        realistic += 2

def question8():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_8 = Answer.objects.filter(question_number = 8)[0].answer
    if answer_8 == 1:
        highSelfEsteem += -2
        ideal += 3
        active += -5
        patient += 1
        comfortable += 5
        hardworking += 4
        extrovert += -4
        realistic += -1
    elif answer_8 == 2:
        highSelfEsteem += 0
        ideal += 2
        active += -4
        patient += 1
        comfortable += 3
        hardworking += 3
        extrovert += -2
        realistic += -1
    elif answer_8 == 3:
        highSelfEsteem += 0
        ideal += 1
        active += -1
        patient += 0
        comfortable += 1
        hardworking += 1
        extrovert += 0
        realistic += 1
    elif answer_8 == 4:
        highSelfEsteem += 0
        ideal += 0
        active += 3
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 1
        realistic += 2
    elif answer_8 == 5:
        highSelfEsteem += 1
        ideal += -2
        active += 5
        patient += -2
        comfortable += -3
        hardworking += -1
        extrovert += 4
        realistic += 3

def question9():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_9 = Answer.objects.filter(question_number = 9)[0].answer
    if answer_9 == 1:
        highSelfEsteem += -2
        ideal += 5
        active += 1
        patient += 2
        comfortable += 4
        hardworking += 3
        extrovert += -5
        realistic += -3
    elif answer_9 == 2:
        highSelfEsteem += -1
        ideal += 4
        active += 1
        patient += 1
        comfortable += 4
        hardworking += 2
        extrovert += -2
        realistic += -1
    elif answer_9 == 3:
        highSelfEsteem += 0
        ideal += 1
        active += 0
        patient += 1
        comfortable += 1
        hardworking += 1
        extrovert += 0
        realistic += 0
    elif answer_9 == 4:
        highSelfEsteem += 0
        ideal += 0
        active += 0
        patient += 0
        comfortable += 0
        hardworking += 0
        extrovert += 1
        realistic += 0
    elif answer_9 == 5:
        highSelfEsteem += 0
        ideal += -4
        active += -1
        patient += -1
        comfortable += -2
        hardworking += -2
        extrovert += 3
        realistic += 2

def question10():
    global highSelfEsteem
    global ideal
    global active
    global patient
    global comfortable
    global hardworking
    global extrovert
    global realistic
    answer_10 = Answer.objects.filter(question_number = 10)[0].answer
    if answer_10 == 1:
        highSelfEsteem += 5
        ideal += -4
        active += -3
        patient += 3
        comfortable += -2
        hardworking += 4
        extrovert += 0
        realistic += 5
    elif answer_10 == 2:
        highSelfEsteem += 3
        ideal += -2
        active += -1
        patient += 1
        comfortable += -2
        hardworking += 2
        extrovert += 0
        realistic += 4
    elif answer_10 == 3:
        highSelfEsteem += 1
        ideal += 0
        active += 0
        patient += 0
        comfortable += 1
        hardworking += 1
        extrovert += 0
        realistic += 2
    elif answer_10 == 4:
        highSelfEsteem += 0
        ideal += 2
        active += 1
        patient += -1
        comfortable += 2
        hardworking += 0
        extrovert += 0
        realistic += -1
    elif answer_10 == 5:
        highSelfEsteem += 0
        ideal += 4
        active += 2
        patient += -2
        comfortable += 2
        hardworking += -1
        extrovert += 0
        realistic += -3