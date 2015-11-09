#!/usr/bin/python
# 
# 
# 
# 
# Kim Brugger (09 Nov 2015), contact: kim@brugger.dk

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

length = 6
numbers = "6 10 4 5 1 2"
numbers = "-12510 -88729 91304 50403 98326 6507 -99014 -92383 60414 -70328 -13385 -22168 -24907 32527 23943 -75321 44858 7766 73636 56179 64201 2022 -33705 37111 32613 98890 10776 58508 -30188 8944 -61460 -73753 63260 -24002 -73314 -45707 51573 -59948 -30479 82801 42355 91668 39246 36627 59098 -53788 -26871 74115 -33785 -64 50758 45437 -62189 59773 -17946 -6983 72012 36967 -12104 84182 68525 21449 42559 -5373 53305 -59957 -5559 14512 -75551 -10343 -83056 23586 38570 -82377 93013 43402 49367 -16357 83868 7415 46605 -39742 -70989 -89631 -85688 -10980 -82459 95641 26187 19152 60556 71428 -7036 9804 41073 -95788 62367 77800 -54942 42061 89535 17200 -33730 89250 99155 68649 -75474 -46502 -30985 -31348 -87037 -9843 99817 -97472 64496 -61459 10899 16903 24004 27382 -45797 -23207 28997 38238 -85577 -94335 -60276 79181 -51693 55847 30635 -9855 72261 26422 64085 50709 78581 -14892 73877 98521 21336 -69506 -8312 86390 53172 -28234 123 -72386 -5669 -87765 74785 88033 42485 -12825 -74829 95740 -7536 45726 -6706 -98804 74671 81085 18944 -59604 -55570 -86984 -3189 21115 -50504 -84764 -37654 -24230 16134 -33491 -22064 -94527 59116 74634 53996 91002 -42876 95568 49818 -81456 22548 74191 -67997 -32110 -15795 -3429 62094 -41279 38733 54294 75301 24845 46524 -80514 -27530 -74098 95854 -71775 -4879 -15574 90564 -85790 88676 -21203 -19810 3945 -40141 -8626 90383 26175 -36494 -43986 52720 -97638 33760 74933 90003 9044 40977 58767 -41290 -99590 -54383 91453 82410 -59001 -72412 -13408 -82086 -57952 44820 29709 90478 13664 37265 -59062 -33197 -70429 -16845 70032 24793 -40786 21904 49706 39364 35038 94303 -12591 91867 70687 -29700 -64478 34054 2125 99164 32138 -91095 -3776 -36888 43026 54669 -7617 -14019 42291 64200 13382 -91344 3455 -19748 -59425 -82086 23628 -23044 9578 -91038 -42352 18336 -85764 64446 895 44013 -41165 18339 31331 91294 67575 11195 -75788 40916 91500 -60940 -46385 27247 -68716 55226 -19702 9867 49556 -36356 -70876 65184 95609 92583 36867 -48932 -63526 78303 26130 -30665 -20950 -15316 65001 73991 42475 65775 12990 -20055 -65600 -60065 58673 44188 28027 36308 -74045 -47339 84797 -44650 -30862 -75390 17837 66972 -67573 48530 3296 25065 -20922 55053 27766 9060 -84729 28433 59638 38496 16258 25356 89803 -31922 25083 -50829 543 93971 54342 -76094 -27571 -74577 13254 24876 30800 -85143 28298 -33174 57651 -62201 -65629 62603 -38026 -41833 79315 74042 77675 -92695 40613 62698 14787 59055 10565 -38488 55405 13102 -62439 -79541 27515 -77306 -43539 -85871 -17009 55532 -68288 -85936 34456 -82859 -53084 28779 -1770 35581 -69093 -65506 59734 -76385 24897 -93485 -98736 -49388 58369 61340 79731 -98763 -58900 -72598 -95900 19129 -71209 7627 69405 57260 -28339 79150 56887 -6541 -79361 -17965 18750 -23869 -72335 -79626 6859 -27311 -70289 35918 68024 -51220 -39112 11220 -80763 55443 -5897 -52803 25393 98012 -1931 32687 -25331 78799 93821 89019 -76312 26890 -81190 65433 82542 17478 12814 82042 68587 -26711 72026 -70139 13655 66417 -22016 -39914 12569 -91087 22306 93264 -91670 72954 51026 72321 -27206 57098 -54334 -88330 16529 -96692 -99587 33182 -44497 97092 46230 -33934 -82807 -88998 1606 -79577 -9236 -6156 -76176 -56152 86703 -65384 97154 -41543 -58258 -54990 16287 94920 -59002 44560 29141 91368 87138 28954 33088 -90529 -48779 -62394 -48878 -45893 -48773 -20579 -12524 24399 24399 -54895 -22991 78825 83471 59066 63674 -91643 68718 93825 -26394 -39848 53405 -31336 28290 -23983 48593 31239 5046 76164 -56991 26464 64221 3091 25496 -1077 -58295 -82511 97305 39223 36214 -67239 70651 -32859 -35091 -28 2964 -85771 -26547 38669 -37197 -53410 41393 24619 71864 92909 -12277 61903 -68627 -35006 -2751 60211 85724 70988 12446 87214 -92184 14420 84871 -5424 -27190 81523 77310 -11745 77568 -32114 90229 6671 -3372 10788 59829 -56046 -12240 -66723 -52227 42446 22964 32342 46153 37906 50191 24457 -77484 25605 -12415 61901 -6858 -4917 31226 3604 8664 -56689 -7545 3965 87887 -35147 -78446 42356 33445 49423 73336 -40356 83565 51932 -83794 39072 30190 54344 19305 -85807 19725 96472 43842 76102 -60021 66229 34984 -14816 -22459 47114 54257 -57234 27378 75846 -84247 -53688 -37155 -92133 -53864 -85568 51812 -25669 51577 8050 24637 -2820 62378 -71997 60541 87175 16149 24414 -26505 58006 5304 71274 94069 -76755 -69521 89994 80436 -45236 -24902 -19180 -55509 23540 58719 -7333 2968 -48303 -96899 -54860 -5081 60508 -96933 -56124 -6255 90765 34263 -39627 -38183 -85697 81756 -35668 52301 54222 20034 -3513 -72672 -4458 -67605 -83769 -89041 17204 -57059 67678 -21210 69796 20996 -29236 -72738 83133 -96027 7028 55317 -20964 5971 13099 -76607 70309 44657 67019 40974 5718 -28053 749 97690 -98826 36906 -42324 97273 55150 -80465 30905 50096 -21322 -78328 -88731 -8309 12421 25100 5855 -15866 -2896 -83552 67837 -99367 -34185 11652 10150 7794 -78057 29780 -64044 -96716 -44072 -44059 -64521 -55573 14947 -43925 -88956 -43856 -21137 35549 -2376 46428 18517 4997 49173 70651 -14851 81893 -36670 -39026 1039 -8223 44254 -8973 -42698 58089 2750 53861 -89230 -98529 -49229 -17947 93220 85082 86115 16211 -81177 -44052 -4598 -63536 48063 47896 90490 73402 327 80735 -60470 -62556 -18885 -66377 64273 -13627 -3702 66967 9715 -95822 32288 3903 46215 77779 68306 14797 -16429 -87905 90594 -55646 -42362 -29984 -85845 52802 37762 -34796 -21381 93658 -69762 -25263 -80367 -72297 -61108 37655 -1449 76224 2233 11604 32986 26345 43714 -30009 -92799 -24883 -65401 -81311 -42783 -1254 17900 30237 -68610 33316 -6223 20510 46391 -97689 -79684 47067 -76330 -36533 -29199 -24537 61042 -16732 70707 -62142 79030 -84915 -35243 39606 38486 -52820 -32777 1238 38515 -36500 34914 34819 -20375 74135 29994 65159 32019 -40747 58996 68094 -8249 -6316 -45344 -82221 -74918 -1451 84357 442 6736 78792 55451 -21646 -99643 -17772 65338 -4028 -63761 -579 48297 11017 -8045 24059 -7515 -46888 -69974 -69176 -236 -41658 -62364 -31761 14997 -13281 -33089 82018 -51128 77981 -78757 -3514 -49589 -87756 -21621 62270 -63578"
numbers = map(int, numbers.split(" "))

swaps = 0

def ins_sort( numbers ):
    
    global swaps

    for i in range(1, len(numbers)):
        k = i
        while ( k > 0 and numbers[ k ] < numbers[ k-1 ]):
            (numbers[ k - 1 ], numbers[ k ]) = (numbers[ k ], numbers[ k -1 ])
            swaps += 1
            k -= 1

    return numbers

#pp.pprint( numbers )

numbers = ins_sort( numbers )
#pp.pprint( numbers )
print swaps
