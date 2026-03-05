import math
import sympy as sp

series = """Input your series in the form of list"""

def difference_finder(series_list: list):
    series_diff_list = []
    for i in range(len(series_list) - 1):
        series_diff_list.append(series_list[i + 1] - series_list[i])

    constant = True
    term_1 = series_diff_list[0]
    for num in series_diff_list:
        if math.isclose(term_1, num):
            continue
        else:
            constant = False

    return (series_diff_list, constant)

def series_difference_aggregates(terms_of_series: list):
    """This function takes given list of series, finds differences
    between them and store it in new list until the
    difference is constant"""
    possible = True
    series_aggregates = {
        "agg_0": terms_of_series
    }

    count = 0
    is_constant = False

    while not is_constant:
        calculate = difference_finder(series_aggregates[f"agg_{count}"])
        count += 1

        if len(calculate[0]) > 1:
            series_aggregates[f"agg_{count}"] = calculate[0]
            is_constant = calculate[1]
        else:
            possible = False
            break

    return (series_aggregates, possible)




def sum_of_series(terms_of_series: list):
    """This function takes terms
    of the series as input and
    returns general formula to
    the sum of series"""

    series_aggregates = series_difference_aggregates(terms_of_series)

    if series_aggregates[1]:
        n = sp.symbols("n")
        aggregates_first_terms = []
        sum = 0
        coeff = 1
        for key, values in series_aggregates[0].items():
            # print(values)
            aggregates_first_terms.append(values[0])

        for i in range(len(aggregates_first_terms)):
            coeff *= (n - i)
            sum += coeff*aggregates_first_terms[i]/(math.factorial(i + 1))

        return f"General equation of sum of series is: {sp.simplify(sum)}"

    else:
        print("Terms are not sufficient to find constant difference\nor it is not possible to find sum.")

if __name__ == "__main__":
    sum_of_series(series)