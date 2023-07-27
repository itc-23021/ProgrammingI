vote_num = 0


def vote(answer):
    print("投票します")
    answer += 1
    return answer


def reset_box():
    print("箱を空にします")
    answer = 0
    return answer


def check_box(answer):
    print("票の数は{}です".format(vote_num))
    return
