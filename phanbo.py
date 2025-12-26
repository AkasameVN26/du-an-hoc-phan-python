import pandas as pd
import matplotlib.pyplot as plt


ten_file_csv = 'thpt2024.csv'
ten_cac_mon = ['toan','ngu_van','vat_ly','hoa_hoc','sinh_hoc','lich_su','dia_ly','gdcd','ngoai_ngu']

try:
    df = pd.read_csv(ten_file_csv)
    print(f"Đọc file: {ten_file_csv}")
except Exception as e:
    print("Lỗi.")
    exit()

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(14, 10))

k = 0

for i in range(3):
    for j in range(3):
        ax = axes[i, j]
        mon_hoc = ten_cac_mon[k]
        
        if mon_hoc in df.columns:
            du_lieu_diem = df[mon_hoc].dropna()
            
            ax.hist(du_lieu_diem, bins=20, range=(0, 10),
                    alpha=0.7, 
                    edgecolor='grey')

            ax.set_title("Phân bố: {ten_mon}".format(ten_mon=mon_hoc))
            ax.set_xlim(0, 10)
            ax.set_xticks(range(0, 11))
            ax.set_yticks(range(0,180000,20000))
        else:
            ax.text(0.5, 0.5, f"Không tìm thấy cột:\n'{mon_hoc}'",
                    ha='center', va='center', color='red')
            ax.set_title(f'Lỗi')

        if i == 2:
            ax.set_xlabel('Điểm')
        
        if j == 0:
            ax.set_ylabel('Số lượng thí sinh')

        k += 1

fig.suptitle(f'Phân bố Phổ điểm 9 Môn (Dữ liệu: {ten_file_csv})', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
