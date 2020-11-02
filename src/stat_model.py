from scipy.stats import ttest_ind
import json

def ttest(df, outfile):
    '''
    The ttest is designed to determine if there is a significant difference
    between the means of two groups namely the first-born babies and all newborn babies.
    Null hypothesis: first borns are likely to arrive at the same time as all newborn babies.
    :param: df: input dataframe
    :param: outfile: file to save the results of the ttest
    '''

    df1 = df['prglength']
    df2 = df[df['birthord']==1]['prglength']
    s, pval = ttest_ind(df1, df2)
    json.dump({"statistic": s, "pvalue": pval}, open(outfile, 'w'))
    return ttest_ind(df1, df2)
