Issue commonmark/cmark#383:
.
*****Hello*world****
.
<p>**<em><strong>Hello<em>world</em></strong></em></p>
.

Issue #246.  Double escaping in ALT
.
![&](#)
.
<p><img src="#" alt="&amp;" /></p>
.

Strip markdown in ALT tags
.
![*strip* [markdown __in__ alt](#)](#)
.
<p><img src="#" alt="strip markdown in alt" /></p>
.

Issue #55:
.
![test]

![test](foo bar)
.
<p>![test]</p>
<p>![test](foo bar)</p>
.


Reference labels: 'i̇θωkå'.toUpperCase() is 'İΘΩKÅ', but these should still be equivalent
.
[İϴΩKÅ]

[i̇θωkå]: /url
.
<p><a href="/url">İϴΩKÅ</a></p>
.


Reference labels: support ligatures (equivalent according to unicode case folding)
.
[ﬀﬁﬂ]

[fffifl]: /url
.
<p><a href="/url">ﬀﬁﬂ</a></p>
.


Issue #35. `<` should work as punctuation
.
an **(:**<br />
.
<p>an <strong>(:</strong><br /></p>
.


Should unescape only needed things in link destinations/titles:
.
[test](<\f\o\o\>\\>)

[test](foo "\\\"\b\a\r")
.
<p><a href="%5Cf%5Co%5Co%3E%5C">test</a></p>
<p><a href="foo" title="\&quot;\b\a\r">test</a></p>
.


Not a closing tag
.
</ 123>
.
<p>&lt;/ 123&gt;</p>
.



Escaping entities in links:
.
[](<&quot;> "&amp;&ouml;")

[](<\&quot;> "\&amp;\&ouml;")

[](<\\&quot;> "\\&quot;\\&ouml;")
.
<p><a href="%22" title="&amp;ö"></a></p>
<p><a href="&amp;quot;" title="&amp;amp;&amp;ouml;"></a></p>
<p><a href="%5C%22" title="\&quot;\ö"></a></p>
.


Checking combination of replaceEntities and unescapeMd:
.
~~~ &amp;&bad;\&amp;\\&amp;
just a funny little fence
~~~
.
<pre><code class="&amp;&amp;bad;&amp;amp;\&amp;">just a funny little fence
</code></pre>
.

Underscore between punctuation chars should be able to close emphasis.

.
_(hai)_.
.
<p><em>(hai)</em>.</p>
.

Regression test, should not match emphasis markers in different link tags:
.
[*b]() [c*]()
.
<p><a href="">*b</a> <a href="">c*</a></p>
.

Those are two separate blockquotes:
.
 - > foo
  > bar
.
<ul>
<li>
<blockquote>
<p>foo</p>
</blockquote>
</li>
</ul>
<blockquote>
<p>bar</p>
</blockquote>
.

Blockquote should terminate itself after paragraph continuation
.
- list
    > blockquote
blockquote continuation
    - next list item
.
<ul>
<li>list
<blockquote>
<p>blockquote
blockquote continuation</p>
</blockquote>
<ul>
<li>next list item</li>
</ul>
</li>
</ul>
.

Regression test (code block + regular paragraph)
.
>     foo
> bar
.
<blockquote>
<pre><code>foo
</code></pre>
<p>bar</p>
</blockquote>
.

Blockquotes inside indented lists should terminate correctly
.
   - a
     > b
     ```
     c
     ```
   - d
.
<ul>
<li>a
<blockquote>
<p>b</p>
</blockquote>
<pre><code>c
</code></pre>
</li>
<li>d</li>
</ul>
.

Don't output empty class here:
.
```&#x20;
test
```
.
<pre><code>test
</code></pre>
.

Setext header text supports lazy continuations:
.
 - foo
bar
   ===
.
<ul>
<li>
<h1>foo
bar</h1>
</li>
</ul>
.

But setext header underline doesn't:
.
 - foo
   bar
  ===
.
<ul>
<li>foo
bar
===</li>
</ul>
.

Tabs should be stripped from the beginning of the line
.
 foo
 bar
	baz
.
<p>foo
bar
baz</p>
.

Tabs should not cause hardbreak, EOL tabs aren't stripped in commonmark 0.27
.
foo1	
foo2    
bar
.
<p>foo1	
foo2<br />
bar</p>
.

List item terminating quote should not be paragraph continuation
.
1. foo
   > quote
2. bar
.
<ol>
<li>foo
<blockquote>
<p>quote</p>
</blockquote>
</li>
<li>bar</li>
</ol>
.

Escaped space is not allowed in link destination, commonmark/CommonMark#493.
.
[link](a\ b)
.
<p>[link](a\ b)</p>
.

Link destination cannot contain '<'
.
[](<foo<bar>)

[](<foo\<bar>)
.
<p>[](&lt;foo<bar>)</p>
<p><a href="foo%3Cbar"></a></p>
.

Link title cannot contain '(' when opened with it
.
[](url (xxx())

[](url (xxx\())
.
<p>[](url (xxx())</p>
<p><a href="url" title="xxx("></a></p>
.

Allow EOL in processing instructions, commonmark/commonmark.js#196.
.
a <?
?>
.
<p>a <?
?></p>
.

Allow meta tag in an inline context, commonmark/commonmark-spec#527.
.
City:
<span itemprop="contentLocation" itemscope itemtype="https://schema.org/City">
  <meta itemprop="name" content="Springfield">
</span>
.
<p>City:
<span itemprop="contentLocation" itemscope itemtype="https://schema.org/City">
<meta itemprop="name" content="Springfield">
</span></p>
.

Coverage. Directive can terminate paragraph.
.
a
<?php
.
<p>a</p>
<?php
.


Coverage. Nested email autolink (silent mode)
.
*<foo@bar.com>*
.
<p><em><a href="mailto:foo@bar.com">foo@bar.com</a></em></p>
.


Coverage. Unpaired nested backtick (silent mode)
.
*`foo*
.
<p><em>`foo</em></p>
.


Coverage. Should continue scanning after closing "```" despite cache
.
```aaa``bbb``ccc```ddd``eee``
.
<p><code>aaa``bbb``ccc</code>ddd<code>eee</code></p>
.


Coverage. Entities.
.
*&*

*&#x20;*

*&amp;*
.
<p><em>&amp;</em></p>
<p><em> </em></p>
<p><em>&amp;</em></p>
.


Coverage. Escape.
.
*\a*
.
<p><em>\a</em></p>
.


Coverage. parseLinkDestination
.
[foo](<
bar>)

[foo](<bar)
.
<p>[foo](&lt;
bar&gt;)</p>
<p>[foo](&lt;bar)</p>
.


Coverage. parseLinkTitle
.
[foo](bar "ba)

[foo](bar "ba\
z")
.
<p>[foo](bar &quot;ba)</p>
<p><a href="bar" title="ba\
z">foo</a></p>
.


Coverage. Image
.
![test]( x )
.
<p><img src="x" alt="test" /></p>
.
.
![test][foo]

[bar]: 123
.
<p>![test][foo]</p>
.
.
![test][[[

[bar]: 123
.
<p>![test][[[</p>
.
.
![test](
.
<p>![test](</p>
.


Coverage. Link
.
[test](
.
<p>[test](</p>
.


Coverage. Reference
.
[
test\
]: 123
foo
bar
.
<p>foo
bar</p>
.
.
[
test
]
.
<p>[
test
]</p>
.
.
> [foo]: bar
[foo]
.
<blockquote></blockquote>
<p><a href="bar">foo</a></p>
.

Coverage. Tabs in blockquotes.
.
>		test

 >		test

  >		test

> ---
>		test

 > ---
 >		test

  > ---
  >		test

>			test

 >			test

  >			test

> ---
>			test

 > ---
 >			test

  > ---
  >			test
.
<blockquote>
<pre><code>  test
</code></pre>
</blockquote>
<blockquote>
<pre><code> test
</code></pre>
</blockquote>
<blockquote>
<pre><code>test
</code></pre>
</blockquote>
<blockquote>
<hr />
<pre><code>  test
</code></pre>
</blockquote>
<blockquote>
<hr />
<pre><code> test
</code></pre>
</blockquote>
<blockquote>
<hr />
<pre><code>test
</code></pre>
</blockquote>
<blockquote>
<pre><code>  	test
</code></pre>
</blockquote>
<blockquote>
<pre><code> 	test
</code></pre>
</blockquote>
<blockquote>
<pre><code>	test
</code></pre>
</blockquote>
<blockquote>
<hr />
<pre><code>  	test
</code></pre>
</blockquote>
<blockquote>
<hr />
<pre><code> 	test
</code></pre>
</blockquote>
<blockquote>
<hr />
<pre><code>	test
</code></pre>
</blockquote>
.

Coverage. Tabs in lists.
.
1. 	foo

	     bar
.
<ol>
<li>
<p>foo</p>
<pre><code> bar
</code></pre>
</li>
</ol>
.

Coverage. Various tags not interrupting blockquotes because of indentation:
.
> foo
    - - - -

> foo
    # not a heading
.
<blockquote>
<p>foo
- - - -</p>
</blockquote>
<blockquote>
<p>foo
# not a heading</p>
</blockquote>
.

Coverage, entities with code > 10FFFF. Made this way for compatibility with commonmark.js.
.
&#x110000;

&#x1100000;
.
<p>�</p>
<p>&amp;#x1100000;</p>
.

Issue #696. Blockquotes should remember their level.
.
>>> foo
bar
>>> baz
.
<blockquote>
<blockquote>
<blockquote>
<p>foo
bar
baz</p>
</blockquote>
</blockquote>
</blockquote>
.

Issue #696. Blockquotes should stop when outdented from a list.
.
1. >>> foo
   bar
baz
   >>> foo
  >>> bar
   >>> baz
.
<ol>
<li>
<blockquote>
<blockquote>
<blockquote>
<p>foo
bar
baz
foo</p>
</blockquote>
</blockquote>
</blockquote>
</li>
</ol>
<blockquote>
<blockquote>
<blockquote>
<p>bar
baz</p>
</blockquote>
</blockquote>
</blockquote>
.

Newline in image description
.
There is a newline in this image ![here
it is](https://github.com/executablebooks/)
.
<p>There is a newline in this image <img src="https://github.com/executablebooks/" alt="here
it is" /></p>
.

Issue #772. Header rule should not interfere with html tags.
.
<!--
==
-->

<pre>
==
</pre>
.
<!--
==
-->
<pre>
==
</pre>
.

Issue #205.  Space in link destination generates IndexError
.
[Contact](http:// mail.com)

[Contact](mailto: mail@mail.com)
.
<p>[Contact](http:// mail.com)</p>
<p>[Contact](mailto: mail@mail.com)</p>
.

Issue #204. Combination of blockquotes, list and newlines causes an IndexError
.
> QUOTE
+ UNORDERED LIST ITEM
  > INDENTED QUOTE



.
<blockquote>
<p>QUOTE</p>
</blockquote>
<ul>
<li>UNORDERED LIST ITEM
<blockquote>
<p>INDENTED QUOTE</p>
</blockquote>
</li>
</ul>
.
