# -----------------------------------------------------------
# 将聚类结果加至数据末尾，需要手动将爬取数据的首列加上id列名
# -----------------------------------------------------------
import pandas as pd
# 读取新闻
news = pd.read_excel("nefu_news.xlsx")
out_path = "add_type_nefu_news.xlsx"
news_df = pd.DataFrame(news)
# 读取聚类结果
# cluster = open('cluster_id.txt')
# text = cluster.read()

# 手动直接将结果复制为数组(笑)
type1 = [0, 1, 2, 3, 4, 5, 9, 16, 17, 21, 26, 27, 28, 36, 37, 44, 50, 55, 56, 57, 64, 73, 79, 80, 83, 93, 102, 103, 108, 109, 112, 121, 123, 124, 131, 132, 136, 150, 152, 153, 154, 156, 162, 165, 174, 175, 176, 177, 182, 183, 185, 194, 199, 200, 203, 204, 205, 206, 210, 211, 223, 228, 229, 230, 237, 238, 239, 240, 255, 257, 258, 259, 266, 269, 284, 298, 306, 324, 325, 330, 331, 335, 353, 354, 359, 360, 385, 404, 414, 423, 433, 439, 445, 447, 452, 459, 462, 468, 474, 485, 488, 491, 502, 515, 516, 519, 521, 531, 533, 537, 538, 541, 542, 544, 545, 548, 550, 556, 560, 562, 566, 567, 570, 573, 574, 575, 585, 589, 590, 602, 603, 604, 611, 612, 619, 628, 630, 635, 636, 637, 640, 641, 648, 649, 653, 657, 659, 664, 665, 667, 670, 675, 677, 678, 682, 687, 696, 699, 705, 707, 708, 709, 710, 711, 712, 716, 726, 727, 728, 729, 734, 736, 737, 738, 739, 740, 741, 743, 751, 755, 756, 757, 758, 761, 762, 764, 765, 767, 770, 772, 780, 782, 786, 787, 788, 790, 791, 793, 794, 796, 799, 802, 803, 804, 805, 806, 808, 809, 811, 815, 816, 817, 823, 825, 828, 831, 832, 833, 834, 835, 837, 839, 840, 846, 852, 854, 857, 859, 866, 868, 869, 881, 886, 888, 894, 895, 910, 913, 917, 918, 919, 920, 921, 922, 923, 924, 932, 933, 935, 936, 937, 938, 940, 942, 946, 947, 948, 949, 950, 951, 958, 959, 961, 962, 964, 965, 966, 967, 969, 970, 972, 979, 980, 987, 988, 990, 991, 994, 997, 999, 1001, 1008, 1010, 1015, 1016, 1019, 1020, 1023, 1026, 1030, 1033, 1034, 1037, 1039, 1044, 1045, 1048, 1049, 1050, 1053, 1055, 1059, 1062, 1063, 1065, 1073, 1077, 1078, 1079, 1082, 1084, 1086, 1087, 1089, 1091, 1092, 1094, 1102, 1103, 1112, 1113, 1115, 1116, 1118, 1120, 1121, 1122, 1123, 1125, 1126, 1132, 1143, 1146, 1151, 1152, 1154, 1155, 1160, 1161, 1162, 1168, 1172, 1175, 1182, 1185, 1186, 1187, 1189, 1190, 1191, 1197, 1198, 1200, 1202, 1211, 1214, 1215, 1216, 1222, 1223, 1224, 1227, 1229, 1231, 1236, 1243, 1251, 1252, 1253, 1258, 1259, 1265, 1272, 1277, 1279, 1280, 1283, 1287, 1288, 1297, 1298, 1301, 1306, 1308, 1309, 1312, 1313, 1314, 1315, 1317, 1326, 1327, 1330, 1335, 1340, 1341, 1342, 1343, 1344, 1346, 1355, 1358, 1364, 1372, 1373, 1374, 1376, 1384, 1387, 1388, 1392, 1401, 1402, 1403, 1405, 1412, 1414, 1417, 1421, 1426, 1427, 1428, 1429, 1431, 1432, 1433, 1435, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1452, 1455, 1456, 1457, 1458, 1460, 1461, 1462, 1473, 1474, 1475, 1476, 1477, 1478, 1481, 1484, 1485, 1486, 1491, 1492, 1505, 1511, 1513, 1514, 1515, 1520, 1527, 1528, 1530, 1534, 1542, 1545, 1548, 1549, 1556, 1557, 1561, 1562, 1563, 1564, 1568, 1571, 1574, 1577, 1578, 1580, 1581, 1583, 1590, 1591, 1592, 1593, 1597, 1600, 1602, 1603, 1605, 1607, 1609, 1610, 1612, 1616, 1617, 1623, 1626, 1629, 1631, 1632, 1634, 1638, 1640, 1642, 1644, 1645, 1646, 1652, 1656, 1657, 1658, 1667, 1669, 1671, 1678, 1682, 1685, 1686, 1687, 1694, 1697, 1700, 1701, 1707, 1717, 1718, 1719, 1723, 1726, 1729, 1731, 1733, 1738, 1746, 1747, 1748, 1750, 1751, 1752, 1753, 1754, 1755, 1757, 1758, 1760, 1762, 1767, 1777, 1779, 1780, 1781, 1782, 1783, 1784, 1786, 1787, 1789, 1792, 1795, 1796, 1809, 1812, 1814, 1816, 1818, 1821, 1824, 1827, 1830, 1832, 1833, 1838, 1841, 1843, 1844, 1845, 1849, 1856, 1859, 1861, 1862, 1866, 1867, 1869, 1870, 1873, 1874, 1878, 1883, 1886, 1889, 1895, 1896, 1898, 1899, 1901, 1904, 1905, 1909, 1910, 1912, 1915, 1918, 1920, 1921, 1924, 1925, 1928, 1929, 1930, 1933, 1934, 1938, 1941, 1942, 1945, 1947, 1949, 1950, 1953, 1954, 1957, 1958, 1959, 1962, 1965, 1967, 1970, 1971, 1974, 1976, 1977, 1978, 1979, 1981, 1983, 1987, 1988, 1991, 1994, 1996, 1998, 2005, 2006, 2007, 2008, 2010, 2012, 2018, 2019, 2025, 2027, 2034, 2039, 2047, 2048, 2054, 2055, 2058, 2063, 2068, 2072, 2073, 2074, 2075, 2081, 2083, 2084, 2087, 2101, 2102, 2103, 2104, 2111, 2113, 2114, 2115, 2116, 2117, 2118, 2129, 2140, 2142, 2143, 2144, 2145, 2146, 2147, 2150, 2158, 2173, 2179, 2186, 2189, 2190, 2191, 2195, 2202, 2206, 2209, 2210, 2213, 2215, 2218, 2219, 2220, 2226, 2227, 2228, 2229, 2230, 2231, 2235, 2238, 2239, 2242, 2244, 2246, 2247, 2255, 2256, 2257, 2258, 2259, 2260, 2263, 2268, 2269, 2273, 2275, 2276, 2284, 2285, 2288, 2292, 2297, 2298, 2300, 2302, 2304, 2305, 2308, 2313, 2314, 2317, 2319, 2321, 2322, 2323, 2326, 2329, 2331, 2333, 2334, 2337, 2342, 2344, 2345, 2347, 2348, 2350, 2351, 2352, 2355, 2360, 2361, 2365, 2371, 2373, 2374, 2377, 2379, 2384, 2389, 2390, 2394, 2396, 2399, 2403, 2406, 2408, 2413, 2425, 2428, 2432, 2453, 2454, 2475, 2476, 2479, 2482, 2483, 2493, 2504, 2505, 2508, 2509, 2514, 2515, 2518, 2522, 2528, 2531, 2532, 2533, 2535, 2537, 2538, 2543, 2544, 2548, 2553, 2557, 2560, 2561, 2562, 2564, 2566, 2567, 2571, 2577, 2582, 2585, 2587, 2589, 2592, 2593, 2594, 2595, 2596, 2600, 2609, 2612, 2614, 2616, 2618, 2621, 2622, 2625, 2630, 2632, 2638, 2641, 2643, 2644, 2645, 2646, 2647, 2650, 2654, 2659, 2663, 2667, 2672, 2673, 2674, 2675, 2676, 2679, 2680, 2689, 2692, 2696, 2701, 2705, 2709, 2720, 2723, 2727, 2730, 2734, 2740, 2741, 2746, 2749, 2752, 2758, 2761, 2762, 2769, 2770, 2787, 2790, 2791, 2832, 2833, 2834, 2835, 2856, 2861, 2862, 2863, 2864, 2871, 2873, 2877, 2885, 2894, 2897, 2900, 2902, 2906, 2909, 2910, 2914, 2923, 2926, 2927, 2931, 2932, 2938, 2939, 2943, 2946, 2947, 2948, 2949, 2951, 2952, 2954, 2955, 2956, 2960, 2961, 2965, 2966, 2967, 2968, 2969, 2974, 2975, 2976, 2977, 2978, 2980, 2981, 2983, 2984, 2986, 2987, 2994, 2995, 2996, 2997, 2998, 3004, 3007, 3008, 3013, 3015, 3016, 3024, 3027, 3033, 3036, 3037, 3041, 3045, 3047, 3053, 3056, 3060, 3065, 3069, 3070, 3074, 3076, 3083, 3089, 3094, 3112, 3117, 3122, 3123, 3125, 3126, 3140, 3142, 3146, 3151, 3152, 3154, 3157, 3162, 3164, 3169, 3171, 3175, 3176, 3180, 3181, 3182, 3183, 3186, 3191, 3193, 3204, 3205, 3209, 3210, 3211, 3213, 3215, 3216, 3222, 3231, 3232, 3233, 3236, 3238, 3240, 3242, 3244, 3245, 3260, 3261, 3262, 3265, 3267, 3271, 3275, 3288, 3300, 3304, 3316, 3317, 3329, 3332, 3334, 3347, 3358, 3361, 3363, 3365, 3367, 3373, 3376, 3383, 3385, 3387, 3389, 3390, 3392, 3394, 3396, 3403, 3404, 3407, 3408, 3409, 3410, 3411, 3412, 3414, 3416, 3418, 3419, 3423, 3425, 3432, 3433, 3436, 3437, 3438, 3439, 3440, 3441, 3442, 3446, 3452, 3454, 3459, 3460, 3461, 3462, 3463, 3464, 3465, 3467, 3469, 3470, 3471, 3475, 3482, 3487, 3488, 3489, 3490, 3491, 3492, 3493, 3494, 3496, 3500, 3501, 3503, 3511, 3518, 3519, 3529, 3530, 3532, 3535, 3537, 3539, 3543, 3547, 3548, 3554, 3555, 3564, 3566, 3568, 3572, 3574, 3580, 3583, 3584, 3592, 3600, 3603, 3609, 3611, 3616, 3622, 3627, 3637, 3642, 3647, 3655, 3669, 3672, 3673, 3677, 3686, 3689, 3693, 3697, 3699, 3700, 3704, 3712, 3719, 3722, 3726, 3728, 3733, 3734, 3739, 3742, 3745, 3749, 3752, 3753, 3768, 3769, 3776, 3781, 3799, 3805, 3810, 3811, 3816, 3819, 3828, 3830, 3834, 3838, 3840, 3845, 3848, 3850, 3854, 3857, 3863, 3864, 3867, 3871, 3884, 3890, 3891, 3911, 3913, 3919, 3940, 3942, 3948, 3952, 3953, 3958, 3968, 3972, 3973, 3976, 3980, 3981, 3988, 3991, 3995, 3996, 3999, 4005, 4008, 4010, 4017, 4020, 4026, 4029, 4034, 4037, 4039, 4042, 4043, 4048, 4049, 4050, 4055, 4058, 4065, 4066, 4069, 4071, 4072, 4077, 4078, 4081, 4084, 4088, 4094, 4095, 4101, 4102, 4103, 4104, 4105, 4110, 4113, 4117, 4118, 4119, 4122, 4126, 4130, 4131, 4132, 4133, 4134, 4136, 4137, 4138, 4140, 4142, 4143, 4144, 4146, 4147, 4148, 4151, 4156, 4165, 4166, 4167, 4169, 4171, 4172, 4173, 4177, 4178, 4179, 4180, 4182, 4185, 4196, 4197, 4198, 4199, 4200, 4202, 4206, 4207, 4208, 4209, 4211, 4218, 4221, 4225, 4226, 4227, 4228, 4229, 4234, 4235, 4237, 4238, 4239, 4247, 4263, 4264, 4266, 4267, 4268, 4292, 4295, 4311, 4314, 4317, 4319, 4322, 4323, 4325, 4346, 4348, 4351, 4352, 4354, 4357, 4373, 4374, 4377, 4383, 4386, 4402, 4403, 4406, 4417, 4419, 4432, 4437, 4438, 4446, 4448, 4451, 4456, 4458, 4461, 4466, 4467, 4469, 4477, 4480, 4485, 4491, 4492, 4498, 4520, 4521, 4526, 4529, 4544, 4551, 4555, 4558, 4565, 4571, 4573, 4580, 4582, 4590, 4594, 4600, 4602, 4606, 4608, 4611, 4619, 4621, 4622, 4624, 4625, 4626, 4628, 4636, 4638, 4639, 4643, 4647, 4648, 4650, 4652, 4661, 4662, 4663, 4664, 4672, 4676, 4677, 4678, 4693, 4698, 4701, 4707, 4717, 4721, 4724, 4727, 4730, 4738, 4739, 4746, 4750, 4753, 4756, 4759, 4764, 4767, 4768, 4775, 4785, 4788, 4797, 4798, 4799, 4805, 4806, 4808, 4810, 4812, 4817, 4818, 4819, 4829, 4831, 4834, 4835, 4837, 4839, 4842, 4844, 4848, 4858, 4860, 4864]
type2 = [6, 8, 10, 13, 15, 18, 19, 25, 29, 30, 33, 35, 38, 54, 63, 77, 78, 81, 82, 86, 92, 96, 97, 98, 101, 105, 106, 107, 110, 111, 116, 119, 120, 122, 125, 126, 127, 130, 135, 137, 138, 139, 141, 142, 145, 148, 149, 151, 158, 164, 166, 167, 168, 170, 171, 179, 180, 181, 187, 192, 193, 197, 198, 208, 209, 213, 214, 215, 217, 221, 222, 226, 227, 231, 232, 234, 235, 242, 243, 244, 246, 251, 260, 261, 263, 264, 271, 274, 276, 280, 292, 300, 303, 313, 321, 332, 342, 350, 361, 379, 381, 382, 401, 403, 405, 407, 409, 410, 411, 430, 432, 434, 436, 438, 440, 441, 443, 444, 446, 457, 463, 464, 465, 467, 469, 470, 472, 473, 475, 476, 477, 478, 483, 486, 492, 493, 494, 495, 497, 498, 501, 503, 504, 505, 506, 507, 512, 520, 522, 524, 526, 527, 530, 532, 536, 549, 551, 552, 553, 555, 559, 565, 571, 572, 576, 579, 580, 581, 582, 584, 588, 595, 598, 599, 600, 601, 605, 608, 609, 613, 614, 615, 616, 618, 624, 627, 629, 633, 638, 642, 643, 644, 645, 650, 652, 654, 656, 658, 662, 668, 679, 681, 683, 688, 690, 691, 693, 694, 697, 706, 717, 719, 720, 722, 723, 725, 731, 732, 735, 744, 752, 754, 760, 763, 769, 773, 783, 789, 792, 798, 800, 807, 812, 819, 820, 826, 829, 836, 841, 843, 844, 848, 849, 855, 861, 862, 870, 872, 873, 875, 877, 878, 882, 883, 884, 890, 891, 896, 897, 902, 903, 904, 906, 907, 911, 912, 925, 926, 931, 954, 955, 957, 960, 971, 973, 975, 976, 977, 983, 984, 986, 989, 993, 995, 996, 1000, 1002, 1004, 1005, 1006, 1009, 1011, 1013, 1014, 1018, 1022, 1024, 1025, 1027, 1028, 1029, 1032, 1035, 1036, 1038, 1040, 1042, 1043, 1046, 1047, 1052, 1056, 1057, 1058, 1061, 1064, 1068, 1070, 1071, 1075, 1076, 1081, 1090, 1093, 1097, 1099, 1100, 1110, 1119, 1130, 1131, 1139, 1141, 1142, 1147, 1159, 1164, 1165, 1169, 1170, 1171, 1176, 1180, 1183, 1193, 1194, 1199, 1204, 1206, 1209, 1212, 1221, 1225, 1228, 1233, 1235, 1237, 1238, 1239, 1242, 1245, 1250, 1254, 1260, 1261, 1266, 1267, 1268, 1271, 1278, 1282, 1289, 1290, 1293, 1300, 1302, 1307, 1311, 1316, 1318, 1322, 1329, 1331, 1334, 1337, 1338, 1345, 1347, 1350, 1351, 1354, 1356, 1357, 1359, 1360, 1363, 1366, 1367, 1369, 1379, 1380, 1383, 1385, 1386, 1389, 1393, 1394, 1395, 1396, 1398, 1407, 1408, 1411, 1415, 1416, 1418, 1422, 1423, 1424, 1425, 1430, 1436, 1437, 1440, 1444, 1459, 1464, 1467, 1469, 1471, 1483, 1490, 1493, 1496, 1498, 1500, 1502, 1504, 1507, 1508, 1512, 1519, 1521, 1523, 1526, 1529, 1531, 1533, 1536, 1537, 1546, 1550, 1552, 1555, 1558, 1559, 1560, 1567, 1575, 1579, 1584, 1588, 1589, 1596, 1599, 1601, 1604, 1606, 1608, 1613, 1622, 1624, 1625, 1628, 1630, 1633, 1635, 1641, 1643, 1651, 1653, 1659, 1660, 1664, 1670, 1672, 1673, 1674, 1675, 1676, 1677, 1679, 1680, 1681, 1688, 1689, 1696, 1699, 1702, 1703, 1704, 1705, 1706, 1708, 1709, 1710, 1711, 1712, 1714, 1716, 1720, 1725, 1728, 1734, 1735, 1739, 1740, 1741, 1743, 1745, 1763, 1764, 1770, 1771, 1774, 1775, 1776, 1790, 1791, 1793, 1794, 1799, 1800, 1803, 1804, 1805, 1810, 1813, 1815, 1819, 1820, 1822, 1823, 1828, 1831, 1839, 1842, 1846, 1847, 1850, 1852, 1857, 1860, 1872, 1875, 1876, 1879, 1881, 1882, 1884, 1888, 1890, 1902, 1903, 1911, 1913, 1917, 1919, 1926, 1927, 1931, 1932, 1940, 1944, 1955, 1956, 1960, 1963, 1969, 1973, 1980, 1985, 1986, 1989, 1992, 2000, 2002, 2003, 2009, 2014, 2017, 2021, 2023, 2029, 2031, 2032, 2035, 2036, 2038, 2040, 2041, 2046, 2050, 2052, 2062, 2064, 2065, 2067, 2069, 2070, 2076, 2077, 2079, 2080, 2093, 2095, 2096, 2097, 2098, 2099, 2100, 2105, 2106, 2108, 2109, 2110, 2112, 2122, 2124, 2125, 2126, 2127, 2128, 2131, 2132, 2135, 2138, 2139, 2141, 2149, 2151, 2152, 2155, 2160, 2161, 2164, 2169, 2170, 2171, 2176, 2178, 2180, 2181, 2184, 2187, 2188, 2193, 2194, 2198, 2199, 2200, 2208, 2216, 2217, 2222, 2223, 2233, 2237, 2265, 2266, 2271, 2281, 2282, 2294, 2295, 2303, 2306, 2307, 2310, 2311, 2320, 2325, 2327, 2328, 2332, 2335, 2336, 2339, 2340, 2343, 2346, 2349, 2354, 2356, 2359, 2362, 2363, 2368, 2369, 2372, 2375, 2376, 2378, 2380, 2381, 2383, 2385, 2388, 2391, 2392, 2395, 2397, 2405, 2407, 2409, 2410, 2412, 2415, 2419, 2420, 2421, 2422, 2424, 2426, 2435, 2436, 2437, 2440, 2444, 2448, 2449, 2450, 2451, 2460, 2464, 2465, 2466, 2469, 2474, 2478, 2489, 2491, 2494, 2495, 2496, 2498, 2503, 2507, 2510, 2511, 2516, 2517, 2520, 2523, 2524, 2525, 2527, 2534, 2536, 2539, 2540, 2545, 2546, 2551, 2555, 2563, 2565, 2568, 2572, 2574, 2580, 2584, 2586, 2591, 2597, 2601, 2603, 2607, 2610, 2611, 2615, 2620, 2631, 2636, 2639, 2640, 2648, 2660, 2664, 2669, 2677, 2682, 2685, 2686, 2687, 2693, 2698, 2700, 2703, 2708, 2711, 2714, 2715, 2716, 2719, 2721, 2724, 2726, 2729, 2732, 2739, 2748, 2750, 2753, 2755, 2756, 2757, 2760, 2765, 2768, 2775, 2776, 2777, 2778, 2783, 2785, 2786, 2789, 2794, 2798, 2799, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2812, 2813, 2814, 2816, 2818, 2820, 2822, 2823, 2827, 2828, 2830, 2831, 2836, 2837, 2839, 2840, 2842, 2843, 2845, 2847, 2849, 2852, 2854, 2857, 2858, 2859, 2860, 2865, 2866, 2868, 2869, 2870, 2872, 2874, 2881, 2883, 2886, 2887, 2888, 2889, 2890, 2895, 2898, 2899, 2901, 2903, 2912, 2918, 2919, 2924, 2928, 2929, 2933, 2941, 2950, 2957, 2958, 2962, 2970, 2971, 2972, 2979, 2985, 2990, 2991, 2992, 2993, 2999, 3000, 3001, 3005, 3006, 3010, 3014, 3019, 3020, 3021, 3022, 3025, 3029, 3030, 3031, 3034, 3035, 3039, 3042, 3044, 3046, 3048, 3049, 3051, 3054, 3058, 3059, 3062, 3064, 3067, 3068, 3071, 3073, 3075, 3077, 3078, 3079, 3080, 3081, 3082, 3084, 3085, 3086, 3087, 3088, 3091, 3093, 3096, 3097, 3098, 3100, 3101, 3102, 3103, 3105, 3108, 3109, 3110, 3111, 3113, 3114, 3115, 3116, 3119, 3124, 3127, 3129, 3130, 3131, 3132, 3134, 3136, 3139, 3143, 3144, 3145, 3148, 3153, 3155, 3160, 3163, 3165, 3168, 3172, 3173, 3177, 3178, 3179, 3184, 3189, 3192, 3195, 3201, 3202, 3206, 3207, 3208, 3212, 3214, 3217, 3220, 3221, 3224, 3230, 3235, 3237, 3241, 3243, 3246, 3249, 3251, 3252, 3254, 3255, 3258, 3264, 3266, 3270, 3272, 3276, 3277, 3278, 3280, 3281, 3283, 3284, 3287, 3290, 3291, 3293, 3294, 3295, 3297, 3299, 3301, 3305, 3306, 3307, 3309, 3311, 3315, 3319, 3320, 3322, 3323, 3324, 3326, 3328, 3330, 3336, 3338, 3340, 3344, 3345, 3346, 3349, 3351, 3352, 3353, 3354, 3355, 3357, 3359, 3364, 3369, 3372, 3374, 3375, 3378, 3380, 3381, 3382, 3386, 3388, 3393, 3398, 3401, 3406, 3415, 3417, 3421, 3422, 3428, 3435, 3447, 3450, 3451, 3457, 3476, 3480, 3481, 3483, 3485, 3497, 3498, 3499, 3504, 3505, 3509, 3510, 3512, 3514, 3516, 3526, 3527, 3528, 3533, 3534, 3536, 3540, 3544, 3545, 3556, 3560, 3565, 3569, 3573, 3575, 3576, 3581, 3582, 3585, 3589, 3593, 3601, 3602, 3604, 3605, 3610, 3613, 3614, 3615, 3620, 3626, 3633, 3634, 3636, 3640, 3646, 3650, 3651, 3662, 3663, 3665, 3675, 3676, 3678, 3679, 3681, 3694, 3696, 3702, 3703, 3705, 3706, 3708, 3710, 3711, 3716, 3717, 3720, 3729, 3730, 3737, 3738, 3740, 3743, 3751, 3756, 3759, 3760, 3762, 3763, 3764, 3765, 3767, 3772, 3773, 3775, 3778, 3780, 3785, 3786, 3788, 3789, 3790, 3791, 3792, 3793, 3794, 3795, 3796, 3797, 3798, 3800, 3802, 3804, 3807, 3809, 3812, 3814, 3815, 3817, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3829, 3831, 3832, 3836, 3837, 3839, 3841, 3843, 3844, 3846, 3849, 3856, 3859, 3861, 3866, 3874, 3875, 3878, 3880, 3881, 3883, 3886, 3888, 3893, 3895, 3896, 3897, 3899, 3903, 3904, 3907, 3909, 3910, 3912, 3914, 3915, 3922, 3924, 3925, 3926, 3928, 3930, 3936, 3939, 3941, 3943, 3944, 3951, 3955, 3956, 3957, 3959, 3965, 3977, 3978, 3979, 3984, 3987, 3989, 4000, 4001, 4002, 4003, 4007, 4013, 4016, 4018, 4024, 4025, 4032, 4036, 4046, 4047, 4053, 4054, 4060, 4063, 4075, 4076, 4079, 4080, 4082, 4087, 4089, 4092, 4100, 4106, 4108, 4109, 4111, 4116, 4124, 4129, 4135, 4139, 4141, 4145, 4153, 4158, 4160, 4168, 4170, 4174, 4175, 4187, 4189, 4193, 4203, 4204, 4212, 4213, 4216, 4217, 4222, 4240, 4241, 4242, 4245, 4246, 4250, 4255, 4257, 4258, 4269, 4272, 4273, 4277, 4278, 4279, 4284, 4286, 4287, 4288, 4289, 4291, 4293, 4294, 4296, 4299, 4300, 4301, 4303, 4304, 4307, 4308, 4310, 4312, 4313, 4315, 4316, 4318, 4320, 4328, 4329, 4330, 4332, 4333, 4336, 4339, 4340, 4342, 4343, 4344, 4345, 4347, 4349, 4365, 4368, 4369, 4371, 4372, 4375, 4381, 4393, 4394, 4395, 4399, 4401, 4404, 4410, 4413, 4416, 4422, 4423, 4424, 4428, 4431, 4439, 4442, 4445, 4449, 4450, 4457, 4460, 4468, 4470, 4474, 4476, 4478, 4479, 4486, 4489, 4490, 4495, 4497, 4499, 4503, 4505, 4507, 4511, 4512, 4514, 4518, 4519, 4524, 4527, 4534, 4536, 4540, 4541, 4543, 4548, 4550, 4556, 4564, 4567, 4570, 4577, 4579, 4584, 4585, 4587, 4591, 4593, 4596, 4599, 4601, 4604, 4605, 4609, 4613, 4614, 4616, 4620, 4623, 4627, 4629, 4631, 4637, 4641, 4644, 4646, 4651, 4653, 4655, 4665, 4668, 4670, 4673, 4675, 4680, 4681, 4683, 4685, 4686, 4687, 4692, 4695, 4696, 4703, 4704, 4708, 4710, 4711, 4712, 4718, 4720, 4722, 4723, 4725, 4726, 4732, 4733, 4736, 4747, 4749, 4751, 4752, 4754, 4763, 4765, 4774, 4776, 4792, 4793, 4795, 4796, 4801, 4811, 4813, 4815, 4816, 4821, 4823, 4824, 4826, 4840, 4843, 4846, 4847, 4852, 4853, 4855, 4861, 4863]
type3 = [7, 12, 32, 42, 71, 84, 113, 134, 140, 143, 155, 157, 159, 161, 163, 169, 178, 184, 186, 188, 190, 191, 195, 196, 207, 212, 216, 219, 220, 224, 225, 233, 241, 245, 249, 252, 254, 262, 268, 270, 272, 278, 281, 283, 290, 294, 297, 299, 301, 319, 323, 326, 347, 355, 367, 376, 383, 396, 406, 412, 424, 435, 453, 460, 479, 480, 489, 499, 500, 508, 509, 528, 529, 535, 554, 557, 564, 577, 583, 586, 591, 592, 594, 606, 610, 620, 621, 623, 631, 639, 647, 651, 660, 666, 671, 672, 676, 680, 692, 695, 700, 701, 713, 721, 746, 749, 750, 766, 775, 778, 779, 781, 784, 785, 795, 810, 813, 814, 822, 824, 827, 845, 851, 853, 856, 860, 864, 874, 885, 889, 893, 898, 899, 900, 916, 927, 928, 929, 934, 939, 941, 945, 963, 968, 974, 978, 1003, 1007, 1012, 1017, 1031, 1041, 1051, 1054, 1060, 1069, 1080, 1083, 1088, 1098, 1104, 1105, 1117, 1124, 1127, 1128, 1129, 1133, 1134, 1144, 1150, 1153, 1156, 1157, 1158, 1166, 1167, 1173, 1181, 1184, 1188, 1195, 1196, 1201, 1203, 1207, 1210, 1213, 1217, 1218, 1219, 1220, 1230, 1232, 1241, 1244, 1246, 1247, 1248, 1249, 1255, 1256, 1257, 1262, 1263, 1264, 1270, 1273, 1274, 1276, 1284, 1285, 1286, 1291, 1292, 1296, 1303, 1305, 1319, 1320, 1325, 1333, 1336, 1339, 1348, 1349, 1362, 1365, 1368, 1370, 1371, 1375, 1377, 1399, 1400, 1404, 1406, 1409, 1438, 1453, 1468, 1472, 1482, 1488, 1497, 1501, 1503, 1517, 1524, 1525, 1532, 1540, 1541, 1543, 1544, 1553, 1554, 1565, 1569, 1570, 1572, 1573, 1582, 1585, 1586, 1587, 1594, 1611, 1614, 1615, 1621, 1636, 1650, 1661, 1662, 1665, 1690, 1691, 1692, 1693, 1698, 1721, 1722, 1727, 1736, 1737, 1749, 1765, 1766, 1768, 1769, 1772, 1773, 1778, 1788, 1797, 1798, 1801, 1802, 1807, 1817, 1825, 1836, 1848, 1854, 1863, 1864, 1865, 1868, 1871, 1877, 1891, 1892, 1893, 1894, 1897, 1900, 1906, 1907, 1908, 1935, 1936, 1937, 1939, 1946, 1961, 1964, 1966, 1968, 1975, 1990, 1993, 1995, 2015, 2016, 2020, 2037, 2043, 2044, 2045, 2049, 2057, 2060, 2066, 2086, 2089, 2130, 2137, 2148, 2156, 2159, 2166, 2167, 2172, 2174, 2175, 2177, 2185, 2196, 2201, 2203, 2204, 2205, 2214, 2234, 2243, 2245, 2248, 2249, 2250, 2264, 2270, 2272, 2274, 2277, 2278, 2279, 2283, 2286, 2287, 2289, 2293, 2299, 2309, 2312, 2315, 2316, 2318, 2324, 2341, 2353, 2357, 2358, 2364, 2370, 2382, 2386, 2387, 2393, 2400, 2401, 2411, 2414, 2416, 2417, 2423, 2429, 2430, 2434, 2439, 2442, 2443, 2445, 2446, 2461, 2463, 2468, 2473, 2477, 2490, 2497, 2502, 2506, 2513, 2519, 2526, 2530, 2542, 2549, 2554, 2556, 2559, 2570, 2578, 2583, 2588, 2590, 2599, 2604, 2605, 2608, 2617, 2619, 2624, 2633, 2634, 2637, 2642, 2651, 2653, 2661, 2662, 2670, 2671, 2681, 2683, 2688, 2690, 2691, 2699, 2704, 2707, 2710, 2712, 2717, 2718, 2722, 2728, 2733, 2736, 2737, 2738, 2742, 2747, 2751, 2764, 2766, 2767, 2771, 2779, 2780, 2781, 2782, 2793, 2797, 2808, 2809, 2810, 2811, 2815, 2817, 2821, 2826, 2844, 2846, 2850, 2908, 2911, 2915, 2936, 2937, 2940, 2944, 2973, 2988, 2989, 3002, 3009, 3017, 3018, 3023, 3026, 3038, 3043, 3052, 3055, 3072, 3104, 3107, 3121, 3133, 3138, 3141, 3150, 3161, 3167, 3170, 3174, 3190, 3203, 3250, 3257, 3279, 3286, 3312, 3314, 3327, 3333, 3335, 3341, 3343, 3348, 3356, 3362, 3371, 3377, 3400, 3424, 3445, 3449, 3453, 3468, 3474, 3478, 3479, 3506, 3507, 3508, 3525, 3559, 3577, 3588, 3594, 3595, 3597, 3606, 3619, 3628, 3632, 3639, 3648, 3649, 3657, 3661, 3668, 3670, 3671, 3682, 3685, 3687, 3688, 3690, 3692, 3695, 3723, 3725, 3727, 3735, 3741, 3746, 3748, 3750, 3754, 3755, 3770, 3771, 3877, 3879, 3900, 3901, 3906, 3908, 3917, 3918, 3929, 3932, 3938, 3946, 3947, 3950, 3961, 3967, 3974, 3985, 3986, 3997, 4004, 4012, 4014, 4015, 4028, 4031, 4033, 4045, 4057, 4061, 4062, 4067, 4068, 4074, 4083, 4085, 4090, 4091, 4096, 4097, 4098, 4107, 4112, 4114, 4127, 4176, 4194, 4205, 4214, 4223, 4232, 4236, 4243, 4254, 4256, 4261, 4265, 4271, 4283, 4285, 4360, 4363, 4389, 4398, 4411, 4412, 4415, 4420, 4427, 4433, 4436, 4440, 4441, 4444, 4453, 4455, 4462, 4465, 4482, 4484, 4487, 4494, 4496, 4506, 4508, 4515, 4516, 4523, 4535, 4537, 4545, 4549, 4553, 4563, 4566, 4568, 4569, 4572, 4574, 4578, 4583, 4588, 4592, 4595, 4597, 4598, 4607, 4612, 4617, 4630, 4635, 4640, 4654, 4660, 4669, 4706, 4719, 4735, 4748, 4757, 4786, 4825, 4845, 4849, 4850, 4854, 4862]
type4 = [11, 14, 20, 22, 23, 31, 34, 39, 40, 41, 43, 45, 46, 47, 48, 49, 51, 52, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69, 70, 72, 74, 75, 76, 85, 87, 88, 89, 90, 91, 94, 95, 99, 100, 104, 114, 115, 117, 118, 128, 129, 133, 144, 146, 147, 160, 172, 173, 189, 201, 202, 286, 315, 346, 375, 386, 415, 420, 428, 442, 449, 458, 461, 466, 471, 481, 484, 487, 490, 510, 513, 514, 517, 518, 523, 534, 539, 540, 543, 546, 547, 558, 561, 563, 568, 569, 578, 587, 593, 596, 597, 607, 617, 622, 625, 626, 632, 634, 646, 655, 661, 663, 669, 673, 674, 684, 685, 686, 689, 698, 702, 703, 704, 714, 715, 718, 724, 730, 733, 742, 745, 747, 748, 753, 759, 768, 771, 774, 776, 777, 797, 801, 818, 821, 830, 838, 842, 847, 850, 858, 863, 865, 867, 871, 876, 879, 880, 887, 892, 901, 905, 908, 909, 914, 915, 930, 943, 944, 952, 953, 956, 981, 982, 985, 992, 998, 1021, 1066, 1067, 1072, 1074, 1085, 1095, 1096, 1101, 1106, 1107, 1108, 1109, 1111, 1114, 1135, 1136, 1137, 1138, 1140, 1145, 1148, 1149, 1163, 1174, 1177, 1178, 1179, 1192, 1205, 1208, 1226, 1234, 1240, 1269, 1275, 1281, 1294, 1295, 1299, 1304, 1310, 1321, 1323, 1324, 1328, 1332, 1352, 1353, 1361, 1378, 1381, 1382, 1390, 1391, 1397, 1410, 1413, 1419, 1420, 1434, 1439, 1442, 1450, 1451, 1454, 1463, 1465, 1466, 1470, 1479, 1480, 1487, 1489, 1494, 1495, 1499, 1506, 1509, 1510, 1516, 1518, 1522, 1535, 1538, 1539, 1547, 1551, 1566, 1576, 1595, 1598, 1618, 1619, 1620, 1627, 1637, 1639, 1647, 1648, 1649, 1654, 1655, 1663, 1666, 1668, 1683, 1684, 1695, 1713, 1715, 1724, 1730, 1732, 1742, 1744, 1756, 1759, 1761, 1785, 1806, 1808, 1811, 1826, 1829, 1834, 1835, 1837, 1840, 1851, 1853, 1855, 1858, 1880, 1885, 1887, 1914, 1916, 1922, 1923, 1943, 1948, 1951, 1952, 1972, 1982, 1984, 1997, 1999, 2001, 2004, 2011, 2013, 2022, 2024, 2026, 2028, 2030, 2033, 2042, 2051, 2053, 2056, 2059, 2061, 2071, 2078, 2082, 2085, 2088, 2090, 2091, 2092, 2094, 2107, 2119, 2120, 2121, 2123, 2133, 2134, 2136, 2153, 2154, 2162, 2163, 2165, 2168, 2182, 2183, 2192, 2197, 2212, 2221, 2224, 2225, 2232, 2241, 2251, 2252, 2253, 2254, 2261, 2267, 2280, 2296, 2301, 2330, 2366, 2398, 2404, 2418, 2427, 2433, 2438, 2441, 2447, 2452, 2455, 2456, 2457, 2458, 2459, 2462, 2467, 2470, 2472, 2481, 2484, 2485, 2486, 2487, 2488, 2492, 2499, 2501, 2512, 2521, 2529, 2541, 2550, 2552, 2558, 2569, 2573, 2575, 2579, 2581, 2598, 2602, 2613, 2623, 2626, 2627, 2629, 2649, 2652, 2655, 2656, 2658, 2665, 2666, 2668, 2678, 2684, 2694, 2695, 2697, 2706, 2713, 2725, 2735, 2743, 2744, 2745, 2754, 2759, 2763, 2772, 2773, 2774, 2788, 2792, 2795, 2796, 2800, 2824, 2825, 2829, 2838, 2853, 2855, 2867, 2875, 2876, 2878, 2882, 2884, 2891, 2893, 2896, 2904, 2905, 2907, 2913, 2917, 2920, 2922, 2925, 2930, 2934, 2935, 2942, 2953, 2959, 2963, 2964, 2982, 3011, 3012, 3028, 3040, 3057, 3061, 3063, 3066, 3090, 3092, 3095, 3106, 3118, 3120, 3135, 3137, 3147, 3149, 3156, 3158, 3159, 3166, 3185, 3187, 3188, 3194, 3196, 3197, 3198, 3199, 3200, 3218, 3219, 3223, 3225, 3226, 3227, 3228, 3229, 3247, 3248, 3256, 3259, 3269, 3273, 3274, 3285, 3289, 3292, 3296, 3298, 3302, 3303, 3308, 3310, 3313, 3318, 3321, 3325, 3331, 3337, 3339, 3342, 3350, 3360, 3366, 3370, 3379, 3384, 3391, 3395, 3399, 3402, 3405, 3413, 3420, 3426, 3427, 3429, 3431, 3434, 3443, 3444, 3448, 3455, 3456, 3458, 3466, 3472, 3473, 3477, 3484, 3486, 3495, 3502, 3513, 3515, 3517, 3520, 3521, 3523, 3524, 3531, 3538, 3541, 3542, 3546, 3549, 3550, 3552, 3553, 3561, 3562, 3563, 3567, 3570, 3571, 3578, 3579, 3590, 3591, 3596, 3598, 3599, 3607, 3608, 3612, 3617, 3618, 3621, 3623, 3624, 3625, 3629, 3630, 3631, 3635, 3638, 3641, 3643, 3644, 3645, 3652, 3653, 3654, 3656, 3658, 3659, 3660, 3664, 3666, 3667, 3674, 3680, 3683, 3684, 3691, 3698, 3701, 3707, 3709, 3713, 3714, 3715, 3718, 3721, 3724, 3731, 3732, 3736, 3744, 3747, 3757, 3758, 3761, 3766, 3774, 3777, 3779, 3782, 3783, 3784, 3787, 3801, 3803, 3806, 3808, 3813, 3818, 3820, 3833, 3835, 3842, 3847, 3851, 3852, 3853, 3855, 3858, 3860, 3862, 3865, 3868, 3869, 3870, 3872, 3873, 3876, 3882, 3885, 3887, 3889, 3892, 3894, 3898, 3902, 3905, 3916, 3920, 3921, 3923, 3927, 3931, 3933, 3934, 3935, 3937, 3945, 3949, 3954, 3960, 3962, 3963, 3964, 3966, 3969, 3970, 3971, 3975, 3982, 3983, 3990, 3992, 3993, 3994, 3998, 4006, 4009, 4011, 4019, 4021, 4022, 4023, 4027, 4035, 4038, 4040, 4041, 4044, 4051, 4052, 4056, 4064, 4070, 4073, 4086, 4093, 4115, 4120, 4121, 4123, 4125, 4149, 4150, 4152, 4154, 4155, 4157, 4159, 4161, 4162, 4163, 4164, 4181, 4183, 4184, 4186, 4188, 4190, 4191, 4192, 4195, 4201, 4210, 4215, 4219, 4220, 4224, 4230, 4231, 4244, 4248, 4249, 4251, 4252, 4253, 4259, 4260, 4270, 4274, 4275, 4276, 4280, 4281, 4282, 4290, 4297, 4298, 4302, 4305, 4306, 4309, 4321, 4324, 4326, 4327, 4331, 4334, 4335, 4337, 4338, 4341, 4350, 4353, 4355, 4358, 4359, 4361, 4362, 4364, 4366, 4367, 4370, 4376, 4378, 4379, 4380, 4382, 4384, 4387, 4388, 4390, 4391, 4392, 4396, 4397, 4400, 4405, 4407, 4408, 4409, 4414, 4418, 4421, 4425, 4426, 4429, 4430, 4434, 4435, 4443, 4447, 4452, 4454, 4459, 4463, 4464, 4471, 4472, 4473, 4475, 4481, 4483, 4488, 4493, 4500, 4501, 4502, 4504, 4509, 4510, 4513, 4517, 4522, 4525, 4528, 4530, 4531, 4532, 4533, 4538, 4539, 4542, 4546, 4547, 4552, 4554, 4557, 4559, 4560, 4561, 4562, 4575, 4576, 4581, 4586, 4589, 4603, 4610, 4615, 4618, 4632, 4633, 4634, 4642, 4645, 4649, 4656, 4657, 4658, 4659, 4666, 4667, 4671, 4674, 4679, 4682, 4684, 4688, 4689, 4690, 4691, 4694, 4697, 4699, 4700, 4702, 4705, 4709, 4713, 4714, 4715, 4716, 4728, 4729, 4731, 4734, 4737, 4740, 4741, 4742, 4743, 4744, 4745, 4755, 4758, 4760, 4761, 4762, 4766, 4769, 4770, 4771, 4772, 4773, 4777, 4778, 4779, 4780, 4781, 4782, 4783, 4784, 4787, 4789, 4790, 4791, 4794, 4800, 4802, 4803, 4804, 4807, 4809, 4814, 4820, 4822, 4827, 4828, 4830, 4832, 4833, 4836, 4838, 4841, 4851, 4856, 4857, 4859, 4865]
type5 = [24, 53, 218, 236, 247, 248, 250, 253, 256, 265, 267, 273, 275, 277, 279, 282, 285, 287, 288, 289, 291, 293, 295, 296, 302, 304, 305, 307, 308, 309, 310, 311, 312, 314, 316, 317, 318, 320, 322, 327, 328, 329, 333, 334, 336, 337, 338, 339, 340, 341, 343, 344, 345, 348, 349, 351, 352, 356, 357, 358, 362, 363, 364, 365, 366, 368, 369, 370, 371, 372, 373, 374, 377, 378, 380, 384, 387, 388, 389, 390, 391, 392, 393, 394, 395, 397, 398, 399, 400, 402, 408, 413, 416, 417, 418, 419, 421, 422, 425, 426, 427, 429, 431, 437, 448, 450, 451, 454, 455, 456, 482, 496, 511, 525, 2157, 2207, 2211, 2236, 2240, 2262, 2290, 2291, 2338, 2367, 2402, 2431, 2471, 2480, 2500, 2547, 2576, 2606, 2628, 2635, 2657, 2702, 2731, 2784, 2819, 2841, 2848, 2851, 2879, 2880, 2892, 2916, 2921, 2945, 3003, 3032, 3050, 3099, 3128, 3234, 3239, 3253, 3263, 3268, 3282, 3368, 3397, 3430, 3522, 3551, 3557, 3558, 3586, 3587, 4030, 4059, 4099, 4128, 4233, 4262, 4356, 4385]

# 测试聚类结果的新闻总数是否正确
# total = type1 + type2 + type3 + type4 + type5
# print(len(total))
# total.sort()
# for i in total:
#      if i != total[i]:
#         print("i = " + str(i) + ", total[i] = " + str(total[i]))
# print(total)
# print("total = " + str(len(type1) + len(type2) + len(type3) + len(type4) + len(type5)))

# 用字典储存新闻id与聚类的对应关系(可用函数简化代码)
news_id = news_df['id']
news_type = {}
for i in news_id:
    if i in type1:
        news_type[i] = 1

for i in news_id:
    if i in type2:
        news_type[i] = 2

for i in news_id:
    if i in type3:
        news_type[i] = 3

for i in news_id:
    if i in type4:
        news_type[i] = 4

for i in news_id:
    if i in type5:
        news_type[i] = 5

# 将聚类结果单独按id升序排序储存为数组
# print(len(news_type))
sort_news_type = sorted(news_type.items())
# print(len(sort_news_type))
# print(sort_news_type)
news_type_column = [] # 结果
for item in sort_news_type:
    news_type_column.append(item[1])

# 将聚类数组加至末尾
# print(news_df.shape)
# print(len(news_type_column))
news_df['type'] = news_type_column
# print(news_df)

# 输出为xlsx文件
news_df.to_excel(out_path,index=False)


