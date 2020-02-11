# BIT SHIFTING

## Exchange two values

```python
a ^= b
b ^= a
a ^= b
```

## Masking to 1

```js
    10010101
 OR 11110000
  = 11110101
```

## Masking to 0

```js
    10010101
AND 00001111
  = 00000101
```

## Querying bit

```js
    10011101
AND 00001000
  = 00001000
```

## Toggling bit

```js
    10011101
XOR 00001111
  = 10010010
```

## XOR

```js
x XOR 0000 = x
x XOR 1111 = ~x
x XOR x = 0
```

## AND

```js
x AND 0000 = 0
x AND 1111 = x
x AND x = x
```

## OR

```js
x OR 0000 = x
x OR 1111 = 1111
x OR x = x
```

## Set a bit

```js
a |= (1 << bit);
```

## Clear a bit

```js
a &= ~(1 << bit);
```

## Test that a bit is set

```js
a & (1 << bit);
```

## Multiplied by the m-th power of 2

```js
n << m;
```

## Divided by the m-th power of 2

```js
n >> m;
```

## Precedence

```js
~ (shifts) & ^ |
```
