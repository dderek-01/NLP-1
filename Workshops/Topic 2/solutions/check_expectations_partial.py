# coding: utf-8
def check_expectations(word_list,freqdist1,freqdist2,headers):
    match_freq = [freqdist1[word] for word in word_list]
    mismatch_freq = [freqdist2[word] for word in word_list]
    as_expected = [match_freq[i]>mismatch_freq[i] for i in range(len(word_list))]
    headers.append('Expected?')
    df = pd.DataFrame(list(zip_longest(word_list,match_freq,mismatch_freq,as_expected)), columns=headers)
    display(df,"\n")