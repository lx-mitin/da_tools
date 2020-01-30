"""Extend DataFrame functionality."""


def unique(df):
    """Return quantity and samples of unique values for each column."""
    uniques = dict(df.nunique())

    for k in uniques.keys():
        vc = df[k].value_counts(normalize=True, dropna=False).head()
        vc = vc.map(lambda v: round(v, 4))
        uniques[k] = {'unique_counts': uniques[k], 'value_counts': dict(vc)}

    return uniques
