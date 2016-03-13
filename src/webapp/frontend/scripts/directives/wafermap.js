var svgApp = angular.module('wafermapApp');


svgApp.directive("wafermap", function($parse,$window) {
  return{
    restrict: "EA",
    template: "<svg width='150' height='150' style='outline: solid #64B5F6' ></svg>",
    link: function(scope, elem, attrs){
            var d3 = $window.d3;
            var rawSvg=elem.find('svg');
            var canvas = d3.select(rawSvg[0]);

            var f = $parse(attrs.mapData)
            var wafermap_data = f(scope);

            scope.$watchCollection(f, function(newVal, oldVal){
               wafermap_data=newVal;
               drawWaferMap();
           });

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