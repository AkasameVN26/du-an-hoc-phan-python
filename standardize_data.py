
import pandas as pd
import os

def standardize_data(file_path, output_dir):
    """
    Standardizes the column names and removes unnecessary columns from a THPT dataset.

    Args:
        file_path (str): The path to the input CSV file.
        output_dir (str): The directory to save the cleaned CSV file.
    """
    df = pd.read_csv(file_path)
    
    # Standardize column names
    column_mapping = {
        'SBD': 'sbd',
        'Toan': 'toan',
        'NguVan': 'ngu_van',
        'VatLy': 'vat_ly',
        'HoaHoc': 'hoa_hoc',
        'SinhHoc': 'sinh_hoc',
        'LichSu': 'lich_su',
        'DiaLy': 'dia_ly',
        'GDCD': 'gdcd',
        'NgoaiNgu': 'ngoai_ngu',
        'Ngu_Van': 'ngu_van',
        'Ngoai_Ngu': 'ngoai_ngu',
        'Vat_Ly': 'vat_ly',
        'Hoa_Hoc': 'hoa_hoc',
        'Sinh_Hoc': 'sinh_hoc',
        'Lich_Su': 'lich_su',
        'Dia_Ly': 'dia_ly',
        'vat_li': 'vat_ly',
        'dia_li': 'dia_ly'
    }
    df.rename(columns=column_mapping, inplace=True)
    
    # Drop unnecessary columns
    columns_to_drop = ['MaMonNgoaiNgu', 'Cum_Thi', 'ma_ngoai_ngu']
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)
    
    # Ensure all column names are lowercase
    df.columns = [col.lower() for col in df.columns]

    # Reorder columns
    column_order = ['sbd', 'toan', 'ngu_van', 'vat_ly', 'hoa_hoc', 'sinh_hoc', 'lich_su', 'dia_ly', 'gdcd', 'ngoai_ngu']
    df = df[column_order]

    # Save the cleaned data
    file_name = os.path.basename(file_path)
    output_path = os.path.join(output_dir, file_name)
    df.to_csv(output_path, index=False)
    print(f"Standardized and saved {file_name} to {output_dir}")

if __name__ == "__main__":
    input_dir = "thpt-dataset"
    output_dir = "thpt-dataset-cleaned"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".csv"):
            file_path = os.path.join(input_dir, file_name)
            standardize_data(file_path, output_dir)
