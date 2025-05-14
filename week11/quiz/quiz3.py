domain = {
    "대한민국": "kr",
    "미국": "us",
    "일본": "jp",
    "독일": "de",
    "슬로바키아": "sk",
    "헝가리": "hu",
    "노르웨이": "no"
}

country = input("국가명을 입력하시오: ")

if country in domain:
    print(f"{country}의 도메인은 {domain[country]}입니다.")
else:
    print("해당 국가의 도메인 정보는 제공되지 않습니다.")
