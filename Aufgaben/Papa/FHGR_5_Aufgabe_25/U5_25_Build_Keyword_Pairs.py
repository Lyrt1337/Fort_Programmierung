import csv

# Suchresultat
keyword_pairs = dict()

# load TOP 10
top10_path = 'U5_21_Keywords_TOP10.csv'

with open(top10_path, 'r', encoding='UTF-8-sig') as file:
    reader = csv.reader(file)
    res_top10 = {rows[0]: int(rows[1]) for rows in reader}
    res_top10_work = res_top10


def build_pairs():
    for [k, v] in res_top10.items():
        print(f"{k}: {v}")
        for k2, v2 in res_top10_work.items():
            print(f"{k2}: {v2}")
            # if not k == k2:
                # i = k + ' ' + k2
                # icheck = k2 + ' ' + k

                # Remove aus res-top10, da sonst umgekehrte Duplikate entstehen, "system - control" und "control - system"
                # if not i in keyword_pairs and not icheck in keyword_pairs:
            keyword_pairs[k + ' ' + k2] = keyword_pairs.get(k + ' ' + k2, 0) + 1

    return keyword_pairs


def main():
    save_path = 'U5_25_Keywords_TOP10_Pairs.csv'

    # Paare bilden
    keyword_pairs_all = build_pairs()

    # Save Excel .csv
    with open(save_path, 'w', encoding='UTF-8') as f:
        for key in keyword_pairs_all.keys():
            f.write("%s, %s\n" % (str(key), keyword_pairs_all[key]))


if __name__ == '__main__':
    main()
