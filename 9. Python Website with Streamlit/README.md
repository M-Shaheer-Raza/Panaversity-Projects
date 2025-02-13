# **Python Website with Streamlit - Simple Data Dashboard**  

## Description  
This project is a **simple data dashboard** built using **Streamlit**. It allows users to upload a **CSV file**, view its contents, filter data based on selected columns, and visualize the data using an **interactive line chart**.  

## Features  
- Upload and read CSV files  
- Display data preview (first 5 rows)  
- Show data summary (statistical insights)  
- Filter data based on a selected column and value  
- Generate an interactive **line chart** for visualizing data  

## Project Structure  
```
streamlit_dashboard_project
│── 📜 app.py                # Main Streamlit app
│── 📜 README.md             # Project documentation
```

## Installation & Setup  

### 1. Install Dependencies  
Before running the app, install the required Python libraries using:  

```bash
pip install streamlit pandas matplotlib
```

### 2. Run the Streamlit App  
Use the following command in the terminal:  

```bash
streamlit run app.py
```

## How to Use  

1. **Upload a CSV File**
- Click on **"Choose a CSV file"** to upload your dataset.  

2. **View Data Preview** 
- The first **five rows** of the dataset will be displayed.  

3. **Check Data Summary**  
- View **statistical summaries** like mean, median, min, max, etc.  

4. **Filter Data**
- Select a column and value to filter specific rows.  

5. **Generate Plot**  
- Choose **X-axis and Y-axis** columns and generate a **line chart**.  

## Technologies Used  
- **Python** 
- **Streamlit**  
- **Pandas**  
- **Matplotlib**