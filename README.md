# ft_Linear_Regression
تعلم الالة
<img width="960" height="720" alt="image" src="https://blog.iqoption.com/wp-content/uploads/2020/01/math.jpg" />
# ft_linear_regression



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


