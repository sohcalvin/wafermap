function WaferMap(jsonMapData){
    //this.jsonMapData = jsonMapData;
    this._load = function(jsonMapDataUrl, callbackFunction){
        var that = this;
        d3.json(jsonMapDataUrl, function(wafermap_data){
            that.jsonMapData = wafermap_data;
            callbackFunction();
		});
    }
    this.loadAndDraw = function(jsonMapDataUrl, containerName){
        var that = this;
        this._load(jsonMapDataUrl, function(){ that.draw(containerName);})
    }
    this.draw = function(containerName){
            wafermap_data = this.jsonMapData;
			var bins = wafermap_data.bindata;
			positions = bins["1"];
			var canvasSizeX = 250;
			var canvasSizeY = canvasSizeX;
			var waferSizeX = wafermap_data.xDim;
			var waferSizeY = wafermap_data.yDim;
			var centerX = canvasSizeX /2;
			var centerY = canvasSizeY /2;
			var radius = canvasSizeX/2;
			var chipSizeX = canvasSizeX / waferSizeX;
			var chipSizeY = canvasSizeY / waferSizeY;
			var title = wafermap_data.title;

			// **** Drawing simple shapes ****
			var canvas = d3.select(containerName)
						.append("svg")
						.attr("style", "outline: thin solid black;") // Give it a border
						.attr("width",canvasSizeX)
						.attr("height",canvasSizeY);


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