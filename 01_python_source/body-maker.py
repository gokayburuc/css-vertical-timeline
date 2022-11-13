import csv

title = ""
date = ""
description = ""
option = ["l", "r"]

# direction-l
# direction-r

pattern = f"""
       <li>
            <div class="direction-{option}">
                <div class="flag-wrapper">
                    <span class="flag">{title}</span>
                    <span class="time-wrapper"><span class="time">{date}</span></span>
                </div>
                <div class="desc">{description}</div>
            </div>
        </li>
"""


def createBox(title, date, description, id):

    # right left choice
    if id % 2 == 0:
        option = "r"
    else:
        option = "l"

    # pattern
    pattern = f"""
       <li>
            <div class="direction-{option}">
                <div class="flag-wrapper">
                    <span class="flag">{title}</span>
                    <span class="time-wrapper"><span class="time">{date}</span></span>
                </div>
                <div class="desc">{description}</div>
            </div>
        </li>
    """

    return pattern


# read csv
# write file into the test.html
with open("test.html", "w") as writeFile:
    with open("chrono.csv", "r") as readMyFile:
        rd = csv.reader(readMyFile)
        id = 0
        print("<body>", file=writeFile)
        print('<ul class="timeline">', file=writeFile)
        for t in rd:
            try:
                id += 1
                x = createBox(title=t[0], date=t[1], description=t[2], id=id)
                print(x, file=writeFile)
            except:
                pass
        print("</body>", file=writeFile)
