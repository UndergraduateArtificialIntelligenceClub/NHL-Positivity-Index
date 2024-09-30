team_data <- read.csv("total_comment_numbers_avg_pos_score_with_logos.csv")

library(ggplot2)
library(ggimage)  # For using images as points
library(showtext)
library(sysfonts)

# Add Google Fonts (Manrope)
font_add_google("Manrope", "manrope")
showtext_auto()


# Create the plot with team logos as points
plot <- ggplot(team_data, aes(x = comments, y = pos_score)) +
  # Add team logos as points
  geom_image(aes(image = logo), size = 0.05) +  # Adjust size for logos
  
  # Add a solid white horizontal line at y = 0
  geom_hline(yintercept = 0, color = "white", size = 1) +
  
  # Custom titles and labels
  labs(x = "Number of Comments", y = "Positivity Score") +
  
  # Set y-axis limits (adjust as needed)
  scale_y_continuous(limits = c(-2, 2), expand = c(0, 0)) +  # Adjust limits based on your data
  coord_cartesian(clip = 'off') +  # Ensure the axis is displayed
  
  # Apply minimal theme and remove all gridlines
  theme_minimal(base_size = 30) +  # Large base font size
  theme(
    plot.background = element_rect(fill = "#201c1c", color = "#201c1c"),  # Updated background color
    panel.background = element_rect(fill = "#201c1c"),  # Updated panel background color
    panel.grid.major = element_blank(),  # Remove major gridlines
    panel.grid.minor = element_blank(),  # Remove minor gridlines
    axis.text = element_text(color = "white", family = "manrope", size = 28),  # Large axis text
    axis.title = element_text(color = "white", size = 34, family = "manrope", face = "bold"),  # Large axis titles
    axis.line.x = element_line(color = "white"),  # White x-axis line
    axis.line.y = element_line(color = "white"),  # White y-axis line
    axis.ticks = element_line(color = "white"),  # White axis ticks
    legend.position = "none"  # No legend needed
  )

# Show the plot
print(plot)
ggsave("team_logo_scatter_plot.jpg", plot = plot, width = 8, height = 6, device = "jpeg", dpi = 300)