import pandas as pd

df = None

def setup_module():
    global df
    if df is None:
        df = pd.read_feather('enron.feather')


def test_overall_stats():
    global df
    assert len(df)==2_499_216
    assert len(df['MailID'].unique())==349849
    assert len(df['Date'].unique())==1187
    assert len(df['From'].unique())==6318
    assert len(df['To'].unique())==18893
    assert sum(df['Recipients'])==254_654_980
    assert len(df['Subject'].unique())==105263
    assert len(df['filename'].unique())==349849


def test_addrs():
    global df
    assert sum(df['From'].str.contains('@'))==0
    assert sum(df['From'].str.contains("'"))==0
    assert sum(df['From'].str.contains("<"))==0
    assert sum(df['From'].str.contains(">"))==0
    assert sum(df['From'].str.contains('.'))==2499216
    assert sum(df['From'].str.contains("-"))==4554
    assert sum(df['To'].str.contains('@'))==0
    assert sum(df['To'].str.contains("'"))==0
    assert sum(df['To'].str.contains("<"))==0
    assert sum(df['To'].str.contains(">"))==0
    assert sum(df['To'].str.contains('.'))==2499216
    assert sum(df['To'].str.contains("-"))==18035


def test_lavorato_filenames():
    global df
    assert sum(df['filename'].str.startswith("lavorato-j/"))==14560
    assert sum(df['filename'].str.startswith("lay-k/"))==19085


def test_kay_mann():
    global df
    expected = ['susan.bailey', 'gerald.nemec', 'e..dickson', 'marie.heard',
                'stephanie.panus', 'ed.mcmichael', 'chris.germany', 'eric.boyt', 'r..price',
                'ruth.concannon', 'kay.mann', 'e..keller', 'paul.darmitzel', 'robin.barbe',
                'mark.haedicke', 'dan.lyons', 't..hodge', 'elizabeth.sager', 'sheila.tweed',
                'suzanne.adams', 'carol.st.', 'leslie.hansen', 'david.portz',
                'reagan.rorschach', 'herman.manis', 'lisa.bills', 'carlos.sole',
                'john.schwartzenburg', 'stephen.thome', 'kathleen.carnahan', 'rhett.jackson',
                'chris.booth', 'jeffrey.hodge', 'ann.white', 'chip.schneider', 'ben.jacoby',
                'margaret.doucette', 'john.moore', 'roseann.engeldorf', 'william.fleenor',
                'mitch.robinson', 'fred.mitro', 'karen.jones', 'jake.thomas',
                'dale.rasmussen', 'gregg.penman', 'catherine.clark', 'becky.spencer',
                'barbara.gray', 'john.rigby', 'ed.iii', 'vanessa.bob', 'bob.carter',
                'heather.kroll', 'ozzie.pagan', 'lorie.leigh', 'barton.clark',
                'matthew.gockerman', 'david.fairley', 'lloyd.will', 'christi.nicolay',
                'jeff.ader', 'mark.bernstein', 'janette.elbertson', 'joshua.wooten',
                'scott.laidlaw', 'steven.krimsky', 'tj.butler', 'greg.krause',
                'robert.sevitz', 'tjbutler', 'renee.alfaro', 'brian.barto', 'randy.pais',
                'body.shop', 'stuart.zisman', 'matt.maxwell', 'scott.dieball',
                'james.steffes', 'geriann.warner', 'marchris.robinson', 'steve.montovano',
                'lisa.mellencamp', 'chauncey.hood', 'christy.chapman', 'rusty.stevens',
                'jeffery.ader', 'taffy.milligan', 'caroline.abramo', 'roger.balog',
                'frank.sayre', 'daniel.rogers', 'andrew.ralston', 'kay.young', 'william.jr',
                'shelby.malkemes', 'joseph.grajewski', 'christina.valdez', 'shirley.oliver',
                'travis.mccullough', 'tana.jones', 'claudette.harvey', 'megan.angelos',
                'eric.booth', 'carolyn.george', 'ernie', 'richard.leibert', 'fred.kelly',
                'peter.nassab', 'jude.rolfes', 'david.marshall', 'genia.fitzgerald',
                'rebecca.walker', 'richard.sanders', 'gloria.cruz', 'david.lund', 'ace.roman',
                'ron.tapscott', 'christopher.calger', 'mike.coleman', 'sheri.cromwell',
                'michael.brown', 'janelle.scheuer', 'chris.gaffney', 'tom.may',
                'kayne.coulter', 'alan.larsen', 'roger.ondreko', 'john.ayres', 'joy.oliver',
                'brett.wiggs', 'jeffrey.keenan', 'lisa.alfaro', 'john.novak', 'jim.gilbert',
                'janet.dietrich', 'john.llodra', 'john.normand', 'legal.1', 'david.marks',
                'william.keeney', 'billy.lemmons', 'cheryl.lipshutz', 'peter.anderson',
                'tracee.bersani', 'karen.carter', 'peggy.banczak', 'richard.vincent',
                'don.miller', 'steve.hooser', 'ross.newlin', 'felicia.doan', 'anne.koehler',
                'joseph.deffner', 'mike.miller', 'scott.healy', 'mark.greenberg',
                'judy.nyegaard', 'rebecca.mcdonald', 'hkroll', 'raimund.grube',
                'jeff.slaughter', 'michelle.cash', 'carol.clair', 'community-relations',
                'bill.williams', 'ed.dannhaus', 'julia.murray', 'debra.perlingiere',
                'geneva.davis', 'gdavis2', 'james.grace', 'mark.taylor', 'kathleen.clark',
                'joel.ephross', 'lou.stoler', 'stephen.plauche', 'jader', 'jordan.mintz',
                'sarah.wesner', 'clickathomepilot2', 'edward.sacks', 'perfmgmt',
                'david.leboe', 'cheryl.costa', 'geneva.holland', 'linda.noske', 'deb.korkmas',
                'al.larsen', 'ron.coker', 'gareth.bahlmann', 'tom.chapman', 'sara.shackleton',
                'russell.murrell', 'teresa.callahan', 'martin.penkwitz', 'larry.soderquist',
                'laura.luce', 'brian.kerrigan', 'chris.herron', 'dean.russell',
                'stacy.dickson', 'dina.snow', 'harry.collins', 'sean.keenan', 'terri.austin',
                'gautam.gupta', 'mark.dobler', 'bill.fox', 'humberto.cubillos-uejbe',
                'community_relations', 'kevin.joyce', 'ken.loch', 'timothy.j.detmering',
                'mark.metts', 'timothy.detmering', 'kathy.mayfield', 'michelle.kapfer',
                'matthew.berry', 'joya.davis', 'thomas.suffield', 'steve.irvin', 'bob.licato',
                'eric.ledain', 'greg.johnston', 'juan.jass', 'donald.solomon',
                'debbie.chance', 'carl.tricoli', 'tom.callaghan', 'jeff.blumenthal',
                'steve.hall', 'reynaldo.garcia', 'brian.hulse', 'christian.yoder',
                'rhonda.denton', 'parking.transportation', 'kimberlee.bennick',
                'theresa.vos', 'paul.garcia', 'legal.4', 'jim.buerkle', 'kaye.ellis',
                'gracie.presas', 'mathew.gimble', 'gail.brownfeld', 'brian.redmond',
                'rob.walls', 'ibuyit', 'deborah.culver', 'harlan.murphy', 'sam.round',
                'mary.ruffer', 'david.bargainer', 'lloyd.wantschek', 'mark.evans',
                'gail.tholen', 'sandi.braband', 'nancy.corbet', 'mary.cook', 'edith.cross',
                'jim.homco', 'corry.bentley', 'brad.morse', 'jeffrey.miller',
                'communityrelations', 'alice.wright', 'thompson', 'carolyn.graham',
                'kortney.brown', 'reginald.yancey', 'andrew.edison', 'marcus.nettelton',
                'john.viverito', 'c..koehler', 'michelle.hicks', 'e..jones', 'n..gray',
                'charles.vetters', 'tammy.brennig', 'h..moore', 'rahil.jafry', 'clint.shay',
                'andy.edison', 'dave.kellermeyer', 'scott.churbock', 'litigation.ljm',
                'eric.raab', 'hotline.isc', 'ward', 'robin.hill', 'brenda.bonhame',
                'adriana.wynn', 'bryan.garrett', 'arshak.sarkissian', 's..presas', 'campbell',
                'zachary.inman', 'keffer', 'deberry', 'g..bushman', 'angela.davis',
                'joan.quick', 'holly.keiser', 'theresa.zucha', 'peter.del', 'lori.pinder',
                'b..hearn', 'cynthia.harkness', 'clement.abrams', 'georgia.fogo',
                'drew.fossum', 'elizabeth.labanowski', 'louis.dicarlo', 'm..presto',
                'cheryl.lindeman', 'alan.aronowitz', 'r..rogers', 'a..robison',
                'wayne.gresham']
    df_ = df[df['From'] == 'kay.mann']
    assert len(df_)==15998
    assert sum(df_['Recipients'])==36958
    assert sorted(df_['To'].unique()) == sorted(expected)


def test_tim_johanson():
    global df
    expected = ['allen.cohrs', 'audrey.robertson', 'becki.sans', 'bill.fowler',
                'bob.burleson', 'bob.stevens', 'chris.sebesta', 'chuck.wilkinson',
                'connie.hook', 'courtney.barker', 'dana.jones', 'dave.neubauer',
                'deborah.cappiello', 'don.powell', 'doug.aschwege', 'eric.gadd',
                'frank.oldenhuis', 'frank.semin', 'g..stage', 'gary.spraggins',
                'jan.moore', 'jane.joyce', 'janet.bowers', 'jo.williams', 'jodie.floyd',
                'john.dushinske', 'john.fiscus', 'john.millar', 'john.pritchard',
                'john.williams', 'joni.bollinger', 'julie.mccoy', 'karen.lagerstrom',
                'kay.threet', 'ken.powers', 'kent.miller', 'kevin.hyatt',
                'kimberly.watson', 'l..johnson', 'larry.pavlou', 'larry.swett',
                'laura.lantefield', 'linda.wehring', 'lindy.donoho', 'lisa.valley',
                'loren.penkava', 'lorna.brennan', 'lorraine.lindberg', 'lynn.blair',
                'michelle.lokay', 'mike.barry', 'penny.mccarran', 'pilar.ramirez',
                'preston.roobaert', 'randy.bryan', 'ranelle.paladino', 'reyna.cabrera',
                'richard.riehm', 'roger.westfall', 'sean.bolks', 'stephanie.korbelik',
                'stephen.herber', 'steve.gilbert', 'steve.thomas', 'steve.weller',
                'steven.harris', 'sue.neville', 'susan.wadle', 'theresa.branney',
                'tk.lohman', 'tom.halpin', 'vernon.mercaldo', 'vicki.berg', 'w..mcgowan']
    df_ = df[df['From'] == 'tim.johanson']
    assert len(df_)==216
    assert sum(df_['Recipients'])==14720
    assert sorted(df_['To'].unique()) == sorted(expected)


def test_ken_lay_senders():
    expected = ['40enron', 'a..davis', 'a..hughes', 'a..lindholm', 'a..schroeder',
                'a..shankman', 'aaron.berutti', 'adnan.patel', 'adriana.wynn',
                'agatha.tran', 'alberto.gude', 'amanda.day', 'amita.gosalia', 'amy.lee',
                'anastasia.aourik', 'andrea.yowman', 'andrew.henderson',
                'andrew.kosnaski', 'andrew.parsons', 'andy.blanchard', 'anita.luong',
                'ann.monshaugen', 'antoinette.beale', 'arthur.goldsmith',
                'arthur.ransome', 'ash.menon', 'ashok.mehta', 'aurora.dimacali',
                'awais.omar', 'barbara.paige', 'becky.zikes', 'ben.glisan',
                'benjamin.rogers', 'betty.alexander', 'betty.hanchey', 'betty.tauzier',
                'beverly.stephens', 'billy.dorsey', 'billy.lemmons', 'binkley.oxley',
                'bjorn.hagelmann', 'bobbie.power', 'body.shop', 'bodyshop',
                'bonnie.allen', 'brenda.anderson', 'brent.vasconcellos',
                'brian.hunter-lindsay', 'brian.oxley', 'brian.redmond', 'brian.terp',
                'bridget.maronge', 'bridget.williams', 'britt.davis', 'bryan.seyfried',
                'c..knightstep', 'c..williams', 'calvin.eakins', 'carlos.vicens',
                'cassandra.schultz', 'cassi.wallace', 'cathy.phillips', 'cecil.stinemetz',
                'cedric.burgher', 'chad.corbitt', 'charlene.jackson', 'charlie.graham',
                'chris.abel', 'chris.connelly', 'chris.long', 'chris.thrall',
                'christa.winfrey', 'christie.patrick', 'chuck.johnson', 'cindy.derecskey',
                'cindy.olson', 'cindy.stark', 'clara.carrington', 'clayton.seigle',
                'compensation.executive', 'corry.bentley', 'craig.buehler', 'curly.baca',
                'cynthia.barrow', 'cynthia.boseman-harris', 'cynthia.sandherr',
                'daler.wade', 'dan.ayers', 'dan.leff', 'dan.rittgers',
                'daniel.allegretti', 'danny.mccarty', 'danz', 'david.delainey',
                'david.forster', 'david.haug', 'david.leboe', 'david.oxley',
                'david.patton', 'david.rollins', 'david.tagliarino', 'david.tonsall',
                'david.truncale', 'deane.pierce', 'debbie.beavers', 'debbie.foot',
                'debbie.perrotta', 'debbie.riall', 'delia.walters', 'diana.peters',
                'diane.bazelides', 'diane.eckels', 'donna.fulton', 'donna.muniz',
                'donnis.traylor', 'dorothy.barnes', 'dorothy.dalton', 'dorothy.mccoppin',
                'dorsey', 'doug.leach', 'douglas.huth', 'e..levingston', 'earlene.ackley',
                'eckels', 'ed.robinson', 'elizabeth.labanowski', 'elizabeth.lay',
                'elizabeth.linnell', 'elizabeth.tilney', 'ellen.fowler', 'elliot.mainzer',
                'elyse.kalmans', 'enrique.gimenez', 'enrique.zambrano', 'eric.letke',
                'eric.shaw', 'eric.thode', 'esmeralda.gonzalez', 'fraisy.george',
                'frank.semin', 'fred.philipson', 'gail.kettenbrink', 'gary.buck',
                'gary.choquette', 'gary.fitch', 'gay.mayeux', 'gayla.seiter',
                'gene.humphrey', 'george.wasaff', 'georgene.moore', 'georgia.fogo',
                'georgia.matula', 'gerri.gosnell', 'gil.muhl', 'gillette',
                'ginger.bissey', 'ginger.dernehl', 'ginger.sinclair', 'glenn.sloan',
                'greg.lewis', 'greg.piper', 'greg.whalley', 'griffith.owens',
                'guido.govers', 'gurinder.tamber', 'gwyn.koepke', 'h..boots', 'h..sutter',
                'hannon', 'hardie.davis', 'hasan.kedwaii', 'hattie.carrington',
                'heath.schiesser', 'hughes', 'ilan.caplan', 'ipayit', 'irene.flynn',
                'iris.mack', 'j..anderson', 'j..detmering', 'j..kean', 'j.oxer',
                'jackie.henry', 'jacqueline.coleman', 'jaime.alatorre', 'jaisinghani',
                'james.derrick', 'jana.mills', 'jane.gustafson', 'janet.butler',
                'janet.dietrich', 'janette.elbertson', 'jeff.donahue', 'jeff.mcclellan',
                'jeff.shields', 'jeffrey.keeler', 'jeffrey.mcclellan', 'jeffrey.mcmahon',
                'jeffrey.sherrick', 'jennifer.richard', 'jim.fallon', 'jim.newgard',
                'jim.roth', 'jim.schwieger', 'jitendra.agarwal', 'joannie.williamson',
                'joe.hillings', 'john.ale', 'john.allison', 'john.ambler', 'john.brindle',
                'john.hardy', 'john.lavorato', 'john.sherriff', 'johnnie.nelson',
                'joseph.hirl', 'joseph.nguyen', 'joseph.pestana', 'josh.duncan',
                'judy.knepshield', 'julie.clyatt', 'julie.cobb', 'justin.rostant',
                'jynell.holliday', 'karen.denne', 'katherine.brown', 'kathryn.corbally',
                'kathryn.schultea', 'kathy.dodgen', 'kathy.johnson', 'kathy.mayfield',
                'kathy.mcmahon', 'kathy.ringblom', 'kayla.crenshaw', 'kelly.johnson',
                'kelly.kimberly', 'ken.rice', 'kenneth.lambert', 'kenneth.lay',
                'kenneth.thibodeaux', 'kevin.garland', 'kevin.hannon', 'kevin.hyatt',
                'kevin.jackson', 'khristina.griffin', 'l..wells', 'la.rose',
                'laine.powell', 'lametrice.dopson', 'lance.schuler-legal', 'larry.izzo',
                'larry.kelley', 'larry.taylor', 'laura.valencia', 'lavorato',
                'leann.walton', 'lee.papayoti', 'lenny.hochschild', 'leonardo.pacheco',
                'linda.faircloth', 'linda.robertson', 'lisa.costello', 'lisa.gillette',
                'lisa.hobbs', 'lisa.iannotti', 'liz.taylor', 'lora.sullivan',
                'loretta.brelsford', 'louise.kitchen', 'lucy.ortiz', 'm..gasdia',
                'marge.nadasky', 'marie.newhouse', 'mario.brunasso', 'mark.brand',
                'mark.fereday', 'mark.frevert', 'mark.harada', 'mark.hudgens',
                'mark.koenig', 'mark.lay', 'mark.metts', 'mark.palmer', 'marsha.shepherd',
                'martin.gonzalez', 'marty.sunde', 'mary.clark', 'mary.joyce',
                'marykay.manning', 'matthew.allan', 'maureen.mcvicker', 'maureen.sampson',
                'maxine.levingston', 'melvin.anderson', 'meredith.philipp',
                'michael.flanigan', 'michael.harris', 'michael.hicks', 'michael.horning',
                'michael.krautz', 'michael.mann', 'michael.norris', 'michelle.foust',
                'michelle.hargrave', 'michelle.nelson', 'mike.coleman', 'mike.croucher',
                'mike.mcconnell', 'mike.underwood', 'miriam.brabham', 'missy.stevens',
                'mitesh.master', 'mrudula.gadade', 'nancy.muchmore', 'nicki.daw',
                'nina.garcia', 'no.address', 'noel.ryan', 'norm.spalding',
                'olalekan.oladeji', 'outlook.team', 'p..dupre', 'pat.radford',
                'pat.shortridge', 'patrick', 'paul.murray', 'paula.rieker',
                'peggy.mahoney', 'perfmgmt', 'peter.berger', 'phylis.karas',
                'priya.jaisinghani', 'r..saunders', 'ralph.blakemore', 'raymond.bowen',
                'rebecca.carter', 'rebecca.longoria', 'rebekah.rushing',
                'regina.karsolich', 'rex.rogers', 'rex.shelby', 'rice',
                'richard.orellana', 'richard.shapiro', 'rick.buy', 'rinetia.turner',
                'rita.ramirez', 'rob.bradley', 'robert.davis', 'robert.gerry',
                'robert.johnston', 'robert.jones', 'robert.saltiel', 'robert.smith',
                'roberto.volonte', 'rod.williams', 'rodney.derbigny', 'rosalee.fleming',
                'russell.diamond', 'ruth.brown', 'ryan.seleznov', 's..presas', 's..smith',
                'saima.qadir', 'sally.beck', 'sally.keepers', 'sandra.lighthill',
                'sarah.novosel', 'scott.affelt', 'scott.vonderheide', 'sean.long',
                'sean.riordan', 'sean.zurbrick', 'shari.thompson', 'sheila.jones',
                'shelley.farias', 'shelley.johnson', 'shelly.mansfield', 'sherri.sera',
                'sherry.butler', 'sherryl.stone', 'shona.wilson', 'simone.la',
                'simone.rose', 'sophie.patel', 'stacy.walker', 'stanley.horton',
                'stephen.perich', 'steve.iyer', 'steve.montovano', 'steven.kean',
                'suketu.patel', 'sunie.ferrington', 'susan.poole', 'susan.skarness',
                'suzanne.adams', 'suzanne.danz', 'sylvia.barnes', 'taria.reed',
                'terrance.devereaux', 'terrie.james', 'theresa.connor-smith',
                'thomas.kalb', 'thomas.moore', 'tim.despain', 'timothy.hubbard',
                'timothy.vail', 'tj.butler', 'todd.renaud', 'tom.chapman', 'tom.donohoe',
                'tori.wells', 'tracey.kozadinos', 'tracy.ralston', 'traylor',
                'treasa.kirby', 'twanda.sweet', 'v..monaghan', 'v.rao',
                'vanessa.groscrand', 'velvet.sugarek', 'vera.jones', 'veronica.parra',
                'vince.kaminski', 'vincent.wagner', 'virginia.cavazos', 'vridhay.mathias',
                'w..pereira', 'wade.cline', 'william.bradford', 'williamson',
                'wilma.williams', 'wilson', 'wilson.kriegel', 'winifred.isaac',
                'xafira.mendonsa', 'xiaowu.huang', 'zach.moring', 'zachary.streight']
    df_ = df[df['To'] == 'kenneth.lay']
    assert len(df_)==3345
    assert sorted(df_['From'].unique()) == sorted(expected)

