#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Rafael Hernamperez'
import random


class CryptoRAF:

    codebase = ''
    matrix = []

    def __init__(self):
        self.codebase = u"!'$%&/()=?1234567890|@#~{[]}qwertyuiop+asdfghjkl<zxcvbnm,.- QWERTYUIOP^*ASDFGHJKL>ZXCVBNM;:_ºªçÇ¿€áéíóúÁÉÍÓÚàèìòùÀÈÌÒÙñÑäëïöüÄËÏÖÜâêîôûÂÊÎÔÛ"

        self.matrix.append(u"ô=tù6;jYbúWO.À{-uqQXûÔÁÑ92g3p'v0ëz&)+aké#Ó^*àCç€dÉî?óAÚmüÍÈ%~D$M}ìïíZª(ÒÙ>S]eºRÜ!n@UPâGV4ÏyN[ÎÄ soTò|HáLx,<¿ñwÊcFIêK:B/8èöÛrÖfJl_5i7EäÌËÇÂ1h")
        self.matrix.append(u"û{7H)òDÎ3=âzñhÌä2Cê]~%K1,FËï/N^0Öë€}*Íc'S(lnwAàÚÓ6ªubdóü5ìtÑB&-J$ú|öxVUQÙ?éEMPkeárÁÒèWÄ.YoIXg+RÛÇÜvm¿ôa[;ç@T9sÔ#LÏiÀí<4Âp_!yº>qÊîùÉÈGjZO8:f ")
        self.matrix.append(u"qºt%cz,>M?|0[Umê3Óu;ù1€Ëï84wEB¿jChÛLª$ü& .éFÂv:)KÖÄûÊN]@IöXÏñ6À_W*ìg'eÎrëÔôYxdkÌîAÒ!Ùú5àóèÉ<Úi}oa/PÈ{(HDfâVOZ27QÁásSbR^yÍ~-#çGn9TpÑ=äÜíJòl+Ç")
        self.matrix.append(u"Lìmú3Ú#jÓ7ç9X!VqUaºG>{+î¿ â~8nñÑsK?ök@1O<È-ôÖÁtMhûxüBzó^Òvl],Û'AgecÇNÏ6PÙ)ªÍêáËpCÄàHïQ042RD_ùrëuÂZF%é€$Ü;I}/Y*[&i=.WÀÔíÉäEòÊSowÎÌyèTdbJ:|5f(")
        self.matrix.append(u"aÓR<è$*O%+t=?äxEfô0nó€rSJcXhÚúÎPâ|~>6FHÌv#&Ôüò9D,TÒª}QsºyÙpá1uMïñ8mBw7'ÄlGCqÍIK;24í!ö]N{ë)çÖÁ.oàËj@ÀVÂgÊ^_êÛÑùîb:d z-ûLiY/ZAW(Ü¿[UÈ3eÇékÉ5Ïì")
        self.matrix.append(u"[ôKóBFËÉ snÛE.ácIJYÇ58_ÙÑî<ñ=êZòr*ÊûT/yN@Ò€~X!eàöÎª:hÖÓSjÄ2m+aL¿AÚv{MWÈÁÏ;%g?R7Àb9ù)p#xUCïwäÂGV3iP6ÌlèO1é^zâ0ºú4&ÔÜf}tQdüu'o(Dç>|Íkqì$]Híë,-")
        self.matrix.append(u"^'ëJüpiDa9dÎìRoô-ÓeÄöXB7ÜqfÔIHE{WMQsî/xàËz!êçZkFPúÑ+T:1€b %G8À3OÍûÈr?òÒíKù;0èS#uñ@Áá]2>U6V<º=$¿jâ[ÖÏÂNÇ.ynäLcïw,&ÌvmA)Yh_4CªÉÙl}ég|~Ú*Ê5Ûó(t")
        self.matrix.append(u"Û cLÀjû+J2#ÂôùöHÒ[ä%4ç5DYú0dë8@ó7àxyÌ$ÓpñTwífXUOÏer}Iuî]éQêÚNGÑaò€_=-1ü?i'kÈ{ìRáªz¿ÉÎÔhAvÊ(3èÙ,g*nÍÖâËMVmb^ÜÇFt&.<~Es|ï!;6BWº9ÄoCPqÁ)>/K:ZSl")
        self.matrix.append(u"ïÄÍM;-äÇjUó?2z[>|PÙk*Û~ë¿âÒôè{Cw3Z'NKD9oÏaqc)mngÁJ:uûtòhàúS v!i%4ÜEb+@7üf0YìÀ(Ô1H/lWÖ8RºêÂ_píVQÌTe6^É<Ë$5=rù,ÚÎª€FÑáñLö]çdIé#O}Gîy&xXÓÈBAsÊ.")
        self.matrix.append(u"è*'4xgIUçÁª$ä_/éîÒRSp¿[mËÌùÙ>ówáNÀ}as|k)e7Ñc5yÔºYâ]C;ítÖ^LÛWTò?ÓFúPQê6ürÜz.qôû&MëÇDobGE(A8=2ÊìÉZ€lÂf-3XÚ9jn<ÄOBñiÍ{,:HàdÏ%~ö#Î@!K0ïu+vÈ1hVJ ")
        self.matrix.append(u"EeÛïIèu{ôBXQ¿sNÊtÀl@ìHqÈ|130äó:òg(.ªSmüMÁ'[,î6vçÒÖa}É$9iFGÜrÏZVÚTà7Ë^ *WöbÇC4ù!?kÂé#cPÔd;8~5ë_ºÙ%yLOáhÎRjY<ûJâ+zUÍÄD=-wAê&píf]Ñ)úño2/xKÌ>nÓ€")
        self.matrix.append(u"äMVváç{cíÔÎàÌIgÚâÈù#ëÑD2ts:8ôª/G&Ù€ÀÛJL}'fwEÏúrö]É~ò%R@Í6ûPñêm|SÒÂUÁÇjq^0(óÊFìü4.uQX7T¿=-AnléChK!5xaiHî$<_ÜbÖYkyºZï*9+?1eË)è[ ;oOd,WÓpN>zÄ3B")
        self.matrix.append(u"ÄWÍe4Ùú+ËDyÚ@Mä*òE,GªTá^PJ¿A}ùÓÇ8xKjÏ[ï.Èì?qkÜÛ5üºubñÁ{C/;#z6L)9>IíÒV0îôÑt7âpr€Bë3öÊ($&g_S|=cÂ:ûÌRZniUÉF1êhsà~lw<-oXYó'Hfçaè] OQNÔÀm%vÖÎ!éd2")
        self.matrix.append(u"(Ë/Rº%ceZªèÜwñÖ|îíPv0>r€Ñ)AVëêyWg-kÁO=5ó9_â7f¿2Y$DÂöEÙ@3ÔH!Bì~p[ÉÌ'6Jqç{áTÄ<I}ï .+*ÊKüd1äÓàò,ôMbuúxÒÏoUXéC&sÇÛNÚ;mGÀÎ:jl]ÈSF8LûQ#zù^athi4?Ín")
        self.matrix.append(u">çjm5rR,3äÉQVü)Â*=?<:ÙL€GºÛî(.ÖSaNÎv@Aïl$qªu0ÇUùÑÄ|Wg-i8{ÈÓ #YtDdZpÒXJË9Fx¿òÜnwíB/]ûë[ìÍÊ;f'ybMèáÚê6ökâ7ú%có!OTé^ñKÁ~CÔhs1&+4À}à_zôÌ2EIoPÏHe")
        self.matrix.append(u"ÉCÄI{/¿+ïâºlikmÑVî~ÏAêñÖÙ6üR4èpaF%P70öHzK[=Q:ëà13_c2}9ËÓéS€yJÍ@û&huD]Ìä'W>e8|#ÜxÂ!Û*f(Ud,nE5tìvwÒ)Yg?bÔôÚ^.sÊªoáB-úçZO óqMXr<ÀTò;ÇÁGLÎ$jNíùÈ")
        self.matrix.append(u"[ÇrÊ(*ûA9IÀípäéK+'ÔDd.Esq,/_zG0Âkw%N;@ti}ÛC~#Yx|ëçÈü PQJ5ùOÒË&mªìv8?ÏÚï]6èÁ€áöÜîÎúF$ó=ÑXà)ÄB!oRWêV2ÖZ:cÙg4M-fHLjaôbu1¿7<ÓÍUSl{eÉn>hò3^ÌºTñây")
        self.matrix.append(u"<púqK3LÙà2Br_^yÜbP=&ân'tíóìmG>ÍÉÌëç(Y+7êi.ñ6~-ÛäuZ¿@ùÊS{î€:%éôïÂw1ÈloÚFCOseE5;*öA|4ÏUzÀXèÒ/hÑ8ªdVº9] ÓMkDÄ}g?HËI0Ç,òaû#xj!$T)QÎáÁcÖ[JüvÔNRWf")
        self.matrix.append(u"=Ñâ&r>4d7ÈqEf0òZNÍn$€aù|GÜ)gÙ9ÛUuhDÊìçñ*~oB(ôT K;ÓM?@Â¿î.ÖûQÎ!YxXcéÒ,/]LÔ-ªjàwlPyWáÚ'üê^H#8}3tzíÉ5óëevk_ïä[62sOÏC:1ApièJÄ{Ì<ËV+%öIÇúFÀRbmSÁº")
        self.matrix.append(u"D>ï,=CÚumò]*$À7eso?:ñáËöp4!dü}&Ü6íîéZ0€PÁ9.'aGIH@LgàÓ{È[rôëR(âº-Ï|ik fn+täQW^Y8ÎFA5ùçÍqBhÂxv¿êT)ÇKNwó#;ÔVOÒMcÊ/É<úSèÑ2jûz1_3ìJb%EÛyÄÖUª~ÌlÙX")
        self.matrix.append(u"3z*JulÎ.ÊmjZ:oüÑCíÈñpÍ{~YHn=ëNv]ê/ÙùÂDÌeçÖÓK6!á$ò[yúìT@>Ú-BÇrb%O,ÛG;?(PafºqM|ôdÁsäéÜ_îû1h}ËE+FkÏW9S' L7^Qx2g€óXRèIVUAÄ#ª0i4É¿5wïÔ8ö)Ò<tâàÀc&")
        self.matrix.append(u"MALÎÁ4aÙîÀ,9Ñïëi;IÂ^8ñû-È*ÚÄ03ü5@>:Qxóè+Vj<BÏªúTpàRzq7é2PùYJêGWáE&vurN6ÊSH${!öÔmk%¿wZäKFfÓÖ ô.bº[Ç~hO}(=XÉÌnâ'_sígUe]Ü#/)çtoòylÍDcC?1|€ÒdÛËì")
        self.matrix.append(u"JÖfpç)zury,äëËÊGÏÚ#K&Ò¿Àwoú%2^Çli ÙöªMèî.QÄcvÌñYÂe4a>àmn;Eù(xÜtNº:8ïB0h[O3Ísqâ5FPó<*é_TWÔêìjí6Ñ€LHV?=É@ZáÁDIC+ô}Ók-gÛ]$S1RûXÎò9!üdA7U{~|b/'È")
        self.matrix.append(u"Q1?+¿|LèÛO(Ç%<éBóAS-qUëÈö9Irdä3ôkºt:Ìa2hXÎÉ;H=l}iÏKuYòbseMN@WÑ8 {gDìáïû#ümî]Ó40!çÒ.^êjZâ7*pÍT$nVPÜz5Fy€wÂàxÚÙ_fG'ÁíúcÖvEoÀ~Ë,[Ä/ñ)Ê6&>ÔJRCùª")
        self.matrix.append(u"NÓ +;*hÖÍûJ7PU?jHÄàâEp<$fyk|òùCÔb=rî{YIMT€XA(Çog5WVzÊÏÁO¿ó}m/0'Éèêëd@ñ#öË.)vÌ~ÜZºSÎôüwKR]È>ÛtnL9&a_F8Ò2Ú[e-lxcíuÂGqÙsìáQB%^4äªiÀ,3Ñé1!D6:çïú")
        self.matrix.append(u"çyé=@4_ïbëàÎz3PIÛ.uKnB~Ìá-5[Â|ÒZ'Ü¿ùaÇÍk<ûG9:â$^0À]êtMN}úUwèöD%ís{ºXmHd&rRäpÏ7iAV6e/ÁLgcJQîo(ÉÊªËTÖ+SW#ñ, YÙÚ>Cv2fO*Äó)jqF1ìÔh!€E?xòü8lÓÈÑ;ô")
        self.matrix.append(u"!àSuü>-À{(~ç+:XHëÊEQéú;ÚÏ,¿W0º=ÒÙY$F[bîGOcM?€eùVsÛg)'3ËRvqh@/U7mB.%ñxêâAríÂó6èoKtz#ajÈPÓÇïNC<1ôDÍp4kÎ}J5fûTÜZÉi2w á8nÑÌÁÄ_9ªl^&ädòö]yÖìÔ*LI|")
        self.matrix.append(u"gk/dÀ.$Ìh@ïe,LNI*vÍá_º!äÒ4ÈE<>ôâCÄRçÖXtZoéî(3líc]YWÉ+-ÔÊnñóù~ÁH;ËAÓ8{ z0#paO^ÙJr9&ÑqTwö6|Ûm2i€s:uèUû)ëày?DbQ¿ü=ÜKÚ1òjªÏÎúS5}FÂ[ê7'xÇPMf%BìVG")
        self.matrix.append(u"#_jù%wÑc0kÇÔZTÓëüAf3áÌÁ[ ÍçL}€&ÄiÂJqêvÉoâxí18Cö$àîÏÚô9U6é/<pèa.n!-uÒÀ=Vr(N@Xªl+eBm*y~ìG?b^M5ºäD|HÙzóòSúñQKËÛ4>W)sFPOY,;g{EÈIÖÎ:h7Êïtû']2d¿ÜR")
        self.matrix.append(u"ü-bª;ïìñEg5e{=VK_NM0YQT)àç>A}*nÑäw¿k!|ZÈiqú€UÄdf~pê[/7uëËCy<DÉ:^8aÇÓ$ósÖÚ&2oÍ4ÁJû%hrâ.GÏ'áíÙÒÀ13ùÂHm@z?èjLöc+]º,6Xév9RF ÊÔPÌÜòBWôI#(ÛîÎxtSlO")
        self.matrix.append(u"öÇ,bf!úÖ32@iº7ÂF5}ÑôTqLn[_òjC-(ÒkñÈtcíès9:<Ì~ìzâ>ï'8Yóêû;hÓ+ü*àZëalÜÉªv%IOP{¿uS/M$HmdWxw1JÊD&ÀùQáÄÛ ?U0çg]y^Ùp€îGBe#ÏÍVÎAXN6Ë=Ô|äéÚE.r)K4ÁRo")
        self.matrix.append(u"LÚa3X-¿}G]'ÊñËv!IA(t6f=#7bsÓ^ÙmÈ[:Îó_.z0ÀYëo+Z%*2Â,ÍBîªûïdhìc1€Òé|/àPáyÜçD;TüUÛÏúQ9{@wnge<q Ml4Çö85ÄÖòêxpk?íNuKÑE>Ì~ÔWiºô$âJRÉVèjäùCFÁOrH&S)")
        self.matrix.append(u"CyZíÒ}SJv@nB€Áªmk{s4*NÈ[E(ÛdçUÌIÜ$AùîRÔÑ<ÉÚ-ÊK Ç~èOà^#Äégf]0.òiìV+Qü/?tê|F;jXá3%>qhÙz8b7P'&¿úÂûLp!_9À:rëDÖËÏóW1ÍÎoG25Óälcï,â)öeMºYw=TxôauH6ñ")
        self.matrix.append(u"tÎZy*}>Ë0VJB-oCçPÈg9DézÉÔüL.xW]4R)&?ÒmIÓ1vÚàKïYÑ¿k[ÇasìáH!êU=ÖNÂäcjTldÛGbpqÊúÏ2uí;âÄ$w@(óòª/Q:è~ºröùÜ8'ô{3nM#i6,€E %ÁÍÙëhÀS^î|5efñûX<+_FA7ÌO")
        self.matrix.append(u"înª3mF}?èPÎ€{%ÙG4Ïq|ô-50Cx8bIÌá=ìQêöÜ9lO;,YwÄûÉ(aÊÈäB7~ÚNíK&Ödùf#gL^À¿Mku_EoÇéjytëÁc@ü<ºó:U+T]AÑ[*)çiÛÒh.1zËSZWòpV JÍ2RÓÂ6sï!Xàe/rú'vHDâ$ñ>Ô")
        self.matrix.append(u"XD9ó#{K^&)dE€oëÚùÏFW4,8VvLSÖÈ!xzeí;áÓû]-j(|âà'*Ñìyhôî5_Òòè@ ï?pÌ<+éÉküZUÀêO3lqgöÁªa/YÜwAIGitºQÙË¿HCTnM6$=2r7uB>ÛÎJÄfbcú%sNmÂÇPçñÊ1:}0R[.ÍÔ~ä")
        self.matrix.append(u"lÂûñyZoî€/çfsBàp39e¿>v,aU.T$-dúÑ5WPQ2Í7ü[ öqDó)RÈO4ÖrÔkéjÊKº{âXÓc*~ÚNÜJG@%AªÇmi']FáÒb|ÏËë;g}:<?nÙùhH0ò#z^äE&(ÁVìwxÀYLÌêÛ8MSôï61íÄ=!è_+CÎIÉtu")
        self.matrix.append(u"$Mbº/ùy<âtSxRJúP]}ªV@j#vêr:|[Ñè(ÎöÀËQ.;c7ì{2!w1dÈHÙ*ç9D€üTIl'OZàLNWuóEp,Ö=fÒ5s¿ÓÔB)í0ÄÛCÁën^g6é~òä%ïÉÚi3-ñ8XYAUÜKm+eaÌÇÏGFîháÂz&_koÊ>ôÍ4?û q")
        self.matrix.append(u"i'pè:NqKÛEPÌ5lÒ{çQyÉÇvYÓáMuaj7,]9¿_mHÜó^[dÑùUäCîhLÈª-cÍÀì@êw|3bIF(J %eû2öRÚÙxôD+€ü/}â.*ïÂgºÖ#Wà;úÔVtíO0T>&zGësrÏ=1<Ak$n)ZÊË684oòÎñÁXfB~?!ÄéS")
        self.matrix.append(u"P3_@x]z}v?ùSäücéAÑeíÚYêoÂ*wº€RLÊl XkEó#è¿ÇHqûbm9TÄ4O<Ùr(ÛyâMÖëôÔga:s26${0j!ÈÒU[+òÍ8FÌhJî7fÀÉ~ö'n,ñÜKQ.çdi-CËup%ïB=áN;IDVW|à1ÎìZ)&tGªÓ/Áú>5^Ï")
        self.matrix.append(u"9ÛÎäÌbª(.À3)jòEB_á^S=?wé#ômiÁZÉëuGpV+!ù[}KoËÂÊ;y,û*<úQfA]€%eOlX8è6-/Rnö1ó¿ïâaÍìHÄ72LxÑgÈÙ&ÜÚv:à ÇTM@îÓ5Yr0JküíWÏ'IqPÖ{~$ÒNCU4ê>ñ|tçzÔchDºdsF")
        self.matrix.append(u"ª#ÔaóyQ-ZÄ>U$|áìô?€c^Mâ)É;îT]èÓ0äÒÜFÛ.Èo~Ùpx8XmjbDúS6<Yç(JuàB!vlsÇi+1Htk=qÁ3,önÀ&fAïrzLOÊE4êûëI:¿dÖË5[/Ì%Ï9íRwVeéN7}@KCÎh 2Â'ñWü_G{ÚùÍòºÑPg*")
        self.matrix.append(u"(Ïç€h,é-4íÑËKÎbIiûe#az!áEÂ)Ûó:yÓT¿äÍ$1lÀ îr&>ÙgHoP3<F?@ÇÄq_ñB^0A/msªcUú[ìRx{5Z%ÉYÁCu9Ò='Ê*V}ùëº8L7wè.|Xtp;DÔNÖfö]+OJvôüï~MSWò6ÈdnjGàÌâ2ÜêkQÚ")
        self.matrix.append(u";p~hÒAôí3òÌmçUKñJÎ5LúÛàödl]b-G_Úfû?Ä€ÓHvcºZ:oN XÖIkÊäqÏWÈêÂëDw<jÔtEî*xP2SâÁ6ªiÜÍÙu)7/á^ï=ìr.M1À#CÉÑYaO&ó('Ë$g9%èy@T4!R{+ÇüVQéF0sBù|,8>}¿[ezn")
        self.matrix.append(u"éÛ ]wnFÀ=.óâûuIvÁmô)'ÎÓ?Z[èÜyÍùsòY$9dB¿<1~xËí!fcÊ;egVEúÑ>PhjºÉ#-L6XÏçiJÒ,OKÚÄ^ÔM*0Go|€ê&2C:tzrÇ}ñHp+3öÙläbÂNaU(S%à@îï7qÈWRk_ÖáüT{8ëQ4A5ª/DìÌ")
        self.matrix.append(u"Xèiï|Rëz€ZoÊvxeQÁ*>âF?%ÒUJöMê-CE8'ÍPÄHAnË{4à9t3D[K}ôÉí6agLÔÜÎ/:7)#º¿+hñwGÛÂûù^ÌBáT;WfªyçV.,=pqÙsÏ óÇìjéN@2IücOÑÓ<î5]k&0ÖòÈd~äúmY_!ÚrÀ$1(Sbul")
        self.matrix.append(u"p:àUt!údJrBºê^1%gázém,|HÛîä]ÉÒuÍÌobìcThQiÄVnOXYxk?èEL4M Ëí¿l>Ïa&R#8ùN(Ç5)ëÖ$DüÎv2<eÚ;+_[Ü@6qPªyÂsçòF0Cw7{IâGñÀW€ÁÙö9ÔS}Óó=fÊjÈû'/ôïKZ-Ñ~*A.3")
        self.matrix.append(u"Pp>!V*:N,ª.%4)òïUçW8+ü|HwÍ60À2ÖÒ1Û'q€ÊâkiSX(-ôÂ/J#nÎF;ëc@ñOLÁföaÚ[ ÉjxbveûyCèà~]í=tÈÓ5á?Aù$éÙuDMZEä<^YÔT{7ÄzËîd3¿Ììg_ÜIºQÇR9Bêmóúr}h&ÑKlGsÏo")
        self.matrix.append(u"fû'HèE{êO-cu]î6e¿tbiá|Ö$Ds)üôÎ4ÏI}méyùÊUjëoG /ÜÛQ35q,.(Cz?€ñÁÀFK:<PÓX;ä8íË9YWaJxúNLpk*@Ç=öhd>nl^ì2wÒ&~gvÚïBªÙÉ70TrZVó1ÂÑS!_ÌRàA#çÍMâºÄò%[+ÈÔ")
        self.matrix.append(u"6YP_HtD?ùl)oIü+Ê*8OÚ.y9[¿vÏÄÌa/ë%R1ímUuà0ªF~ìrÍç,{nLe<TÎ]Ö>Ñ4€V'B5dÂáÜK#ZûQ^ÒbNòsÔESc7JhCMxÙ ñöX}wA(qïäW|jiô:-À;Èk=úÁfÇê!$ºÉ@éâèÛgîpËz&Óó3G2")
        self.matrix.append(u"MÈWùuY=jaèÏû%ÒÂ*$!6/nSÄ?úÉÍüw|e+xòb5ëÙB4]09'>(ªp,OKAIÁXÖtQ7ômJidqrN}zÇ#k€Rì öºàäóyFâËHÌV~vÔU_DgîçÛ[-f8ÚêLí:3céñ<há&ÀsCï¿ÑTÜP@Ó)1Ê{^GolEÎ;Z.2")
        self.matrix.append(u"î'Zª#¿t5à|x{ºKÇOUêÌGÛ2géÖ^c$~ÜJle;FäS3CöÈ6Qy!YÒÍí_€ÚLHMzdáwN?*vs.>òoÎ[7róú-ñDÊiÀ+X&Wfhç:q@RÙuI1üÓ%âÉÂBÏnmTEÄ,ÑP/ûb<ô}ìïÔùpk80=4(èaË AVj)9ëÁ]")
        self.matrix.append(u"cúÓ/àLªZ-gíaÌ8B@x$]ÈhâEé^ÖrdWRöP(5ïëñÔìy~êÀ+3[ =7q_ÛY€ÚS*i|,ºOÄF0ò<QTomôe>1IÂkÎHçfûUÍ)sXb#Üp.KCzAänÉ:ùN'M%ÊJuVvÒÙü!îáGjËwD¿Ñ9}?Ï2èó6&Ç4lt;{Á")
        self.matrix.append(u"Mçù:Î€ÇÛhP<;Óü2ª¿]qîJ3v'ÌIXK(ÚÏ4yWVégYíbÍ1ê9s)}À=?ASUodÑ#ÖBÙº~|n/ÄïÁw-Rk$[EÜ%plû+rÈà&òeDzÔä8úL,âÂO!*>ójÒiGëì05.x{áNC@Zf7FTÉtËöôÊmñuQ6^_ acèH")
        self.matrix.append(u"'1g%cÑ~ÀÊÌ}ÄÛ$VÔTL0Âìê+v]oWëMÙó¿i[bI:QsèB3?8KzemXDéªî^<€rCZ/ñ çÁUfºq5ú7kxGYJíF>=ÚyÍùÏAO,ÉSû!Ó#@9N4ËndhÎïÜHÇÒ|6üÖô&_luá2pjà;a(t)âäPö-.wR{È*òE")
        self.matrix.append(u"m5VNP'sjºEv>pË¿ 4^@)]ÑuÈqZëdM*;ôÊ?Âli|ÎHübÄ&RïBn:ÔKâaoêûyÚÜªñÇäzfçÁ0ÙéX#1<$-+ÏgQW.x_3ÓYJ7ÀeÒFtw€!Grìî(Í,kÌùöAòh2í}Ö8óèI/%TC[Dá{Û=cúUÉL9~OS6à")
        self.matrix.append(u"/fZGLiñ8Yw-ê!CÍ2óP[}{Vbú Ê?~JcÁûÚvsq3É<E*Dª_$jB5MÔ|pFS4gé]>QhKòzÈo'%y¿ù&îd.ËNxÖ^Ûï7Ü(r+àôRèu)1áçAâì@ºaÇÂ:WU=Ù,ükÄÎÌH9í;O#IönltÒÏ6€ëTÀÓ0äemÑX")
        self.matrix.append(u"cX]#ÇàM>lLÂâ).èsÜ^iÔñ%pòGëj!Vz5@Uyç_îÚwÎáÀmdu:ùºHÖÈíPZ38RÄ|h,tSYW~/kú*g(+?O{q0}éD[9A2ÏJôïÉrÁI6EKFÑ;ö ÊÌäfoÒ&eÍ=¿ü1ÓBûQbxv-Û4ìÙ7ª<CË'aó€$NênT")
        self.matrix.append(u"*jwLºUÎY/ÈÙIx~BÔmk¿Éhyúàêä5$Ó3eR[l1@sñfÒô{üçÂÄÍ7ÑCìtJËEÊAèóáP=TQ 4bÜ'Mur9î8ë}Fz^>(?ûSÚÀp<ö&â;2Á]iG!WÖï.V%ò6ngéOK,íNvoÏ€q+)ÛD_0HZacÌ#X|-ùªd:Ç")
        self.matrix.append(u"GfuMÒó5ìá{i0~¿ÄJÎÌú+qâûQCÛ€oÂÏ'ÜÀ9_Hï1}Wë=ù<PÊîZck*hÈË(öº Íé[Y^&#$l|ñÓTÁà3òm>Ñ@/2ô7E!g.O:Is;yzbêtBÙ%dKN-çFU?èxRavVª]w)äÚípjASÖe6XÇÔ4ÉüL,D8rn")
        self.matrix.append(u"OS(RAbp,ÜW}gç;ÄB>lÑNÀ$ôt{ºZsq%€Â~QUoÙxê_][ÛìY.èhf?63ÏócâPÉÓ08XÍñïö7M5ÊÁI9Jzwm)ÈvLj<a!ETduäû-ªÌúÇ'Úkîy&nrH2ÒD/ÎKàC4FáÔ:é|òí1^=+ËGü#Ö ù@*ëieV¿")
        self.matrix.append(u"0cv(hNW|éi&jüAPy-ÉBwOömTòÛbàÀ%êÚ6è?ÏÖDªÁLK]EaìË$:H+kJ> ä*xfâ^ÔtÇÓó_,¿Cr[çVîQÎ)R3G<~7Ñ2úáÌoMeIºF9U{ù€;XZpñzgïd!8Äu5Üë.ls=ÂûYn@ôí'Ê#q4}Ù/1ÈSÍÒ")
        self.matrix.append(u"Á_ú(V4Yoë$n&r)f+i<pÒ/º{^EéôtU6ÓÉkàò!ËBT?8AÊÄhX¿lüN:qd=H,jKgRa*Íís7%ZÙçÚ#J v9È-ªWGeêOFóÎ.è@L]u2y3CI|>'SáM}PÖ€mz5ûù0wïäQÌÔböâxìÀÏ1îDÑÜcÂñÇÛ[;~")
        self.matrix.append(u"MÄx>Êêyî'OëLäJ/SPÌnqèe3ÈHBCdvo{$5Û=àm€Òbjéû2Ñ,RÇu@Y_çÎ;ZáÙÉQp¿Örªº:9FIùôí] .V%úâ~c[KÀ<Â)D6Ï4WkÁñzÚlüìò1|Íï7-?&i^AstÔË8fÜXGa+ö0#T!h}wE*ÓNU(gó")
        self.matrix.append(u"$ü~ä1Î()ô+,tAÊhV@ú#óWTÛp¿LáÍ7é_ûò3UG&9Ì*Òèo/6ìj.5€ËaXÁPÇOfw{iÀE'%!gSÑKDeduÂ:ZÚs]<FvNëJ>È2ÙCÜâÏz0qÓö-?Rb=º;BMx yêH8kù|àQîÖc[r}ÔYIlïÉÄ^ªnmíñç4")
        self.matrix.append(u"^ÍHùëE#ä;òâ>óÎ<à@YÊ0~'f?9nêº{ÇcoDTÏ-g)Nì+üM(%ÀËÒCPöÙ.yÉG3}!dS8éu]€LOaswÌÂ:ôèkhj5iïÛZ&/î42Ö,*ÑWFrá¿VñzIÓÈB6íÁ| ÜÄçÔûtRAª[Qqxvb1lX=7_K$UpeÚúJm")
        self.matrix.append(u"Sú/vR'ojÀëz%BwËª:4X,8=9ò}Á[ÛkJ@.Lùd+sb_çfûÒVö)ìQ(í]2ÇäT;-i¿ÜE xYîWéÌÊ#€âAÑÔ0OnÖ<È1gôÄ&3óêlàhHÍCu!$áD6Âc|MpUrÎGïIÙ^75?m>ñyÓFüKÉº{PaÏ*ÚNeZt~èq")
        self.matrix.append(u" ña,*_Ó$sÖmyòq#ËóVx(JáAtÁnZdHè5DEe&)êTMçb|9àCXwlWÙíÔº0FÄ['hzÑY]BÏô<~oÎIâÉéëkSì2j@G6vÈÒö=Í4ÂOcKúpüÚ.¿RÌQ:ÛÀîi/38Ç€ï;>^1%Ü7+?fNûuÊärùª{}g-!UPL")
        self.matrix.append(u"Î, ºcÈ&Ñ^*ª_vàTêÛZûÒëYV2Ôô8úLyÚ'KE4qËM$6sFÙP|m=0ò~f3]ñï7nÄe€ç1)öO?oÌár>l}NRÇW%éìî.QBÍ<zÁxiüùw(+óäp#gÀCtÊÖaÂÓ/!XhÉGU[ÜSkdHAD¿:@èíIu-{5âbjJ9;Ï")
        self.matrix.append(u"yUn'OóYQÒüÊàJjcÔ>tKêX$bÙ|Äaò%ç)FéWPïN&.Ñd}/B@Áªâ<hzCLmE;:ú3HrùÏeÛ{ËqS7Z#Vûì+!ôÌ4l~D*-ºkäá^R5T9íîÍfÂ?]ow0,1Óxöë[6ÇÎp8=sÉ€ñÖÀÈèiG¿ Iv_(ÜgMAÚ2u")
        self.matrix.append(u"fÌ*îù[@MºªòÎÍy6Ñe('óÄoVhc^ÂNJSdjïR_ék€%PáY2;DÇí¿]Ê UO3lëÉÒ/TêHÏ7ñ-.úü#)wnÙuWÔ?{ôtâI<Z4|Ó=vÚçX!ËAG+8Ö5qEx~91L,öÛû:KaQsiB}0F>CmèìbàÈ&$zrgÁÜpäÀ")
        self.matrix.append(u"ÇkQAdá[B] =$È4Gz*¿(vP^ZCSÉXÚ0:ìwt€75Ë!}úäYLr{?yÏçEFmñ;anó6ÍguâíÊh9xÌ%ªioÒ_Ó2ù8TôbÜ<ïMl'JÎ@pfÁ,e-òüÛsRÂHDÀö)&.cqÔ+>ëOêàÑI3VUWÖ|jºèûî~Ké1ÙN#Ä/")
        self.matrix.append(u"ír%3!vÌ ,=8#^ÈaÑ0SELgqÒmÜK1áò€ÙÔçI;6WY5jêïdªktFu?b&yp><ÁºëÄPTn{~)ÚÓâ-è(/Go+îV_àû*Ds9[ùñÎöHZìli}Ízüx.Ê@eÀäËCX|'ÇwMÖ]hBQcÏJô4RA$é2Û¿OUÂfóúNÉ7:")
        self.matrix.append(u"élÚÜZtág)MVW@ÉTíQA?xo(ÍnÓÂjsaòîÑ70KvªdÏúGEñÙN$4Ô!Ç€yì:Y /U{BfÛôbÌàhPê]ü}%^RmïS+_>CHDë9ç*ÀÄw,1LùuÁirÈ¿8-6OÒkâö'ûzË.äºÎce2qè|I<p#Ê&=~;5Fó[ÖJ3X")
        self.matrix.append(u"Öh_ <ÉbÂV$v€éèK6ÈiÔ9qGOû2&%.Fy:Í|,ºÀIE'Q¿üÎwê>WòÊñt][SMîÇ+~Pâ5ïNÒXj/puíDrö?á}Ú@0k7c)oYzÜÑd(ª4ÙçCìÓ!eJ-ëRùÄ;8Û{1äôúsBa*xÏËófÁAÌ^UH3Zmnl#=gTLà")
        self.matrix.append(u"ZNt/eúC5sDFó6áëQÂOW(TÁä<üÍ2vÜÙÔÒGö7}&Ä+BñJ8À0 Hk3àl€í.MPªbÎÉxòoÇ#¿a{f~)=èÓUâÌu!û1Ï_IVrÊÖ>ôSÚc;$EgçdXm9-ÛÑ%[q,*ny'hîLìùA?RiYjwÈ4ê]ºË|^ép:zïK@")
        self.matrix.append(u"&hûqNöºÙÄÈ<$Rr>leJz1ü#YOpBÍ*Z/6E0xú^U âs7faiL2F.(Cn[SªVoP'íÖÔ?ÉQbïéçwàIÎ;êKÏ5¿!XñtÊ}ÂèÒÁWò%Ë8gc)uÑDäôkÀj,+ÚmîÌ-ù€]AMy_ÜT9dÓëG4=Û3~Çìó@áv{|H:")
        self.matrix.append(u"rüúÁ-%HpIsà1Ü4WáÂºÍkÔÖóè>0ç&é]ocU}ù¿2ÚTqÌEmD:ïVÄÒfhPËzîûBì€FÓ?ÙjnK$ÉO=gä~X6íCñw9x'8LN,(_ªëG QZÈAd.lÀ{t[5Jêâö#i^<ô!3Û|YÏyu*R+;/@aeÇbò7ÑvÎMÊS)")
        self.matrix.append(u"Ù;l.9y($ìzÁ,6Òú'ÑeW{%YBwn2üI[_FVÈNc¿OPÉxÌèªÓjä)ZUÂsaô=J|]Ä<D}À CÊ#@h*kÔá~Ú&?>iíÍuEÛdÜ01G5ËñKÏâºÎ/ïoQùó^öûpR!34HÇ€vtrMq7ê:XgëÖòéfSLç-T8à+Aîmb")
        self.matrix.append(u"Êç'gpxì%#è}L8ªP_îwÉ&áYT*kâÏ|üXcñÓÍä){ºeÒ,ÖEÈI¿$+1Wz^ïnFëUù5ÌËÂ;ò2Ñ~D4óKÁímbêfÀltsQà/VûaC903![iyJöH]BAôr=?ÇéÛ€oO@G6h>(N<ÙMÚuZj. vÜú:-RSÎqdÔÄ7")
        self.matrix.append(u"H=Óq!ÊNÎRû*:oCr/a^z3ÇhYBFúxÚë;í)DöòvW$d}8iÈe>JZ'XÙ,&E4ÒuÖê7àÑ¿ bÜÔImï([áñÄw~Sì9ÛÉ.K+ªºÁîO?]%AÌc1ù05PQgy€ü<{2ÂjËkçô6ó_stÏn-ÀVäflâèT|UéL#Mp@ÍG")
        self.matrix.append(u"ö;d€a!ºZjÛËòè?&S|ME~4çWáLxiÊuñtg_0Ñ.Ü=9<Î1fQlÈÔ*óí)5ûÀ@â2ÖÍDù%o^hkà(ÁìÚy}cAÏ#w¿3qúC+O]ïîÂVzäün I6YÉXr-8sÇmbpëéFTÓª'KÙ>eÒPNvHÄ$U/J:,êG7RB[{Ìô")
        self.matrix.append(u"^~U=Éw(.eÎ3fÙ}BXgÍòaVÛtÁoâ'LÊ9é;ÈQ#ÏKàÂÓªë@+$6rûE*Pê2á/uI hGîÑn4<ËkyHÖZ&DYJ[Úmçñ>OS€{,Ü7¿zdsóö_Ô|0ÇW:ìqèúMÀl)Tv8Rô]?ºiÒÄbFcïj%üä1íA-pxNCÌ!ù5")
        self.matrix.append(u"EêÇ<áN=1zâQúÜ@ëd43,^ïùPVéÙÎ)ÓçûM&HJ-cLÄº*ueìoÌhlgSíZ|Ô.AwÍ0FóqX¿Ukà8G}9[KRsIC6yä+ËaxÒö :B7Ê'ªè]vÈi?2{#ÉWOmÚÁ5_üb(ÏtôfDÂ>/~!nòîÀ€jYrÛ$ÑpÖ%;ñT")
        self.matrix.append(u"éOë¿í+qv&È>tï(<Ö8YeLbIxCilÊg@Ç%ùÒTºâè[äç3êfÁz}]mìdhX6B.Ra^sÍJËK5ÎñFjDÌ9GQ1*!70=M#kNÛ/4Wªy:HÜVo'){öÉ$S_€-Àá;, cÂUî2úÙnûòÚPÓô|ópr~uwÄüZàÑ?ÔAÏE")
        self.matrix.append(u"ú>Sé%*ê~F.@ÚÑü<ïÈóçkùÇhÍXË'òô-Àº{Wñ7Jf6w}iäL/q(0ëÎTc^OÖz[ÛE4Z9RuP!K&U8Gâ$oÉÊt+ÔáM=û:25bÙàdaí1,rs;NÄAöY]m#g?ÌÂ|ÜÓ€CyÁÏHVèvîjI e3ì_)x¿pªÒlnBDQ")
        self.matrix.append(u"?s=n@wËàÁ*kCçäâ{53îªtiÙ]UgÀ;1-dó>Û8Çòp#QíÌ|ÂlV/.SáozeRïa(ô7N0ì<DùüEKjOÄH¿Bh}ûÏb)ºèuJ'MfZêm9!:ë$xc~A2[ÚÓÜv,ÉÖXPÒ6Ñ^IÎY&ÊérqöÈ_ñÍLÔTW+G€úFy4 %")
        self.matrix.append(u"ÂÖhÔ~ëà0}ºÁfP)¿(I8eÙ9!ûÀâ#ú2g?NnajuÚ€,*'&/Î.î[F%ÑW>iü-ÈoCb@;DlTíkJx4çX<á6GrùÇAé5EÉÊèö{ZQOHªKqÏïRêLÍì1|czSwËóÄvô+mt]ÛÒV3pMñ_Ìs^UdòBÓ:y7= YÜä$")
        self.matrix.append(u"À]k€?uÌÒÍBbv(X:147é8âHûOQç[È'i&.CÑ*)3_dm¿ªPrIÖ}MÔcôna2îgÊEáYST+AR5úqG;$hÏìj=^Âl#êópw{íWÁ-zË0ÜFàÉ ,6fòÄÛVÓxU!>ë9tLNyèJKÚÇäDº~/ùöü%o<ZñïÙÎe@s|")
        self.matrix.append(u"(f>1YV}.ÓQ)aÀâáë=Ôb$/jí%{0nPvcmÏÒ_XZoé8C'|7ª6[èóHäùEÁwÖàÂGìRM@OS ,4Îph*¿ÛñÄBúkAyWDI^TlºtÊË#ur<dÍ~Ñ]eûqîïJç!öÉ&:3iN-È5K?Ùz9g;êÜÌôÚLòsF2+üU€Çx")
        self.matrix.append(u"ÁÓôR(yW9^À-ìubñî/âº|JK@<¿ÒÈQGxkáFò{öÏª4Ç';UËMeÛ3%Blr.Is1~€mdC}2àn&û,L0ù5)Üg]T>8:oÎq*=ÔÊcíaèO#vwHê?ç7z!ïÄÑäÌSjóP6YúVN$üEAÉpÙÂ[_thXZfÚÍ +ëDÖéi")
        self.matrix.append(u"ñmÀC0î~íè_+/çêDâW=eÎ}Û8zTÏ'ÂbÄJ^ªo(G{sà ÇiÁM6uºyB€3ì2YÚ*ÊLÈ-Éù.úqXÍï>vw,&RÔ|dnpaÌ)chk:9të$%!O?I4ÒEjòSUP#N<QáÓüÑKHéVÖöôó;7ûr5l¿@Ü[äFËÙ1fxg]AZ")
        self.matrix.append(u"hÜÂWuÎa<úb4PÒËsÄ€tÙÈíÛ0ÏdñîTèÚò,2_+L[#r&m}V^nâÌ@vÁÖN¿lICéEÊ8oyïGêkU-OcjfÓ$à1;É?ªäzÀóYü|ì:.Í=%7BSöD5xÑ]MQç/Z9iJK '{A*6R(F~Çgeº3HëûÔwXùô!>áq)p")
        self.matrix.append(u"ÂÁHJd<mbDáÛ2Q!hä$IS ÌëRT+Cu.AÉ~t=ÖÎ]5PGKey@nê>Ò?ïaÔÄÀÇiúXûZEòÑ;wôjf[é18cí€Ú#voºª0BùFüY/{(^gç)*3Êz,Ísî6öUqÈ4-¿M'OpèÜrkl}ñ&9à%|WÓN:óËâìxVÏÙL_7")
        self.matrix.append(u"bkfù}F5R$;t-ÒW6*AJpàZxä]cËéD!ÏI~9'HÄÙÂLºqaÌ1?ÁQrûi>u)GöTEyn#ÜúÖMzªsÔXoè+V.â%ñÉBNô¿w{:|PÛîÚKê8[eÀ3ÓÑCóáüì2Ol&/íïU7dYÇ=òë_gSÎ^0Í <,4€jh@Ê(vçmÈ")
        self.matrix.append(u"oëÄjò&€5ÁYsêÉÎ(ûC'%)RÔÏú*Ë:PTÚÇàïéÂ!Ùí;#Ûmhá2Mâ~uGFBfxñÜw=çkIr-<lq0K>U[entîäQÑ$ô^,È4.p_yV7HSXü+}NÓ8D{ÒÍªaW6ÖLÌ/c?9O|dJögvE¿Ê@óA3ù]ìºibÀZzè 1")
        self.matrix.append(u"?;YrIKcURj~a&:$,âS5Ümlq8ÖB NET4%ºuDvÊW<=êÒCèÓ1íH¿)J|GÍgùÇ>bé]î-7Á/öÌûÉF}tìôò2o3QÛÈ+6A*@ZzLÔÂpPúfàX0yËh9.ÑOxniÄªÏ_€dswñ(áeM{ÙëüäÀ[#k'^!ÎVÚóçï")
        self.matrix.append(u"8}!5n9ÎQLGÏX.¿1~dôÛÈébaK60WhöSÒñ4y'ü-xCPó,;ÉîUDùÂ=[ªìB2€@3ÙáEÀ&JH òâïsÊ?u%m]VÚÁúçäq{:R+IYAÓºê>cË^íOÌvÍÇw$ÑZTëop/û<ef7àzgèjNlÔ)(kr|ÜF_*Ö#MiÄt")
        self.matrix.append(u"â$<èüvÎT&},:òbàÇÀ@zRP4rª9]?e!;çVOjëG*lêÉFÁaM~ÄÏô¿ûcÓ>XS0Aé(YÙEìnCIU#Ë{gí|Kú€ñds1/m2îZ-yÍok573ÑNÖJ%6ºÚ.+[BÌxÜ^Âi'HWhÛtÊwäuLq=Ôpfï8QÒ)ö _óùDáÈ")
        self.matrix.append(u"ODè7{ô(tªÚBUREÑTáêÜkËÄ+/L0qWòÔë8iÈ%^MzmXVöüóÖr)º:3ñxÍJ6pÂAìCÁZfÇlî?Ê}# a.QK[Àcsu,G|à¿bnúSY*2=wûvj1ï$€<-@o_;4ç&>'Û!ÎÓíPHF5gdÌÉIe9hù~N]äÒâÏÙyé")
        self.matrix.append(u"ÇIÍOGê5îu+>.íôÁ@VCEú USÔï(cÈ-ËwÚìöN^?Ank:)a8çé{Ùv<Êè'$ÉHhy;¿r#74lÂDY3âÎÑe_]QoKiTóÏq|[FXùÀ2ºZ*ë9BPÌÓÄÜJj&Ûbds=Mñ6LáWÖÒ0x,ªmRüpàz~ä/1%€tgû!f}ò")
        self.matrix.append(u"|<îL:2oËGj1º.0u=Ôê+4Eù/Y8pÑ?t^ûPO%Möl5úbÛ]üF;ÌÀ9Ü>mSVUë#fZgKÉhqA3&€xàªïsw*D6 aíÎBdWHrR(áy)ÖòéNcJ$èÁÊ!Iâ{nÍeñÓQ-Ï'@ÂçÒv[Ù_i7ìÈÇÄkzäôÚ~ó,XT}¿C")
        self.matrix.append(u"öJÖÎ!2>(EaMVlÉì=ï$tHÓ á@Ár}Òy0PnÑçI59;Ï#{èô€3Ì7üóòâÂñävhêF~).À+d-&gí*4j^ÄOÜ'S[:D?ÛAÍºkmÙ¿iªeNÊxÔ/o<_ÈWËûàUGps8Y]QwùÚzé6Z|%RúBXLbCîÇc,Kqëfu1T")
        self.matrix.append(u"-eªxô~UÌÑC4VZÎ3Û:=_7D.P]#ó<giúûShÓIâ>'QÍÂ;üL2ùÜËcX¿trNGYjyÖls)èçé€TñAö[îEíuÙÔKÉn?90^Ä1Md}BW(@wÁº+ào%qìÚ/8pmÏ!á{zëFÇOäÈ6&a,kRò| ÒÊf5HbêïJ$v*À")
        self.matrix.append(u"C2ï:|SHDúwY;#ùÔFüq(+é3l9Á)ä4fÎs,dî¿uì<OíêÈÄ}èëÉg?6ZmÇ [&ÛcÜyÒ]JñË^ÖNç5~òW0!j1pMÓnivÑ${Ieâxb.ÏáXQtUÍoó%ôûºrözk*ÌKªAhT8L/B_@=àa'Ù-RP7ÚÀ>EV€ÊÂG")
        self.matrix.append(u"IË%wi_6!uàmè)Nî;ñ~órúù:éyÒxëfÁ^Uh*Ín9vûT{Ô o¿dMDÏª,zEÖpÛÈL0(]Se|€FW#B}t3áYâ=VlJºK-í[ä@ÓÂ.ÌqÀÑÎQ/CXçôüjHêbòïk?4öaÚ7gÙ<5OPÇ>ìÜ12ZÄÊ&A'ÉsR+G$c8")
        self.matrix.append(u"ËâÎ.BíAC@]$ò/Ò*ûFkÉ8Z=Eî&}4ó{ª^dDt2SÀºçL70ñÍÊT~Vrj#1eômHïÙ-ÈéÑyäèx?ÇN3Yhw +Úàlës¿u)JÜGvÄX!9ÁÓI(ìiR'zn€êúùf;ÂQ6o:><_aá,%McU5pKÖgöWbqPOÌÛÔ|Ï[ü")
        self.matrix.append(u"ÂóÌPâf5î0iRÒ%Ó,ÖCÁÑ?uª-7ìXGöoaïàüÄÚZès:)Ç;~ÊlhUû4{úHÎçze€ºEYdA81+>[ô!TÔ(äyëq&}=]W_ÈÉw69êËjÀSIDtQÙpñNÜÏéùxí*ÛK2gO$rVJ3c <@v'|n^/LMòÍ.bF¿á#mBk")
        self.matrix.append(u"#AèÎ+>ë?U$*Wòz,)¿f_ÜÙ<8B]MÄQaÚïÔÀXJà IDiem}|Nq6âFÑç-ñ7n49ÊÇËöp;xHÏR'ê@áCKh:sûÍ/ôP^ÉÌSªcº=í5[Z%2óVÖÒùEÁvOo(kgl0Gd{3!ÈÛwL.rìuÂî&j~€éätbÓ1yüúTY")
        self.matrix.append(u"ÌXB.Y]lNiñM7L!ÈTÛÓòy,jgI4Ë^Òv|ôf$ÑPç(d }JâÄëpàGÖtªs{*Ô?UOÉ3äcHîûbö<í2ù[€CuRSúüó8Î=ÚQ;m1rwÀ9#~KaFÜÏxkÇénêèï+ÁV_Â:Zá6@¿eqoW5'ºì%Ùz0/hAÍDÊ&-E>)")
        self.matrix.append(u"ä;W4xÉöÑáç9yh@à^!V*èTÇ[_aïÚFo]r5#sJùÛ,Mò cÔÀÙP|ó)EYk2uíX'ÂÊîwüN.=ÒU+(zBë?Of}CêDv01¿ú/ì>LÏé%ÁSQR8tÎÌÈû7Üm~Ë3Í6Ii-qâªe€Apn:Öôb&ÓGg<HjZ${ÄlñºKd")
        self.matrix.append(u"Ûê=LÒ¿ÖìnâÓw^h8-?2Üû:ôF&PX/i,É3k5DÁÇ#TAmÄ%äü1*ï+O|Ë<eWóÍzJRGªfc4.0;@ÏÈÔàÑ$ùg)ú[SBvlUNt(ñ7Îb_xQHICqÂá'íMÀ6KÚ~uo!sdarîÙè pYÊ€ö}jç>]VÌòyEº{ëZ9é")
        self.matrix.append(u"ÉÁe|[ÙÊ#0]SIáä74lfybjÇstRñ¿ÔÚ*+ëuZ$?ù@1Öé.K&aJô83FY'VíE!9Wwi/Ó>G5ûÌçhpì_H<QÍúgÎqL^öâXU{ó2dª-NPAk€DÀË~Ovº(;Är%C,òà)BêînÈÏïmzÒÜ:oÛÂc6è=Ñ}TüxM ")
        self.matrix.append(u"Á3>MQÀ;XT]SdJaAlÜÚ(5VÛuî8K,gp@çÎ29úëïmr=oD Ìx'èjÊìsUùWüÂÈ)~%7äªE4hYÏ!?nû}cÍËwêbH1Ç€Cñ<iRPâô0Ô-IzÒ/Zk&íÄyÉóLGéq+òÓ_{#:*¿ö[F.B$|eNOfÖtÑà6ávº^Ù")
        self.matrix.append(u"oCÛ*ÜÊ:ì7ª=FxuS8|P$äv3Où{1ºg-ëÀÌî]Y€Vr)GUQúLÈ(XôçMè@àwAiIs4ÚR2km%#ïdÇÓzíBÙcüÍ<óû[0tâbN6áTjòl&Ñé!;n5EÉaq,ÖêÒy9Á'}W~Ï?/ñ_^ Â.Jhf¿ÔDÎËepZö>K+ÄH")
        self.matrix.append(u"€/ñb{GlHDËîùLÒo:Nt10ÙQu-2Â}Uà=VwsJçÏ+cFëÔê^rÎúB|&9Am_d>'Eq,$6Éó~iÊ *8ÚYXOvÁìPIÀpÓTâÈMSä#7¿üÍxÌïKeº4z[öÇ@!fôCWkaéÑí.;(j)Z3%5èáyò?hÄ<ªÜgnRÖÛû]")
        self.matrix.append(u"$X&1UÈÎªºçÍ9ZÂDlvg_ó5qWíï#B~P}.áFLÖA'>%üËY4€äojÔcQOò+ÙKx@n20:NÑÒ*k=)e<ê7û/aruàh?mz!SH JÛèMë3îdÉÁwÌitfs[G]pÄù-EÓ6ö8ôé;ñú(ÏÊ,ÜÀVC{Ú|ì¿^TbRyâIÇ")
        self.matrix.append(u"u<ÍGRwÉá$FÇçÔ8Ì1Ù)*yMh'fqcUv€Êi-~Bà óSQ|ªî7Nrñ;:ú,òâ{2xYÜEÎXÀtbPùÁÖ90íd.ÏÈûOJÓküH3ô/]VTaIZÂCeD?ìLKömo=A!_j}Ñ4Wpl@6+ëÛsé¿ºè%Ú(&ïËg>êz#Ä5^Ò[än")
        self.matrix.append(u"@1áJª;,MP3èÖH!éÏÀ-t[y$4ÈsùäóLZÙÁ+:0êDìGQú7ÇIOîl)CípY^bâz>ÒWj5S6û&òrKÍ/É{EÄXqRTknñüçeËÛ9€Ìdf}àN.hï'Âº i8oAÚÓö_Êëgcw<Üx2aÔ=Fvu?Ñ(¿*|]~BôUm%V#Î")
        self.matrix.append(u"GV*lTZª8Ï|Ë9ü'öd1KÇB4Ì/J¿fÖ0CèLRI<o~>òúÑbkçî%éêeñà{qjUÍÉmÊ$]x&ÙAÎ,;XFÔg S?OawÓ6ïrÚ-hs^Yâ(Á7_iäuÂÄ:MùÀ+zì3€P2WáQÈEt.#DÒp!}[n5íº@Û=)ÜNûcyvHëôó")
        self.matrix.append(u"wfû8ì1Ñ7tÍè¿yMS|RÎg+/'Ü!dL(<h àîúáb$@ö€NC3ÒAmJ:[çoÉZD2eYFñªsi&Ö;5)0ÓQV-ÇÚ6ù^v]rEa#?jTOº>ü,lÏ9PÈk%ÂíêWIé.ïÔqÌ_X4ÛëóÊÁp=KcË*UÄxuôz~ÀHn{ä}âBÙGò")
        self.matrix.append(u"q+€àánriô?2èvDÖ;Z{ùbyXU_zñjÜçRCÓGÙÛ7PkÈÁû1À[.s,TöF!5%Lm0â:ÒfKcÇI)ò|~/E=Ëúü@4l8ÄÎ¿îóìoeÏÑ9JÚdÂuQ}aY'^ígShMëN-6ï$>Ì ª<ÉOpHÍW*&xÊBÔ]w#(ºäVê3étA")
        self.matrix.append(u"èS0ÑÄÇq|ºÚ{$ùìÂE=ewDÊfóU~áöôîY5/J3KêHç%úW€jÜNcnàûL (}bI#*Í7ÛÈpÖ4ª1zÙ.&hÒVM[?ËÏ_ïRmd8'ls^-AéÌÉy<rä2ëòFiQ;oñg]tZ,íGüBÀx¿O@X>uÎa6Ô:)+TâCÓkPÁv9!")
        self.matrix.append(u"K~7ÄtF-PäZà2.ÛÔk/Wd^LÈÊ<VEMëºA1Rq;,Cehiwâr'=Àc)ÉfòSÜì53lÚU%+6¿somXúá|n#ùQ!g?aIôûYÙ>4BzüéJpª8:vjTê@DíÑuÇóÖ_(Îöñy9OG€Ë ÂÍçbÁÓ*{}N[èÏÌ0x&î]$HÒï")
        self.matrix.append(u"(J6a5c~GIÎFx!èá$f2HwQRîÉ8k}rúv?ó=1üuÚAñÇö]lêûL0ôÜìÁ 4VÌPTySËùs|ÛmÑÔÒEh.ï<Óz%ÍtÀ¿N[&9/bÖYKZ-€Bi^OòWojçë{È;ÂDd:â_3nÊéÏMº'à@,í*#Ä7>Ù+Cª)UäeqpgX")
        self.matrix.append(u"?-ªfç/dÄûó€ÊILE^lNÑàQHj;<Z8îTzm7Às@R2#ÖDApUòÜÇ:ÁÍS!Ïq¿Â),Ëb>4}y3*êÈúèÒw|9ì%hÌ$_arºO6gPÙB ~Y+0ñÔMäávX5ekëtuâG[]ÚcoôíönÎüW.{FxÛ&CÉéùïÓ1KJ='Vi(")
        self.matrix.append(u"ÌÔÉmÑp€ÂHF3ÍrDáb})qúB/4Ït! ~.nP5ñg=7Cª_ys1º]{ujV9,Òè#ÙKfÁ'é[Näôw<Ë%ûízâüdGvMEOYòçÇ6LacR+S(Ê:ÎAó>ù;Óx$lo^àT¿?2ëÖZJ0W8îÀXï@Ü*hiQUÈ&Äê|öIìÚ-keÛ")
        self.matrix.append(u"ô^6ÈëÇv+{=eñ}<nÜf5(zTq/SCÚ:~R0yhÙ#è?Ów3mÌX_ìÀÂûZ ÉIN€lÛpójG7ÎdV*|aüPÄEKrïäÊoî2QéºÔHM-$.Òsù&i[9Aö!UªË'Öê;Íòxb¿çBÁâÏ%L>FÑD,úkcáít14gu)]YOW8àJ@")
        self.matrix.append(u"bQF)eaO_k^C€GÎäÓÔdìi5ûèZ,çqú#w l@Âª=îÍ/cAuÇ27óàù1À4{ñ8p~R&Êüg(yYÚIâË*j<êfHé;J}öSÛÉBÈr|XWvòhÏ[ëºoíÜ9ôÖ]0V+EK'.3ïn%?-T¿áÒtPÁs:6DÌLÄmÑ$>!MUÙxzN")
        self.matrix.append(u"^{Âhï,_W[ñlsFÓ)3]I.t56x$RcçpwvZYÌ ºLäûó1rUâdaú<?ÍjáG&ÀoÄK*S9Men@z€+/AÏ¿=ifqu'7|4òö;èÖ-TíÈÉg>àêÜ~îÛH}:Oé2ªÙë8ük#PDÔËÁ(yôÒìQÎÑÊXBE!0VNmùÚJ%ÇCb")
        self.matrix.append(u"F}óÎ@ÙÛìû/w>ÉyôÏm16ÀVÖE^ªPgIRs_jÌ.á|îuÇQcG+úW?OÂlÓéç4JY-&<rëSöp*fH{º:äà8~%vïÈo[Tña$LùeÔt]!¿Áâ'ZAdêB€i9Kí;0Í(è,2qÄü3ÜU5Ën#ÚÒx hò7kÊDXNCÑ=Mz)b")
        self.matrix.append(u"ÔÂñÒª^1iëó$mêU*cCö'g?úËïRy}u- &/nÍ%N[zsà4Ñ0Ì@Qo9ÉÙÊ>PâeÄ.¿xYBhçäl:#{<FdòI8bAº!ÛqXk7VMÓ+ÎJ|Ü2pLfüD3]á~OKùvíîÚ;èéÈWÁaSwÀûÇ)Hì(ZôGjE6,_tT=ÏÖr€5")
        self.matrix.append(u"ï67woàiIÚt;!Èî~ùfÀlTGk Ñ¿Lëv5}ü'qÜö=/[ÂÁÇú-€]x?ûnA_XârNáÓÎ^KVuFb&éz<y#.%ôÔH(ªjÄË4120cíêR3>ÙU*òºM{añBsÏdQ,P$CÌ@ç|ÛäEY)ÉW:ÍóD9SpZ+ÖÊmeèghJ8ÒOì")
        self.matrix.append(u"ÛÎZmÊáíxJÙäRAë@âÁ!êov ËGl+€>Íï<u8ódÚÈjQ)Nñ:aODü^kÄF3]IcùÜC*V?ôEÏèºÔb-fHòLMKÌ$q5W&Â6~0;ÓÀ(i|,é1%7.#Éà[ît¿}gPÇXS{4_öçswe2r'YyUBhûÑÒìªpnzÖ/T9=ú")
        self.matrix.append(u"éúNÄÁÛTîqÂwÍ~ÑDd*Ç;Vtôn9]€b?i0e{z|>/4EXícê8AÓ&)¿R.:rÌâÏ1G$çàjB}h3ëIÔ#ÙLüZäª=òkW_ÊìïyxU^%oSuC!HóQpÎ@áñÜº[7g<al56(PËFK MYm+sÚfövO,-ùÖÒûJ'2ÀÉÈè")
        self.matrix.append(u"ríÄÀ2(ïQ5ñ'Ü+Âmb)kçä6ÒîÌpI8-qPág%>eOÔST9Lyù€Y ûAn]vVX$|Ö/cjÎ#G<ÈêKz1[ËôtdRM=éDuf_ºÊÍ!@òú4iwªBZ{s}hìlÙ3ÉÚ,J~NÁöEÇH;óÑWÏU¿ü?*^aèÛâ0:ëo.à&FÓ7xC")
        self.matrix.append(u"a0OÙüÊkògH(IV{W)D_6c4!ôîûÂTZJEN5xïh'¿ÁójFA*|;RMYºÍíª-à/XÎùëÒÓ21Cmçäq,ULÉGÖy=?€i}nèÀ]uË>3Ñ8K~dñÚ#ìsvâÇeÄ&QöÛrÈá9Ìp[êÏwÔo.zltS^$Bbfé%7:<+ÜPú @")
        self.matrix.append(u"óMOd0/o{Òímîëò:è>(CnÌÇ+A€t)FÍñ[Ô-ËìD@ÛÁQcÉ8qô ïg¿ä|!ûBrjáTU~Üe<Ùù7ÄylfYÎ^sÊG5%À='LêiÈXv9b3Hz&$a.pÓ?hI]Öö}éwJ*RSPª,kçÂºúÚ_6uNK;EVâ#à21ZWxüÑÏ4")
        self.matrix.append(u"=x' SyôºjwsêÉr04&ùÌé$ªëNZÀB/U;cXâÜmîRËïFD:Â)ûÙloÛ+n>~EÇÎ|P}Jbè^ú1ç!Ä.ìiaY{](e9v?L*Ñ@fÓdöKÖñíH8V<ÚA%-pzWh#gÊM_IOÍ,¿€Ò72Èk5äóüÏQtqòGàTá6Á[uÔ3C")
        self.matrix.append(u"Ivs8níiZ*ÇYç]Ìä+È4NSò^~UËHWm#b?¿uwKqh$Fºö)e g</Ü@áBRî:9Lc&rJïV,üû!Pâéo6êÄÀtÉ(2ú0ó|MQèyÖ5ëÔÎDñÂjÓÑÛ'TXôaù=Í>Oª%Ï[_kÁl{z€ìÙà3}CAÒdÊÚEp;x-Gf1.7")

    def remove_char(self, text, pos):
        result = u''
        imax = len(text)
        i = 0

        while i < imax:
            if i != pos:
                result += text[i]

            i += 1

        return result

    def get_random_line(self):
        result = u""
        pending = self.codebase

        random.seed()

        while len(pending) > 0:
            pos = random.randint(0, len(pending) - 1)
            result += pending[pos]

            pending = self.remove_char(pending, pos)

        return result

    def create_random_matrix(self):
        result = []

        for i in range(0, len(self.codebase)):
            result.append(self.get_random_line())
            print u'self.matrix.append(u"' + result[i] + u'")'

        return result

    def code_hex(self, text):
        result = u''
        i = 0
        imax = len(text)

        while i < imax:
            pos = self.codebase.find(text[i])
            virt = u''

            if len(str(hex(pos))) < 4:
                virt = u'0'

            virt += str(hex(pos))[2:]

            result += virt

            #print str(i) + " >> " + text[i] + " >> " + str(pos) + " >> " + hex(pos) + " >> " + virt
            i += 1

        return result

    # def decode_hex(self, text):
    #     result = u''
    #     i = 0
    #     imax = len(text)

    #     while i < imax:
    #         hexa = "0x" + text[i:i + 2]
    #         c = int(hexa, 0)

    #         # print str(i) + " >> " + hexa + " >> " + str(c)

    #         result += self.codebase[c]

    #         i += 2

    #     return result

    def code(self, text, key):
        result = u''
        i = y = 0
        imaxi = len(text)
        imaxy = len(key)

        # Inspecting the text
        while i < imaxi:
            # index in key
            if y == imaxy:
                y = 0

            # Locating the current position of the key in codebase
            x = self.codebase.find(key[y])
            # Select matrix[x] and locate the current position in text
            z = self.matrix[x].find(text[i])

            if z > -1:
                result += self.codebase[z]
            else:
                result += text[i]

            y += 1
            i += 1

        return result

    # def decode(self, text, key):
    #     result = u''
    #     i = y = 0
    #     imaxi = len(text)
    #     imaxy = len(key)

    #     # Inspecting the text
    #     while i < imaxi:
    #         # index in key
    #         if y == imaxy:
    #             y = 0

    #         # Locating the current position of the key in codebase
    #         x = self.codebase.find(key[y])
    #         # Select matrix[x] and locate the current position in text
    #         z = self.codebase.find(text[i])

    #         if z > -1:
    #             result += self.matrix[x][z]
    #         else:
    #             result += text[i]

    #         y += 1
    #         i += 1

    #     return result

    def encrypt(self, text, key):
        result = self.code(text, key)
        result = self.code_hex(result)
        return result

    # def decrypt(self, text, key):
    #     result = self.decode_hex(text)
    #     result = self.decode(result, key)
        
    #     return result

