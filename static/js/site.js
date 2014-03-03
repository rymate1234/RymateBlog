$(document).ready(function () {

    $("#editor").markdown({
        autofocus: false,
        savable: false
    })

    if ($(window).width() < 768) {
        $("#preview").hide()

        $("#editor_tab").click(function () {
            $("#editor_tab").addClass("active");
            $("#preview_tab").removeClass("active");

            $("#textview").show()
            $("#preview").hide()
        });

        $("#preview_tab").click(function () {
            $("#editor_tab").removeClass("active");
            $("#preview_tab").addClass("active");

            $("#textview").hide()
            $("#preview").show()
        });
    }
});