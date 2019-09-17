import os
import operator as op
import random

completed = {"Season": False, "Month": False, "Number": False, "division": True}
math_dict = {"addition": op.add, "subtraction": op.sub, "乘法": op.mul, "division": op.truediv}


# The main function.
def main():
    clear_screen()
    print("親愛的小樂公主殿下 歡迎光臨 : ")
    print("你很厲害嗎?")
    begin_math_stage()
    print("冏!好厲害呀~ 這麼難的題目都難不倒你嗎?")
    if input("再玩一次? 退出? (Y/N):\n> ").strip().lower() =="y":
        main()


def display_incomplete_stages():
    i = 0
    incomplete_stages = list()
    for stage, status in completed.items():
        if not status:
            print("\t (%2d) %s" % (i, stage))
            incomplete_stages.append(stage)
            i += 1
    return incomplete_stages


def check_int(val):
    try:
        val = int(val)
        return val
    except ValueError:
        return False


def begin_math_stage():
    incomplete_stages = display_incomplete_stages()
    stage = input("請選擇想玩的遊戲:\n> ").strip().lower()
    stage_id = check_int(stage)
    if  stage_id <= len(incomplete_stages):
        stage = incomplete_stages[stage_id]
    try:
        if not completed[stage] or completed:
            math_stage(stage)
    except KeyError:
        print("{} 輸入錯誤囉 請輸入關卡編號.".format(stage))
        begin_math_stage()


def math_symbol(choice):
    if choice == "Season":
        return season
    elif choice == "Month":
        return month
    elif choice == "Number":
        return number


def get_questions(choice):
    season = {'春天（要喝雪碧）': 'spring',
              '夏天': 'summer',
              '秋天（什麼東西掉下來？）': 'fall',
              '冬天（風很大）': 'winter'}
    month = {'一月': 'January',
             '二月': 'February',
             '三月（好多）': 'March',
             '四月(是你的生日喔)': 'April',
             '五月': 'May',
             '六月': 'June',
             '七月': 'July',
             '八月（爸爸的生日）': 'August',
             '九月': 'September',
             '十月': 'October',
             '十一月': 'November',
             '十二月（聖誕老公公）': 'December'}
    number = {'one': 'first',
              'two': 'second',
              'three': 'third',
              'four': 'forth',
              'five': 'fifth',
              'six': 'sixth',
              'seven': 'seventh',
              'eight': 'eighth',
              'nine': 'ninth',
              'ten': 'tenth',
              'eleven': 'eleventh'}
    if choice == "Season":
        return season
    elif choice == "Month":
        return month
    elif choice == "Number":
        return number


def math_stage(stage, answers=None):
    print("現在進入%s關卡." % stage)
    input("按Enter繼續...")
    questions = get_questions(stage)
    # print(questions)
    if not answers:
        answers = list()
    wrong_answer = list()
    for question in questions:
        if questions[question] in answers:
            continue
        answer = questions[question]
        while True:
            try:
                # Question number 1: What is 5 * 5
                user_answer = str(input("請問{}怎麼拼".format(question)))
                break
            except ValueError:
                print("哈哈哈!答錯就看袁騰飛看到大學畢業吧~~~.\n> ")
            except TypeError:
                print("哈哈哈!答錯就看袁騰飛看到大學畢業吧~~~.\n> ")
        if answer != user_answer:
            print("答錯囉! ㄟ~有豬在飛耶~ 正確的答案是 {} 啦".format(answer))
            wrong_answer.append(answer)
            math_stage(stage, answers)
        else:
            answers.append(user_answer)
    
    print("恭喜你{}成功過關 !".format(stage))
    completed[stage] = True

    if not stages_complete():
        begin_math_stage()
    else:
        return False
        
            
def stages_complete():
    for status in completed.values():
        if not status:
            return False

    return True


# Clears the console screen.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Calls the main function on startup.
if __name__ == "__main__":
    main()