'''Tigress Constant values.'''
VN = 1
DATA = 'D'
ABSTRACT = 'A'
CONTROL_FLOW = 'C'
VIRTUALIZATION = 'V'


TIGRESS_RE = {
    'while-random-funs': r'while \(randomFuns_i5.*',
    'argc-nl': r'argc !=.* {\n.*',
    'char-password': r'(char password\[100\].*)',
    'one-nl': r'\1\n',
    'printf-please': r'(printf\("Please.*\n  scanf\("%s", password\);)',
    'string-compare-result': r'(stringCompareResult = strncmp\(password,.*\n.*)',
    'random-funs-value': r'(randomFuns_value6 =.*\n    input\[randomFuns_i5\].*)',
    'int-activation-code': r'int activationCode ;',
    'unsigned-long-activation-code': r'(unsigned long activationCode ;)',
    'activation-code': r'(activationCode =.*)',
    'failed': r'(failed \|= activationCode !.*)',
    'arg-code': r'unsigned long input\[.*] ;'}

TIGRESS_REPLACE = {
    'pass': '  char password{count}[100] = "";',
    'printf': '  printf("Please enter password:");\n  ' \
              'scanf("%s", password{count});',
    'check-pass': '  stringCompareResult = strncmp(password{count}, "{password}", 100UL);\n  ' \
                  'failed |= stringCompareResult != 0UL;',
    'while': '  while (randomFuns_i5 < {count}) {{',
    'num-code': 'unsigned long input[{count}] ;',
    'code': '  unsigned long activationCode{count} ;',
    'input': '  activationCode{count} = input[{count2}UL];',
    'check-code': '  failed |= activationCode{count} != {code}UL;',

    'randfuns': '    randomFuns_value6 = strtoul(argv[randomFuns_i5 + {index}], 0, 10);\n    ' \
                'input[randomFuns_i5 + {index2}] = randomFuns_value6;',

    'mega-init': 'argc != {count} ) {{\n    ' \
                 'printf("Call this program with %i arguments ' +
                 repr('\\n').replace('\'', '') + '", {count2});',
    'unsigned-long-activation-code': 'unsigned long activationCode ;'

}

'''
Taken reference from:
Holder, William & Mcdonald, J & Andel, Todd. (2017).
Evaluating Optimal Phase Ordering in Obfuscation Executives.
10.1145/3151137.3151140.
'''
TIGRESS_CMD = {
    'abstract': 'tigress \
        --Verbosity=1 \
        --FilePrefix=v{vn}a \
        --Transform=Split \
        --Seed=0 \
        --SplitKinds=deep,block,top \
        --SplitCount=10 \
        --Functions=authenticate \
        --Transform=CleanUp \
        --CleanUpKinds=annotations \
        --out={output} {input}',

    'abstract-2': '''tigress \
        --FilePrefix=v{vn}b \
        --Verbosity=1  \
        --Transform=RndArgs \
        --Seed=0 \
        --RndArgsBogusNo=2?5 \
                ''' + '--Functions=_v{vn}a_1_authenticate_authenticate_split_1'
                  + ',_v{vn}a_1_authenticate_authenticate_split_2'
                  + ',_v{vn}a_1_authenticate_authenticate_split_3'
                  + ',_v{vn}a_1_authenticate_authenticate_split_4'
                  + ',_v{vn}a_1_authenticate_authenticate_split_5'
                  + ',_v{vn}a_1_authenticate_authenticate_split_6'
                  + ',_v{vn}a_1_authenticate_authenticate_split_7'
                  + ',_v{vn}a_1_authenticate_authenticate_split_8'
                  + ',_v{vn}a_1_authenticate_authenticate_split_9'
                  + ',_v{vn}a_1_authenticate_authenticate_split_10 ' +
                  '''--Transform=CleanUp \
        --CleanUpKinds=annotations \
        --out={output} {input}''',

    'abstract-3': '''tigress --Verbosity=1   \
        --FilePrefix=v{vn} \
        --Transform=InitEntropy \
        --Functions=main  \
        --Transform=InitOpaque \
        --Functions=main \
        --InitOpaqueCount=2 \
        --InitOpaqueStructs=list,array  \
                --Transform=Merge \
                ''' + '--Functions=_v{vn}a_1_authenticate_authenticate_split_1'
                  + ',_v{vn}a_1_authenticate_authenticate_split_2'
                  + ',_v{vn}a_1_authenticate_authenticate_split_3'
                  + ',_v{vn}a_1_authenticate_authenticate_split_4'
                  + ',_v{vn}a_1_authenticate_authenticate_split_5'
                  + ',_v{vn}a_1_authenticate_authenticate_split_6'
                  + ',_v{vn}a_1_authenticate_authenticate_split_7'
                  + ',_v{vn}a_1_authenticate_authenticate_split_8'
                  + ',_v{vn}a_1_authenticate_authenticate_split_9'
                  + ',_v{vn}a_1_authenticate_authenticate_split_10 ' +
                  '''--Transform=CleanUp \
        --CleanUpKinds=annotations \
        --out={output} {input}''',

    'control-flow': 'tigress \
        --Verbosity=1 \
        --FilePrefix=v{vn} \
        --Transform=InitOpaque \
        --Functions=main \
        --Transform=UpdateOpaque \
        --Functions=authenticate \
        --UpdateOpaqueCount=10 \
        --Transform=AddOpaque \
        --Functions=authenticate \
        --AddOpaqueCount=10  \
        --AddOpaqueKinds=call,bug,true,junk \
        --Transform=Flatten \
        --Functions=authenticate \
        -FlattenObfuscateNext=true \
        --FlattenDispatch=switch \
        --Transform=CleanUp \
        --CleanUpKinds=annotations \
        --out={output} {input}',

    'data': 'tigress \
        --Verbosity=1  \
        --FilePrefix=v{vn} \
        --Transform=InitEntropy \
        --Functions=main  \
        --Transform=EncodeLiterals \
        --Functions=authenticate  \
        --Transform=CleanUp \
        --CleanUpKinds=annotations \
        --out={output} {input}',

    'virtualization': 'tigress \
        --Verbosity=1  \
        --FilePrefix=v{vn} \
        --Transform=Virtualize \
        --Functions=authenticate \
        --VirtualizeDispatch=switch \
        --Transform=CleanUp \
        --CleanUpKinds=annotations \
        --out={output} {input}',

    'generate': 'tigress \
        --Verbosity=1 \
        --Seed=0 \
        --Transform=RandomFuns \
        --RandomFunsName=authenticate \
        --RandomFunsType=long \
        --RandomFunsInputSize=1 \
        --RandomFunsStateSize=1 \
        --RandomFunsOutputSize=1 \
        --RandomFunsCodeSize=10 \
        {option} \
        --RandomFunsFailureKind=segv  \
        --out={output} {input}',

    'code': '--RandomFunsActivationCodeCheckCount=1 \
             --RandomFunsActivationCode={code}',

    'pass': '--RandomFunsPasswordCheckCount=1 \
             --RandomFunsPassword={password}'
}
