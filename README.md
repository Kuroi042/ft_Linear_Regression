# ft_Linear_Regression
تعلم الالة
<img width="960" height="720" alt="image" src="https://blog.iqoption.com/wp-content/uploads/2020/01/math.jpg" />
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

## 2-Week Roadmap

### Week 1 — Foundation + Mandatory

| Day | Type | Focus | Key outcome |
|---|---|---|---|
| 1 | Theory | Math foundations | Understand Σ notation, slope, derivative intuition |
| 2 | Theory | Linear regression theory | Grasp hypothesis, MSE cost function, gradient descent |
| 3 | Theory | Deep-dive: update formulas | Derive tmpθ₀ and tmpθ₁ by hand for a 3-point dataset |
| 4 | Code | Program 1 — Predictor | `predict.py` working with hardcoded θ values |
| 5 | Code | Program 2 — Trainer skeleton | Gradient descent loop structure in `train.py` |
| 6 | Code | Feature normalization | Prevent divergence from mileage/price scale mismatch |
| 7 | Review | Integration + debugging | Both programs work end-to-end; loss converging |

### Week 2 — Polish + Bonus + Mastery

| Day | Type | Focus | Key outcome |
|---|---|---|---|
| 8 | Bonus | Data visualization | Scatter plot + regression line overlay |
| 9 | Bonus | Precision program | MSE and R² score implemented from scratch |
| 10 | Bonus | Loss curve + extras | Cost-per-iteration plot; convergence verified |
| 11 | Code | Bridge to computer vision | Connect regression to pseudo-landmark prediction |
| 12 | Review | Code cleanup | Peer-review-ready repo with README and comments |
| 13 | Review | Verbal understanding drill | Explain every design decision out loud |
| 14 | Review | Buffer + final submission | Edge case testing, clean clone test, git submission |

---

## Critical pitfalls

### 1. Feature normalization (Day 6) — the most common trap
The subject doesn't explicitly require it, but without it gradient descent will diverge. Mileage (~100,000) and price (~5,000) are on completely different scales.

```python
# Normalize before training
mean_x = sum(mileage) / m
std_x  = (sum((x - mean_x)**2 for x in mileage) / m) ** 0.5
mileage_norm = [(x - mean_x) / std_x for x in mileage]
```

Apply the same transformation to the user's input in `predict.py`.

### 2. Simultaneous update — do not use updated θ₀ to compute θ₁
```python
# WRONG
theta0 -= learning_rate * grad0
theta1 -= learning_rate * grad1  # grad1 now uses the updated theta0 — wrong

# CORRECT
tmp0 = learning_rate * grad0
tmp1 = learning_rate * grad1
theta0 -= tmp0
theta1 -= tmp1
```

### 3. What is `m`?
`m` is the number of rows in your dataset — the number of (mileage, price) pairs. The subject coyly says "I let you guess" — it's just `len(data)`.

---

## Peer review checklist

Your evaluator will verify:
- [ ] No libraries that do the regression for you (no `numpy.polyfit`, no `sklearn.linear_model`)
- [ ] Correct hypothesis: `estimatePrice = θ₀ + θ₁ × mileage`
- [ ] Correct training formulas: exactly as specified in the subject
- [ ] Simultaneous update of θ₀ and θ₁
- [ ] θ values saved to a file and loaded by the predictor

---

## Bonus targets

| Bonus | What to implement |
|---|---|
| Data plot | `matplotlib` scatter (mileage vs price) + regression line |
| Precision | MSE and R² score from scratch — no sklearn |
| Loss curve | Store cost per iteration, plot convergence |

Bonuses are only evaluated if the mandatory part is **perfect**.

---

## Bridge to computer vision (Leaffliction)

After completing this project, the connection to pseudo-landmark detection becomes clear:

- A **pseudo-landmark** is a predicted (x, y) coordinate on a plant image
- A **landmark predictor** is a regression model: `f(image_features) → (x, y)`
- Gradient descent is the same algorithm — just with more features and two output values
- Understanding θ₀, θ₁, and the update rule gives you the intuition for why neural networks train the way they do

---

## Recommended resources

| Resource | Use |
|---|---|
| [3Blue1Brown — Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) | Episodes 1–2 for derivative intuition (Day 1) |
| [Andrew Ng — ML Specialization Week 1](https://www.coursera.org/learn/machine-learning) | Gradient descent lectures (Day 2, free audit) |
| Subject PDF (`en_subject.pdf`) | Primary reference — re-read after Day 2 |

---

## Notes

- Language: Python (recommended for visualization ease)
- Forbidden: `numpy.polyfit`, any library that performs regression automatically
- Allowed: `pandas` for CSV reading, `matplotlib` for plotting, `numpy` for array math (as long as you implement the update rules yourself)
