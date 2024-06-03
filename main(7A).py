import pandas as pd

codes_for_questions = pd.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_questions.csv")
codes_for_answers = pd.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_answers.csv")
list_of_answers = pd.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/list_of_answers.csv")

def get_party_label(party_code: str) -> str:
    """
    Get the label of the party based on its code.
    
    Args:
    - party_code (str): The party code.
    
    Returns:
    - str: The label of the party.
    
    >>> get_party_label('מחל')
    1
    """
    def split_and_check(label):
        if isinstance(label, str):
            parts = label.split(' - ')
            return parts[0] == party_code
        return False

    filtered = codes_for_answers[(codes_for_answers['Value'] == 'Q2') & (codes_for_answers['Label'].apply(split_and_check))]
    
    if not filtered.empty:
        return filtered['Code'].values[0]
    else:
        raise ValueError(f"No label found for party code {party_code}")

def support_in_one_party_elections(party: str) -> int:
    """
    Calculate the number of supporters for a party in single-party elections (Q2).
    
    Args:
    - party (str): The code of the party.
    
    Returns:
    - int: The number of supporters for the party.
    
    >>> support_in_one_party_elections('מחל')
    134
    """
    return list_of_answers[list_of_answers['Q2'] == get_party_label(party)].shape[0]

def support_in_multi_party_elections(party: str) -> int:
    """
    Calculate the number of supporters for a party in multi-party elections (Q3).
    
    Args:
    - party (str): The code of the party.
    
    Returns:
    - int: The number of supporters for the party.
    
    >>> support_in_multi_party_elections('מחל')
    162
    """
    return list_of_answers[list_of_answers['Q3_'+str(get_party_label(party))] == 1.0].shape[0]

def parties_with_different_relative_order():
    """
    Find pairs of parties with different relative order of support in Q2 and Q3.
    
    Returns:
    - list: Pairs of parties with a different relative order.
    
    >>> parties_with_different_relative_order()
    [(6, 4), (7, 3), (7, 8), (7, 12), (7, 14), (8, 3), (10, 3), (10, 7), (10, 8), (10, 12), (10, 14), (11, 12), (13, 3), (13, 7), (13, 8), (13, 12), (13, 14), (16, 14), (16, 15), (17, 4), (17, 6), (17, 9), (17, 11), (17, 12)]
    """
    def support_in_one_party_elections(code: int) -> int:
        """
        Calculate the number of supporters for a party in single-party elections (Q2).
        
        Args:
        - code (int): The code of the party.
        
        Returns:
        - int: The number of supporters for the party.
        """
        return list_of_answers[list_of_answers['Q2'] == code].shape[0]

    def support_in_multi_party_elections(code: int) -> int:
        """
        Calculate the number of supporters for a party in multi-party elections (Q3).
        
        Args:
        - code (int): The code of the party.
        
        Returns:
        - int: The number of supporters for the party.
        """
        return list_of_answers[list_of_answers['Q3_'+str(code)] == 1.0].shape[0]

    different_order_parties = []
    for i in range(1, 18):
        for j in range(1, 18):
            s1i = support_in_one_party_elections(i)
            smi = support_in_multi_party_elections(i)
            s1j = support_in_one_party_elections(j)
            smj = support_in_multi_party_elections(j)
            if i != j and s1i > s1j and smj > smi:
                different_order_parties.append((i, j))
    
    return different_order_parties

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    party = input("Enter party code or 'parties_with_different_relative_order': ")
    if party == "parties_with_different_relative_order":
        print(parties_with_different_relative_order())
    else:
        print(support_in_one_party_elections(party), support_in_multi_party_elections(party))
