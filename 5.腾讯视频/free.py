'''免费视频
影视数据、网课基本都是m3u8流媒体数据
1、视频解析网站：https://jx.vcs6.com/
2、腾讯视频随便一个视频 ，例如：https://v.qq.com/x/cover/324olz7ilvo2j5f/i00350r6rf4.html
3、打开视频，按F12，network中的media如果找不到资源，则在所有资源包中搜索m3u8
4、找到m3u8文件，以下为示例m3u8资源：
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-TARGETDURATION:17
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:12.000,
00_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=0&start=0&end=12000&brs=0&bre=1102995&ver=4&token=a95a6a08128bfb4e4cf26a178a570b18
#EXTINF:10.600,
01_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=1&start=12000&end=22600&brs=1102996&bre=1343635&ver=4&token=8a42e364c74a53ef0f6b4a95472d4cb1
#EXTINF:11.033,
02_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=2&start=22600&end=33633&brs=1343636&bre=1702527&ver=4&token=d596db59d4551c4a0e9f4ce4e7c492f0
#EXTINF:11.933,
03_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=3&start=33633&end=45566&brs=1702528&bre=3987291&ver=4&token=6570ca4b7f6182432134043c9040192a
#EXTINF:12.000,
04_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=4&start=45566&end=57566&brs=3987292&bre=6241035&ver=4&token=8ff68d875044c048e89c7782183ad4d7
#EXTINF:11.034,
05_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=5&start=57566&end=68600&brs=6241036&bre=10870347&ver=4&token=06631eed4527734e33c31c5480d39f35
#EXTINF:12.000,
06_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=6&start=68600&end=80600&brs=10870348&bre=15007475&ver=4&token=0a898cb6d6a37ab1e53328a8c876013a
#EXTINF:11.666,
07_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=7&start=80600&end=92266&brs=15007476&bre=17154999&ver=4&token=d518fa1a71266462192b1ec2bb6b001c
#EXTINF:12.000,
08_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=8&start=92266&end=104266&brs=17155000&bre=19417391&ver=4&token=f1441ea96c60aa02b1ea0569bcbde5d9
#EXTINF:12.000,
09_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=9&start=104266&end=116266&brs=19417392&bre=20963315&ver=4&token=bb3e176d7556c697f9639392a0c80278
#EXTINF:12.000,
010_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=10&start=116266&end=128266&brs=20963316&bre=23413895&ver=4&token=79a02363f8ad0cd59072ef5b6602cd4c
#EXTINF:12.000,
011_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=11&start=128266&end=140266&brs=23413896&bre=25071303&ver=4&token=baf1b1e29f82eb56ffb7ec2fb5324e69
#EXTINF:11.367,
012_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=12&start=140266&end=151633&brs=25071304&bre=28347767&ver=4&token=8e6573a10e84383a62daa55ebc6f72ae
#EXTINF:11.833,
013_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=13&start=151633&end=163466&brs=28347768&bre=30677651&ver=4&token=341603d9c81d79312e0174fe89332ac6
#EXTINF:11.934,
014_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=14&start=163466&end=175400&brs=30677652&bre=34090415&ver=4&token=694a62f0029760eff298b0637e915fef
#EXTINF:12.000,
015_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=15&start=175400&end=187400&brs=34090416&bre=37457307&ver=4&token=931d2c8d0e7b0a9c91e460e2a847ff81
#EXTINF:12.000,
016_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=16&start=187400&end=199400&brs=37457308&bre=40343671&ver=4&token=281e3b7d2d14c2b570387d90b5cca31c
#EXTINF:12.000,
017_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=17&start=199400&end=211400&brs=40343672&bre=45467987&ver=4&token=2f808a0e0f25febde0f51216d8800f2c
#EXTINF:12.000,
018_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=18&start=211400&end=223400&brs=45467988&bre=46583203&ver=4&token=7f34b7513076612cea176f0a2a201ba1
#EXTINF:12.000,
019_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=19&start=223400&end=235400&brs=46583204&bre=47281811&ver=4&token=053a43dd5a84c65883aaf596d1b45ad9
#EXTINF:12.000,
020_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=20&start=235400&end=247400&brs=47281812&bre=48430491&ver=4&token=c78725017e281556baf0b6ff72ca876f
#EXTINF:11.700,
021_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=21&start=247400&end=259100&brs=48430492&bre=50759059&ver=4&token=b277ffce3e4d18f260cce7e60c1fd75e
#EXTINF:12.000,
022_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=22&start=259100&end=271100&brs=50759060&bre=53165835&ver=4&token=11f358c2378b3f3ec356ec96c3a1ff22
#EXTINF:12.000,
023_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=23&start=271100&end=283100&brs=53165836&bre=54601591&ver=4&token=bfdf48e0ae7b44164072ea2150084184
#EXTINF:12.000,
024_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=24&start=283100&end=295100&brs=54601592&bre=56240011&ver=4&token=8349517437c89f3da86fee57bfa81e69
#EXTINF:11.666,
025_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=25&start=295100&end=306766&brs=56240012&bre=57169295&ver=4&token=38e22b3c35782ab1a860656589240d41
#EXTINF:12.000,
026_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=26&start=306766&end=318766&brs=57169296&bre=58287331&ver=4&token=2baa9d05f697ea85595ad9dafacb5dfd
#EXTINF:12.000,
027_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=27&start=318766&end=330766&brs=58287332&bre=59855439&ver=4&token=caa8faf60ddd1107bfa326bbf2a4c80f
#EXTINF:11.100,
028_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=28&start=330766&end=341866&brs=59855440&bre=61044539&ver=4&token=8e6d01f14e9c6f9f1aa448824f49a8a0
#EXTINF:12.000,
029_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.1.ts?index=29&start=341866&end=353866&brs=61044540&bre=62165959&ver=4&token=48977afae44f4e1a13a0c4fac477b660
#EXTINF:11.934,
030_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=30&start=353866&end=365800&brs=0&bre=1162403&ver=4&token=476cf8500984735b11fc637771e4eadb
#EXTINF:11.566,
031_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=31&start=365800&end=377366&brs=1162404&bre=2551911&ver=4&token=03d7efe866ae2d6c19a43bb7fc5fe774
#EXTINF:12.000,
032_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=32&start=377366&end=389366&brs=2551912&bre=4643975&ver=4&token=eb851f26fc18e3838305c5f15048454e
#EXTINF:10.567,
033_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=33&start=389366&end=399933&brs=4643976&bre=6458551&ver=4&token=243220289bf944cdf5886c77f7877f03
#EXTINF:11.267,
034_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=34&start=399933&end=411200&brs=6458552&bre=8441387&ver=4&token=7c5a32339eb475bab90011075fb87d13
#EXTINF:11.533,
035_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=35&start=411200&end=422733&brs=8441388&bre=10577819&ver=4&token=9102241dcadaf26ef144bfb8618340eb
#EXTINF:12.000,
036_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=36&start=422733&end=434733&brs=10577820&bre=12021659&ver=4&token=353aa33d77fb4001b697b6e0d05be191
#EXTINF:11.167,
037_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=37&start=434733&end=445900&brs=12021660&bre=14763263&ver=4&token=6d4df785b96381ed4472265d36ed9b25
#EXTINF:11.633,
038_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=38&start=445900&end=457533&brs=14763264&bre=18817483&ver=4&token=cc8bb67c4b3ac10a77dea9a9eac7e8a1
#EXTINF:11.233,
039_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=39&start=457533&end=468766&brs=18817484&bre=21799915&ver=4&token=5cc059f211b117861eba1527578659e1
#EXTINF:11.534,
040_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=40&start=468766&end=480300&brs=21799916&bre=24645107&ver=4&token=8fb958c1081ecb41eef6194d0f8bb748
#EXTINF:11.233,
041_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=41&start=480300&end=491533&brs=24645108&bre=27494435&ver=4&token=51ec392a36aa3ab3625d34bc961af6d8
#EXTINF:11.000,
042_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=42&start=491533&end=502533&brs=27494436&bre=30636479&ver=4&token=9c8d1fc62cccd83e5b42aead943f3252
#EXTINF:10.867,
043_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=43&start=502533&end=513400&brs=30636480&bre=33340671&ver=4&token=f3f7dfcd61ab1c267c0dcd12bff5abe9
#EXTINF:10.633,
044_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=44&start=513400&end=524033&brs=33340672&bre=36504711&ver=4&token=9f2e4d4fadd1d9c5ea7304dae61b59c2
#EXTINF:11.700,
045_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=45&start=524033&end=535733&brs=36504712&bre=38875391&ver=4&token=d7fb10c4fdfad03fb982c1306936f160
#EXTINF:12.000,
046_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=46&start=535733&end=547733&brs=38875392&bre=40873455&ver=4&token=9b6c17f80d26540b6fa16c8ac6d14c40
#EXTINF:11.000,
047_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=47&start=547733&end=558733&brs=40873456&bre=42545151&ver=4&token=a8888ccf3bc429b32f13ca86105ce7cf
#EXTINF:11.167,
048_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=48&start=558733&end=569900&brs=42545152&bre=43745155&ver=4&token=a95e291dd119a03dee7f34e15c77faf9
#EXTINF:12.000,
049_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=49&start=569900&end=581900&brs=43745156&bre=44890639&ver=4&token=e13deacce27c15add9686c2bbea080cd
#EXTINF:11.433,
050_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=50&start=581900&end=593333&brs=44890640&bre=46050787&ver=4&token=6c3ee2c219957e9ac58146f5500610a2
#EXTINF:11.467,
051_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=51&start=593333&end=604800&brs=46050788&bre=47861415&ver=4&token=c4ca3af3491096384b8847190d5f1360
#EXTINF:12.000,
052_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=52&start=604800&end=616800&brs=47861416&bre=49312211&ver=4&token=4a1fc9633add52c9f1e592819af74a77
#EXTINF:11.700,
053_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=53&start=616800&end=628500&brs=49312212&bre=50317447&ver=4&token=e07a3e0ab3d483696e34c1ccdf40a7c5
#EXTINF:12.000,
054_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=54&start=628500&end=640500&brs=50317448&bre=51395439&ver=4&token=a8fb618cfe901180f46e56f422e4dccc
#EXTINF:12.000,
055_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=55&start=640500&end=652500&brs=51395440&bre=53141207&ver=4&token=e2101d7dc78968c58a7538049409ad02
#EXTINF:12.000,
056_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=56&start=652500&end=664500&brs=53141208&bre=54726235&ver=4&token=cece60eeee59c052f69436bf3bd3c429
#EXTINF:11.700,
057_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=57&start=664500&end=676200&brs=54726236&bre=56846123&ver=4&token=fe63a6c44924aade76d1c802d72ed11e
#EXTINF:11.266,
058_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=58&start=676200&end=687466&brs=56846124&bre=58434723&ver=4&token=5465851e52ca8afc29b0390ad5da9846
#EXTINF:11.867,
059_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.2.ts?index=59&start=687466&end=699333&brs=58434724&bre=61172003&ver=4&token=e076a91da3caa74fa9ef87f6d2210194
#EXTINF:11.167,
060_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=60&start=699333&end=710500&brs=0&bre=1612475&ver=4&token=b6f7f565a707dd5f708dac8d27550412
#EXTINF:11.166,
061_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=61&start=710500&end=721666&brs=1612476&bre=3698335&ver=4&token=054b7eee30f2807c18bd1b58b2d1f1c9
#EXTINF:10.267,
062_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=62&start=721666&end=731933&brs=3698336&bre=6773263&ver=4&token=6fa6d1149639c6c49b33c5a2e8dde76e
#EXTINF:11.767,
063_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=63&start=731933&end=743700&brs=6773264&bre=8413375&ver=4&token=a9673c6118c962333ba1aaf4aedd1875
#EXTINF:11.133,
064_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=64&start=743700&end=754833&brs=8413376&bre=9835783&ver=4&token=69b15cfe632eceb96c585e66709d042a
#EXTINF:12.000,
065_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=65&start=754833&end=766833&brs=9835784&bre=12070539&ver=4&token=a202c8f08ba62976e7a0880b475f82be
#EXTINF:12.000,
066_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=66&start=766833&end=778833&brs=12070540&bre=13938131&ver=4&token=1d4d4c642e835467fca43a4696fe69ed
#EXTINF:11.233,
067_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=67&start=778833&end=790066&brs=13938132&bre=15233451&ver=4&token=0ec3a3fd2e3b448625af7f6f4d12135f
#EXTINF:11.034,
068_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=68&start=790066&end=801100&brs=15233452&bre=16414655&ver=4&token=8575063fa97d8fda6555c194f3282dfb
#EXTINF:11.900,
069_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=69&start=801100&end=813000&brs=16414656&bre=18752435&ver=4&token=98071a68e8dd78ef8e5442b79737b4f1
#EXTINF:10.833,
070_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=70&start=813000&end=823833&brs=18752436&bre=19836067&ver=4&token=4f323067b921460cb8cd6365c59859b2
#EXTINF:11.333,
071_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=71&start=823833&end=835166&brs=19836068&bre=21520171&ver=4&token=d77e69c3f7af5ffda1bbc16e60e8255b
#EXTINF:11.967,
072_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=72&start=835166&end=847133&brs=21520172&bre=23528763&ver=4&token=5164955d7742a42aeb7adf9493ae0d6b
#EXTINF:12.000,
073_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=73&start=847133&end=859133&brs=23528764&bre=26661407&ver=4&token=01b037f269b4af4cfecb6a9e8eafa2ec
#EXTINF:10.967,
074_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=74&start=859133&end=870100&brs=26661408&bre=29462795&ver=4&token=139fa55eda617e6fd2e93900fa28073f
#EXTINF:11.233,
075_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=75&start=870100&end=881333&brs=29462796&bre=32910903&ver=4&token=373a1b92daa3a64bc5af5c8424d55bf1
#EXTINF:11.733,
076_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=76&start=881333&end=893066&brs=32910904&bre=36216131&ver=4&token=3d730a019d11d9cc01b3c42090a9e8bc
#EXTINF:10.500,
077_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=77&start=893066&end=903566&brs=36216132&bre=39309859&ver=4&token=c2ab9351420939c0a8ed81704a939021
#EXTINF:11.734,
078_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=78&start=903566&end=915300&brs=39309860&bre=41390079&ver=4&token=d420ad560ffaefb9ebc4283aed4af0d2
#EXTINF:11.333,
079_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=79&start=915300&end=926633&brs=41390080&bre=42646107&ver=4&token=f445572ec43aedc169b3210c4a75b803
#EXTINF:11.267,
080_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=80&start=926633&end=937900&brs=42646108&bre=44194287&ver=4&token=02ed1bdbc7c559b97fdf8900d6e1d614
#EXTINF:11.100,
081_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=81&start=937900&end=949000&brs=44194288&bre=45310067&ver=4&token=bd805fd16b85356af2ce4b4fa39a279b
#EXTINF:10.500,
082_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=82&start=949000&end=959500&brs=45310068&bre=46810307&ver=4&token=73faf423f6a3c2e45b2e89d58d6d03b2
#EXTINF:11.666,
083_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=83&start=959500&end=971166&brs=46810308&bre=49636887&ver=4&token=45570221850b70a87322de1701561b1a
#EXTINF:10.567,
084_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=84&start=971166&end=981733&brs=49636888&bre=50850615&ver=4&token=48bbfd976ed1cc5153690c9e76cbb1e3
#EXTINF:11.833,
085_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=85&start=981733&end=993566&brs=50850616&bre=53085559&ver=4&token=8cfc48879aa585acad1b1d585096d694
#EXTINF:10.934,
086_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=86&start=993566&end=1004500&brs=53085560&bre=57148991&ver=4&token=322d3b9077d688d79323153d6c502b00
#EXTINF:11.333,
087_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=87&start=1004500&end=1015833&brs=57148992&bre=59819719&ver=4&token=ae3d136f23a123d7300c130a1c4d227a
#EXTINF:12.000,
088_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=88&start=1015833&end=1027833&brs=59819720&bre=61421667&ver=4&token=36ba944f90c655ec3d69d4cc0dffb42c
#EXTINF:11.267,
089_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.3.ts?index=89&start=1027833&end=1039100&brs=61421668&bre=63296215&ver=4&token=0824398575f7e4dc3649700753e5af84
#EXTINF:11.233,
090_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=90&start=1039100&end=1050333&brs=0&bre=1496855&ver=4&token=f52cdf8bd4e723a78dacb566b06a2d73
#EXTINF:11.700,
091_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=91&start=1050333&end=1062033&brs=1496856&bre=3253527&ver=4&token=5c278e92f306ef74ac5526e95cdbf611
#EXTINF:11.267,
092_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=92&start=1062033&end=1073300&brs=3253528&bre=5750543&ver=4&token=a3a068e3001d059cd3fe51cebf9cf493
#EXTINF:12.000,
093_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=93&start=1073300&end=1085300&brs=5750544&bre=8252071&ver=4&token=609fc608195ccb2768392c73083601f9
#EXTINF:11.433,
094_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=94&start=1085300&end=1096733&brs=8252072&bre=10255399&ver=4&token=98fea0b6a4786525c6796d546d75e8a1
#EXTINF:10.467,
095_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=95&start=1096733&end=1107200&brs=10255400&bre=12874051&ver=4&token=056b674bdc6a230d3f664f7da7873c0a
#EXTINF:12.000,
096_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=96&start=1107200&end=1119200&brs=12874052&bre=14325787&ver=4&token=4ea03be188d999a1a9ebafcf2aea31aa
#EXTINF:11.800,
097_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=97&start=1119200&end=1131000&brs=14325788&bre=15391935&ver=4&token=6a36ab946f2cae6828ac1e7f642ab7da
#EXTINF:10.633,
098_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=98&start=1131000&end=1141633&brs=15391936&bre=17491331&ver=4&token=1ed6a47c7c27ab7c7d9b2343f8975814
#EXTINF:16.255,
099_gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.4.ts?index=99&start=1141633&end=1157888&brs=17491332&bre=19128999&ver=4&token=515f23a9cb262c89daf4e09237c4f42b
#EXT-X-ENDLIST
'''

import requests
import re
import os
from tqdm import tqdm

free_dir = 'free'
if not os.path.exists(free_dir):
  os.makedirs(free_dir)

# 创建headers基本的反爬策略
headers = {
  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

m3u8_url = 'https://apd-vlive.apdcdn.tc.qq.com/defaultts.tc.qq.com/cwmuWGVr8gG4f7yjncUyncdgSU7SbI0j_3Qoz0CC_-rzvjmUAr_42FHxRfau9g2AHbV0Ng1oKfRTRgDxAmHAgKV7TcNx97F1BfYAMAqz_FLv6Ht1ENrPOtkKUreHH-Lxo0-t2AK-YbPRM6MHI6UvS_lAaNtOOyj0FWgT1Q5XmRG0A975vue14r0DF_UX-Mg5/gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f322063.ts.m3u8?ver=4'

# 请求资源
response = requests.get(url = m3u8_url, headers=headers)

# 获取资源
m3u8_text = response.text

# 解析出所有片段链接
ts_list = re.findall(',\n(.*?)\n#', m3u8_text)

# 提取请求前缀，从m3u8_url中
m3u8_prefix = '/'.join(m3u8_url.split('/')[:-1])  + '/'

# 请求完整的内容
for ts_url in tqdm(ts_list):
  url = m3u8_prefix + ts_url
  print(url)
  # 视频内容基本都是content
  response = requests.get(url = url, headers=headers)
  with open(f'{free_dir}/free.mp4', 'ab') as f:
    f.write(response.content)







