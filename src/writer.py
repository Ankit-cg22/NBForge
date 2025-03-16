import os 
def write_to_file(output_dir , file_name , file_content):
    os.makedirs(output_dir, exist_ok=True)
    os.path.join(output_dir, file_name)
    file_path = f"{output_dir}/{file_name}"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)
