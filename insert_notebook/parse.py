import json,sys

def parseNotebook(dir):
    with open(dir,mode='r',encoding='UTF-8') as f:
        lines = f.readlines()
    preamble = [];document = []
    packageBegin = -1; packageEnd = -1; documentBegin = -1; documentEnd = -1; parskipIndex=-1;
    for i in range(len(lines)):
        if 'maketitle' in lines[i]:
            titleIndex = i
        if 'usepackage{parskip}' in lines[i]:
            parskipIndex = i
        if 'documentclass' in lines[i]:
            packageBegin = i+1
        if 'begin{document}' in lines[i]:
            packageEnd = i
            documentBegin = i+1
        if 'end{document}' in lines[i]:
            documentEnd = i
    preamble = lines[packageBegin:packageEnd]
    document = lines[documentBegin:titleIndex]+lines[titleIndex+1:documentEnd]

    return preamble,document,parskipIndex

def merge(notebook_dir,output_dir,template_dir='../template-config.tex',config_dir='report_config.json'):
    nb_preamble, nb_document, parskipIndex = parseNotebook(notebook_dir)
    with open(template_dir,mode='r',encoding='UTF-8') as f:
        lines = f.readlines()
    packageBegin = -1;packageEnd = -1;documentBegin = -1;documentEnd = -1
    processIndex = -1;summaryIndex = -1
    for i in range(len(lines)):
        if 'documentclass' in lines[i]:
            packageBegin = i
        if 'begin{document}' in lines[i]:
            packageEnd = i
            documentBegin = i
        if 'end{document}' in lines[i]:
            documentEnd = i+1
        if 'startUrProcess' in lines[i]:
            processIndex = i
        if 'startUrSummary' in lines[i]:
            summaryIndex = i
    tp_preamble = lines[packageBegin:packageEnd]
    # tp_document = lines[documentBegin:documentEnd]
    beforeProcess = lines[documentBegin:processIndex]
    beforeSummary = lines[processIndex+1:summaryIndex]
    afterSummary = lines[summaryIndex+1:documentEnd]


    with open(config_dir,mode='r',encoding='UTF-8') as j:
        config = json.load(j)
    preamble = []
    if config['use']:
        keys = list(config.keys())
        keys.remove('use')
        if config['indent']:
            nb_preamble.pop(parskipIndex-1)
        keys.remove('indent')
        keys.remove('preview')
        keys.remove('summary')

        for key in keys:
            preamble.append('\\renewcommand{\\X%s}{%s}\n' % (key,config[key]))

        if config['preview']['use']:
            subkeys = list(config['preview'].keys())
            subkeys.remove('use')
            for subkey in subkeys:
                preamble.append('\\renewcommand{\\X%s}{%s}\n' % (subkey,config['preview'][subkey].replace('\n',' \\\\ ')))

        if config['summary']['use']:
            subkeys = list(config['summary'].keys())
            subkeys.remove('use')
            for subkey in subkeys:
                preamble.append('\\renewcommand{\\X%s}{%s}\n' % (subkey, config['summary'][subkey].replace('\n',' \par ')))

    o = open(output_dir,mode='w',encoding='UTF-8')
    o.writelines(tp_preamble+nb_preamble+preamble+beforeProcess+nb_document+beforeSummary+afterSummary)
    o.close()
    j.close()
    f.close()

if __name__ == '__main__':
    # merge(
    #     notebook_dir='./sample/Sample.tex',
    #     output_dir='./sample/Merged.tex',
    #     template_dir='../template-config.tex',
    #     config_dir='./report_config.sample.json',
    # )
    paras = sys.argv
    if len(paras) == 3:
        merge(
            notebook_dir=paras[1],
            output_dir=paras[2]
        )
    elif len(paras) == 4:
        merge(
            notebook_dir=paras[1],
            output_dir=paras[2],
            config_dir=paras[3]
        )
    elif len(paras) == 5:
        merge(
            notebook_dir=paras[1],
            output_dir=paras[2],
            template_dir=paras[3],
            config_dir=paras[4]
        )
    else:
        print("***ERROR***\nAccepted arguments:\n   [\'notebook_dir\',\'output_dir\']\nOR [\'notebook_dir\',\'output_dir\',\'config_dir\']\nOR [\'notebook_dir\',\'output_dir\',\'template_dir\',\'config_dir\']\n")
        raise Exception("Invalid arguments given:", sys.argv)
    print('合并成功。')