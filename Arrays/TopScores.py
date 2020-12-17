#   Top Scores program
"""
You created a game that is more popular than angry birds.
Each round, players receive a score between 0 and 100, which you can use to rank them from highest to lowest. So far you are using
an algorithm that sorts in O(nlogn) time, but players are complaining that their ranking are not updated fast enough.
you need a faster sorting algorithm.
"""


def sort_score(unsorted_scores : list, highest_possible_score : int) -> list : 
    hashtable = [0]*highest_possible_score
    output = list()

    for score in unsorted_scores : hashtable[score] += 1
    
    for i in range(len(hashtable)-1, -1, -1) :
        times = hashtable[i]
        score = i

        for _ in range(times) : 
            output.append(score)

    return output


if __name__ == "__main__":
    unsorted_scores = [37, 89, 41, 65, 91, 53]
    HIGHEST_SCORE_POSSIBLE = 100

    print(sort_score(unsorted_scores, HIGHEST_SCORE_POSSIBLE))

