from graphviz import Source
source = r"""
  digraph feature_interaction_illustration3 {
    graph [fontname = "helvetica"];
    node [fontname = "helvetica"];
    edge [fontname = "helvetica"];
    0 [label=<x<SUB><FONT POINT-SIZE="11">3</FONT></SUB> &lt; 2.5 ?>, shape=box];
    1 [label="+1.6"];
    2 [label=<x<SUB><FONT POINT-SIZE="11">2</FONT></SUB> &lt; -1.2 ?>, shape=box];
    3 [label="+0.1"];
    4 [label="-0.3"];
    0 -> 1 [labeldistance=2.0, labelangle=45, headlabel="Yes"];
    0 -> 2 [labeldistance=2.0, labelangle=-45, headlabel="           No/Missing"];
    2 -> 3 [labeldistance=2.0, labelangle=45, headlabel="Yes/Missing           "];
    2 -> 4 [labeldistance=2.0, labelangle=-45, headlabel="No"];
  }
"""
Source(source, format='png').render('../_static/feature_interaction_illustration3', view=False)
Source(source, format='svg').render('../_static/feature_interaction_illustration3', view=False)