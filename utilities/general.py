import sys


def count_lines_in_file(file_name: str):
    print("Checking file...")
    try:
        line_count = sum((1 for i in open(file_name, 'rb')))
    except FileNotFoundError:
        exit(2)
    return line_count


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def parse_xml(file_name: str, db: str):
    current_line = 0
    data = {}
    total_lines = count_lines_in_file(file_name)
    f = open("result.txt", 'a')
    print("Parsing started...")
    try:
        for line in open(file_name):

            current_line += 1
            if current_line % 10000 == 0:
                progress(current_line, total_lines, status="Parsing file")

            #sys.stdout.write("\r%d%%" % current_line)
            work_line = line.strip()
            if work_line == "</ROW>":
                # print(data)
                f.write(str(data) + '\n')
                continue
            if work_line == "<ROW>":
                data = {}
            if work_line == "":
                continue
            data_string = parse_line(work_line)
            if data_string is None:
                continue
            data[data_string[0]] = data_string[1]
    except FileNotFoundError:
        print("error with reading file " + file_name)
        exit(2)
    f.close()
    return


def parse_line(input_str: str):
    cat = input_str[input_str.find("<") + 1: input_str.find(">")]
    start = input_str.find(">") + 1
    end = input_str.find("<", start)
    result = [cat, ' '.join(str.strip(input_str[start:end]).split())]
    if result[0] == '' or result[1] == '':
        return None
    return result
