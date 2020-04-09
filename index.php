<!DOCTYPE HTML>
<html>
<head>  

<script>

           



    //jQuery.get('file.txt', function (data) {
    //    var myvar = data;
    //});

    window.onload = function () {
                               <?php
       // PHPlot Example: Simple line graph
       //require 'phplot.php';
         $file = "/home/pi/data.txt";
          $content = file_get_contents($file);
          $value = '';
          $array = [];
          $count = 0;
          $valueint = 0;
          foreach (explode("\n", $content) as $line) {
              $value =  $line ."\n";
              $array[$count] = $value;
              $count = $count +1;
            //  $value =  $line ."\n";
              // line is "word1", "word2", "word3", etc.
              //echo $value;
              $valueint = intval($value);
         }


               ?>


        var count = "<?php echo $count ?>"
        var count = parseInt(count); 



        var jArray = <?php echo json_encode($array); ?>;
        var valore = [];
        var test = [jArray.length];

        for(var i=0; i<jArray.length; i++){
            test[i] = { y: parseInt(jArray[i])};
        }



   //   var myVariable = 4;
        //var test = [
        //    { y: valore[0]},
        //    { y: 414 },
        //    { y: 520, indexLabel: "\u2191 highest", markerColor: "red", markerType: "triangle" },
        //    { y: 460 },
        //    { y: 450 },
        //    { y: 500 },
        //    { y: 480 },
        //    { y: 480 },
        //    { y: 410, indexLabel: "\u2193 lowest", markerColor: "DarkSlateGrey", markerType: "cross" },
        //    { y: 500 },
        //    { y: 480 },
        //    { y: 510 },
        //    { y: 510 }
        //];

        //test[0] = { y: parseInt(jArray[0])};
        //test[1] = { y: 100 };
        //test[2] = { y: 100 };


  var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Water pump monitor"
	},
	axisY:{
		includeZero: false
	},
	data: [{        
		type: "line",
        indexLabelFontSize: 16,

        dataPoints : test
       
    
   //     dataPoints: [          
   //         { y: 500 },
			//{ y: 414},
			//{ y: 520, indexLabel: "\u2191 highest",markerColor: "red", markerType: "triangle" },
			//{ y: 460 },
			//{ y: 450 },
			//{ y: 500 },
			//{ y: 480 },
			//{ y: 480 },
			//{ y: 410 , indexLabel: "\u2193 lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
			//{ y: 500 },
			//{ y: 480 },
   //         { y: 510 },
   //         { y: 510 }
   //     ]

           
	}]
});



chart.render();

    }

          

</script>
</head>
<body>
<div id="chartContainer" style="height: 300px; width: 100%;"></div>
<script src="graphscript.js"></script>
</body>
</html>