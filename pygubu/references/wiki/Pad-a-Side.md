To apply padding to only one side of a widget in Pygubu Designer, separate the values of both sides with a space.

## **padx**

For example, if you have: padx **50** in Pygubu, it will apply a padx of 50 to both sides (left and right).
![padx_50](https://user-images.githubusercontent.com/8467919/158874317-a23fd964-ac51-4664-af8a-c76e2e4df516.png)

***

If you want to apply the value only to the left side of the widget and not the right, change padx to **50 0**
![padx_right](https://user-images.githubusercontent.com/8467919/158874287-52c635ab-06e9-43f0-9fd4-786c27b12bb9.png)

***

Similarly, if you want to apply the padding to the right side of the widget, but not the left, change padx to **0 50**
![padx_left](https://user-images.githubusercontent.com/8467919/158874241-b5994991-cbdb-43aa-8143-6d18cc55c073.png)

This applies to both pack and grid and the same technique can be used for pady as well.

## **pady**

If you have: pady 50 in Pygubu, it will apply the padding to both the top and the bottom of the widget.

![pady_both](https://user-images.githubusercontent.com/8467919/158874215-fc3357d9-d120-4a9d-91d2-685c1c0dd2e2.png)

***

If you want to apply pady 50 to the top only, set pady to **50 0**

![pady_top](https://user-images.githubusercontent.com/8467919/158874184-e7ef4698-f352-494c-8c7a-51d67cabd6a0.png)

***

If you want to apply pady 50 to the bottom only, set pady **0 50**

![pady_bottom](https://user-images.githubusercontent.com/8467919/158874165-051534b1-8a10-4285-a364-63932ac486cc.png)

## **Different padding on each side**

The value of zero (0) means you don't want to set a value for that side, but you could specify a different value for each side.

For example, if you wanted the right side to have more spacing than the left:
padx **20 40**

![padx_diff](https://user-images.githubusercontent.com/8467919/158874139-87eab580-f4c9-416a-a476-68df49467152.png)

That will give the left side of the widget a padx of **20** and the right side of the widget a padx of **40**.