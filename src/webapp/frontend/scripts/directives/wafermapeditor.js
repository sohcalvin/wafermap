var svgApp = angular.module('wafermapApp');


svgApp.directive("wafermapEditor", function($parse,$window) {
  return{
    restrict: "EA",
    scope : {
        mapData : "="
    },
    template: function(elem, attr) {
            var width = attr.width || 250;
            var height = attr.height || 250;
            return "<div><button ng-click='clear()' class='btn btn-default navbar-btn'>Clear</button></div>"
                    +"<svg width="+width+" height="+height+" style='outline: solid #64B5F6' ></svg>";
    },
    link: function(scope, elem, attrs){

          scope.clear = function(){
            console.log("Clearing");
            init();
          };

          init();
          function init(){
              scope.mapData={} ;
              var canvas = getSvg();
              canvas.selectAll("*").remove();
              drawGrid(canvas,100,100);
          }
          function getSvg(){
            var d3 = $window.d3;
            var rawSvg=elem.find('svg');
            var svg = d3.select(rawSvg[0]);
            return svg;
          }

          function drawGrid(canvas, rows, columns){
              console.log("Drawing grid of " + rows + " rows by " + columns + " columns");
              var canvasSizeX = canvas.attr("width");
              var canvasSizeY = canvas.attr("height");
              var centerX = canvasSizeX /2;
              var centerY = canvasSizeY /2;
              var radius = canvasSizeX/2;
              var chipSizeX = canvasSizeX / columns;
              var chipSizeY = canvasSizeY / rows;
              var circle = canvas.append("circle")
                            .attr("cx",centerX)
                            .attr("cy",centerY)
                            .attr("r",radius)
                            .attr("fill","lightblue");
              var xTicks = d3.range(chipSizeX, canvasSizeX, chipSizeX);
              var yTicks = d3.range(chipSizeY, canvasSizeY, chipSizeY);
              var gridStroke = "gray";
              var gridStrokeWidth = 0.5;
              canvas.selectAll(".yline").data(yTicks)
                 .enter()
                 .append("line")
                 .attr("x1", 0)
                 .attr("y1", function(d){ return d;})
                 .attr("x2", canvasSizeX)
                 .attr("y2", function(d){ return d;})
                 .attr("stroke-width", gridStrokeWidth)
                 .attr("stroke", gridStroke);
              canvas.selectAll(".xline").data(xTicks)
                 .enter()
                 .append("line")
                 .attr("x1", function(d){ return d;})
                 .attr("y1", 0)
                 .attr("x2", function(d){ return d;})
                 .attr("y2", canvasSizeY)
                 .attr("stroke-width", gridStrokeWidth)
                 .attr("stroke", gridStroke);


                var drag = d3.behavior.drag();
                canvas.call(drag);
                drag.on("drag", markCell);
                canvas.on("click", markCell);
                function markCell(d, i) {
                        posXY = d3.mouse(this);
                        cellXY = positionToCell(posXY[0],posXY[1]);
                        if(!scope.mapData[cellXY]){
                            fillCell(cellXY);
                        }
                        scope.mapData[cellXY] = 1;
                }
                function fillCell(cellXY){
                    var posX = cellXY[0] * chipSizeX;
                    var posY = cellXY[1] * chipSizeY;
                    canvas.append("rect")
                            .attr("x",posX)
                            .attr("y",posY)
                            .attr("width", chipSizeX)
                            .attr("height", chipSizeY)
                            .attr("fill","black");
                }
                function positionToCell(xPos, yPos){
                    var cellXY = [];
                    cellXY[0] = Math.floor(xPos / chipSizeX);
                    cellXY[1] = Math.floor(yPos / chipSizeY);
                    return cellXY;
                }
            }
//            function drawWaferMap(){
//                if(!wafermap_data){
//                    console.log("Mapdata at " + attrs.mapData + "  not ready");
//                    return;
//                }
//                var bins = wafermap_data.bindata;
//                positions = bins["1"];
//                var canvasSizeX = 150;
//                var canvasSizeY = canvasSizeX;
//                var waferSizeX = wafermap_data.xDim;
//                var waferSizeY = wafermap_data.yDim;
//                var centerX = canvasSizeX /2;
//                var centerY = canvasSizeY /2;
//                var radius = canvasSizeX/2;
//                var chipSizeX = canvasSizeX / waferSizeX;
//                var chipSizeY = canvasSizeY / waferSizeY;
//                var title = wafermap_data.title;
//
//                 var circle = canvas.append("circle")
//                            .attr("cx",centerX)
//                            .attr("cy",centerY)
//                            .attr("r",radius)
//                            //.attr("fill","white");
//                            .attr("fill","lightblue");
//
//
//                positions.forEach(function(i){
//                    var posX = i.x * chipSizeX;
//                    var posY = i.y * chipSizeY;
//                    canvas.append("rect")
//                            .attr("x",posX)
//                            .attr("y",posY)
//                            .attr("width", chipSizeX)
//                            .attr("height", chipSizeY);
//                });
//
//                canvas.append("text")
//                    .attr("x",5)
//                    .attr("y",25)
//                    .text(title);
//            }
//
    }
  };
});