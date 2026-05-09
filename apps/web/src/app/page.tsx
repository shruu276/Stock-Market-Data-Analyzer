"use client";

import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  BarChart,
  Bar,
  Legend,
} from "recharts";
import { TrendingUp, TrendingDown, RefreshCw, Activity, DollarSign, BarChart2 } from "lucide-react";

export default function Home() {
  const [ticker, setTicker] = useState("AAPL");
  const [rows, setRows] = useState<any[]>([]);
  const [bt, setBt] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const API_URL = "http://localhost:8000";

  async function loadData() {
    setLoading(true);
    setError("");
    try {
      const r = await fetch(`${API_URL}/chart/${ticker}`);
      if (!r.ok) throw new Error("Failed to fetch data");
      const data = await r.json();
      setRows(data);
      // Reset backtest when changing ticker
      setBt(null);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function runBacktest() {
    setLoading(true);
    try {
      const r = await fetch(`${API_URL}/backtest/sma`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker }),
      });
      if (!r.ok) {
        const err = await r.json();
        throw new Error(err.detail || "Backtest failed");
      }
      const res = await r.json();
      setBt(res.stats);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadData();
  }, [ticker]);

  const latestPrice = rows.length > 0 ? rows[rows.length - 1].close : 0;
  const prevPrice = rows.length > 1 ? rows[rows.length - 2].close : 0;
  const priceChange = latestPrice - prevPrice;
  const priceChangePct = prevPrice ? (priceChange / prevPrice) * 100 : 0;
  const isPositive = priceChange >= 0;

  return (
    <div className="min-h-screen p-8 max-w-7xl mx-auto space-y-8">
      {/* Header */}
      <header className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 tracking-tight">
            QuantEdge Analyzer
          </h1>
          <p className="text-slate-400 mt-1">Institutional-grade market insights</p>
        </div>
        
        <div className="flex gap-3 items-center glass-panel p-2 rounded-xl">
          <input
            className="bg-slate-800/50 border border-slate-700 rounded-lg px-4 py-2 text-white outline-none focus:border-blue-500 transition-colors w-32 uppercase"
            value={ticker}
            onChange={(e) => setTicker(e.target.value.toUpperCase())}
            onKeyDown={(e) => e.key === "Enter" && loadData()}
            placeholder="AAPL"
          />
          <button
            className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors"
            onClick={loadData}
            title="Refresh Data"
          >
            <RefreshCw className={`w-5 h-5 ${loading ? "animate-spin" : ""}`} />
          </button>
          <button
            className="px-4 py-2 rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-medium shadow-lg shadow-blue-900/20 transition-all active:scale-95"
            onClick={runBacktest}
            disabled={loading}
          >
            Run Backtest
          </button>
        </div>
      </header>

      {error && (
        <div className="bg-red-500/10 border border-red-500/50 text-red-400 p-4 rounded-xl">
          {error}
        </div>
      )}

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="glass-panel p-6 rounded-2xl flex flex-col justify-between">
          <div className="flex justify-between items-start text-slate-400">
            <span className="font-medium text-sm">Latest Price ({ticker})</span>
            <DollarSign className="w-5 h-5" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold">${latestPrice.toFixed(2)}</span>
            <div className={`flex items-center gap-1 text-sm font-medium mt-2 ${isPositive ? 'text-emerald-400' : 'text-red-400'}`}>
              {isPositive ? <TrendingUp className="w-4 h-4" /> : <TrendingDown className="w-4 h-4" />}
              <span>{Math.abs(priceChange).toFixed(2)} ({Math.abs(priceChangePct).toFixed(2)}%)</span>
            </div>
          </div>
        </div>

        <div className="glass-panel p-6 rounded-2xl flex flex-col justify-between">
          <div className="flex justify-between items-start text-slate-400">
            <span className="font-medium text-sm">Volume</span>
            <BarChart2 className="w-5 h-5" />
          </div>
          <div className="mt-4">
            <span className="text-3xl font-bold">
              {rows.length > 0 ? (rows[rows.length - 1].volume / 1000000).toFixed(2) + "M" : "0"}
            </span>
            <div className="text-sm font-medium mt-2 text-slate-500">Daily traded shares</div>
          </div>
        </div>

        <div className="glass-panel p-6 rounded-2xl flex flex-col justify-between md:col-span-2 relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-r from-emerald-600/20 to-blue-600/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
          <div className="relative z-10 flex justify-between items-start text-slate-300">
            <div>
              <span className="font-medium text-sm flex items-center gap-2">
                <Activity className="w-4 h-4" /> Strategy Performance
              </span>
              <p className="text-xs text-slate-500 mt-1">SMA 20/50 Crossover Backtest</p>
            </div>
            {bt ? (
              <span className={`px-3 py-1 rounded-full text-xs font-bold ${bt.pnl >= 0 ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'}`}>
                {(bt.pnl * 100).toFixed(2)}% Net PnL
              </span>
            ) : (
              <span className="text-xs px-3 py-1 rounded-full bg-slate-800 text-slate-400">Not Run</span>
            )}
          </div>
          
          <div className="mt-4 grid grid-cols-3 gap-4 relative z-10">
            <div>
              <div className="text-xs text-slate-500 uppercase tracking-wider">Win Rate</div>
              <div className="text-lg font-bold mt-1 text-slate-200">{bt ? (bt.win_rate * 100).toFixed(1) + "%" : "—"}</div>
            </div>
            <div>
              <div className="text-xs text-slate-500 uppercase tracking-wider">Max Drawdown</div>
              <div className="text-lg font-bold mt-1 text-slate-200">{bt ? (bt.max_dd * 100).toFixed(1) + "%" : "—"}</div>
            </div>
            <div>
              <div className="text-xs text-slate-500 uppercase tracking-wider">Trades</div>
              <div className="text-lg font-bold mt-1 text-slate-200">{bt ? bt.trades : "—"}</div>
            </div>
          </div>
        </div>
      </div>

      {/* Main Chart */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-lg font-semibold flex items-center gap-2">
             Price & Moving Averages
          </h2>
          <div className="flex items-center gap-4 text-xs font-medium text-slate-400">
            <span className="flex items-center gap-1"><div className="w-3 h-3 rounded-full bg-blue-500" /> Close</span>
            <span className="flex items-center gap-1"><div className="w-3 h-3 rounded-full bg-emerald-500" /> SMA 20</span>
            <span className="flex items-center gap-1"><div className="w-3 h-3 rounded-full bg-purple-500" /> SMA 50</span>
          </div>
        </div>
        
        <div className="h-[400px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={rows} margin={{ top: 5, right: 0, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
              <XAxis 
                dataKey="date" 
                stroke="#64748b" 
                fontSize={12} 
                tickLine={false} 
                axisLine={false}
                minTickGap={30}
              />
              <YAxis 
                domain={['auto', 'auto']} 
                stroke="#64748b" 
                fontSize={12} 
                tickLine={false} 
                axisLine={false}
                tickFormatter={(value) => `$${value}`}
              />
              <Tooltip 
                contentStyle={{ backgroundColor: '#1e293b', border: '1px solid #334155', borderRadius: '8px', color: '#f8fafc' }}
                itemStyle={{ color: '#f8fafc' }}
              />
              <Line type="monotone" dataKey="close" stroke="#3b82f6" strokeWidth={2} dot={false} activeDot={{ r: 6, fill: "#3b82f6", stroke: "#0f172a", strokeWidth: 2 }} />
              <Line type="monotone" dataKey="sma20" stroke="#10b981" strokeWidth={1.5} dot={false} />
              <Line type="monotone" dataKey="sma50" stroke="#a855f7" strokeWidth={1.5} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* RSI Chart */}
      <div className="glass-panel p-6 rounded-2xl">
         <h2 className="text-lg font-semibold mb-6 flex items-center gap-2">
            Relative Strength Index (14)
          </h2>
          <div className="h-[200px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={rows} margin={{ top: 5, right: 0, left: 0, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                <XAxis dataKey="date" hide />
                <YAxis domain={[0, 100]} stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} ticks={[0, 30, 70, 100]} />
                <Tooltip contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '8px' }} />
                {/* Overbought/Oversold zones */}
                <rect x={0} y={30} width="100%" height={40} fill="rgba(59, 130, 246, 0.05)" />
                <Line type="monotone" dataKey="rsi14" stroke="#f59e0b" strokeWidth={1.5} dot={false} />
                {/* Lines for 30 and 70 */}
                <line x1="0" y1="70" x2="100%" y2="70" stroke="#ef4444" strokeDasharray="3 3" opacity={0.5} />
                <line x1="0" y1="30" x2="100%" y2="30" stroke="#10b981" strokeDasharray="3 3" opacity={0.5} />
              </LineChart>
            </ResponsiveContainer>
          </div>
      </div>
    </div>
  );
}
