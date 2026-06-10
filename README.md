# Scenario D: Smart Power Grid Anomaly Detection

This project detects residential zones whose power consumption exceeds an industrial baseline.

## Dataset
Household Power Consumption dataset was used. A sample CSV file was placed inside the `input_stream` folder.

## How to Run
```bash
python stream_processing.py

A sliding window with watermarking was used to analyze power consumption data in near real time. The sliding window was chosen because it continuously monitors overlapping time periods and allows faster anomaly detection. Watermarking handles late arriving records while maintaining state efficiently. The pipeline requires state because Spark stores aggregation information for active windows. An alert is triggered whenever the average residential power consumption exceeds the industrial baseline.
