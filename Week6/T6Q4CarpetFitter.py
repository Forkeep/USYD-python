def carpet_area(length,width):
    try:
        if  (not isinstance(width,float) and not isinstance(width,int)) or (not isinstance(length,float) and not isinstance(length,int)):
            raise TypeError('Error: length and width must be numeric.')
        if width < 0 :
            raise ValueError('Error: width must be positive')
        if length < 0:
            raise ValueError('Error: length must be positive')
        return width*length
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
#
# a = carpet_area(10.0,10.0)
# print(a)

def total_area(ls):
    area_sum = 0
    index = 0
    while True:
        try:
            area_one = carpet_area(ls[index][0],ls[index][1])
            if  isinstance(area_one,str):
                raise ValueError(area_one)
            else:
                area_sum += area_one
        except ValueError as e:
            # print(e)
            pass
        finally:
            index += 1
            if  index == len(ls):
                break
    return area_sum

#
# ls = [(3, 4), (10, 12), (5, 5)]
# print(total_area(ls))   # 157



