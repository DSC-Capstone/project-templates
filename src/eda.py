
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


def scatter_matrix(data, outdir):

    pd.plotting.scatter_matrix(data)
    plt.suptitle('Independent Gaussians')
    plt.savefig(os.path.join(outdir, 'scatter_matrix.png'))


def histograms_by_var(data, outdir):

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    sns.violinplot(data=pd.melt(data), x='variable', y='value', ax=axes[0])
    axes[0].title.set_text('Violin plot of each variable') 
    pd.melt(data).groupby('variable')['value'].plot(kind='kde', ax=axes[1])
    axes[1].title.set_text('distribution of each variable') 
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, 'histogram.png'))


def basic_stats(data, outdir):

    out = pd.concat(
        [data.mean().rename('means'), 
         data.std().rename('standard deviations')], 
        axis=1)

    out.to_csv(os.path.join(outdir, 'basic_stats.csv'))


def normality_test(data, outdir):

    from scipy.stats import normaltest

    out = (
        data
        .apply(lambda x: pd.Series(
            normaltest(x), 
            index=['skew-test + kurtosis-test', 'p-value']
        )).T
    )

    out.to_csv(os.path.join(outdir, 'normality_results.csv'))

    return


def ks_results(data, outdir):

    from scipy.stats import ks_2samp
    res = ks_2samp(data['x_0'], data['x_1'])

    out = pd.Series({'ks statistic': res.statistic, 'p-value': res.pvalue}).rename('KS Test')
    out.to_csv(os.path.join(outdir, 'ks_results.csv'))


def generate_stats(data, outdir, **kwargs):

    os.makedirs(outdir, exist_ok=True)
    scatter_matrix(data, outdir)
    histograms_by_var(data, outdir)
    basic_stats(data, outdir)
    normality_test(data, outdir)
    ks_results(data, outdir)
    
    return
