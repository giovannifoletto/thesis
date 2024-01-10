
class LogData:
    def __init__(self) -> None:
        self.keys = dict() # name: how-to-find-it

    def read_file(self, infile, start_with="Records") -> None:
        """
            start_with: it's needed since the file we had work are formed by a object containing only one parameters ('Records' => an array of log)
        """
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
        
def import_transform_with_new_class(files=FLAWS_CLOUDTRAILS_FILES):
    logdata = LogData()
    logdata.read_files(files)
    print(len(logdata.keys))

def vectorize():
    import csv
    vectorizer = CountVectorizer()
    f_input = open(CSV_FILE, "r")
    print(type (f_input))
    X_train = vectorizer.fit_transform(f_input)
    print(vectorizer.get_feature_names_out())


def refine_unique_keywords():
    for w in unique_keys:
        ws = w.split(".")[0]
        # forbidden words gets aggregated
        for fw in aggregate:
            if ws != fw:
                output_keys.append(w)

    print("==== MAIN KEYWORD CHOOSEN ====")
    output_keys.sort()
    for w in output_keys:
        print(w)

def get_ready_to_csv(files=FLAWS_CLOUDTRAILS_FILES):
    corpus.clear()
    for cloud_file in files:
        print(f"File {cloud_file}")
        with open(cloud_file) as filej:
            read_json = json.load(filej)
            for i in read_json["Records"]:
                record = ""
                cl = Parser(i)
                cl.parse_log()

                for wc in output_keys:
                    if cl.element.get(wc):
                        record += str(cl.element.get(wc)) + ","
                    else:
                        record += " ,"

                corpus.append(record)

    print(f"============= RECORDS  IMPORT =============")

    print(f"Imported: {len(corpus)} elements")

def save_to_csv():
    with open(CSV_FILE, "w") as file_all:
        for line in corpus:
            file_all.write(line)

def read_csv():
    print(f"Importing CSV file: {CSV_FILE}")
    with open(CSV_FILE, "r") as file_all:
        for line in file_all.readlines():
            corpus.append(line)

def use_spell_vectorizer():
    from testing.Spell import LogParser
    input_dir  = '.'  # The input directory of log file
    output_dir = 'demo_result/'  # The output directory of parsing results
    log_file   = CSV_FILE  # The input log file name
    log_format = ''  # HDFS log format
    tau        = 0.5  # Message type threshold (default: 0.5)
    regex      = []  # Regular expression list for optional preprocessing (default: [])

    for e in FeatureLog:
        log_format += f"<{e.value}>, "
    
    print(f"LOF-FORMAT: {log_format}")

    parser = LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
    parser.parse(log_file)

def torch_applied():
    from torch import nn, torch
    import pandas as pd
    log_file = pd.read_csv(CSV_FILE)
