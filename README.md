# Hi, I'm Amit Kumar Jha 👋

[![CRAN package](https://img.shields.io/badge/CRAN-CustomDerivative-276DC3?style=flat-square&logo=r)](https://cran.r-project.org/package=CustomDerivative)
[![External pull requests](https://img.shields.io/badge/GitHub-External%20Pull%20Requests-a855f7?style=flat-square&logo=github)](https://github.com/pulls?q=is%3Apr+author%3AAIM-IT4+-user%3AAIM-IT4)
[![Desk2Quant](https://img.shields.io/badge/Platform-Desk2Quant-00F2FE?style=flat-square&logo=vercel&logoColor=black)](https://desk2quant.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-akjha002-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/akjha002)
[![arXiv](https://img.shields.io/badge/arXiv-Research-B31B1B?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2512.03123)

> Quantitative risk modeller at UBS, former Reserve Bank of India research analyst, CRAN package maintainer and contributor to QuantLib.

My work sits at the intersection of derivatives pricing, counterparty credit risk, numerical methods, market microstructure and scientific computing. I primarily use Python, C++, R and kdb+/Q.

## 📦 Open-source impact

### QuantLib contributions

I contribute fixes and tests to [QuantLib](https://github.com/lballabio/QuantLib), a widely used open-source quantitative-finance library. Recent merged work includes:

- [Use dirty price in `CallableBond` effective duration and convexity](https://github.com/lballabio/QuantLib/pull/2671)
- [Add explanatory documentation to default-probability calculations](https://github.com/lballabio/QuantLib/pull/2670)
- [Clarify expected tranche-loss units](https://github.com/lballabio/QuantLib/pull/2672)
- [Prevent zero-BPS division in `FloatFloatSwap` fair-spread calculations](https://github.com/lballabio/QuantLib/pull/2678)
- [Add the 2026 South Korean Chuseok substitute holiday](https://github.com/lballabio/QuantLib/pull/2680)

These contributions include production C++ changes, regression tests, documentation corrections and responses to upstream maintainer review.

### CustomDerivative

[`CustomDerivative`](https://github.com/AIM-IT4/CustomDerivative) is an R package published on CRAN for transparent derivative-pricing and risk-analysis examples. Its current implemented scope includes:

- Black-Scholes-Merton pricing for European calls and puts
- continuous dividend yields
- extensible terminal-payoff functions
- Monte Carlo pricing with antithetic and control variates
- standard errors and confidence intervals
- geometric Brownian motion path simulation
- Asian and discretely monitored barrier payoff helpers
- finite-difference Greeks
- reproducible simulation, validation and cross-platform package checks

The package currently assumes a single underlying following risk-neutral geometric Brownian motion with constant parameters. Early exercise, stochastic volatility, jump diffusion and multi-asset correlation are outside the released model scope.

## 🚀 Selected projects

### [Advanced XVA Framework](https://github.com/AIM-IT4/Advanced-XVA-Framework)

Python framework exploring CVA, DVA, FVA, MVA, KVA, collateralised exposure, wrong-way risk and netting-set dynamics. It is a research and educational implementation, not a production valuation system.

### [Thermodynamic BSDE XVA Engine](https://github.com/AIM-IT4/Thermodynamic_BSDE_XVA_Engine)

Experimental research code combining nonlinear backward stochastic differential equations with ideas from stochastic thermodynamics and volatility-surface repair.

### [KDB Market Microstructure Study](https://github.com/AIM-IT4/KDB-Market-Microstructure-Study---Billion-Quote-Analysis)

kdb+/Q research implementation for high-frequency quote and trade analysis, including spreads, order-flow imbalance and inventory-risk diagnostics.

### [Quantitative Derivative Models](https://github.com/AIM-IT4/QuantitativeDerivativeModels)

Educational notebooks covering derivative-pricing models, lattice methods, finite differences, credit models and stochastic-process examples.

### [Desk2Quant](https://desk2quant.vercel.app)

A quantitative-finance education and mentorship platform with interactive resources, booking workflows and digital products.

## 🔬 Research

| Work | Area | Link |
|---|---|---|
| A Stochastic Thermodynamics Approach to Price Impact and Arbitrage | Market microstructure | [arXiv:2512.03123](https://arxiv.org/abs/2512.03123) |
| A Sinusoidal Hull-White Model for Interest Rate Dynamics | Interest-rate modelling | [arXiv:2506.06317](https://arxiv.org/abs/2506.06317) |
| Digitization Impact on Indian Banking Assets, 2009–2019 | Banking econometrics | [SSRN 4164875](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4164875) |

## 🏦 Professional background

- **UBS, Mumbai:** quantitative risk modelling across counterparty credit risk, exposure measures, securities-financing transactions, Repo VaR and risk-factor backtesting.
- **Reserve Bank of India:** research on market microstructure and large-scale tick data.
- **IIT Jodhpur:** M.Sc. in Digital Humanities, focused on computational economics and quantitative finance.
- **Jamia Millia Islamia:** B.Sc. (Hons.) in Physics.

## 🛠️ Technical focus

| Area | Tools and methods |
|---|---|
| Quantitative finance | XVA, PFE/EPE/EE, derivatives pricing, stochastic calculus, Monte Carlo, PDEs, interest-rate and credit models |
| Programming | Python, C++, R, kdb+/Q, SQL, Bash and LaTeX |
| Data and engineering | NumPy, SciPy, Pandas, PySpark, Databricks, QuantLib, PyTorch and Numba |
| Research | market microstructure, stochastic processes, numerical analysis and computational economics |

## 🎓 Community and education

I created [Desk2Quant](https://desk2quant.vercel.app) and provide quantitative-finance mentorship through [Topmate](https://topmate.io/amit_kumar_jha). This commercial and educational work is separate from the open-source maintenance evidence listed above.

## 📫 Contact

- [GitHub](https://github.com/AIM-IT4)
- [LinkedIn](https://www.linkedin.com/in/akjha002)
- [Email](mailto:jha.8@alumni.iitj.ac.in)
- [Desk2Quant](https://desk2quant.vercel.app)
