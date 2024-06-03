import sqlite3, requests

with open("poll.db", "wb") as file:
    response = requests.get("https://github.com/erelsgl-at-ariel/research-5784/raw/main/06-python-databases/homework/poll.db")
    file.write(response.content)
db = sqlite3.connect("poll.db")


def find_q6_num(name1:str):
    """
    Finds the variable name (Q6_num) based on the label.

    Args:
    name1 (str): The label to search for.

    Returns:
    str: The variable name (Q6_num) if found, else None.

    Examples:
    >>> find_q6_num("בנימין נתניהו")
    'Q6_1'
    >>> find_q6_num("יאיר לפיד")
    'Q6_2'
    """
    cursor = db.cursor()

    cursor.execute("SELECT Variable FROM codes_for_questions WHERE Label=?", (name1,))
    result = cursor.fetchone()


    if result:
        return result[0]  
    else:
        return None  
    

def find_label_by_variable(variable:str):
    """
    Finds the label based on the variable name (Q6_num).

    Args:
    variable (str): The variable name (Q6_num) to search for.

    Returns:
    str: The label if found, else None.

    Examples:
    >>> find_label_by_variable("Q6_1")
    'בנימין נתניהו'
    >>> find_label_by_variable("Q6_2")
    'יאיר לפיד'
    """
    cursor = db.cursor()

    cursor.execute("SELECT Label FROM codes_for_questions WHERE Variable=?", (variable,))
    result = cursor.fetchone()


    if result:
        return result[0]  
    else:
        return None  

def net_support_for_candidate1(candidate1:str, candidate2:str)->int:
    """
    Calculates the net support for candidate1 over candidate2.

    Args:
    candidate1 (str): The first candidate name or Q6_num.
    candidate2 (str): The second candidate name or Q6_num.

    Returns:
    int: The net support for candidate1.

    Examples:
    >>> net_support_for_candidate1('בנימין נתניהו', 'יאיר לפיד')
    -35
    >>> net_support_for_candidate1('Q6_1', 'Q6_2')
    -35
    """
    cursor = db.cursor()
    if "Q6_" not in candidate1 and "Q6_" not in candidate1:
        candidate1 = find_q6_num(candidate1)
        candidate2 = find_q6_num(candidate2)
    count1 = 0
    count2 = 0

    cursor.execute(f"SELECT {candidate1}, {candidate2} FROM list_of_answers")
    rows = cursor.fetchall()

    for row in rows:
        q6_f_value = row[0]  
        q6_s_value = row[1]
        if q6_f_value <= q6_s_value:
            count1 += 1
        else:
            count2 += 1

    return count1 - count2
    

def condorcet_winner()->str:
    """
    Finds the Condorcet winner among the candidates.

    Returns:
    str: The label of the Condorcet winner.

    Examples:
    >>> condorcet_winner()
    'נפתלי בנט'
    """
    for i in range(1,9):
        flag = True
        for j in range(1,9):
            if i!=j and net_support_for_candidate1('Q6_'+str(i),'Q6_'+str(j))<0:
                flag = False
                break
        if flag:
            return find_label_by_variable('Q6_'+str(i))
    return 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    party = input()
    if party == "condorcet_winner":
        print(condorcet_winner())
    else:
        candidate1,candidate2 = party.split(",")
        print(net_support_for_candidate1(candidate1,candidate2))
    db.close()
