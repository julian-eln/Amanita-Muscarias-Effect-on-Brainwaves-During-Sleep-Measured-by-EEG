import pandas as pd
import numpy as np
from scipy.signal import welch, detrend
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# --- SETTINGS ---
FS = 215.34 
ARTIFACT_THRESHOLD = 5000 
# ----------------

# 1. Load and Clean
file_path = r'C:\Users\julia\Downloads\Treatment_MindMonitor (1).csv'
df = pd.read_csv(file_path)
eeg_cols = ['TP9', 'AF7', 'AF8', 'TP10']
df = df.dropna(subset=eeg_cols).reset_index(drop=True)

# 2. Configuration
epoch_samples = int(4 * FS)
start_time = df['TimeStamp'].min()
df['Time_Min'] = (df['TimeStamp'] - start_time) / 60.0
df['Window_5Min'] = (df['Time_Min'] // 5).astype(int)
unique_windows = sorted(df['Window_5Min'].unique())

bands = {
    'Delta': (1.0, 4.0), 'Theta': (4.0, 8.0), 'Alpha': (8.0, 12.0),
    'Sigma': (12.0, 15.0), 'Beta': (15.0, 30.0), 'Gamma': (30.0, 45.0)
}

coords = {
    'TP9':  (-0.8, -0.2), 
    'AF7':  (-0.4, 0.8), 
    'AF8':  (0.4, 0.8), 
    'TP10': (0.8, -0.2)
}

# 3. Calculation
# Store both 'db' (absolute) and 'rel' (relative ratio)
results = {band: {'db': {}, 'rel': {}} for band in bands}

for w in unique_windows:
    w_data = df[df['Window_5Min'] == w][eeg_cols].values
    num_epochs = len(w_data) // epoch_samples
    if num_epochs == 0: continue
    
    epoch_results = []
    for e in range(num_epochs):
        epoch = detrend(w_data[e*epoch_samples : (e+1)*epoch_samples], axis=0)
        if np.max(np.ptp(epoch, axis=0)) > ARTIFACT_THRESHOLD: continue 
        
        freqs, psd = welch(epoch, fs=FS, nperseg=int(epoch_samples // 2), axis=0)
        df_freq = freqs[1] - freqs[0]
        
        # Absolute Power (Linear scale first)
        b_pwr_lin = {b: np.sum(psd[(freqs >= f_min) & (freqs <= f_max), :], axis=0) * df_freq for b, (f_min, f_max) in bands.items()}
        total_pwr = sum(b_pwr_lin.values())
        
        # Store as both dB and Relative
        epoch_results.append({
            'db': {b: 10 * np.log10(p + 1e-9) for b, p in b_pwr_lin.items()},
            'rel': {b: p / (total_pwr + 1e-9) for b, p in b_pwr_lin.items()}
        })
    
    if epoch_results:
        for b in bands:
            results[b]['db'][w] = np.mean([ep['db'][b] for ep in epoch_results], axis=0)
            results[b]['rel'][w] = np.mean([ep['rel'][b] for ep in epoch_results], axis=0)

# 4. Visualization Loop
x, y = [coords[c][0] for c in eeg_cols], [coords[c][1] for c in eeg_cols]
grid_x, grid_y = np.mgrid[-1.2:1.2:100j, -1.2:1.2:100j]
mask = (grid_x**2 + grid_y**2) > 1

# Plotting function
def plot_topo(data_dict, title_prefix, cbar_label):
    valid_windows = sorted(data_dict.keys())
    all_z = np.vstack(list(data_dict.values()))
    vmin, vmax = np.min(all_z), np.max(all_z)
    
    num_plots = len(valid_windows)
    rows = math.ceil(num_plots / 5)
    fig, axes = plt.subplots(rows, 5, figsize=(20, 4*rows))
    axes = np.atleast_1d(axes).flatten()
    
    for idx, w in enumerate(valid_windows):
        ax = axes[idx]
        z = data_dict[w]
        rbfi = Rbf(x, y, z, function='linear')
        grid_z = rbfi(grid_x, grid_y)
        grid_z[mask] = np.nan
        
        contour = ax.contourf(grid_x, grid_y, grid_z, levels=20, cmap='viridis', vmin=vmin, vmax=vmax)
        
        # Clinical Elements
        ax.add_patch(patches.Circle((0, 0), radius=1, fill=False, lw=2, color='black'))
        ax.plot([-0.1, 0, 0.1], [1, 1.1, 1], color='black', lw=2)
        ax.add_patch(patches.Ellipse((-1, 0), 0.1, 0.3, fill=False, lw=2, color='black'))
        ax.add_patch(patches.Ellipse((1, 0), 0.1, 0.3, fill=False, lw=2, color='black'))
        
        for ch in eeg_cols:
            ax.plot(coords[ch][0], coords[ch][1], 'ro', markersize=6, zorder=5)
            ax.text(coords[ch][0]+0.05, coords[ch][1]+0.05, ch, fontsize=9, fontweight='bold', zorder=6)
            
        ax.set_title(f"{w*5}-{w*5+5} min")
        ax.axis('off')
        
    for idx in range(num_plots, len(axes)): axes[idx].axis('off')
    
    fig.subplots_adjust(right=0.9)
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    fig.colorbar(contour, cax=cbar_ax, label=cbar_label)
    plt.suptitle(f'{title_prefix}', fontsize=16)
    plt.show()

# Generate Plots
for band_name in bands.keys():
    if results[band_name]['db']:
        plot_topo(results[band_name]['db'], f'{band_name} Absolute Power (dB)', 'Power (dB)')
        plot_topo(results[band_name]['rel'], f'{band_name} Relative Power (Ratio)', 'Relative Power')
