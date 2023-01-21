html = """
<html>
    <header>
        <style>

            .post_table{
    background-color: black;
    color: gold;
    width:700px;
    margin-left: 400px;
    border-radius: 10px;
    text-align: center;

}

.butImg{
    width: 20px;
    height: 20px;
}
.butImg:hover{
    border-style: solid;
    border-color: black;
}
.author{
    text-align: left;
    float: left;
    width: auto;
    
}


        </style>
    </header>
    <body> 
    <table style="background-color: black;color: gold; width:700px;margin-left: 400px;border-radius: 10px;text-align: center;">
        <tr><td colspan="3" class="author">{{@comment.user}}</td></tr>
        <tr><td class="spacing_1"></td></tr>
        <tr><td  colspan="3">comment.desc</td></tr>
        <tr><td style="text-align: left;float: left; width: auto;"><input style="width: 20px; height: 20px;"  class="butImg" type="image" src="http://cdn.mcauto-images-production.sendgrid.net/ebd3842f43901da8/186fa1fd-ed80-4b59-ae94-c8bda0f063b0/940x996.png" (click)="likeComment(comment.id);">
                                <input style="border-style:solid; border-color:gold; border-radius:1px;" *ngIf="comment.liked" class="butImg" type="image" src="../../assets/likebutton.png" (click)="unlikeComment(comment.id);"></td><td class="author" >{{comment.likes-comment.dislikes}} </td>
            <td  style="text-align: left;float: left; width: auto;"><input *ngIf="!comment.disliked" class="butImg" type="image" src="../../assets/dislikebutton.png" (click)="dislikeComment(comment.id);">
                                <input class="butImg" *ngIf="comment.disliked" style="border-style:solid; border-color:gold; border-radius:1px;" type="image" src="../../assets/dislikebutton.png" (click)="undislikeComment(comment.id);"></td>
        </table> 
    </body>
    </html>
    
"""