# Mejoras de la Calculadora Científica/Física

## Cambios Implementados

### 1. **Soporte para Números Negativos**
- ✅ El botón `±` ahora funciona de manera inteligente:
  - Si la expresión está vacía, agrega un signo negativo
  - Si hay un número completo, cambia su signo
  - Si estás en medio de una expresión, busca el último número y cambia su signo
  - Permite agregar números negativos con paréntesis: `(-`

- ✅ El operador `-` ahora se puede usar al inicio o después de operadores para números negativos
  - Ejemplos: `-5`, `3×(-2)`, `5+(-3)`

### 2. **Operador de Potencia `^`**
- ✅ Agregado el botón `^` en el modo básico (fila inferior)
- ✅ Funciona tanto en modo básico como científico
- ✅ Permite elevar cualquier número a cualquier potencia
  - Ejemplos: `2^3 = 8`, `5^2 = 25`, `(-2)^3 = -8`, `2^(-1) = 0.5`

### 3. **Mejoras para Cálculos Científicos/Físicos**
- ✅ Soporte completo para paréntesis `()` en modo básico
- ✅ Botón `ANS` en modo básico para usar el resultado anterior
- ✅ Multiplicación implícita: `2(3)` se interpreta como `2×3`
- ✅ Constantes matemáticas mejoradas: `π` y `e`
- ✅ Manejo inteligente de notación científica (no confunde `e` en `1e5` con la constante `e`)

### 4. **Atajos de Teclado**
- ✅ Tecla `^` del teclado ahora funciona para potencias
- ✅ Todos los operadores básicos funcionan desde el teclado
- ✅ Paréntesis `()` funcionan desde el teclado

## Ejemplos de Uso

### Números Negativos:
```
-5 + 3 = -2
(-2) × 3 = -6
5 + (-3) = 2
(-5)^2 = 25
```

### Potencias:
```
2^3 = 8
10^2 = 100
2^(-1) = 0.5
(-2)^3 = -8
5^0.5 = 2.236... (raíz cuadrada)
```

### Cálculos Físicos:
```
9.8 × (-2) = -19.6
(5 + 3)^2 = 64
2π × 5 = 31.415...
e^2 = 7.389...
(-9.8) × 2 + 5 = -14.6
```

## Distribución de Botones (Modo Básico)

```
┌─────┬─────┬─────┬─────┐
│  C  │  ⌫  │  %  │  /  │
├─────┼─────┼─────┼─────┤
│  7  │  8  │  9  │  ×  │
├─────┼─────┼─────┼─────┤
│  4  │  5  │  6  │  -  │
├─────┼─────┼─────┼─────┤
│  1  │  2  │  3  │  +  │
├─────┼─────┼─────┼─────┤
│  (  │  0  │  .  │  )  │
├─────┼─────┼─────┼─────┤
│  ±  │  ^  │ ANS │  =  │
└─────┴─────┴─────┴─────┘
```

## Notas Técnicas
- La evaluación de expresiones ahora maneja correctamente números negativos en cualquier posición
- El operador `^` se convierte internamente a `**` para Python
- La función `evaluar_expresion()` ahora usa regex para manejar casos especiales
- Soporte mejorado para constantes matemáticas sin conflictos con notación científica
