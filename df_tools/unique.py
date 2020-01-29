"""Extend DataFrame functionality."""


def unique(df):
    """Return quantity and samples of unique values for each column."""
    uniques = dict(df.nunique())
    for k in uniques.keys():
        uniques[k] = {'quantity':uniques[k], 'list':df[k].unique()}

    return uniques
