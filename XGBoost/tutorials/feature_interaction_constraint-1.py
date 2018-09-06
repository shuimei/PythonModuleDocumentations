from graphviz import Source
source = r"""
  digraph feature_interaction_illustration1 {
    graph [fontname = "helvetica"];
    node [fontname = "helvetica"];
    edge [fontname = "helvetica"];
    0 [label=<x<SUB><FONT POINT-SIZE="11">10</FONT></SUB> &lt; -1.5 ?>, shape=box, color=red, fontcolor=red];
    1 [label=<x<SUB><FONT POINT-SIZE="11">2</FONT></SUB> &lt; 2 ?>, shape=box];
    2 [label=<x<SUB><FONT POINT-SIZE="11">7</FONT></SUB> &lt; 0.3 ?>, shape=box, color=red, fontcolor=red];
    3 [label="...", shape=none];
    4 [label="...", shape=none];
    5 [label=<x<SUB><FONT POINT-SIZE="11">1</FONT></SUB> &lt; 0.5 ?>, shape=box, color=red, fontcolor=red];
    6 [label="...", shape=none];
    7 [label="...", shape=none];
    8 [label="Predict +1.3", color=red, fontcolor=red];
    0 -> 1 [labeldistance=2.0, labelangle=45, headlabel="Yes/Missing           "];
    0 -> 2 [labeldistance=2.0, labelangle=-45,
            headlabel="No", color=red, fontcolor=red];
    1 -> 3 [labeldistance=2.0, labelangle=45, headlabel="Yes"];
    1 -> 4 [labeldistance=2.0, labelangle=-45, headlabel="             No/Missing"];
    2 -> 5 [labeldistance=2.0, labelangle=-45, headlabel="Yes",
            color=red, fontcolor=red];
    2 -> 6 [labeldistance=2.0, labelangle=-45, headlabel="           No/Missing"];
    5 -> 7;
    5 -> 8 [color=red];
  }
"""
Source(source, format='png').render('../_static/feature_interaction_illustration1', view=False)
Source(source, format='svg').render('../_static/feature_interaction_illustration1', view=False)