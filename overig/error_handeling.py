def handle_exceptions():
    try:
        print("\nWelcome to the Exception Handling Demo!\n")

        # Example 1: ZeroDivisionError
        num = int(input("Enter a number to divide 100 by: "))
        result = 100 / num
        print(f"Result: {result}")

        # Example 2: ValueError
        age = int(input("Enter your age: "))
        print(f"You are {age} years old.")

        # Example 3: IndexError
        my_list = [1, 2, 3]
        index = int(input("Enter an index (0-2) to access the list: "))
        print(f"List value: {my_list[index]}")

        # Example 4: KeyError
        my_dict = {"name": "Alice", "age": 25}
        key = input("Enter a key to access the dictionary: ")
        print(f"Value: {my_dict[key]}")

        # Example 5: FileNotFoundError
        filename = input("Enter a filename to read: ")
        with open(filename, "r") as file:
            print(file.read())

        # Example 6: FloatingPointError (Rare)
        import math
        if num > 1e308:
            raise FloatingPointError("Floating point calculation overflow")

        # Example 7: OverflowError
        big_number = 2 ** 10000
        print(f"Big number calculated successfully (only if no OverflowError)")

        # Example 8: PermissionError
        with open("restricted_file.txt", "w") as file:
            file.write("Test")
    
    except ZeroDivisionError:
        print("❌ Error: You can't divide by zero!")
    
    except ValueError:
        print("❌ Error: Invalid input! Please enter a valid number.")
    
    except IndexError:
        print("❌ Error: Index out of range! The list has only 3 elements.")
    
    except KeyError:
        print("❌ Error: The specified key does not exist in the dictionary.")
    
    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    
    except PermissionError:
        print("❌ Error: You don't have permission to access this file.")
    
    except FloatingPointError:
        print("❌ Error: Floating point operation failed.")
    
    except OverflowError:
        print("❌ Error: Number too large to be represented.")
    
    except TypeError:
        print("❌ Error: Mismatched data types were used!")
    
    except IsADirectoryError:
        print("❌ Error: Expected a file, but found a directory.")
    
    except NotADirectoryError:
        print("❌ Error: Expected a directory, but found a file.")
    
    except EOFError:
        print("❌ Error: Unexpected end of input.")
    
    except ImportError:
        print("❌ Error: Module import failed.")
    
    except KeyboardInterrupt:
        print("\n❌ Error: Keyboard Interrupt detected! Exiting safely.")
    
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
    
    finally:
        print("✅ Program execution completed.")

if __name__ == "__main__":
    handle_exceptions()
