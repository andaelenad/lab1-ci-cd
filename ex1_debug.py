"""Run this with: python -i ex1_debug.py
then inspect variables manually."""

import re

def tokenize(expr):
    return re.findall(r'\d+|[+\-*()]', expr)

def parse_factor(tokens, pos):
    if tokens[pos] == '(':
        val, pos = parse_expr(tokens, pos + 1)
        return val, pos + 1
    return int(tokens[pos]), pos + 1

def parse_term(tokens, pos):
    left, pos = parse_factor(tokens, pos)
    if pos < len(tokens) and tokens[pos] == '*':
        right, pos = parse_term(tokens, pos + 1)
        return left * right, pos
    return left, pos

def parse_expr(tokens, pos):
    left, pos = parse_term(tokens, pos)
    if pos < len(tokens) and tokens[pos] in ('+', '-'):
        op = tokens[pos]
        right, pos = parse_expr(tokens, pos + 1)
        print(f"  parse_expr: {left} {op} {right}")
        if op == '+':
            return left + right, pos
        else:
            return left - right, pos
    return left, pos

def evaluate(expr):
    tokens = tokenize(expr)
    print(f"Tokens: {tokens}")
    result, _ = parse_expr(tokens, 0)
    return result

# Test the failing case
print("=== Debug 10 - 3 - 2 ===")
r = evaluate("10 - 3 - 2")
print(f"Result: {r} (expected 5)")
print()

# Test correct cases
for expr in ["2 + 3", "2 * 3 + 1", "(10 - 3) * 2"]:
    r = evaluate(expr)
    print(f"  {expr} = {r}")
    print()
