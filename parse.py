import xlrd
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_high_risk(x_labels, frequencies):

    freq_series = pd.Series.from_array(frequencies)
    print('#' * 50)
    print(freq_series)
    print(x_labels)
    print('#' * 50)
    # Plot the figure.
    plt.figure(figsize=(12, 8))
    ax = freq_series.plot(kind='bar')
    ax.set_title('Amount Frequency')
    ax.set_xlabel('Amount ($)')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    # For each bar: Place a label
    for rect in rects:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:}".format(y_value)

        # Create annotation
        plt.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)  # Vertically align label differently for
        # positive and negative values.

    plt.savefig("image.png")

def plot_pie(labels, values):
    # labels = 'Python', 'C++', 'Ruby', 'Java'
    # sizes = [215, 130, 245, 210]
    # colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    colors = ['yellowgreen', 'lightcoral']
    explode = (0.1, 0)  # explode 1st slice

    # Plot
    plt.pie(values, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.savefig("pie.png")

if __name__ == "__main__":
    # read xlsx
    edges_info = xlrd.open_workbook("edges.xlsx")
    edges = edges_info.sheet_by_index(0)

    # mapping back to the node info
    node_raw = xlrd.open_workbook("nodes.xlsx")
    nodes = node_raw.sheet_by_index(0)

    # dict for (key, value) record
    out_degree = {}
    # threshold --> top 20 high risk node
    threshold = 20

    # do the counting
    for row in range(1, edges.nrows):
        cols = edges.row_values(row)
        # format
        # cols[0] = from node #, cols[1] = to node #, cols[2] = edge weight
        out_degree[cols[0]] = out_degree.get(cols[0], 0) + 1

    safe_node = []
    for index in range(1, nodes.nrows):
        if str(index) not in out_degree:
            safe_node.append(index)
    plot_pie(labels=['safe_node', 'risk_node'], values=[len(safe_node), nodes.nrows - len(safe_node)])
    #print('safe node portion: ', len(safe_node) / nodes.nrows)

    # sorting based on value
    sort_out_degree = sorted(out_degree.items(), key=operator.itemgetter(1), reverse=True)[:threshold]


    node_info = []
    for row in range(1, nodes.nrows):
        cols = nodes.row_values(row)
        node_info.append(cols[1:])
    print(node_info)

    high_risk_node = []
    for n, v in sort_out_degree:
        current = []
        current.extend(node_info[int(n)])
        current.append(v)
        high_risk_node.append(current)
    print(high_risk_node)
    # plot_high_risk([x[0] for x in high_risk_node], [x[2] for x in high_risk_node])


