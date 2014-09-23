#!/usr/bin/python3
# -*- coding: UTF-8 -*-

w_api = 'YE3YUE-WPHP5KGTXE'
letter_set = ''
needed = ''

import sys

if len(sys.argv) < 2:
    print("No charset given. Aborting.")
    exit()
else:
    letter_set = sys.argv[1]
    if len(sys.argv) >= 3:
        needed = sys.argv[2]

import wap

server = 'http://api.wolframalpha.com/v2/query.jsp'
appid = w_api
input_str = 'words with ' + letter_set

scantimeout = '3.0'
podtimeout = '4.0'
formattimeout = '6.0'
async = 'False'


waeo = wap.WolframAlphaEngine(appid, server)
waeo.ScanTimeout = scantimeout
waeo.PodTimeout = podtimeout
waeo.FormatTimeout = formattimeout
waeo.Async = async

queryStr = waeo.CreateQuery(input_str)

waq = wap.WolframAlphaQuery(queryStr, appid)
waq.ScanTimeout = scantimeout
waq.PodTimeout = podtimeout
waq.FormatTimeout = formattimeout
waq.Async = async
waq.AddPodIndex('WordsMadeWithOnlyLetters')
waq.AddPodState('WordsMadeWithOnlyLetters__Disallow repetition  ')
waq.AddPodState('WordsMadeWithOnlyLetters__Sorted by length')
waq.AddPodState('WordsMadeWithOnlyLetters__More')

e_r = waeo.PerformQuery(waq.Query)
result = wap.WolframAlphaQueryResult(e_r)

for pod in result.Pods():
    waPod = wap.Pod(pod)
    for subpod in waPod.Subpods():
        waSubpod =  wap.Subpod(subpod)
        t = waSubpod.Plaintext()[0]
        s = t.split('  |  ')
        results = []
        for w in s[:-1]:
            if (needed != ''):
                for c in needed:
                    if (c in w) and (w not in results):
                        results.append(w)
            else:
                results.append(w)
        for r in results:
            print(r)