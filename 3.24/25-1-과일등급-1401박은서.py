a = int(input(f'과일 무게(g): '))
if a>=370 or a<210:
    print('"판정 불가"')
if 300<=a<=375:
    print('"특"')
if 250<=a<300:
    print('"상"')
if 210<=a<250:
    print('"보통"')