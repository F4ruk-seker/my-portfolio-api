import subprocess
import difflib


def get_installed_packages():
    """Kurulu Python paketlerini listele"""
    return subprocess.check_output([f"pip freeze"]).decode("utf-8").splitlines()


def get_requirements_txt():
    """requirements.txt içeriğini oku"""
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()


def update_requirements_txt(new_packages):
    """requirements.txt dosyasını güncelle"""
    with open('requirements.txt', 'w') as f:
        f.write("\n".join(new_packages))
    print("requirements.txt dosyası güncellendi.")


def main():
    installed_packages = get_installed_packages()
    requirements_txt = get_requirements_txt()

    diff = list(difflib.unified_diff(requirements_txt, installed_packages, lineterm=""))

    if diff:
        print("\nYüklü paketlerle 'requirements.txt' dosyası arasında farklar var:")
        print("\n".join(diff))

        confirm = input("requirements.txt dosyasını güncellemek ister misiniz? (Evet/Hayır): ").strip().lower()

        if confirm in ['evet', 'e']:
            update_requirements_txt(installed_packages)
            subprocess.run(['git', 'add', 'requirements.txt'])
            subprocess.run(['git', 'commit', '-m', 'Güncellenmiş requirements.txt dosyası'])
        else:
            print("Güncelleme iptal edildi.")
            exit(1)
    else:
        print("requirements.txt güncel.")


if __name__ == '__main__':
    main()
