# ELTE - Operációkutatás Számítógépes Módszerei

2025/2026-os tanév II. (tavaszi) félév.

## A tárgy célja

A tárgy célja, hogy a hallgatók a félév során megismerkedjenek különféle optimalizációs feladatok gyakorlati, számítógépes megoldásának lehetőségeivel.

A félév nagy részében egészértékű programozási módszerekkel foglalkozunk: alapvető feladatok (hátizsák feladat, utazóügynök feladat, stb.); alapvető modellezési technikák; vágás-generálás (utazóügynök feladat, gépütemezés, stb.); oszlop-generálás (szabási feladat, stb.); stb. Röviden - pár feladat erejéig - szó lesz még korlátozás programozásról, és lokális keresésen alapuló heurisztikák is előkerülnek majd.

A gyakorlatokon a feladatok megoldásához a Python programozási nyelvet használjuk.

## Követelmények

A hallgatóknak a félév során **két beadandó feladat**ot kell teljesíteniük a gyakorlati jegy megszerzéséhez.

## A félév menete
<!--
Csütörtök 8:00-10:00 Hetek: 2,3,4,5,6,7,8,10,11,12,13,14,15

Első tanítási nap: 2026. február 9. (hétfő)
Tavaszi szünet: 2026. április 1–7. (szerda–kedd)
2026. május 1., péntek munkaszüneti nap	
Pázmány-nap (tanítási szünet): 2026. május 8. (péntek)
Utolsó tanítási nap: 2026. május 16. (szombat)
-->

**Csütörtök 8:30-10:00**, D 3.105 (Grafika labor) | **Ha valaki a saját laptopján szeretné az órai munkát végezni, nyugodtan hozza magával. Sőt!**

**<p style="text-decoration: line-through">[1] 2026.02.05. (Regisztrációs időszak)</p>**

**[2] 2026.02.12.**

Korlátozás programozás: bevezetés, `alldifferent` constraint.

<a href="https://github.com/hmarko89/mathoptintro/blob/master/src/sendmoremoney.py" target="_blank">`sendmoremoney.py`</a>
<a href="https://github.com/hmarko89/mathoptintro/blob/master/src/sudoku.py" target="_blank">`sudoku.py`</a>
<a href="https://github.com/hmarko89/mathoptintro/blob/master/src/queens.py" target="_blank">`queens.py`</a>

**[3] 2026.02.19.**

Korlátozás programozás: interval variables, non-overlapping constraints.

<a href="https://github.com/hmarko89/mathoptintro/blob/master/src/scheduling.py" target="_blank">`scheduling.py`</a> (<a href="https://github.com/hmarko89/mathoptintro/blob/master/src/scheduling_instances.py" target="_blank">`scheduling_instances.py`</a>)
<a href="https://github.com/hmarko89/mathoptintro/blob/master/src/rectangle.py" target="_blank">`rectangle.py`</a>

**[4] 2026.02.26.**

**[5] 2026.03.05.**

**[6] 2026.03.12.**

**[7] 2026.03.19.**

**[8] 2026.03.26.**

**<p style="text-decoration: line-through">[9] 2026.04.02. (Tavaszi szünet)</p>**

**[10] 2026.04.09.**

**[11] 2026.04.16.**

**[12] 2026.04.23.**

**[13] 2026.04.30.**

**<p style="text-decoration: line-through">[14] 2026.05.07. (Eötvös nap)</p>**

**[15] 2026.05.14.**

## Elérhetőség

📧 marko.horvath (kukac) sztaki (pont) hu

📍 SZTAKI (1111 Budapest, Kende utca 13-17.), K518

📅 Fogadóórák előre egyeztetett időpontban.

## Technikai dolgok

### Visual Studio Code

Az órán <a href="https://code.visualstudio.com/" target="_blank">Visual Studio Code</a>-ban mutatom a példákat, de persze, mindenki használhatja a kedvenc szerkesztőjét.

### Python

A következő csomagokat fogjuk használni:

#### Google OR-Tools

Korlátozás programozáshoz a **CP-SAT**-ot, egészértékű programozáshoz a <a href="https://developers.google.com/optimization/math_opt" target="_blank">**MathOpt**</a> csomagot használjuk majd.
```
python -m pip install ortools
```

A MathOpt jó pár solver-t támogat, de ezek nem mindegyike jön automatikusan a telepítéskor.
Érdemes ezért telepíteni valamelyiket a következők közül:

- **<a href="https://highs.dev/" target="_blank">HiGHS:</a>** Nyílt forráskodó megoldó (MIP, QP).

- **<a href="https://scipopt.org/" target="_blank">SCIP:</a>** Nyílt forráskodó megoldó (MIP, MINLP, CIP).

- **<a href="https://www.gurobi.com/downloads/gurobi-software/" target="_blank">Gurobi:</a>**
    Kereskedelmi megoldó, de tudtok diák licence-t igényelni hozzá.
    A 12-es verziót érdemes telepíteni, mert a MathOpt annál újabbat egyelőre nem támogat.

#### Egyéb csomagok

**Matplotlib**. Rajzolni.
```
python -m pip install matplotlib
```

**NetworkX**. Gráfokhoz.
```
python -m pip install networkx
```
