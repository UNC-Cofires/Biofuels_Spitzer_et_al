#_____________________________________________________________#
#Script to create the geographic depiction of 5000 acres, 
#located outside of Vero Beach and the town of Chapel Hill.

#Set as working directory (R studio users)
setwd(dirname(dirname(rstudioapi::getActiveDocumentContext()$path)))


# Load required libraries
library(leaflet)
library(sf)
library(htmlwidgets)
library(webshot2)
library(ggplot2)
library(gridExtra)
library(png)
library(grid)


#_____________________________________________________________#
####Vero Beach Florida

# Define the center coordinates of Vero Beach, Florida
#Vero Beach - (27.6386, -80.3973)
center_lat <- 27.6386
center_lon <- -80.3973

# Calculate the side length of a square representing 5000 acres
acres_to_square_meters <- 5000 * 4046.86
side_length <- sqrt(acres_to_square_meters)
half_side <- side_length / 2

# Create a polygon representing the 5000 acre area
polygon_coords <- matrix(c(
  center_lon - half_side/(111111 * cos(center_lat * pi/180))-0.09, center_lat - half_side/111111+0.04,
  center_lon + half_side/(111111 * cos(center_lat * pi/180))-0.09, center_lat - half_side/111111+0.04,
  center_lon + half_side/(111111 * cos(center_lat * pi/180))-0.09, center_lat + half_side/111111+0.04,
  center_lon - half_side/(111111 * cos(center_lat * pi/180))-0.09, center_lat + half_side/111111+0.04,
  center_lon - half_side/(111111 * cos(center_lat * pi/180))-0.09, center_lat - half_side/111111+0.04
), ncol = 2, byrow = TRUE)

# Create an sf object
polygon_sf <- st_sfc(st_polygon(list(polygon_coords)), crs = 4326)

# Create the map
m <- leaflet() %>%
  setView(lng = center_lon, lat = center_lat, zoom = 12) %>%
  addTiles() %>%  # Add default OpenStreetMap tiles
  addPolygons(data = polygon_sf,
              fillColor = "blue",
              fillOpacity = 0.3,
              color = "black",
              weight = 2,
              popup = "Approximately 5000 acres") %>%
  addMeasure(
    position = "topright",
    primaryLengthUnit = "meters",
    primaryAreaUnit = "acres",
    activeColor = "#3D535D",
    completedColor = "#7D4479"
  )

# Display the map
m

# Save the map as an HTML file
saveWidget(m, file = "figures/vero_beach.html")

# Capture the map as PNG
webshot("figures/vero_beach.html", file = "figures/vero_beach.png", 
        cliprect = "viewport", vwidth = 800, vheight = 600)

#_____________________________________________________________#
####Chapel Hill, North Carolina

# Define the center coordinates of Vero Beach, Florida
#Chapel Hill - (35.9049, -79.0469)
center_lat <- 35.9049
center_lon <- -79.0469

# Calculate the side length of a square representing 5000 acres
acres_to_square_meters <- 5000 * 4046.86
side_length <- sqrt(acres_to_square_meters)
half_side <- side_length / 2

# Create a polygon representing the 5000 acre area
polygon_coords <- matrix(c(
  center_lon - half_side/(111111 * cos(center_lat * pi/180))-0.01, center_lat - half_side/111111+0.01,
  center_lon + half_side/(111111 * cos(center_lat * pi/180))-0.01, center_lat - half_side/111111+0.01,
  center_lon + half_side/(111111 * cos(center_lat * pi/180))-0.01, center_lat + half_side/111111+0.01,
  center_lon - half_side/(111111 * cos(center_lat * pi/180))-0.01, center_lat + half_side/111111+0.01,
  center_lon - half_side/(111111 * cos(center_lat * pi/180))-0.01, center_lat - half_side/111111+0.01
), ncol = 2, byrow = TRUE)

# Create an sf object
polygon_sf <- st_sfc(st_polygon(list(polygon_coords)), crs = 4326)

# Create the map
m <- leaflet() %>%
  setView(lng = center_lon, lat = center_lat, zoom = 12) %>%
  addTiles() %>%  # Add default OpenStreetMap tiles
  addPolygons(data = polygon_sf,
              fillColor = "blue",
              fillOpacity = 0.3,
              color = "black",
              weight = 2,
              popup = "Approximately 5000 acres") %>%
  addMeasure(
    position = "topright",
    primaryLengthUnit = "meters",
    primaryAreaUnit = "acres",
    activeColor = "#3D535D",
    completedColor = "#7D4479"
  )

# Display the map
m

# Save the map as an HTML file
saveWidget(m, file = "figures/chapel_hill.html")

# Capture the map as PNG
webshot("figures/chapel_hill.html", file = "figures/chapel_hill.png", 
        cliprect = "viewport", vwidth = 800, vheight = 600)

#_____________________________________________________________#
####Combine the plots

# Read the PNG file
img1 <- readPNG("figures/vero_beach.png")
img2 <- readPNG("figures/chapel_hill.png")

# Create a plot from the image
create_labeled_plot <- function(img, label) {
  ggplot() +
    annotation_custom(rasterGrob(img, width = unit(1, "npc"), height = unit(1, "npc")), 
                      xmin = -Inf, xmax = Inf, ymin = -Inf, ymax = Inf) +
    theme_void() +
    labs(title = label) +
    theme(plot.title = element_text(hjust = 0, size = 16, face = "bold"))
}

# Create two plots with labels
plot1 <- create_labeled_plot(img1, "A")
plot2 <- create_labeled_plot(img2, "B")

# Create a null plot for spacing
null_plot <- ggplot() + theme_void()

# Create the 2x1 plot with null plot spacing
combined_plot <- grid.arrange(plot1, null_plot, plot2, 
                              ncol = 3, 
                              widths = c(1, 0.1, 1))

# Save the combined plot
ggsave("figures/combined_plot.png", combined_plot, width = 18, height = 6, dpi = 300)
