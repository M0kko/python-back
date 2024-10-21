def pipeline(stages: list[int], details: list[int]) -> list[int]:
    n = len(stages)
    m = len(details)
    complete_time = [0] * m
    cur_time = [0] * n
    det = dict((j, details[j]) for j in range(m))
    def val(x):
        return det[x]
    k = sorted(det, key=val)

    details.sort()
    for j in range(m):
        arrival_time = details[j]
        for i in range(n):
            if i == 0:
                cur_time[i] = max(arrival_time, cur_time[i]) + stages[i]
            else:
                cur_time[i] = max(cur_time[i - 1], cur_time[i]) + stages[i]
        complete_time[k[j]] = cur_time[-1]
    return complete_time