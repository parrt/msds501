import pandas as pd

df = None


def setup_module():
    global df
    if df is None:
        df = pd.read_feather('enron.feather')


def test_overall_stats():
    global df
    assert len(df) == 2496625
    assert len(df['MailID'].unique()) == 347731
    assert len(df['Date'].unique()) == 1187
    assert len(df['From'].unique()) == 6286
    assert len(df['To'].unique()) == 18814
    assert sum(df['Recipients']) == 254603223
    assert len(df['Subject'].unique()) == 104834
    assert len(df['filename'].unique()) == 347731


def test_addrs():
    global df
    assert sum(df['From'].str.contains('@')) == 0
    assert sum(df['From'].str.contains("'")) == 0
    assert sum(df['From'].str.contains("<")) == 0
    assert sum(df['From'].str.contains(">")) == 0
    assert sum(df['From'].str.contains('.')) == 2496625
    assert sum(df['From'].str.contains("-")) == 4486
    assert sum(df['To'].str.contains('@')) == 0
    assert sum(df['To'].str.contains("'")) == 0
    assert sum(df['To'].str.contains("<")) == 0
    assert sum(df['To'].str.contains(">")) == 0
    assert sum(df['To'].str.contains('.')) == 2496625
    assert sum(df['To'].str.contains("-")) == 18032


def test_lavorato_filenames():
    global df
    assert sum(df['filename'].str.startswith("lavorato-j/")) == 14556
    assert sum(df['filename'].str.startswith("lay-k/")) == 19075


def test_kay_mann():
    global df
    expected = ['a..robison', 'ace.roman', 'adriana.wynn', 'al.larsen', 'alan.aronowitz',
                'alan.larsen', 'alice.wright', 'andrew.edison', 'andrew.ralston',
                'andy.edison', 'angela.davis', 'ann.white', 'anne.koehler',
                'arshak.sarkissian', 'b..hearn', 'barbara.gray', 'barton.clark',
                'becky.spencer', 'ben.jacoby', 'bill.fox', 'bill.williams',
                'billy.lemmons', 'bob.carter', 'bob.licato', 'body.shop', 'brad.morse',
                'brenda.bonhame', 'brett.wiggs', 'brian.barto', 'brian.hulse',
                'brian.kerrigan', 'brian.redmond', 'bryan.garrett', 'c..koehler',
                'campbell', 'carl.tricoli', 'carlos.sole', 'carol.clair', 'carol.st.',
                'caroline.abramo', 'carolyn.george', 'carolyn.graham', 'catherine.clark',
                'charles.vetters', 'chauncey.hood', 'cheryl.costa', 'cheryl.lindeman',
                'cheryl.lipshutz', 'chip.schneider', 'chris.booth', 'chris.gaffney',
                'chris.germany', 'chris.herron', 'christi.nicolay', 'christian.yoder',
                'christina.valdez', 'christopher.calger', 'christy.chapman',
                'claudette.harvey', 'clement.abrams', 'clickathomepilot2', 'clint.shay',
                'community-relations', 'community_relations', 'communityrelations',
                'corry.bentley', 'cynthia.harkness', 'dale.rasmussen', 'dan.lyons',
                'daniel.rogers', 'dave.kellermeyer', 'david.bargainer', 'david.fairley',
                'david.leboe', 'david.lund', 'david.marks', 'david.marshall',
                'david.portz', 'dean.russell', 'deb.korkmas', 'debbie.chance', 'deberry',
                'deborah.culver', 'debra.perlingiere', 'dina.snow', 'don.miller',
                'donald.solomon', 'drew.fossum', 'e..dickson', 'e..jones', 'e..keller',
                'ed.dannhaus', 'ed.iii', 'ed.mcmichael', 'edith.cross', 'edward.sacks',
                'elizabeth.labanowski', 'elizabeth.sager', 'eric.booth', 'eric.boyt',
                'eric.ledain', 'eric.raab', 'ernie', 'felicia.doan', 'frank.sayre',
                'fred.kelly', 'fred.mitro', 'g..bushman', 'gail.brownfeld', 'gail.tholen',
                'gareth.bahlmann', 'gautam.gupta', 'gdavis2', 'geneva.davis',
                'geneva.holland', 'genia.fitzgerald', 'georgia.fogo', 'gerald.nemec',
                'geriann.warner', 'gloria.cruz', 'gracie.presas', 'greg.johnston',
                'greg.krause', 'gregg.penman', 'h..moore', 'harlan.murphy',
                'harry.collins', 'heather.kroll', 'herman.manis', 'holly.keiser',
                'hotline.isc', 'humberto.cubillos-uejbe', 'ibuyit', 'jader',
                'jake.thomas', 'james.grace', 'james.steffes', 'janelle.scheuer',
                'janet.dietrich', 'janette.elbertson', 'jeff.ader', 'jeff.blumenthal',
                'jeff.slaughter', 'jeffery.ader', 'jeffrey.hodge', 'jeffrey.keenan',
                'jeffrey.miller', 'jim.buerkle', 'jim.gilbert', 'jim.homco', 'joan.quick',
                'joel.ephross', 'john.ayres', 'john.llodra', 'john.moore', 'john.normand',
                'john.novak', 'john.rigby', 'john.schwartzenburg', 'john.viverito',
                'jordan.mintz', 'joseph.deffner', 'joseph.grajewski', 'joshua.wooten',
                'joy.oliver', 'joya.davis', 'juan.jass', 'jude.rolfes', 'judy.nyegaard',
                'julia.murray', 'karen.carter', 'karen.jones', 'kathleen.carnahan',
                'kathleen.clark', 'kathy.mayfield', 'kay.mann', 'kay.young', 'kaye.ellis',
                'kayne.coulter', 'keffer', 'ken.loch', 'kevin.joyce', 'kimberlee.bennick',
                'kortney.brown', 'larry.soderquist', 'laura.luce', 'legal.1', 'legal.4',
                'leslie.hansen', 'linda.noske', 'lisa.alfaro', 'lisa.bills',
                'lisa.mellencamp', 'litigation.ljm', 'lloyd.wantschek', 'lloyd.will',
                'lori.pinder', 'lorie.leigh', 'lou.stoler', 'louis.dicarlo', 'm..presto',
                'marchris.robinson', 'marcus.nettelton', 'margaret.doucette',
                'marie.heard', 'mark.bernstein', 'mark.dobler', 'mark.evans',
                'mark.greenberg', 'mark.haedicke', 'mark.metts', 'mark.taylor',
                'martin.penkwitz', 'mary.cook', 'mary.ruffer', 'mathew.gimble',
                'matt.maxwell', 'matthew.berry', 'matthew.gockerman', 'megan.angelos',
                'michael.brown', 'michelle.cash', 'michelle.hicks', 'michelle.kapfer',
                'mike.coleman', 'mike.miller', 'mitch.robinson', 'n..gray',
                'nancy.corbet', 'ozzie.pagan', 'parking.transportation', 'paul.darmitzel',
                'paul.garcia', 'peggy.banczak', 'perfmgmt', 'peter.anderson', 'peter.del',
                'peter.nassab', 'r..price', 'r..rogers', 'rahil.jafry', 'raimund.grube',
                'randy.pais', 'reagan.rorschach', 'rebecca.mcdonald', 'rebecca.walker',
                'reginald.yancey', 'renee.alfaro', 'reynaldo.garcia', 'rhett.jackson',
                'rhonda.denton', 'richard.leibert', 'richard.sanders', 'richard.vincent',
                'rob.walls', 'robert.sevitz', 'robin.barbe', 'robin.hill', 'roger.balog',
                'roger.ondreko', 'ron.coker', 'ron.tapscott', 'roseann.engeldorf',
                'ross.newlin', 'russell.murrell', 'rusty.stevens', 'ruth.concannon',
                's..presas', 'sam.round', 'sandi.braband', 'sara.shackleton',
                'sarah.wesner', 'scott.churbock', 'scott.dieball', 'scott.healy',
                'scott.laidlaw', 'sean.keenan', 'sheila.tweed', 'shelby.malkemes',
                'sheri.cromwell', 'shirley.oliver', 'stacy.dickson', 'stephanie.panus',
                'stephen.plauche', 'stephen.thome', 'steve.hall', 'steve.hooser',
                'steve.irvin', 'steve.montovano', 'steven.krimsky', 'stuart.zisman',
                'susan.bailey', 'suzanne.adams', 't..hodge', 'taffy.milligan',
                'tammy.brennig', 'tana.jones', 'teresa.callahan', 'terri.austin',
                'theresa.vos', 'theresa.zucha', 'thomas.suffield', 'thompson',
                'timothy.detmering', 'timothy.j.detmering', 'tj.butler', 'tjbutler',
                'tom.callaghan', 'tom.chapman', 'tom.may', 'tracee.bersani',
                'travis.mccullough', 'vanessa.bob', 'ward', 'wayne.gresham',
                'william.fleenor', 'william.jr', 'william.keeney', 'zachary.inman']
    df_ = df[df['From'] == 'kay.mann']
    assert len(df_) == 15989
    assert sum(df_['Recipients']) == 36949
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
    assert len(df_) == 216
    assert sum(df_['Recipients']) == 14720
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
                'robert.johnston', 'robert.saltiel', 'robert.smith', 'roberto.volonte',
                'rod.williams', 'rodney.derbigny', 'rosalee.fleming', 'russell.diamond',
                'ruth.brown', 'ryan.seleznov', 's..presas', 's..smith', 'saima.qadir',
                'sally.beck', 'sally.keepers', 'sandra.lighthill', 'sarah.novosel',
                'scott.affelt', 'scott.vonderheide', 'sean.long', 'sean.riordan',
                'sean.zurbrick', 'shari.thompson', 'sheila.jones', 'shelley.farias',
                'shelley.johnson', 'shelly.mansfield', 'sherri.sera', 'sherry.butler',
                'sherryl.stone', 'shona.wilson', 'simone.la', 'simone.rose',
                'sophie.patel', 'stacy.walker', 'stanley.horton', 'stephen.perich',
                'steve.iyer', 'steve.montovano', 'steven.kean', 'suketu.patel',
                'sunie.ferrington', 'susan.poole', 'susan.skarness', 'suzanne.adams',
                'suzanne.danz', 'sylvia.barnes', 'taria.reed', 'terrance.devereaux',
                'terrie.james', 'theresa.connor-smith', 'thomas.kalb', 'thomas.moore',
                'tim.despain', 'timothy.hubbard', 'timothy.vail', 'tj.butler',
                'todd.renaud', 'tom.chapman', 'tom.donohoe', 'tori.wells',
                'tracey.kozadinos', 'tracy.ralston', 'traylor', 'treasa.kirby',
                'twanda.sweet', 'v..monaghan', 'v.rao', 'vanessa.groscrand',
                'velvet.sugarek', 'vera.jones', 'veronica.parra', 'vince.kaminski',
                'vincent.wagner', 'virginia.cavazos', 'vridhay.mathias', 'w..pereira',
                'wade.cline', 'william.bradford', 'williamson', 'wilma.williams',
                'wilson', 'wilson.kriegel', 'winifred.isaac', 'xafira.mendonsa',
                'xiaowu.huang', 'zach.moring', 'zachary.streight']
    df_ = df[df['To'] == 'kenneth.lay']
    assert len(df_) == 3344
    assert sorted(df_['From'].unique()) == sorted(expected)
