# PyPolyStar-GCE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org) <!-- update after upload -->

**PyPolyStar-GCE** is an open-source Python package that provides a **numerical implementation of the stellar structure equations** (Lane-Emden + full 4-ODE solver) with direct application to **galactic chemical evolution**. Designed for undergraduate research and full reproducibility.

Developed as a capstone project spanning **Stellar Structure & Evolution**, **PDEs**, **Galactic & Extragalactic Astrophysics**, and **Numerical Analysis** (University of Science and Technology at Zewail City, 2026).

### Features
- Accurate Lane-Emden solver for polytropes n = 0 to 5 (matches standard textbook values to 6+ digits)
- Physical scaling to real stellar models (white dwarfs n=1.5, radiative stars n=3)
- Publication-quality plotting routines (Mass–Radius, density profiles, etc.)
- Ready-to-extend one-zone galactic chemical evolution module
- Zero external dependencies beyond NumPy/SciPy/Matplotlib

### Figure 1 (already included)
Mass–Radius relation for non-relativistic white dwarfs (n=1.5) with real observed points (Sirius B, 40 Eri B, etc.).

### Installation
```bash
git clone https://github.com/AhmedGamalIsaa/PyPolyStar-GCE.git
cd PyPolyStar-GCE
pip install -r requirements.txt
