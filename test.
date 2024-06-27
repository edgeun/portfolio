<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>0604_SQL_데이터 검색 속도 높이기 (INDEX) ~ 데이터 복구 3 (FLASHBACK DROP)</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	padding-inline-start: 0;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.page-description {
    margin-bottom: 2em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-uiBlue { background-color: rgba(35, 131, 226, .07); }
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-transparentGray { background-color: rgba(227, 226, 224, 0); }
.select-value-color-translucentGray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }
.select-value-color-pageGlass { background-color: undefined; }
.select-value-color-washGlass { background-color: undefined; }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="2474cee5-125c-4d01-a737-bb965d923432" class="page sans"><header><div class="page-header-icon undefined"><span class="icon">🐣</span></div><h1 class="page-title">0604_SQL_데이터 검색 속도 높이기 (INDEX) ~ 데이터 복구 3 (FLASHBACK DROP)</h1><p class="page-description"></p></header><div class="page-body"><h3 id="88adc0ab-8aba-4417-8785-34be8ec514c5" class="">📋 목차</h3><p id="11f8d8a0-a7dc-4871-8da2-ea218b7c83cb" class=""><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432.html">97. 데이터 검색 속도를 높이기 (INDEX)</a></p><p id="37f233eb-5d60-4fd1-be25-2f2d930f2049" class=""><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432.html">98. 절대로 중복되지 않는 번호 만들기 (SEQUENCE)</a></p><p id="3d12b2ae-423e-475f-9ecb-a3d5f323c147" class=""><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432.html">99. 실수로 지운 데이터 복구하기 1 (FLASHBACK QUERY)</a></p><p id="5ce5e19c-4c73-4af2-9773-95056748fc6f" class=""><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432.html">100. 실수로 지운 데이터 복구하기 2(FLASHBACK TABLE)</a></p><p id="ebedb690-9df3-43ed-a013-12bbaa2df3a4" class=""><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432.html">101. 실수로 지운 데이터 복구하기 3 (FLASHBACK DROP)</a></p><p id="6f19e8a6-df57-489d-97ea-5f457da97b25" class="">
</p><p id="fd43c987-5c36-4a66-bd0a-86c9c3949907" class="">(점심문제) 나이가 많으면서 비만이면 의료비가 더 많이 드는가?</p><ul id="e47a8c0d-0650-4cd8-8d80-c7889a28a123" class="bulleted-list"><li style="list-style-type:disc">귀무가설: 나이가 많으면서 비만인것은 의료비와 연관이 없다.</li></ul><ul id="d25c0e3f-d8d2-43bc-9ac9-1b4a81c58ff0" class="bulleted-list"><li style="list-style-type:disc">대립가설: 나이가 많으면서 비만인것은 의료비와 연관이 있다.</li></ul><p id="5c7ed23b-7620-444e-bd82-f407b8cd1a1e" class="">나이는 60살을 기준으로 60살 이상이면 1 아니면 0으로 하는 파생컬럼을 추가하세요.</p><p id="3e0ac65a-ae27-4cb5-ba66-b58a50f4119d" class="">비만지수는 30을 기준으로 1과 0으로 구분된 bmi30을 그대로 사용합니다.</p><ul id="f665ce51-0e3d-4f70-90df-f57ac65eb478" class="bulleted-list"><li style="list-style-type:disc">나이 60이상 0 or 1 컬럼 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="7f434667-458c-4594-aca5-148674ada882" class="code"><code class="language-SQL">ALTER TABLE insurance
 ADD bmi_age_old    NUMBER(10);
 
SELECT * FROM insurance;</code></pre><ul id="f0a666e2-367b-486f-a9a8-8eedf532603f" class="bulleted-list"><li style="list-style-type:disc">나이 60이상 컬럼 0 or 1 업데이트</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="60a1a103-c331-4451-8772-ab171ee6e8d7" class="code"><code class="language-SQL">UPDATE insurance
 SET bmi_age_old = 0;
 
UPDATE insurance
 SET bmi_age_old = 1
 WHERE bmi30 = 1 AND age &gt;= 60;

COMMIT;
 
SELECT * FROM insurance;</code></pre><ul id="5f785df3-4834-47e5-9d06-e42e66afe407" class="bulleted-list"><li style="list-style-type:disc">회귀 분석 스크립트로 테이블 학습</li></ul><p id="596b6768-5f34-4a0a-9d0e-df47658205ba" class=""><a href="0603_SQL_%E1%84%8B%E1%85%B5%E1%86%B7%E1%84%89%E1%85%B5%20%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%86%AF%20%E1%84%89%E1%85%A2%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC%20(CREATE%20TEMPORAY%20TAB%206d2369f6f2f14aab963270f4f40e5f8e.html">https://www.notion.so/edgeun/0603_SQL_-CREATE-TEMPORAY-TABLE-SQL-6d2369f6f2f14aab963270f4f40e5f8e?pvs=4#cbb82a2ef9184e4faee1706ace8c1ffa</a></p><figure id="52b8406e-a806-4292-bf98-bb77e8c1463f" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled.png"><img style="width:408px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled.png"/></a></figure><ul id="bafe8c3f-2c7b-4fa2-8444-7544cd27341b" class="bulleted-list"><li style="list-style-type:disc">정답치와 상관계수 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="14cb79f8-cf6a-4d49-aee1-df4e38bcd74d" class="code"><code class="language-SQL">SELECT CORR(EXPENSES, MODEL_PREDICT_RESPONSE)
 FROM (SELECT ID, AGE, SEX, EXPENSES, 
          ROUND(PREDICTION (MD_REG_MODEL2 USING *),2) MODEL_PREDICT_RESPONSE
  FROM INSURANCE_TEST T);</code></pre><figure id="2948d081-c581-4a0b-8f5e-8ac273be8a10" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%201.png"><img style="width:340px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%201.png"/></a></figure><ul id="3be261b6-61c1-42b0-a1ec-0ab1c1bd91c7" class="bulleted-list"><li style="list-style-type:disc">회귀계수와 p-value 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="e2b0fcaf-6ee1-4bee-a5c3-044ae3c133b5" class="code"><code class="language-SQL">-- 7. 회귀분석 모델의 회귀계수를 확인합니다.

SELECT ATTRIBUTE_NAME, ATTRIBUTE_VALUE, ROUND(COEFFICIENT), e.*
  FROM TABLE (DBMS_DATA_MINING.GET_MODEL_DETAILS_GLM (&#x27;MD_REG_MODEL2&#x27;)) e;</code></pre><figure id="aada9e0f-7630-4a5d-8128-a0487d7e2a3e" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%202.png"><img style="width:230px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%202.png"/></a></figure><p id="2fe5ad9e-a2d6-43f2-9f44-1eab711a587a" class="">
</p><hr id="d972d4b8-f302-4f34-a6a2-5b0a4edb2a75"/><h3 id="43cf0afd-1c8b-4484-9d16-ce2e8a293461" class="">97. 데이터 검색 속도를 높이기 (INDEX)</h3><p id="23abd30d-fa73-4435-87b3-b5a447a04181" class="">인덱스(index) 란 ? 테이블에서 데이터를 검색할 때 검색속도를 향상 시켜주는 데이터베이스 오브젝트</p><h3 id="f164a4ab-9868-45f6-ab97-3166f0b2c03a" class="">DB 오브젝트(object) 5가지 ?</h3><p id="0eca9eef-7830-450f-b454-2cd893cfce26" class="">테이블 / 인덱스 / 뷰 / 시노님 / 시퀀스</p><p id="140baaa1-29e7-46cf-9fad-9ea3800783da" class="">
</p><p id="6dbb87b9-0f31-49e5-99b0-ceaa7b3eda92" class="">빅데이터 환경에서 인덱스가 없다면 검색이 너무 느려서 아무런 작업을 할 수 없습니다. 인덱스는 두꺼운 책에 목차를 연상하면 됩니다.</p><p id="82fc52ac-f09a-47e9-a6e3-d18e142dd3ea" class="">
</p><figure id="288acbcc-7262-4e61-b15c-46c9101fb5ee" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%203.png"><img style="width:565px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%203.png"/></a></figure><p id="d44abe62-1dcd-476d-936a-cecc14433e57" class="">
</p><ul id="11e09774-f8ad-4c81-8268-0b2f75e6a516" class="bulleted-list"><li style="list-style-type:disc">인덱스는 책의 목차와 같은 것입니다.</li></ul><ul id="4e9ef4d0-c73a-47db-a204-850022188e51" class="bulleted-list"><li style="list-style-type:disc">인덱스는 컬럼 값과 rowid로 구성되어있습니다.</li></ul><ul id="1a89db1f-4809-46c8-ad91-fb429072b21b" class="bulleted-list"><li style="list-style-type:disc">컬럼 값은 데이터가 ascending하게 정렬이 되어있습니다. (빨리 검색하기 위해서)</li></ul><ul id="5213b823-a529-4361-9c5e-e0bba0e897d8" class="bulleted-list"><li style="list-style-type:disc">문자는 abcd 순으로 정렬해서 저장했고 숫자는 낮은 값에서 높은 값순으로 정렬해서 저장했습니다. 책 앞에 목차가 가나다라 순서면 우너파는 페이지를 빠르게 검색할 수 있는 것과 같습니다.</li></ul><ul id="ba7f6d9f-60bb-49bc-8d95-c449a856f9ed" class="bulleted-list"><li style="list-style-type:disc">만약 인덱스가 없다면 테이블을 처음부터 끝까지 FULL TABLE SACN을 해야합니다.</li></ul><p id="b1aa9754-9737-4ff6-9fad-316920b4e625" class="">
</p><p id="adcdb65f-93fc-43c4-9c91-53d5b970b158" class="">문제 570) 사원 테이블에 월급에 인덱스를 생성하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="78e32525-2074-4b9a-9364-9b25ce49bde3" class="code"><code class="language-SQL">CREATE INDEX emp_sal -- 이름은 반드시 문자로 작성
ON emp(sal);</code></pre><p id="475ecba0-59fa-4391-a85f-57dbf2cc1f21" class="">
</p><p id="7d118e65-53ca-49a7-994d-eb15a5cdc8c6" class="">문제 571) 사원 테이블에 월급에 인덱스가 잘 생성되었는지 데이터 사전을 조회해서 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="7c9c488b-d62a-4745-8884-68188d167f90" class="code"><code class="language-SQL">SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP&#x27;; -- 여기서 테이블 이름은 반드시 대문자로 작성</code></pre><figure id="a765ba0c-52e3-4d31-a9ba-9f4e94375e38" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%204.png"><img style="width:697px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%204.png"/></a></figure><p id="973843bb-e053-44a1-aa09-82cc220b5cca" class="">⇒ 테이블 명을 반드시 대문자로 작성해야 검색이 되는 이유는 테이블 창에 생성된 테이블 명이 대문자이기 때문에 (이름 검색할 때 대문자면 대문자로 검색하는 것처럼)</p><p id="58565bd5-fa00-458b-8dbe-6618897e3bde" class="">
</p><p id="81024c05-f23c-4ea6-ae1f-923503ddaccf" class="">문제 572) emp_sal 인덱스가 어떻게 생겼는지 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="0f0c6a6a-000c-4918-b1c1-fdd1a6c74174" class="code"><code class="language-SQL">SELECT sal, rowid
 FROM emp
 WHERE sal &gt;= 0;</code></pre><figure id="b5d4bab9-9d75-46e8-b4bd-58eea439b846" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%205.png"><img style="width:204px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%205.png"/></a></figure><p id="f3d572b9-ab2f-4b0d-a6a3-bb6cb7a7b51f" class="">⇒ ORDER BY절을 사용하지 않았는데도 컬럼값이 ASC로 정렬이 되어있습니다. 이는 테이블에서 이 데이터를 읽어온게 아니라 emp_sal 인덱스에서 데이터를 읽어왔기 때문입니다. 그래서 인덱스는 rowid로 구성되어있고 컬럼값은 ascending하게 정렬이 되어있습니다.</p><p id="aa3ec25a-e2fa-4329-87d1-0d47a19c0ac1" class="">
</p><p id="2a33d4dd-4c22-4ba8-a219-2986da721365" class="">⇒ 인덱스에서 데이터를 읽어오려면 반드시 WHERE 절이 필요합니다. WHERE 절에 줄 조건은</p><ul id="c418fd8b-bf6d-4e77-a37b-e55a4d3ce845" class="bulleted-list"><li style="list-style-type:disc">숫자 &gt; = 0</li></ul><ul id="199663f9-1b1f-455b-8a36-822221d42091" class="bulleted-list"><li style="list-style-type:disc">문자 &gt; ‘   ‘</li></ul><ul id="73cebd63-5306-4bd4-9140-49824b6669b7" class="bulleted-list"><li style="list-style-type:disc">날짜 &lt; TO_DATE(’9999/12/31’, ‘RRRR/MM/DD’)</li></ul><p id="5a82d823-275f-4d2e-996f-1174df990385" class="">
</p><p id="7613a0cb-641a-4ac5-abcb-1211d58c67d5" class="">문제 573) 월급이 3000인 사원의 이름과 월급을 출력하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="9a8084b8-4460-4cf0-9648-06d8ae153c9b" class="code"><code class="language-SQL">SELECT ename, sal
 FROM emp
 WHERE sal &gt;= 3000;</code></pre><p id="1f1e8a1d-ad9a-469e-925e-47c379c37bdf" class="">
</p><p id="2caef01b-929a-48c8-950b-149392882b15" class="">문제 574) 위의 데이터를 검색할 때 인덱스를 통해서 테이블의 데이터를 검색했는지 아니면 그냥 테이블을 FULL TABLE SCAN을 했는지 실행계획을 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="bb389bbd-bd9b-4cf9-9224-39550c626226" class="code"><code class="language-SQL">EXPLAIN PLAN FOR
SELECT ename, sal
 FROM emp
 WHERE sal &gt;= 3000;
 
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);</code></pre><figure id="861dcfa9-2fc3-4a4a-90d8-38916dccf6a1" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%206.png"><img style="width:565px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%206.png"/></a></figure><figure id="f68525fe-9a29-404e-89de-c8d131546f91" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%207.png"><img style="width:565px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%207.png"/></a></figure><ul id="913039f6-f8ba-4ef0-bb28-d426f8279847" class="bulleted-list"><li style="list-style-type:disc">실행계획 읽는 순서 : ID 2 → 1 → 0</li></ul><ul id="e3ea62f6-28e0-47e3-aee0-7cb73d763721" class="bulleted-list"><li style="list-style-type:disc">실행계획을 읽는 방법은 안쪽에서 바깥쪽으로 읽으면 됩니다. 지금 실행하는 실행계획에서는 emp_sal 인덱스를 먼저 range scan 하고 emp_sal 인덱스의 rowid에 의해서 테이블을 엑세스하는 실행 계획입니다.</li></ul><p id="298dfe67-0178-4911-a826-b8bb39bdd3c6" class="">
</p><p id="f9a3e3aa-4474-4de8-b3e6-9c3a9487481d" class="">문제 575) 이름이 SCOTT인 사원의 이름과 월급을 출력하는 쿼리문의 실행계획을 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b5b7c1c3-69ae-4dee-8611-f30bc785dfd2" class="code"><code class="language-SQL">EXPLAIN PLAN FOR
SELECT ename, sal
 FROM emp
 WHERE ename = &#x27;SCOTT&#x27;;
 
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);</code></pre><figure id="958f1a15-fd2a-4034-9c07-0b2b659db79e" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%208.png"><img style="width:534px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%208.png"/></a></figure><figure id="5634987f-9ec4-46a1-a119-c172f5487aea" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%209.png"><img style="width:1090px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%209.png"/></a></figure><p id="d0cf68ad-a357-4874-aca1-82456b1a513f" class="">
</p><p id="552c55b4-9e4c-4c64-9209-9e37a7aa8788" class="">문제 576) 위의 SQL의 검색 속도를 높이기 위해서 emp 테이블 ename에 인덱스를 생성하세요</p><ul id="5f26ffb6-21df-4d1e-b5cb-bf66d97c5041" class="bulleted-list"><li style="list-style-type:disc">이름 컬럼 인덱스 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="5cd318d5-a971-489c-95f3-297f79f8fafd" class="code"><code class="language-SQL">CREATE INDEX emp_ename
 ON emp(ename);</code></pre><ul id="49365d35-6613-421b-8c72-33ece58ecf65" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="ef155285-f024-4982-8b0f-103c54fa60ef" class="code"><code class="language-SQL">SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP&#x27;;</code></pre><figure id="8010ce92-cb96-429a-8706-4b21b84da3e7" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2010.png"><img style="width:587px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2010.png"/></a></figure><p id="9987f9ed-28a5-4bbe-8ae4-33fde564c672" class="">⇒ WHERE절에 검색하는 데이터가 뭔지 확인해서 그 컬럼에 인덱스를 생성해야 해당 쿼리문의 검색속도를 높일 수 있습니다.</p><p id="ebbf5a79-6cf6-4aee-a8ac-f728646da4ac" class="">인덱스 하나만 잘 생성해도 수많은 SQL 튜닝을 할 필요가 없어집니다.</p><p id="9f55ffee-6050-427d-a465-c8cc52c98f5d" class="">
</p><p id="4fd169dc-7e15-4ff6-8fbd-54f4764900db" class="">문제 577) 위의 SQL의 실행 계획을 확인하세요</p><ul id="c34eaa8d-d373-4ef4-b0c0-6493433a9097" class="bulleted-list"><li style="list-style-type:disc">SQL 실행 결과 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="4ecfdf44-8202-4c17-8cb8-4d896617637a" class="code"><code class="language-SQL">EXPLAIN PLAN FOR
SELECT ename, sal
 FROM emp
 WHERE ename = &#x27;SCOTT&#x27;;
 
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);</code></pre><figure id="498a8990-6cc4-4810-97f2-fc757ac7a754" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2011.png"><img style="width:435px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2011.png"/></a></figure><figure id="e7f97248-e284-4a46-92e1-6f8298d69950" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2012.png"><img style="width:565px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2012.png"/></a></figure><p id="0c8aba9c-a796-4506-b335-d14102c58cad" class="">
</p><p id="6c647fef-b699-4d66-8675-269d6a1bf0fa" class="">문제 578) emp-ename 인덱스의 구조를 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="70d3c1ad-ca5c-424a-82a3-6e57b710e277" class="code"><code class="language-SQL">SELECT ename, rowid
 FROM emp
 WHERE ename &gt; &#x27; &#x27;; -- 공백문자 하나 넣기 =&gt; 공백문자 하나 보다 큰 것</code></pre><p id="4764d169-005f-44be-ae8c-560835d915dd" class="">⇒ emp_ename 인덱스는 문자형 컬럼이라서 컬럼이 ABCD 순서대로 저장되어있고 컬럼값 + rowid로 인덱스가 구성되어 있습니다.</p><p id="4e0060a0-430c-4e01-9720-838a13664c8a" class="">
</p><p id="dfcb9952-83f7-44e9-b6a8-97fea77a0048" class="">문제 579) 아래의 SQL의 검색속도를 높이기 위해서 인덱스를 생성하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="3fcaf1a2-2934-4cbe-82bb-e140c778e086" class="code"><code class="language-SQL">SELECT ename, hiredate
 FROM emp
 WHERE hiredate = TO_DATE(&#x27;81/11/17&#x27;, &#x27;RR/MM/DD&#x27;);</code></pre><ul id="a3b95251-29e5-4577-b932-4780ad1ffaf7" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="5e02edaa-2d21-4ea0-9594-f17088768126" class="code"><code class="language-SQL">CREATE INDEX emp_hiredate
 ON emp(hiredate);</code></pre><ul id="a7e1798e-e00d-4ef1-b63a-1a3b984f2568" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="ad376cc8-4496-4c93-a419-d8e195d69516" class="code"><code class="language-SQL">SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP&#x27;;</code></pre><ul id="2a88ad9d-b092-453f-88c7-adb5a040eb9e" class="bulleted-list"><li style="list-style-type:disc">SQL 실행 결과 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="73f18585-c6b0-4c70-9bae-48d6b3c23489" class="code"><code class="language-SQL">EXPLAIN PLAN FOR
SELECT ename, hiredate
 FROM emp
 WHERE hiredate = TO_DATE(&#x27;81/11/17&#x27;, &#x27;RR/MM/DD&#x27;);
 
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);</code></pre><figure id="234e0f93-6ab3-40fe-ba2e-8ee5ba30ad1b" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2013.png"><img style="width:484px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2013.png"/></a></figure><p id="d554692d-5a49-42df-a2af-9c275e77d719" class="">
</p><p id="7de18eee-ade3-4747-b3e9-26da6075ffda" class="">문제 580) 아래의 SQL의 검색속도를 높이기 위해서 적절한 인덱스를 생성하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="1254076b-2166-48d6-8489-89d47c751db7" class="code"><code class="language-SQL">SELECT ename, sal, deptno
 FROM emp
 WHERE deptno = 10;</code></pre><ul id="668db91f-079b-4b55-891e-0629709310d0" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="e27dba3c-712c-4a6f-8397-60e5d7918280" class="code"><code class="language-SQL">CREATE INDEX emp_deptno
 ON emp(deptno);</code></pre><ul id="0ad73978-3ede-4bda-bfde-a53872eca9f9" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="e7274cbb-e343-4f10-ae54-83d1b05d286d" class="code"><code class="language-SQL">SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP&#x27;;</code></pre><ul id="1a492c07-f637-48b7-9ea7-008ea9529381" class="bulleted-list"><li style="list-style-type:disc">SQL 실행 계획 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="d620faad-caf3-4970-a8b9-017a92588ac2" class="code"><code class="language-SQL">EXPLAIN PLAN FOR
SELECT ename, sal, deptno
 FROM emp
 WHERE deptno = 10;
 
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);</code></pre><figure id="02bff138-ca76-478e-9e9f-e7eb0ff617cb" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2014.png"><img style="width:475px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2014.png"/></a></figure><p id="b4912896-26d6-4f2a-b90c-77cd40c655b6" class="">⇒ emp 테이블이 14건 밖에 안되서 인덱스가 있던 없던 상관없이 빠르게 데이터가 검색되어서 튜닝을 한 것 같지가 않습니다. 그래서 튜닝한 효과를 볼 수 있도록 buffer의 갯수를 확인해서 튜닝을 하겠습니다.</p><p id="89b0df93-df6a-45aa-9273-e8f84beec85b" class="">
</p><p id="d2a0d74d-e0e4-4725-b239-82ef55a74242" class="">문제 581) emp 테이블에 걸린 모든 인덱스를 다 삭제하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="02814568-9fd6-4376-a9ae-1f6c04aed952" class="code"><code class="language-SQL">DROP INDEX emp_sal;
DROP INDEX emp_ename;
DROP INDEX emp_hiredate;
DROP INDEX emp_deptno;

SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP&#x27;;</code></pre><p id="037b1dcc-b25b-40e9-bf39-e45680ed4506" class="">
</p><p id="2f879b31-6c8b-4fbe-894a-1d716bc2fea9" class="">문제 582) 아래의 SQL의 실행계획을 확인하는데 BUFFER의 갯수도 확인할 수 있게 실행계획을 출력하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="81439bee-a82f-48f0-b4b2-cecc97c5bdd0" class="code"><code class="language-SQL">SELECT ename, sal
 FROM emp
 WHERE sal = 3000;</code></pre><ul id="6ce059c0-ffb9-4c80-925a-32cd773489f8" class="bulleted-list"><li style="list-style-type:disc">실행계획 확인 (실제 실행계획 - buffer 출력)</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="097b5bb4-1bd3-424c-970c-aefa87a76562" class="code"><code class="language-SQL">SELECT /*+ GATHER_PLAN_STATISTICS */ ename, sal
 FROM emp
 WHERE sal = 3000;
 
SELECT * 
 FROM TABLE(dbms_xplan.display_cursor(null, null, &#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="f89c4aa7-f8ea-49e3-8100-ed3e99fa3bac" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2015.png"><img style="width:565px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2015.png"/></a></figure><p id="7a84ce7c-77f0-478a-aa38-2376adecdf30" class="">⇒ FULL TABLE SCAN 하면서 buffer 의 갯수를 7개를 읽었습니다.</p><h3 id="74c5c517-91db-4e01-9cec-75f0feb32cbd" class="">실행 계획 보는 방법 2가지 ?</h3><p id="f7f5b8c6-5d42-47f5-972d-3867142f3bb5" class="">1) 예상 실행계획</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="6042c904-092c-4d94-911b-3896c45255b3" class="code"><code class="language-SQL">explain  plan  for
select ename, sal
 from emp
 where ename=&#x27;SCOTT&#x27;;

SELECT * from table(dbms_xplan.display);</code></pre><p id="8401bf65-0240-423f-9fd2-2f41e3a872cb" class="">2. 실제 실행계획 (버퍼를 확인할 수 있음)</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="6c75be0f-4391-4f65-b54c-529232976004" class="code"><code class="language-SQL">select /*+ gather_plan_statistics */ ename, sal
 from  emp
 where  ename =&#x27;SCOTT&#x27;; 

SELECT * 
 FROM TABLE(dbms_xplan.display_cursor(null,null,&#x27;ALLSTATS LAST&#x27;)); </code></pre><p id="38b7ee66-dda6-480c-bcc5-7ef71dcf017e" class="">
</p><p id="0d4d769a-2dab-48fd-9d99-3e2c01e32e47" class="">문제 583) 아래의 SQL을 튜닝하세요 (인덱스를 생성합니다)</p><p id="0b2fb4d8-f53e-4383-a173-2e0eb1842c8b" class="">버퍼의 갯수가 줄어드는지 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="3a9249d4-ce33-49b1-aa64-565f0b9774d2" class="code"><code class="language-SQL">SELECT ename, sal
 FROM emp
 WHERE sal = 3000;</code></pre><ul id="4c85f4bd-285d-423c-b292-6c0215bf387f" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="ea450d95-5afb-44a3-b7e4-7f51eedeea18" class="code"><code class="language-SQL">CREATE INDEX emp_sal
 ON emp(sal);</code></pre><ul id="41e0c365-5ccc-45d5-95a9-78d593026a62" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="131b08e7-6aed-472f-9e06-f3955fdd4051" class="code"><code class="language-SQL">SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP&#x27;;</code></pre><ul id="601b9a6f-8ba4-497d-bb45-e63b593804d3" class="bulleted-list"><li style="list-style-type:disc">위의 SQL을 실행하고 실행계획 확인 (버퍼를 확인하기 위해 2번 실행계획으로 출력)</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="d2d35241-09e8-438f-b751-c99169063ef1" class="code"><code class="language-SQL">SELECT /*+ gather_plan_statistics */ ename, sal
 FROM emp
 WHERE sal = 3000;
 
SELECT * 
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL,&#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="0e9c8886-bc88-4f0e-98e0-51ca337aadeb" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2016.png"><img style="width:751px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2016.png"/></a></figure><p id="526d7802-dbfe-4aab-a722-a56c7526784e" class="">⇒ 버퍼가 2개로 줄어들었음 ⇒ 튜닝이 되었다는 의미</p><p id="cfa8bea6-ba9d-47bb-93d6-386af40d5c4e" class="">
</p><p id="cff54d39-2501-4983-ac1d-94c5abf651d7" class="">문제 584) (SQL 튜너 직업체험) 아래의 SQL을 튜닝하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="08b2bbae-1b5e-4672-9566-749ffe008107" class="code"><code class="language-SQL">SELECT ename, age
 FROM emp19
 WHERE ename = &#x27;이원석&#x27;;</code></pre><ul id="04bdde9c-4ff5-4d23-b3cd-7c400f19ac20" class="bulleted-list"><li style="list-style-type:disc">튜닝 전 실행 계획 출력 및 버퍼 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="e93c7b9b-47df-4308-88ac-a76c1209ebfa" class="code"><code class="language-SQL">SELECT /*+ gather_plan_statistics */ ename, age
 FROM emp19
 WHERE ename = &#x27;이원석&#x27;;

SELECT * 
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL,&#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="b7bfd7d2-715e-4a60-a929-d7b5f72f5e9e" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2017.png"><img style="width:129px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2017.png"/></a></figure><ul id="be18f451-ebfd-4ffa-919c-a769d203ae94" class="bulleted-list"><li style="list-style-type:disc">튜닝하기 위한 인덱스 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="d2c5deed-a434-4b57-a429-2267c6e5f9f9" class="code"><code class="language-SQL">CREATE INDEX emp19_ename
 ON emp19(ename);</code></pre><ul id="6a7f1aa2-0a31-4af6-b118-bfa56ff9275a" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="83301763-6764-43be-bc19-979e4c4a1f2b" class="code"><code class="language-SQL">SELECT *
 FROM user_indexes
 WHERE table_name = &#x27;EMP19&#x27;;</code></pre><ul id="36c7c2fe-499b-418e-866e-66c0b50a78c7" class="bulleted-list"><li style="list-style-type:disc">위의 SQL을 실행하고 실행 계획을 출력해서 버퍼가 줄어들었는지 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="164bd8d2-a39f-4183-8881-41e51fc2d530" class="code"><code class="language-SQL">SELECT /*+ gather_plan_statistics */ ename, age
 FROM emp19
 WHERE ename = &#x27;이원석&#x27;;

SELECT * 
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL,&#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="6834fef7-b3c5-4824-a2d5-cb1eeffd7a65" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2018.png"><img style="width:89px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2018.png"/></a></figure><p id="7aaea30c-b2aa-414a-a965-61213f5188a1" class="">⇒ 버퍼가 줄어들었음</p><h3 id="67b79522-0ed8-46a5-9a95-ab5d7c9a28d5" class="">인덱스가 이미 있는데도 불구하고 SQL을 잘 못 작성해서 성능이 느린 경우가 많기 때문에 SQL 튜닝이 필요합니다.</h3><p id="991c92bb-3a91-4923-9141-db381a8ceb1c" class="">
</p><p id="95b30738-94cd-4383-825f-40dda4c71729" class="">문제 585) 아래의 SQL의 실제 실행계획을 확인하세요</p><ul id="2607c641-2ff0-4502-b5ca-63c717af2411" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="788df585-4b43-4c35-aa99-a7576e8c2ec2" class="code"><code class="language-SQL">SELECT ename, sal
 FROM emp
 WHERE sal * 12 &gt;= 36000;</code></pre><ul id="9c7a0ab6-8c8d-4cbf-8470-5deb77e53e36" class="bulleted-list"><li style="list-style-type:disc">실제 실행계획 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b885b5c0-01a1-42a9-9692-e4a866e046d6" class="code"><code class="language-SQL">SELECT /*+ gather_plan_statistics */ ename, sal * 12 AS 연봉
 FROM emp
 WHERE sal * 12 &gt;= 36000;
 
SELECT * 
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL,&#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="e3a32121-283f-4719-8caf-c3c0c347a514" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2019.png"><img style="width:622px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2019.png"/></a></figure><p id="65665900-c32a-4272-876a-73c523955620" class="">⇒ emp_sal 의 인덱스가 존재함에도 불구하고 FULL TABLE SCAN을 해서 버퍼가 갯수가 7개임 ⇒ 그 이유는 sal 에 * 12를 했기 때문입니다.</p><p id="04e60785-e1a2-4811-92fa-4bd1ed6c9309" class="">⇒ 이것을 전문용어로 <mark class="highlight-red_background">인덱스 컬럼을 가공했다</mark>라고 합니다. 인덱스 컬럼을 가공하면 인덱스가 존재해고 테이블 전체를 스캔함 ⇒ 튜닝이 적용되지 않음</p><p id="c4c35187-b2de-4c37-95b1-71c4966fea3d" class="">
</p><p id="2318990d-a9c5-419d-a50f-a8ffbc8b1541" class="">문제 586) (직업 체험) 위의 SQL을 튜닝하세요</p><ul id="bbf2cb7a-a943-4bc5-98bb-3c908545acfc" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="c049f7db-2375-4588-a252-6916e3982c1a" class="code"><code class="language-SQL">SELECT /*+ gather_plan_statistics */ ename, sal * 12 AS 연봉
 FROM emp
 WHERE sal * 12 &gt;= 36000;
 
SELECT * 
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL,&#x27;ALLSTATS LAST&#x27;));</code></pre><ul id="a0b21fd3-18a2-4609-8ff6-3420f33ba7cc" class="bulleted-list"><li style="list-style-type:disc">튜닝 후</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="05d4e983-240a-404f-9ac6-a81d97bfba54" class="code"><code class="language-SQL">SELECT /*+ gather_plan_statistics */ ename, sal * 12 AS 연봉
 FROM emp
 WHERE sal &gt;= 36000 / 12; -- sal 에 있던 연산을 오른쪽 값에다가 옮겨 줌
 
SELECT * 
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL,&#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="e3b9da28-62f0-40ff-9f16-fd8138a75b11" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2020.png"><img style="width:565px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2020.png"/></a></figure><p id="54c7a480-1cc7-417b-a4f9-5a8245aa8678" class="">
</p><p id="11883ff7-e187-4f87-b7ef-68a1d221b550" class="">문제 587) 아래의 SQL을 튜닝하세요</p><ul id="f966c00c-c079-4c91-9c23-4f6936ff1601" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="5a67a1aa-7817-4461-aba8-7f4db6905e07" class="code"><code class="language-SQL">SELECT ename, job
 FROM emp
 WHERE job = &#x27;SALESMAN&#x27;;</code></pre><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="d0279cd8-e368-401b-a231-40933a087fcb" class="code"><code class="language-SQL">-- 튜닝 전의 실행계획 확인
SELECT /*+ GATHER_PLAN_STATISTICS */ ename, job
 FROM emp
 WHERE job = &#x27;SALESMAN&#x27;;
 
SELECT *
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, &#x27;ALLSTATS LAST&#x27;));
 
-- 인덱스 생성
CREATE INDEX emp_job
 ON emp(job);
 
-- 다시 실행계획 확인
SELECT /*+ GATHER_PLAN_STATISTICS */ ename, job
 FROM emp
 WHERE job = &#x27;SALESMAN&#x27;;
 
SELECT *
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, &#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="fa51a7aa-c75b-480d-8a21-e40f24434382" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2021.png"><img style="width:96px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2021.png"/></a></figure><p id="78a12847-8c0c-486c-abc3-4e6c32ab03bc" class="">⇒ 버퍼의 갯수가 7개에서 2개로 줄어들었습니다.</p><p id="8d488a46-83ff-4258-b798-28ad9ac6c67c" class="">
</p><p id="28faa6ac-679d-41af-a851-9e38f064425e" class="">문제588)  (직업체험) 아래의 SQL을 튜닝하시오 !  답글로 올려주세요 ~</p><ul id="0c9a3552-0040-4426-acf5-3996bf89ecef" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="45902453-e924-4017-9535-2ddb161ff787" class="code"><code class="language-SQL">SELECT ename, job
 FROM emp
 WHERE SUBSTR(job, 1, 5) = &#x27;SALES&#x27;;</code></pre><p id="934f908b-f759-47f7-ab66-cb32610d7457" class="">⇒ job 에 인덱스가 생성되어 있지만 위의 SQL은 full table scan 을 합니다.<br/>왜냐하면 where 절에 인덱스 컬럼이 가공되었기 때문입니다.<br/>substr 이라는 함수로 job 이 둘러싸여있습니다.<br/>그러면 인덱스를 사용하지 못하고 full table scan을 하게 됩니다.<br/>그래서 튜닝 방법이 where job ? 이어야합니다.<br/></p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="7befd048-6409-4262-b81b-92b76684ae00" class="code"><code class="language-SQL">SELECT /*+ GATHER_PLAN_STATISTICS */ ename, job
 FROM emp
 WHERE substr(job, 1, 5) = &#x27;SALES&#x27;;

SELECT *
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, &#x27;ALLSTATS LAST&#x27;));</code></pre><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="450fdeb5-1f20-4296-bca9-9f9931aa2592" class="code"><code class="language-SQL">SELECT /*+ GATHER_PLAN_STATISTICS */ ename, job
 FROM emp
 WHERE job LIKE &#x27;SALES%&#x27;;

SELECT *
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, &#x27;ALLSTATS LAST&#x27;));</code></pre><p id="087cb70b-31de-4b83-b2a3-78e321a39935" class="">⇒ LIKE로 연산자를 작성하고 와일드 카드(%)는 뒤쪽에 있어야 인덱스를 통해 검색됩니다.</p><p id="b3a410bd-45df-47d6-a36b-416bd6a8e558" class="">
</p><p id="b0b186e9-fb1e-455f-ab18-7df0badb7934" class="">문제 589) (점심시간 문제) 아래의 SQL을 튜닝하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="ddfd1a5e-2213-4356-b730-3b3425340b9f" class="code"><code class="language-SQL">CREATE INDEX emp_hiredate
 ON emp(hiredate);</code></pre><ul id="30357173-e613-4cf5-88e6-9ce287bfc856" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="d5127ed1-f83b-4b28-a913-0a92efb7c6f2" class="code"><code class="language-SQL">SELECT /*+ GATHER_PLAN_STATISTICS */ ename, hiredate
 FROM emp
 WHERE TO_CHAR(hiredate, &#x27;RRRR&#x27;) = &#x27;1980&#x27;;
 
SELECT *
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, &#x27;ALLSTATS LAST&#x27;));</code></pre><ul id="3a5889b7-cb6e-4873-b8e3-7390569c5586" class="bulleted-list"><li style="list-style-type:disc">튜닝 후</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="4837e563-4341-4f8d-8ce5-d7afae525af9" class="code"><code class="language-SQL">SELECT /*+ GATHER_PLAN_STATISTICS */ ename, hiredate
 FROM emp
 WHERE hiredate BETWEEN TO_DATE(&#x27;1980/01/01&#x27;, &#x27;RRRR/MM/DD&#x27;)
                    AND TO_DATE(&#x27;1980/12/31&#x27;, &#x27;RRRR/MM/DD&#x27;);
 
SELECT *
 FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(NULL, NULL, &#x27;ALLSTATS LAST&#x27;));</code></pre><figure id="275af77d-97ab-45ae-9c08-b989a7c113a7" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2022.png"><img style="width:116px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2022.png"/></a></figure><p id="a7224752-c75c-4a75-8b66-5c944c295f51" class="">⇒ WHERE절에 인덱스 컬럼을 가공하면 FULL TABLE SCAN을 하게 되므로 인덱스 컬럼을 가공하면 안된다</p><h3 id="1fb5524f-3980-4b86-bf03-19b4b9dea580" class=""><mark class="highlight-yellow_background">※ 인덱스 생성 지침을 따르세요</mark></h3><figure id="ee0102e9-1a99-4e21-aa66-094cf63328c5" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2023.png"><img style="width:612px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2023.png"/></a></figure><ol type="1" id="719a6bf4-f61e-4d4e-b9ba-529740f480dd" class="numbered-list" start="1"><li>emp 테이블 처럼 작은 테이블에 인덱스를 걸면 별로 효과를 못봅니다. 데이터가 많은 테이블에 인덱스를 생성해야 인덱스 효과를 볼 수 있습니다.</li></ol><ol type="1" id="3cd125af-2ac5-4773-93ff-5c54e49b7654" class="numbered-list" start="2"><li>emp 테이블의 커미션 처럼 NULL 값이 많은 컬럼에 인덱스를 걸면 효과가 좋습니다. NULL 값은 인덱스로 구성이 안됩니다. 책도 빈 페이지는 목차에 안 나옵니다. 굳이 빈 페이지를 목차로 구성할 필요는 없습니다. NULL 이 아닌 값들만으로 인덱스가 구성이 됩니다. 어떤 책의 내용에 절반 넘게 빈 페이지가 있으면 FULL TABLE SCAN을 하게 되면 넘길 때 마다 빈 페이지니까 검색 시간만 오래걸리게 됩니다.</li></ol><ol type="1" id="1b3b2d7d-a8ee-405a-ac4e-d98f04fb1a0d" class="numbered-list" start="3"><li><mark class="highlight-red"><strong>!! 중요 !! WEHRE절에 자주 등장하는 컬럼에 인덱스를 생성하는게 바람직합니다.</strong></mark></li></ol><ol type="1" id="f045d194-efbf-4a8e-802b-7a117a7be6c7" class="numbered-list" start="4"><li>검색하려는 데이터의 전체 테이블의 데이터 중에서 <mark class="highlight-red_background">2~4% 미만</mark>인 컬럼에 인덱스를 거는게 바람직합니다.</li></ol><ul id="2f121501-54f3-48a5-bfbe-bf92633fdaf1" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성에 바람직한 컬럼</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b6e4c4aa-cec6-4031-ade2-45741aad7bd8" class="code"><code class="language-SQL">SELECT ename, sal
 FROM emp
 WHERE empno = 7788;</code></pre><ul id="42e171fa-8516-494b-8523-82cf5aa7d9cd" class="bulleted-list"><li style="list-style-type:disc">인덱스 생성에 바람직한 컬럼</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="0fad038c-3d3f-4fde-ba74-efb92055a51a" class="code"><code class="language-SQL">SELECT ename, gender
 FROM emp19
 WHERE gender = &#x27;남&#x27;;</code></pre><p id="f0aba4d7-fd37-4ddf-85bf-90511d0ca018" class="">⇒ 검색하려는 데이터가 테이블의 50%면 그냥 FULL TABLE SCAN이 더 빠릅니다.</p><h3 id="f9d616a9-445d-47ba-ae1e-544de039dcba" class=""><mark class="highlight-red_background">※ 인덱스를 생성하면 안되는 경우</mark></h3><ol type="1" id="082d5a10-3990-45d4-835f-2c98c4620692" class="numbered-list" start="1"><li>WHERE 절에서 자주 검색되지 않는 컬럼</li></ol><ol type="1" id="188cb9e9-3db6-4d28-a99c-ac4936ec7f64" class="numbered-list" start="2"><li>emp 테이블 처럼 작거나 검색하려는 데이터가 전체 데이터에 2~4% 이상으로 검색하려고 할 때</li></ol><ol type="1" id="f4d60b39-f260-4cab-93c5-dff2b93d78c9" class="numbered-list" start="3"><li>자주 갱신되는 컬럼 (⇒ 업데이트가 자주 일어나는 컬럼)<ul id="5a69e2aa-5095-4b74-839a-c17292e99638" class="bulleted-list"><li style="list-style-type:disc">테이블의 데이터를 자주 갱신하면 인덱스도 자주 갱신되어야합니다.</li></ul></li></ol><p id="6212f761-c396-4bcd-a267-934251bd0b0a" class="">⇒ 테이블의 이름 BLAKE를 JANE으로 변경했으면 테이블은 변경이 되지만 인덱스는 변경되지 않고 새로운 데이터가 입력이 됩니다. 테이블에 UPDATE가 많아지면 인덱스가 점점 커집니다.</p><p id="69fbddbc-2d48-40fe-96de-5b5851096344" class="">
</p><p id="4e883326-0c6e-4aba-b5af-44fc417794cb" class=""><mark class="highlight-blue_background">결론 !! 어떤 컬럼에 인덱스를 생성해야하나요 ?</mark></p><ol type="1" id="adb38fb2-dca8-43e2-bd81-354c76ece89c" class="numbered-list" start="1"><li>큰 테이블 (몇 백만 건 ~ 몇 천만 건)</li></ol><ol type="1" id="ba260087-c572-4836-8d1e-9a1976342aa7" class="numbered-list" start="2"><li>WHERE절에서 자주 검색되는 컬럼</li></ol><ol type="1" id="8aecd36c-88e9-41a7-ab2a-7997362b950c" class="numbered-list" start="3"><li>검색하려는 데이터가 전체 데이터에서 2~4% 미만인 컬럼</li></ol><ol type="1" id="20a86725-e578-4ffa-b34f-496a78aa2544" class="numbered-list" start="4"><li>NULL 값이 많은 컬럼</li></ol><p id="a2a2e618-710b-429f-8877-76455ede414c" class="">
</p><p id="fdfe3395-7f63-4615-a541-722096ec06da" class=""><mark class="highlight-red_background">어떤 컬럼에 인덱스를 생성하지 않는게 바람직한가 ?</mark></p><ol type="1" id="4428a1df-c322-4d4f-8414-4828cd6f1c2a" class="numbered-list" start="1"><li>자주 UPDATE 되는 컬럼</li></ol><p id="d0d71731-6c4c-4c5a-bcfa-70964daf85a9" class="">
</p><p id="4d252d71-396b-4d55-abd6-b17546ffb7c9" class="">문제 590) 내가 가지고 있는 인덱스 리스트를 확인하고 전부 DROP 하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="55d43cdf-b372-4fe4-b474-98daf8f70fc8" class="code"><code class="language-SQL">SELECT index_name
 FROM user_indexes;</code></pre><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="41e18220-5853-4cdb-b7b9-4d71d65293e5" class="code"><code class="language-SQL">DROP INDEX EMP19_BIRTH;
DROP INDEX EMP_JOB;
DROP INDEX EMP_SAL;
DROP INDEX EMP19_ENAME;
DROP INDEX EMP_HIREDATE;

-- 혹은

SELECT &#x27;DROP INDEX&#x27;||index_name||&#x27;;&#x27;
 FROM user_indexes;
 
-- 해서 나온 출력값 복사해서 붙여넣기</code></pre><p id="b325f37a-78f6-4b82-b189-ad879cde61bb" class="">
</p><h3 id="67f530ae-72fd-4fe7-a7bb-7f46293aa885" class="">98. 절대로 중복되지 않는 번호 만들기 (SEQUENCE)</h3><p id="89d011f9-b574-455d-86c1-f5c05b2cd1f0" class="">테이블에 empno 같은 값처럼 unique한 컬럼이 있어야 데이터 검색이나 머신러닝을 이용한 예측을 할 때 잘 할 수 있습니다.</p><p id="5cb31d9f-02e5-40f4-9eed-fa1bdf14785e" class="">사람이 emp 테이블에 empno에 값을 입력하게 되면 사람이 하는 일이다보니 실수를 해서 중복된 데이터를 입력할 수 있습니다. 그래서 시퀀스를 이용해서 값을 unique하게 생성합니다.</p><ul id="dce72f14-c616-4164-9dc7-697d0d3a332f" class="bulleted-list"><li style="list-style-type:disc">시퀀스 생성 문법</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f374b31a-02f6-4962-a957-ab5ba9028797" class="code"><code class="language-SQL">CREATE SEQUENCE seq1
START WITH 1
INCREMENT BY 1
MAXVALUE 10000;

SELECT seq1.NEXTVAL
 FROM dual;</code></pre><ul id="7c1b75c5-90db-446d-96f3-1f4d679ac2d4" class="bulleted-list"><li style="list-style-type:disc">시퀀스 삭제</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="59ddae6c-97d7-4eb5-8edf-758367c161ee" class="code"><code class="language-SQL">DROP SEQUENCE seq1;</code></pre><p id="3c1076c7-b6b1-40af-970c-0650fc029af7" class="">
</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="30ec866a-05a2-4ebf-91bc-f8807175da7f" class="code"><code class="language-SQL">CREATE TABLE emp923
(empno NUMBER(10),
 ename VARCHAR2(10) );</code></pre><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="7b7c3408-b12a-4cd8-b68c-57bc8ce0cce8" class="code"><code class="language-SQL">INSERT INTO emp923
 VALUES(seq1.NEXTVAL, &#x27;no name&#x27;);

SELECT * FROM emp923;</code></pre><figure id="5ebce8b1-103f-4c89-acb2-98bf8c5baa77" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2024.png"><img style="width:156px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2024.png"/></a></figure><ul id="22e5556f-1bc6-436e-809c-3dcfacd96bf7" class="bulleted-list"><li style="list-style-type:disc">만약에 시퀀스가 없었거나 또는 시퀀스라는게 있는지 모르는 회사에서는 다음과 같이 INSERT를 합니다.</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="984c69ae-ba0f-428f-b35c-a9ed78a22e45" class="code"><code class="language-SQL">INSERT INTO emp923 VALUES(34, &#x27;no name&#x27;);

SELECT MAX(empno) + 1
 FROM emp923;
 
INSERT INTO emp923 VALUES(35, &#x27;no name&#x27;);</code></pre><p id="5efd336d-1a3e-4d6a-8f33-ac648a2d414a" class="">⇒ 시퀀스가 없다면 위와 같이 몇번까지 데이터가 입력되었는지 확인해서 입력을 해야합니다.</p><p id="a8f2a0bd-2d99-472b-b908-c8997cc999d3" class="">
</p><p id="ec84d1f5-9eda-4f8c-b3b3-a4aa38e5c4c1" class="">문제 591) 만들어진 시퀀스를 확인하고 시쿼스를 삭제하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="71be0178-a4c1-4d28-b3c4-ec8792c54027" class="code"><code class="language-SQL">SELECT *
 FROM user_sequences;
 
DROP SEQUENCE seq1;</code></pre><p id="2e03a05d-f14c-4850-a13d-2497ecd73b8f" class="">
</p><h3 id="92e32593-40f1-415d-98f6-1c7d56e6f241" class="">99. 실수로 지운 데이터 복구하기 1 (FLASHBACK QUERY)</h3><p id="d33534d3-d6ab-4c82-adb7-e6d2eefac475" class="">
</p><h3 id="9def712c-cfc9-4698-9f2c-6e6f861275ad" class="">오라클의 타임머신 기능 !</h3><ol type="1" id="1f138d60-157e-47d1-b684-915d3cad9d18" class="numbered-list" start="1"><li>Flashback Query : 과거의 데이터를 검색하는 기능</li></ol><ol type="1" id="96a9cdea-51f7-4ed3-bd6c-d29ee4636032" class="numbered-list" start="2"><li>Flashback Table : 테이블을 과거 시점으로 되돌리는 기능</li></ol><ol type="1" id="c19c167e-3b35-4416-9eeb-1735a29065fa" class="numbered-list" start="3"><li>Flashback Drop : 테이블을 휴지통에서 복구하는 기능</li></ol><ol type="1" id="d25c0412-91dc-48f4-9462-bca6b4a65181" class="numbered-list" start="4"><li>Flashback Version Query : 테이블이 과거로부터 지금까지 어떻게 변경되어 왔는지 그 이력정보 확인</li></ol><ol type="1" id="6d257969-b191-4025-a06d-7dc648ccc307" class="numbered-list" start="5"><li>Flashback Transaction Query : 테이블을 과거로 되돌리기 위한 DML 문장을 보여주는 쿼리문 </li></ol><p id="754c2407-5662-4aff-bc4a-2a8833a043a9" class="">
</p><ul id="676ee064-be0c-4972-94ab-dde6e4e53c08" class="bulleted-list"><li style="list-style-type:disc">emp 테이블을 모두 delete하고 commit 하기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="dcce2ce8-bf53-4bde-af2f-757ef522366e" class="code"><code class="language-SQL">DELETE FROM emp;

COMMIT;</code></pre><ul id="f9c2da76-8520-45c5-8d88-0ab99681ad56" class="bulleted-list"><li style="list-style-type:disc">emp 테이블에서 지워지기 전에 데이터 상태를 확인하기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b6fb2470-b105-44eb-8af1-31a90263c052" class="code"><code class="language-SQL">SELECT *
 FROM emp
  AS OF TIMESTAMP
  TO_TIMESTAMP(&#x27;2024/06/04 14:45:00&#x27;, &#x27;RRRR/MM/DD HH24:MI:SS&#x27;);</code></pre><ul id="5b91448d-f4d1-4902-99e1-6eb865624514" class="bulleted-list"><li style="list-style-type:disc">위의 결과를 별도의 테이블로 백업하세요</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="a236ada4-7722-42e2-8c52-825b8e1f585a" class="code"><code class="language-SQL">CREATE TABLE emp_20240604
AS
SELECT *
 FROM emp
  AS OF TIMESTAMP
  TO_TIMESTAMP(&#x27;2024/06/04 14:45:00&#x27;, &#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
  
SELECT * FROM emp_20240604;</code></pre><p id="d41a5df5-6f8e-463e-b2d4-be18b7ab6292" class=""><mark class="highlight-red_background">※ 복구할 수 있는 골든타임을 놓칠 수 있으니 시간을 돌린 데이터 상태 자체를 다시 백업해서 새 테이블로 생성합니다.</mark></p><ul id="6f6c30da-e9a2-4e04-9d05-af580c4166e2" class="bulleted-list"><li style="list-style-type:disc">emp 테이블을 2024/06/04 14:45:00 초로 복구하세요</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="9e5ac3e3-a6df-4287-900e-e2b168cb783e" class="code"><code class="language-SQL">ALTER TABLE emp ENABLE ROW MOVEMENT;

FLASHBACK TABLE emp TO TIMESTAMP
 TO_TIMESTAMP(&#x27;2024/06/04 14:45:00&#x27;, &#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
 
SELECT * FROM emp;

COMMIT;</code></pre><p id="0d925404-bf0b-4a2e-b125-0b5bc8790261" class="">
</p><p id="499bf4b5-52fe-4454-a74d-4e629962c944" class="">문제 592) (짝꿍이 지움) 3개의 테이블 중 2개를 DELETE하고 COMMIT 하시오</p><ol type="1" id="4f9b408b-eafe-447b-8d48-006bd08df29f" class="numbered-list" start="1"><li>EMP19</li></ol><ol type="1" id="dc2aa7cf-be14-4af0-8df6-a45e0a140f00" class="numbered-list" start="2"><li>SALGRADE</li></ol><ol type="1" id="d877ab62-2dfb-4cfd-a72b-f3e509126481" class="numbered-list" start="3"><li>INSURANCE</li></ol><p id="dfbd3b03-9496-44c5-a898-9da49c2b14bb" class="">
</p><p id="50d79691-c009-4a0c-9ec9-4af6ca6526a2" class="">문제 593) 자리로 돌아와서 위의 3개의 테이블 중 없는 데이터가 뭐지 확인하고 flashback으로 복구합니다</p><ul id="f8047de5-1976-4c3f-8556-8f03dd9f95c7" class="bulleted-list"><li style="list-style-type:disc">과거 데이터 백업 테이블 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="8bacce1c-eaf0-4d4c-b62d-61964f8892dd" class="code"><code class="language-SQL">CREATE TABLE emp19_20240604
AS
SELECT *
 FROM emp19
  AS OF TIMESTAMP
  TO_TIMESTAMP(&#x27;2024/06/04 14:45:00&#x27;, &#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
  
SELECT * FROM emp19_20240604;

--

CREATE TABLE salgrade_20240604
AS
SELECT *
 FROM salgrade
  AS OF TIMESTAMP
  TO_TIMESTAMP(&#x27;2024/06/04 14:45:00&#x27;, &#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
  
SELECT * FROM salgrade_20240604;

--

CREATE TABLE insurance_20240604
AS
SELECT *
 FROM insurance
  AS OF TIMESTAMP
  TO_TIMESTAMP(&#x27;2024/06/04 14:45:00&#x27;, &#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
  
SELECT * FROM insurance_20240604;
</code></pre><ul id="cbecf67e-0d96-494f-8faf-7baccda4b5ac" class="bulleted-list"><li style="list-style-type:disc">과거데이터 복구</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="217f1fc0-49af-4770-a789-a871fc341762" class="code"><code class="language-SQL">alter table emp19 enable row movement;

flashback table emp19 to timestamp
 to_timestamp (&#x27;2024/06/04 14:45:00&#x27;,&#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
 
select * from emp19;
 
commit;

--

alter table salgrade enable row movement;

flashback table salgrade to timestamp
 to_timestamp (&#x27;2024/06/04 14:45:00&#x27;,&#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
 
select * from salgrade;
 
commit;

--

alter table insurance enable row movement;

flashback table insurance to timestamp
 to_timestamp (&#x27;2024/06/04 14:45:00&#x27;,&#x27;RRRR/MM/DD HH24:MI:SS&#x27;);
 
select * from insurance;
 
commit;</code></pre><p id="2451957a-ee96-4512-8281-f7aef511e16e" class="">
</p><ul id="2dd76fdf-89a9-435c-8564-80e2f81b3558" class="bulleted-list"><li style="list-style-type:disc">내가 데이터를 잘 못 삭제하는 경우도 있고 다른 개발자나 SQL 사용자가 데이터를 실수로 지우는 일이 빈번하게 발생합니다. (1달에 1~2번은 일어납니다.) 그래서 다음과 같이 중요 테이블들을 백업을 해야합니다.</li></ul><h3 id="7791b902-53a1-40a5-8236-23c79848c94b" class="">백업한 테이블 dmp파일로 익스포트하고 , dmp파일 임포트하기</h3><p id="91eb48d0-60e3-4cd4-aa9a-d9e2666394cd" class="">문제 594) 내가 소유하고 있는 테이블들을 전부 백업하는 스크립트를 생성하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f2289d39-b078-40ae-a9c1-e7c565149e97" class="code"><code class="language-SQL">SELECT &#x27;CREATE TABLE &#x27; || table_name || &#x27;_20240604 AS SELECT * FROM &#x27; || table_name || &#x27;;&#x27;
 FROM user_tables
 WHERE table_name NOT LIKE &#x27;DM%&#x27;;</code></pre><figure id="a7d73306-aabc-4184-aa33-aa6a3a69c664" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2025.png"><img style="width:539px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2025.png"/></a></figure><p id="411bc69a-737a-490f-bc7e-261c66e18b87" class="">
</p><p id="ed8b0ffa-04e7-4196-b6c3-7122fb84c101" class="">문제 595) SQL 포트폴리오 준비 테이블을 DB 링크 없이 짝꿍자리에 만들고 싶거나 또는 집에 노트북에 만들고 싶다면 다음과 같이 백업해야합니다.</p><ol type="1" id="ea933a69-2312-485b-904c-3ed25984667a" class="numbered-list" start="1"><li>명령 프롬프트 창을 열고 다음과 같이 SQL 포트폴리오 테이블을 EXPORT 합니다.</li></ol><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="addd1d1f-a25e-4cfa-a98e-58e17fe1a16b" class="code"><code class="language-XML">PS C:\Users\itwill&gt; exp c##scott/tiger tables=ty_all file=ty_all.dmp</code></pre><figure id="55e66b3e-95f9-4dd1-8c59-65d12049f1ab" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2026.png"><img style="width:629px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2026.png"/></a></figure><figure id="fdb6d86e-b9fd-4fd7-ab87-6a157064f0fe" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2027.png"><img style="width:384px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2027.png"/></a></figure><ol type="1" id="375a28a4-bd65-4d76-92a8-e26cd75b12f5" class="numbered-list" start="2"><li>짝꿍에게 받은 emp.dmp 파일을 내 database에 import를 합니다. 짝꿍에게 받은 emp.dmp를 c 드라이브 밑에 users 밑에 itwill 밑에 가져다 둡니다. 그리고 다시 명령프롬프트에서 이번엔 imp 명령어로 임포트합니다.</li></ol><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="97ebc399-74b1-4d9f-94b3-1c5f2be9709d" class="code"><code class="language-XML">PS C:\Users\itwill&gt; imp c##scott/tiger tables=hosp_info file=hosp_info.dmp</code></pre><p id="792fac89-674c-4d77-ae83-bf2dab64a04f" class="">
</p><h3 id="ab5de1bc-c2a6-4cf5-9e79-ca233abd9fe0" class="">100. 실수로 지운 데이터 복구하기 2(FLASHBACK TABLE)</h3><p id="df0c4606-fb55-418a-b15b-1165c846ebcf" class="">
</p><p id="11a3dc84-c31e-4a86-a456-7859918fb1dc" class="">문제 596) emp 테이블을 전부 지우고 commit 하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="1ab0791d-8dbc-46d7-8150-131193163021" class="code"><code class="language-SQL">select * from emp;

delete from emp;
commit;</code></pre><p id="4c808cc1-76e0-4405-a2f1-629f382695b4" class=""><br/>문제 597) emp 테이블을 현재시간에서 5분전으로 되돌리세요<br/></p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f2b061b5-7b62-4561-ba5c-484dc2c8afde" class="code"><code class="language-SQL">alter table emp enable row movement;

flashback table emp to timestamp(systimestamp - interval &#x27;5&#x27; minute);
 
select * from emp;
commit;</code></pre><p id="43c315ef-e40b-4ed4-a32c-d59057c44e77" class="">
</p><p id="9a6b08d1-9184-4951-b22d-7d97e3bedc4c" class="">문제 598) dept 테이블을 모두 delete하고 commit하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="dfedef68-abca-4ab5-a5e5-9f45ad1f1b84" class="code"><code class="language-SQL">select * from dept;

delete from dept;
commit;</code></pre><p id="160f25e4-8e97-4ec8-9a7a-8f8d14053e4a" class="">
</p><p id="6db89acf-0c6a-4e60-95dc-863cd00b8b2f" class="">문제 599) delete한 dept 테이블을 5분 전으로 되돌리세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f9c89740-be4f-426c-bb7f-06a87dc8bb95" class="code"><code class="language-SQL">alter table dept enable row movement;

flashback table dept to timestamp(systimestamp - interval &#x27;5&#x27; minute);

select * from dept;
commit;</code></pre><p id="968ba5e5-2d2a-43ae-8980-d498bcc27c5e" class="">
</p><h3 id="182a909e-69b4-4429-8e8c-f73466a9f8e3" class="">101. 실수로 지운 데이터 복구하기 3 (FLASHBACK DROP)</h3><p id="40ff27d6-5efb-4f43-bd32-a138a4e084a7" class="">휴지통에서 DROP된 테이블을 살려내는 복구 방법입니다.</p><p id="d095aef3-1fa1-44f8-964c-f1b59dd7258d" class="">
</p><ul id="a4dee0b3-7a4f-4a69-affc-dfeeeeb0c240" class="bulleted-list"><li style="list-style-type:disc">사원 테이블에 월급에 인덱스를 생성</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="a3ab7b8b-b1fe-46c3-827e-5ffe3f2fdd46" class="code"><code class="language-SQL">create index emp_sal on emp(sal);

select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;</code></pre><ul id="ceaf553b-4262-46e0-9a6e-30246f948563" class="bulleted-list"><li style="list-style-type:disc">사원 테이블을 drop하기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="1e805aca-8ee8-4fbc-b5d8-881fac5d1c90" class="code"><code class="language-SQL">drop table emp;</code></pre><ul id="78e2e21f-38dc-40af-b591-31c9d39f8a27" class="bulleted-list"><li style="list-style-type:disc">drop된 테이블이 휴지통에 있는지 확인</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b97b0422-d5ff-41b8-9a53-a08599c16a8b" class="code"><code class="language-SQL">show recyclebin;

select * from user_recyclebin;</code></pre><ul id="93a328cf-67a7-45cf-87cb-ae231d315caa" class="bulleted-list"><li style="list-style-type:disc">휴지통에 있는 emp 테이블 복원하기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="0305a071-7f58-4ba5-a697-5f182b087184" class="code"><code class="language-SQL">flashback table emp to before drop;

select * from emp;</code></pre><ul id="b250f877-69a7-4b74-baf7-2838d42b2fc0" class="bulleted-list"><li style="list-style-type:disc">(21c에서 해결이 되는지 확인) emp 테이블에 걸린 인덱스도 복구되었는지 확인하기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b88ca1c2-1f4f-4681-b9b6-f1248c8e893b" class="code"><code class="language-SQL">select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;</code></pre><figure id="488f5faf-1de3-42c3-99b9-fc7ec17fff76" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2028.png"><img style="width:244px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2028.png"/></a></figure><p id="6a396d9b-8729-4e3f-8018-55307a881ec4" class="">⇒ 테이블을 DROP하면 인덱스도 같이 DROP되는데 테이블을 복원하면 인덱스도 복원이 됩니다. 그런데 다음과 같이 인덱스 이름이 이상하게 보입니다.</p><ul id="981b3617-7eca-4dd9-9f97-02aa192d8f07" class="bulleted-list"><li style="list-style-type:disc">복원된 인덱스 이름을 원래 이름으로 변경하기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="7483cdce-2284-4727-8d2e-ab8324dcc913" class="code"><code class="language-SQL">alter index &quot;BIN$IjNmui9hSFOm2wV2awrZcQ==$1&quot;
 rename to emp_sal;
 
select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;</code></pre><p id="6013127c-aa68-4d95-a16c-b578998c0a39" class="">⇒ 21c에서도 해결되지 못한 버그(bug)입니다.</p><p id="27fd1b88-d1da-42ec-b3cb-2d845249d951" class="">테이블을 휴지통에서 복구했으면 관련 인덱스의 이름을 다시 원래대로 돌려놔야합니다.</p><ul id="65aaa0f4-448c-4bc4-8830-7f36e7467901" class="bulleted-list"><li style="list-style-type:disc">테이블 휴지통 비우기</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="62b49e85-d9d9-4248-a544-81d8d9d6a459" class="code"><code class="language-SQL">purge recyclebin;

show recyclebin;</code></pre><p id="3bd97249-eeb9-4d5c-a780-43db58644796" class="">
</p><p id="755e0e00-25b1-4fb2-80ed-f2640cdbd4ba" class="">문제 600) emp 테이블에 월급과 직업에 다음과 같이 인덱스를 거세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="c96a5bc8-ca31-4f32-95a6-086838d7f4b6" class="code"><code class="language-SQL">-- 실습을 위해 기존 인덱스 지우기
select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;
 
drop index emp_sal;</code></pre><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="b846e5d6-ff27-41a7-be28-a19b1c44cfa2" class="code"><code class="language-SQL">create index emp_sal;

create index emp_sal on emp(sal);
create index emp_job on emp(job);</code></pre><p id="2f0c85de-e5c9-434b-9244-e3e5f8f40006" class="">
</p><p id="619db733-a022-4a05-b5c2-90943d3bee9d" class="">문제 601) emp 테이블을 drop을 하고 emp 테이블에 걸린 인덱스도 같이 삭제되었는지 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f69bf196-b529-42d7-a63e-b33860ca68f5" class="code"><code class="language-SQL">drop table emp;

select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;</code></pre><figure id="cfcb666c-42f7-482e-af65-544074266093" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2029.png"><img style="width:108px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2029.png"/></a></figure><p id="dbbb7078-3f1f-45b4-859e-5f317d9c9e43" class="">
</p><p id="37bb4ef0-1970-421d-ac61-de8eeccf61bc" class="">문제 602) 휴지통에 테이블과 인덱스가 있는지 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="a37bb7c3-3433-43e9-a75f-d56b388a1109" class="code"><code class="language-SQL">select * from recyclebin;</code></pre><figure id="6177ea7d-cec6-4f20-a9cd-4b5be52f9f13" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2030.png"><img style="width:585px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2030.png"/></a></figure><p id="364638a5-0810-430b-80ab-19440f1a3750" class="">
</p><p id="5ce6e580-a4d5-437e-ac24-a6821568ff84" class="">문제 603) !! 순서 주의 !! emp 테이블을 휴지통에서 복구하기 전에 인덱스 이름을 원래 이름으로 돌려놓는 스크립트를 생성하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="5ba77b27-ffee-40ba-8390-9856395cf9b5" class="code"><code class="language-SQL">select &#x27; alter index &#x27; || &#x27;&quot;&#x27; || object_name || &#x27;&quot;&#x27; || &#x27; rename to &#x27; || original_name || &#x27;;&#x27;
 from user_recyclebin
 where type = &#x27;INDEX&#x27;;</code></pre><figure id="9477945b-b0fb-4219-8738-578c72962de5" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2031.png"><img style="width:495px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2031.png"/></a></figure><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="c913aae7-0ff8-475a-b5b7-e85f7f73074c" class="code"><code class="language-SQL"> alter index &quot;BIN$cRIZ/6YSSnSHWvTyFpKvPw==$0&quot; rename to EMP_JOB;
 alter index &quot;BIN$CrMMxh5ZRTm6B+jcnCyevQ==$0&quot; rename to EMP_SAL;</code></pre><p id="01e06e8d-754a-4011-8072-fccc1d2d6555" class="">
</p><p id="6d43f493-ed76-49b3-9a1b-b69eda364502" class="">문제 604) emp 테이블을 휴지통에서 빼내세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="857f0bac-1798-4b6c-a1be-1a3e6fa89257" class="code"><code class="language-SQL">flashback table emp to before drop;

alter index &quot;BIN$cRIZ/6YSSnSHWvTyFpKvPw==$0&quot; rename to EMP_JOB;
alter index &quot;BIN$CrMMxh5ZRTm6B+jcnCyevQ==$0&quot; rename to EMP_SAL;

select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;</code></pre><p id="96791b5e-7304-4cad-afe0-3cbd4eaf1ca5" class="">
</p><p id="bc0ef40d-8e20-4381-83f2-764d3995ca45" class="">문제 605) (복습) emp 테이블의 월급의 인덱스의 구조를 확인하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="a50ef445-2bc1-41f8-8c52-cb3c5c153bfc" class="code"><code class="language-SQL">select sal, rowid
 from emp
 where sal &gt;= 0;</code></pre><figure id="565ec821-2080-4ba2-8aad-c2f03fcdbe73" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2032.png"><img style="width:201px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2032.png"/></a></figure><p id="eaf78a9d-667e-4fc1-9ee4-6bd79335bf81" class="">
</p><p id="530d2910-cb05-4d57-a845-76e2b3aabf45" class=""><mark class="highlight-yellow">문제 606) (복습) 이름과 월급을 출력하는데 월급이 낮은 사원부터 높은 사원 순으로 출력하세요</mark></p><ul id="31db80dc-0849-4b95-ad36-c32c18d594dd" class="bulleted-list"><li style="list-style-type:disc"><mark class="highlight-yellow">튜닝 전 (인덱스를 생성하기 전)</mark></li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="80931f27-5786-4114-b6c3-334484fb4d76" class="code"><code class="language-SQL">select ename, sal
 from emp
 order by sal asc;</code></pre><p id="61bf0031-7661-4023-b807-fe0886911e88" class="">⇒ 빅데이터 환경에서는 order by절이 검색 성능에 부하를 크게 줍니다</p><p id="4a7b19a6-d463-42e4-b1b8-227f7ef9a18e" class="">
</p><p id="a7fce389-a911-4b5f-8e6e-b8b0c967a96e" class=""><mark class="highlight-yellow">문제 607) 위의 SQL을 튜닝하세요</mark></p><ul id="cea207eb-a382-4344-a5c2-cddea982e409" class="bulleted-list"><li style="list-style-type:disc"><mark class="highlight-yellow">튜닝 후 (sal에 대한 인덱스를 생성한 후)</mark></li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="652f6419-a0fb-46c1-8898-1a4711f1d6ec" class="code"><code class="language-SQL">select ename, sal
 from emp
 where sal &gt;= 0;</code></pre><figure id="2bd61f71-147e-4065-98a3-414061edc303" class="image"><a href="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2033.png"><img style="width:131px" src="0604_SQL_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%A9%20%E1%84%82%E1%85%A9%E1%87%81%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%20(INDEX)%20~%20%E1%84%83%E1%85%A6%E1%84%8B%202474cee5125c4d01a737bb965d923432/Untitled%2033.png"/></a></figure><p id="a42bdbed-e854-47a1-a3fb-1aaf08114750" class="">⇒ emp_sal 인덱스의 데이터를 읽어오려고 일부러 where 절에 sal &gt;= 0 을 써줬습니다.</p><h3 id="30bd598e-4b6a-4e7c-a263-9ff5adbe2db5" class="">※ 인덱스를 생성한 후 where 절의 검색조건은 ?</h3><ol type="1" id="182c180b-b4e9-4daa-a6ca-65837026ab47" class="numbered-list" start="1"><li>숫자 &gt;= 0</li></ol><ol type="1" id="c5e2c998-db95-4a2c-96a8-1b94a4f82dad" class="numbered-list" start="2"><li>문자 &gt; ‘ ‘ (공백 한 칸 넣기)</li></ol><ol type="1" id="dcb980e9-9648-40af-a09e-6ef7502c9b1d" class="numbered-list" start="3"><li>날짜 &lt;= to_date(’9999/12/31’, ‘RRRR/MM/DD’)</li></ol><p id="16d82d70-efa0-494e-9485-711695e2ded5" class="">
</p><p id="490f1b6b-764e-4760-b0d6-0e9fc1660fe2" class="">문제 608)  사원 테이블에  ename 에 인덱스를 생성하세요</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="032705be-3820-4e81-9d20-317f9b53e98d" class="code"><code class="language-SQL">create index emp_ename
on emp(ename);

select index_name
 from user_indexes
 where table_name = &#x27;EMP&#x27;;</code></pre><p id="aa69b198-6b80-47c9-bf32-92a53759daba" class="">
</p><p id="49f5a033-d3c2-4388-9df6-f28165dbf13f" class="">문제609) 아래의 SQL을 튜닝하세요  (order by 절 안쓰고 결과를 출력하세요)</p><ul id="447e657f-eacb-4002-a4e2-44a28f64641b" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f0ac1682-2da4-44ac-99ae-eaf70ba135dc" class="code"><code class="language-SQL">select ename, sal
 from emp
 order by ename asc;</code></pre><ul id="c298fbd3-e9b5-4014-8c24-66d904524f16" class="bulleted-list"><li style="list-style-type:disc">튜닝 후</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="6935ea29-6e94-4122-96a7-c889ddb70a9c" class="code"><code class="language-SQL">select ename, sal
 from emp
 where ename &gt; &#x27; &#x27;;</code></pre><p id="6346f229-c0d0-4317-b7aa-921ef12f5bfe" class="">
</p><p id="7280264d-18bc-4679-bcaa-bb5a9ee938dc" class="">문제610)  아래의 SQL을 튜닝하세요 (order  by 절 안쓰고 결과를 출력하세요)</p><ul id="c7de11cc-7902-4639-8361-4cb29029c501" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="c3cc0041-9e39-41fd-8206-b67da8bc543b" class="code"><code class="language-SQL">select ename, sal
 from emp
 order by sal desc; -- asc 말고 반대로 desc</code></pre><ul id="ba3ea944-72f4-472a-9a8c-8de34ccc63d7" class="bulleted-list"><li style="list-style-type:disc">튜닝 후</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="aacc9aa3-698e-49eb-ae5e-5fffb09366dc" class="code"><code class="language-SQL">select /*+ index_desc(emp emp_sal) */ ename, sal
 from emp
 where sal &gt;= 0;</code></pre><p id="8929c1a4-9a85-490b-ba13-90f0f16b9d21" class="">⇒ where 절에 sal이 반드시 검색조건으로 있어야 하고, index_desc 힌트를 써서 emp_sal 인덱스를 descending 하게 읽습니다.</p><p id="4666ff84-d8d8-4e0e-a600-74a32845ee26" class="">
</p><p id="ab442f19-9a59-4c6c-87a2-a0c3cb5972c7" class="">문제611) (오늘의 마지막 문제1) 아래의 SQL을 튜닝하세요 (order by 절 안쓰고 출력하세요)</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="1fb55ce6-cad4-49d5-89e2-605ebe09068e" class="code"><code class="language-SQL">create index emp_hiredate
on emp(hiredate);</code></pre><ul id="197bcb4c-45f8-4fc4-8ecc-02a56b3011af" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="f2598648-d947-4eda-a4a1-1f718b1470dd" class="code"><code class="language-SQL">select ename, hiredate
 from emp
 order by hiredate desc;</code></pre><ul id="0cec9d09-2f17-4949-8ff4-3da597d65fc6" class="bulleted-list"><li style="list-style-type:disc">튜닝 후</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="e8a606e6-daaa-409e-80d3-cdb778f78380" class="code"><code class="language-SQL">select /*+ index_desc(emp emp_hiredate) */ ename, hiredate
 from emp
 where hiredate &lt;= to_date(&#x27;9999/12/31&#x27;, &#x27;RRRR/MM/DD&#x27;);</code></pre><p id="262e096f-0693-407c-adaf-d1ded459c68a" class="">
</p><p id="a6dc012b-4e99-4cce-beba-52815ea86460" class="">문제612) (오늘의 마지막 문제2) 아래의 SQL을 튜닝하세요 (order by 절 안쓰고 출력하세요)</p><ul id="72c7949a-3206-4199-8ae7-625e31773053" class="bulleted-list"><li style="list-style-type:disc">튜닝 전</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="44437829-38d0-428e-9d66-5be3ac14e4b8" class="code"><code class="language-SQL">select ename, sal
 from emp
 where job = &#x27;SALESMAN&#x27;
 order by sal desc;</code></pre><ul id="e80b0346-00fa-4377-b419-f9ed4058d7dc" class="bulleted-list"><li style="list-style-type:disc">튜닝 후</li></ul><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="631897c0-8870-4006-a79f-0d307fa9776c" class="code"><code class="language-SQL">select /*+ index_desc(emp emp_sal) */ ename, sal
 from emp
 where job = &#x27;SALESMAN&#x27; and sal &gt;= 0;</code></pre></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>
