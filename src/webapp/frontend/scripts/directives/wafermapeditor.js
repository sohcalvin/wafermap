var svgApp = angular.module('wafermapApp');


svgApp.directive("wafermapEditor", function($parse,$window) {
  return{
    restrict: "EA",
    template: function(elem, attr) {
            var width = attr.width || 250;
            var height = attr.height || 250;
            return "<svg width="+width+" height="+height+" style='outline: solid #64B5F6' ></svg>";
    },
    link: function(scope, elem, attrs){
          function getSvg(){
            var d3 = $window.d3;
            var rawSvg=elem.find('svg');
            var svg = d3.select(rawSvg[0]);
            return svg;
          }

          var canvas = getSvg();
          drawGrid(canvas,100,100);



          var f = $parse(attrs.mapData)
            var wafermap_data = f(scope);

            scope.$watchCollection(f, function(newVal, oldVal){
               wafermap_data=newVal;
               drawWaferMap();
           });



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
                            //.attr("fill","white");
                            .attr("fill","lightblue");

              canvas
              .selectAll("line").data([20,21,22,23,24,25,26,27,28,29]).enter()
                 .append("line")
                 .attr("x1", 0)
                 .attr("y1", function(d){ return d;})
                 .attr("x2", canvasSizeX)
                 .attr("y2", function(d){ return d;})
                 .attr("stroke-width", 1)
                 .attr("stroke", "black");
              canvas
              .selectAll("line").data([5], function(d){  return d;}).enter()
                 .append("line")
                 .attr("x1", 0)
                 .attr("y1", function(d){ return d;})
                 .attr("x2", canvasSizeX)
                 .attr("y2", function(d){ return d;})
                 .attr("stroke-width", 1)
                 .attr("stroke", "black");


          }

            function drawWaferMap(){
                if(!wafermap_data){
                    console.log("Mapdata at " + attrs.mapData + "  not ready");
                    return;
                }
                var bins = wafermap_data.bindata;
                positions = bins["1"];
                var canvasSizeX = 150;
                var canvasSizeY = canvasSizeX;
                var waferSizeX = wafermap_data.xDim;
                var waferSizeY = wafermap_data.yDim;
                var centerX = canvasSizeX /2;
                var centerY = canvasSizeY /2;
                var radius = canvasSizeX/2;
                var chipSizeX = canvasSizeX / waferSizeX;
                var chipSizeY = canvasSizeY / waferSizeY;
                var title = wafermap_data.title;

                 var circle = canvas.append("circle")
                            .attr("cx",centerX)
                            .attr("cy",centerY)
                            .attr("r",radius)
                            //.attr("fill","white");
                            .attr("fill","lightblue");


                positions.forEach(function(i){
                    var posX = i.x * chipSizeX;
                    var posY = i.y * chipSizeY;
                    canvas.append("rect")
                            .attr("x",posX)
                            .attr("y",posY)
                            .attr("width", chipSizeX)
                            .attr("height", chipSizeY);
                });

                canvas.append("text")
                    .attr("x",5)
                    .attr("y",25)
                    .text(title);
            }
    }
  };
});