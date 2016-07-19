library(igraph)

plot_graph <- function(graph, number, main_title="", custom_color=FALSE)
{
    graph_title = paste("Graph -", number, sep=" ")
    
    # Set node color if the graph does not have custom color
    if (custom_color == FALSE) {
        V(graph)$color = "royalblue"
    }
    
    plot(graph,
         layout = layout.circle,
         main = main_title,
         xlab = graph_title,
         vertex.size = 35,
         vertex.color = V(graph)$color,
         vertex.frame.color = "white",
         vertex.label.color = "white",
         vertex.label.family = "sans",
         edge.width = 2,
         edge.color = "black")
}

# Graph Rules
# 1. Nodes (N) will be between 2 and 20
# 2. Edges (K) will be between (N-1) and (N * (N - 1)) / 2

# Use dev.off() in case of inconsistent graphics state.

########################################################## Graph: N=2, K=1, Answer=1
title <- "Graph with N = 2 and K = 1. Answer = 1"
graph_01 <- make_empty_graph(directed=FALSE)
graph_01 <- graph_01 + vertices(c('A', 'B'))
graph_01 <- graph_01 + edges(c('A','B'))

# par(mfrow=c(1, 1))
# plot_graph(graph_01, 1, title)

########################################################## Graph: N=3, K=2, Answer=3
title <- "Graph with N = 3 and K = 2. Answer = 3"
graph_02 <- make_empty_graph(directed=FALSE)
graph_02 <- graph_02 + vertices(c('A', 'B', 'C'))
graph_02 <- graph_02 + edges(c('A','B', 'B','C'))

graph_03 <- make_empty_graph(directed=FALSE)
graph_03 <- graph_03 + vertices(c('A', 'B', 'C'))
graph_03 <- graph_03 + edges(c('A','B', 'C','A'))

graph_04 <- make_empty_graph(directed=FALSE)
graph_04 <- graph_04 + vertices(c('A', 'B', 'C'))
graph_04 <- graph_04 + edges(c('B','C', 'C','A'))

# par(mfrow=c(1, 3))
# plot_graph(graph_02, 1)
# plot_graph(graph_03, 2, title)
# plot_graph(graph_04, 3)

########################################################## Graph: N=3, K=3, Answer=1
title <- "Graph with N = 3 and K = 3. Answer = 1"
graph_05 <- make_empty_graph(directed=FALSE)
graph_05 <- graph_05 + vertices(c('A', 'B', 'C'))
graph_05 <- graph_05 + edges(c('A','B', 'B','C', 'C','A'))

# par(mfrow=c(1, 1))
# plot_graph(graph_05, 1, title)

########################################################## Graph: N=4, K=3, Answer=16
title <- "Graph with N = 4 and K = 3. Answer = 16"

graph_06 <- make_empty_graph(directed=FALSE)
graph_06 <- graph_06 + vertices(c('A', 'B', 'C', 'D'))
graph_06 <- graph_06 + edges(c('A','B', 'B','C', 'C','D'))

graph_07 <- make_empty_graph(directed=FALSE)
graph_07 <- graph_07 + vertices(c('A', 'B', 'C', 'D'))
graph_07 <- graph_07 + edges(c('A','B', 'B','C', 'D','A'))

graph_08 <- make_empty_graph(directed=FALSE)
graph_08 <- graph_08 + vertices(c('A', 'B', 'C', 'D'))
graph_08 <- graph_08 + edges(c('A','B', 'B','C', 'A','C'))
V(graph_08)$color = "royalblue"
V(graph_08)['D']$color <- "red1"

graph_09 <- make_empty_graph(directed=FALSE)
graph_09 <- graph_09 + vertices(c('A', 'B', 'C', 'D'))
graph_09 <- graph_09 + edges(c('A','B', 'B','C', 'B','D'))

graph_10 <- make_empty_graph(directed=FALSE)
graph_10 <- graph_10 + vertices(c('A', 'B', 'C', 'D'))
graph_10 <- graph_10 + edges(c('A','B', 'C','D', 'D','A'))

graph_11 <- make_empty_graph(directed=FALSE)
graph_11 <- graph_11 + vertices(c('A', 'B', 'C', 'D'))
graph_11 <- graph_11 + edges(c('A','B', 'C','D', 'A','C'))

graph_12 <- make_empty_graph(directed=FALSE)
graph_12 <- graph_12 + vertices(c('A', 'B', 'C', 'D'))
graph_12 <- graph_12 + edges(c('A','B', 'C','D', 'B','D'))

graph_13 <- make_empty_graph(directed=FALSE)
graph_13 <- graph_13 + vertices(c('A', 'B', 'C', 'D'))
graph_13 <- graph_13 + edges(c('A','B', 'D','A', 'A','C'))

graph_14 <- make_empty_graph(directed=FALSE)
graph_14 <- graph_14 + vertices(c('A', 'B', 'C', 'D'))
graph_14 <- graph_14 + edges(c('A','B', 'D','A', 'B','D'))
V(graph_14)$color = "royalblue"
V(graph_14)['C']$color <- "red1"

graph_15 <- make_empty_graph(directed=FALSE)
graph_15 <- graph_15 + vertices(c('A', 'B', 'C', 'D'))
graph_15 <- graph_15 + edges(c('A','B', 'A','C', 'B','D'))

graph_16 <- make_empty_graph(directed=FALSE)
graph_16 <- graph_16 + vertices(c('A', 'B', 'C', 'D'))
graph_16 <- graph_16 + edges(c('B','C', 'C','D', 'D','A'))

graph_17 <- make_empty_graph(directed=FALSE)
graph_17 <- graph_17 + vertices(c('A', 'B', 'C', 'D'))
graph_17 <- graph_17 + edges(c('B','C', 'C','D', 'A','C'))

graph_18 <- make_empty_graph(directed=FALSE)
graph_18 <- graph_18 + vertices(c('A', 'B', 'C', 'D'))
graph_18 <- graph_18 + edges(c('B','C', 'C','D', 'B','D'))
V(graph_18)$color = "royalblue"
V(graph_18)['A']$color <- "red1"

graph_19 <- make_empty_graph(directed=FALSE)
graph_19 <- graph_19 + vertices(c('A', 'B', 'C', 'D'))
graph_19 <- graph_19 + edges(c('B','C', 'D','A', 'A','C'))

graph_20 <- make_empty_graph(directed=FALSE)
graph_20 <- graph_20 + vertices(c('A', 'B', 'C', 'D'))
graph_20 <- graph_20 + edges(c('B','C', 'D','A', 'B','D'))

graph_21 <- make_empty_graph(directed=FALSE)
graph_21 <- graph_21 + vertices(c('A', 'B', 'C', 'D'))
graph_21 <- graph_21 + edges(c('B','C', 'A','C', 'B','D'))

graph_22 <- make_empty_graph(directed=FALSE)
graph_22 <- graph_22 + vertices(c('A', 'B', 'C', 'D'))
graph_22 <- graph_22 + edges(c('C','D', 'D','A', 'A','C'))
V(graph_22)$color = "royalblue"
V(graph_22)['B']$color <- "red1"

graph_23 <- make_empty_graph(directed=FALSE)
graph_23 <- graph_23 + vertices(c('A', 'B', 'C', 'D'))
graph_23 <- graph_23 + edges(c('C','D', 'D','A', 'B','D'))

graph_24 <- make_empty_graph(directed=FALSE)
graph_24 <- graph_24 + vertices(c('A', 'B', 'C', 'D'))
graph_24 <- graph_24 + edges(c('C','D', 'A','C', 'B','D'))

graph_25 <- make_empty_graph(directed=FALSE)
graph_25 <- graph_25 + vertices(c('A', 'B', 'C', 'D'))
graph_25 <- graph_25 + edges(c('D','A', 'A','C', 'B','D'))

# par(mfrow=c(4, 5))
# plot_graph(graph_06, 1)
# plot_graph(graph_07, 2)
# plot_graph(graph_08, 3, title, custom_color = TRUE)
# plot_graph(graph_09, 4)
# plot_graph(graph_10, 5)
# plot_graph(graph_11, 6)
# plot_graph(graph_12, 7)
# plot_graph(graph_13, 8)
# plot_graph(graph_14, 9, custom_color = TRUE)
# plot_graph(graph_15, 10)
# plot_graph(graph_16, 11)
# plot_graph(graph_17, 12)
# plot_graph(graph_18, 13, custom_color = TRUE)
# plot_graph(graph_19, 14)
# plot_graph(graph_20, 15)
# plot_graph(graph_21, 16)
# plot_graph(graph_22, 17, custom_color = TRUE)
# plot_graph(graph_23, 18)
# plot_graph(graph_24, 19)
# plot_graph(graph_25, 20)

########################################################## Graph: N=4, K=4, Answer=15
title <- "Graph with N = 4 and K = 4. Answer = 15"

graph_26 <- make_empty_graph(directed=FALSE)
graph_26 <- graph_26 + vertices(c('A', 'B', 'C', 'D'))
graph_26 <- graph_26 + edges(c('A','B', 'B','C', 'C','D', 'D','A'))

graph_27 <- make_empty_graph(directed=FALSE)
graph_27 <- graph_27 + vertices(c('A', 'B', 'C', 'D'))
graph_27 <- graph_27 + edges(c('A','B', 'B','C', 'C','D', 'A','C'))

graph_28 <- make_empty_graph(directed=FALSE)
graph_28 <- graph_28 + vertices(c('A', 'B', 'C', 'D'))
graph_28 <- graph_28 + edges(c('A','B', 'B','C', 'C','D', 'B','D'))

graph_29 <- make_empty_graph(directed=FALSE)
graph_29 <- graph_29 + vertices(c('A', 'B', 'C', 'D'))
graph_29 <- graph_29 + edges(c('A','B', 'B','C', 'D','A', 'A','C'))

graph_30 <- make_empty_graph(directed=FALSE)
graph_30 <- graph_30 + vertices(c('A', 'B', 'C', 'D'))
graph_30 <- graph_30 + edges(c('A','B', 'B','C', 'D','A', 'B','D'))

graph_31 <- make_empty_graph(directed=FALSE)
graph_31 <- graph_31 + vertices(c('A', 'B', 'C', 'D'))
graph_31 <- graph_31 + edges(c('A','B', 'B','C', 'A','C', 'B','D'))

graph_32 <- make_empty_graph(directed=FALSE)
graph_32 <- graph_32 + vertices(c('A', 'B', 'C', 'D'))
graph_32 <- graph_32 + edges(c('A','B', 'C','D', 'D','A', 'A','C'))

graph_33 <- make_empty_graph(directed=FALSE)
graph_33 <- graph_33 + vertices(c('A', 'B', 'C', 'D'))
graph_33 <- graph_33 + edges(c('A','B', 'C','D', 'D','A', 'B','D'))

graph_34 <- make_empty_graph(directed=FALSE)
graph_34 <- graph_34 + vertices(c('A', 'B', 'C', 'D'))
graph_34 <- graph_34 + edges(c('A','B', 'C','D', 'A','C', 'B','D'))

graph_35 <- make_empty_graph(directed=FALSE)
graph_35 <- graph_35 + vertices(c('A', 'B', 'C', 'D'))
graph_35 <- graph_35 + edges(c('A','B', 'D','A', 'A','C', 'B','D'))

graph_36 <- make_empty_graph(directed=FALSE)
graph_36 <- graph_36 + vertices(c('A', 'B', 'C', 'D'))
graph_36 <- graph_36 + edges(c('B','C', 'C','D', 'D','A', 'A','C'))

graph_37 <- make_empty_graph(directed=FALSE)
graph_37 <- graph_37 + vertices(c('A', 'B', 'C', 'D'))
graph_37 <- graph_37 + edges(c('B','C', 'C','D', 'D','A', 'B','D'))

graph_38 <- make_empty_graph(directed=FALSE)
graph_38 <- graph_38 + vertices(c('A', 'B', 'C', 'D'))
graph_38 <- graph_38 + edges(c('B','C', 'C','D', 'A','C', 'B','D'))

graph_39 <- make_empty_graph(directed=FALSE)
graph_39 <- graph_39 + vertices(c('A', 'B', 'C', 'D'))
graph_39 <- graph_39 + edges(c('B','C', 'D','A', 'A','C', 'B','D'))

graph_40 <- make_empty_graph(directed=FALSE)
graph_40 <- graph_40 + vertices(c('A', 'B', 'C', 'D'))
graph_40 <- graph_40 + edges(c('C','D', 'D','A', 'A','C', 'B','D'))

# par(mfrow=c(3, 5))
# plot_graph(graph_26, 1)
# plot_graph(graph_27, 2)
# plot_graph(graph_28, 3, title)
# plot_graph(graph_29, 4)
# plot_graph(graph_30, 5)
# plot_graph(graph_31, 6)
# plot_graph(graph_32, 7)
# plot_graph(graph_33, 8)
# plot_graph(graph_34, 9)
# plot_graph(graph_35, 10)
# plot_graph(graph_36, 11)
# plot_graph(graph_37, 12)
# plot_graph(graph_38, 13)
# plot_graph(graph_39, 14)
# plot_graph(graph_40, 15)

########################################################## Graph: N=4, K=5, Answer=6
title = "Graph with N = 4 and K = 5. Answer = 6"

graph_41 <- make_empty_graph(directed=FALSE)
graph_41 <- graph_41 + vertices(c('A', 'B', 'C', 'D'))
graph_41 <- graph_41 + edges(c('A','B', 'B','C', 'C','D', 'D','A', 'A','C'))

graph_42 <- make_empty_graph(directed=FALSE)
graph_42 <- graph_42 + vertices(c('A', 'B', 'C', 'D'))
graph_42 <- graph_42 + edges(c('A','B', 'B','C', 'C','D', 'D','A', 'B','D'))

graph_43 <- make_empty_graph(directed=FALSE)
graph_43 <- graph_43 + vertices(c('A', 'B', 'C', 'D'))
graph_43 <- graph_43 + edges(c('A','B', 'B','C', 'C','D', 'A','C', 'B','D'))

graph_44 <- make_empty_graph(directed=FALSE)
graph_44 <- graph_44 + vertices(c('A', 'B', 'C', 'D'))
graph_44 <- graph_44 + edges(c('A','B', 'B','C', 'D','A', 'A','C', 'B','D'))

graph_45 <- make_empty_graph(directed=FALSE)
graph_45 <- graph_45 + vertices(c('A', 'B', 'C', 'D'))
graph_45 <- graph_45 + edges(c('A','B', 'C','D', 'D','A', 'A','C', 'B','D'))

graph_46 <- make_empty_graph(directed=FALSE)
graph_46 <- graph_46 + vertices(c('A', 'B', 'C', 'D'))
graph_46 <- graph_46 + edges(c('B','C', 'C','D', 'D','A', 'A','C', 'B','D'))

# par(mfrow=c(2, 3))
# plot_graph(graph_41, 1)
# plot_graph(graph_42, 2, title)
# plot_graph(graph_43, 3)
# plot_graph(graph_44, 4)
# plot_graph(graph_45, 5)
# plot_graph(graph_46, 6)

########################################################## Graph: N=4, K=6, Answer=1
title <- "Graph with N = 4 and K = 6. Answer = 1"

graph_47 <- make_empty_graph(directed=FALSE)
graph_47 <- graph_47 + vertices(c('A', 'B', 'C', 'D'))
graph_47 <- graph_47 + edges(c('A','B', 'B','C', 'C','D', 'D','A', 'A','C', 'B','D'))

par(mfrow=c(1, 1))
plot_graph(graph_47, 1, title)
