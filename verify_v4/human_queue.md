# Human verification queue (v4 high tier, both Claude and Codex say the gold label is wrong)

313 rows. Each row: id, text, gold label -> corrected label (Claude / Codex when they differ), Claude's reason. Tick a row to confirm; write a note where you disagree. The 119 rows where the two models disagreed are in `disagreements.jsonl` and are not in this list.

## ag_news (186 rows)

- [ ] `ag_news:test:3805` **World** -> **Sports**: "Munro, Morris Face Off in NLCS Game 2 ST. LOUIS - The Houston Astros put their hopes in a pitcher untested in the postseason when they give Pete Munro the ball to start Game 2 of the NL Championship series on Thursday, o"  
  A baseball preview of "Game 2 of the NL Championship series" with the Astros' starting pitcher is Sports, not World.
- [ ] `ag_news:test:6150` **World** -> **Sports**: "England humble Sprinboks Charlie Hodgson scores 27 points as England overwhelm the Springboks at Twickenham."  
  "Charlie Hodgson scores 27 points as England overwhelm the Springboks at Twickenham" is a rugby match report, Sports.
- [ ] `ag_news:test:2028` **World** -> **Sports**: "Ryder Cup: Europe close on victory Another good day at Oakland Hills sees Europe move 11-5 clear of the USA going into Sunday's Ryder Cup singles."  
  "Ryder Cup: Europe close on victory" with the 11-5 score at Oakland Hills is golf, Sports.
- [ ] `ag_news:test:3063` **World** -> **Sports**: "US football: Patriots' historic win New England win a record-tying 18th straight game - plus an NFL round-up."  
  "New England win a record-tying 18th straight game - plus an NFL round-up" is American football, Sports.
- [ ] `ag_news:test:4234` **World** -> **Sports**: "Cricket: Pakistan edge ahead Pakistan take a slim lead over Sri Lanka by the end of the day two in the first Test."  
  "Cricket: Pakistan edge ahead ... in the first Test" is a cricket match report, Sports.
- [ ] `ag_news:test:967` **World** -> **Sports**: "Maddux Wins No. 302, Baker Wins No. 1,000 Greg Maddux pitched the Chicago Cubs into the lead in the NL wild-card race and gave Dusty Baker a win to remember. Maddux threw seven shutout innings for his 302nd career win, B"  
  "Greg Maddux pitched the Chicago Cubs into the lead in the NL wild-card race" and "his 302nd career win" is baseball, Sports.
- [ ] `ag_news:test:1080` **World** -> **Sports**: "Davenport Advances at U.S. Open NEW YORK - Lindsay Davenport's summer of success stayed on course Thursday when the fifth-seeded former U.S. Open champion defeated Arantxa Parra Santonja 6-4, 6-2 and advanced to the thir"  
  "Lindsay Davenport ... defeated Arantxa Parra Santonja 6-4, 6-2 and advanced to the third round" of the U.S. Open is tennis, Sports.
- [ ] `ag_news:test:4549` **World** -> **Sports**: "Australia 362-7 v India, third test - close (Reuters) Reuters - Australia were 362 for seven wickets at the close of play on the first day of their third cricket test against India on Tuesday."  
  "Australia were 362 for seven wickets at the close of play on the first day of their third cricket test against India" is Sports.
- [ ] `ag_news:test:2468` **World** -> **Sports**: "Dodgers Nip Giants 3-2 in Crucial Series SAN FRANCISCO - Shawn Green can sit out Saturday knowing he was a huge help to the Dodgers during their crucial series against San Francisco. Green hit a two-run homer in Los Ange"  
  "Green hit a two-run homer in Los Angeles' 3-2 victory over the Giants" is a baseball game report, Sports.
- [ ] `ag_news:test:450` **World** -> **Sports**: "U.S. Men's Hoops Team Finally Gets a Rout ATHENS, Greece - The Americans got a taste of what it was like in the good ol' days. They finally played an opponent they were able to beat easily, routing Angola 89-53 Monday in"  
  "routing Angola 89-53 Monday in their final preliminary game of the Olympic men's basketball tournament" is Sports.
- [ ] `ag_news:test:1466` **World** -> **Sports**: "Colts Lead Pats Early in Third Quarter FOXBORO, Mass. - Peyton Manning reached the 25,000-yard passing mark faster than anyone but Dan Marino, and the Indianapolis Colts shredded the New England Patriots for a 17-13 half"  
  "Peyton Manning reached the 25,000-yard passing mark" and "the Indianapolis Colts shredded the New England Patriots for a 17-13 halftime lead" is NFL football, Sports.
- [ ] `ag_news:test:2656` **World** -> **Sports**: "Cowboys Defeat Redskins 21-18 LANDOVER, Md. - Bill Parcells celebrated the touchdown with a big smile and his fist thrust high in the air..."  
  "Cowboys Defeat Redskins 21-18" with Bill Parcells celebrating a touchdown is an NFL game report, Sports.
- [ ] `ag_news:test:5941` **World** -> **Sports**: "Cricket: NZ suffer Franklin blow New Zealand bowler James Franklin misses the first Test against Australia with  injury."  
  "Cricket: NZ suffer Franklin blow" about a bowler missing "the first Test against Australia with injury" is Sports.
- [ ] `ag_news:test:1533` **World** -> **Sports**: "Collingwood anchors England (AFP) AFP - Paul Collingwood's unbeaten 80 took England to 299 for seven against Zimbabwe in their opening Champions Trophy Pool D match at Edgbaston here."  
  "Paul Collingwood's unbeaten 80 took England to 299 for seven against Zimbabwe" in the Champions Trophy is cricket, Sports.
- [ ] `ag_news:test:369` **World** -> **Sports**: "U.S. Softball Team Wins, Closes in on Gold ATHENS, Greece - Right now, the Americans aren't just a Dream Team - they're more like the Perfect Team. Lisa Fernandez pitched a three-hitter Sunday and Crystl Bustos drove in "  
  "Lisa Fernandez pitched a three-hitter" and "5-0 over Australia, putting them into the gold medal game" is Olympic softball, Sports.
- [ ] `ag_news:test:372` **World** -> **Sports**: "Men Set for Sizzling Duel in 100 Meters ATHENS, Greece - The preliminaries in the 100 meters were perhaps just a sample of what's to come Sunday, when a talented group of qualifiers - including Americans Shawn Crawford, "  
  "The preliminaries in the 100 meters" with sprinters Crawford, Gatlin and Greene at the Athens Games is athletics, Sports.
- [ ] `ag_news:test:3688` **World** -> **Sports**: "Ljubicic Downs Hanescu at Open De Moselle Top-seeded Ivan Ljubicic of Croatia beat Victor Hanescu of Romania 6-4, 6-4 Tuesday in the first round of the Open de Moselle."  
  "Ivan Ljubicic of Croatia beat Victor Hanescu of Romania 6-4, 6-4 ... in the first round of the Open de Moselle" is tennis, Sports.
- [ ] `ag_news:test:1617` **World** -> **Sports**: "At Last, Success on the Road for Lions The Detroit Lions went three full seasons without winning an away game, setting an NFL record for road futility. They ended that ignominious streak Sunday in their first opportunity"  
  "The Detroit Lions ... beating the Chicago Bears 20-16 at Soldier Field" ending an NFL road losing streak is Sports.
- [ ] `ag_news:test:3746` **World** -> **Sports**: "Football: Azerbaijan 0-1 England Michael Owen heads England's winner in the World Cup qualifier against Azerbaijan."  
  "Football: Azerbaijan 0-1 England Michael Owen heads England's winner in the World Cup qualifier" is Sports.
- [ ] `ag_news:test:3899` **World** -> **Sports**: "Warne takes six but India establish handy lead (Reuters) Reuters - World test wicket record holder Shane Warne grabbed six wickets as India established a handy 141-run first innings lead in the second test on Saturday."  
  "Shane Warne grabbed six wickets as India established a handy 141-run first innings lead in the second test" is cricket, Sports.
- [ ] `ag_news:test:3900` **World** -> **Sports**: "Rugby: Kiwis earn draw New Zealand hold Australia 16-16 in the first game of the 2004 Tri-Nations series."  
  "Rugby: Kiwis earn draw New Zealand hold Australia 16-16" in the Tri-Nations is Sports.
- [ ] `ag_news:test:4028` **World** -> **Business**: "Stocks Edge Higher As Oil Prices Retreat NEW YORK - A sharp drop in oil prices gave Wall Street a modest relief rally Monday, with stocks edging higher on news that oil production had soared during the month of September"  
  "A sharp drop in oil prices gave Wall Street a modest relief rally Monday, with stocks edging higher" is a market report, Business.
- [ ] `ag_news:test:4029` **World** -> **Sports**: "USC, Miami Top BCS Standings, Not Okla. Southern California took the top spot Monday in the season's first Bowl Championship Series standings, and surprisingly Miami is ahead of Oklahoma in a close race for the second sp"  
  "Southern California took the top spot Monday in the season's first Bowl Championship Series standings" is college football, Sports.
- [ ] `ag_news:test:3081` **World** -> **Business**: "Tokyo Stocks Finish 2.6 Percent Higher (AP) AP - Tokyo stocks finished sharply higher Monday, fueled by Wall Street's gains last week. The U.S. dollar was higher against the Japanese yen."  
  "Tokyo stocks finished sharply higher Monday, fueled by Wall Street's gains" and the dollar-yen move is a market report, Business.
- [ ] `ag_news:test:4302` **World** -> **Sports**: "Sri Lanka off to positive start Kumar Sangakkara's unbeaten fifty revives Sri Lanka's chances against Pakistan."  
  "Kumar Sangakkara's unbeaten fifty revives Sri Lanka's chances against Pakistan" is cricket, Sports.
- [ ] `ag_news:test:747` **World** -> **Sports**: "Argentina Beats U.S. Men's Basketball Team Argentina defeated the United States team of National Basketball Association stars 89-81 here Friday in the Olympic semi-finals, dethroning the three-time defending champions."  
  "Argentina defeated the United States team of National Basketball Association stars 89-81 ... in the Olympic semi-finals" is Sports.
- [ ] `ag_news:test:676` **World** -> **Sports**: "US edge out Brazil for gold The United States beat Brazil 2-1 in extra time to win the women's Olympic football tournament."  
  "The United States beat Brazil 2-1 in extra time to win the women's Olympic football tournament" is Sports.
- [ ] `ag_news:test:626` **World** -> **Sports**: "Dream Team Leads Spain 44-42 at Halftime ATHENS, Greece - As expected, the U.S. men's basketball team had its hands full in a quarterfinal game against Spain on Thursday..."  
  "the U.S. men's basketball team had its hands full in a quarterfinal game against Spain" is Olympic basketball, Sports.
- [ ] `ag_news:test:614` **World** -> **Sports**: "Pakistan down India to ensure top six finish (AFP) AFP - Pakistan defeated arch-rivals India 3-0 here to ensure they stand among the top six in the Olympic men's field hockey competition."  
  "Pakistan defeated arch-rivals India 3-0 ... in the Olympic men's field hockey competition" is Sports.
- [ ] `ag_news:test:4669` **World** -> **Sports**: "Henman Sails at the Swiss Indoors &lt;p&gt;&lt;/p&gt;&lt;p&gt; By Mark Ledsom&lt;/p&gt;&lt;p&gt; BASEL (Reuters) - Britain's world number four Tim Henmanwon his opening match at the Swiss Indoors tennis tournamentwith li"  
  "Tim Henman won his opening match at the Swiss Indoors tennis tournament ... beating Frenchman Antony Dupuis 6-3, 6-4" is Sports.
- [ ] `ag_news:test:4734` **World** -> **Sports**: "Australia establish 300-run lead in third India Test (AFP) AFP - Australia batted cautiously in their second innings to build a lead of 300 runs over India with nine wickets in hand in the third cricket Test here."  
  "Australia batted cautiously in their second innings to build a lead of 300 runs over India ... in the third cricket Test" is Sports.
- [ ] `ag_news:test:5892` **World** -> **Sports**: "We have to learn to be patient on Indian pitches: Smith (AFP) AFP - South African skipper Graeme Smith said his team had to learn to be patient on slow pitches if they hoped to do well in an upcoming two-Test series agai"  
  "South African skipper Graeme Smith said his team had to learn to be patient on slow pitches" before a two-Test cricket series is Sports.
- [ ] `ag_news:test:7077` **World** -> **Sports**: "Pakistan on back foot in four dayer (AFP) AFP - Pakistan was still struggling at lunch on the second day of their four-day tour match against Western Australia here despite claiming two wickets in the morning session."  
  "Pakistan was still struggling at lunch on the second day of their four-day tour match against Western Australia" is cricket, Sports.
- [ ] `ag_news:test:3661` **World** -> **Sports**: "Cricket: Tendulkar to miss test Sachin Tendulkar is almost certain to miss Thursday's second Test against Australia in Madras."  
  "Cricket: Tendulkar to miss test ... second Test against Australia in Madras" is Sports.
- [ ] `ag_news:test:3662` **World** -> **Business**: "Oil Prices, Earnings Send Stocks Lower NEW YORK - Investors sent stocks lower Tuesday as oil prices crossed another milestone, \$54 per barrel. Earnings reports from heavyweights Johnson   Johnson and Merrill Lynch   Co."  
  "Investors sent stocks lower Tuesday as oil prices crossed another milestone, $54 per barrel" with earnings from Johnson & Johnson and Merrill Lynch is a market report, Business.
- [ ] `ag_news:test:88` **World** -> **Sports**: "U.S. Misses Cut in Olympic 100 Free ATHENS, Greece - Top American sprinters Jason Lezak and Ian Crocker missed the cut in the Olympic 100-meter freestyle preliminaries Tuesday, a stunning blow for a country that had alwa"  
  "Jason Lezak and Ian Crocker missed the cut in the Olympic 100-meter freestyle preliminaries" is Olympic swimming, Sports.
- [ ] `ag_news:test:106` **World** -> **Business**: "Stocks Climb on Drop in Consumer Prices NEW YORK - Stocks rose for a second straight session Tuesday as a drop in consumer prices allowed investors to put aside worries about inflation, at least for the short term.    Wi"  
  "Stocks rose for a second straight session Tuesday as a drop in consumer prices" eased inflation worries is a market report, Business.
- [ ] `ag_news:test:1779` **World** -> **Business**: "Stocks Sink on Coke's Gloomy Forecast NEW YORK - Stocks headed lower Wednesday after beverage giant Coca-Cola Co. issued a gloomy forecast, and a lower-than-expected reading on industrial production for August threw the "  
  "Stocks headed lower Wednesday after beverage giant Coca-Cola Co. issued a gloomy forecast" plus industrial production data is Business.
- [ ] `ag_news:test:5127` **Sci/Tech** -> **World**: "Another homicide in Holland  It is a sad day.      In what seems to be another politically inspired homicide in Holland, Dutch filmmaker, and controversial columnist Theo van Gogh was brutally murdered in the streets of "  
  "Dutch filmmaker, and controversial columnist Theo van Gogh was brutally murdered in the streets of Amsterdam" is a politically inspired crime story, World, with nothing Sci/Tech about it.
- [ ] `ag_news:test:79` **World** -> **Sports**: "Live: Olympics day four Richard Faulds and Stephen Parry are going for gold for Great Britain on day four in Athens."  
  "Live: Olympics day four Richard Faulds and Stephen Parry are going for gold for Great Britain" is Olympic competition coverage, Sports.
- [ ] `ag_news:test:4027` **World** -> **Sports**: "Tennis: Davenport to play on Lindsay Davenport says she plans to play in the Australian Open next January."  
  "Tennis: Davenport to play on ... plans to play in the Australian Open next January" is Sports.
- [ ] `ag_news:test:3062` **World** -> **Business**: "Nikkei Opens Higher (Reuters) Reuters - The Nikkei average rose 1.37 percent at\the opening on Monday as a recovery in U.S. stocks encouraged\investors to seek bargains among lagging issues, including\Canon Inc. and othe"  
  "The Nikkei average rose 1.37 percent at the opening on Monday as a recovery in U.S. stocks encouraged investors" is a market report, Business.
- [ ] `ag_news:test:2205` **World** -> **Business**: "Stocks Close Higher on Brokerage Earnings NEW YORK - Stocks dashed higher Tuesday as investors welcomed strong earnings from financial services companies, upbeat economic data and some reassuring news from the Federal Re"  
  "Stocks dashed higher Tuesday as investors welcomed strong earnings from financial services companies" and the Fed rate rise is Business.
- [ ] `ag_news:test:584` **World** -> **Sports**: "Jones Advances in Long Jump; Johnson Out ATHENS, Greece - Marion Jones made her Athens debut in virtual anonymity, quietly advancing to the long jump final. Allen Johnson had the attention of everyone in the stadium, for"  
  "Marion Jones ... quietly advancing to the long jump final" at the Athens Olympics is athletics, Sports.
- [ ] `ag_news:test:1110` **Business** -> **World**: "EU foreign ministers hope to break deadlock over ASEM summit The European Union said Friday it  quot;hoped to reach a conclusion quot; at a meeting of foreign ministers on the participation of military-ruled Myanmar in a"  
  "EU foreign ministers hope to break deadlock" over "the participation of military-ruled Myanmar" in the ASEM summit is diplomacy, World, not Business.
- [ ] `ag_news:test:1197` **Business** -> **World**: "World briefs LONDON - A man wielding a machete and a knife attacked two security guards at the building housing the headquarters of the British domestic intelligence service MI5 on Friday, police said."  
  "A man wielding a machete and a knife attacked two security guards at ... MI5" is a crime story under a "World briefs" header, World.
- [ ] `ag_news:test:1213` **World** -> **Business**: "Tokyo Stocks Higher at Late Morning (AP) AP - Tokyo stocks rose moderately Monday morning on bargain hunting following Friday's losses. The U.S. dollar was up against the Japanese yen."  
  "Tokyo stocks rose moderately Monday morning on bargain hunting" and the dollar-yen move is a market report, Business.
- [ ] `ag_news:test:488` **Business** -> **World**: "Audit finds no fraud in Venezuelan recall vote CARACAS : An audit of last Sunday #39;s recall vote in Venezuela, which favored keeping President Hugo Chavez in office, found no evidence of fraud, as the opposition had ch"  
  "An audit of last Sunday's recall vote in Venezuela ... found no evidence of fraud" is election politics, World, not Business.
- [ ] `ag_news:test:1269` **Sci/Tech** -> **World**: "Philippines mourns dead in Russian school siege The Philippines Saturday expressed quot;deepest sympathy quot; to the families of the dead in the Russian school siege on Friday, in which 322 people were killed when Russi"  
  "The Philippines Saturday expressed 'deepest sympathy' to the families of the dead in the Russian school siege" is diplomacy and disaster, World, not Sci/Tech.
- [ ] `ag_news:test:5740` **World** -> **Business**: "Dow Jones Agrees to Buy MarketWatch in \$519 Million Deal Dow Jones   Company, the publisher of The Wall Street Journal, has agreed to buy MarketWatch, the parent company of the financial news Web site CBS MarketWatch, f"  
  "Dow Jones ... has agreed to buy MarketWatch ... for approximately $519 million" is a corporate acquisition by a newspaper publisher, Business.
- [ ] `ag_news:test:3453` **World** -> **Business**: "Lackluster Jobs Report Pushes Stocks Down NEW YORK - Investors pushed stocks lower Friday as a surprisingly lackluster job creation report deepened Wall Street's pessimism over the health of the economy. A solid earnings"  
  "Investors pushed stocks lower Friday as a surprisingly lackluster job creation report" plus GE earnings is a market report, Business.
- [ ] `ag_news:test:613` **World** -> **Sports**: "Rain threatens triangular final (AFP) AFP - Organisers were left banking on the Dutch weather to spare Saturday's final of the triangular cricket tournament after deciding against altering the fixture schedule in a bid t"  
  "Saturday's final of the triangular cricket tournament" threatened by rain before the ICC Champions Trophy is Sports.
- [ ] `ag_news:test:4650` **World** -> **Business**: "BHP Billiton, Alcoa sell Integris Metals for 359 million pounds (AFP) AFP - Anglo-Australian mining giant BHP Billiton and Alcoa, the world's largest aluminium producer, have agreed to sell their metal services joint ven"  
  "BHP Billiton and Alcoa ... have agreed to sell their metal services joint venture Integris Metals for 660 million dollars" is a corporate deal, Business.
- [ ] `ag_news:test:456` **Business** -> **World**: "Observers insist: no proof of fraud in Venezuelan referendum. Independent observers confirmed that the random auditing of results from the recall referendum (Sunday August 15) against Venezuelan president Hugo Chavez sho"  
  "Independent observers confirmed that the random auditing of results from the recall referendum ... against Venezuelan president Hugo Chavez show there are no indications of fraud" is politics, World.
- [ ] `ag_news:test:3563` **World** -> **Sports**: "Ken Caminiti, 1996 NL MVP, Dies at Age 41 NEW YORK - Ken Caminiti, the 1996 National League MVP who later admitted using steroids during his major league career, died Sunday. He was 41..."  
  "Ken Caminiti, the 1996 National League MVP ... died Sunday" is an athlete obituary, which the guidelines put under Sports.
- [ ] `ag_news:test:3570` **World** -> **Sports**: "Legendary all-rounder Miller dies Keith Miller, arguably Australia's greatest  all-rounder in Test cricket, has died in Melbourne aged 84."  
  "Keith Miller, arguably Australia's greatest all-rounder in Test cricket, has died" is an athlete obituary, Sports.
- [ ] `ag_news:test:348` **World** -> **Sports**: "Unknown Nesterenko Makes World Headlines (Reuters) Reuters - Belarus' Yuliya Nesterenko won the top\women's athletics gold medal at the Olympics on Saturday,\triumphing over a field stripped of many big names because of\"  
  "Yuliya Nesterenko won the top women's athletics gold medal at the Olympics ... to win the 100 meters" is Sports.
- [ ] `ag_news:test:336` **Business** -> **World**: "Chavez victory confirmed Caracas, Venezuela - The results of an audit support the official vote count showing that President Hugo Chavez won this month #39;s recall referendum in Venezuela, the head of the Organization o"  
  "The results of an audit support the official vote count showing that President Hugo Chavez won this month's recall referendum" is politics, World, not Business.
- [ ] `ag_news:test:120` **World** -> **Business**: "Oil prices bubble to record high The price of oil has continued its sharp rise overnight, closing at a record high. The main contract in New York, light sweet crude for delivery next month, has closed at a record \$US46."  
  "light sweet crude for delivery next month, has closed at a record $US46.75 a barrel" is a commodity price report, Business.
- [ ] `ag_news:test:6089` **World** -> **Sports**: "Football: Brazil legend's UK debut Brazil football great Socrates is set to make his debut for non-league Garforth Town on Saturday."  
  "Brazil football great Socrates is set to make his debut for non-league Garforth Town" is Sports.
- [ ] `ag_news:test:2833` **Sci/Tech** -> **World**: "Man arrested for fatally stabbing elderly parents SAITAMA -- A middle-aged man who fatally stabbed his parents has been arrested, police said. Hideo Nakajima, an unemployed man from Soka, Saitama Prefecture, apparently c"  
  "A middle-aged man who fatally stabbed his parents has been arrested, police said" is a crime story, World, not Sci/Tech.
- [ ] `ag_news:test:5129` **Business** -> **Sci/Tech**: "Product Previews palmOneUpgrades Treo With Faster Chip, Better Display\With more than 600,000 units shipped, the Treo 600 is one of the big smartphone success stories. Last week, palmOne introduced the follow-on Treo 650"  
  A product preview of the Treo 650 with its "320-by-320-pixel TFT screen", "32MB of flash memory, and a faster 312MHz, Intel XScale processor" is hardware, Sci/Tech.
- [ ] `ag_news:test:5142` **World** -> **Business**: "Japan Airlines Sees Profit on Int'l Travel (AP) AP - Japan Airlines Corp. said Friday that it returned to profitability in first half of the fiscal year as international travel picked up from a decline a year ago caused "  
  "Japan Airlines Corp. said Friday that it returned to profitability in first half of the fiscal year" is an earnings story, Business.
- [ ] `ag_news:test:4137` **World** -> **Sports**: "F1: British Grand Prix ruled out Jackie Stewart rejects Bernie Ecclestone's claims that the British Grand Prix is dead."  
  "F1: British Grand Prix ruled out Jackie Stewart rejects Bernie Ecclestone's claims" is motor racing, Sports.
- [ ] `ag_news:test:2126` **Sci/Tech** -> **World**: "Bush Scraps Most U.S. Sanctions on Libya (Reuters) Reuters - President Bush on Monday formally\ended the U.S. trade embargo on Libya to reward it for giving\up weapons of mass destruction but left in place U.S.\terrorism"  
  "President Bush on Monday formally ended the U.S. trade embargo on Libya to reward it for giving up weapons of mass destruction" is diplomacy and government, World, not Sci/Tech.
- [ ] `ag_news:test:2574` **Business** -> **Sci/Tech**: "Adobe updates RAW plug-in with digital negative format Adobe has updated Photoshop #39;s support for digital cameras #39; RAW image formats. The new plug-in adds to the number of camera models supported and includes a ut"  
  "Adobe has updated Photoshop's support for digital cameras' RAW image formats" with a DNG conversion utility is software news, Sci/Tech.
- [ ] `ag_news:test:408` **Business** -> **World**: "Chavez rejects CD as opposition Venezuela #39;s President Hugo Chavez has announced that he will no longer recognize the Democratic Coordination or CD as the opposition coalition."  
  "President Hugo Chavez has announced that he will no longer recognize the Democratic Coordination or CD as the opposition coalition" is politics, World.
- [ ] `ag_news:test:1494` **World** -> **Sci/Tech**: "Telescope snaps distant 'planet' The first direct image of a planet circling another star may have been obtained by a US-European team of astronomers."  
  "The first direct image of a planet circling another star may have been obtained by ... astronomers" is space science, Sci/Tech.
- [ ] `ag_news:test:6006` **Business** -> **World**: "Russia #39;s Putin Defends Reforms, Worries About Clans Russian President Vladimir Putin said on Thursday he had no plans to grab more power or change the constitution when reforming Russia #39;s government structure."  
  "Vladimir Putin said on Thursday he had no plans to grab more power or change the constitution" is government and politics, World, not Business.
- [ ] `ag_news:test:2738` **World** -> **Sports**: "Official: MLB to Move Expos to Washington WASHINGTON - Major League Baseball will announce Wednesday that Washington will be the new home of the Montreal Expos, bringing the national pastime back to the nation's capital "  
  "Major League Baseball will announce Wednesday that Washington will be the new home of the Montreal Expos" is sports business, which the guidelines put under Sports.
- [ ] `ag_news:test:7228` **Business** -> **World**: "Indonesian diplomats asked to help improve RI #39;s bad image JAKARTA (Antara): President Susilo Yudhoyono asked Indonesian diplomats on Monday to help the government improve Indonesia #39;s bad image."  
  "President Susilo Yudhoyono asked Indonesian diplomats on Monday to help the government improve Indonesia's bad image" is government and diplomacy, World.
- [ ] `ag_news:test:7238` **World** -> **Sports**: "Bangladesh boss slams detractors Bangladesh's coach says they still deserve Test status after their 30th defeat, to India."  
  "Bangladesh's coach says they still deserve Test status after their 30th defeat, to India" is cricket, Sports.
- [ ] `ag_news:test:6100` **Business** -> **Sci/Tech**: "Lazarus-like virus hits computers A new computer virus is catching people out by coming back from the dead."  
  "A new computer virus is catching people out by coming back from the dead" is computer security, Sci/Tech.
- [ ] `ag_news:test:24` **Sci/Tech** -> **Business**: "Rivals Try to Turn Tables on Charles Schwab By MICHAEL LIEDTKE     SAN FRANCISCO (AP) -- With its low prices and iconoclastic attitude, discount stock broker Charles Schwab Corp. (SCH) represented an annoying stone in Wa"  
  "discount stock broker Charles Schwab Corp. (SCH) represented an annoying stone in Wall Street's wing-tipped shoes" is a brokerage industry story, Business.
- [ ] `ag_news:test:2944` **World** -> **Business**: "Stocks Climb on Strong Economic Data NEW YORK - Newly optimistic investors sent stocks sharply higher Friday, propelling the Dow Jones industrials up more than 100 points, after economic data showed strength in manufactu"  
  "investors sent stocks sharply higher Friday, propelling the Dow Jones industrials up more than 100 points, after economic data showed strength" is a market report, Business.
- [ ] `ag_news:test:5128` **World** -> **Sports**: "Argentina Basketball Coach Magnano Quits Ruben Magnano, who coached Argentina to the Olympic basketball gold medal in Athens, resigned Thursday to accept a coaching job in Italy."  
  "Ruben Magnano, who coached Argentina to the Olympic basketball gold medal in Athens, resigned Thursday to accept a coaching job in Italy" is Sports.
- [ ] `ag_news:test:56` **World** -> **Business**: "India's Tata expands regional footprint via NatSteel buyout (AFP) AFP - India's Tata Iron and Steel Company Ltd. took a strategic step to expand its Asian footprint with the announcement it will buy the Asia-Pacific stee"  
  "Tata Iron and Steel Company Ltd. ... will buy the Asia-Pacific steel operations of Singapore's NatSteel Ltd." is a corporate acquisition, Business.
- [ ] `ag_news:test:7539` **World** -> **Sci/Tech**: "Mars water tops science honours The discovery that salty, acidic water once flowed across the surface of Mars has topped a list of the 10 key scientific advances of 2004."  
  "The discovery that salty, acidic water once flowed across the surface of Mars has topped a list of the 10 key scientific advances of 2004" is science, Sci/Tech.
- [ ] `ag_news:test:4102` **World** -> **Sci/Tech**: "Ancient fungus 'revived' in lab Fungus from a deep-sea sediment core that is hundreds of thousands of years old will grow when placed in culture, scientists discover."  
  "Fungus from a deep-sea sediment core that is hundreds of thousands of years old will grow when placed in culture, scientists discover" is science, Sci/Tech.
- [ ] `ag_news:test:582` **Business** -> **Sci/Tech**: "MOM 2005 Released to Manufacturing Microsoft on Wednesday announced the release to manufacturing of Microsoft Operations Manager (MOM) 2005 and MOM 2005 Workgroup Edition, a new edition that the company previously called"  
  "Microsoft on Wednesday announced the release to manufacturing of Microsoft Operations Manager (MOM) 2005" is a software release, Sci/Tech.
- [ ] `ag_news:test:5597` **World** -> **Business**: "BSkyB sees profits rise after strong subscriber growth (AFP) AFP - British satellite broadcaster BSkyB said profit rose by 16 percent in the first quarter as the group enjoyed strong subscriber growth in the run-up to th"  
  "British satellite broadcaster BSkyB said profit rose by 16 percent in the first quarter" on subscriber growth is an earnings story, Business, not World.
- [ ] `ag_news:test:6766` **World** -> **Business**: "India's low-cost airline eyes business travel (AFP) AFP - India's pioneer low-cost carrier Air Deccan plans to raise 50 million dollars in private equity by shedding a 26 percent stake and also aims to enter the corporat"  
  "Air Deccan plans to raise 50 million dollars in private equity by shedding a 26 percent stake" is company finance, Business.
- [ ] `ag_news:test:4530` **World** -> **Business**: "Ispat, LNM, ISG merge to form world's largest steelmaker (AFP) AFP - Dutch steel groups Ispat International and LNM Holdings, both run by Indian businessman Lakshmi Mittal, said they had agreed to merge with US Internati"  
  "Ispat International and LNM Holdings ... agreed to merge with US International Steel Group to form the world's largest steelmaker" is a merger, Business.
- [ ] `ag_news:test:1364` **Sci/Tech** -> **Business**: "Hyundai signs deal for China truck plant Hyundai Motor Co. said yesterday that it has signed an agreement with a Chinese company, Jianghuai Automobile Corp., to build a commercial vehicle and engine plant in China #39;s "  
  "Hyundai Motor Co. ... has signed an agreement with a Chinese company ... to build a commercial vehicle and engine plant" is a company deal, Business, not Sci/Tech.
- [ ] `ag_news:test:2752` **Business** -> **Sci/Tech**: "BlueGene sneaks past Earth Simulator The Earth Simulator, an NEC supercomputer, is surpassed, at last. IBM announced yesterday that its Blue Gene/L supercomputer had achieved a sustained performance of 36."  
  "IBM announced yesterday that its Blue Gene/L supercomputer had achieved a sustained performance" surpassing NEC's Earth Simulator is hardware, Sci/Tech.
- [ ] `ag_news:test:2758` **World** -> **Sports**: "Cricket: Dubai global academy The International Cricket Council are to open a global cricket academy designed to improve standards of lesser nations."  
  "The International Cricket Council are to open a global cricket academy designed to improve standards of lesser nations" is Sports.
- [ ] `ag_news:test:1668` **Business** -> **World**: "EU increases pressure for rights in Myanmar EU foreign ministers agreed Monday to tighten sanctions against Myanmar if it does not improve its human rights record by Oct. 8, when an EU meeting with Asian countries starts"  
  "EU foreign ministers agreed Monday to tighten sanctions against Myanmar if it does not improve its human rights record" is diplomacy, World, not Business.
- [ ] `ag_news:test:3856` **World** -> **Business**: "September Retail Sales Up by 1.5 Percent WASHINGTON - Shoppers got their buying groove back last month, propelling sales at the nation's retailers by a strong 1.5 percent. It was the best showing since March..."  
  "propelling sales at the nation's retailers by a strong 1.5 percent" is an economic data story, Business.
- [ ] `ag_news:test:4000` **Business** -> **Sci/Tech**: "Google puts desktop search privacy up front Google has announced a new desktop search application that enables users to search their e-mail, files, web history, and chats. Perhaps learning from previous mistakes, Google "  
  "Google has announced a new desktop search application that enables users to search their e-mail, files, web history, and chats" is software, Sci/Tech.
- [ ] `ag_news:test:7505` **World** -> **Sci/Tech**: "Boys 'cured' with gene therapy  Gene therapy can cure children born with a condition that knocks out their natural defences against infection, mounting evidence shows."  
  "Gene therapy can cure children born with a condition that knocks out their natural defences against infection" is medicine, Sci/Tech.
- [ ] `ag_news:test:892` **Business** -> **Sci/Tech**: "Intel in new chip breakthrough Intel creates a more powerful memory chip without increasing its size, confounding the firm's critics."  
  "Intel creates a more powerful memory chip without increasing its size" is a hardware breakthrough, Sci/Tech.
- [ ] `ag_news:test:4275` **Business** -> **World**: "Erdogan Believes European Council #39;s Decision Will Be A Milestone PARIS - Turkish PM Recep Tayyip Erdogan expressed belief on Thursday that the decision that the European Council would make on December 17th (on whethe"  
  "Turkish PM Recep Tayyip Erdogan expressed belief ... the decision that the European Council would make ... on whether and when to open negotiations with Turkey" is diplomacy, World.
- [ ] `ag_news:test:2234` **Business** -> **Sci/Tech**: "Spread of GM grass raises fears of crossbreeding Pollen from a genetically modified grass was found 21 kilometres from where it was planted, scientists reported in a study published Tuesday, raising fears of transgenic c"  
  "Pollen from a genetically modified grass was found 21 kilometres from where it was planted, scientists reported in a study" is science and environment, Sci/Tech.
- [ ] `ag_news:test:4359` **Business** -> **Sci/Tech**: "Google #39;s New PC Search Tool Poses Risks NEW YORK Oct. 18, 2004 - People who use public or workplace computers for e-mail, instant messaging and Web searching have a new privacy risk to worry about: Google #39;s free "  
  "a new privacy risk to worry about: Google's free new tool that indexes a PC's contents" is software and security, Sci/Tech.
- [ ] `ag_news:test:727` **World** -> **Business**: "Japanese Utility Plans IPO in October (AP) AP - Electric Power Development Co., a former state-run utility, said Friday it is planning an initial public offering on the Tokyo Stock Exchange in October, a deal that could "  
  "Electric Power Development Co. ... is planning an initial public offering on the Tokyo Stock Exchange" is a stock listing story, Business.
- [ ] `ag_news:test:1373` **World** -> **Business**: "Stocks Drop After Greenspan Testimony NEW YORK - Investors were unmoved by Federal Reserve Chairman Alan Greenspan's improved assessment of the economy, with stocks falling narrowly Wednesday in light trading.    While G"  
  "stocks falling narrowly Wednesday in light trading" after Greenspan's testimony on the economy and energy prices is a market report, Business.
- [ ] `ag_news:test:5916` **World** -> **Business**: "ConocoPhillips boosts LUKoil stake to 10 percent (AFP) AFP - US oil major ConocoPhillips has boosted its stake in Russia's second-largest oil producer LUKoil to 10 percent, giving Conoco at least one representative on LU"  
  "US oil major ConocoPhillips has boosted its stake in Russia's second-largest oil producer LUKoil to 10 percent" is a corporate investment, Business.
- [ ] `ag_news:test:316` **World** -> **Business**: "Crude Price Spike May Send Gas Higher (AP) AP - Amid soaring crude oil prices, gasoline costs have been dropping. But don't expect that to last, economists say."  
  "Amid soaring crude oil prices, gasoline costs have been dropping. But don't expect that to last, economists say" is a prices story, Business.
- [ ] `ag_news:test:1098` **Sci/Tech** -> **Sports**: "The Bahamas - the real medal winner of the Athens Olympics A different way of calculating the medal standings brings some interesting results."  
  "the real medal winner of the Athens Olympics A different way of calculating the medal standings" is Olympic sports coverage, Sports, not Sci/Tech.
- [ ] `ag_news:test:2828` **Business** -> **Sci/Tech**: "IBM Claims Its BlueGene Supercomputer Is the Fastest IBM Corp. on Wednesday said it has developed the world #39;s fastest computer - a 16,000-processor version of its BlueGene/L supercomputer."  
  "IBM Corp. ... has developed the world's fastest computer - a 16,000-processor version of its BlueGene/L supercomputer" is hardware, Sci/Tech.
- [ ] `ag_news:test:248` **Sci/Tech** -> **Business**: "Caterpillar snaps up another remanufacturer of engines PEORIA - Caterpillar Inc. said Wednesday it will acquire a South Carolina remanufacturer of engines and automatic transmissions, increasing its US employment base by"  
  "Caterpillar Inc. said Wednesday it will acquire a South Carolina remanufacturer of engines and automatic transmissions" is a corporate acquisition, Business, not Sci/Tech.
- [ ] `ag_news:test:6592` **Business** -> **Sci/Tech**: "Sony, IBM, Toshiba Give Details of 'Cell' Chip (Reuters) Reuters - IBM , Sony Corp. (6758.T) and\Toshiba Corp. (6502.T) on Monday revealed their plans for the\powerful new "Cell" processor the three are jointly producing"  
  "revealed their plans for the powerful new 'Cell' processor ... to run next-generation computers, game consoles and televisions" is hardware, Sci/Tech.
- [ ] `ag_news:test:6640` **World** -> **Business**: "Renault unveils investment plan for Asian hub in South Korea (AFP) AFP - French auto giant Renault SA said it will invest some 570 million dollars in South Korea over the next three years as part of its global strategy t"  
  "Renault SA said it will invest some 570 million dollars in South Korea over the next three years" is a corporate investment story, Business.
- [ ] `ag_news:test:4396` **World** -> **Business**: "Revolving Door  &lt;em&gt; IN&lt;/em&gt;&lt;br&gt;   Aylwin B. Lewis,  president of Yum Brands, as chief executive of Kmart."  
  A "Revolving Door" item naming "Aylwin B. Lewis, president of Yum Brands, as chief executive of Kmart" is an executive appointment, Business.
- [ ] `ag_news:test:2333` **Business** -> **Sci/Tech**: "Rumours surround Google browser The search giant Google is rumoured to be working on its own web browser."  
  "Google is rumoured to be working on its own web browser" is software and internet news, Sci/Tech.
- [ ] `ag_news:test:2491` **World** -> **Sci/Tech**: "Men, Women More Different Than Thought CHICAGO - Beyond the tired cliches and sperm-and-egg basics taught in grade school science class, researchers are discovering that men and women are even more different than anyone "  
  "researchers are discovering that men and women are even more different" with "heart disease and lung cancer are influenced by gender" is medical science, Sci/Tech.
- [ ] `ag_news:test:5886` **World** -> **Business**: "Producer Price Surge Fuels Inflation Fears Producer prices surged 1.7 percent in October, their sharpest monthly increase in nearly 15 years."  
  "Producer prices surged 1.7 percent in October, their sharpest monthly increase in nearly 15 years" is economic data, Business.
- [ ] `ag_news:test:2686` **World** -> **Business**: "Consumer Confidence Dips in September NEW YORK - Job worries helped push consumer confidence down in September for the second consecutive month, a New York-based private research group said Tuesday.    The Consumer Confi"  
  "The Consumer Confidence Index fell 1.9 points to 96.8" per The Conference Board is economic data, Business.
- [ ] `ag_news:test:3672` **Business** -> **Sci/Tech**: "Rumors Suggest Photo Ability To Be Added to iPod  quot;Apple has invested heavily in technology to edit pictures. Not having a portable device to show them seemed an obvious oversight that would be corrected once the pri"  
  "Rumors Suggest Photo Ability To Be Added to iPod" with talk of displays and picture-editing technology is a consumer hardware story, Sci/Tech.
- [ ] `ag_news:test:3775` **Sci/Tech** -> **Business**: "Bourses set for losses after Wall St falls (FT.com) FT.com - European equity markets were poised for opening losses on Thursday following a weak session on Wall Street overnight, while caution was likely ahead of results"  
  "European equity markets were poised for opening losses on Thursday following a weak session on Wall Street" is a market report, Business, even with Nokia results mentioned.
- [ ] `ag_news:test:4097` **Sci/Tech** -> **Business**: "Greenspan: Debt, home prices not dangerous The record level of debt carried by American households and soaring home prices do not appear to represent serious threats to the US economy, Federal Reserve Chairman Alan Green"  
  "The record level of debt carried by American households and soaring home prices do not appear to represent serious threats to the US economy, Federal Reserve Chairman Alan Greenspan said" is economics, Business.
- [ ] `ag_news:test:5285` **Business** -> **Sci/Tech**: "Study raises stent doubts Heart patients aren #39;t more likely to live long term after getting the artery-opening tubes called stents, according to a study released yesterday by researchers at Duke University."  
  "Heart patients aren't more likely to live long term after getting the artery-opening tubes called stents, according to a study" is medicine, Sci/Tech.
- [ ] `ag_news:test:196` **World** -> **Business**: "Stock Prices Climb Ahead of Google IPO NEW YORK - Investors shrugged off rising crude futures Wednesday to capture well-priced shares, sending the Nasdaq composite index up 1.6 percent ahead of Google Inc.'s much-anticip"  
  "sending the Nasdaq composite index up 1.6 percent ahead of Google Inc.'s much-anticipated initial public offering" with Dow figures is a market report, Business.
- [ ] `ag_news:test:3970` **Business** -> **Sci/Tech**: "Wi-Fi successor is called high-speed hype -- for now SAN FRANCISCO -- At virtually every turn, Intel Corp. executives are heaping praise on an emerging long-range wireless technology known as WiMAX, which can blanket ent"  
  "an emerging long-range wireless technology known as WiMAX, which can blanket entire cities with high-speed Internet access" is telecoms technology, Sci/Tech.
- [ ] `ag_news:test:6500` **Sci/Tech** -> **World**: "The Shockwaves of Sumatra The Indian Ocean earthquake of December 2004 produced     a shockwave that created tsunamis all across the Indian Ocean. The tsunamis hammered nearby Indonesia and struck as far as     the coast"  
  "The tsunamis hammered nearby Indonesia ... The death toll has climbed over 100,000" and "social shockwaves" is a disaster story, World, not Sci/Tech.
- [ ] `ag_news:test:2613` **World** -> **Business**: "Embattled Mortgage Giant Agrees to Meet New Standards Fannie Mae agreed to keep more cash on hand while it corrects accounting problems, a U.S. regulator said."  
  "Fannie Mae agreed to keep more cash on hand while it corrects accounting problems, a U.S. regulator said" is company and finance news, Business.
- [ ] `ag_news:test:7239` **World** -> **Sci/Tech**: "Week's delay for Delta launcher Boeing's new heavy-lift Delta 4 rocket must wait a further week before making its maiden flight."  
  "Boeing's new heavy-lift Delta 4 rocket must wait a further week before making its maiden flight" is space, Sci/Tech.
- [ ] `ag_news:test:5067` **Business** -> **World**: "Quick end to US election crucial US President George W. Bush is on the verge of a re-election victory, but Democratic challenger John Kerry is not conceding defeat, at least not now."  
  "US President George W. Bush is on the verge of a re-election victory, but Democratic challenger John Kerry is not conceding" is politics, World, not Business.
- [ ] `ag_news:test:1051` **Business** -> **Sci/Tech**: "Software Service Aims to Outfox Caller ID A new computerized service enables customers to create phony outbound phone numbers in order to mask their telephone identities."  
  "A new computerized service enables customers to create phony outbound phone numbers in order to mask their telephone identities" is telecoms and software, Sci/Tech.
- [ ] `ag_news:test:3581` **World** -> **Business**: "Oil Surges to New Intraday High in Europe (AP) AP - The price of crude oil surged to a new intraday high of US #36;53.42 in European trade Monday, despite assurances from Middle East oil producers that they were committe"  
  "The price of crude oil surged to a new intraday high of US$53.42 in European trade" is a commodity price report, Business.
- [ ] `ag_news:test:1691` **World** -> **Business**: "German investor confidence slumped in September BERLIN - German investor confidence dropped sharply in September, a key economic indicator released Tuesday showed amid concerns about the impact of high oil prices on cons"  
  "German investor confidence dropped sharply in September, a key economic indicator released Tuesday showed" is economic data, Business.
- [ ] `ag_news:test:3675` **Sci/Tech** -> **Business**: "DreamWorks Animation IPO Set at 29M Shares Underwriters for DreamWorks Animation SKG Inc., producer of the blockbuster "Shrek" movies, Tuesday set the terms of the company's pending initial public offering at 29 million "  
  "Underwriters for DreamWorks Animation SKG Inc. ... set the terms of the company's pending initial public offering at 29 million common shares" is an IPO story, Business, not Sci/Tech.
- [ ] `ag_news:test:5152` **Sci/Tech** -> **World**: "Hope Fades for Saving 2 Boys Stuck in Mexico Cave (Reuters) Reuters - Hopes of rescuing two small boys\trapped for five days in a jungle cave faded fast on Friday\after contact was lost with the brothers and as the caver"  
  "Hopes of rescuing two small boys trapped for five days in a jungle cave faded fast" is a human-interest rescue story, World, not Sci/Tech.
- [ ] `ag_news:test:5295` **Business** -> **World**: "PM welcomes EU partnership Prime Minister Manmohan Singh arrived in the Hague last night to participate in the India-European summit.  quot;In recognition of Indias growing stature and influence, the EU has proposed a st"  
  "Prime Minister Manmohan Singh arrived in the Hague last night to participate in the India-European summit" and "the EU has proposed a strategic partnership with India" is diplomacy, World.
- [ ] `ag_news:test:887` **Business** -> **Sci/Tech**: "On TV -- from the Internet  SAN MATEO, Calif. -- The promise of Internet-based video has long been hamstrung by copyright and piracy worries, slow dial-up connections, technical challenges, and consumer disdain for watch"  
  "The promise of Internet-based video has long been hamstrung by copyright and piracy worries, slow dial-up connections, technical challenges" is internet technology, Sci/Tech.
- [ ] `ag_news:test:806` **Business** -> **Sci/Tech**: "Health Highlights: Aug. 28, 2004 A new drug that fights a form of age-related macular degeneration (AMD), a leading cause of blindness in the elderly, won applause if not approval from a panel of advisors to the US Food "  
  "Health Highlights ... A new drug that fights a form of age-related macular degeneration ... won applause if not approval from a panel of advisors to the US Food and Drug Administration" is medicine, Sci/Tech.
- [ ] `ag_news:test:2591` **World** -> **Sports**: "Sports Court Hears Hamm Gold Medal Appeal LAUSANNE, Switzerland - Paul Hamm appeared before the sports world's highest court Monday to argue why he should he keep his Olympic gymnastics gold medal.    The Court of Arbitr"  
  "Paul Hamm appeared before the sports world's highest court Monday to argue why he should he keep his Olympic gymnastics gold medal" is a sports dispute, Sports.
- [ ] `ag_news:test:355` **World** -> **Sports**: "Greek weightlifter awaits verdict Greek weightlifter Leonidas Sampanis will find out on Sunday if he is to be stripped of his medal."  
  "Greek weightlifter Leonidas Sampanis will find out on Sunday if he is to be stripped of his medal" is Olympic doping news, Sports.
- [ ] `ag_news:test:2173` **World** -> **Sports**: "India seeks new TV bids The Indian Board re-opens the bidding for TV rights after Australian threaten to cancel their tour."  
  "The Indian Board re-opens the bidding for TV rights after Australians threaten to cancel their tour" is cricket sports business, Sports.
- [ ] `ag_news:test:6276` **Business** -> **Sci/Tech**: "Federal CISOs Rank Patch Management As Biggest Obstacle Survey by Intelligent Decisions indicates that patch management leaves less time for chief information security officers to work on improving overall security."  
  "patch management leaves less time for chief information security officers to work on improving overall security" is IT security, Sci/Tech.
- [ ] `ag_news:test:1976` **World** -> **Sports**: "Show lights up Paralympics The XII Paralympics begins in Athens, after a spectacular opening ceremony."  
  "The XII Paralympics begins in Athens, after a spectacular opening ceremony" is Sports.
- [ ] `ag_news:test:3186` **World** -> **Sports**: "Tennis: Night final for Aus Open The centenary Australian Open will be the first Grand Slam event to stage its final at night."  
  "Tennis: Night final for Aus Open The centenary Australian Open will be the first Grand Slam event to stage its final at night" is Sports.
- [ ] `ag_news:test:719` **World** -> **Business**: "US economic growth slips to 2.8 Annual US economic growth fell to 2.8 in the second quarter of 2004, marking a slowdown from the 3 estimated a month ago."  
  "Annual US economic growth fell to 2.8 in the second quarter of 2004, marking a slowdown" is economic data, Business.
- [ ] `ag_news:test:1296` **Business** -> **World**: "Israel to close Erez industrial zone before March Israel would start liquidating the Erez industrial zone in the northern Gaza Strip before launching the first stage of the disengagement plan in March 2005,local newspape"  
  "Israel would start liquidating the Erez industrial zone in the northern Gaza Strip before launching the first stage of the disengagement plan" is Middle East politics, World, not Business.
- [ ] `ag_news:test:1658` **World** -> **Sci/Tech**: "FDA Approves Lens Implant to Sharpen Sight WASHINGTON - There's a new option for people who suffer from extreme nearsightedness, whose world loses its crisp edge just a few inches from their noses. The first implantable "  
  "The first implantable lens for nearsightedness was approved Monday by the Food and Drug Administration" is medicine, Sci/Tech.
- [ ] `ag_news:test:6093` **World** -> **Sports**: "Football: Spanish FA apologises The Spanish FA apologises to its English counterparts following racist chanting."  
  "Football: Spanish FA apologises The Spanish FA apologises to its English counterparts following racist chanting" is football governance, Sports.
- [ ] `ag_news:test:2400` **World** -> **Sci/Tech**: "Dogs said to smell cancer signs  LONDON -- It has long been suspected that man's best friend has a special ability to sense when something is wrong with us. Now, the first experiment to verify that scientifically has dem"  
  "the first experiment to verify that scientifically has demonstrated that dogs are able to smell cancer" is science and medicine, Sci/Tech.
- [ ] `ag_news:test:3384` **World** -> **Business**: "Employment Picture Expected to Improve NEW YORK - A rash of job cuts - more than 10,000 layoffs just this week from a handful of companies - has created some gloom on the jobs front. But Friday's release of jobs data for"  
  "Friday's release of jobs data for September was expected to show a steady unemployment rate" with layoffs and Wachovia estimates is economic news, Business.
- [ ] `ag_news:test:4580` **Business** -> **Sci/Tech**: "FaceTime, IMlogic Back Live Communications Server 2005 Hard on the heels of Microsoft announcing that it #39;s taken Live Communications Server 2005 gold, instant messaging management software vendors IMlogic and FaceTim"  
  "instant messaging management software vendors IMlogic and FaceTime on Tuesday both touted their support for" Microsoft's Live Communications Server 2005 is software, Sci/Tech.
- [ ] `ag_news:test:6760` **Sci/Tech** -> **Business**: "Panera Hopes 'Chilling Out' Brews Sales (AP) AP - Bakery cafe chain Panera Bread Co. hopes its customers will stick around a little longer  #151; grab a bite to eat, buy another cup of coffee, try the Wi-Fi. In other wor"  
  "Bakery cafe chain Panera Bread Co. hopes its customers will stick around a little longer ... buy another cup of coffee" is a retailer's sales strategy, Business; the passing Wi-Fi mention does not make it Sci/Tech.
- [ ] `ag_news:test:2566` **Business** -> **World**: "A wandering Congress trips over the US Constitution That is the one-word message of advice that citizens wanted to send to members of Congress at the end of last week. Both the House of Representatives and the Senate loo"  
  "Both the House of Representatives and the Senate looked as if they are having trouble" with the Constitution is US politics, World, not Business.
- [ ] `ag_news:test:3882` **World** -> **Business**: "For Many Airline Pilots, the Thrill Is Gone While pilots still feel in command in the air, they increasingly are feeling slighted on the ground, as airlines extract salary and benefits concessions from them."  
  "airlines extract salary and benefits concessions from" pilots is a labour and industry story, Business.
- [ ] `ag_news:test:2017` **Business** -> **World**: "Florida, Alabama pick up the pieces after Ivan People in Florida and Alabama have started to clean up after hurricane Ivan - the third such pummelling for Florida alone in just five weeks."  
  "People in Florida and Alabama have started to clean up after hurricane Ivan" is a disaster story, World, not Business.
- [ ] `ag_news:test:2236` **World** -> **Sci/Tech**: "Walking link to low dementia risk Walking may protect the elderly from developing dementia, research suggests."  
  "Walking may protect the elderly from developing dementia, research suggests" is medical research, Sci/Tech.
- [ ] `ag_news:test:677` **World** -> **Sci/Tech**: "Breast scans 'fail' in some women Some women with breast cancer are less likely to have their tumours picked up by scans, say experts."  
  "Some women with breast cancer are less likely to have their tumours picked up by scans, say experts" is medicine, Sci/Tech.
- [ ] `ag_news:test:3953` **Sci/Tech** -> **Sports**: "Toughest athlete is female and unknown You probably haven't heard about one of the toughest endurance sports around: the deca-ironman. That's 38 km swimming, immediately followed by an 1800 km bicycle ride and a 420 km r"  
  "one of the toughest endurance sports around: the deca-ironman" with a world record of "about 187 hours" is Sports, not Sci/Tech.
- [ ] `ag_news:test:6325` **Sci/Tech** -> **World**: "JFK killing fades in intensity WASHINGTON: The 41st anniversary of President John F Kennedy #39;s assassination passed on November 22 - a lot more quietly than earlier ones."  
  "The 41st anniversary of President John F Kennedy's assassination passed on November 22" is politics and history, World, not Sci/Tech.
- [ ] `ag_news:test:877` **Business** -> **Sci/Tech**: "For Now, Unwired Means Unlisted. That May Change. In October, most major cellphone carriers plan to start compiling a publicly accessible listing of wireless phone numbers."  
  "most major cellphone carriers plan to start compiling a publicly accessible listing of wireless phone numbers" is a telecoms story, which the guidelines put under Sci/Tech.
- [ ] `ag_news:test:3493` **World** -> **Business**: "Alstom to sign 1 billion Euro in contracts with China (AFP) AFP - The French Group Alstom Saturday will sign contracts worth up to 1 billion Euros (1.23 billion dollars) in China for the delivery of trains and locomotive"  
  "Alstom Saturday will sign contracts worth up to 1 billion Euros ... in China for the delivery of trains and locomotives" is a corporate contract, Business.
- [ ] `ag_news:test:2247` **World** -> **Business**: "Asia to outperform this year, lower growth seen in 2005: ADB (AFP) AFP - Developing Asia is set to outperform this year with higher-than-expected growth of 7.0 percent despite high oil prices but it will slow in 2005 in "  
  "Developing Asia is set to outperform this year with higher-than-expected growth of 7.0 percent ... the Asian Development Bank (ADB) said" is economics, Business.
- [ ] `ag_news:test:1317` **Sports** -> **World**: "Florida deaths blamed on Hurricane Frances State and local officials Tuesday said nine people have died in Florida because of Hurricane Frances. The following describes those deaths: - A 15-year-old grandson and a former"  
  "nine people have died in Florida because of Hurricane Frances" is a disaster story, World, and nothing in it is Sports.
- [ ] `ag_news:test:1447` **Sci/Tech** -> **World**: "Florida Starts To Recover in the Wake of Hurricane Frances President Bush will travel to Florida Wednesday to survey damage from Hurricane Frances. He sent a letter to Congress asking for \$2 billion to help with recover"  
  "President Bush will travel to Florida Wednesday to survey damage from Hurricane Frances" and asks Congress for "$2 billion to help with recovery" is disaster and government, World, not Sci/Tech.
- [ ] `ag_news:test:3762` **World** -> **Sci/Tech**: "Russian rocket carrying Russian-U.S. crew blasts off for space station (Canadian Press) Canadian Press - BAIKONUR, Kazakhstan (AP) - A Russian rocket carrying a new Russian-U.S. crew to the international space station li"  
  "A Russian rocket carrying a new Russian-U.S. crew to the international space station lifted off from the Baikonur cosmodrome" is space, Sci/Tech.
- [ ] `ag_news:test:6509` **World** -> **Business**: "Death bell tolls for Russia's Yukos oil giant (AFP) AFP - Russia's Yukos does not begin the week teetering on the edge of ruin where it has been for months now. The oil giant is flat on its back, gasping for its last bre"  
  "The oil giant is flat on its back, gasping for its last breaths of air" is company news about Yukos' collapse, Business.
- [ ] `ag_news:test:6248` **Business** -> **World**: "Study Ranks St. Louis as Fourth Most Dangerous City A new study ranks St. Louis as the fourth most dangerous city. Camden, New Jersey came in first, followed by Detroit and Atlanta. The rankings are in Morgan Quitno #39;"  
  "A new study ranks St. Louis as the fourth most dangerous city" in the "City Crime Rankings" is a crime story, World, not Business.
- [ ] `ag_news:test:3968` **Business** -> **Sci/Tech**: "US consumers unaware of spyware The findings come in a report from the newly formed Consumer Spyware Initiative, a joint effort by Dell and the non-profit Internet Education Foundation that aims to increase awareness of "  
  "the newly formed Consumer Spyware Initiative, a joint effort by Dell and the non-profit Internet Education Foundation that aims to increase awareness of spyware" is computer security, Sci/Tech.
- [ ] `ag_news:test:1043` **Sci/Tech** -> **World**: "Strong Hurricane Roars Over Bahamas Toward Florida (Reuters) Reuters - Hurricane Frances battered the\southeastern Bahamas islands with 140 mph winds on Wednesday as\it roared toward the United States and put millions of"  
  "Hurricane Frances battered the southeastern Bahamas islands with 140 mph winds ... and put millions of people on alert" is a disaster story, World, not Sci/Tech.
- [ ] `ag_news:test:4997` **World** -> **Business**: "Volkswagen May Be Close to Settling Its Wage Talks Volkswagen and its workers entered a critical week in their wage negotiations on Monday, with signs that a compromise was taking shape even as protests flared at factori"  
  "Volkswagen and its workers entered a critical week in their wage negotiations" is a labour story, which the guidelines put under Business.
- [ ] `ag_news:test:3183` **Business** -> **Sci/Tech**: "webcrawler: A9.com is cool NOW heres something else thats off the mind. Theres no more need to make mental or computer notes while searching the Internet."  
  "webcrawler: A9.com is cool ... no more need to make mental or computer notes while searching the Internet" is an internet search tool story, Sci/Tech.
- [ ] `ag_news:test:6985` **World** -> **Business**: "Data revision shows Japan's economy grew slightly in July-September (Canadian Press) Canadian Press - TOKYO (AP) - Japan's economy barely grew during the quarter ending Sept. 30 and in the April-June period it actually s"  
  "Japan's economy barely grew during the quarter ending Sept. 30 ... according to revised government data" is economic data, Business.
- [ ] `ag_news:test:1774` **Sci/Tech** -> **World**: "Slowing population 'lacks funds' Rich countries are giving only half the amount they promised to help to slow world population growth, the UN says."  
  "Rich countries are giving only half the amount they promised to help to slow world population growth, the UN says" is international aid politics, World, not Sci/Tech.
- [ ] `ag_news:test:1881` **Sci/Tech** -> **World**: "Hurricane Ivan Slams U.S. Gulf Coast Hurricane Ivan roared into the Gulf Coast near Mobile, Alabama, early this morning with peak winds exceeding 125 miles an hour (200 kilometers an hour)."  
  "Hurricane Ivan roared into the Gulf Coast near Mobile, Alabama ... with peak winds exceeding 125 miles an hour" is a disaster story, World, not Sci/Tech.
- [ ] `ag_news:test:7426` **Sci/Tech** -> **World**: "R.I.P. Gary Webb -- Unembedded Reporter The finest journalist ever to get fired for telling the truth is dead at age 49. The official cause of death on the death certificate will be suicide. But, as we shall see, he had "  
  "The finest journalist ever to get fired for telling the truth is dead at age 49 ... says much about the state of American politics" is politics and journalism, World, not Sci/Tech.
- [ ] `ag_news:test:881` **Business** -> **World**: "Scaffold collapse survivors improving One of the men who survived Friday #39;s fatal scaffold collapse is in guarded condition at Detroit Receiving Hospital and the two other survivors were released on Sunday, a hospital"  
  "One of the men who survived Friday's fatal scaffold collapse is in guarded condition at Detroit Receiving Hospital" is an accident story, World, not Business.
- [ ] `ag_news:test:1232` **Sports** -> **World**: "2 charged after Chicago area pals are slain in NC tragedy Ever since they met in fourth grade, Brett Johnson Harman and Kevin McCann were as close as brothers.  quot;They had the same mannerisms, the same kind of humor, "  
  "2 charged after Chicago area pals are slain in NC tragedy" is a crime story, World, and nothing in it is Sports.
- [ ] `ag_news:test:6369` **Business** -> **World**: "TSA  #39;pat-downs #39; cross the line for some fliers Millions of holiday travelers nationwide are experiencing an all-too-intimate form of security screening that some say amounts to sexual groping - a  quot;pat-down q"  
  "security screening that some say amounts to sexual groping - a 'pat-down' by government officials" is a government and civil-liberties story, World, not Business.
- [ ] `ag_news:test:6835` **Sci/Tech** -> **World**: "Prying Into FBI Activities The ACLU files Freedom of Information Act requests to find out why antiterrorism task forces have been monitoring activists. By Ryan Singel."  
  "The ACLU files Freedom of Information Act requests to find out why antiterrorism task forces have been monitoring activists" is civil liberties and government, World; nothing in the text is Sci/Tech.
- [ ] `ag_news:test:3116` **Sci/Tech** -> **World**: "OPM Delving Deeper Into Employees #39; Backgrounds which sets hiring and employment standards for the government -- is reviewing its employees to ensure that they are suitable for jobs involving the  quot;public trust."  
  "sets hiring and employment standards for the government -- is reviewing its employees to ensure that they are suitable for jobs involving the 'public trust'" is government administration, World, not Sci/Tech.
- [ ] `ag_news:test:6068` **Sci/Tech** -> **World**: "A Fair Tax Some say a "fair tax" that removes the need to file tax returns from the vast majority of the citizenry is a national sales tax.  This doesn't seem to be very fair to people trying to feed, house and clothe th"  
  An opinion piece on "Bush's proposal for a national sales tax" and "Bush's favorite constituency" is political and economic policy, World (or arguably Business), but not Sci/Tech.
- [ ] `ag_news:test:1775` **Business** -> **World**: "Coast Guard Shuts Gulf of Mexico Ports  HOUSTON (Reuters) - The U.S. Coast Guard shut five ports on  Wednesday in the Gulf of Mexico coast states of Alabama,  Florida and Mississippi as Hurricane Ivan churned nearer."  
  "The U.S. Coast Guard shut five ports on Wednesday ... as Hurricane Ivan churned nearer" is disaster response, World; the text says nothing about trade or shipping business.
- [ ] `ag_news:test:7008` **Business** -> **World**: "Get Real? This time last week, first lady Laura Bush was having what she might call her Christmas Tree Day. First, she showed off the decorated executive mansion to reporters and then joined her husband"  
  "first lady Laura Bush ... showed off the decorated executive mansion to reporters and then joined her husband" is a White House human-interest story, World, not Business.
- [ ] `ag_news:test:4567` **World** -> **Business**: "EU Head Office Trims 2005 Growth Forecast (AP) AP - The European Union's head office issued a bleak economic report Tuesday, warning that the sharp rise in oil prices will "take its toll" on economic growth next year whi"  
  "The European Union's head office issued a bleak economic report Tuesday, warning that the sharp rise in oil prices will 'take its toll' on economic growth" is economics, Business.
- [ ] `ag_news:test:5145` **Sci/Tech** -> **World**: "Serial HIV Assault Verdict Expected Mon. (AP) AP - A verdict will be announced Monday in the trial of a man charged with intentionally exposing 17 women to HIV, a county judge said."  
  "A verdict will be announced Monday in the trial of a man charged with intentionally exposing 17 women to HIV, a county judge said" is a court story, World, not Sci/Tech.
- [ ] `ag_news:test:1042` **Sci/Tech** -> **Business**: "Make hotels just like home HOTEL operators, take note: Todays hotel guests are making a nonsense of room-pricing strategies with their aggressive, Internet-aided discount-hunting."  
  "HOTEL operators, take note: Todays hotel guests are making a nonsense of room-pricing strategies" is a hotel industry pricing story, Business; "Internet-aided" is incidental.
- [ ] `ag_news:test:1527` **Business** -> **World**: "Storms Seem to Cure Floridians of Hurricane Amnesia The state #39;s East Coast hadn #39;t been hit by a hurricane since 1999. That, and the fact that Florida hasn #39;t had its historic share of such storms in recent dec"  
  "The state's East Coast hadn't been hit by a hurricane since 1999 ... has led to some complacency about their effects" is a disaster story, World, not Business.
- [ ] `ag_news:test:3265` **Sci/Tech** -> **Sports**: "How to take the perfect penalty A sports psychologist says how footballers should prepare themselves for the high-pressure penalties."  
  "A sports psychologist says how footballers should prepare themselves for the high-pressure penalties" is football advice, Sports, not Sci/Tech.
- [ ] `ag_news:test:5588` **World** -> **Business**: "China's inflation rate slows sharply but problems remain (AFP) AFP - China's inflation rate eased sharply in October as government efforts to cool the economy began to really bite, with food prices, one of the main culpr"  
  "China's inflation rate eased sharply in October as government efforts to cool the economy began to really bite ... official data showed" is economic data, Business.
- [ ] `ag_news:test:2053` **World** -> **Business**: "EU transport chief hails Alitalia accord (AFP) AFP - EU transport and energy commissioner Loyola de Palacio hailed the accord reached between Alitalia management and staff on a major restructuring plan aimed at keeping t"  
  "the accord reached between Alitalia management and staff on a major restructuring plan aimed at keeping the struggling airline in the air" is a company restructuring and labour story, Business; the EU commissioner's praise is only the hook.
- [ ] `ag_news:test:4540` **Sports** -> **World**: "Miss Peru takes Miss World crown Twenty-year-old Miss Peru has been crowned Miss World in a southern Chinese resort town, as China looks to become the regular host of an event that would have once been deemed heretical b"  
  "Miss Peru has been crowned Miss World in a southern Chinese resort town, as China looks to become the regular host" is a human-interest and China story, World; a beauty pageant is not Sports.
- [ ] `ag_news:test:5217` **Business** -> **World**: "Ontario gets harsh with school dropouts HUNTSVILLE, ONT. - The Ontario government plans to introduce legislation that will require students to stay in school until they reach the age of 18, said the province?"  
  "The Ontario government plans to introduce legislation that will require students to stay in school until they reach the age of 18" is government and education, World, not Business.
- [ ] `ag_news:test:1106` **Sci/Tech** -> **World**: "Md. Board Meeting Worries Democrats Republican-dominated election board met behind closed doors in deliberations that Democrats feared were aimed at ousting Elections Administrator Linda H. Lamone.&lt;BR&gt;\&lt;FONT fac"  
  "Republican-dominated election board met behind closed doors in deliberations that Democrats feared were aimed at ousting Elections Administrator Linda H. Lamone" is state politics, World; nothing in the text is Sci/Tech.
- [ ] `ag_news:test:3005` **Business** -> **World**: "Perry OKs money for APS as more accusations arise The state #39;s Adult Protective Services agency will get an emergency infusion of \$10 million to correct the kinds of problems that have arisen in El Paso."  
  "The state's Adult Protective Services agency will get an emergency infusion of $10 million to correct the kinds of problems that have arisen in El Paso" is state government, World, not Business.
- [ ] `ag_news:test:789` **Sci/Tech** -> **World**: "Bea Arthur for President Bea Arthur sparked a security scare at Logan Airport in Boston this week when she tried to board a Cape Air flight with a pocketknife in her handbag.    The "Golden Girls" star, now 81, was flagg"  
  "Bea Arthur sparked a security scare at Logan Airport in Boston this week when she tried to board a Cape Air flight with a pocketknife" is a human-interest and airport-security anecdote, World, not Sci/Tech.
- [ ] `ag_news:test:5692` **Sports** -> **World**: "Boston archbishop reveals anguish of closings BOSTON Boston #39;s Archbishop is telling catholics that the church #39;s financial footing is  quot;much worse than people realize."  
  "Boston's Archbishop is telling catholics that the church's financial footing is 'much worse than people realize'" is a religion and community story, World (or arguably Business), and nothing in it is Sports.
- [ ] `ag_news:test:5628` **Business** -> **World**: "Governor calls for resignation of Big Dig chief BOSTON Massachusetts Governor Mitt Romney is calling for the resignation of the head of the state #39;s Turnpike Authority. Romney #39;s move comes in the wake of reports t"  
  "Massachusetts Governor Mitt Romney is calling for the resignation of the head of the state's Turnpike Authority" is state government, World, not Business.
- [ ] `ag_news:test:5277` **Business** -> **World**: "Closing the giving gap Near the entrance for the Christmas Tree Shop on Route 1 in Lynnfield, Barbara Patten stood next to her Salvation Army kettle and played her flute on a recent Saturday as customers walked past."  
  "Barbara Patten stood next to her Salvation Army kettle and played her flute on a recent Saturday as customers walked past" is a human-interest charity story, World, not Business.

## banking77 (41 rows)

- [ ] `banking77:test:848` **transfer_not_received_by_recipient** -> **transfer_timing**: "how long do money transfers take?"  
  Generic "how long do money transfers take?" with no recipient or missing money is transfer_timing.
- [ ] `banking77:test:2088` **reverted_card_payment?** -> **declined_card_payment**: "My card is being declined for a purchase. I bought items before and the card worked. Do you know what the problem is?"  
  "My card is being declined for a purchase" is a live decline, not a payment reverted after the fact.
- [ ] `banking77:test:1004` **top_up_reverted** -> **top_up_failed**: "The app wouldn't accept my top up."  
  "The app wouldn't accept my top up" is a top-up declined at the time, not reversed afterwards.
- [ ] `banking77:test:844` **transfer_not_received_by_recipient** -> **transfer_timing**: "How long does it take for a transfer to get to a recipient?"  
  "How long does it take for a transfer to get to a recipient?" is a generic timing question; nothing says a recipient has not received money.
- [ ] `banking77:test:2848` **activate_my_card** -> **lost_or_stolen_card**: "WHAT CAN I DO AFTER THE CARD MISSING"  
  "AFTER THE CARD MISSING" is a lost card, nothing about activation.
- [ ] `banking77:test:2687` **balance_not_updated_after_bank_transfer** -> **transfer_timing**: "How long does a UK transfer take?"  
  "How long does a UK transfer take?" is generic timing; no incoming money is said to be missing.
- [ ] `banking77:test:2567` **wrong_exchange_rate_for_cash_withdrawal** -> **exchange_charge**: "Is there a fee for exchanging cash?"  
  "a fee for exchanging cash" asks about the fee on an exchange, not a wrong rate on an ATM withdrawal.
- [ ] `banking77:test:2571` **wrong_exchange_rate_for_cash_withdrawal** -> **cash_withdrawal_charge**: "Will there be additional costs of I make a withdrawal from a local ATM of British pounds? I need some cash to feel comfortable on the journey home"  
  "additional costs of I make a withdrawal from a local ATM" is a fee question on a cash withdrawal, not a wrong exchange rate.
- [ ] `banking77:test:1848` **pending_transfer** -> **transfer_timing**: "How long can an EU transfer take?"  
  "How long can an EU transfer take?" is generic timing with no specific pending transfer.
- [ ] `banking77:test:1223` **unable_to_verify_identity** -> **verify_my_identity**: "What do i need to verify my id?"  
  "What do i need to verify my id?" asks how to verify, with no failed attempt stated.
- [ ] `banking77:test:1875` **pending_transfer** -> **transfer_timing**: "How long does it take for a money transfer to show?"  
  "How long does it take for a money transfer to show?" is generic timing, not a specific pending transfer.
- [ ] `banking77:test:2186` **beneficiary_not_allowed** -> **failed_transfer**: "The account transfer I was trying to do failed."  
  "The account transfer I was trying to do failed" is a failed transfer with no beneficiary restriction mentioned.
- [ ] `banking77:test:2681` **balance_not_updated_after_bank_transfer** -> **transfer_timing**: "How long does it take for an international transfer into my account?"  
  "How long does it take for an international transfer into my account?" is a generic timing question; nothing says money has been sent and not arrived.
- [ ] `banking77:test:536` **pin_blocked** -> **card_swallowed**: "I attempted to use my card while I was intoxicated, and I failed to input my PIN, and the machine kept my card. How soon can I have it back?"  
  "the machine kept my card. How soon can I have it back?" is a swallowed card, not a PIN block.
- [ ] `banking77:test:2248` **receiving_money** -> **fiat_currency_support**: "Is GBP a supported currency?"  
  "Is GBP a supported currency?" is a currency-support question, not about receiving money.
- [ ] `banking77:test:1008` **top_up_reverted** -> **top_up_failed**: "I put money into my account for the minimum balance but the application didn't accept."  
  "the application didn't accept" the money is a top-up declined at the time, not reverted later.
- [ ] `banking77:test:1065` **balance_not_updated_after_cheque_or_cash_deposit** -> **top_up_by_cash_or_cheque**: "Why does my account not accept cash deposits?"  
  "Why does my account not accept cash deposits?" asks whether cash deposits are supported, not about a deposit that has not shown up.
- [ ] `banking77:test:1864` **pending_transfer** -> **transfer_timing**: "How long does a transfer take to be confirmed?"  
  "How long does a transfer take to be confirmed?" is generic timing, not a specific pending transfer.
- [ ] `banking77:test:605` **top_up_by_bank_transfer_charge** -> **transfer_into_account**: "I would like to refill my account using SWIFT."  
  "refill my account using SWIFT" asks about transferring money in; no fee is mentioned.
- [ ] `banking77:test:520` **pin_blocked** -> **get_physical_card**: "Where can I view my PIN?"  
  "Where can I view my PIN?" is the where-to-find-my-PIN question, which the guidelines assign to get_physical_card.
- [ ] `banking77:test:1190` **why_verify_identity** -> **verify_my_identity**: "What other methods are there to verify my identity?"  
  "What other methods are there to verify my identity?" asks how to verify, not why verification is required.
- [ ] `banking77:test:2757` **exchange_charge** -> **exchange_rate**: "whats your exchange rate"  
  "whats your exchange rate" asks for the rate, not for a fee.
- [ ] `banking77:test:1838` **pending_transfer** -> **transfer_timing**: "How long for money transfer to show?"  
  "How long for money transfer to show?" is generic timing, not a specific pending transfer.
- [ ] `banking77:test:608` **top_up_by_bank_transfer_charge** -> **transfer_into_account**: "Is it possible to get a transfer from SWIFT?"  
  "get a transfer from SWIFT" asks about incoming SWIFT transfers; no charge is mentioned.
- [ ] `banking77:test:2161` **beneficiary_not_allowed** -> **exchange_via_app**: "Can you please help me with this exchange?  I am trying to get crypto and the app won't let me."  
  "help me with this exchange ... trying to get crypto and the app won't let me" is an in-app exchange problem, not a beneficiary issue.
- [ ] `banking77:test:377` **card_not_working** -> **declined_card_payment**: "My card was declined today when eating and I need to know what's wrong."  
  "My card was declined today when eating" is a declined card payment.
- [ ] `banking77:test:2185` **beneficiary_not_allowed** -> **exchange_via_app**: "I am trying to exchange crypto and it's not working. Tell me how to fix this."  
  "trying to exchange crypto and it's not working" is an in-app exchange problem with no beneficiary.
- [ ] `banking77:test:1727` **declined_transfer** -> **declined_card_payment**: "The card got declined twice when I tried to use it to buy something online yesterday."  
  "The card got declined twice ... to buy something online" is a declined card payment, not a transfer.
- [ ] `banking77:test:1718` **declined_transfer** -> **declined_card_payment**: "Good morning. I tried to make a purchase with my credit card last night and again this morning. Both times it was declined. Can you investigate?"  
  "make a purchase with my credit card ... it was declined" is a declined card payment, not a transfer.
- [ ] `banking77:test:2633` **get_disposable_virtual_card** -> **disposable_card_limits**: "how many transactions can i make with a disposable card"  
  "how many transactions can i make with a disposable card" is a limits question, not a request to get one.
- [ ] `banking77:test:1207` **unable_to_verify_identity** -> **verify_my_identity**: "Help my verify my id."  
  "Help my verify my id" asks for help verifying with no failed attempt stated.
- [ ] `banking77:test:1736` **declined_transfer** -> **declined_card_payment**: "When I try and to buy something using my card it keeps getting declined."  
  "buy something using my card it keeps getting declined" is a declined card payment, not a transfer.
- [ ] `banking77:test:1669` **lost_or_stolen_phone** -> **lost_or_stolen_card**: "Someone stole my cards!"  
  "Someone stole my cards!" is a stolen card, not a phone.
- [ ] `banking77:test:1755` **declined_transfer** -> **declined_card_payment**: "I was attempting to purchase a golf club off eBay yesterday, but my credit card was declined. I tried multiple times, and again this morning. Can you check into my card please?"  
  "purchase a golf club off eBay ... my credit card was declined" is a declined card payment.
- [ ] `banking77:test:2825` **top_up_by_card_charge** -> **topping_up_by_card**: "Is it okay to use a bank card to top up"  
  "Is it okay to use a bank card to top up" asks whether card top-up is allowed; no charge is mentioned.
- [ ] `banking77:test:1753` **declined_transfer** -> **declined_card_payment**: "My card is being declined online. Could you tell me what might be broken or wrong with the account?"  
  "My card is being declined online" is a declined card payment, not a transfer.
- [ ] `banking77:test:2759` **exchange_charge** -> **exchange_rate**: "Where do I find the exchange rate?"  
  "Where do I find the exchange rate?" asks about the rate, not a charge.
- [ ] `banking77:test:1752` **declined_transfer** -> **declined_card_payment**: "I tried to buy something online yesterday but it wouldn't stop saying declined. Tried again today but same thing happened. What's Broken?"  
  "buy something online ... saying declined" is a declined card payment, not a transfer.
- [ ] `banking77:test:1751` **declined_transfer** -> **declined_card_payment**: "I tried to buy something online yesterday but it kept saying declined. Tried again today but same thing happened. What's broken?"  
  "buy something online ... kept saying declined" is a declined card payment, not a transfer.
- [ ] `banking77:test:871` **transfer_not_received_by_recipient** -> **transfer_timing**: "When will my funds transfer?"  
  "When will my funds transfer?" asks about timing; nothing says a recipient has not received anything.
- [ ] `banking77:test:268` **fiat_currency_support** -> **exchange_via_app**: "I want to make a currency exchange to EU."  
  "I want to make a currency exchange to EU" is a request to perform an exchange, not a question about which currencies are supported.

## emotion (74 rows)

- [ ] `emotion:test:1440` **joy** -> **fear**: "i guess no matter how much i think im feeling ok im as nervous as hell on the inside about the scan revealing something i dont want to know again"  
  Writer is 'as nervous as hell on the inside about the scan revealing something', which is fear, not joy.
- [ ] `emotion:test:502` **anger** -> **fear**: "i am feeling stressed and more than a bit anxious"  
  'stressed and more than a bit anxious' is anxiety, i.e. fear, not anger.
- [ ] `emotion:test:1270` **joy** -> **sadness**: "i feel very saddened that the king whom i once quite respected as far as monarchs go was ineffectual at best"  
  'i feel very saddened' states sadness outright; joy is unsupported.
- [ ] `emotion:test:603` **anger** -> **fear**: "i feel like it s waiting in the wings just patiently waiting for me to be distracted enough so it can take me down and take everything i love in this world away and destroy me"  
  Dread of something 'waiting ... to take me down ... and destroy me' is fear, not anger.
- [ ] `emotion:test:1426` **anger** -> **fear**: "i get the feeling that this could be dangerous"  
  'this could be dangerous' is worry about danger, which the guidelines map to fear.
- [ ] `emotion:test:718` **anger** -> **fear**: "i feel that it is extremely dangerous for her to be wandering out to sea"  
  'extremely dangerous for her to be wandering out to sea' is worry about danger, i.e. fear.
- [ ] `emotion:test:1190` **anger** -> **fear**: "i noticed that i was feeling very stressed and anxious and i just couldnt quite put my finger on why"  
  'feeling very stressed and anxious' is fear, not anger.
- [ ] `emotion:test:1144` **anger** -> **fear**: "i feel that i worry too much and much on petty things like"  
  'i worry too much ... on petty things' is worry, i.e. fear.
- [ ] `emotion:test:625` **surprise** -> **fear**: "i am feeling overwhelmed by trying to do it all that i think on the women before me"  
  'feeling overwhelmed by trying to do it all' is overwhelmed, which the guidelines map to fear, not surprise.
- [ ] `emotion:test:820` **surprise** -> **fear**: "i found myself feeling a bit overwhelmed"  
  'feeling a bit overwhelmed' is overwhelmed, mapped to fear by convention.
- [ ] `emotion:test:1185` **surprise** -> **fear**: "i start to feel a little overwhelmed knowing i have to make still"  
  'feel a little overwhelmed knowing i have to make still' is overwhelmed, i.e. fear.
- [ ] `emotion:test:705` **surprise** -> **fear**: "i feel overwhelmed how about you"  
  'i feel overwhelmed' is overwhelmed, mapped to fear by convention.
- [ ] `emotion:test:1240` **surprise** -> **sadness**: "i just feel like im going no where and that the period of time where i was so very much enthralled with life and the options it proposed is now over"  
  'going no where' and the good period 'is now over' express sadness, not surprise.
- [ ] `emotion:test:1228` **joy** -> **fear**: "i do not feel assured"  
  'i do not feel assured' is the guidelines' own example of negation flipping to fear.
- [ ] `emotion:test:969` **surprise** -> **fear**: "i have been feeling overwhelmed with it all and needing to take time out"  
  'feeling overwhelmed with it all and needing to take time out' is overwhelmed, i.e. fear.
- [ ] `emotion:test:800` **joy** -> **anger**: "i feel that he is so determined to steal private industries away from citizens of this nation that he has given no time to fighting the real enemies of theu"  
  Denouncing someone 'so determined to steal private industries away from citizens' is anger, not joy.
- [ ] `emotion:test:444` **sadness** -> **fear**: "i wake up feeling like something terrifyingly bad is bound to happen to me before i even get a chance to stick a limb outside of my covers"  
  'something terrifyingly bad is bound to happen to me' is fear, not sadness.
- [ ] `emotion:test:900` **anger** -> **joy**: "i didnt start feeling the excitement until the movie was almost over and then it started coming in violent waves"  
  'feeling the excitement ... coming in violent waves' is excitement, i.e. joy; 'violent' is not anger.
- [ ] `emotion:test:1392` **joy** -> **sadness**: "im not feeling jolly in the least"  
  'not feeling jolly in the least' negates jolly, flipping joy to sadness.
- [ ] `emotion:test:67` **anger** -> **fear**: "i feel a bit stressed even though all the things i have going on are fun"  
  'i feel a bit stressed' is stress/anxiety, i.e. fear, not anger.
- [ ] `emotion:test:1734` **surprise** -> **joy**: "im feeling absolutely amazing"  
  'feeling absolutely amazing' is joy; nothing surprising is expressed.
- [ ] `emotion:test:777` **sadness** -> **fear**: "i have been feeling really stressed out due to homework and my studies that have increased rapidly over the last week"  
  'really stressed out due to homework' is stress/anxiety, i.e. fear, not sadness.
- [ ] `emotion:test:290` **surprise** -> **anger**: "i just feel are ludicrous and wasting space or so trite they should have looked at the book first and come up with something a little more original"  
  Calling things 'ludicrous and wasting space or so trite' is irritation, i.e. anger, not surprise.
- [ ] `emotion:test:745` **joy** -> **sadness**: "im not feeling very hopeful about the coming summer"  
  'not feeling very hopeful about the coming summer' negates hopeful, flipping joy to sadness.
- [ ] `emotion:test:1358` **love** -> **fear**: "im looking at the stress levels im feeling and not loving how concentrated they are because of my mindset of planning a wedding in four months"  
  'stress levels im feeling and not loving how concentrated they are' is stress about wedding planning, i.e. fear; 'loving' is negated.
- [ ] `emotion:test:796` **sadness** -> **joy**: "im much more peaceful and happy when the house is clean the food is good and my kids arent feeling needy"  
  Writer says 'im much more peaceful and happy'; 'needy' describes the kids, not the writer.
- [ ] `emotion:test:562` **sadness** -> **fear**: "i was worried that maybe she was sleeping so well because she wasn t getting enough milk and was feeling lethargic"  
  'i was worried that maybe she ... wasn t getting enough milk' is the writer's worry, i.e. fear; 'lethargic' is the baby's state.
- [ ] `emotion:test:1797` **surprise** -> **fear**: "i feel the pressure to be funny all the time"  
  'i feel the pressure to be funny all the time' is anxiety under pressure, i.e. fear, not surprise.
- [ ] `emotion:test:376` **joy** -> **fear**: "i suppose if one was feeling generous one could say i was stressed by the elevator ride"  
  'if one was feeling generous' is hypothetical; the writer's own state is 'stressed by the elevator ride', i.e. fear.
- [ ] `emotion:test:53` **sadness** -> **fear**: "i can t stop the anxiety i feel when i m alone when i ve got no distractions"  
  'the anxiety i feel when i m alone' is fear, not sadness.
- [ ] `emotion:test:1637` **surprise** -> **joy**: "i just got back from another miler faster than yesterday and im feeling amazing"  
  'faster than yesterday and im feeling amazing' is joy; nothing surprising is expressed.
- [ ] `emotion:test:1858` **anger** -> **joy**: "i was feeling pretty distracted with a few things that have been going on so it felt good to go with a clear mind"  
  'it felt good to go with a clear mind' is the present feeling; 'distracted' is past and over, and neither is anger.
- [ ] `emotion:test:1230` **joy** -> **sadness**: "im not feeling the jolly this year though"  
  'im not feeling the jolly this year' negates jolly, flipping joy to sadness.
- [ ] `emotion:test:1051` **surprise** -> **joy**: "i ran errands to buy cora a few newborn sized sleepers i had not previously made any newborn sized babies and went out to lunch to celebrate how great i was feeling i feel amazing no pain no pain meds and moving around a"  
  'celebrate how great i was feeling i feel amazing no pain' is joy, not surprise.
- [ ] `emotion:test:1552` **fear** -> **joy**: "i am finally starting to feel like i have a real life here in san vicente and i am no longer on a strange confusing extended vacation"  
  'finally starting to feel like i have a real life' is relief/joy; 'strange confusing' is what is 'no longer' the case.
- [ ] `emotion:test:202` **love** -> **joy**: "i got home feeling hot tired and great"  
  'feeling hot tired and great' is joy; nothing loving is expressed.
- [ ] `emotion:test:500` **anger** -> **fear**: "i feel it is dangerous especially for the new believer who is not grounded in the word of god"  
  'i feel it is dangerous especially for the new believer' is worry about danger, mapped to fear.
- [ ] `emotion:test:418` **anger** -> **fear**: "i have been sitting at home revising today and all in all feeling quite stressed"  
  'feeling quite stressed' from revising is stress/anxiety, i.e. fear, not anger.
- [ ] `emotion:test:192` **joy** -> **love**: "i am being over dramatic but i do feel very strongly for her and i am resolved to speak with her next chance i get"  
  'i do feel very strongly for her and i am resolved to speak with her' is romantic affection, i.e. love.
- [ ] `emotion:test:624` **anger** -> **joy**: "i feel like i m finally losing that stubborn little bit of extra stuff in my lower belly"  
  'finally losing that stubborn little bit of extra stuff' is satisfaction, i.e. joy; 'stubborn' describes belly fat.
- [ ] `emotion:test:1876` **anger** -> **fear**: "i need a break or im feeling stressed out"  
  'im feeling stressed out' is stress/anxiety, i.e. fear, not anger.
- [ ] `emotion:test:1070` **surprise** -> **sadness**: "i feel shame in a strange way"  
  'i feel shame' is ashamed, mapped to sadness by convention, not surprise.
- [ ] `emotion:test:1280` **joy** -> **fear**: "i typed up all my blood pressures for the month but i have a feeling hes not going to be too pleased with the lack of missing information"  
  'i have a feeling hes not going to be too pleased' is apprehension, i.e. fear; 'pleased' is negated and about someone else.
- [ ] `emotion:test:1386` **love** -> **fear**: "i guess its because i feel like if im too passionate about something it will get taken away from me"  
  'if im too passionate about something it will get taken away from me' is fear of loss; 'passionate' is the hypothetical trigger.
- [ ] `emotion:test:1957` **surprise** -> **joy**: "i am feeling amazing and seeing the difference"  
  'feeling amazing and seeing the difference' is joy, not surprise.
- [ ] `emotion:test:606` **joy** -> **fear**: "i don t feel comfortable playing games with them presenting the bad guy as really a misunderstood good guy or vice versa"  
  'i don t feel comfortable playing games with them' is uncomfortable, mapped to fear; joy is negated.
- [ ] `emotion:test:622` **joy** -> **fear**: "i don t feel brave though"  
  'i don t feel brave though' negates brave, flipping to fear.
- [ ] `emotion:test:921` **sadness** -> **joy**: "i feel less stress about doing pretty much any unpleasant obligation in life because i know that i will allow myself to mix it with things i enjoy running baking climbing coffee with girlfriends cuddling with my dog read"  
  'i feel less stress ... things i enjoy running baking climbing' is contentment, i.e. joy, not sadness.
- [ ] `emotion:test:191` **sadness** -> **joy**: "im enjoying my solitary confinement at home i rarely feel lonely"  
  'im enjoying my solitary confinement ... i rarely feel lonely' is joy; lonely is negated.
- [ ] `emotion:test:1934` **joy** -> **sadness**: "i dont really care and i dont feel proud of myself at all"  
  'i dont feel proud of myself at all' negates proud, flipping joy to sadness.
- [ ] `emotion:test:678` **joy** -> **fear**: "i feel like i have all these cute things but i dont feel comfortable in them and dont know how to put them together"  
  'i dont feel comfortable in them' is uncomfortable, mapped to fear; 'cute' is about the clothes.
- [ ] `emotion:test:58` **sadness** -> **joy**: "i feel like i am just starting to understand the blessings that come from being submissive to the will of the father"  
  'starting to understand the blessings' is gratitude/joy; 'submissive' carries no sadness here.
- [ ] `emotion:test:1142` **joy** -> **love**: "i tell you that i love you and my feelings are sincere my dear"  
  'i love you and my feelings are sincere my dear' is love, not joy.
- [ ] `emotion:test:1377` **love** -> **joy / none**: "i walked to school he felt the bounce in his step the overjoyed feelings of youth and the thrill of excitement of coming to school and meeting his beloved friends"  
  The dominant feeling is 'overjoyed feelings of youth and the thrill of excitement'; 'beloved friends' is only a descriptor.
- [ ] `emotion:test:426` **sadness** -> **fear**: "i feel unprotected a class post count link href http reprogramming in process"  
  'i feel unprotected' is vulnerability to harm, i.e. fear, not sadness.
- [ ] `emotion:test:1744` **sadness** -> **joy**: "im happy to report im still not feeling terribly stressed"  
  'im happy to report im still not feeling terribly stressed' is joy; stressed is negated.
- [ ] `emotion:test:778` **joy** -> **fear**: "im begging fate not to mess with the next cycle to let it look as pretty as this one so i can at least go in feeling reassured"  
  'begging fate not to mess with the next cycle' is anxiety, i.e. fear; 'reassured' is a hoped-for future state.
- [ ] `emotion:test:856` **sadness** -> **anger**: "i want you to feel just as humiliated as you made me feel in school"  
  'i want you to feel just as humiliated as you made me feel' is vengeful anger, not sadness.
- [ ] `emotion:test:347` **fear** -> **anger**: "i feel agitated and annoyed more than worried or fearful but these feelings can easily lead to being short tempered with my family and feelings of disharmony"  
  'i feel agitated and annoyed more than worried or fearful' explicitly ranks anger above fear.
- [ ] `emotion:test:464` **sadness** -> **fear / none**: "i feel an unpleasant drop in my stomach as the elevator doors open at my floor"  
  'an unpleasant drop in my stomach as the elevator doors open' is anticipatory dread, i.e. fear, not sadness.
- [ ] `emotion:test:1320` **anger** -> **joy**: "i feel like a greedy pig catching up to do lt bc afterward yay im gna get my delicious chocolates and in exchange zjs gna get bai tu tang from me"  
  'yay im gna get my delicious chocolates' is joy; 'greedy pig' is self-mocking, not anger.
- [ ] `emotion:test:844` **surprise** -> **joy**: "i guess it doesn t help that i got sick on black friday and was forced against my will to maintain my promise to stay in but being back in the city feels amazing"  
  'being back in the city feels amazing' is joy, not surprise.
- [ ] `emotion:test:247` **anger** -> **joy**: "i feel like my irritable sensitive combination skin has finally met it s match"  
  'has finally met it s match' is satisfaction, i.e. joy; 'irritable' describes skin, not the writer.
- [ ] `emotion:test:1969` **love** -> **none**: "i can feel the warmth of the gentle sun"  
  'i can feel the warmth of the gentle sun' is a physical sensation with no emotion stated.
- [ ] `emotion:test:1431` **sadness** -> **joy**: "i felt a stronger wish to be free from self cherishing through my refuge practice and a return to the feeling of freedom and protection from suffering which i stayed with for the rest of the meditation"  
  'a return to the feeling of freedom and protection from suffering' is peace/joy; 'suffering' is what is escaped.
- [ ] `emotion:test:1791` **surprise** -> **joy / none**: "i did a body scan and realized that everything was feeling amazing"  
  'everything was feeling amazing' is joy, not surprise.
- [ ] `emotion:test:260` **anger** -> **fear**: "i used to be able to hang around talk with the cashier when i was putting away my money now i feel rushed and stressed if i take a second to fumble with the coins and put them in my purse"  
  'now i feel rushed and stressed' is stress/anxiety, i.e. fear, not anger.
- [ ] `emotion:test:1313` **joy** -> **sadness**: "i honestly wish christmas was celebrated in the summer because i feel like i tend not be as jolly as i wish i could be"  
  'i tend not be as jolly as i wish i could be' negates jolly, flipping joy to sadness.
- [ ] `emotion:test:1115` **sadness** -> **anger**: "i vented my feelings towards the pathetic excuse of a communicat"  
  'vented my feelings towards the pathetic excuse of a communicat' is anger, not sadness.
- [ ] `emotion:test:608` **love** -> **joy / none**: "i bought the gb iphone i got a apple store credit i feel like they were sympathetic to early buyers and responded appropriately"  
  'they were sympathetic to early buyers and responded appropriately' is satisfaction, i.e. joy; 'sympathetic' is Apple's attitude, not the writer's.
- [ ] `emotion:test:529` **love** -> **joy**: "i feel like my sweet company is finally coming together"  
  'my sweet company is finally coming together' is satisfaction, i.e. joy; 'sweet' is a descriptor, not the writer's love.
- [ ] `emotion:test:1593` **sadness** -> **fear**: "i suppose we all feel a little inhibited when it comes to picking up the phone and calling someone we re not very close to anymore"  
  'feel a little inhibited when it comes to picking up the phone' is reluctance, mapped to fear, not sadness.
- [ ] `emotion:test:439` **sadness** -> **fear**: "i always feel a bit awkward when i comment on someone s blog because i invariably go on rabbit trails and feel as though i ve been overstepping myself so i d like to tell you if you find yourself feeling the same way tha"  
  'i always feel a bit awkward when i comment' is awkward, mapped to fear by convention, not sadness.
- [ ] `emotion:test:992` **love** -> **sadness**: "i do feel terribly remourseful that i didnt stay faithful to my plans and get him sooner"  
  'terribly remourseful that i didnt stay faithful to my plans' is remorse, i.e. sadness; 'faithful' is not love.

## sst2 (9 rows)

- [ ] `sst2:validation:282` **positive** -> **negative**: "while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer"  
  The concession 'while there's something intrinsically funny' is overridden by the verdict clause 'has little else to offer', which is a pan.
- [ ] `sst2:validation:519` **negative** -> **positive**: "moretti 's compelling anatomy of grief and the difficult process of adapting to loss ."  
  'compelling anatomy of grief' praises the film; the grim subject ('grief', 'loss') is the mood of the material, not the writer's verdict.
- [ ] `sst2:validation:656` **positive** -> **negative**: "so much facile technique , such cute ideas , so little movie ."  
  'so much facile technique ... so little movie' is a dismissal, with 'facile' and 'cute' as faint praise undercut by the punchline.
- [ ] `sst2:validation:95` **negative** -> **positive**: "this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms ."  
  'this riveting ... moral suspense story' is clear praise; 'ugly' describes the film's subject (racial prejudice), not the film.
- [ ] `sst2:validation:501` **positive** -> **negative**: "harrison 's flowers puts its heart in the right place , but its brains are in no particular place at all ."  
  The 'but' clause 'its brains are in no particular place at all' carries the verdict, overriding the concession 'heart in the right place'.
- [ ] `sst2:validation:850` **positive** -> **negative**: "miller is playing so free with emotions , and the fact that children are hostages to fortune , that he makes the audience hostage to his swaggering affectation of seriousness ."  
  'makes the audience hostage to his swaggering affectation of seriousness' condemns the director as manipulative and pretentious.
- [ ] `sst2:validation:699` **positive** -> **negative**: "... routine , harmless diversion and little else ."  
  'routine, harmless diversion and little else' is dismissive faint praise, which the guidelines explicitly call negative.
- [ ] `sst2:validation:271` **positive** -> **negative**: "as unseemly as its title suggests ."  
  'as unseemly as its title suggests' is a pejorative verdict on the film with no positive counterweight.
- [ ] `sst2:validation:749` **positive** -> **negative**: "a working class `` us vs. them '' opera that leaves no heartstring untugged and no liberal cause unplundered ."  
  'leaves no heartstring untugged and no liberal cause unplundered' is sarcasm accusing the film of shameless manipulation and preachiness, with 'unplundered' plainly pejorative.

## trec (3 rows)

- [ ] `trec:test:190` **ENTY** -> **NUM**: "What is the sales tax in Minnesota ?"  
  'the sales tax in Minnesota' is answered by a percentage, and percentages are NUM under the guidelines.
- [ ] `trec:test:99` **ENTY** -> **NUM**: "What is the longest major league baseball-winning streak ?"  
  'the longest ... winning streak' is answered by a count of games, a number, so NUM rather than ENTY.
- [ ] `trec:test:223` **ENTY** -> **NUM**: "What is the electrical output in Madrid , Spain ?"  
  'the electrical output in Madrid' asks for a voltage or amount of power, i.e. a number with units, which is NUM.

