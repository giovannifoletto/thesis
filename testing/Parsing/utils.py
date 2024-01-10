import json
import costants
from Parsing.Parser import Parser

def feature_extraction(files=costants.FLAWS_CLOUDTRAILS_FILES):
    global FeatureLog
    log_section = dict()
    
    print(f"=========== READING ALL FILES ============")
    for cloud_file in files:
        print(f"File {cloud_file}")
        with open(cloud_file) as filej:
            read_json = json.load(filej)
            for i in read_json["Records"]:
                #cl = ClusterLog(i)
                cl = Parser(i)
                cl.parse_log()

                for k, v in cl.element.items():
                    #print(k.split("."))
                    #print(k.split(".")[0])
                    for notgood in costants.aggregate:
                        if k.split(".")[0] != notgood:
                            if k not in log_section:
                                # USERAGENT = useragent
                                log_section[k.split(".")[0].upper()] = k

                #corpus.append(cl.to_csv())

    print(f"====== FEATURE EXTRACTION COMPLETED =======")

    print(f"Keys found: {len(log_section)}")

    print(f"Creatin Enum: ")

    import enum
    FeatureLog = enum.Enum('FeatureLog', log_section)

    print(f"============ PRINTING ENUM FOUND ============")
    print([e for e in FeatureLog])
    
    print(f"========== TRANSFORM FILES TO CSV  ==========")
    csv_file = open(costants.CSV_FILE, "w")
    for cloud_file in files:
        print(f"File {cloud_file}")
        with open(cloud_file) as filej:
            read_json = json.load(filej)
            for i in read_json["Records"]:
                #cl = ClusterLog(i)
                cl = Parser(i)
                cl.parse_log()

                #print(cl.element.items())

                res = cl.create_csv_from_enum(FeatureLog)

                #corpus.append(res)
                csv_file.write(res + "\n")
    csv_file.close()

# in order to restore this function is necessary to add unique_keys and corpus
# array in the function statement
# def import_and_transform_data(files=costants.FLAWS_CLOUDTRAILS_FILES):
#     key_len = []

#     for cloud_file in files:
#         print(f"File {cloud_file}")
#         with open(cloud_file) as filej:
#             read_json = json.load(filej)
#             for i in read_json["Records"]:
#                 #cl = ClusterLog(i)
#                 cl = Parser(i)
#                 cl.parse_log()
#                 key_len.append(len(cl.keys))

#                 for k, v in cl.element.items():
#                     if k not in unique_keys:
#                         unique_keys.add(k)

#                 corpus.append(cl.to_csv())

#     print(f"============ IMPORT  COMPLETED ============")
#     import numpy as np
#     print(f"Keys found: MEAN {np.mean(key_len)}, MAX: {max(key_len)}, MIN: {min(key_len)}")

#     print(f"Imported: {len(corpus)} elements")

#     print(f"========== ALL UNIQUE KEYS FOUND ==========")
#     with open("unique_keys.csv", "w") as wf:
#         for i in unique_keys:
#             wf.write(i + ", ")

def refine_to_json():
    import json
    for fc in costants.FLAWS_CLOUDTRAILS_FILES:
        print(f"Importing '{fc}'")
        with open(fc) as j:
            read_json = json.load(j)
            with open(costants.JSON_REFINED, "a") as wnj:
                # wnj = write new json
                for line in read_json["Records"]:
                    wnj.write(f"{line}, \n")

def drain_testing():
    from drain3 import TemplateMiner
    import time

    template_miner = TemplateMiner()

    with open(costants.JSON_REFINED) as f:
        lines = f.readlines()

    start_time = time.time()
    batch_start_time = start_time
    batch_size = 10000
    line_count = 0

    for line in lines:
        #line = line.rstrip()
        #line = line.partition(": ")[2]
        result = template_miner.add_log_message(line)
        line_count += 1
        if line_count % batch_size == 0:
            time_took = time.time() - batch_start_time
            rate = batch_size / time_took
            #print(f"Processing line: {line_count}, rate {rate:.1f} lines/sec, "
            #            f"{len(template_miner.drain.clusters)} clusters so far.")
            batch_start_time = time.time()
        if result["change_type"] != "none":
            result_json = json.dumps(result)
            #print(f"Input ({line_count}): {line}")
            #print(f"Result: {result_json}")

    time_took = time.time() - start_time
    rate = line_count / time_took

    print(f"--- Done processing file in {time_took:.2f} sec. Total of {line_count} lines, rate {rate:.1f} lines/sec, "
                f"{len(template_miner.drain.clusters)} clusters")

    sorted_clusters = sorted(template_miner.drain.clusters, key=lambda it: it.size, reverse=True)
    for cluster in sorted_clusters:
        print(cluster)

    print("Prefix Tree:")
    template_miner.drain.print_tree()

    template_miner.profiler.report(0)