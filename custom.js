// Reusable C++/Python code tab switcher. Vanilla JS, no dependencies.
// Markup convention (see root README "Mixing prose and code" for the full pattern):
//
// <div class="code-tabs">
// <div class="code-tabs-nav">
// <button class="code-tab-btn active" onclick="simShowTab(this, 'cpp')">C++</button>
// <button class="code-tab-btn" onclick="simShowTab(this, 'python')">Python</button>
// </div>
// <div class="code-tab-panel active" data-lang="cpp">
//
// ```cpp
// // code
// ```
//
// </div>
// <div class="code-tab-panel" data-lang="python">
//
// ```python
// # code
// ```
//
// </div>
// </div>
//
// Blank lines around each fenced code block are required — they let mdBook's markdown
// parser treat the code fence as real markdown instead of swallowing it as raw HTML.

function simShowTab(btn, lang) {
    var group = btn.closest(".code-tabs");
    if (!group) return;

    var buttons = group.querySelectorAll(".code-tab-btn");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("active");
    }

    var panels = group.querySelectorAll(".code-tab-panel");
    for (var j = 0; j < panels.length; j++) {
        panels[j].classList.remove("active");
    }

    btn.classList.add("active");
    var panel = group.querySelector('.code-tab-panel[data-lang="' + lang + '"]');
    if (panel) panel.classList.add("active");
}
