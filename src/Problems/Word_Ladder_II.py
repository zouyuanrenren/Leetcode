'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        alphabet = [chr(ord("a")+k) for k in range(26)]
        if start == end:
            return [[start]]
        graph = {start:[], end:[]}
        for word in dict:
            graph[word] = []
        for word in dict:
            for i in range(len(word)):
                for c in alphabet:
                    next = word[:i]+c+word[i+1:]
                    if next == start or next == end or next in dict:
                        if next != word and next not in graph[word]:
                            graph[word].append(next)
                            graph[next].append(word)
        results = []
        queue = [[start]]
        visited = set([start])
        boarder = set()
        step = 0
        size = 1
        while len(queue):
            path = queue.pop(0)
            if step and len(path) > step:
                break
            if len(path) > size:
                size += 1
                visited |= boarder
                boarder = set()
            word = path[-1]
            for next in graph[word]:
                if next == end:
                    step = len(path)
                    results.append(path+[next])
                elif next not in visited:
                    queue.append(path+[next])
                    boarder.add(next)        
        return results
    
sol = Solution()
# start = "nape"
# end = "mild"
# dict = ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"]
start = "a"
end = "c"
dict = ["a","b","c"]
print sol.findLadders(start, end, dict)
   
                        