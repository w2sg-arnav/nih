import pandas as pd

def format_csv_data(input_file):
    # Read the raw file
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Initialize lists to store the data
    data_rows = []
    current_record = {}
    
    print("Processing file...")
    
    for i, line in enumerate(lines):
        # Skip empty lines and braces
        line = line.strip()
        if not line or line in ['{', '}']:
            continue
            
        try:
            # Remove any trailing commas and quotes
            line = line.strip(',"')
            
            # Split on ":"
            if ':' in line:
                key, value = [x.strip('"') for x in line.split(':', 1)]
                print(f"Line {i}: Found key={key}, value={value}")  # Debug print
                
                # Store in current record
                current_record[key] = value
                
                # If we have all fields, add to data_rows
                if len(current_record) == 5:
                    print(f"Complete record found: {current_record}")  # Debug print
                    data_rows.append(current_record.copy())
                    current_record = {}
                    
        except Exception as e:
            print(f"Error processing line {i}: {line}")
            print(f"Error: {str(e)}")
            continue
    
    print(f"\nTotal records processed: {len(data_rows)}")
    
    if data_rows:
        # Create DataFrame
        df = pd.DataFrame(data_rows)
        
        # Ensure columns are in the desired order
        columns = ['gene', 'count', 'tissue', 'patient_id', 'file_id']
        df = df.reindex(columns=columns)
        
        return df
    else:
        print("No data was processed successfully!")
        return pd.DataFrame(columns=['gene', 'count', 'tissue', 'patient_id', 'file_id'])

# Use the function
try:
    print("Starting script...")
    df = format_csv_data(r"C:\Users\sonav\Documents\cerebellum_rnaseq_counts.csv")
    
    # Display first few rows to verify
    print("\nFirst few rows of formatted data:")
    print(df.head())
    
    # Display shape of DataFrame
    print("\nDataFrame shape:", df.shape)
    
    # Save to new CSV file
    output_path = r"C:\Users\sonav\Documents\formatted_cerebellum_counts.csv"
    df.to_csv(output_path, index=False)
    print(f"\nFormatted data saved to: {output_path}")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")