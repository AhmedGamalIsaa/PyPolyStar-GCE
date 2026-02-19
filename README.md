# PyPolyStar-GCE

**Python package for polytropic stellar models and one-zone Galactic Chemical Evolution**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-pending-orange)](https://arxiv.org)  <!-- update later -->

## Overview
Open-source toolkit that:
- Solves the Lane-Emden equation (n = 0–5) with high accuracy
- Computes white-dwarf mass–radius relations (n=1.5) and density profiles
- Integrates custom stellar models into simple one-zone GCE for Milky-Way-like or dwarf galaxies

Perfect for courses in **Stellar Structure & Evolution**, **PDEs**, **Numerical Analysis**, and **Galactic & Extragalactic Astrophysics**.

## Features
- Numerical solver (`scipy.integrate.solve_ivp` + event termination)
- Analytic n=1 solution for validation
- White-dwarf M–R relation + comparison to observed objects
- Density/pressure/mass profiles
- One-zone GCE with customizable SFH, infall/outflow, and stellar-model-driven yields/lifetimes
- Reproducible Jupyter notebooks for every figure

## Installation
```bash
Add professional README
git clone https://github.com/yourusername/PyPolyStar-GCE.git
cd PyPolyStar-GCE
pip install -e .
