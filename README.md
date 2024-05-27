# Adafruit CSV to JSON Processor

This Python script processes CSV files containing hexadecimal encoded JSON strings, converts them into readable JSON files, and saves each record as a separate JSON file.

It is meant to be used with the myoware-simulation software after establishing a connection with the LightBlue BLE testing environment and creating some simulated events using the toggle switch 'myoware-simulation-ble-dataLite.ino' software

## Requirements
- Python 3.x
- pandas library

## Setup and Run the Script

1. Ensure Python 3.x is installed on your system.
2. Install pandas if it is not already installed:
   ```bash
   pip3 install pandas
3. Install json if not already intalled:
   ```bash
   pip3 install json
4. Edit lines 55 and 56 of the script to be the correct file path on your computer.
5. Put the Adafruit IO CSV file from the LightBlueArduino data feed into the input folder.
6. Rename the csv file 'input.csv'
7. Go to your terminal
8. Run the following command in a fresh terminal window:
   ```bash
   python3 <insert file path to where you saved the script on your local machine>adafruitParser.py
9. The files will save to the file path you specified in step 4.
