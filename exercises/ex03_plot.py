import marimo

__generated_with = "0.22.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # Exercise 3: Plotting Visualizations 📊

    **Plot Visuals!**

    **What you'll do:**

    - Create visualizations

    **Instructions:**

    - Complete each TODO section
    - Run cells to see your results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Your First Plot - Bar Chart
    """)
    return


@app.cell
def _():
    # TODO: Create a bar chart showing sales by category
    # Use plotly express (px.bar)
    # - x-axis: product_category
    # - y-axis: total sales
    # - Add a title
    # - Color the bars

    # Hint: Make sure category_sales is a valid dataframe first!
    import polars as pl
    import plotly.express as px
    # Create category_sales by grouping data
    # Load sales data
    sales = pl.read_json("data/raw/sales.json")

    # Sales by category
    category_sales = sales.group_by("product_category").agg(
        pl.sum("total_amount").alias("total_sales")
    )
    # Create bar chart
    ex_fig1 = px.bar(
        category_sales.to_pandas(),
        x="product_category",
        y="total_sales",
        title="Total Sales by Product Category",
        color="product_category",
    )
    ex_fig1.show()
    # Uncomment when ready:
    # ex_fig1.show()
    return category_sales, px, sales


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Line Chart - Sales Over Time
    """)
    return


@app.cell
def _(px, sales):
    # TODO: Create a line chart showing sales trends by month
    # Use px.line
    # - x-axis: month
    # - y-axis: total revenue
    # - Add markers to the line
    # - Add a title

    ex_fig2 = px.line(
        sales.to_pandas(),
        x="month",
        y="total_amount",
        title="Sales Trends by Month",
        markers=True,
    )
    ex_fig2.show()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Scatter Plot - Exploring Relationships
    """)
    return


@app.cell
def _(px, sales):
    # TODO: Create a scatter plot showing the relationship between
    # attendance_rate (x-axis) and test_score (y-axis)
    # - Color points by grade_level
    # - Add a trendline (trendline="ols")
    # - Add appropriate title and labels

    ex_fig3 = px.scatter(
        sales.to_pandas(),
        x="attendance_rate",
        y="test_score",
        color="grade_level",
        trendline="ols",
        title="Attendance Rate vs Test Score by Grade Level",
        labels={"attendance_rate": "Attendance Rate", "test_score": "Test Score"},
    )  
    ex_fig3.show()

    # Uncomment when ready:
    # ex_fig3.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Histogram - Distribution Analysis
    """)
    return


@app.cell
def _(px, sales):
    # TODO: Create a histogram of transaction amounts (total_amount)
    # - Use 30 bins
    # - Add a title
    # - Label the axes
    # - Try adding nbins=30 parameter

    ex_fig4 = px.histogram(
        sales.to_pandas(),
        x="total_amount",
        nbins=30,
        title="Distribution of Transaction Amounts",
        labels={"total_amount": "Transaction Amount"},
    )
    ex_fig4.show()

    # Uncomment when ready:
    # ex_fig4.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Advanced - Multiple Subplots
    """)
    return


@app.cell
def _(category_sales, px):
    # TODO: Create a dashboard with 2 subplots:
    # 1. Top plot: Bar chart of sales by category (reuse category_sales)
    # 2. Bottom plot: Bar chart of sales by region (reuse region_summary)

    # Hint: Use go.Figure() with make_subplots or add multiple traces
    # This is challenging - check the solution if you get stuck!

    ex_fig5 = px.bar(
        category_sales.to_pandas(),
        x="product_category",
        y="total_sales",
        title="Total Sales by Product Category",
        color="product_category",
    )
    ex_fig5.show()

    # Uncomment when ready:
    # ex_fig5.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the plotting exercises!

    **What you practiced:**

    - ✅ Bar charts
    - ✅ Line charts
    - ✅ Scatter plots
    - ✅ Histograms
    - ✅ Advanced: Subplots
    - ✅ Multiple chart types (bar, line, scatter, histogram)
    - ✅ Combining data analysis with visualization

    **What's next?**

    - Try creating your own visualizations with the data!

    **Pro Tips:**

    - Plotly charts are interactive - hover, zoom, pan!
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
