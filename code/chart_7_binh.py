import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
file_path = r'D:\CODE\CMC\du-an-hoc-phan-python\thpt-dataset-cleaned\thpt2024.csv'
df = pd.read_csv(file_path)

# Define subject groups with Vietnamese names for display
natural_sciences = ['toan', 'vat_ly', 'hoa_hoc', 'sinh_hoc', 'ngoai_ngu']
social_sciences = ['ngu_van', 'lich_su', 'dia_ly', 'gdcd', 'ngoai_ngu']

# Create a mapping for better labels
label_mapping = {
    'toan': 'Toán',
    'vat_ly': 'Vật lý',
    'hoa_hoc': 'Hóa học',
    'sinh_hoc': 'Sinh học',
    'ngoai_ngu': 'Ngoại ngữ',
    'ngu_van': 'Ngữ văn',
    'lich_su': 'Lịch sử',
    'dia_ly': 'Địa lý',
    'gdcd': 'GDCD'
}

# --- Enhanced Interactive Plot for Natural Sciences ---
print("Đang chuẩn bị biểu đồ tương tác cho khối Khoa học Tự nhiên...")

# Create the interactive scatter matrix with color gradient based on mean score
df['mean_score_natural'] = df[natural_sciences].mean(axis=1)

fig_khtn = px.scatter_matrix(
    df,
    dimensions=natural_sciences,
    color='mean_score_natural',
    color_continuous_scale='Viridis',  # Modern color scheme
    title='<b>Ma trận Tương quan - Khối Khoa học Tự nhiên & Ngoại ngữ</b>',
    labels=label_mapping,
    opacity=0.6,  # Add transparency to see overlapping points
    height=1000,
    width=1400
)

# Update layout for better aesthetics
fig_khtn.update_layout(
    title={
        'text': '<b>Ma trận Tương quan - Khối Khoa học Tự nhiên & Ngoại ngữ</b>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'family': 'Arial Black'}
    },
    hovermode='closest',
    coloraxis_colorbar={
        'title': 'Điểm TB',
        'thicknessmode': 'pixels',
        'thickness': 15,
        'lenmode': 'pixels',
        'len': 300,
        'yanchor': 'middle',
        'y': 0.5
    },
    font=dict(size=11, family='Arial'),
    plot_bgcolor='rgba(240, 240, 245, 0.5)',  # Light background
    paper_bgcolor='white',
    margin=dict(l=50, r=50, t=80, b=50)
)

# Update trace properties for better visuals
fig_khtn.update_traces(
    diagonal_visible=True,
    showupperhalf=True,
    marker=dict(
        size=3,
        line=dict(width=0),  # Remove marker borders for cleaner look
    )
)

# Customize axes
fig_khtn.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')
fig_khtn.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')

fig_khtn.show()


# --- Enhanced Interactive Plot for Social Sciences ---
print("\nĐang chuẩn bị biểu đồ tương tác cho khối Khoa học Xã hội...")

# Create the interactive scatter matrix with color gradient
df['mean_score_social'] = df[social_sciences].mean(axis=1)

fig_khxh = px.scatter_matrix(
    df,
    dimensions=social_sciences,
    color='mean_score_social',
    color_continuous_scale='Plasma',  # Different color scheme for distinction
    title='<b>Ma trận Tương quan - Khối Khoa học Xã hội & Ngoại ngữ</b>',
    labels=label_mapping,
    opacity=0.6,
    height=1000,
    width=1400
)

# Update layout
fig_khxh.update_layout(
    title={
        'text': '<b>Ma trận Tương quan - Khối Khoa học Xã hội & Ngoại ngữ</b>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'family': 'Arial Black'}
    },
    hovermode='closest',
    coloraxis_colorbar={
        'title': 'Điểm TB',
        'thicknessmode': 'pixels',
        'thickness': 15,
        'lenmode': 'pixels',
        'len': 300,
        'yanchor': 'middle',
        'y': 0.5
    },
    font=dict(size=11, family='Arial'),
    plot_bgcolor='rgba(240, 240, 245, 0.5)',
    paper_bgcolor='white',
    margin=dict(l=50, r=50, t=80, b=50)
)

# Update trace properties
fig_khxh.update_traces(
    diagonal_visible=True,
    showupperhalf=True,
    marker=dict(
        size=3,
        line=dict(width=0),
    )
)

# Customize axes
fig_khxh.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')
fig_khxh.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')

fig_khxh.show()

print("\n✓ Đã hoàn thành.")