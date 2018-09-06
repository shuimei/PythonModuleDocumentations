from graphviz import Source
source = r"""
  digraph feature_interaction_illustration2 {
    graph [fontname = "helvetica"];
    node [fontname = "helvetica"];
    edge [fontname = "helvetica"];
    0 [label=<x<SUB><FONT POINT-SIZE="11">0</FONT></SUB> &lt; 5.0 ?>, shape=box];
    1 [label=<x<SUB><FONT POINT-SIZE="11">2</FONT></SUB> &lt; -3.0 ?>, shape=box];
    2 [label="+0.6"];
    3 [label="-0.4"];
    4 [label="+1.2"];
    0 -> 1 [labeldistance=2.0, labelangle=45, headlabel="Yes/Missing           "];
    0 -> 2 [labeldistance=2.0, labelangle=-45, headlabel="No"];
    1 -> 3 [labeldistance=2.0, labelangle=45, headlabel="Yes"];
    1 -> 4 [labeldistance=2.0, labelangle=-45, headlabel="           No/Missing"];
  }
"""
Source(source, format='png').render('../_static/feature_interaction_illustration2', view=False)
Source(source, format='svg').render('../_static/feature_interaction_illustration2', view=False)