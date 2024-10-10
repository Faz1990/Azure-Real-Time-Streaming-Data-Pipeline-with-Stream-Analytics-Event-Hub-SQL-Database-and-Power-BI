# Building-a-Real-Time-Data-Pipeline-with-Azure-Event-Hub-Stream-Analytics-and-Power-BI

## Project Description

This project demonstrates the creation of a **real-time streaming data pipeline** using **Azure Stream Analytics**, **Azure Event Hub**, and **Azure SQL Database**. It aims to build a robust, scalable pipeline integrating both real-time and batch processing. The pipeline is designed to ingest, process, and store data from sources such as **transportation**, **geolocation**, and **user data**. **Azure Event Hub** and **Azure Stream Analytics** are used for event streaming, while **Azure SQL Database** handles persistent storage.

## Architecture Diagram

![Azure Data Pipeline Architecture](Architecture.Avif)

## Table of Contents
1. [Project Description](#project-description)
2. [Batch Processing](#batch-processing)
3. [Stream Processing](#stream-processing)
4. [Technologies Used](#technologies-used)
5. [Usage](#usage)
6. [File Structure](#file-structure)
7. [What I Learned](#what-i-learned)
8. [Improvements (If I Had More Time)](#improvements-if-i-had-more-time)
9. [License](#license)

## Batch Processing

The batch processing component of the pipeline involves setting up **Azure Stream Analytics** to process data from **Azure Event Hub** and write it to **Azure SQL Database**. **API Gateway** acts as the entry point for receiving data, which is then streamed into Event Hub. **Azure Stream Analytics** jobs process the data, applying necessary transformations, and write the results into SQL tables for analysis and reporting.

## Stream Processing

In the real-time streaming component, **Azure Stream Analytics** is used to process live data from **Azure Event Hub**. The data is transformed and analyzed in real-time before being stored in **Azure SQL Database**. This allows for immediate insights and supports continuous data flow for dynamic analysis.

## Technologies Used

- **Azure Event Hub**: A scalable data streaming platform for real-time data ingestion.
- **Azure Stream Analytics**: A managed real-time analytics service that processes streaming data.
- **Azure SQL Database**: A relational database for storing processed data.
- **Azure API Gateway**: Exposes APIs for data flow management.
- **Python**: Used for scripting the ingestion of data into Azure Event Hub.
- **Power BI**: Visualizes data stored in Azure SQL Database for insights.

## Usage

### Data Ingestion
- **Event Hub** receives data from various sources, which is then processed by **Azure Stream Analytics**.

### Data Transformation
- Real-time data streams undergo transformation and aggregation in **Azure Stream Analytics** before being written to **SQL tables**.

### Data Storage
- Transformed data is stored in **Azure SQL Database** for further analysis.

### Execution
- **Real-time data streaming** is handled by **Azure Stream Analytics**, while **Power BI** visualizes the processed data.

## File Structure

```
azure-streaming-data-pipeline/
├── .gitignore
├── 0ec6d756577b_dag.py                      # Airflow DAG for batch processing
├── Streaming_Job_Setup_2024-09-23.ipynb      # Jupyter Notebook for Stream Analytics setup
├── Azure_SQL_Connection_Setup_2024-08-27.ipynb # Jupyter Notebook for SQL and Power BI integration
├── Azure_Data_Pipeline_Architecture.png      # Cloud architecture diagram
├── README.md                                # Documentation
├── data_ingestion_script.py                 # Script for ingesting data into Event Hub
├── stream_processing_script.py              # Script for streaming data processing
```

## What I Learned

- **Real-time stream processing**: Gained proficiency in handling real-time data streams using **Azure Event Hub** and **Azure Stream Analytics**.
- **Batch processing**: Developed skills in batch processing workflows using **Azure Stream Analytics**.
- **Data transformation**: Learned how to perform large-scale data transformations using **SQL** and **Stream Analytics**.
- **Azure Integration**: Gained hands-on experience integrating various **Azure services** (Event Hub, Stream Analytics, SQL Database) into a unified data pipeline.
- **Big Data management**: Developed an understanding of how to process, clean, and store large datasets in **Azure SQL Database** for real-time and batch processing use cases.

## Improvements (If I Had More Time)

- **Performance Tuning**: Optimize streaming and analytics jobs for higher efficiency.
- **Security Enhancements**: Implement better security practices, such as encrypting data in transit and at rest, and using **Azure Managed Identities** for restricted access.
- **Monitoring & Alerts**: Add more comprehensive monitoring and alerting mechanisms using **Azure Monitor** and **Log Analytics**.
- **Cost Optimization**: Introduce cost-saving mechanisms, such as using **Azure Functions** for event-driven data processing where appropriate.
- **Enhanced Data Quality Checks**: Implement more rigorous data validation and anomaly detection mechanisms within the data pipeline to ensure higher data accuracy.

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute the code as per the terms of the license.
