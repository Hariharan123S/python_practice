import random
import Day_14_higher_or_lower
import art
print(art.logo_14)
datas = Day_14_higher_or_lower.data


def rdm(u_compare):
    rdm_name = u_compare['name']
    rdm_des = u_compare['description']
    rdm_country = u_compare['country']
    return f"{rdm_name}, {rdm_des}, from {rdm_country}"


def compare(u_guess, a_compare, b_compare):
    if a_compare > b_compare:
        return u_guess == "a"
    else:
        return u_guess == "b"
score = 0
compare_b = random.choice(datas)
continue_game = True
while continue_game:

    compare_a = compare_b
    compare_b = random.choice(datas)
    if compare_a == compare_b:
        compare_b = random.choice(datas)

    print(f"Compare A: {rdm(compare_a)}")
    print(art.logo14)
    print(f"Compare B: {rdm(compare_b)}")

    guess = input("Guess who has more followers? 'A' or 'B: ").lower()
    a_followers = compare_a['followers']
    b_followers = compare_b['followers']
    is_correct = compare(guess, a_followers, b_followers)
    print("\n" * 20)

    if is_correct:
        score += 1
        print("You're right!")
    else:
        print(f"Sorry!Game Over.Your final score is {score}")
        continue_game = False
