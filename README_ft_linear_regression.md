# ft_linear_regression — Learning Roadmap

A structured 2-week study plan to go from **complete ML beginner** to a working, peer-defensible implementation of linear regression with gradient descent, based on the 42 School `ft_linear_regression` subject (v4.1).

---

## Context

This roadmap was built for a student who:
- Is a **complete beginner in ML and math**
- Has **intermediate Python** experience (OpenCV, NumPy, Matplotlib)
- Has a **2-week deadline** with **5–6 hours/day** available
- Is using this project as a **bridge** back to a computer vision project (Leaffliction — specifically the pseudo-landmarks step in PlantCV)

---

## Project objective

Build two Python programs:

| Program | Role |
|---|---|
| `predict.py` | Reads saved θ values, prompts for mileage, returns estimated price |
| `train.py` | Reads `data.csv`, runs gradient descent, saves θ₀ and θ₁ |

**Hypothesis:** `estimatePrice(mileage) = θ₀ + (θ₁ × mileage)`

**Update rules (simultaneous):**
```
tmpθ₀ = learningRate × (1/m) × Σ (estimatePrice(mileage[i]) − price[i])
tmpθ₁ = learningRate × (1/m) × Σ (estimatePrice(mileage[i]) − price[i]) × mileage[i]
```
where `m` = number of training examples.

---


