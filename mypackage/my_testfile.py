import matplotlib.pyplot as plt
import seaborn as sns
from . import r_helper
from subprocess import run, PIPE

RFUNCTIONS, R = r_helper.return_r_path()


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

    .. plot::
        :context: close-figs

        from mypackage import plot_something
        fig = plot_something('species', 'petal_length')
        fig.show()
    """
    iris = sns.load_dataset("iris")
    fig, ax = plt.subplots()
    sns.scatterplot(data=iris, x=x, y=y, ax=ax)

    return fig


def a_function_with_R(test_string):
    r"""
    This function uses a local R installation to run a script and output the value

    Parameters
    ----------
    test_string: str
        A string to echo with R

    Returns
    -------
    str
        Output of rcode

    Examples
    --------
    >>> r = a_function_with_R('Hello World')  # doctest: +ELLIPSIS
    Calling: [..., '--vanilla', ..., 'Hello World']

    """
    command = [R, '--vanilla', RFUNCTIONS, test_string]
    print(f"Calling: {command}")

    p = run(command,
            stdout=PIPE,
            universal_newlines=True)

    r_out = p.stdout.strip()

    return r_out
