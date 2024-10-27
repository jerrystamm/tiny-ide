import subprocess
import psutil

class ProgramProcessManager:

    def __init__(self):
        self.process = None
        self.output_length = []

    def processCode(self, language, code):

        match language:
            case 'Python':
                src = 'input.py'
                command = 'py src/io/' + src
            case 'JavaScript':
                src = 'input.js'
                command = 'node src/io/' + src
            case 'C++':
                src = 'input.cpp'
                command = 'src/io/input'
            case default:
                # err
                return

        self.output_length.clear()
        code_file = open('src/io/' + src, "w")
        code_file.write(code)
        code_file.close()

        if language == 'C++':
            subprocess.call(["g++", "src/io/input.cpp", "-o", "src/io/input"])

        standard_output = open("src/io/standard_output", "w+")
        self.process = subprocess.Popen(command, shell = False, stdin = subprocess.PIPE, stdout = standard_output, stderr = standard_output)
        standard_output.close()

    def writeSTDIN(self, input):
        self.process.stdin.write(input.encode('utf-8') + b"\n")
        self.process.stdin.flush()

    def runCode(self, insert_function, code, language):

        standard_output = open("src/io/standard_output", "w+")
        standard_output.truncate(0)

        self.processCode(language, code)

        while True:

            line = standard_output.readline()

            if line != '':
                insert_function(line)
                self.output_length.append(len(line))

            if self.isZombie(self.process.pid) and line == '':
                break

        standard_output.close()
            
    def isZombie(self, pid):
        try:
            process = psutil.Process(pid)

            if process.status() == 'running':
                return False
            else:
                return True
            
        except psutil.NoSuchProcess:
            return True
