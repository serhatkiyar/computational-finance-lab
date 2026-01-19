import numpy as np

class StrategyAnalyzer:
    """
    Trading stratejilerinin performansını ölçmek için kullanılan analiz sınıfı.
    """
    def __init__(self, equity_curve, trades=None, rf=0.0):
        self.equity_curve = np.array(equity_curve)
        self.trades = np.array(trades) if trades else np.array([])
        self.rf = rf
        self.returns = np.diff(self.equity_curve) / self.equity_curve[:-1]

    def cagr(self, periods_per_year=252):
        if len(self.equity_curve) < 2:
            return 0.0
        
        initial = self.equity_curve[0]
        final = self.equity_curve[-1]
        years = len(self.equity_curve) / periods_per_year
        
        return (final / initial) ** (1 / years) - 1

    def sharpe_ratio(self):
        excess_returns = self.returns - self.rf
        mean_excess = np.mean(excess_returns)
        std_excess = np.std(excess_returns, ddof=1)

        if std_excess == 0:
            return 0.0
        return mean_excess / std_excess

    def max_drawdown(self):
        peak = self.equity_curve[0]
        max_dd = 0.0

        for value in self.equity_curve:
            if value > peak:
                peak = value
            drawdown = (value - peak) / peak
            if drawdown < max_dd:
                max_dd = drawdown
        return max_dd

    def win_rate(self):
        if len(self.trades) == 0:
            return 0.0
        wins = self.trades[self.trades > 0]
        return len(wins) / len(self.trades)

    def profit_factor(self):
        gains = self.trades[self.trades > 0]
        losses = self.trades[self.trades < 0]
        
        total_loss = np.sum(losses)
        if total_loss == 0:
            return np.inf
        
        return np.sum(gains) / abs(total_loss)

    def get_performance_report(self):
        return {
            "CAGR": self.cagr(),
            "Sharpe Ratio": self.sharpe_ratio(),
            "Max Drawdown": self.max_drawdown(),
            "Win Rate": self.win_rate(),
            "Profit Factor": self.profit_factor()
        }