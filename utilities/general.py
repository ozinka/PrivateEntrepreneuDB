import sys
import sqlite3
import time


def count_lines_in_file(file_name: str):
    print("Checking file...")
    line_count = 0
    try:
        line_count = sum((1 for i in open(file_name, 'rb')))
    except FileNotFoundError:
        exit(2)
    print("Lines in the file: ", line_count)
    return line_count


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def check_speed(n: float, m: float):
    if m == 0:
        return "∞"
    return str(round(n / m, 1))


def parse_name(name_str: str):
    name_lst = name_str.split()
    if len(name_lst) >= 3:
        return (name_lst[0], name_lst[1], ' '.join(name_lst[2:]))
    if len(name_lst) == 2:
        name_lst.append("")
        return tuple(name_lst)
    if len(name_lst) == 1:
        name_lst = name_lst + ["", ""]
        # print(name_lst)
        return tuple(name_lst)


def parse_xml(file_name: str, db: str):
    current_line = 0
    total_lines = count_lines_in_file(file_name)
    data = {}
    record_cnt = 0
    start = round(time.clock(), 1)

    conn = sqlite3.connect(db)  # , isolation_level=None)

    for line in open(file_name):
        # if current_line >= 5000:
        #     break
        if current_line % 10000 == 0:
            conn.commit()
            tm = round(time.clock() - start, 1)
            sts = "time: " + str(tm) + " s, speed: " + check_speed(record_cnt, tm) + " r/s"
            progress(current_line, total_lines, status=sts)

        current_line += 1

        work_line = line.strip()

        if work_line == "</ROW>":
            b = parse_name(data.get('ПІБ', "Null")) + (data.get('Місце_проживання', "Null"),
                                                       data.get('Основний_вид_діяльності', "Null"),
                                                       data.get('Стан', "Null"))
            try:
                sql = "INSERT INTO main(surname, first_name, patronymic, live_place, activity_type, state) VALUES (?,?,?,?,?,?)"
                conn.cursor().execute(sql, b)
                record_cnt += 1
            except sqlite3.OperationalError:
                print("Error on Data: ", b)
                print("Line in file: ", current_line)
                exit(2)

            continue

        if work_line == "<ROW>":
            data = {}
            continue
        if work_line == "":
            continue
        data_string = parse_line(work_line)
        if data_string is None:
            continue
        else:
            data[data_string[0]] = data_string[1]

    conn.close()
    print("Current line: ", current_line)
    return


def parse_line(input_str: str):
    cat = input_str[input_str.find("<") + 1: input_str.find(">")]
    start = input_str.find(">") + 1
    end = input_str.find("<", start)
    result = [cat, ' '.join(str.strip(input_str[start:end]).split())]
    if result[0] == '' or result[1] == '':
        return None
    return result
