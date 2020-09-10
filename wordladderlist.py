words = ['abed', 'abet', 'able', 'ably', 'aced', 'aces', 'acid', \
        'acts', 'adds', 'afar', 'agar', 'aged', 'ager', 'ages', \
        'ahem', 'aide', 'aids', 'ails', 'aims', 'airs', 'airy', \
        'alas', 'alee', 'ales', 'alit', 'alls', 'ally', 'aloe', \
        'alow', 'alps', 'also', 'alto', 'alts', 'alum', 'amen', \
        'amid', 'amts', 'anas', 'ands', 'anes', 'anew', 'anil', \
        'anis', 'anon', 'ante', 'anti', 'ants', 'aped', 'apes', \
        'apex', 'apps', 'area', 'ares', 'arid', 'arks', 'arms', \
        'army', 'arts', 'arty', 'asea', 'ashy', 'asks', 'asps', \
        'asse', 'atar', 'atom', 'atop', 'aune', 'aunt', 'aura', \
        'auto', 'aver', 'aves', 'avid', 'avow', 'away', 'awed', \
        'awes', 'awls', 'awns', 'awol', 'awry', 'axed', 'axel', \
        'axes', 'axle', 'axon', 'ayes', 'baal', 'baas', 'baba', \
        'babe', 'babu', 'baby', 'bach', 'back', 'bade', 'bads', \
        'bael', 'baes', 'baff', 'bags', 'bail', 'bait', 'bake', \
        'bald', 'bale', 'balk', 'ball', 'balm', 'bams', 'banc', \
        'band', 'bane', 'bang', 'bank', 'bans', 'baps', 'barb', \
        'bard', 'bare', 'barf', 'bark', 'barm', 'barn', 'bars', \
        'base', 'bash', 'bask', 'bass', 'bast', 'bate', 'bath', \
        'bats', 'batt', 'baud', 'bawd', 'bawl', 'bawn', 'bays', \
        'bead', 'beak', 'beam', 'bean', 'bear', 'beat', 'beau', \
        'beck', 'beds', 'beef', 'been', 'beep', 'beer', 'bees', \
        'beet', 'begs', 'bell', 'bels', 'belt', 'bema', 'bend', \
        'bens', 'bent', 'berg', 'berm', 'best', 'beta', 'beth', \
        'bets', 'bevy', 'bias', 'bibb', 'bibs', 'bice', 'bide', \
        'bids', 'bier', 'biga', 'bigs', 'bike', 'bile', 'bilk', \
        'bill', 'bind', 'bine', 'bing', 'bins', 'bios', 'bird', \
        'birk', 'birl', 'birr', 'bisk', 'bite', 'bits', 'bitt', \
        'blab', 'blae', 'blah', 'blat', 'blaw', 'bleb', 'bled', \
        'blew', 'blin', 'blip', 'blob', 'bloc', 'blog', 'blot', \
        'blow', 'blub', 'blue', 'blur', 'boar', 'boas', 'boat', \
        'bobo', 'bobs', 'bock', 'bode', 'bods', 'body', 'boff', \
        'bogs', 'bogy', 'boho', 'boil', 'bola', 'bold', 'bole', \
        'boll', 'bolo', 'bolt', 'bomb', 'bond', 'bone', 'bong', \
        'bonk', 'bony', 'book', 'boom', 'boon', 'boor', 'boos', \
        'boot', 'bops', 'bora', 'bore', 'bork', 'born', 'bort', \
        'bosh', 'bosk', 'boss', 'bota', 'bote', 'both', 'bots', \
        'boun', 'bout', 'bowl', 'bows', 'boxy', 'boys', 'bozo', \
        'brad', 'brae', 'brag', 'brah', 'bran', 'bras', 'brat', \
        'braw', 'bray', 'bred', 'bren', 'brew', 'brig', 'brim', \
        'brio', 'brit', 'bros', 'brow', 'bruh', 'brut', 'bubo', \
        'bubs', 'buck', 'buds', 'buff', 'bugs', 'buhl', 'bulb', \
        'bulk', 'bull', 'bumf', 'bump', 'bums', 'bung', 'bunk', \
        'bunn', 'buns', 'bunt', 'buoy', 'burb', 'burg', 'burl', \
        'burn', 'burp', 'burr', 'bury', 'bush', 'busk', 'buss', \
        'bust', 'busy', 'buts', 'butt', 'buys', 'byes', 'byre', \
        'byte', 'cabs', 'cack', 'cade', 'cads', 'cafe', 'cage', \
        'cagy', 'cain', 'cake', 'calc', 'calf', 'calk', 'call', \
        'calm', 'calx', 'came', 'cami', 'camo', 'camp', 'cams', \
        'cane', 'cans', 'cant', 'cany', 'cape', 'capo', 'caps', \
        'carb', 'card', 'care', 'cark', 'carl', 'carn', 'carp', \
        'cars', 'cart', 'casa', 'case', 'cash', 'cask', 'cast', \
        'cate', 'cats', 'caul', 'cave', 'cavy', 'caws', 'cays', \
        'cede', 'cees', 'ceil', 'cell', 'cels', 'celt', 'cent', \
        'cere', 'cero', 'cess', 'cete', 'chad', 'chai', 'cham', \
        'chap', 'char', 'chas', 'chat', 'chaw', 'chef', 'cher', \
        'chew', 'chex', 'chia', 'chic', 'chip', 'chis', 'chit', \
        'chop', 'chou', 'chub', 'chug', 'chum', 'ciao', 'cigs', \
        'cine', 'cion', 'circ', 'cist', 'cite', 'cits', 'city', \
        'clad', 'clam', 'clan', 'clap', 'claw', 'clay', 'clef', \
        'clem', 'clew', 'clip', 'clod', 'clog', 'clop', 'clot', \
        'cloy', 'club', 'clue', 'coak', 'coal', 'coat', 'coax', \
        'cobs', 'coca', 'coco', 'coda', 'code', 'cods', 'coed', \
        'cogs', 'coif', 'coil', 'coin', 'coir', 'coke', 'cola', \
        'cold', 'cole', 'colt', 'coly', 'coma', 'comb', 'come', \
        'comp', 'cone', 'conk', 'conn', 'cons', 'cony', 'cook', \
        'cool', 'coom', 'coop', 'coos', 'coot', 'cope', 'cops', \
        'copy', 'cord', 'core', 'corf', 'cork', 'corm', 'corn', \
        'cors', 'cosh', 'cost', 'cosy', 'cote', 'cots', 'coup', \
        'cove', 'cowl', 'cows', 'coxa', 'coys', 'coze', 'cozy', \
        'crab', 'crag', 'cram', 'crap', 'craw', 'cray', 'cred', \
        'crew', 'crib', 'crit', 'croc', 'crop', 'crow', 'crud', \
        'crus', 'crut', 'crux', 'cube', 'cubs', 'cuds', 'cued', \
        'cues', 'cuff', 'cuke', 'cull', 'culm', 'cult', 'cume', \
        'cups', 'curb', 'curd', 'cure', 'curl', 'curn', 'curr', \
        'curs', 'curt', 'cush', 'cusk', 'cusp', 'cuss', 'cute', \
        'cuts', 'cyan', 'cyme', 'cyst', 'dabs', 'dace', 'dada', \
        'dado', 'dads', 'daff', 'daft', 'dags', 'dahs', 'dais', \
        'daks', 'dale', 'dals', 'dame', 'damn', 'damp', 'dams', \
        'dang', 'dank', 'dans', 'daps', 'dare', 'darg', 'dark', \
        'darn', 'dart', 'dash', 'dast', 'data', 'date', 'daub', \
        'dauk', 'dawk', 'dawn', 'daws', 'days', 'daze', 'dead', \
        'deaf', 'deal', 'dean', 'dear', 'debs', 'debt', 'deck', \
        'deco', 'deed', 'deem', 'deen', 'deep', 'deer', 'dees', \
        'deft', 'defy', 'deil', 'dele', 'delf', 'deli', 'dell', \
        'dels', 'deme', 'demo', 'demy', 'dens', 'dent', 'deny', \
        'dere', 'derm', 'dern', 'derp', 'desk', 'deva', 'devs', \
        'dews', 'dewy', 'deys', 'dhal', 'dhow', 'diad', 'dial', \
        'dibs', 'dice', 'dido', 'died', 'dies', 'diet', 'digs', \
        'dike', 'dill', 'dime', 'dims', 'dine', 'ding', 'dins', \
        'dint', 'diol', 'dips', 'dipt', 'dire', 'dirk', 'dirl', \
        'dirt', 'disc', 'dish', 'disk', 'dite', 'dits', 'ditz', \
        'diva', 'dive', 'doat', 'dock', 'dodo', 'doer', 'does', \
        'doff', 'doge', 'dogs', 'doit', 'dojo', 'dole', 'doll', \
        'dols', 'dolt', 'dome', 'doms', 'dona', 'done', 'dons', \
        'doom', 'door', 'dopa', 'dope', 'dops', 'dopy', 'dore', \
        'dorm', 'dorp', 'dorr', 'dors', 'dory', 'dose', 'doss', \
        'dost', 'dote', 'doth', 'dots', 'doty', 'dour', 'dove', \
        'down', 'dows', 'doxy', 'doze', 'dozy', 'drab', 'drag', \
        'dram', 'drat', 'draw', 'dray', 'dree', 'dreg', 'drew', \
        'drib', 'drip', 'drop', 'drub', 'drug', 'drum', 'drys', \
        'duad', 'dual', 'dubs', 'duce', 'duck', 'duct', 'dude', \
        'duds', 'duel', 'dues', 'duet', 'duff', 'dugs', 'duke', \
        'dull', 'duly', 'duma', 'dumb', 'dump', 'dune', 'dung', \
        'dunk', 'duns', 'dunt', 'duos', 'dupe', 'dups', 'dura', \
        'dure', 'dusk', 'dust', 'duty', 'dyad', 'dyed', 'dyer', \
        'dyes', 'dyne', 'each', 'earl', 'earn', 'ears', 'ease', \
        'east', 'easy', 'eath', 'eats', 'eave', 'ebon', 'echo', \
        'echt', 'ecos', 'ecru', 'ecus', 'eddo', 'eddy', 'edge', \
        'edgy', 'edhs', 'edit', 'eels', 'eely', 'egad', 'egal', \
        'eggs', 'eggy', 'egis', 'egos', 'eide', 'eked', 'ekes', \
        'elan', 'elds', 'elks', 'ells', 'elms', 'else', 'elve', \
        'emes', 'emir', 'emit', 'emos', 'emus', 'ends', 'enol', \
        'enow', 'enuf', 'envy', 'eons', 'epee', 'epha', 'epic', \
        'epos', 'equi', 'eras', 'ergo', 'ergs', 'even', 'ever', \
        'eves', 'evil', 'ewer', 'ewes', 'exam', 'exec', 'exes', \
        'exit', 'exon', 'eyed', 'eyen', 'eyer', 'eyes', 'face', \
        'fact', 'fade', 'fado', 'fads', 'fail', 'fain', 'fair', \
        'fake', 'fall', 'falx', 'fame', 'fams', 'fane', 'fang', \
        'fans', 'fard', 'fare', 'farl', 'farm', 'faro', 'fast', \
        'fate', 'fats', 'faun', 'faux', 'fave', 'fawn', 'faze', \
        'feal', 'fear', 'feat', 'feds', 'feed', 'feel', 'fees', \
        'feet', 'fell', 'felt', 'feme', 'fems', 'fend', 'fens', \
        'fere', 'fern', 'fess', 'fest', 'feta', 'fete', 'feud', \
        'fews', 'fiat', 'fibs', 'fice', 'fico', 'fids', 'fief', \
        'fife', 'figs', 'file', 'fill', 'film', 'fils', 'find', \
        'fine', 'fini', 'fink', 'fins', 'fire', 'firm', 'firs', \
        'fisc', 'fish', 'fist', 'fits', 'five', 'fizz', 'flab', \
        'flag', 'flak', 'flam', 'flan', 'flap', 'flat', 'flaw', \
        'flax', 'flay', 'flea', 'fled', 'flee', 'flew', 'flex', \
        'flip', 'flit', 'floc', 'floe', 'flog', 'flop', 'flow', \
        'flub', 'flue', 'flus', 'flux', 'foal', 'foam', 'foes', \
        'fogs', 'fogy', 'fohn', 'foil', 'foin', 'fold', 'folk', \
        'fond', 'font', 'food', 'fool', 'foot', 'fops', 'fora', \
        'ford', 'fore', 'fork', 'form', 'fort', 'foul', 'four', \
        'fowl', 'foxy', 'fozy', 'frag', 'frap', 'frat', 'fray', \
        'free', 'fret', 'frit', 'froe', 'frog', 'from', 'frow', \
        'frum', 'fubs', 'fuci', 'fuel', 'fugs', 'fugu', 'full', \
        'fume', 'fumy', 'fund', 'funk', 'funs', 'furl', 'furs', \
        'fury', 'fuse', 'fuss', 'futz', 'fuze', 'fuzz', 'fyce', \
        'fyke', 'fyrd', 'gabs', 'gaby', 'gads', 'gaff', 'gaga', \
        'gage', 'gags', 'gain', 'gait', 'gala', 'gale', 'gall', \
        'gals', 'game', 'gamp', 'gams', 'gamy', 'gang', 'gaol', \
        'gape', 'gaps', 'garb', 'gare', 'gars', 'gasp', 'gast', \
        'gate', 'gats', 'gaud', 'gaur', 'gave', 'gawk', 'gawp', \
        'gaws', 'gaze', 'gean', 'gear', 'gedd', 'geds', 'geed', \
        'geek', 'gees', 'geld', 'gels', 'gelt', 'gems', 'gena', \
        'gene', 'gens', 'gent', 'genu', 'germ', 'gest', 'geta', \
        'gets', 'geum', 'ghat', 'ghee', 'gibe', 'gibs', 'gifs', \
        'gift', 'gigs', 'gild', 'gill', 'gilt', 'gins', 'gips', \
        'gird', 'girl', 'girt', 'gist', 'gite', 'gits', 'give', \
        'glad', 'glam', 'glee', 'gleg', 'glen', 'glib', 'glim', \
        'glob', 'glom', 'glop', 'glow', 'glue', 'glug', 'glum', \
        'glut', 'gnar', 'gnat', 'gnaw', 'goad', 'goaf', 'goal', \
        'goas', 'goat', 'gobs', 'goby', 'goer', 'gogo', 'gold', \
        'golf', 'gone', 'gong', 'good', 'goof', 'goon', 'goop', \
        'goos', 'gore', 'gorm', 'gorp', 'gory', 'gosh', 'gout', \
        'gowd', 'gown', 'grab', 'grad', 'gram', 'gran', 'gray', \
        'gree', 'grew', 'grey', 'grid', 'grig', 'grim', 'grin', \
        'grip', 'grit', 'grog', 'grok', 'grot', 'grow', 'grub', \
        'grue', 'grum', 'guac', 'guan', 'guar', 'guck', 'guff', \
        'guib', 'gula', 'gulf', 'gull', 'gulp', 'guls', 'gump', \
        'gums', 'guna', 'gunk', 'guns', 'guru', 'gush', 'gust', \
        'guts', 'guys', 'gybe', 'gyms', 'gyre', 'gyro', 'haaf', \
        'haar', 'hack', 'hade', 'hadj', 'haft', 'hags', 'haik', \
        'hail', 'hair', 'haji', 'hajj', 'hajs', 'hake', 'hale', \
        'half', 'hall', 'halm', 'halo', 'halt', 'hame', 'hams', \
        'hand', 'hang', 'hank', 'hant', 'haps', 'hard', 'hare', \
        'hark', 'harm', 'harp', 'hart', 'hash', 'hasp', 'hast', \
        'hate', 'hath', 'hats', 'haul', 'haut', 'have', 'hawk', \
        'haws', 'hays', 'haze', 'hazy', 'head', 'heal', 'heap', \
        'hear', 'heat', 'heck', 'heed', 'heel', 'heer', 'heft', \
        'hehs', 'heir', 'held', 'helm', 'help', 'heme', 'hemi', \
        'hemp', 'hems', 'hens', 'hent', 'herb', 'herd', 'here', \
        'herl', 'herm', 'hern', 'hero', 'hers', 'hest', 'heth', \
        'hewn', 'hews', 'hick', 'hide', 'hied', 'hies', 'high', \
        'hike', 'hill', 'hilt', 'hims', 'hins', 'hint', 'hips', \
        'hire', 'hiss', 'hist', 'hits', 'hive', 'hoar', 'hoax', \
        'hobo', 'hobs', 'hock', 'hods', 'hoed', 'hoer', 'hogg', \
        'hogs', 'hoke', 'hold', 'hole', 'holm', 'holp', 'holt', \
        'holy', 'home', 'homy', 'hone', 'hong', 'honk', 'hons', \
        'hood', 'hoof', 'hook', 'hoop', 'hoot', 'hope', 'hops', \
        'horn', 'hose', 'host', 'hots', 'hour', 'hove', 'howe', \
        'howl', 'hows', 'hoya', 'hoys', 'hubs', 'huck', 'hued', \
        'hues', 'huff', 'huge', 'hugs', 'hula', 'hulk', 'hull', \
        'hump', 'hums', 'hung', 'hunk', 'hunt', 'hurl', 'hurt', \
        'hush', 'husk', 'huts', 'hyla', 'hype', 'hypo', 'hyps', \
        'iamb', 'iced', 'ices', 'icon', 'idea', 'idem', 'ides', \
        'imam', 'inch', 'info', 'inks', 'inky', 'inns', 'ions', \
        'ires', 'irks', 'item', 'jabs', 'jack', 'jade', 'jags', \
        'jail', 'jaks', 'jamb', 'jams', 'jane', 'jape', 'jars', \
        'jass', 'jaws', 'jays', 'jazz', 'jean', 'jeed', 'jeer', \
        'jees', 'jeez', 'jell', 'jerk', 'jess', 'jest', 'jete', \
        'jets', 'jiao', 'jibb', 'jibe', 'jibs', 'jill', 'jilt', \
        'jimp', 'jink', 'jinn', 'jins', 'jinx', 'jiva', 'jive', \
        'jobs', 'jock', 'joes', 'joey', 'jogs', 'john', 'join', \
        'joke', 'jole', 'jolt', 'jook', 'josh', 'joss', 'jots', \
        'jouk', 'jowl', 'jows', 'joys', 'juba', 'jube', 'judo', \
        'jugs', 'juju', 'juke', 'jump', 'junk', 'jury', 'just', \
        'jute', 'juts', 'kagu', 'kail', 'kain', 'kaka', 'kaki', \
        'kale', 'kame', 'kang', 'kaon', 'kaph', 'kava', 'keas', \
        'keck', 'keel', 'keen', 'keep', 'kegs', 'keir', 'kelp', \
        'kelt', 'kemp', 'keno', 'kens', 'kent', 'kepi', 'kept', \
        'kerb', 'kerf', 'kern', 'keta', 'keto', 'keys', 'khan', \
        'khat', 'kibe', 'kick', 'kier', 'kill', 'kiln', 'kilo', \
        'kilt', 'kind', 'kine', 'king', 'kink', 'kino', 'kins', \
        'kips', 'kirk', 'kirn', 'kish', 'kiss', 'kist', 'kite', \
        'kith', 'kits', 'kiva', 'kiwi', 'knap', 'knee', 'knew', \
        'knit', 'knob', 'knop', 'knot', 'know', 'knub', 'knur', \
        'koan', 'koas', 'kobo', 'kobs', 'koel', 'kohl', 'kois', \
        'kola', 'kook', 'koto', 'kris', 'kudu', 'kuru', 'labs', \
        'lace', 'lack', 'lacs', 'lacy', 'lade', 'lads', 'lady', \
        'lags', 'laic', 'laid', 'lain', 'lair', 'lake', 'lakh', \
        'laky', 'lama', 'lamb', 'lame', 'lamp', 'lams', 'land', \
        'lane', 'lang', 'lank', 'laps', 'lard', 'lari', 'lark', \
        'lars', 'lase', 'lash', 'lass', 'last', 'late', 'lath', \
        'lats', 'laud', 'lava', 'lave', 'lavs', 'lawn', 'laws', \
        'lays', 'laze', 'lazy', 'lead', 'leaf', 'leak', 'leal', \
        'lean', 'leap', 'lear', 'leas', 'lech', 'leek', 'leer', \
        'lees', 'leet', 'left', 'legs', 'leis', 'lend', 'leno', \
        'lens', 'lent', 'less', 'lest', 'lets', 'levo', 'levy', \
        'lewd', 'leys', 'liar', 'libs', 'lice', 'lich', 'lick', \
        'lido', 'lids', 'lied', 'lief', 'lien', 'lier', 'lies', \
        'lieu', 'life', 'lift', 'like', 'lilt', 'lily', 'limb', \
        'lime', 'limn', 'limo', 'limp', 'limy', 'line', 'ling', \
        'link', 'lino', 'lins', 'lint', 'lion', 'lips', 'lira', \
        'lire', 'lisp', 'list', 'lite', 'lith', 'lits', 'live', \
        'load', 'loaf', 'loam', 'loan', 'lobe', 'lobs', 'loca', \
        'loch', 'loci', 'lock', 'loco', 'lode', 'loft', 'loge', \
        'logo', 'logs', 'logy', 'loin', 'loll', 'loma', 'lone', \
        'long', 'loof', 'look', 'loom', 'loon', 'loop', 'loos', \
        'loot', 'lope', 'lops', 'lord', 'lore', 'lorn', 'lory', \
        'lose', 'loss', 'lost', 'lota', 'lote', 'loth', 'lots', \
        'loud', 'loup', 'lour', 'lout', 'love', 'lown', 'lows', \
        'luau', 'lube', 'luce', 'luck', 'lude', 'lues', 'luff', \
        'luge', 'lugs', 'lull', 'lulu', 'lump', 'lune', 'lung', \
        'lunk', 'lunt', 'luny', 'lure', 'lurk', 'lush', 'lust', \
        'lute', 'luxe', 'lyes', 'lyre', 'maar', 'mace', 'mach', \
        'mack', 'macs', 'made', 'mads', 'mage', 'mags', 'maid', \
        'mail', 'maim', 'main', 'make', 'mako', 'male', 'mall', \
        'malm', 'malt', 'mama', 'mams', 'mana', 'mane', 'mano', \
        'mans', 'many', 'maps', 'mara', 'marc', 'mare', 'mark', \
        'marl', 'mars', 'mart', 'mash', 'mask', 'mass', 'mast', \
        'mate', 'math', 'mats', 'matt', 'maud', 'maul', 'maws', \
        'maxi', 'maya', 'mayo', 'mays', 'maze', 'mazy', 'mead', \
        'meal', 'mean', 'mear', 'meat', 'meds', 'meed', 'meek', \
        'meet', 'megs', 'meld', 'mell', 'melt', 'meme', 'memo', \
        'mend', 'menu', 'meow', 'mere', 'merk', 'merl', 'mesa', \
        'mesh', 'mess', 'meta', 'mete', 'meth', 'mewl', 'mews', \
        'mhos', 'mica', 'mice', 'mics', 'midi', 'mids', 'mien', \
        'miff', 'mike', 'mild', 'mile', 'milf', 'milk', 'mill', \
        'milo', 'mils', 'milt', 'mime', 'mina', 'mind', 'mine', \
        'mini', 'mink', 'mint', 'minx', 'mire', 'mirk', 'miry', \
        'mise', 'miso', 'miss', 'mist', 'mite', 'mitt', 'mixt', \
        'moan', 'moas', 'moat', 'mobs', 'mock', 'mode', 'mods', \
        'mogs', 'moil', 'mojo', 'mola', 'mold', 'mole', 'moll', \
        'mols', 'molt', 'moly', 'mome', 'moms', 'mong', 'monk', \
        'mono', 'mons', 'mony', 'mood', 'mook', 'moon', 'moor', \
        'moos', 'moot', 'mope', 'mops', 'mopy', 'mora', 'more', \
        'morn', 'mort', 'mosh', 'moss', 'most', 'mote', 'moth', \
        'moto', 'mots', 'moue', 'move', 'mowe', 'mown', 'mows', \
        'moxa', 'much', 'muck', 'muds', 'mugs', 'mule', 'mull', \
        'mumm', 'mump', 'mums', 'mumu', 'mung', 'muon', 'mure', \
        'murk', 'muse', 'mush', 'musk', 'muss', 'must', 'mute', \
        'mutt', 'myth', 'naan', 'nabs', 'nada', 'nags', 'naif', \
        'nail', 'name', 'nana', 'nano', 'nans', 'naos', 'napa', \
        'nape', 'naps', 'narc', 'nard', 'nark', 'nary', 'nave', \
        'navy', 'nays', 'neap', 'near', 'neat', 'neck', 'need', \
        'nefs', 'negs', 'nemo', 'neon', 'nerd', 'ness', 'nest', \
        'nets', 'neve', 'news', 'newt', 'next', 'nibs', 'nice', \
        'nick', 'nide', 'nidi', 'nigh', 'nill', 'nils', 'nims', \
        'nina', 'nine', 'nisi', 'nite', 'nits', 'nobs', 'nock', \
        'node', 'nods', 'noes', 'nogs', 'noil', 'noir', 'noma', \
        'nome', 'none', 'noob', 'nook', 'noon', 'nope', 'nori', \
        'norm', 'nose', 'nosh', 'nosy', 'nota', 'note', 'noun', \
        'nous', 'nova', 'nows', 'nowt', 'nubs', 'nude', 'nuke', \
        'null', 'numb', 'nuns', 'nurl', 'nuts', 'oafs', 'oaks', \
        'oars', 'oary', 'oast', 'oath', 'oats', 'obey', 'obis', \
        'obit', 'oboe', 'obol', 'odds', 'odea', 'odes', 'odic', \
        'odor', 'offs', 'ogam', 'ogee', 'ogle', 'ogre', 'ohms', \
        'oils', 'oily', 'oink', 'okay', 'okra', 'olds', 'oldy', \
        'olea', 'oleo', 'olio', 'olla', 'omen', 'omit', 'once', \
        'only', 'onto', 'onus', 'onyx', 'oohs', 'oops', 'ooze', \
        'oozy', 'opah', 'opal', 'oped', 'open', 'opes', 'opry', \
        'opts', 'opus', 'orad', 'oral', 'oras', 'orbs', 'orca', \
        'orcs', 'ores', 'orgy', 'orle', 'orlo', 'orts', 'oryx', \
        'orzo', 'ossa', 'otic', 'otto', 'ouch', 'ouis', 'ours', \
        'oust', 'outs', 'ouzo', 'oval', 'oven', 'over', 'ovum', \
        'owed', 'owes', 'owls', 'owns', 'owse', 'oxen', 'oxes', \
        'oxid', 'oyer', 'oyes', 'oyez', 'paca', 'pace', 'pack', \
        'pacs', 'pact', 'pads', 'page', 'paid', 'pail', 'pain', \
        'pair', 'pale', 'pall', 'palm', 'palp', 'pals', 'paly', \
        'pams', 'pane', 'pang', 'pans', 'pant', 'papa', 'paps', \
        'para', 'pard', 'pare', 'park', 'parr', 'pars', 'part', \
        'pash', 'pass', 'past', 'pate', 'path', 'pats', 'pave', \
        'pawl', 'pawn', 'paws', 'pays', 'peak', 'peal', 'pean', \
        'pear', 'peas', 'peat', 'peba', 'peck', 'pecs', 'peed', \
        'peek', 'peel', 'peen', 'peep', 'peer', 'pees', 'pegs', \
        'peke', 'pelf', 'pelt', 'pend', 'pens', 'pent', 'peon', \
        'pepo', 'peps', 'perc', 'pere', 'peri', 'perk', 'perm', \
        'perp', 'pert', 'peso', 'pest', 'pets', 'pews', 'phat', \
        'phew', 'phis', 'phon', 'phot', 'pial', 'pian', 'pica', \
        'pice', 'pick', 'pics', 'pied', 'pier', 'pies', 'piet', \
        'pigs', 'pika', 'pike', 'pile', 'pill', 'pimp', 'pina', \
        'pine', 'ping', 'pink', 'pins', 'pint', 'piny', 'pion', \
        'pipe', 'pips', 'pipy', 'pirn', 'pise', 'pish', 'pita', \
        'pith', 'pits', 'pity', 'pixy', 'plan', 'plat', 'play', \
        'plea', 'pleb', 'pled', 'plod', 'plop', 'plot', 'plow', \
        'ploy', 'plug', 'plum', 'plus', 'pock', 'poco', 'pods', \
        'poem', 'poet', 'pogy', 'pois', 'poke', 'poky', 'pole', \
        'poll', 'polo', 'pols', 'poly', 'pome', 'pomp', 'pond', \
        'pone', 'pong', 'pons', 'pony', 'poof', 'pooh', 'pool', \
        'poon', 'poop', 'poor', 'poos', 'pope', 'pops', 'pore', \
        'pork', 'porn', 'port', 'pose', 'posh', 'post', 'posy', \
        'pots', 'pouf', 'pour', 'pout', 'pows', 'prad', 'pram', \
        'prat', 'pray', 'prep', 'prey', 'prez', 'prie', 'prig', \
        'prim', 'proa', 'prob', 'prof', 'prog', 'prom', 'prop', \
        'pros', 'prow', 'pubs', 'puce', 'puck', 'puds', 'puff', \
        'pugh', 'pugs', 'puka', 'puke', 'puky', 'pule', 'pull', \
        'pulp', 'puls', 'pulu', 'puma', 'pump', 'pung', 'punk', \
        'puns', 'punt', 'puny', 'pupa', 'pups', 'pure', 'puri', \
        'purl', 'purr', 'purs', 'push', 'puss', 'puts', 'putt', \
        'pyes', 'pyre', 'pyro', 'qats', 'quad', 'rabs', 'race', \
        'rack', 'racy', 'rads', 'raff', 'raft', 'raga', 'rage', \
        'rags', 'ragu', 'raid', 'rail', 'rain', 'rais', 'raja', \
        'rake', 'rale', 'rami', 'ramp', 'rams', 'rand', 'rang', \
        'rani', 'rank', 'rant', 'raps', 'rapt', 'rare', 'rase', \
        'rash', 'rasp', 'rate', 'rath', 'rats', 'rave', 'raws', \
        'rays', 'raze', 'read', 'real', 'ream', 'reap', 'rear', \
        'rebs', 'reck', 'recs', 'rede', 'redo', 'reds', 'reed', \
        'reef', 'reek', 'reel', 'rees', 'refs', 'reft', 'regs', \
        'rein', 'reis', 'rely', 'rend', 'rent', 'repo', 'reps', \
        'rest', 'rete', 'rets', 'revs', 'rhea', 'rhos', 'rial', \
        'ribs', 'rice', 'rich', 'rick', 'ride', 'rids', 'rife', \
        'riff', 'rift', 'rigs', 'rile', 'rill', 'rime', 'rims', \
        'rimy', 'rind', 'ring', 'rink', 'riot', 'ripe', 'rips', \
        'rise', 'risk', 'rite', 'ritz', 'rive', 'road', 'roam', \
        'roan', 'roar', 'robe', 'robs', 'rock', 'rocs', 'rode', \
        'rods', 'roes', 'roil', 'roke', 'role', 'roll', 'romp', \
        'rood', 'roof', 'rook', 'room', 'root', 'rope', 'ropy', \
        'rose', 'ross', 'rosy', 'rota', 'rote', 'roto', 'rots', \
        'roue', 'roup', 'rout', 'roux', 'rove', 'rows', 'rube', \
        'rubs', 'ruby', 'ruck', 'rudd', 'rude', 'rued', 'ruer', \
        'rues', 'ruff', 'ruga', 'rugs', 'ruin', 'rule', 'rump', \
        'rums', 'rune', 'rung', 'runs', 'runt', 'ruse', 'rush', \
        'rusk', 'rust', 'ruth', 'ruts', 'ryes', 'rynd', 'ryot', \
        'sack', 'sacs', 'sads', 'safe', 'saga', 'sage', 'sago', \
        'sags', 'said', 'sail', 'sain', 'sake', 'saki', 'sale', \
        'salp', 'sals', 'salt', 'same', 'samp', 'sand', 'sane', \
        'sang', 'sank', 'sans', 'saps', 'sard', 'sari', 'sark', \
        'sash', 'sass', 'sate', 'sats', 'save', 'sawm', 'sawn', \
        'saws', 'says', 'scab', 'scad', 'scag', 'scam', 'scan', \
        'scar', 'scat', 'scot', 'scow', 'scud', 'scum', 'scup', \
        'scut', 'seal', 'seam', 'sear', 'seas', 'seat', 'secs', \
        'sect', 'seed', 'seek', 'seel', 'seem', 'seen', 'seep', \
        'seer', 'sees', 'sego', 'self', 'sell', 'seme', 'semi', \
        'send', 'sent', 'sept', 'sera', 'sere', 'serf', 'seta', \
        'sets', 'sett', 'sewn', 'sews', 'sext', 'sexy', 'shad', \
        'shag', 'shah', 'sham', 'shaw', 'shay', 'shea', 'shed', \
        'shes', 'shew', 'shim', 'shin', 'ship', 'shiv', 'shod', \
        'shoe', 'shog', 'shoo', 'shop', 'shot', 'show', 'shun', \
        'shut', 'shwa', 'sial', 'sibs', 'sice', 'sick', 'sics', \
        'side', 'sift', 'sign', 'sike', 'sild', 'silk', 'sill', \
        'silo', 'silt', 'sima', 'simp', 'sine', 'sing', 'sink', \
        'sins', 'sipe', 'sips', 'sire', 'sirs', 'site', 'sith', \
        'sits', 'situ', 'size', 'sizy', 'skag', 'skas', 'skat', \
        'skee', 'skeg', 'skep', 'skew', 'skid', 'skim', 'skin', \
        'skip', 'skis', 'skit', 'slab', 'slag', 'slam', 'slap', \
        'slat', 'slaw', 'slay', 'sled', 'slew', 'sley', 'slid', \
        'slim', 'slip', 'slit', 'slob', 'sloe', 'slog', 'slop', \
        'slot', 'slow', 'slub', 'slue', 'slug', 'slum', 'slur', \
        'smew', 'smit', 'smog', 'smug', 'smut', 'snag', 'snap', \
        'snib', 'snip', 'snit', 'snob', 'snod', 'snog', 'snot', \
        'snow', 'snub', 'snug', 'soak', 'soap', 'soar', 'sobs', \
        'sock', 'socs', 'soda', 'sods', 'sofa', 'soft', 'soil', \
        'soke', 'sola', 'sold', 'sole', 'soli', 'solo', 'sols', \
        'soma', 'some', 'sone', 'song', 'sons', 'sook', 'soon', \
        'soot', 'sopa', 'soph', 'sops', 'sora', 'sorb', 'sord', \
        'sore', 'sori', 'sort', 'soul', 'soup', 'sour', 'sous', \
        'sown', 'sows', 'soys', 'spae', 'span', 'spas', 'spat', \
        'spay', 'spec', 'sped', 'spew', 'spin', 'spit', 'spiv', \
        'spot', 'spry', 'spud', 'spue', 'spun', 'spur', 'stab', \
        'stag', 'star', 'stat', 'staw', 'stay', 'stem', 'step', \
        'stet', 'stew', 'stir', 'stob', 'stop', 'stot', 'stow', \
        'stub', 'stud', 'stum', 'stun', 'stye', 'subs', 'such', \
        'suck', 'sudd', 'suds', 'sued', 'suer', 'sues', 'suet', \
        'suit', 'sulk', 'sumo', 'sump', 'sums', 'sung', 'sunk', \
        'suns', 'supe', 'sups', 'sura', 'surd', 'sure', 'surf', \
        'suss', 'swab', 'swag', 'swam', 'swan', 'swap', 'swat', \
        'sway', 'swig', 'swim', 'swob', 'swop', 'swot', 'swum', \
        'syke', 'syne', 'tabi', 'tabs', 'tabu', 'tace', 'tach', \
        'tack', 'taco', 'tact', 'tads', 'tael', 'tags', 'tahr', \
        'tail', 'tain', 'take', 'talc', 'tale', 'tali', 'talk', \
        'tall', 'tame', 'tamp', 'tams', 'tang', 'tank', 'tans', \
        'tapa', 'tape', 'taps', 'tare', 'tarn', 'taro', 'tarp', \
        'tars', 'tart', 'tase', 'task', 'tats', 'taus', 'taut', \
        'taws', 'taxa', 'taxi', 'taze', 'teak', 'teal', 'team', \
        'tear', 'teas', 'teat', 'tech', 'tecs', 'teds', 'teed', \
        'teel', 'teem', 'teen', 'tees', 'tegs', 'teil', 'tele', \
        'tell', 'temp', 'tend', 'tens', 'tent', 'term', 'tern', \
        'test', 'text', 'than', 'thar', 'that', 'thaw', 'thee', \
        'them', 'then', 'thew', 'they', 'thin', 'this', 'thou', \
        'thro', 'thru', 'thud', 'thug', 'thus', 'tick', 'tics', \
        'tide', 'tidy', 'tied', 'tier', 'ties', 'tiff', 'tike', \
        'tiki', 'tile', 'till', 'tils', 'tilt', 'time', 'tine', \
        'ting', 'tins', 'tint', 'tiny', 'tipi', 'tips', 'tire', \
        'tirl', 'tiro', 'titi', 'toad', 'toby', 'tods', 'tody', \
        'toed', 'toes', 'toff', 'toft', 'tofu', 'toga', 'togs', \
        'toil', 'toke', 'told', 'tole', 'toll', 'tolu', 'tomb', \
        'tome', 'toms', 'tone', 'tong', 'tonk', 'tons', 'tony', \
        'took', 'tool', 'toom', 'toon', 'toot', 'tope', 'topi', \
        'tops', 'torc', 'tore', 'tori', 'torn', 'toro', 'tors', \
        'tort', 'tosh', 'toss', 'tost', 'tote', 'tots', 'tour', \
        'tout', 'town', 'tows', 'towy', 'toys', 'tram', 'trap', \
        'tray', 'tree', 'tref', 'trek', 'tret', 'trey', 'trig', \
        'trim', 'trio', 'trip', 'trod', 'trot', 'trow', 'tsar', \
        'tuba', 'tube', 'tubs', 'tuck', 'tufa', 'tuff', 'tuft', \
        'tugs', 'tule', 'tump', 'tums', 'tuna', 'tune', 'tuns', \
        'tups', 'turd', 'turf', 'turn', 'tush', 'tusk', 'tuts', \
        'tutu', 'twas', 'twee', 'twig', 'twin', 'twit', 'twos', \
        'tyke', 'tyne', 'type', 'tyre', 'uber', 'udon', 'ughs', \
        'ugly', 'ukes', 'vaca', 'vacs', 'vail', 'vain', 'vair', \
        'vale', 'vamp', 'vane', 'vang', 'vans', 'vape', 'vary', \
        'vasa', 'vase', 'vast', 'vats', 'veal', 'veep', 'veer', \
        'vees', 'vegs', 'veil', 'vein', 'vela', 'veld', 'vena', \
        'vend', 'vent', 'vera', 'verb', 'vert', 'very', 'vest', \
        'veto', 'vets', 'vial', 'vias', 'vibe', 'vice', 'vide', \
        'vied', 'vies', 'view', 'vigs', 'vile', 'vill', 'vims', \
        'vina', 'vine', 'vino', 'viny', 'viol', 'visa', 'vise', \
        'vita', 'viva', 'vlog', 'void', 'vole', 'volt', 'vote', \
        'vows', 'wack', 'wade', 'wads', 'wady', 'waft', 'wage', \
        'wags', 'waif', 'wail', 'wain', 'wait', 'wake', 'wale', \
        'walk', 'wall', 'wand', 'wane', 'wans', 'want', 'wany', \
        'waps', 'ward', 'ware', 'warm', 'warn', 'warp', 'wars', \
        'wart', 'wary', 'wash', 'wast', 'watt', 'wave', 'wavy', \
        'waxy', 'ways', 'weak', 'weal', 'wean', 'wear', 'webs', \
        'weds', 'weed', 'week', 'ween', 'weep', 'weft', 'weir', \
        'weld', 'well', 'welt', 'wend', 'wens', 'went', 'wept', \
        'were', 'wert', 'west', 'wets', 'weys', 'wham', 'whap', \
        'what', 'whee', 'when', 'whet', 'whew', 'whey', 'whid', \
        'whig', 'whim', 'whin', 'whip', 'whir', 'whit', 'whiz', \
        'whoa', 'whom', 'wick', 'wide', 'wife', 'wigs', 'wiki', \
        'wild', 'wile', 'will', 'wilt', 'wily', 'wimp', 'wind', \
        'wine', 'wing', 'wink', 'wino', 'wins', 'winy', 'wipe', \
        'wire', 'wiry', 'wise', 'wish', 'wisp', 'wist', 'wite', \
        'with', 'wits', 'wive', 'woad', 'woes', 'woke', 'woks', \
        'wold', 'wolf', 'womb', 'wonk', 'wons', 'wont', 'wood', \
        'woof', 'wool', 'woos', 'woot', 'word', 'wore', 'work', \
        'worm', 'worn', 'wort', 'wost', 'wove', 'wows', 'wrap', \
        'wren', 'writ', 'wuss', 'wyes', 'wynd', 'wyte', 'xyst', \
        'yack', 'yaks', 'yams', 'yang', 'yank', 'yaps', 'yard', \
        'yare', 'yarn', 'yaud', 'yaup', 'yawl', 'yawn', 'yawp', \
        'yaws', 'yeah', 'yean', 'year', 'yeas', 'yech', 'yeld', \
        'yelk', 'yell', 'yelp', 'yens', 'yeps', 'yerk', 'yews', \
        'yins', 'yipe', 'yips', 'yobs', 'yoga', 'yogi', 'yoke', \
        'yolk', 'yond', 'yore', 'your', 'yous', 'yowl', 'yuck', \
        'yuks', 'yule', 'yups', 'yurt', 'zags', 'zany', 'zaps', \
        'zeal']