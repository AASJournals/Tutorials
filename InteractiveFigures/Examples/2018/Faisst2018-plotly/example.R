
### BEGIN R CODE ######

# import library
library(colorRamps) # colormap
library(plotly)

# create color map
color.map.length <- 30
color.map <- matlab.like2(color.map.length)


# create data frame for x, y, z values as well as color (4th dimension, e.g., the specific star formation rate of the galaxies)
d <- data.frame(x=x,y=y,z=z,c=ssfr)

# define marker layout
marker_layout <- list(size=3 , colorbar=list(thicknessmode="pixels", thickness=50 , title="log sSFR" , titlefont=list(size=20, family="Times New Roman") , tickfont=list(size=15, family="Times New Roman") , lenmode="fraction" , len=0.7))

# create plot
p <- plot_ly(d, x = d$x, y = d$y , z = d$z , type = 'scatter3d' , mode = "markers" , color=d$c , colors=color.map , marker=marker_layout , name=" ") %>%
add_markers() %>%
layout( scene = list(xaxis = list(title = "log(M)" , ticklen=5 , tickwidth=4 , linewidth=4 , gridwidth=2 , zeroline=FALSE , titlefont=list(size=20, family="Times New Roman") , tickfont=list(size=15, family="Times New Roman")),
                     yaxis = list(title = 'log([NII]/Ha)' , ticklen=5 , tickwidth=4 , linewidth=4 , gridwidth=2 , zeroline=FALSE , titlefont=list(size=20, family="Times New Roman") , tickfont=list(size=15, family="Times New Roman")),
                     zaxis = list(title = 'log([OIII]/Hb)' , ticklen=5 , tickwidth=4 , linewidth=4 , gridwidth=2 , zeroline=FALSE , titlefont=list(size=20, family="Times New Roman") , tickfont=list(size=15, family="Times New Roman"))),
       showlegend=FALSE
                     )

# save as html widget (imported by the “plotly” package)
# This saves the html file and creates also a directory with the dependent javascript.
# If selfcontained=FALSE, this means that saveWidget() creates an html file and a folder with all the JS.
# If TRUE, it will create a self contained HTML file with external files base 64 encoded. 
# To do so, one has to have PANDOC installed (see https://github.com/rstudio/rmarkdown/blob/master/PANDOC.md).
htmlwidgets::saveWidget(as_widget(p), "/Users/afaisst/Work/TMP/htmltmp/my3Dplot.html" , selfcontained=FALSE)


### END R CODE ###