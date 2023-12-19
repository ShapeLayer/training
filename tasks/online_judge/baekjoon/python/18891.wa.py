from math import floor
from sys import stdin
input = stdin.readline

class Party:
    def __init__(self, name: str, district: int, vote: int):
        '''
        :param name: 정당 이름
        :param district: 지역구 의석
        :param vote: 비례대표 득표수
        :param rate: 득표율
        :param prop_rate: 비례득표율
        :param calc_target: 봉쇄 조항 통과 여부 (계산 대상)
        :param p: 
        :param p_rate: 
        '''
        self.name = name
        self.district = district
        self.vote = vote
        self.rate = 0
        self.prop_rate = 0
        self.calc_target = False
        self.p = [-1, 0, 0, 0]
        self.p_rate = [-1, 0, 0, 0]
        self.gains = 0

def round(n: float) -> int:
    return n + 1 if n - int(n) >= .5 else n

def compute(p: int, v: int, av: int, parties: list[Party]):
    def preprocess(p: int, v: int, av: int, parties: list[Party]):
        '''
        전처리 단계
        봉쇄 조항 처리
        '''

        # 득표율
        for party in parties:
            party.rate = party.vote / av
            party.calc_target = party.district >= 5 or party.rate >= .03
            if not party.calc_target:
                av -= party.vote
        
        # 비례득표율
        for party in parties:
            if party.calc_target:
                party.prop_rate = party.vote / av
    
    def compute_step_1(p: int, v: int, av: int, parties: list[Party]):
        '''
        (1단계) 30석에 대해 전국단위 준연동(연동비율 50%) 방식으로 각 정당별 연동배분의석수 산정
        '''
        total, district = 300, 253
        for party in parties:
            if not party.calc_target:
                continue
            district -= party.district
        
        for party in parties:
            if not party.calc_target:
                continue
            party.p[1] = ((total - district) * party.prop_rate - party.district) / 2
            party.p[1] = round(party.p[1]) if party.p[1] >= 1 else 0
    
    def compute_step_2(p: int, v: int, av: int, parties: list[Party]):
        '''
        (2-1단계) 각 정당별 연동배분의석수의 합계 < 30석일 경우 ☞ 잔여의석에 대해 기존 의석배분방식(병립형) 적용 배분
        (2-2단계) 각 정당별 연동배분의석수의 합계 > 30석 ☞ 각 정당별 연동배분의석수비율대로 배분
        '''
        linked_dist = 0
        for party in parties:
            if not party.calc_target:
                continue
            linked_dist += party.p[1]
        
        if linked_dist == 30:
            for party in parties:
                party.p2 = party.p1
            return
        

        # compute_step_2_other
        make_30 = 0
        if linked_dist < 30:
            # compute_step_2_1
            for party in parties:
                if not party.calc_target:
                    continue
                party.p_rate[2] = party.p[1] + (30 - linked_dist) * party.prop_rate
                party.p[2] = int(party.p_rate[2])
                party.p_rate[2] -= party.p[2]
                make_30 += party.p[2]
            for party in sorted(parties, key=lambda each: (each.p_rate[2], each.name), reverse=True):
                if not party.calc_target:
                    continue
                if make_30 >= 30:
                    break
                party.p[2] += 1
                make_30 += 1
        else:
            # compute_step_2_2
            for party in parties:
                if not party.calc_target:
                    continue
                party.p_rate[2] = (30 * party.p[1]) / linked_dist
                party.p[2] = int(party.p_rate[2])
                party.p_rate[2] -= party.p[2]
                make_30 += party.p[2]
            for party in sorted(parties, key=lambda each: (each.p_rate[2], each.name), reverse=True):
                if not party.calc_target:
                    continue
                if make_30 >= 30:
                    break
                party.p[2] += 1
                make_30 += 1

    def compute_step_3(p: int, v: int, av: int, parties: list[Party]):
        '''
        (3단계) 17석에 대해 기존 의석배분방식(병립형) 적용 배분
        '''
        total = 0
        for party in parties:
            if not party.calc_target:
                continue
            party.p_rate[3] = 17 * party.prop_rate
            party.p[3] = int(party.p_rate[3])
            party.p_rate[3] -= party.p[3]
            total += party.p[3]
        
        for party in sorted(parties, key=lambda each: (each.p_rate[3], each.name), reverse=True):
            if not party.calc_target:
                continue
            if total >= 17:
                break
            party.p[3] += 1
            total += 1

    preprocess(p, v, av, parties)
    compute_step_1(p, v, av, parties)
    compute_step_2(p, v, av, parties)
    compute_step_3(p, v, av, parties)

    for party in parties:
        if party.calc_target:
            party.gains = party.district + party.p[2] + party.p[3]
        else:
            party.gains = party.district

    return parties

if __name__ == '__main__':
    p, v = map(int, input().split())
    parties: list[Party] = []
    av = 0
    for _i in range(p):
        name, dist, vote = input().split()
        parties.append(Party(name, int(dist), int(vote)))
        av += int(vote)
    parties = compute(p, v, av, parties)
    for party in sorted(parties, key=lambda each: [-each.gains, each.name]):
        print(party.name, party.gains)
