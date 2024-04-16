# Data Visualization Class

## Overview

The Data Visualization Class is a Python class designed for visualizing data using various plots. It provides methods for generating different types of plots to visualize relationships and distributions in the data.

## Attributes

- None

## Methods

### create_heatmap

    The generate_heatmap function visualizes the correlation matrix of numeric features within a DataFrame. It utilizes Seaborn and Matplotlib to create a heatmap, where colors represent the strength and direction of correlations. The annotations display correlation coefficients, aiding in interpretation. This visualization aids in understanding relationships between features and identifying patterns in data.

### create_histogram

    The create_histogram method generates histogram plots for each numeric column in the DataFrame. Utilizing Seaborn's histplot function, it displays the distribution of values for each column. The overlay of a kernel density estimate aids in visualizing the distribution's shape. Each histogram is presented individually with the column name as the title, and axes labeled accordingly, offering insight into the data's distribution patterns.

### create_barplot

    The create_barplot function generates a bar plot using Seaborn to visualize the relationship between two variables in the DataFrame. It supports both basic and grouped bar plots based on the presence of the 'hue_label' parameter. The function sets the background style and figure size, then creates the appropriate type of bar plot using Seaborn's barplot. Depending on the presence of the 'hue_label' parameter, it either creates a basic bar plot or a grouped bar plot. Custom labels for the hue categories can be provided using the 'labels_hue' parameter. The plot's title, x-axis label, and y-axis label are set using the provided parameters. If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot. Finally, the function displays the plot using plt.show() and does not return any value.



### create_scatterplot

    The create_scatterplot function generates a scatter plot using Seaborn to visualize the relationship between two variables in the DataFrame. It supports both basic and grouped scatter plots based on the presence of the 'hue_label' parameter. The function sets the background style and figure size, then creates the appropriate type of scatter plot using Seaborn's scatterplot. Depending on the presence of the 'hue_label' parameter, it either creates a basic scatter plot or a grouped scatter plot. Custom labels for the hue categories can be provided using the 'labels_hue' parameter. The plot's title, x-axis label, and y-axis label are set using the provided parameters. If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot. Finally, the function displays the plot using plt.show() and does not return any value.

### create_boxplot


    The create_boxplot function generates a box plot using Seaborn to visualize the distribution of a numeric variable across different categories. It supports both basic and grouped box plots based on the presence of the 'hue_label' parameter. Depending on whether 'hue_label' is provided, it creates either a basic box plot or a grouped box plot using Seaborn's boxplot. Custom labels for the hue categories can be provided using the 'labels_hue' parameter. The plot's title, x-axis label, and y-axis label are set using the provided parameters. If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot. Finally, the function displays the plot using plt.show() and does not return any value.

### create_violinplot

    The create_violinplot function generates a violin plot using Seaborn to visualize the distribution of a numeric variable across different categories. It supports both basic and grouped violin plots based on the presence of the 'hue_label' parameter. Depending on whether 'hue_label' is provided, it creates either a basic violin plot or a grouped violin plot using Seaborn's violinplot. Custom labels for the hue categories can be provided using the 'labels_hue' parameter. The plot's title, x-axis label, and y-axis label are set using the provided parameters. If 'hue_label' is not None and 'labels_hue' is provided, a legend is added to the plot. Finally, the function displays the plot using plt.show() and does not return any value.

## Installation

    To install the Graph Module, simply clone this repository and ensure you have the required dependencies installed:

    ```bash
    git clone https://github.com/your_username/graph_module.git
    cd graph_module
    pip install -r requirements.txt


## Usage

    #import the necessary library
    from graph import DataVisualizer 

    #initializating the class datavisluizer
    dv = DataVisualizer(df)  #df is the pandas dataframe
