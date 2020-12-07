import re

with open('day4.txt', 'r') as f:
    batch = f.read()

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

re_passport_group = r"(.+\n?.+\n?.+\n?.+\n?.+\n?.+\n?.+\n?.+)"

passport_groups = re.findall(re_passport_group, batch)

valid_passports = []
"""
for pg in passport_groups:
    is_valid = True
    for field in fields:
        is_valid *= field in pg

    if is_valid:
        valid_passports.append(pg)
"""

re_byr = r"byr:(\d+)"
re_iyr = r"iyr:(\d+)"
re_eyr = r"eyr:(\d+)"
re_hgt = r"hgt:(\d+)(cm|in)"
re_hcl = r"hcl:#([a-f0-9]{6})"
re_ecl = r"ecl:(amb|blu|brn|gry|grn|hzl|oth)"
re_pid = r"pid:([0-9]{9})"


def getByr(passport):
    byr = re.findall(re_byr, passport)
    if len(byr) > 0:
        return int(byr[0]) <= 2002 and int(byr[0]) >= 1920
    else:
        return False


def getIyr(passport):
    iyr = re.findall(re_iyr, passport)
    if len(iyr) > 0:
        return int(iyr[0]) <= 2020 and int(iyr[0]) >= 2010
    else:
        return False


def getEyr(passport):
    eyr = re.findall(re_eyr, passport)
    if len(eyr) > 0:
        return int(eyr[0]) <= 2030 and int(eyr[0]) >= 2020
    else:
        return False


def getHgt(passport):
    hgt = re.findall(re_hgt, passport)
    if len(hgt) > 0:
        if hgt[0][1] == 'cm':
            return int(hgt[0][0]) <= 193 and int(hgt[0][0]) >= 150
        elif hgt[0][1] == 'in':
            return int(hgt[0][0]) <= 76 and int(hgt[0][0]) >= 59
        else:
            return False
    else:
        return False


def getHcl(passport):
    hcl = re.findall(re_hcl, passport)
    if len(hcl) > 0:
        if len(hcl[0]) == 6:
            return True
    else:
        return False


def getEcl(passport):
    ecl = re.findall(re_ecl, passport)
    if len(ecl) == 1:
        return True
    else:
        return False


def getPid(passport):
    pid = re.findall(re_pid, passport)
    if len(pid) > 0:
        return len(pid[0]) == 9
    else:
        return False


strict_passports = []
for passport in passport_groups:
    is_valid = True
    is_valid *= getByr(passport)
    is_valid *= getIyr(passport)
    is_valid *= getEyr(passport)
    is_valid *= getHgt(passport)
    is_valid *= getHcl(passport)
    is_valid *= getEcl(passport)
    is_valid *= getPid(passport)
    if is_valid:
        strict_passports.append(passport)

m = ";".join(strict_passports)
n = m.splitlines()
o = " ".join(n)
q = re.sub(";", "\n", o)
