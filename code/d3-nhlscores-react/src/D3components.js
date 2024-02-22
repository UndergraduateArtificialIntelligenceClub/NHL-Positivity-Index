import React, { useState, useRef, useEffect } from "react";
import * as d3 from "d3";
import { isVisible } from "@testing-library/user-event/dist/utils";

const BarChartWithImages = ({ data }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    const getColor = (value) => {
      const baseGreen = d3.rgb("#008000"); // Dark green
      const lightGreen = d3.rgb("#fff"); // Light green
      const baseRed = d3.rgb("#FF0000"); // Dark red
      const lightRed = d3.rgb("#fff"); // Light red

      // Calculate the intensity based on the value's magnitude, capped between 0 and 10
      let intensity = Math.min(Math.abs(value));

      // Interpolate between the base and light colors based on the intensity
      if (value >= 0) {
        return d3.interpolate(lightGreen, baseGreen)(intensity / 10); // For positive values, interpolate between light and dark green
      } else {
        return d3.interpolate(lightRed, baseRed)(intensity / 10); // For negative values, interpolate between light and dark red
      }
    };

    if (data && chartRef.current) {
      // Define dimensions
      const margin = { top: 20, right: 20, bottom: 30, left: 500 };

      const width = 800;
      const height = 20 * data.length;

      // Create SVG canvas
      const svg = d3
        .select(chartRef.current)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      // Define scales
      const xScale = d3
        .scaleLinear()
        .domain(d3.extent(data, (d) => d.value)) // d.value is the numeric value for each bar
        .range([0, width]);

      const yScale = d3
        .scaleBand()
        .domain(data.map((d) => d.name)) // d.name is the category name for each bar
        .range([height, 0])
        .padding(0.1);

      // Create bars
      svg
        .selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("fill", (d) => getColor(d.value)) //giving it colour
        .attr("x", (d) => xScale(Math.min(0, d.value)))
        .attr("y", (d) => yScale(d.name))
        .attr("width", (d) => Math.abs(xScale(d.value) - xScale(0)))
        .attr("height", yScale.bandwidth());

      // Adding values
      svg
        .selectAll(".bar-value")
        .data(data)
        .enter()
        .append("text")
        .attr("class", "bar-value")
        .attr("x", (d) =>
          d.value > 0 ? xScale(d.value) + 5 : xScale(d.value) - 35
        ) // Position the text slightly to the right of the end of the bar
        .attr("y", (d) => yScale(d.name) + yScale.bandwidth() / 2) // Center the text vertically within the bar
        .attr("dy", ".35em") // Vertically center the text
        .text((d) => d.value) // Set the text content to the bar's value
        .attr("font-size", "12px") // Set the font size
        .attr("font-weight", 700)
        .attr("fill", "#111")
        .text((d) => d.value.toFixed(2)); //allowing 2 decimal place precision

      // Add x-axis
      svg
        .append("g")
        .attr("class", "axis-x")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(xScale));

      // Add y-axis
      svg
        .append("g")
        .attr("class", "axis-y")
        .attr("transform", `translate(-40, 0)`)
        .call(d3.axisLeft(yScale));

      // Removing visibility of axis
      d3.selectAll(".axis-x").style("display", "none"); // Hides the axes

      // Clean up on unmount
      return () => {
        svg.selectAll("*").remove();
      };
    }
  }, [data]); // Redraw chart if data changes

  return <svg ref={chartRef} style={{ overflow: "visible" }} />;
};

export default BarChartWithImages;
