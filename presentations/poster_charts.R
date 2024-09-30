library(ggplot2)
library(dplyr)
library(showtext)
library(sysfonts)
# Add Google Fonts (Manrope)
font_add_google("Manrope", "manrope")

# Enable showtext to use the added fonts
showtext_auto()
# Calculate mean and standard deviation of pos_score for color scaling
# Calculate mean and standard deviation of pos_score for color scaling
# Calculate mean and standard deviation of pos_score for color scaling
# Calculate mean and standard deviation of pos_score for color scaling
# Calculate mean and standard deviation of pos_score for color scaling
mean_pos <- mean(pts_pos_df$pos_score)
sd_pos <- sd(pts_pos_df$pos_score)

# Extracted PiYG hex colors
PiYG_colors <- c('#8e0152', '#c51b7d', '#de77ae', '#f1b6da', '#fde0ef', 
                 '#f7f7f7', '#e6f5d0', '#b8e186', '#7fbc41', '#4d9221', '#276419')

# Create the plot with PiYG color gradient based on standard deviations
plot <- ggplot(pts_pos_df, aes(x = P., y = pos_score, color = pos_score)) +
  # Scatter plot with smaller points
  geom_point(size = 3) +  # Reduced point size
  scale_color_gradientn(
    colors = PiYG_colors,  # Apply PiYG colors
    limits = c(mean_pos - 2 * sd_pos, mean_pos + 2 * sd_pos),  # Color scale based on 2 SDs
    oob = scales::squish  # Ensure out-of-bound values are handled correctly
  ) +
  
  # Add a trend line with R^2 display and a light gray dashed line
  geom_smooth(method = "lm", se = FALSE, color = "#D3D3D3", linetype = "dashed", size = 1) +
  
  # Add a solid white horizontal line at y = 0
  geom_hline(yintercept = 0, color = "white", size = 1) +
  
  # Custom titles and labels
  labs(x = "Point Percentage", y = "Positivity Score") +
  
  # Set y-axis limits to -5 to 5
  scale_y_continuous(limits = c(-5, 5), expand = c(0, 0)) +  # Set y-axis from -5 to 5
  coord_cartesian(clip = 'off') +  # Ensure the axis is displayed
  
  # Apply minimal theme and remove all gridlines
  theme_minimal(base_size = 30) +  # Increase base font size significantly for the plot
  theme(
    plot.background = element_rect(fill = "#201c1c", color = "#201c1c"),  # Updated background color
    panel.background = element_rect(fill = "#201c1c"),  # Updated panel background color
    panel.grid.major = element_blank(),  # Remove major gridlines
    panel.grid.minor = element_blank(),  # Remove minor gridlines
    axis.text = element_text(color = "white", family = "manrope", size = 28),  # Very large axis text
    axis.title = element_text(color = "white", size = 34, family = "manrope", face = "bold"),  # Very large axis titles
    axis.line.x = element_line(color = "white"),  # White x-axis line
    axis.line.y = element_line(color = "white"),  # White y-axis line
    axis.ticks = element_line(color = "white"),  # White axis ticks
    legend.position = "none"  # Remove legend if not needed
  ) +
  
  # Position the x-axis at y = 0
  theme(axis.line.x.bottom = element_line(color = "white"))  # Place the x-axis at the middle

# Fit a linear model to calculate R^2
lm_fit <- lm(pos_score ~ P., data = pts_pos_df)
r_squared <- summary(lm_fit)$r.squared

# Add bold R² annotation to the plot with very large font size
plot <- plot +
  annotate("text", x = min(pts_pos_df$P.), y = max(pts_pos_df$pos_score),
           label = paste("R² =", round(r_squared, 2)),
           color = "white", size = 14, hjust = 0, family = "manrope", face = "bold")  # Very large R^2 text

# Show the plot
print(plot)

# Save the plot to a high-resolution JPG file
ggsave("pos_score_vs_point_percent.jpg", plot = plot, width = 8, height = 6, device = "jpeg", dpi = 300)