km1 = ["ABACD", "BCEFD"]
tg1 = ["ABCD","AABB"]

''' 1. target을 나눠서 한 글자씩 쪼갠다
    2. 쪼갠 한 글자들이 keymap 안의 key에 있는지 확인한다
    3. 그 글자가 key에 있으면, 그 key 문자열에서 몇 번째인지를 idx 리스트에 넣는다
    4. key1, key2, key3 ... 다 확인한 다음 여러개면 그 중 가장 작은 숫자만 idx에 남긴다
    5. idx+1을 index에 append하여 전체 반복하고, index의 원소들의 합을 구한다
'''

def solution(keymap, targets):
    targetlist = []
    index = []

    for target in targets:
        sp_target = list(target)
        targetlist.append(sp_target)

    # print(targetlist)
    # [['A', 'B', 'C', 'D'], ['A', 'A', 'B', 'B']]
    #    tg3 = ["ASA","BGZ"]
    

    # km1 = ["ABACD", "BCEFD"]
    # km3 = ["AGZ", "BSSS"]

    for target in targetlist:
        sum = 0
        for t in target:
            idx = []
            for key in keymap:
                if t in key:
                    idx.append((key.index(t)+1))

            if len(idx) == 0:
                index = [-1]
                return index
                
            sum += min(idx)
        index.append(sum)

    return index


if __name__ == '__main__':
    km1 = ["ABACD", "BCEFD"]
    km2 = ["AA"]
    km3 = ["AGZ", "BSSS"]

    tg1 = ["ABCD","AABB"]
    tg2 = ["B"]
    tg3 = ["ASA","BGZ"]

    rs1 = [9, 4]
    rs2 = [-1]
    rs3 = [4, 6]

    print(solution(km2, tg2))