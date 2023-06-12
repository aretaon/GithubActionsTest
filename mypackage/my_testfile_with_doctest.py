import matplotlib.pyplot as plt
import seaborn as sns


def plot_something(x: str, y: str) -> plt.figure:
    """
    Testing plot function

    Parameters
    ----------

    x: str
        Column name x
    y: str
        Column name y

    Returns
    -------
    plt.figure
        The figure object

    Examples
    --------
    This is an example plot

    >>> fig = plot_something('species', 'petal_length')  # doctest: +SKIP
    >>> fig.show() # doctest: +SKIP

    .. plot::
        :context: close-figs

        >>> from mypackage import plot_something
        >>> fig = plot_something('species', 'petal_length')
        >>> fig.show()

    .. testcode::
        :hide:

        fig = plot_something('species', 'petal_length')
        data = fig.axes[0].collections[0].get_offsets().data
        print(np.median(data[data.T[0] == 1].T[1]))

    .. testoutput::
        :hide:

        4.35
    """
    iris = sns.load_dataset("iris")
    fig, ax = plt.subplots()
    sns.scatterplot(data=iris, x=x, y=y, ax=ax)

    return fig
