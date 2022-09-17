// ==UserScript==
// @name         10944 Random Game Random Submitter (Redirection Part)
// @namespace    https://jonghyeon.me
// @version      1
// @description  Baekjoon Online Judge Random Game Random Submitter (Redirection Part)
// @author       ShapeLayer
// @match        https://www.acmicpc.net/status?*problem_id=10944*
// @grant        GM_setValue
// @grant        GM_getValue
// @run-at       document-end
// ==/UserScript==

(function() {
  const now = new Date()
  const key = now.getFullYear() + ' ' + now.getMonth() + ' ' + now.getDate()
  var nowTried = GM_getValue(key, 0)
  GM_setValue(key, nowTried+1)
  console.log(key + ' tried: ' + nowTried + ', delayed: ' + 10*((nowTried/50)+1)*1000)
  setTimeout(() => {window.location.href='https://www.acmicpc.net/submit/10944'}, 10*((nowTried/50)+1)*1000)
})();