"""Extend DataFrame functionality."""


def unique(df, number=5, columns=[]):
    """Return quantity and samples of unique values for each column."""
    if columns:
        uniques = dict(df[columns].nunique())
    else:
        uniques = dict(df.nunique())

    for k in uniques.keys():
        val_c = df[k].value_counts(normalize=True, dropna=False).head(number)
        val_c = val_c.map(lambda v: round(v, 4))
        uniques[k] = {'unique_counts': uniques[k], 'value_counts': dict(val_c)}

    return uniques
