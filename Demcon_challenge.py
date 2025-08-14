import pandas as pd

def plan_and_schedule(acts_df):
    """
    Assigns each act to the lowest-numbered available stage and calculates the total stages needed.
    """
    # This list will track the time when each stage becomes free.
    # The index of the list corresponds to the stage number (e.g., index 0 is Stage 1).
    stage_free_times = []
    
    # This list will store the details for our final schedule.
    schedule_plan = []

    # Process each act one by one, in order of their start time.
    for act in acts_df.itertuples(index=False):
        found_a_stage = False
        # Find the first stage that is free before this act starts.
        for i, free_time in enumerate(stage_free_times):
            # A stage is free if the act starts at or after the time the stage is free.
            if act.start >= free_time:
                # Assign this act to the found stage (stage number is index + 1).
                stage_number = i + 1
                schedule_plan.append({
                    'Show': act.show, 
                    'Stage_Num': stage_number, 
                    'Start_time': act.start, 
                    'End_time': act.end
                })
                
                # Update the time this specific stage will become free again.
                stage_free_times[i] = act.end + 1
                found_a_stage = True
                break # Important: stop searching and move to the next act
        
        # If after checking all existing stages, none were free, we must open a new one.
        if not found_a_stage:
            # Add a new stage to our list. Its number will be the new length of the list.
            stage_number = len(stage_free_times) + 1
            stage_free_times.append(act.end + 1)
            schedule_plan.append({
                'Show': act.show, 
                'Stage_Num': stage_number, 
                'Start_time': act.start, 
                'End_time': act.end
            })

    # The total number of stages needed is the number of stages we had to open.
    total_stages = len(stage_free_times)
    schedule_plan.append({'Show': "Minimum number of stages required:", 'Stage_Num': total_stages})
    schedule_df = pd.DataFrame(schedule_plan)
    
    return total_stages, schedule_df


def acts_data():
    """
    This function reads the acts data from acts.csv and returns a DataFrame.
    """
    try:
        raw_acts = pd.read_csv("acts.csv", header=None)[0]
    except FileNotFoundError:
        print("Error: acts.csv not found. Please create it in the same directory.")
        return pd.DataFrame()

    acts = []
    for row in raw_acts:
        parts = row.split()
        if len(parts) == 3:
            acts.append({'show': parts[0], 'start': int(parts[1]), 'end': int(parts[2])})
        else:
            print(f"Warning: Skipping malformed row in acts.csv: '{row}'")

    if not acts:
        return pd.DataFrame()
        
    acts_df = pd.DataFrame(acts)
    acts_df.sort_values(by='start', inplace=True)
    return acts_df


if __name__ == "__main__":
    # Load data from acts.csv
    all_acts = acts_data()
    
    if not all_acts.empty:
        num_stages_needed, final_schedule = plan_and_schedule(all_acts)

        output_filename = "schedule.csv"
        final_schedule.to_csv(output_filename, index=False)
        
        print(f"Minimum number of stages required: {num_stages_needed}")
        print(f"Detailed schedule saved to: {output_filename}")