brain2paths = {
    "8557": {
        "ab": "precomputed://https://dlab-colm.neurodata.io/2021_10_06/8557/Ch_647",
        "bg": "precomputed://https://dlab-colm.neurodata.io/2021_10_06/8557/Ch_561",
        "endo": "precomputed://https://dlab-colm.neurodata.io/2021_10_06/8557/Ch_488",
    },
    "8555": {
        "ab": "precomputed://https://dlab-colm.neurodata.io/2021_12_2/8555/Ch_647",
        "bg": "precomputed://https://dlab-colm.neurodata.io/2021_12_2/8555/Ch_561",
        "endo": "precomputed://https://dlab-colm.neurodata.io/2021_12_2/8555/Ch_488",
    },
    "8607": {
        "ab": "precomputed://https://dlab-colm.neurodata.io/2021_12_2/8607/Ch_647",
        "bg": "precomputed://https://dlab-colm.neurodata.io/2021_12_2/8607/Ch_561",
        "endo": "precomputed://https://dlab-colm.neurodata.io/2021_12_2/8607/Ch_488",
    },
    "8468": {
        "ab": "precomputed://s3://smartspim-precomputed-volumes/2022_01_19/8468/Ch_647_iso",
        "bg": "precomputed://s3://smartspim-precomputed-volumes/2022_01_19/8468/Ch_561_iso",
        "endo": "precomputed://s3://smartspim-precomputed-volumes/2022_01_19/8468/Ch_488_iso",
    },
    "8606": {
        "ab": "precomputed://s3://smartspim-precomputed-volumes/2022_03_15/8606/Ch_647",
        "bg": "precomputed://s3://smartspim-precomputed-volumes/2022_03_15/8606/Ch_561",
        "endo": "precomputed://s3://smartspim-precomputed-volumes/2022_03_15/8606/Ch_488",
        "vizlink": "https://viz.neurodata.io/?json_url=https://json.neurodata.io/v1?NGStateID=18lUZ-z6xx15Rg",
    },
    "8529": {
        "ab": "precomputed://s3://smartspim-precomputed-volumes/2022_03_02/8529/Ch_647_iso",
        "bg": "precomputed://s3://smartspim-precomputed-volumes/2022_03_02/8529/Ch_561_iso",
        "endo": "precomputed://s3://smartspim-precomputed-volumes/2022_03_02/8529/Ch_488_iso",
        "vizlink": "https://viz.neurodata.io/?json_url=https://json.neurodata.io/v1?NGStateID=IWLsOxwqVpLPew",
    },
    "8477": {
        "ab": "precomputed://s3://smartspim-precomputed-volumes/2022_03_14/8477/Ch_647_iso",
        "bg": "precomputed://s3://smartspim-precomputed-volumes/2022_03_14/8477/Ch_561_iso",
        "endo": "precomputed://s3://smartspim-precomputed-volumes/2022_03_14/8477/Ch_488_iso",
        "vizlink": "https://viz.neurodata.io/?json_url=https://json.neurodata.io/v1?NGStateID=Dqm1DQwl5pPmDg",
    },
    "8531": {
        "ab": "precomputed://s3://smartspim-precomputed-volumes/2022_03_10/8531/Ch_647_iso",
        "bg": "precomputed://s3://smartspim-precomputed-volumes/2022_03_10/8531/Ch_561_iso",
        "endo": "precomputed://s3://smartspim-precomputed-volumes/2022_03_10/8531/Ch_488_iso",
        "vizlink": "https://viz.neurodata.io/?json_url=https://json.neurodata.io/v1?NGStateID=42tANDn1cjREEA",
    },
}

# first entry is somas, second is nonsomas
brain2centers = {
    "8557": [
        [
            [
                [
                    2011.743408203125,
                    2835.38671875,
                    1535.5,
                ],  # first 10 train, second 10 test, 3rd 10 train, 4th 10 test
                [2430.76171875, 3053.81494140625, 713.5],
                [1780.8623046875, 2691.490234375, 1538.5001220703125],
                [1642.8656005859375, 3693.246337890625, 1540.4998779296875],
                [1924.112060546875, 2812.427978515625, 1539.5],
                [2228.993896484375, 3124.892333984375, 710.4999389648438],
                [976.0220336914062, 2615.152587890625, 1295.4998779296875],
                [2246.654296875, 4579.09912109375, 1681.5],
                [2383.7158203125, 2945.70166015625, 768.5000610351562],
                [2287.11474609375, 3137.698486328125, 713.5],
                [3852.977783203125, 5670.54296875, 1325.5],
                [785.1561889648438, 2881.677978515625, 1418.5],
                [3049.8564453125, 5896.8427734375, 1018.5],
                [3077.5703125, 4926.2783203125, 1903.4998779296875],
                [1411.1312255859375, 4952.9912109375, 1653.4998779296875],
                [2617.185546875, 3935.150146484375, 1544.5],
                [1847.7435302734375, 3412.42529296875, 1539.5],
                [2568.662109375, 4020.066162109375, 1544.5],
                [2636.25927734375, 2863.755615234375, 956.5],
                [3214.722412109375, 5058.56689453125, 1903.4998779296875],
                [3381.364501953125, 5440.7744140625, 716.5],
                [2136.887451171875, 3078.10009765625, 712.4999389648438],
                [3805.26220703125, 5721.7451171875, 951.5000610351562],
                [2653.3818359375, 5837.59521484375, 894.5],
                [3070.020263671875, 3609.991943359375, 1418.5001220703125],
                [2138.659423828125, 2925.73681640625, 998.5000610351562],
                [3354.067626953125, 4763.74365234375, 706.5],
                [3323.818603515625, 5509.31494140625, 1012.5],
                [2382.930908203125, 5729.60888671875, 865.5],
                [2535.490234375, 2913.681396484375, 1531.5001220703125],
                [2822.101318359375, 5940.8447265625, 870.4999389648438],
                [3124.767578125, 3648.263427734375, 1415.5],
                [1567.5830078125, 2865.05859375, 1543.5],
                [1854.7235107421875, 3435.424072265625, 707.5],
                [1830.0322265625, 3484.5322265625, 708.5],
                [2262.647705078125, 5039.2021484375, 1647.5001220703125],
                [3200.597412109375, 5456.03173828125, 1322.5],
                [3243.903564453125, 4821.22607421875, 1903.4998779296875],
                [1673.142822265625, 3517.357666015625, 1540.5],
                [2999.173095703125, 4204.28271484375, 1639.5],
                [3006.562744140625, 4938.923828125, 1900.4998779296875],
                [2886.84716796875, 4451.986328125, 1665.5],
                [2811.046142578125, 5642.18701171875, 1671.5],
                [2037.578125, 4099.0029296875, 1909.4998779296875],
                [2907.236083984375, 4148.60107421875, 1664.5],
                [1602.658447265625, 5768.17724609375, 1487.5001220703125],
                [3856.97119140625, 4785.84375, 857.5],
                [1390.650390625, 3785.47607421875, 965.5],
                [1575.3089599609375, 2840.33544921875, 1542.5],
                [3515.720458984375, 5792.529296875, 1298.5],
                [2600.551513671875, 4095.101806640625, 1625.5001220703125],
                [3057.936767578125, 4192.6103515625, 1639.5],
                [3038.3564453125, 5691.2783203125, 683.5],
                [846.10400390625, 2795.954833984375, 1418.5],
                [2105.562744140625, 3077.30859375, 1352.5001220703125],
                [1439.8948974609375, 3693.8486328125, 730.4999389648438],
                [3055.538330078125, 4010.5537109375, 1539.4998779296875],
                [3415.8681640625, 5375.50439453125, 1374.5],
                [3523.255126953125, 3717.175048828125, 1638.5],
                [2503.846923828125, 3003.74267578125, 1541.5001220703125],
                [1884.9224853515625, 2402.20849609375, 1678.5],
                [3248.570068359375, 5417.93310546875, 688.5],
                [2692.116455078125, 4005.279052734375, 1538.5],
                [3563.275634765625, 3705.658447265625, 1649.4998779296875],
                [2643.770751953125, 5856.18603515625, 1472.5001220703125],
                [2928.4404296875, 4202.427734375, 1675.5],
                [953.2669677734375, 2733.28125, 1309.5001220703125],
                [3091.98779296875, 3658.0458984375, 1415.5],
                [1855.5592041015625, 2653.33349609375, 1537.5],
                [1412.1038818359375, 3816.89013671875, 944.5],
                [2335.27001953125, 6059.69287109375, 1400.5001220703125],
                [1119.7874755859375, 2634.51416015625, 1298.5],
                [1957.525146484375, 4067.762939453125, 1902.5],
                [942.6224975585938, 2604.65576171875, 1289.5],
                [1973.50634765625, 2371.421142578125, 1679.5],
                [2820.294921875, 4667.92822265625, 1910.5],
                [3765.234375, 5184.81494140625, 945.5000610351562],
                [3022.6396484375, 3871.55029296875, 1821.5001220703125],
                [3415.100341796875, 4669.4833984375, 1899.5],
                [1424.1728515625, 3417.180419921875, 1546.5001220703125],
                [3486.880615234375, 5367.294921875, 691.5],
                [3473.42138671875, 4550.96630859375, 1674.4998779296875],
                [3116.014892578125, 3670.91748046875, 1420.5001220703125],
                [2862.326416015625, 4161.21630859375, 1652.5],
                [3097.629638671875, 4741.66015625, 2023.5],
                [1919.5633544921875, 3037.014892578125, 715.5],
                [1947.3941650390625, 2633.284912109375, 1526.4998779296875],
                [2806.36083984375, 3986.090576171875, 1539.4998779296875],
                [2474.282958984375, 3113.071044921875, 713.5],
                [2144.11767578125, 3158.352783203125, 1352.5001220703125],
                [2958.302490234375, 2309.1650390625, 984.5],
                [3150.5234375, 4555.67626953125, 1900.4998779296875],
                [2712.485595703125, 3920.850341796875, 1549.4998779296875],
                [3850.980712890625, 4883.8349609375, 864.4999389648438],
                [3039.634765625, 4971.02294921875, 1903.4998779296875],
                [3015.31689453125, 4547.89453125, 1902.499755859375],
                [2083.13671875, 4309.87451171875, 1899.5],
                [3471.501953125, 4553.08544921875, 1656.4998779296875],
                [2458.521240234375, 3214.04345703125, 713.5],
                [3287.51318359375, 5237.70654296875, 709.5000610351562],
            ],
            [
                [3596, 5609, 803],  # first 2 train second 2 test
                [2598, 5486, 770],
                [2652, 5673, 786],
                [2303, 2849, 749],
            ],
            [
                [2318.09521484375, 2485.178955078125, 1527.5],
                [1635.3116455078125, 2331.905517578125, 1768.5],
                [2193.0791015625, 2726.747802734375, 1211.5],
                [2409.182861328125, 2669.866943359375, 1341.5],
                [1743.907470703125, 2388.040771484375, 1767.5001220703125],
                [2157.878173828125, 2805.24755859375, 1369.4998779296875],
                [2098.080322265625, 2730.603271484375, 1372.5],
                [2003.1942138671875, 2934.714599609375, 1665.5],
                [1617.6641845703125, 2868.2744140625, 1605.5],
                [2124.177001953125, 2696.021240234375, 1214.4998779296875],
                [2039.519775390625, 2760.2958984375, 1369.4998779296875],
                [2288.05224609375, 2662.501220703125, 1218.5],
                [2274.144775390625, 2496.862548828125, 1660.5001220703125],
                [1894.0166015625, 2491.237060546875, 1619.5],
                [1907.9498291015625, 2203.0966796875, 1768.5],
                [1956.9765625, 2558.140625, 1524.5],
                [2535.978759765625, 2914.857421875, 1531.5],
                [1780.215087890625, 2691.882568359375, 1536.5],
                [2075.762451171875, 2779.568603515625, 1755.4998779296875],
                [2055.613525390625, 2577.921875, 1609.5001220703125],
                [1520.401123046875, 2948.193359375, 1763.5],
                [1680.18408203125, 2866.0986328125, 1531.5],
                [2158.89013671875, 2810.61328125, 1759.5],
                [1659.9925537109375, 2911.289306640625, 1526.5001220703125],
                [1883.435302734375, 2400.013671875, 1642.5001220703125],
                [2051.018798828125, 2541.380615234375, 1522.5],
                [2207.011474609375, 2611.92333984375, 1530.5],
                [1855.024658203125, 2652.99853515625, 1537.5001220703125],
                [1714.272216796875, 2647.7744140625, 1904.5001220703125],
                [1945.9052734375, 2710.395751953125, 1345.4998779296875],
                [1767.45751953125, 2664.34033203125, 1898.5001220703125],
                [1650.673828125, 2605.89453125, 1644.5],
                [1785.98876953125, 2738.3974609375, 1374.5],
                [2318.779052734375, 2721.1611328125, 1217.5],
                [1936.9541015625, 2587.83251953125, 1909.5],
                [2036.6278076171875, 2621.339111328125, 1764.5],
                [1970.27783203125, 2762.362548828125, 1783.4998779296875],
                [1582.7296142578125, 2859.6044921875, 1598.5001220703125],
                [1972.7930908203125, 2370.911865234375, 1661.5],
                [2091.961669921875, 2580.457763671875, 1613.5001220703125],
                [1897.4464111328125, 2672.50146484375, 1529.5],
                [1654.885986328125, 2980.4580078125, 1376.4998779296875],
                [2183.41796875, 2695.958740234375, 1537.5001220703125],
                [2066.1376953125, 2855.551513671875, 1214.4998779296875],
                [1749.412353515625, 2913.853515625, 1531.5],
                [1632.429443359375, 2872.829345703125, 1528.5],
                [2433.615966796875, 2691.986328125, 1217.5],
                [1883.190673828125, 2400.920166015625, 1659.5001220703125],
                [1499.0296630859375, 2925.872314453125, 1374.4998779296875],
                [1531.9852294921875, 2859.349365234375, 1584.5],
                [1960.080322265625, 2679.495361328125, 1528.5],
                [1991.217529296875, 2661.793701171875, 1608.5],
                [1981.2701416015625, 2693.5009765625, 1608.5],
                [2260.4736328125, 3006.7529296875, 1211.5],
                [1440.1346435546875, 2903.248046875, 1373.5],
                [2010.471923828125, 2836.4697265625, 1535.5001220703125],
                [1580.5489501953125, 2845.78955078125, 1371.4998779296875],
                [1854.3056640625, 2653.375732421875, 1530.5],
                [1758.447998046875, 2692.822021484375, 1914.5],
                [2063.34423828125, 2899.00341796875, 1208.5],
                [1647.9302978515625, 2444.91357421875, 1926.5001220703125],
            ],
        ],
        [  # nonsomas
            [
                [3717.254150390625, 4600.33984375, 2236.5],  # first10 train next 9 test
                [2405.4306640625, 3981.74853515625, 799.4999389648438],
                [2450.216064453125, 2035.8717041015625, 1388.5],
                [1393.8924560546875, 2702.320068359375, 907.5],
                [2197.689208984375, 5329.3505859375, 1559.4998779296875],
                [2732.838134765625, 3567.6171875, 1556.4998779296875],
                [901.0664672851562, 4493.27197265625, 1695.4998779296875],
                [2473.236328125, 3967.60546875, 907.5000610351562],
                [1349.7891845703125, 4999.54443359375, 1699.5],
                [3879.52734375, 5786.0390625, 1399.5],
                [1820.3192138671875, 4988.37841796875, 799.4999389648438],
                [1743.709716796875, 2824.9189453125, 1373.5],
                [3654.88720703125, 4952.98291015625, 1387.4998779296875],
                [2422.846435546875, 5315.03271484375, 1702.5],
                [1102.1307373046875, 1870.1595458984375, 1854.5001220703125],
                [3086.711181640625, 4087.082763671875, 1875.5],
                [3545.043212890625, 5263.32861328125, 1387.5],
                [3005.282470703125, 3506.512451171875, 1550.5],
                [2897.065185546875, 3204.1494140625, 1300.5001220703125],
                [
                    3501.636474609375,
                    3396.54638671875,
                    1537.499755859375,
                ],  # next 10 for train
                [
                    852.2304077148438,
                    4556.865234375,
                    1541.5001220703125,
                ],
                [881.656982421875, 2553.561767578125, 2226.5],
                [
                    3084.20849609375,
                    4085.383544921875,
                    1904.5,
                ],
                [
                    2670.98974609375,
                    3177.840576171875,
                    1496.5001220703125,
                ],
                [
                    2604.623046875,
                    1348.0390625,
                    1502.5,
                ],
                [
                    443.4283142089844,
                    2811.697998046875,
                    1529.4998779296875,
                ],
                [
                    2242.6259765625,
                    4298.91259765625,
                    1529.5001220703125,
                ],
                [
                    2363.44384765625,
                    5047.8857421875,
                    1066.5,
                ],
                [
                    4287.8984375,
                    4006.61767578125,
                    1069.5,
                ],
            ],
            [
                [518, 4516, 3001],  # first 5 train second 5 test
                [2287, 4660, 3001],
                [451, 5893, 3210],
                [518, 4421, 3268],
                [1311, 6546, 3268],
                [3918, 5896, 796],
                [378, 6549, 3270],
                [30, 6212, 3270],
                [401, 6266, 3270],
                [92, 6539, 3270],
            ],
            [
                [
                    1627.2305908203125,
                    4896.90966796875,
                    795.5000610351562,
                ],  # first 5 train
                [2523.58984375, 4272.1826171875, 961.5],
                [1682.463623046875, 5623.48583984375, 1587.4998779296875],
                [
                    2101.8681640625,
                    3492.00439453125,
                    1542.5001220703125,
                ],
                [
                    2178.76904296875,
                    2596.552734375,
                    1538.5001220703125,
                ],
                [
                    1359.5174560546875,
                    782.538330078125,
                    2442.5,
                ],  # next 6 test
                [3000.8994140625, 1582.5877685546875, 1324.5],
                [
                    2150.790771484375,
                    5722.9775390625,
                    1364.5,
                ],
                [
                    757.184326171875,
                    5052.00830078125,
                    1364.5,
                ],
                [2655, 2438, 1521],
                [3482, 4189, 1496],
            ],
        ],
    ],
    "8555": [
        [
            [
                [4256.267578125, 5383.6376953125, 1950.4998779296875],  # first 10 test
                [2956.0263671875, 1910.708984375, 1891.5],
                [2692.0771484375, 2204.79931640625, 1892.5],
                [2142.25244140625, 2135.18994140625, 1907.5001220703125],
                [3237.661865234375, 5790.5009765625, 1859.4998779296875],
                [3121.011962890625, 6361.93408203125, 1692.5],
                [3252.493896484375, 2362.432373046875, 2100.499755859375],
                [3190.64794921875, 2247.239501953125, 2101.5],
                [1991.2828369140625, 2464.6015625, 2106.5],
                [891.5779418945312, 4202.66552734375, 1717.5],
                [2753.240478515625, 3586.9443359375, 1686.5],  # second 10 train
                [3247.01806640625, 3563.534912109375, 1689.5],
                [3335.767333984375, 3457.741455078125, 1689.5],
                [2703.674560546875, 6272.76123046875, 1647.5],
                [3147.158203125, 6402.54345703125, 1636.5],
                [2528.369873046875, 1840.259033203125, 1643.4998779296875],
                [2293.098876953125, 2016.0142822265625, 1636.4998779296875],
                [2372.586181640625, 1975.3580322265625, 1635.5001220703125],
                [2990.31103515625, 1779.50048828125, 1641.4998779296875],
                [3044.330078125, 1976.0841064453125, 1641.4998779296875],
            ],
        ],
        [
            [
                [2297.11279296875, 4473.45263671875, 1717.5],  # first 10 test
                [1791.894775390625, 4388.5166015625, 1717.5],
                [3208.728515625, 6492.125, 1802.4998779296875],
                [2674.0478515625, 877.765625, 1708.4998779296875],
                [2408.22216796875, 703.9223022460938, 1708.5],
                [4116.11181640625, 4527.5810546875, 1725.4998779296875],
                [5517.99560546875, 3281.881103515625, 1731.5],
                [5121.599609375, 3508.56201171875, 1731.5],
                [974.9075317382812, 3781.5888671875, 1719.5],
                [4277.98876953125, 5606.38037109375, 1757.5],
                [
                    744.5549926757812,
                    2463.279541015625,
                    1639.5001220703125,
                ],  # second 10 train
                [4825.396484375, 4241.51025390625, 2440.499755859375],
                [2332.400634765625, 4129.59375, 2414.5],
                [2031.938720703125, 4381.470703125, 2414.5],
                [2293.27294921875, 4838.482421875, 2414.500244140625],
                [4630.88671875, 5999.6953125, 971.5],
                [2196.729248046875, 6003.4013671875, 971.5000610351562],
                [1868.711181640625, 790.8681030273438, 971.5],
                [1568.2215576171875, 748.6834716796875, 475.5000305175781],
                [3462.517822265625, 3661.1572265625, 477.50006103515625],
            ]
        ],
    ],
    "8607": [
        [
            [
                [3923.309814453125, 1490.7852783203125, 1574.5],  # first 10 test
                [3912.675048828125, 1582.424072265625, 1573.5],
                [3972.31884765625, 1636.0765380859375, 1575.5],
                [4029.65673828125, 1626.795166015625, 1579.5001220703125],
                [3485.149169921875, 1350.9903564453125, 1576.5],
                [2720.345458984375, 1256.7242431640625, 1566.5001220703125],
                [2662.961181640625, 1080.000732421875, 1523.4998779296875],
                [2537.82763671875, 1115.92041015625, 1469.5],
                [1351.3319091796875, 2902.065185546875, 1471.5001220703125],
                [1510.79052734375, 3041.47802734375, 1469.5],
                [1436.2779541015625, 3112.0107421875, 1470.5],
                [2587.204345703125, 3733.973388671875, 1470.5],
                [2627.138427734375, 3716.552490234375, 1472.5001220703125],
                [2706.06884765625, 3817.862060546875, 1480.500244140625],
                [2536.62890625, 3735.08251953125, 1475.5001220703125],
                [2557.787353515625, 3826.930419921875, 1486.5],
                [2693.40234375, 3753.0458984375, 1483.5],
                [2748.80322265625, 3737.8271484375, 1480.5],
                [2917.288330078125, 3788.912109375, 1481.4998779296875],
                [990.8594970703125, 4578.4091796875, 1481.4998779296875],
                [895.0261840820312, 4683.11083984375, 1492.5],
                [1972.852294921875, 5634.7431640625, 1501.4998779296875],
                [2154.2177734375, 5271.3701171875, 1503.5],
                [2517.465087890625, 2666.370849609375, 2397.499755859375],
                [2663.596923828125, 2479.174072265625, 2388.5],
                [2751.21728515625, 2366.7353515625, 2378.499755859375],
                [2052.651611328125, 2221.338623046875, 2377.5],
                [2141.46044921875, 4056.967041015625, 2375.5],
                [2274.8681640625, 4040.199951171875, 2377.5],
                [1452.4447021484375, 3663.112060546875, 2378.5],
                [1446.770751953125, 3702.18505859375, 2379.5],
                [1114.31494140625, 3384.252197265625, 2380.5],
                [1400.34716796875, 3390.469970703125, 2376.5],
                [1353.8094482421875, 3410.3779296875, 2366.499755859375],
                [2813.72265625, 5092.12353515625, 2537.5],
                [2793.09716796875, 4691.53759765625, 2447.499755859375],
                [2111.962158203125, 3808.759033203125, 2407.499755859375],
                [1626.752197265625, 3443.947509765625, 2396.5],
                [2873.197998046875, 3137.03564453125, 787.5],
                [2863.83740234375, 3039.789306640625, 787.5],
                [2678.880859375, 3153.294677734375, 789.5],
                [2266.440185546875, 3096.909423828125, 788.5],
                [2048.507568359375, 3178.971923828125, 788.5],
                [2076.322998046875, 3160.12939453125, 783.4999389648438],
                [2078.715576171875, 3056.0458984375, 783.4999389648438],
                [2112.213623046875, 3073.9912109375, 783.4999389648438],
                [1999.1575927734375, 3019.556884765625, 783.4999389648438],
                [2216.365966796875, 2996.19580078125, 783.4999389648438],
                [2269.138427734375, 2904.182373046875, 783.4999389648438],
                [2380.907958984375, 2886.32080078125, 783.4999389648438],
                [2935.327392578125, 2567.49951171875, 783.4999389648438],
                [2719.227294921875, 2489.011962890625, 790.4999389648438],
                [2728.90869140625, 2390.47021484375, 790.4999389648438],
                [2298.62109375, 1337.2855224609375, 787.5],
                [3797.217041015625, 2726.20068359375, 693.5],
                [3781.20703125, 2646.897705078125, 697.4999389648438],
                [2134.492919921875, 1481.8536376953125, 656.5000610351562],
                [1072.88427734375, 1969.1795654296875, 1333.5],
                [1127.2364501953125, 1861.7392578125, 1333.5],
                [890.94189453125, 2259.278076171875, 1337.5],
                [1680.106201171875, 1436.3148193359375, 1315.5],
                [1777.1837158203125, 1365.872314453125, 1313.5],
                [4006.6025390625, 1637.9608154296875, 1313.5001220703125],
                [3945.90380859375, 1679.582763671875, 1313.5001220703125],
                [4155.97216796875, 2956.021728515625, 1310.5],
                [3607.488525390625, 3676.251220703125, 1310.5],
                [2691.33544921875, 3501.38818359375, 1312.5],
                [2815.258056640625, 3501.406982421875, 1312.5],
                [2920.0322265625, 976.1478271484375, 1299.4998779296875],
                [4015.35009765625, 1854.82275390625, 1501.4998779296875],
                [4015.634765625, 1540.1451416015625, 1501.5001220703125],
            ]
        ],
        [
            [
                [3615.2509765625, 1540.1510009765625, 1508.5],  # first 10 test
                [3815.814697265625, 1166.3028564453125, 1501.5],
                [4195.56103515625, 1115.5001220703125, 1501.4998779296875],
                [1006.802734375, 1750.7830810546875, 1516.4998779296875],
                [856.7860107421875, 2503.805419921875, 1516.5001220703125],
                [2224.43798828125, 2264.25732421875, 1454.5],
                [3093.23095703125, 5162.31298828125, 1470.5001220703125],
                [4048.682373046875, 3907.422119140625, 1446.5001220703125],
                [2930.699951171875, 2955.205078125, 1446.5],
                [231.4591522216797, 3921.257568359375, 1488.5],
                [4190.6064453125, 1176.6483154296875, 798.5],
                [2896.87548828125, 586.461181640625, 798.5],
                [3541.799560546875, 3457.042236328125, 609.5000610351562],
                [3238.160400390625, 2231.261962890625, 604.5],
                [2103.206787109375, 1914.586669921875, 552.5],
                [2199.031982421875, 3135.140625, 581.5],
                [2248.79638671875, 2939.645751953125, 584.5],
                [3935.2802734375, 2489.034912109375, 587.4999389648438],
                [2775.91015625, 3113.589599609375, 2574.500244140625],
                [2939.407958984375, 2627.815185546875, 2625.499755859375],
                [2405.598388671875, 3884.212890625, 2681.500244140625],
                [1919.37646484375, 3424.30224609375, 2677.500244140625],
                [1627.232666015625, 3716.60791015625, 2677.5],
                [1340.1866455078125, 4673.443359375, 2677.5],
                [1173.817626953125, 2691.956298828125, 2677.5],
                [2101.3681640625, 2532.558349609375, 2645.5],
                [1970.875732421875, 2317.755859375, 2644.5],
                [3299.53857421875, 2921.47900390625, 2646.5],
                [2302.12744140625, 2052.287353515625, 1691.4998779296875],
                [2357.10791015625, 2132.09765625, 1691.4998779296875],
                [4079.69970703125, 1487.0792236328125, 1730.5001220703125],
                [3825.9755859375, 1217.6103515625, 1732.5001220703125],
                [427.88677978515625, 3974.369140625, 1636.5001220703125],
                [988.5870361328125, 4249.9462890625, 1636.5001220703125],
                [1497.3358154296875, 5245.5009765625, 1636.4998779296875],
                [2349.62646484375, 5215.95751953125, 1636.5],
                [2713.1923828125, 3243.998779296875, 1636.499755859375],
            ]
        ],
    ],
}
