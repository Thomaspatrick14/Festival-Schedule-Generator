# 🎶 Festival Stage Planner

A Python script to solve the festival scheduling problem. This tool takes a list of performances with fixed start and end times and determines the **minimum number of stages** required to host all events without overlap. It also generates a detailed schedule assigning each act to a specific stage.

-----

## 📜 The Problem

Organizing a music festival with many acts on a tight schedule is a classic logistics challenge. Given a fixed timetable for dozens of acts, how do you determine the absolute minimum number of stages you need to build? This script answers that question by implementing an optimal greedy algorithm to create the most efficient schedule possible.

-----

## ✨ Features

  * **Optimal Stage Calculation:** Determines the exact minimum number of stages required.
  * **Detailed Scheduling:** Assigns each act to a specific, numbered stage.
  * **Efficient Re-use:** The scheduling logic always re-assigns acts to the lowest-numbered stage that is currently available.
  * **CSV Input:** Easily reads a list of acts from a simple `acts.csv` file.
  * **CSV Output:** Saves the complete, final schedule to a `schedule.csv` file for easy viewing and use.

-----

## 🚀 How to Use

### Prerequisites

You need Python (version 3.7 or newer) and the `pandas` library installed.

```bash
pip install pandas
```

### 1\. Prepare Your Input File

Create a file named `acts.csv` in the same directory as the script. The file should contain one act per line, with the show name, start time, and end time separated by spaces.

**`acts.csv` Example:**

```csv
show_1 29 33
show_2 2 9
show_3 44 47
show_4 26 30
show_5 15 20
show_6 8 15
```

### 2\. Run the Script

Execute the script from your terminal. Assuming you've named the file `scheduler.py`:

```bash
python scheduler.py
```

### 3\. Check the Output

The script will produce two outputs:

**A message in your console:**

```
Minimum number of stages required: 9
Detailed schedule saved to: schedule.csv
```

**A new file named `schedule.csv`:**
This file will contain the complete schedule with stage assignments.

**`schedule.csv` Example Output:**
| Show | Stage\_Num | Start\_time | End\_time |
| :--- | :--- | :--- | :--- |
| show\_9 | 1 | 1 | 9 |
| show\_11 | 2 | 1 | 4 |
| show\_2 | 3 | 2 | 9 |
| ... | ... | ... | ... |

-----

## 🧠 Algorithm Explained

The script uses a **greedy algorithm** to create the schedule. This approach is proven to be optimal for this type of problem.

1.  **Sort:** All acts are first sorted by their **start time**. This is the most crucial step.
2.  **Assign:** The script iterates through the sorted list of acts. For each act, it checks the existing stages to find one that is free.
3.  **Policy:** The policy for choosing a stage is to pick the one with the **lowest number** that is available (i.e., its last show has already finished).
4.  **Create:** If all existing stages are occupied at the required time, a new stage is created and added to the pool.
5.  **Result:** The final number of stages created is the calculated minimum required for the event.
