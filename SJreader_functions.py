import numpy as np

def get_my_keys(dataframe):
    keys1 = dataframe['keyword1'].values
    keys2 = dataframe['keyword2'].values
    keys3 = dataframe['keyword3'].values
    keys4 = dataframe['keyword4'].values

    my_keys = []
    for key in keys1:
        my_keys.append((key).strip())
    for key in keys2:
        my_keys.append((key).strip())
    for key in keys3:
        my_keys.append((key).strip())
    for key in keys4:
        my_keys.append((key).strip())

    my_keys = filter(None,my_keys)
    my_keys = [x.lower() for x in my_keys]
    keys = list(set(my_keys))

    return(keys)

def title_key_scores(keys, titles):
    title_scores = np.zeros([len(titles),1])
    for n, title in enumerate(titles):
        score = 0
        title = title.lower()
        for key in keys:
            if key in title:
                score+=1
        title_scores[n,0] = score
    return(title_scores)

def title_word_scores(my_titles, titles):
    scores = 0
    return(scores)

def journal_scores(my_journals, journals):
    my_journal_set = list(set(my_journals))
    journal_score = np.zeros([len(journals),1])
    for n, journal in enumerate(journals):
        if journal in my_journal_set:
            journal_score[n,0] = 1
    return(journal_score)

def keyword_scores(my_keys, dataframe):
    keys1 = dataframe['keyword1'].values
    keys2 = dataframe['keyword2'].values
    keys3 = dataframe['keyword3'].values
    keys4 = dataframe['keyword4'].values

    key_scores = np.zeros([len(keys1),1])

    for N in range(len(keys1)):
        keys = []
        keys.append((keys1[N]).strip())
        keys.append((keys2[N]).strip())
        keys.append((keys3[N]).strip())
        keys.append((keys4[N]).strip())
        keys = [x.lower() for x in keys]
        for key in keys:
            if key in my_keys:
                key_scores[N]+=1
    return(key_scores)

def abstract_key_scores(keys, abstracts):
    scores = np.zeros([len(abstracts),1])
    for n, abs in enumerate(abstracts):
        score = 0
        abs = abs.lower()
        for key in keys:
            if key in abs:
                score+=1
        scores[n,0] = score
    return(scores)

def abstract_word_scores(my_abstracts, abstracts):
    scores = 0
    return(scores)