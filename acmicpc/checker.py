import sys
import os
import filecmp


def main(argv):
    if len(argv) == 0:
        problem_num = input('문제 번호를 입력하세요: ')
    else:
        problem_num = argv[0]
    try:
        base = os.getcwd()
        input_path = '{}/input/{}.txt'.format(base, problem_num)
        answer_path = '{}/output/{}.txt'.format(base, problem_num)
        output_path = 'output.txt'
        command = 'cat {} | python3 -u {}.py > {}'.format(
            input_path, problem_num, output_path)
        os.system(command)

        result = filecmp.cmp(answer_path, 'output.txt')
        if result:
            print('정답입니다')
            print_file(output_path)
        else:
            print('틀렸습니다')
            print_file(answer_path)
            print_file(output_path)
        os.remove(output_path)
    except FileNotFoundError:
        print('파일이 존재하지 않습니다.')


def print_file(path: str):
    file = open(path)
    file_name = path.split('/')[-1]
    print('========={}========='.format(file_name))
    for line in file.readlines():
        print(line, end='')
    file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
