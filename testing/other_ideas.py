import costants
from Parsing.Parser import Parser

class LogData:
    def __init__(self) -> None:
        self.keys = dict() # name: how-to-find-it

    def read_file(self, infile, start_with="Records") -> None:
        """
            start_with: it's needed since the file we had work are formed by a object containing only one parameters ('Records' => an array of log)
        """
        import json
        with open(infile) as fj:
            read_json = json.load(fj)
            for log in read_json[start_with]:
                parser = Parser(log)
                parser.parse_log()
                for i in parser.keys:
                    if i not in self.keys.keys():
                        self.keys[i] = 1
                #print(parser)
                #print("======")
                #print(parser.to_csv())
                #print("======")
    
    def read_files(self, infiles, start_with="Records") -> None:
        for f in infiles:
            self.read_file(f, start_with=start_with)

class LogTemplate:
    def __init__(self):
        self.userAgent
        self.eventID
        self.userIdentity
        self.type
        self.principalId
        self.arn
        self.accountId
        self.accessKeyId
        self.sessionContext
        self.attributes
        self.mfaAuthenticated
        self.creationDate
        self.eventType
        self.sourceIPAddress
        self.eventName
        self.eventSource
        self.recipientAccountId
        self.requestParameters
        self.roleName
        self.assumeRolePolicyDocument
        self.awsRegion
        self.requestID
        self.responseElements
        self.role
        self.assumeRolePolicyDocument
        self.arn
        self.roleId
        self.createDate
        self.roleName
        self.path
        self.eventVersion
        self.eventTime

class ClusterLog:
    def __init__(self, json_log):
        self.string  = ""
        self.isError = False
        self.keys    = []

        if type(json_log) == type(dict()): 
            self.string  = self.undict(json_log) + "\n"
            self.isError = False
            self.keys    = [] #self.findall_keys(json_log)
             
        else:
            self.string  = ""
            self.isError = True
            self.keys    = []

    def undict(self, tstr):
        if type(tstr) == type(dict()):
            temp = ""
            for i in tstr.keys():
                if i =="assumeRolePolicyDocument" or i == "responseElements":
                    print(tstr[i])

                recall = self.undict(tstr[i])

                if recall is None:
                    temp += "None,"
                else:
                    temp += str(recall)
            return temp
        elif type(tstr) == type(list()):
            #print(f"Found array in {tstr}")
            for i in tstr:
                return self.undict(i)
        else:
            if tstr is not None:
                return str(tstr) + ","
            else:
                return "None,"
    
    def findall_keys(self, log):
        #print(f"{log}", f"{self.keys}")
        if type(log) == type(dict()):
            for k in log.keys():
                self.keys.append(str(k))
                self.findall_keys(log[k])
        else:
            return
        
def import_transform_with_new_class(files=costants.FLAWS_CLOUDTRAILS_FILES):
    logdata = LogData()
    logdata.read_files(files)
    print(len(logdata.keys))

def vectorize():
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()
    f_input = open(costants.CSV_FILE, "r")
    print(type (f_input))
    X_train = vectorizer.fit_transform(f_input)
    print(vectorizer.get_feature_names_out())


def refine_unique_keywords():
    for w in costants.unique_keys:
        ws = w.split(".")[0]
        # forbidden words gets aggregated
        for fw in costants.aggregate:
            if ws != fw:
                costants.output_keys.append(w)

    print("==== MAIN KEYWORD CHOOSEN ====")
    costants.output_keys.sort()
    for w in output_keys:
        print(w)

def get_ready_to_csv(files=costants.FLAWS_CLOUDTRAILS_FILES):
    import json
    costants.corpus.clear()
    for cloud_file in files:
        print(f"File {cloud_file}")
        with open(cloud_file) as filej:
            read_json = json.load(filej)
            for i in read_json["Records"]:
                record = ""
                cl = Parser(i)
                cl.parse_log()

                for wc in costants.output_keys:
                    if cl.element.get(wc):
                        record += str(cl.element.get(wc)) + ","
                    else:
                        record += " ,"

                costants.corpus.append(record)

    print(f"============= RECORDS  IMPORT =============")

    print(f"Imported: {len(costants.corpus)} elements")

def save_to_csv():
    with open(costants.CSV_FILE, "w") as file_all:
        for line in costants.corpus:
            file_all.write(line)

def read_csv():
    print(f"Importing CSV file: {costants.CSV_FILE}")
    with open(costants.CSV_FILE, "r") as file_all:
        for line in file_all.readlines():
            costants.corpus.append(line)

def use_spell_vectorizer(feature_enum):
    from Spell import LogParser
    input_dir  = '.'  # The input directory of log file
    output_dir = 'demo_result/'  # The output directory of parsing results
    log_file   = costants.JSON_REFINED  # The input log file name
    log_format = ''  # HDFS log format
    tau        = 0.5  # Message type threshold (default: 0.5)
    regex      = []  # Regular expression list for optional preprocessing (default: [])

    for e in feature_enum:
        log_format += f"<{e.value}>|"
    
    print(f"LOF-FORMAT: {log_format}")

    parser = LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
    parser.parse(log_file)

def torch_applied():
    from torch import nn, torch
    import pandas as pd
    log_file = pd.read_csv(costants.CSV_FILE)

def log_components_extraction(files=costants.FLAWS_CLOUDTRAILS_FILES):
    # from Parsing.utils import feature_extraction
    # import json
    # ## In order to make this works, we could semplify the organization of the log file
    # ## making some order in the parameters: first some ever present, and then ordered by
    # ## some sort of sorting algorithm (like alphabetical order).
    # first_line = ""
    # print(f"=========== READING ALL FILES ============")
    # for cloud_file in files:
    #     print(f"File {cloud_file}")
    #     with open(cloud_file) as filej:
    #         read_json = json.load(filej)
    #         for i in read_json["Records"]:
    #             cl = Parser(i)
    #             cl.parse_log()
                
    #             first_line = cl.return_only_first_level()
    #             break

    # print(f"====== FEATURE EXTRACTION COMPLETED =======")

    # for fi in first_line:
        

    #print(f"Keys found: {len(log_section)}")
    return first_line