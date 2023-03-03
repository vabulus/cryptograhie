# Kryptografie Tools
## ElGamal 
### Angabe 
$p=5, b=2 (geheimer Schlüssel), a=2 (Zufallszahl)$

$G=(1,1), M=(2,2), y^{2}= x^{3}-4x +4, k=-4, w=3$

### Gesucht:
$C=(R,S), Y, Entschlüsseln$

$Y = b * G = 2 * (1_{x1},1_{y1}) = (x_{3}, y_{3})$

### Rechnungen  
**Berechnung des vollständig öffentlichen Schlüssels bzw. von $Y$**

$Y = b * G = 2 * (1_{x1},1_{y1}) = (x_{3}, y_{3})$

$\lambda = \frac{3*1^{2}-4}{2*1}=-\frac{1}{2}=2$

$x_{3}=2^2-2*1=2$

$y_{3}=2*(1-2)-1=-3 = 2$

**Ergebnis**: $Y = b * G = 2 * (1_{x1},1_{y1}) = (2_{x3}, 2_{y3})$

#### Verschlüsselung
Hierfür berechnen wir die Variablen $R,S$ und verwenden folgende Formeln:

`R = a * G`

`S = M + a * Y`

##### Berechnung von R
$R = 2*(1_{x1},1_{y1}) = (_{x3},_{y3})$

$\lambda=\frac{3*1^2-4}{2*1}=\frac{-1}{2}=2$

$x_{3}=2^2-2*1=2$

$y_{3}=2*(1-2)-1=-3 = 2$

**Ergebnis**: $R = a * G = 2 * (1_{x1},1_{y1}) = (2_{x3}, 2_{y3})$

##### Berechnung von S
$S = (2,2) + 2*(2_{x1},2_{y1}) = (_{x3}, _{y3})$

1. Zuerst berechnen wir in der oberen Gleichung das $2*(2_{x1},2_{y1})$

$a*Y=2*(2_{x1},2_{y1}) = (_{x3}, _{y3})$

$\lambda=\frac{3*2^2-4}{2*2}=\frac{8}{4}=2$

$x_{3}=2^2-2*2=0$

$y_{3}=2*(2-0)-2=2$

**Ergebnis: $a*Y=2*(2_{x1},2_{y1}) = (0_{x3}, 2_{y3})$**

2. Nun setzen wir das Ergebnis ein und berechnen die Addition davon: 

$S = (2_{x1},2_{y1}) + (0_{x2},2_{y2}) = (_{x3}, _{y3})$

$\lambda=\frac{2-2}{0-2}=0$

$x_3=0^2-2-0=-2=3$

$y_{3}=0*(2-3)-2=-2=3$

**Ergebnis**:$S = (2_{x1},2_{y1}) + (0_{x2},2_{y2}) = (3_{x3}, 3_{x3})$

Nun sendet Alice and Bob folgende Werte (Geheimtext):

$R,S = (2,2),(3,3)$

#### Entschlüsseln 
Bob erhält von Alice die Werte $R,S = (2,2),(3,3)$ diese entschlüsselt er mit folgenden Formeln:

`Z = -b *R`

`M = Z + S`

##### Berechnung von Z
Wir drehen das Ergebnis um, weil $-2*$

$Z = -2 * (2_{x1},2_{y1}) =(_{x3},_{y3})$

$\lambda=\frac{3*2^2-4}{2*2}=\frac{8}{4}=2$

$x_{3}=2^2-2*2=0$

$y_{3}=2*(2-0)-2= 2 \equiv -2 \equiv 3$

**Ergebnis: $Z =(0_{x3}, 3_{y3})$

##### Berechnung von M 
$M = (0_{x1},3_{y1}) + (3_{x2},3_{y2}) = (_{x3}, _{y3})$

$\lambda=\frac{3-3}{3-0}=0$

$x_{3}=0^{2}-0-3=-3 \mod{5} =2$

$y_{3}=0*(0-2)-3=-3\mod{5}=2$
