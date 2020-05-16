def latest(scores):
    return scores[-1]


def personal_best(scores):
    output = -1

    for x in scores:
        if x > output:
            output = x

    return output


def personal_top_three(scores):

    output = []

    if len(scores) >= 3:
        for x in range(3):
            output.append(personal_best(scores))
            scores.remove(personal_best(scores))
    else:
        for x in range(len(scores)):
            output.append(personal_best(scores))
            scores.remove(personal_best(scores))



    return output


