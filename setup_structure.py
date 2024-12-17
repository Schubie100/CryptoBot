import os

# Define the updated folder and file structure
folder_structure = {
    "crypto_bot": [
        {"01_MainProgram": [
            "01_fetch_data.py",
            "02_process_data.py",
            "03_apply_strategy.py",
            "04_optimize_strategy.py",
            "05_run_pipeline.py"
        ]},
        {"02_LiveTrading": [
            "01_fetch_live_data.py",
            "02_apply_strategy_live.py",
            "03_trade_execution.py",
            "04_monitor_performance.py"
        ]},
        {"03_Utils": [
            "indicators.py",
            "clustering.py",
            "gpt_trend_analysis.py"
        ]}
    ]
}

def create_structure(base_path, structure):
    """
    Recursively creates folders and files with ordered names.
    Adds a placeholder README file in folders to ensure proper structure.
    """
    for key, value in structure.items():
        folder_path = os.path.join(base_path, key)
        os.makedirs(folder_path, exist_ok=True)

        # Add a placeholder README file to each folder
        placeholder_file = os.path.join(folder_path, "00_README.md")
        with open(placeholder_file, 'w') as f:
            f.write(f"# {key} - Auto-generated folder\n")

        for item in value:
            if isinstance(item, dict):  # Nested folders
                create_structure(folder_path, item)
            else:  # Files
                file_path = os.path.join(folder_path, item)
                with open(file_path, 'w') as f:
                    f.write(f"# {item} - Auto-generated\n")

# Run the function
if __name__ == "__main__":
    create_structure(".", folder_structure)
    print("Folder structure has been updated successfully!")
