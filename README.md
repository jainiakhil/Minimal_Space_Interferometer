# Space Interferometer Simulation (Historical Archive 2018–2021)

[![PASA Publication](https://img.shields.io/badge/PASA-10.1017%2Fpasa.2021.34-blue.svg)](https://doi.org/10.1017/pasa.2021.34)
[![arXiv](https://img.shields.io/badge/arXiv-2108.03113-b31b1b.svg)](https://doi.org/10.48550/arXiv.2108.03113)

This repository contains the software implementation for simulating a minimal space radio interferometer configuration in Low Earth Orbit (LEO).

---

## 📄 Associated Research & Documentation

- **Published Journal Paper (PASA)**: [A minimal space interferometer configuration for imaging at low radio frequencies](https://doi.org/10.1017/pasa.2021.34)  
  *Publications of the Astronomical Society of Australia (PASA), Volume 38, 2021, e038.*
- **arXiv Preprint**: [arXiv:2108.03113 [astro-ph.IM]](https://doi.org/10.48550/arXiv.2108.03113)
- **Project Report**: Included in this archive at [`docs/2014A3TS0295P.pdf`](docs/2014A3TS0295P.pdf).

---

## 📌 Project Overview

At ultra-low radio frequencies ($\lesssim 30\text{ MHz}$), ground-based radio astronomy is limited by ionospheric opacity and solar radiation. Space-based radio interferometers overcome these constraints.

This simulator models a 3-satellite (and 4-satellite) space interferometer constellation orbiting Earth. It calculates:
- **Satellite Orbital Dynamics**: Real-time 3D orbital propagation around Earth with axial tilt ($23.4^\circ$).
- **$u$-$v$ Baseline Coverage**: Baseline calculation across perpendicular orbital planes (equatorial and polar).
- **Weighting Schemes & Beam Patterns**: Uniform and natural $u$-$v$ weighting, dirty beam point-spread function (PSF) generation.
- **Solar & Ionospheric Avoidance**: Solar position modeling ($1\text{ AU}$) and baseline filtering outside ionospheric boundaries.

---

## 🌌 Physical System & Constellation Configuration

- **Earth**: Mass $5.972 \times 10^{24}\text{ kg}$, Radius $6371\text{ km}$, Axial Tilt $23.4^\circ$ along Y-axis.
- **Sun**: Sphere of radius $695,700\text{ km}$, Mass $1.989 \times 10^{30}\text{ kg}$, Distance $146.6 \times 10^6\text{ km}$ ($1\text{ AU}$).
- **Satellite Constellation**:
  - **Satellite 1** (`sat1`, red): Equatorial orbit (axis overlaps with Earth Y-axis).
  - **Satellite 2** (`sat2`, blue): Perpendicular polar orbit (axis along Z-axis).
  - **Satellite 3** (`sat3`, green): Perpendicular polar orbit (axis along X-axis).
  - **Field of View**: $180^\circ$ uniform hemisphere FOV for all satellites.
- **Default Satellite Altitudes (LEO)**:
  - `sat1`: $429\text{ km}$
  - `sat2`: $729\text{ km}$
  - `sat3`: $1029\text{ km}$

---

## ⚙️ Standard Operating Procedure & Parameters

The following parameters can be adjusted directly within the primary simulation scripts or updated interactively during runtime:

| Parameter | Description | Range / Units | Default Value |
| :--- | :--- | :--- | :--- |
| **Source Position (RA)** | Right Ascension of target radio source | $0\text{ to } 24\text{ h}$ (h, m, s) | `3h 0m 0s` |
| **Source Position (Dec)** | Declination of target radio source | $-90^\circ\text{ to }+90^\circ$ (deg, min, sec) | `45° 0' 0"` |
| **Source Distance** | Initial distance from Earth center | AU (Astronomical Units) | $10^9\text{ AU} \approx 15,800\text{ ly}$ |
| **Initial Satellite Phase** | Orbit starting phase (`satXphase`) | $0^\circ\text{ to } 360^\circ$ | `Sat1 = 0°`, `Sat2 = Sat3 = 90°` |
| **Satellite Heights** | Altitude above Earth (`satXdist`) | $400\text{ to } 2000\text{ km}$ (LEO) | `429`, `729`, `1029 km` |
| **Frame Step ($\Delta t$)** | Simulation step interval (`deltat`) | $1\text{ to } 10\text{ s}$ | `1 s` |
| **Graph Plot Interval** | Frequency of graph plotting (`Nt`) | $1\text{ to } \infty\text{ s}$ | `10 s` |
| **Max Runtime ($t_{max}$)** | Maximum system execution time | Seconds | $1,209,600\text{ s} \approx 2\text{ weeks}$ |

---

## 🖥️ Interactive GUI & System Controls

When running a primary script in VIDLE / VPython, three windows are presented:
1. **System of Satellites (Main Window)**: 3D visual representation of Earth, orbits, and source vectors on the left, with interactive control sliders and text inputs on the right.
2. **Real-time 3D Animation Window**: Displays real-time satellite positions. Can be hidden to maximize performance.
3. **$u$-$v$ Plot Window**: Displays live plotting of the $u$-$v$ visibility plane as baselines observe the target.

### Main Control Options:
- **Set Rate Slider**: Adjust frame rate ($1\text{--}5000\text{ frames/sec}$, default `500`).
- **Update Source Button**: Update target RA/Dec/Distance during execution to launch a new $u$-$v$ plot window.
- **Save u-v Plot Button**: Exports current $u$-$v$ plot in PDF format and saves `.npy` binary files (`u-v Array XXX.npy` & `Source Info XXX.npy`).
- **Plot Coverage Button**: Exports baseline coverage maps and dirty beam plots to PDF, printing cell filling percentage to the console.

---

## 📂 Output Folder Structure

Output files generated during simulation runs are organized into four standard folders:

- **`PDF Plots from Live Run/`**: Contains PDF $u$-$v$ plots and dirty beam figures exported during live interactive execution.
- **`Binary Files/`**: Stores raw `.npy` arrays containing $(u, v)$ baseline coordinates and target source metadata.
- **`EPS Plots from Binary/`**: Stores high-resolution vector EPS plots generated from `.npy` files via auxiliary scripts.
- **`Test Results from Live Run/`**: Logs of Python shell output detailing coverage percentages and runtime statistics.

---

## 📜 Auxiliary Binary Plotters

Post-processing scripts (named `test_Jan20_*_from_binary.py`) allow generating $u$-$v$ coverage, grid filling, and dirty beam plots directly from saved `.npy` binary files without needing to re-run the 3D orbital propagation:

1. Copy the target `.npy` file names (`Source Info XXX.npy` and `u-v Array XXX.npy`) into the auxiliary script variables.
2. Run the auxiliary script to output vector EPS/PDF figures and print exact grid coverage percentages.

---

## 📁 Repository File Index

```
github-export/
├── docs/
│   └── 2014A3TS0295P.pdf                           # Project Work Report
├── scripts/
│   # --- Primary Simulation Scripts (Feb 2021 Final Release) ---
│   ├── test_Feb21_with hermitian_uniform weighting_4_satellitees_v3_no_ionosphere_updated.py
│   ├── test_Feb21_with hermitian_uniform weighting_4_satellitees_v3_no_ionosphere_no_sun.py
│   ├── test_Feb21_with hermitian_uniform weighting_source_all_corrected_v3_no_ionosphere_coverage_plot.py
│   ├── test_Feb21_with hermitian_uniform weighting_source_all_corrected_v3_no_ionosphere_no_sun.py
│   # --- Auxiliary Offline Binary Plotter Scripts (Jan 2020) ---
│   ├── test_Jan20_4sat_plot_uv_from_binary.py
│   ├── test_Jan20_4sat_plot_uv_grid_and_dirty_beam_from_binary.py
│   ├── test_Jan20_for_Sun_plot_uv_from_binary.py
│   ├── test_Jan20_for_Sun_plot_uv_grid_and_dirty_beam_from_binary.py
│   ├── test_Jan20_plot_uv_from_binary.py
│   ├── test_Jan20_plot_uv_from_binary_out_of_ionosphere.py
│   ├── test_Jan20_plot_uv_grid_and_dirty_beam_from_binary.py
│   └── test_Jan20_plot_uv_grid_and_dirty_beam_from_binary_out_of_ionosphere.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚠️ Legacy Environment & Archival Notice

> **Note**: This repository is a historical code archive (2018–2021) preserved as-is.
> The simulation scripts were designed for Python 2.7 / 3.x using **VPython 6/7 (Visual module)**, **wxPython**, **NumPy**, **SciPy**, and **Matplotlib**. 
> Hardcoded local paths present in legacy script save statements reflect the original execution environment and can be adjusted if running in new environments.
