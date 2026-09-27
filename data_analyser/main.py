from analyser import Dataset

def main():
        
    filepath = input("Enter CSV file path: ")

    obj = Dataset(filepath)
    obj.load()
    current = obj.row

    print(f"loaded {len(obj.row)} rows, {len(obj.column)} columns")
    print("----DATA ANALYSER----")

    while True:
        print(f"1. display data\n2. show statistics\n3. filter rows\n4. sort data\n5. search keyword\n6. save results\n7. exit")
        
        try:
            operation = int(input("choose option: "))
        except ValueError:
            print("please enter a number")
            continue

        match operation:
            case 1:
                obj.display()

            case 2:
                obj.statistics()

            case 3:
                col = input("Enter the column: ")
                on = input("Enter the column keyword: ")
            
                try:
                    result = obj.filter(col=col, on=on)
                    current = result
                    print(result)
                except KeyError as e:
                    print(f"column error: {e}")

            case 4:
                for col in obj.column:
                    print(col)

                column = input("Enter the column name: ")
                des = (input("In descending order(y/n): "))
                descend = des.lower() == 'y'
                result = obj.sort(column, descending=descend)
                print(result)
                current = result

            case 5:
                key = input("Enter the keyword to search: ")
                result = obj.search(keyword=key)
                print(result)
                current = result

            case 6:
                filepath = input("Enter the path to save: ")
                obj.save(rows=current, filepath=filepath)
            case 7:
                break
            

if __name__ == "__main__":
    main()