# 🧠 Project One: Minimum Palindrome Partitioning

## 📌 Problem Statement
Given a string `s`, the task is to partition it into the fewest number of palindromic substrings.  
Return the **minimum number of cuts** required to achieve this.

> A **palindrome** is a string that reads the same forwards and backwards.

---

## 💡 Example
**Input:** `"aab"`  
**Valid Palindrome Partitions:**
- `"a" | "a" | "b"` → 2 cuts  
- `"aa" | "b"` → ✅ **1 cut**

**Output:** `1` (Minimum cuts)

---

## 🧩 Solution Idea
The solution utilizes **Dynamic Programming (DP)** for efficiency.

### 1. Palindrome Table (`is_palindrome[i][j]`)
- A 2D boolean table to check if the substring `s[i..j]` is a palindrome.

### 2. DP Table (`dp[i]`)
- An array where `dp[i]` stores the **minimum number of cuts** needed for the substring `s[0..i]`.

---

## 🧮 Algorithm Steps

### Step 1: Build the `is_palindrome` Table
- `is_palindrome[i][j] = True` if `s[i..j]` is a palindrome.
- Logic:
  - A single character is always a palindrome.
  - Two identical characters side-by-side are a palindrome.
  - Longer substrings are palindromes if:
    - The outer characters match **AND**
    - The inner substring is also a palindrome.

### Step 2: Use the `dp` Array
- For each index `i`, check all possible previous positions `j`:
  - If `s[j+1..i]` is a palindrome:
    - Update `dp[i] = min(dp[i], dp[j] + 1)`
  - If the entire substring `s[0..i]` is a palindrome:
    - Set `dp[i] = 0` (no cuts needed)

---

## ⏱️ Time and Space Complexity
- **Time Complexity:** `O(n^2)`  
  (All substrings are checked to fill the tables)
- **Space Complexity:** `O(n^2)`  
  (To store the `is_palindrome` table and the `dp` array)

---

## ✅ Output
The program displays:
- The **minimum number of cuts**
- The **final palindrome partitions**
- The **DP table** and **Palindrome table** visually via the GUI

---

## 🛠️ Tools Used
- **Language:** Python
- **GUI Framework:** Tkinter
- **Features:**
  - Interactive string input
  - Visual display of DP and palindrome tables
  - Reset button for clearing inputs and results

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🔐 Project Two: Huffman Coding Compression Tool

## 📌 Problem Statement
Given a string `s`, compress it using **Huffman Coding** so that characters with higher frequency are assigned **shorter binary codes**.  
The goal is to minimize the total number of bits needed to represent the string.

---

## 💡 Example

**Input:** `"abacabad"`  
**Character Frequencies:**

**Generated Huffman Codes (example):**

**Encoded Output:** `0100110010111`  
**Decoded Output:** `abacabad`

---

## 🧩 Solution Overview

We apply a **Greedy Algorithm** using a **Huffman Tree** to assign binary codes based on character frequency.

### Steps:
1. **Count Frequency:** Count each character in the input string.
2. **Build Huffman Tree:** Use a priority queue (min-heap) to merge the two lowest-frequency nodes repeatedly.
3. **Generate Codes:** Assign binary codes by traversing the Huffman Tree:
   - `0` for left branch, `1` for right branch.
4. **Encode:** Replace each character in the input string with its corresponding binary code.
5. **Decode:** Use the tree and binary string to reconstruct the original input.

---

## 🧮 Algorithm Details

### Step 1: Count Frequencies
- Traverse the input and count how many times each character appears.

### Step 2: Build Huffman Tree
- Use a **min-heap** to always combine the two lowest-frequency nodes until one root remains.

### Step 3: Generate Huffman Codes
- Recursively traverse the tree and assign:
  - `0` for left branches
  - `1` for right branches

### Step 4: Encode the String
- Replace each character in the string with its binary Huffman code.

### Step 5: Decode the Binary
- Traverse the Huffman Tree using bits from the encoded string until a leaf (character) is reached.

---

## ⏱️ Time and Space Complexity

### Time Complexity:
- **Frequency Count:** `O(n)`  
- **Build Heap:** `O(k log k)` where `k` = number of unique characters  
- **Tree Construction + Code Generation:** `O(k)`  
- **Encoding:** `O(n)`  
**➡ Total:** `O(n + k log k)`

### Space Complexity:
- `O(k)` for the Huffman code map  
- `O(n)` for the encoded binary string  
- `O(k)` for the min-heap and tree nodes

---

## ✅ Output

- ✅ **Huffman Encoded Binary String**  
- ✅ **Character-to-Code Table**  
- ✅ **Decoded Output** (should match original input)  
- ✅ **Optional Huffman Tree Visualization**

---

## 🛠️ Tools Used

- **Languages:** HTML, CSS, JavaScript  
- **Visualization:** [D3.js](https://d3js.org/) for displaying the Huffman Tree  
- **UI Elements:**
  - Textarea input for the original string
  - Buttons for Compress and Decompress
  - Output sections for codes, encoded string, and decoded result

---
