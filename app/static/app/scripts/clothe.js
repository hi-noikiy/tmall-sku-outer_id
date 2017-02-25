

$(function() {


	$(".addclothe-alone").bind("click", function() {
		var num = $("#sku" + $(this).attr("data-id")).attr("data-num");
		var skuid = $(this).attr("data-id");
		var $div = $(".clothe-row-" + skuid + "-0").clone().removeAttr("style")
			.removeClass("clothe-row-" + skuid + "-0")
			.addClass("clothe-row-" + skuid + "-" + num);
		$("select", $div).removeClass("clothe-" + skuid + "-0")
			.addClass("clothe-" + skuid + "-" + num);
		$("input,span", $div).attr("data-order", num);
		$(".type-sync", $div).bind("click", type_sync);
		$(".type-delete", $div).bind("click", type_delete);

		$(this).before($div);
		$(".color-row-" + skuid).append($(".color-" + skuid + "-0").clone()
			.removeAttr("style")
			.removeClass("color-" + skuid + "-0")
			.addClass("color-" + skuid + "-" + num).attr("data-order", num));
		$("#sku" + $(this).attr("data-id")).attr("data-num", (parseInt(num) + 1))
	});
	$(".addclothe").bind("click", type_add);


	$(".commodity-detail").addClass("active");

	$("img").bind("click", function() {
		$("#show-target").attr("src", $(this).attr("src"))
		$("#showimgs").modal({
			show: true
		})
	});

	$(".type-sync").bind("click", type_sync);
		$(".code-add").bind("click", add_pic);
	$(".code-delete").bind("click", code_delete);




	$(".allcheckbox").bind("click", function() {
		var tt = true;
		$("input[type='checkbox']").each(function() {
			if (tt) {
				this.checked = tt;
			} else {
				$(this).removeAttr("checked");
			}
		});
	});



	$(".recleckbox").bind("click", function() {
		$("input[type='checkbox']").each(function() {
			this.checked = !this.checked;
		})
	})

	$(".code-sync").bind("click", code_sync);






	$("#save-all").bind("click", function() {
		var data = getdata();
		$("#save-all").attr("disabled","disabled").text("正在同步,请稍后!!")

		$("#loading").show(500);



		if (data != null) {
			$.ajax({
				url: "/updata/",
				data: {
					id: $("#GETid").val(),
					csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
					data: data
				},
				dataType: "json",
				type: "post",
				success: function(req) {
					$("#save-all").removeAttr("disabled").text("保存并上传");
			
					$("#loading").hide(500);
				},
				error: function() {
					$("#save-all").removeAttr("disabled").text("保存并上传");
					alert("服务器内部出现问题, 请稍后再试!或请联系程序猿");
					$("#loading").hide(500);
				}
			});
		}else{
			alert("您有颜色信息或产品类型没有选择!");
			$("#loading").hide(500);


		};
	});


	$(".type-delete").bind("click", type_delete);



	$("#commoditysync").click(function() {
		if (confirm("这里是更新商品现有信息,可能会消耗一些时间,\n 请问要继续吗?")) {
			$(this).addClass("disabled").text("正在同步.....");
			$("#loading").show(500);
			$.ajax({
				url: '/commodity/detail/',
				type: "post",
				dataType: "json",
				data: {
					id:$("#GETid").val(),
					csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
				},
				success: function(e) {
					if (e["code"] == "ok") {
						history.go(0);
					};
				}
			})
		};
	});



});

function type_add() {
	$("input:checked").each(function() {
		
		var num = parseInt($(this).attr("data-num")),
			skuid = parseInt($(this).attr("data-id")),
			$target = $(".sku[data-id='" + skuid + "-0']").clone();

		$target.attr("data-id", skuid + "-" + (num)).attr("data-order", num);
		$(".img-row-" + skuid, $target).remove();
		$("[data-order='0']",$target).attr("data-order", num);

		$(".sku[data-id='" + skuid + "-0']").after($target);
		$(".img-row-" + skuid, $(".sku[data-id='" + skuid + "-0']")).attr("rowspan", num + 1);

		$(this).attr("data-num", num + 1);
		$(".type-sync").unbind("click");
		$(".code-add").unbind("click");
		$(".code-delete").unbind("click");
		$(".code-sync").unbind("click");
		$(".type-delete").unbind("click");


		$(".type-delete").bind("click",type_delete);
		$(".type-sync").bind("click", type_sync);
		$(".code-add").bind("click", add_pic);
		$(".code-delete").bind("click", code_delete);


		
					
		$(".code-sync").bind("click", code_sync);
	

	})





}



function type_sync() {
	var id = $(this).attr("data-id"),
	order = $(this).attr("data-order");
	var clothe_v = $('.clothe-' + id +"[data-order='"+order+"']").val();

	if ($(".checkbox-title[data-id='"+id+"']" )[0].checked) {
		var ids = [];
		$(".checkbox-title").each(function() {
			var skuid = $(this).attr("data-id");
			if (this.checked) {	
				$(".clothe-"+skuid+"[data-order='"+order+"']").find("option[value='" + clothe_v + "']").attr("selected", true)
			};
		});

		$.ajax({
			url: "/clothe/get/color/",
			data: {
				id: clothe_v
			},
			dataType: "json",
			type: "get",
			success: function(req) {
				var color_data = req.sort(function(a, b) {
					return b.length - a.length
				});

				$(".checkbox-title").each(function(){	
					if (this.checked) {
						var skuid = $(this).attr("data-id");
						var $target = $(".color-"+skuid+"[data-order='"+order+"']");
						$("option", $target).remove();


						for (var i in color_data) {
							var op = $("<option />").val(color_data[i]).text(color_data[i]);
							$target.append(op);
						};
						var color = $("#color" + skuid).attr("name");


						for (var i in color_data) {
							if (color.indexOf(color_data[i]) >= 0) {
								$target.find("option[value='" + color_data[i] + "']").attr("selected", true);

								break
							};
									};


					};
				});

			}
			
			
		});

	} else {
		alert("您点击的颜色并没有选中!")
	}
};


function code_sync() {
	var skuid = $(this).attr("data-id");
	var order = $(this).attr("data-order");
	var order2 = $(this).attr("data-order2")

	var option = $(".clothe-"+skuid+"-"+order).val()
	var dd = $(".pic-" + skuid + "-" + order2+"[data-order='"+order+"']").val();

	if ($(".checkbox-title[data-id='"+skuid+"']")[0].checked && dd != "") {
		+
		$(".checkbox-title").each(function() {
			var skuid = $(this).attr("data-id");
			if (this.checked) {

				var css = ".pic-"+skuid+"-"+order2+"[data-order='"+order+"']";
				console.log(css);


				$(css).val(dd);
			


			};
		});
	} else {
		alert("点击的选项并没有选中或编码并没有填写哦的哦!")

	};
}



function type_delete() {

	var skuid = $(this).attr("data-id");
	var num = $(".checkbox-title[data-id='"+skuid+"']" ).attr("data-num");
	var order = $(this).attr("data-order");
	console.log(skuid,order);
	if (parseInt(num) > 1) {
		if (parseInt(order) > 0) {
		
		
			$(".sku[data-id='"+skuid+"-"+order+"']").remove();
			$(".checkbox-title[data-id='"+skuid+"']").attr("data-num", num - 1)

			$(".img-row-"+skuid).attr("rowspan",num-1)

		};
		
		if (parseInt(num) > 2 && parseInt(num) > (parseInt(order) + 1)) {
			for (var i = parseInt(order); i < parseInt(num); i++) {




	
				var $t = $(".sku[data-id='"+skuid+"-"+(i+1)+"']").attr("data-id",skuid+'-'+(i)).attr("data-order",i);


				$("[data-order='" + (i+1) + "']", $t).attr("data-order", i );

				


				$(".clothe-row-" + skuid + "-" + (i+1)).addClass("clothe-row-" + skuid + "-" + i).removeClass("clothe-row-" + skuid + "-" +(i+1));
				$(".clothe-" + skuid + "-" + (i+1)).addClass("clothe-" + skuid + "-" + i).removeClass("clothe-" + skuid + "-" + (i+1));
			};
		};
	};
}

function add_pic() {

	if (String($(this).attr("id")) == "code-add") {

		$(".checkbox-title").each(function() {
			if (this.checked) {


				var skuid = $(this).attr("data-id");
				var num = parseInt($(this).attr("data-num"));

				
				for (var i = 0 ; i <num; i++) {
		
				
					var css = ".pic-div-" + skuid + "-0[data-order='0']";
					var $div = $(css, $(".pic-row-" + skuid + "[data-order='0']")).clone();



					var num2 = parseInt($(".pic-row-" + skuid + "[data-order='"+i+"']").attr("data-num"));


				



					$(".code-sync", $div).unbind("click");
					$(".code-delete", $div).unbind("click");					
					$(".code-sync", $div).bind("click", code_sync);
					$(".code-delete", $div).bind("click", code_delete);

					$div.removeClass("pic-div-" + skuid + "-0").attr("data-order2", num2).attr("data-order",i);
					$div.addClass("pic-div-" + skuid + "-" + num2).removeAttr("style");
					$("input", $div).removeClass("pic-" + skuid + "-0").addClass("pic-" + skuid + "-" + num2);
					$div.children().attr("data-order2", num2).attr("data-order",i);
					$("[data-order='0']",$div).attr("data-order",i);
					$(".code-add-"+skuid+"[data-order='"+i+"']").before($div);
					$(".pic-row-" + skuid + "[data-order='" + i + "']").attr("data-num", num2 + 1);



					};
				
			}
		})
	} else {

		var skuid = $(this).attr("data-id");
		var order = $(this).attr("data-order");
		var num = parseInt($(".pic-row-" + skuid+ "[data-order='" + order + "']").attr("data-num"));
		var order = parseInt($(this).attr("data-order"));
		var css = ".pic-div-" + skuid + "-0[data-order='0']";
		var $div = $(css, $(".pic-row-" + skuid + "[data-order='0']")).clone();
		$(".code-sync", $div).unbind("click");
		$(".code-delete", $div).unbind("click");					
		$(".code-sync", $div).bind("click", code_sync);
		$(".code-delete", $div).bind("click", code_delete);
		$div.removeClass("pic-div-" + skuid + "-0")
		$div.addClass("pic-div-" + skuid + "-" + num).removeAttr("style");
		$("input", $div).removeClass("pic-" + skuid + "-0").addClass("pic-" + skuid + "-" + num);

		$div.attr("data-order2",num).attr("data-order",order);

		$div.children().attr("data-order2", num);
		$(this).before($div)
		$(".pic-row-" + skuid + "[data-order='" + order + "']").attr("data-num", num + 1);
	}
}


function code_delete() {
	var order = parseInt($(this).attr("data-order")),
	order2 =$(this).attr("data-order2");
	var skuid = parseInt($(this).attr("data-id"));
	var num = parseInt($(".pic-row-" + skuid+"[data-order='"+order+"']").attr("data-num"));
	if (num > 1) {
		$(".pic-div-"+skuid+"-"+order2+"[data-order='"+order+"']").remove()

		var $t = $(".pic-row-" + skuid+"[data-order='"+order+"']").attr("data-num", num - 1)
		for (var i = order2 ; i < num; i++) {
			console.log(i);
			var $t = $(".pic-div-" + skuid + "-" + i,$(".pic-row-" + skuid+"[data-order='"+order+"']"))
			.removeClass("pic-div-" + skuid + "-" + i)
			.addClass("pic-div-" + skuid + "-" + (i - 1))
			.attr("data-order2", i - 1);
			$("[data-order2='"+i+"']",$t).attr("data-order2",i-1)
			$("input",$t).removeClass("pic-"+skuid+"-"+i)
			.addClass("pic-"+skuid+"-"+(i-1));


			$("span", $t).attr("data-order2", i - 1);
		
		};
	};

}



function getdata() {
	ajax_data = [];

	$(".checkbox-title").each(function(){
		var num = $(this).attr("data-num"),
		skuid = $(this).attr("data-id");
			var clothes = [];
		 for (var i = 0; i < parseInt(num); i++) {
		 	var clothe = $(".clothe-"+skuid+"[data-order='"+i+"']").val(),
		 	color = $(".color-"+skuid+"[data-order='"+i+"']").val(),
		 	pic_num = $(".pic-row-"+skuid+"[data-order='"+i+"']").attr("data-num");
		 	if (color=="") {
		 			return null
		 		};



		 	var piccode = [];
		 	for (var ii = 0; ii < parseInt(pic_num); ii++) {

		 		var v = $(".pic-"+skuid+"-"+ii+"[data-order='"+i+"']").val()
		 		if (v!="" && v!=undefined) {
		 			piccode.push(v)
		 		};
		 		};

		 		clothes.push({
		 			"clothe":clothe,
		 			"color":color,
		 			"code":piccode
		 		});


		 };
		 ajax_data.push({"data":clothes,
		 			"skuid":skuid})




	})

	if (ajax_data.length > 0) {
		return JSON.stringify(ajax_data)
	} else {
		return null
	}


}



	// $(".sku").each(function() {
	// 	var skuid = $(this).attr("data-id"),
	// 		num = $(this).attr("data-num");
	// 	var data = [];
	// 	var od_color = $(this).attr("data-odcolor");
	// 	for (var i = 0; i < parseInt(num); i++) {
	// 		if ($(".color-" + skuid + "-" + i).val() == "" || $(".color-" + skuid + "-" + i).val() == null) {
	// 			return null
	// 		};
	// 		data.push({
				
	// 			"clothe": $(".clothe-" + skuid + "-" + i).val(),
	// 			"color": $(".color-" + skuid + "-" + i).val()
	// 		})
	// 	};
	// 	var num2 = $("#pic-row-" + skuid).attr("data-num")
	// 	var data2 = [];
	// 	for (var i = 0; i < parseInt(num2); i++) {
	// 		data2.push({
	// 			"code": $(".pic-" + skuid + "-" + i).val()
	// 		})
	// 	};
	// 	ajax_data.push({
	// 		"skuid":skuid,
	// 		"clothe": data,
	// 		"code": data2,
			
	// 	})
	// });

