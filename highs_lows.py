import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中提取最高温和日期和最低气温
# filename='sitka_weather_07-2018_simple.csv'
# filename='sitka_weather_2018_simple.csv'

# 错误检查
filename='death_valley_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows=[],[],[]
    for row in reader:
        # current_date=datetime.strptime(row[2],"%Y-%m-%d")
        # high =int(row[5])
        # highs.append(high)
        #
        # dates.append(current_date)
        #
        # low=int(row[6])
        # lows.append(low)

        # 错误检查，使用try-except-else,当然在具体问题的处理中，可以使用continue来跳过一些数据，或者使用remove()或del将已提取的数据删除
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)

    for index,column_header in enumerate(header_row):
        print(index,column_header)

    # 根据数据绘制图形
    fig=plt.figure(dpi=128,figsize=(6,4))
    # plt.plot(highs,c='red')
    # plt.plot(dates,highs,c='red')
    # plt.plot(dates,lows,c='blue')

    # alpha表示透明度，0表示完全透明，1（默认值）表示完全不透明
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    # 设置图形的格式
    # plt.title("Daily high temperatures,July 2018",fontsize=18)
    # plt.title("Daily high temperatures,2018", fontsize=18)
    # plt.title("Daily high and low temperatures,2018", fontsize=18)
    title="Daily high and low temperatures,2018\nDeath Valley,CA"
    plt.title(title,fontsize=12)

    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)",fontsize=8)
    plt.tick_params(axis='both',which='major',labelsize=14)

    plt.show()
