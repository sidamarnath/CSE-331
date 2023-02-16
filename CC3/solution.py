"""
CC3 Student Submission
Name: Sidharth Amarnath
"""

from typing import List, Tuple


def calculate(participants: List[str], character_details: List[Tuple[str, str, int]]) \
        -> List[Tuple[str, int]]:
    """
    docstring: PLEASE fill it here,
    example is on CC1
    """
    num_of_participants = len(participants)
    power_levels_list = []
    eng_to_jap_dict = {}
    jap_to_eng_dict = {}

    for idx in range(num_of_participants):
        participant = participants[idx]
        for jdx in range(len(character_details)):
            row = character_details[jdx]
            name1 = row[0]
            name2 = row[1]
            score = row[2]

            if participant in (name1, name2):
                power_levels_list.append(score)

    for kdx in range(len(character_details)):
        row = character_details[kdx]
        name1 = row[0]
        name2 = row[1]
        if 64 < ord(name1[0]) < 123:
            eng_to_jap_dict[name1] = name2
            jap_to_eng_dict[name2] = name1
        else:
            eng_to_jap_dict[name2] = name1
            jap_to_eng_dict[name1] = name2

        kdx = kdx + 1

    final_score = []
    for ndx in range(num_of_participants):
        current_score = power_levels_list[ndx]
        original_score = current_score
        current_participant = participants[ndx]
        total_score = 0

        for mdx in range(ndx + 1, num_of_participants):
            next_score = power_levels_list[mdx]
            if current_score >= next_score:
                total_score += next_score
            else:
                break

        if 64 < ord(current_participant[0]) < 123:
            current_participant_jap = eng_to_jap_dict[current_participant]
            current_participant_eng = current_participant
        else:
            current_participant_eng = jap_to_eng_dict[current_participant]
            current_participant_jap = current_participant

        if original_score <= 9000:
            pair = (current_participant_eng, total_score)
        else:
            pair = (current_participant_jap, total_score)

        final_score.append(pair)
        ndx = ndx + 1

    return final_score
