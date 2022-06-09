// ==UserScript==
// @name         10944 Random Game Random Submitter
// @namespace    https://jonghyeon.me
// @version      1
// @description  Baekjoon Online Judge Random Game Random Submitter
// @author       ShapeLayer
// @match        https://www.acmicpc.net/submit/10944
// @grant        none
// @run-at       document-end
// ==/UserScript==

function submitCode() {
  var newForm = document.createElement('form')
  newForm.id = 'newForm'
  newForm.method = 'post'
  var input__code_open = document.createElement('input')
  input__code_open.name = 'code_open'
  input__code_open.value = 'open'
  newForm.appendChild(input__code_open)
  var input__csrf_key = document.createElement('input')
  input__csrf_key.name = 'csrf_key'
  input__csrf_key.value = document.getElementsByName('csrf_key')[0].value
  newForm.appendChild(input__csrf_key)
  var input__language = document.createElement('input')
  input__language.name = 'language'
  input__language.value = '58'
  newForm.appendChild(input__language)
  var input__problem_id = document.createElement('input')
  input__problem_id.name = 'problem_id'
  input__problem_id.value = '10944'
  newForm.appendChild(input__problem_id)
  var input__source = document.createElement('input')
  input__source.name = 'source'
  input__source.value = '10'
  newForm.appendChild(input__source)

  document.getElementsByTagName('body')[0].appendChild(newForm)
  newForm.submit()
}

(function() {
  submitCode()
})();