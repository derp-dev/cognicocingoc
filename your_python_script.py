import io
import re

with io.open("your.txt", "r", encoding="utf-8") as f:
    content = f.read()


def generator(code_block, keywords_and_functions):
    # Step 1: Initialize the variables
    key_dict = {}
    generated_content = ""
    current_line = 1

    # Step 2: Analyze the input code block
    for line in re.sub(r"\t", " ", content).splitlines():
        # Step 3: Check for value statements
        if ":" in line:
            key, value = line.split(":", maxsplit=1)
            key_dict[key] = value
        # Step 4: Check for function statements
        elif "fn(" in line:
            function_text, parameters = line.split("(", maxsplit=1)
            function_name, function_body = function_text.split(" ", maxsplit=1)

            if function_name not in key_dict:
                generated_content += f"def {function_name}({parameters}):\n"
            else:
                generated_content += f"def {function_name}("

            # Step 5: Create the parameter list, if needed
            if "(" in parameters:
                parameter_list = parameters.replace("(", "").replace(")", "").split(",")
                for param in parameter_list:
                    if param in keywords_and_functions:
                        generated_content += f"{param}={key_dict[param]}, "
                    else:
                        generated_content += f"{param}, "
            else:
                if function_name in keywords_and_functions:
                    generated_content += f"{function_name}={key_dict[function_name]}, "
                else:
                    generated_content += f"{function_name}, "

            generated_content += "):\n"

            # Step 6: Handle function arguments
            for arg in function_body.split(" "):
                if arg == "*":
                    generated_content += "*"
                elif arg == "~":
                    generated_content += "~"
                elif arg == "!":
                    generated_content += "!"
                elif arg == "-":
                    generated_content += "-"
                elif arg == "+":
                    generated_content += "+"
                elif arg == ">":
                    generated_content += ">"
                elif arg == "<":
                    generated_content += "<"
                elif arg == "<=":
                    generated_content += "<="
                elif arg == ">=":
                    generated_content += ">="
                elif arg == "?":
                    generated_content += "?"
                elif arg == "{":
                    generated_content += "{"
                elif arg in keywords_and_functions:
                    generated_content += f"{arg}={key_dict[arg]}, "

    # Step 7: Close the function and continue to the next line
    generated_content += ")"
    if current_line < len(content.splitlines()):
        generated_content += "\n"

    current_line += 1

    with open("output.py", "w", encoding="utf-8") as f:
        f.write(generated_content)

    return generated_content
