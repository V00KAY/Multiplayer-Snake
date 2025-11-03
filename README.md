# 🐍 Multiplayer Snake

A simple **two-player Snake game** written in Python using the `turtle` module.  
Each player controls their own snake, competing to collect apples and avoid collisions.

---

## 🎮 Controls

**Player 1**
- Move Up: `W`  
- Move Down: `S`  
- Move Left: `A`  
- Move Right: `D`

**Player 2**
- Move Up: `↑`  
- Move Down: `↓`  
- Move Left: `←`  
- Move Right: `→`

---

## 🧠 Rules

- Each player starts with **3 lives**.  
- Hitting a wall or your own body costs **one life**.  
- If your head hits any segment of the opponent’s snake, **you lose one life**, and the opponent **loses all body segments from the hit segment to the tail** (their score decreases accordingly).
- Eating an apple increases your **score** and adds one body segment.  
- The first player to reach **10 points** wins.  
- The game also ends if one player runs out of lives.

---

## ⚙️ Requirements

This game uses only the built-in **Python `turtle` module** —  
no extra dependencies are required.

✅ **Python 3.10+ recommended**

---

## 🚀 How to Run

1. Clone or download this repository  
2. Run python main.py
