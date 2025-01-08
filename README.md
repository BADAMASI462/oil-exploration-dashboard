# Oil Exploration Dashboard: Power BI Mock Project

This project demonstrates the use of Python to simulate a dataset and create visualizations that can be further utilized in Power BI to design interactive dashboards. The focus is on oil exploration trends, success rates, and cost efficiency.

## Key Features

- **Simulated Dataset**: The script generates a dataset with fields such as exploration costs, barrels produced, and success rates for multiple fields.
- **Data Visualizations**:
  - Bar Chart: Highlights success rates by field.
  - Scatter Plot: Explores the relationship between costs and barrels produced.
  - Heatmap: Shows correlations between various metrics.
- **Export to CSV**: The simulated dataset is saved as a CSV file for integration into Power BI.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/oil-exploration-dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd oil-exploration-dashboard
   ```
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
4. Run the script:
   ```bash
   python script.py
   ```
5. Locate the generated CSV file (`mock_oil_exploration_data.csv`) in the project directory.
6. Import the CSV file into Power BI and use it to create an interactive dashboard.

## Power BI Dashboard Example
Use the dataset to design a dashboard with the following elements:

- **Bar Chart**: Success rates for each field.
- **Scatter Plot**: Visualize costs vs. barrels produced.
- **KPI Metrics**: Display average success rates, total costs, and barrels produced.
- **Interactive Filters**: Enable filtering by fields or success rates.

## Repository Structure

```
|-- script.py                # Python script for data generation and visualization
|-- mock_oil_exploration_data.csv  # Simulated dataset for Power BI
|-- README.md                # Project documentation
```

## Dependencies

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Future Improvements

- Expand the dataset with additional metrics like environmental impact and revenue.
- Integrate real-world data from public APIs.
- Build and share the Power BI dashboard file (.pbix).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

---

Feel free to explore the dataset, enhance the visuals, and share your insights!

