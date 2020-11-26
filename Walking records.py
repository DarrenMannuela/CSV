file = None
with open("Walking Records.csv", "r") as d:
    file = d.read()

data = file.split("\n")
res = {}
for line in range(0, len(data)):
    temp = data[line].split(",")
    if line == 0:
        for header in temp:
            res[header.strip().split('\"')[1]] = []
    else:
        if len(temp) == 1:
            break
        res["steps"].append(temp[0].split("\"")[1])

        res["date"].append(temp[1][2:12].split(","))

        interval = (temp[2][0:4].split("\""))
        res["interval"].append(interval[0].split())

steps_list_length = len(res["steps"])
weekday_or_weekend = {}
total_steps_in_a_day = {}
steps_per_interval_in_a_day = {}
interval_in_a_day = {}
mean = {}
median = {}
new_res = {}
NA_count = 0
day_counter = 1
for step_count in range(steps_list_length-1):
    steps = res["steps"][step_count]
    date = res["date"][step_count][0]
    interval = res["interval"][step_count][0]

    weekday_or_weekend.setdefault(date, "")
    total_steps_in_a_day.setdefault(date, 0)
    steps_per_interval_in_a_day.setdefault(date, [])
    interval_in_a_day.setdefault(date, [])
    new_res.setdefault("steps", [])
    new_res.setdefault("date", [])
    new_res.setdefault("interval", [])
    interval_in_a_day[date].append(interval)

    if day_counter <= 5:
        weekday_or_weekend[date] = "Weekday"
        day_counter += 1
    else:
        weekday_or_weekend[date] = "Weekend"
        day_counter += 1

    if day_counter > 7:
        day_counter = 1

    if steps == "NA":
        NA_count += 1
        steps = "0"
        steps = int(steps)
        total_steps_in_a_day[date] += steps
        steps_per_interval_in_a_day[date].append(steps)
        continue
    else:
        mean.setdefault(date, 0)
        median.setdefault(date, 0)
        steps = int(steps)
        if date == date:
            steps_per_interval_in_a_day[date].append(steps)
            length_interval_in_a_day = len(interval_in_a_day[date])
            length_steps_per_interval_in_a_day = len(steps_per_interval_in_a_day[date])
            total_steps_in_a_day[date] += steps
            mean[date] = total_steps_in_a_day[date]/length_interval_in_a_day
            median_date = length_steps_per_interval_in_a_day % 2
            if median_date == 0:
                index = length_interval_in_a_day//2
                median[date] = steps_per_interval_in_a_day[date][index]
            else:
                index = length_interval_in_a_day // 2
                median[date] = steps_per_interval_in_a_day[date][index-1]
        new_res["steps"].append(steps)
        new_res["date"].append(date)
        new_res["interval"].append(steps)

print("1.", total_steps_in_a_day)
print("2.Mean:", mean)
print("2.Median:", median)
print("3.NA Count:", NA_count)
print("5.New dict:", new_res)
print("6.Weekend or weekday:", weekday_or_weekend)
