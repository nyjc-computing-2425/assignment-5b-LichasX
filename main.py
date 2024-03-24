# Part 1
def read_csv(filename):
    """ test """
    data = []
    with open(filename, "r") as f:
      header = f.readline().split(",")
      for lines in f:
        lst = []
        count = 0
        for line in lines.split(","):
          if count == 0 or count == 3:
            line = int(line)
          lst.append(line)
          count += 1
        data.append(lst)
      return (header, data)
          
    


# Part 2
def filter_gender(enrolment_by_age, sex):
    """ test """
    lst = []
    for row in enrolment_by_age:
      if row[2] == sex:
        row.remove(sex)
        lst.append(row)
    return lst


# Part 3
def sum_by_year(enrolment):
    """ test """
    seen_years = []
    output = []
    for row in enrolment:
      if  row[0] not in seen_years:
        seen_years.append(row[0])
        try:
          output.append([year, total_enrolment])
        except UnboundLocalError:
          pass
        year = row[0]
        total_enrolment = 0
      total_enrolment += row[-1]
    return output
      


# Part 4
def write_csv(filename, header, data):
    """ test """
    with open(filename, "w") as f:
      f.writelines(header)
      for lists in data:
        lists = map(str, lists)
        f.write(",".join(lists))

