import string, sys, pprint

#Source: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
CONST_LETTERS_SORTED_BY_OCCURENCE = [
    "E", "A", "R", "I", "O", "T", "N", "S", "L", "C", "U", "D", "P", "M", "H", "G", "B", "F", "Y", "W", "K", "V", "X", "Z", "J", "Q",
]

#Few letters have nearly the same probability of occurence. Just swap out these letters here, if you identify the errors -> Trial + Error
#index = plaintext key, value = ciphertext key (mapping is done after frequence analysis below)
guessed_plaintext_mapping = [
    "E", "A", "T", "S", "O", "R", "N", "I", "H", "L", "C", "D", "U", "P", "M", "F", "W", "G", "Y", "B", "K", "V", "X", "Z", "J", "Q",
]

#Configuration
ciphertext = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS CGZNL YJBEN QYDLQ ZQSUQ NZCYD SNQVU BFGBK GQUQZ QSUQN UZCYD SNJDS UDCXJ ZCYDS NZQSU QNUZB WSBNZ QSUQN UDCXJ CUBGS BXJDS UCTYV SUJQG WTBUJ KCWSV LFGBK GSGZN LYJCB GJSZD GCHMS UCJCU QJLYS BXUMA UJCJM JCBGZ CYDSN CGKDC ZDSQZ DVSJJ SNCGJ DSYVQ CGJSO JCUNS YVQZS WALQV SJJSN UBTSX COSWG MTASN BXYBU CJCBG UWBKG JDSQV YDQAS JXBNS OQTYV SKCJD QUDCX JBXQK BMVWA SNSYV QZSWA LWAKB MVWAS ZBTSS QGWUB BGJDS TSJDB WCUGQ TSWQX JSNRM VCMUZ QSUQN KDBMU SWCJJ BZBTT MGCZQ JSKCJ DDCUE SGSNQ VUJDS SGZNL YJCBG UJSYY SNXBN TSWAL QZQSU QNZCY DSNCU BXJSG CGZBN YBNQJ SWQUY QNJBX TBNSZ BTYVS OUZDS TSUUM ZDQUJ DSICE SGNSZ CYDSN QGWUJ CVVDQ UTBWS NGQYY VCZQJ CBGCG JDSNB JULUJ STQUK CJDQV VUCGE VSQVY DQASJ UMAUJ CJMJC BGZCY DSNUJ DSZQS UQNZC YDSNC USQUC VLANB FSGQG WCGYN QZJCZ SBXXS NUSUU SGJCQ VVLGB ZBTTM GCZQJ CBGUS ZMNCJ LUDQF SUYSQ NSYNB WMZSW TBUJB XDCUF GBKGK BNFAS JKSSG QGWDC USQNV LYVQL UKSNS TQCGV LZBTS WCSUQ GWDCU JBNCS UESGN SUDSN QCUSW JBJDS YSQFB XUBYD CUJCZ QJCBG QGWQN JCUJN LALJD SSGWB XJDSU COJSS GJDZS GJMNL GSOJD SKNBJ STQCG VLJNQ ESWCS UMGJC VQABM JCGZV MWCGE DQTVS JFCGE VSQNQ GWTQZ ASJDZ BGUCW SNSWU BTSBX JDSXC GSUJS OQTYV SUCGJ DSSGE VCUDV QGEMQ ESCGD CUVQU JYDQU SDSKN BJSJN QECZB TSWCS UQVUB FGBKG QUNBT QGZSU QGWZB VVQAB NQJSW KCJDB JDSNY VQLKN CEDJU TQGLB XDCUY VQLUK SNSYM AVCUD SWCGS WCJCB GUBXI QNLCG EHMQV CJLQG WQZZM NQZLW MNCGE DCUVC XSJCT SQGWC GJKBB XDCUX BNTSN JDSQJ NCZQV ZBVVS QEMSU YMAVC UDSWJ DSXCN UJXBV CBQZB VVSZJ SWSWC JCBGB XDCUW NQTQJ CZKBN FUJDQ JCGZV MWSWQ VVAMJ JKBBX JDSYV QLUGB KNSZB EGCUS WQUUD QFSUY SQNSU QVJDB MEDGB QJJSG WQGZS NSZBN WUXBN JDSYS NCBWU MNICI STBUJ ACBEN QYDSN UQENS SJDQJ UDQFS UYSQN SKQUS WMZQJ SWQJJ DSFCG EUGSK UZDBB VCGUJ NQJXB NWQXN SSUZD BBVZD QNJSN SWCGQ ABMJQ HMQNJ SNBXQ TCVSX NBTDC UDBTS ENQTT QNUZD BBVUI QNCSW CGHMQ VCJLW MNCGE JDSSV CPQAS JDQGS NQAMJ JDSZM NNCZM VMTKQ UWCZJ QJSWA LVQKJ DNBME DBMJS GEVQG WQGWJ DSUZD BBVKB MVWDQ ISYNB ICWSW QGCGJ SGUCI SSWMZ QJCBG CGVQJ CGENQ TTQNQ GWJDS ZVQUU CZUQJ JDSQE SBXUD QFSUY SQNST QNNCS WJDSL SQNBV WQGGS DQJDQ KQLJD SZBGU CUJBN LZBMN JBXJD SWCBZ SUSBX KBNZS UJSNC UUMSW QTQNN CQESV CZSGZ SBGGB ISTAS NJKBB XDQJD QKQLU GSCED ABMNU YBUJS WABGW UJDSG SOJWQ LQUUM NSJLJ DQJJD SNSKS NSGBC TYSWC TSGJU JBJDS TQNNC QESJD SZBMY VSTQL DQISQ NNQGE SWJDS ZSNST BGLCG UBTSD QUJSU CGZSJ DSKBN ZSUJS NZDQG ZSVVB NQVVB KSWJD STQNN CQESA QGGUJ BASNS QWBGZ SCGUJ SQWBX JDSMU MQVJD NSSJC TSUQG GSUYN SEGQG ZLZBM VWDQI SASSG JDSNS QUBGX BNJDC UUCOT BGJDU QXJSN JDSTQ NNCQE SUDSE QISAC NJDJB QWQME DJSNU MUQGG QKDBK QUAQY JCUSW BGTQL JKCGU UBGDQ TGSJQ GWWQM EDJSN RMWCJ DXBVV BKSWQ VTBUJ JKBLS QNUVQ JSNQG WKSNS AQYJC USWBG XSANM QNLDQ TGSJW CSWBX MGFGB KGZQM USUQJ JDSQE SBXQG WKQUA MNCSW BGQME MUJQX JSNJD SACNJ DBXJD SJKCG UJDSN SQNSX SKDCU JBNCZ QVJNQ ZSUBX UDQFS UYSQN SMGJC VDSCU TSGJC BGSWQ UYQNJ BXJDS VBGWB GJDSQ JNSUZ SGSCG ASZQM USBXJ DCUEQ YUZDB VQNUN SXSNJ BJDSL SQNUA SJKSS GQGWQ UUDQF SUYSQ NSUVB UJLSQ NUACB ENQYD SNUQJ JSTYJ CGEJB QZZBM GJXBN JDCUY SNCBW DQISN SYBNJ SWTQG LQYBZ NLYDQ VUJBN CSUGC ZDBVQ UNBKS UDQFS UYSQN SUXCN UJACB ENQYD SNNSZ BMGJS WQUJN QJXBN WVSES GWJDQ JUDQF SUYSQ NSXVS WJDSJ BKGXB NVBGW BGJBS UZQYS YNBUS ZMJCB GXBNW SSNYB QZDCG EQGBJ DSNSC EDJSS GJDZS GJMNL UJBNL DQUUD QFSUY SQNSU JQNJC GEDCU JDSQJ NCZQV ZQNSS NTCGW CGEJD SDBNU SUBXJ DSQJN SYQJN BGUCG VBGWB GRBDG QMANS LNSYB NJSWJ DQJUD QFSUY SQNSD QWASS GQZBM GJNLU ZDBBV TQUJS NUBTS JKSGJ CSJDZ SGJMN LUZDB VQNUD QISUM EESUJ SWJDQ JUDQF SUYSQ NSTQL DQISA SSGST YVBLS WQUQU ZDBBV TQUJS NALQV SOQGW SNDBE DJBGB XVQGZ QUDCN SQZQJ DBVCZ VQGWB KGSNK DBGQT SWQZS NJQCG KCVVC QTUDQ FSUDQ XJSCG DCUKC VVGBS ICWSG ZSUMA UJQGJ CQJSU UMZDU JBNCS UBJDS NJDQG DSQNU QLZBV VSZJS WQXJS NDCUW SQJDDSNSM YBGVS ENQGW QNBUS KCJDQ ENQIS QGWUJ QJSVL QCNQG WANBM EDJTS JDSAS SJVSX NBTQE VQUUZ QUSCG KDCZD CJKQU SGZVB USWCJ KQUQA SQMJC XMVUZ QNQAQ SMUQG WQJJD QJJCT SMGFG BKGJB GQJMN QVCUJ UBXZB MNUSQ ENSQJ YNCPS CGQUZ CSGJC XCZYB CGJBX ICSKJ DSNSK SNSJK BNBMG WAVQZ FUYBJ UGSQN BGSSO JNSTC JLBXJ DSAQZ FQGWQ VBGEB GSGSQ NJDSB JDSNJ DSUZQ VSUKS NSSOZ SSWCG EVLDQ NWQGW EVBUU LKCJD QVVJD SQYYS QNQGZ SBXAM NGCUD SWEBV WJDSK SCEDJ BXJDS CGUSZ JKQUI SNLNS TQNFQ AVSQG WJQFC GEQVV JDCGE UCGJB ZBGUC WSNQJ CBGCZ BMVWD QNWVL AVQTS RMYCJ SNXBN DCUBY CGCBG NSUYS ZJCGE CJ"
encrypted_challenge = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS"


#Setup
letters = list(string.ascii_uppercase) #Get all letters in the alphabet
frequenceAnalysis = {}
guessed_key_dict = {} #Will hold final mapping of ciphertextletter : plaintextletter


#Reusable decrypt function
def decrypt(ciphertext, key_dict):
    #Decrypt using a key_dict of this format: cipherletter : plaintextletter
    print(f"Ciphertext:\n{ciphertext}")
    plaintext = ""
    for char in ciphertext:
        if(char in letters):
            plaintext += guessed_key_dict[char]
        else:
            plaintext += char
    print(f"Plaintext:\n{plaintext}")


#Count letter occurence in ciphertext
for char in ciphertext.upper():
    if(char in letters):
        if(char in frequenceAnalysis):
            frequenceAnalysis.update({char : frequenceAnalysis[char] + 1})
        else:
            frequenceAnalysis.update({char : 1})

#Sort by occurence
frequenceAnalysis = sorted(frequenceAnalysis.items(), key=lambda item: item[1], reverse=True)

#Create key_dict (map results from frequence analysis to the most probably letters in the english language)
counter = 0
for tuple in frequenceAnalysis:
    guessed_key_dict.update({tuple[0] : guessed_plaintext_mapping[counter]})
    counter += 1

decrypt(ciphertext, guessed_key_dict)
decrypt(encrypted_challenge, guessed_key_dict)
#pprint.pprint(guessed_key_dict)s


