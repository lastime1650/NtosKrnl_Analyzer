# HalpRestoreHvEnlightenment

- RVA: `0x0054D130`–`0x0054D4CA` (길이 `922` bytes)
- VA: `0x000000014054D130`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `157`개 명령, `922/922` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **51**

### Outgoing calls
- `0x0054D4BF` → [HalpTimerUpdateApiConsumers](../56/HalpTimerUpdateApiConsumers_function_00562D28.md) (function, `0x00562D28`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0054D134` → RVA `0x00FC1C60` (`.data`; read)
- `0x0054D145` → RVA `0x00FC1EE0` (`.data`; read)
- `0x0054D152` → RVA `0x00FC1EE4` (`.data`; read)
- `0x0054D160` → RVA `0x00FC1EFC` (`.data`; read)
- `0x0054D16E` → RVA `0x00FC1F00` (`.data`; read)
- `0x0054D17E` → RVA `0x00FC1F10` (`.data`; read)
- `0x0054D18E` → RVA `0x00FC1F18` (`.data`; read)
- `0x0054D19E` → RVA `0x00FC1F20` (`.data`; read)
- `0x0054D1AE` → RVA `0x00FC1F28` (`.data`; read)
- `0x0054D1BE` → RVA `0x00FC1F30` (`.data`; read)
- `0x0054D1CE` → RVA `0x00FC1F38` (`.data`; read)
- `0x0054D1DE` → RVA `0x00FC1F50` (`.data`; read)
- `0x0054D1EE` → RVA `0x00FC1F78` (`.data`; read)
- `0x0054D201` → RVA `0x00FC1F80` (`.data`; read)
- `0x0054D214` → RVA `0x00FC1F88` (`.data`; read)
- `0x0054D227` → RVA `0x00FC1F90` (`.data`; read)
- `0x0054D23A` → RVA `0x00FC1F98` (`.data`; read)
- `0x0054D24D` → RVA `0x00FC1FA0` (`.data`; read)
- `0x0054D260` → RVA `0x00FC2068` (`.data`; read)
- `0x0054D273` → RVA `0x00FC2070` (`.data`; read)
- `0x0054D286` → RVA `0x00FC1FE0` (`.data`; read)
- `0x0054D299` → RVA `0x00FC1FC8` (`.data`; read)
- `0x0054D2AC` → RVA `0x00FC1FD0` (`.data`; read)
- `0x0054D2BF` → RVA `0x00FC1EE8` (`.data`; read)
- `0x0054D2CF` → RVA `0x00FC1EF0` (`.data`; read)
- `0x0054D2DF` → RVA `0x00FC1F40` (`.data`; read)
- `0x0054D2EF` → RVA `0x00FC1F48` (`.data`; read)
- `0x0054D2FF` → RVA `0x00FC1F58` (`.data`; read)
- `0x0054D30F` → RVA `0x00FC1F60` (`.data`; read)
- `0x0054D322` → RVA `0x00FC1F68` (`.data`; read)
- `0x0054D335` → RVA `0x00FC1F70` (`.data`; read)
- `0x0054D348` → RVA `0x00FC1FB0` (`.data`; read)
- `0x0054D35B` → RVA `0x00FC1FB8` (`.data`; read)
- `0x0054D36E` → RVA `0x00FC1FC0` (`.data`; read)
- `0x0054D381` → RVA `0x00FC1FD8` (`.data`; read)
- `0x0054D394` → RVA `0x00FC1FE8` (`.data`; read)
- `0x0054D3A7` → RVA `0x00FC1FF0` (`.data`; read)
- `0x0054D3BA` → RVA `0x00FC1FF8` (`.data`; read)
- `0x0054D3CD` → RVA `0x00FC2000` (`.data`; read)
- `0x0054D3E0` → RVA `0x00FC2008` (`.data`; read)
- `0x0054D3F3` → RVA `0x00FC2010` (`.data`; read)
- `0x0054D406` → RVA `0x00FC2018` (`.data`; read)
- `0x0054D419` → RVA `0x00FC2020` (`.data`; read)
- `0x0054D42C` → RVA `0x00FC2028` (`.data`; read)
- `0x0054D43F` → RVA `0x00FC2030` (`.data`; read)
- `0x0054D452` → RVA `0x00FC2038` (`.data`; read)
- `0x0054D465` → RVA `0x00FC2040` (`.data`; read)
- `0x0054D478` → RVA `0x00FC2048` (`.data`; read)
- `0x0054D48B` → RVA `0x00FC2050` (`.data`; read)
- `0x0054D49E` → RVA `0x00FC2058` (`.data`; read)
- `0x0054D4B1` → RVA `0x00FC2060` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054D130  48 83 EC 28                     sub rsp, 0x28
0054D134  48 8D 05 25 4B A7 00            lea rax, [rip + 0xa74b25]
0054D13B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0054D140  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D145  8B 05 95 4D A7 00               mov eax, dword ptr [rip + 0xa74d95]
0054D14B  89 01                           mov dword ptr [rcx], eax
0054D14D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D152  8B 05 8C 4D A7 00               mov eax, dword ptr [rip + 0xa74d8c]
0054D158  89 41 04                        mov dword ptr [rcx + 4], eax
0054D15B  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D160  8B 05 96 4D A7 00               mov eax, dword ptr [rip + 0xa74d96]
0054D166  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
0054D169  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D16E  48 8B 05 8B 4D A7 00            mov rax, qword ptr [rip + 0xa74d8b]
0054D175  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
0054D179  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D17E  48 8B 05 8B 4D A7 00            mov rax, qword ptr [rip + 0xa74d8b]
0054D185  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
0054D189  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D18E  48 8B 05 83 4D A7 00            mov rax, qword ptr [rip + 0xa74d83]
0054D195  48 89 41 38                     mov qword ptr [rcx + 0x38], rax
0054D199  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D19E  48 8B 05 7B 4D A7 00            mov rax, qword ptr [rip + 0xa74d7b]
0054D1A5  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
0054D1A9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D1AE  48 8B 05 73 4D A7 00            mov rax, qword ptr [rip + 0xa74d73]
0054D1B5  48 89 41 48                     mov qword ptr [rcx + 0x48], rax
0054D1B9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D1BE  48 8B 05 6B 4D A7 00            mov rax, qword ptr [rip + 0xa74d6b]
0054D1C5  48 89 41 50                     mov qword ptr [rcx + 0x50], rax
0054D1C9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D1CE  48 8B 05 63 4D A7 00            mov rax, qword ptr [rip + 0xa74d63]
0054D1D5  48 89 41 58                     mov qword ptr [rcx + 0x58], rax
0054D1D9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D1DE  48 8B 05 6B 4D A7 00            mov rax, qword ptr [rip + 0xa74d6b]
0054D1E5  48 89 41 70                     mov qword ptr [rcx + 0x70], rax
0054D1E9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D1EE  48 8B 05 83 4D A7 00            mov rax, qword ptr [rip + 0xa74d83]
0054D1F5  48 89 81 98 00 00 00            mov qword ptr [rcx + 0x98], rax
0054D1FC  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D201  48 8B 05 78 4D A7 00            mov rax, qword ptr [rip + 0xa74d78]
0054D208  48 89 81 A0 00 00 00            mov qword ptr [rcx + 0xa0], rax
0054D20F  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D214  48 8B 05 6D 4D A7 00            mov rax, qword ptr [rip + 0xa74d6d]
0054D21B  48 89 81 A8 00 00 00            mov qword ptr [rcx + 0xa8], rax
0054D222  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D227  48 8B 05 62 4D A7 00            mov rax, qword ptr [rip + 0xa74d62]
0054D22E  48 89 81 B0 00 00 00            mov qword ptr [rcx + 0xb0], rax
0054D235  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D23A  48 8B 05 57 4D A7 00            mov rax, qword ptr [rip + 0xa74d57]
0054D241  48 89 81 B8 00 00 00            mov qword ptr [rcx + 0xb8], rax
0054D248  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D24D  48 8B 05 4C 4D A7 00            mov rax, qword ptr [rip + 0xa74d4c]
0054D254  48 89 81 C0 00 00 00            mov qword ptr [rcx + 0xc0], rax
0054D25B  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D260  48 8B 05 01 4E A7 00            mov rax, qword ptr [rip + 0xa74e01]
0054D267  48 89 81 88 01 00 00            mov qword ptr [rcx + 0x188], rax
0054D26E  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D273  48 8B 05 F6 4D A7 00            mov rax, qword ptr [rip + 0xa74df6]
0054D27A  48 89 81 90 01 00 00            mov qword ptr [rcx + 0x190], rax
0054D281  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D286  48 8B 05 53 4D A7 00            mov rax, qword ptr [rip + 0xa74d53]
0054D28D  48 89 81 00 01 00 00            mov qword ptr [rcx + 0x100], rax
0054D294  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D299  48 8B 05 28 4D A7 00            mov rax, qword ptr [rip + 0xa74d28]
0054D2A0  48 89 81 E8 00 00 00            mov qword ptr [rcx + 0xe8], rax
0054D2A7  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D2AC  48 8B 05 1D 4D A7 00            mov rax, qword ptr [rip + 0xa74d1d]
0054D2B3  48 89 81 F0 00 00 00            mov qword ptr [rcx + 0xf0], rax
0054D2BA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D2BF  48 8B 05 22 4C A7 00            mov rax, qword ptr [rip + 0xa74c22]
0054D2C6  48 89 41 08                     mov qword ptr [rcx + 8], rax
0054D2CA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D2CF  48 8B 05 1A 4C A7 00            mov rax, qword ptr [rip + 0xa74c1a]
0054D2D6  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0054D2DA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D2DF  48 8B 05 5A 4C A7 00            mov rax, qword ptr [rip + 0xa74c5a]
0054D2E6  48 89 41 60                     mov qword ptr [rcx + 0x60], rax
0054D2EA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D2EF  48 8B 05 52 4C A7 00            mov rax, qword ptr [rip + 0xa74c52]
0054D2F6  48 89 41 68                     mov qword ptr [rcx + 0x68], rax
0054D2FA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D2FF  48 8B 05 52 4C A7 00            mov rax, qword ptr [rip + 0xa74c52]
0054D306  48 89 41 78                     mov qword ptr [rcx + 0x78], rax
0054D30A  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D30F  48 8B 05 4A 4C A7 00            mov rax, qword ptr [rip + 0xa74c4a]
0054D316  48 89 81 80 00 00 00            mov qword ptr [rcx + 0x80], rax
0054D31D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D322  48 8B 05 3F 4C A7 00            mov rax, qword ptr [rip + 0xa74c3f]
0054D329  48 89 81 88 00 00 00            mov qword ptr [rcx + 0x88], rax
0054D330  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D335  48 8B 05 34 4C A7 00            mov rax, qword ptr [rip + 0xa74c34]
0054D33C  48 89 81 90 00 00 00            mov qword ptr [rcx + 0x90], rax
0054D343  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D348  48 8B 05 61 4C A7 00            mov rax, qword ptr [rip + 0xa74c61]
0054D34F  48 89 81 D0 00 00 00            mov qword ptr [rcx + 0xd0], rax
0054D356  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D35B  48 8B 05 56 4C A7 00            mov rax, qword ptr [rip + 0xa74c56]
0054D362  48 89 81 D8 00 00 00            mov qword ptr [rcx + 0xd8], rax
0054D369  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D36E  48 8B 05 4B 4C A7 00            mov rax, qword ptr [rip + 0xa74c4b]
0054D375  48 89 81 E0 00 00 00            mov qword ptr [rcx + 0xe0], rax
0054D37C  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D381  48 8B 05 50 4C A7 00            mov rax, qword ptr [rip + 0xa74c50]
0054D388  48 89 81 F8 00 00 00            mov qword ptr [rcx + 0xf8], rax
0054D38F  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D394  48 8B 05 4D 4C A7 00            mov rax, qword ptr [rip + 0xa74c4d]
0054D39B  48 89 81 08 01 00 00            mov qword ptr [rcx + 0x108], rax
0054D3A2  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D3A7  48 8B 05 42 4C A7 00            mov rax, qword ptr [rip + 0xa74c42]
0054D3AE  48 89 81 10 01 00 00            mov qword ptr [rcx + 0x110], rax
0054D3B5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D3BA  48 8B 05 37 4C A7 00            mov rax, qword ptr [rip + 0xa74c37]
0054D3C1  48 89 81 18 01 00 00            mov qword ptr [rcx + 0x118], rax
0054D3C8  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D3CD  48 8B 05 2C 4C A7 00            mov rax, qword ptr [rip + 0xa74c2c]
0054D3D4  48 89 81 20 01 00 00            mov qword ptr [rcx + 0x120], rax
0054D3DB  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D3E0  48 8B 05 21 4C A7 00            mov rax, qword ptr [rip + 0xa74c21]
0054D3E7  48 89 81 28 01 00 00            mov qword ptr [rcx + 0x128], rax
0054D3EE  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D3F3  48 8B 05 16 4C A7 00            mov rax, qword ptr [rip + 0xa74c16]
0054D3FA  48 89 81 30 01 00 00            mov qword ptr [rcx + 0x130], rax
0054D401  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D406  48 8B 05 0B 4C A7 00            mov rax, qword ptr [rip + 0xa74c0b]
0054D40D  48 89 81 38 01 00 00            mov qword ptr [rcx + 0x138], rax
0054D414  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D419  48 8B 05 00 4C A7 00            mov rax, qword ptr [rip + 0xa74c00]
0054D420  48 89 81 40 01 00 00            mov qword ptr [rcx + 0x140], rax
0054D427  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D42C  48 8B 05 F5 4B A7 00            mov rax, qword ptr [rip + 0xa74bf5]
0054D433  48 89 81 48 01 00 00            mov qword ptr [rcx + 0x148], rax
0054D43A  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D43F  48 8B 05 EA 4B A7 00            mov rax, qword ptr [rip + 0xa74bea]
0054D446  48 89 81 50 01 00 00            mov qword ptr [rcx + 0x150], rax
0054D44D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D452  48 8B 05 DF 4B A7 00            mov rax, qword ptr [rip + 0xa74bdf]
0054D459  48 89 81 58 01 00 00            mov qword ptr [rcx + 0x158], rax
0054D460  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D465  48 8B 05 D4 4B A7 00            mov rax, qword ptr [rip + 0xa74bd4]
0054D46C  48 89 81 60 01 00 00            mov qword ptr [rcx + 0x160], rax
0054D473  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D478  48 8B 05 C9 4B A7 00            mov rax, qword ptr [rip + 0xa74bc9]
0054D47F  48 89 81 68 01 00 00            mov qword ptr [rcx + 0x168], rax
0054D486  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D48B  48 8B 05 BE 4B A7 00            mov rax, qword ptr [rip + 0xa74bbe]
0054D492  48 89 81 70 01 00 00            mov qword ptr [rcx + 0x170], rax
0054D499  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D49E  48 8B 05 B3 4B A7 00            mov rax, qword ptr [rip + 0xa74bb3]
0054D4A5  48 89 81 78 01 00 00            mov qword ptr [rcx + 0x178], rax
0054D4AC  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054D4B1  48 8B 05 A8 4B A7 00            mov rax, qword ptr [rip + 0xa74ba8]
0054D4B8  48 89 81 80 01 00 00            mov qword ptr [rcx + 0x180], rax
0054D4BF  E8 64 58 01 00                  call 0x140562d28
0054D4C4  48 83 C4 28                     add rsp, 0x28
0054D4C8  C3                              ret
0054D4C9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpRestoreHvEnlightenment(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = v_rip + 10963749;
    *(unsigned int *)(v_stack_p8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10964373)));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10964364)));
    *(unsigned int *)(v_stack_p8 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10964374)));
    *(unsigned __int64 *)(v_stack_p8 + 32) = *(unsigned __int64 *)(v_rip + 10964363);
    *(unsigned __int64 *)(v_stack_p8 + 48) = *(unsigned __int64 *)(v_rip + 10964363);
    *(unsigned __int64 *)(v_stack_p8 + 56) = *(unsigned __int64 *)(v_rip + 10964355);
    *(unsigned __int64 *)(v_stack_p8 + 64) = *(unsigned __int64 *)(v_rip + 10964347);
    *(unsigned __int64 *)(v_stack_p8 + 72) = *(unsigned __int64 *)(v_rip + 10964339);
    *(unsigned __int64 *)(v_stack_p8 + 80) = *(unsigned __int64 *)(v_rip + 10964331);
    *(unsigned __int64 *)(v_stack_p8 + 88) = *(unsigned __int64 *)(v_rip + 10964323);
    *(unsigned __int64 *)(v_stack_p8 + 112) = *(unsigned __int64 *)(v_rip + 10964331);
    *(unsigned __int64 *)(v_stack_p8 + 152) = *(unsigned __int64 *)(v_rip + 10964355);
    *(unsigned __int64 *)(v_stack_p8 + 160) = *(unsigned __int64 *)(v_rip + 10964344);
    *(unsigned __int64 *)(v_stack_p8 + 168) = *(unsigned __int64 *)(v_rip + 10964333);
    *(unsigned __int64 *)(v_stack_p8 + 176) = *(unsigned __int64 *)(v_rip + 10964322);
    *(unsigned __int64 *)(v_stack_p8 + 184) = *(unsigned __int64 *)(v_rip + 10964311);
    *(unsigned __int64 *)(v_stack_p8 + 192) = *(unsigned __int64 *)(v_rip + 10964300);
    *(unsigned __int64 *)(v_stack_p8 + 392) = *(unsigned __int64 *)(v_rip + 10964481);
    *(unsigned __int64 *)(v_stack_p8 + 400) = *(unsigned __int64 *)(v_rip + 10964470);
    *(unsigned __int64 *)(v_stack_p8 + 256) = *(unsigned __int64 *)(v_rip + 10964307);
    *(unsigned __int64 *)(v_stack_p8 + 232) = *(unsigned __int64 *)(v_rip + 10964264);
    *(unsigned __int64 *)(v_stack_p8 + 240) = *(unsigned __int64 *)(v_rip + 10964253);
    *(unsigned __int64 *)(v_stack_p8 + 8) = *(unsigned __int64 *)(v_rip + 10964002);
    *(unsigned __int64 *)(v_stack_p8 + 16) = *(unsigned __int64 *)(v_rip + 10963994);
    *(unsigned __int64 *)(v_stack_p8 + 96) = *(unsigned __int64 *)(v_rip + 10964058);
    *(unsigned __int64 *)(v_stack_p8 + 104) = *(unsigned __int64 *)(v_rip + 10964050);
    *(unsigned __int64 *)(v_stack_p8 + 120) = *(unsigned __int64 *)(v_rip + 10964050);
    *(unsigned __int64 *)(v_stack_p8 + 128) = *(unsigned __int64 *)(v_rip + 10964042);
    *(unsigned __int64 *)(v_stack_p8 + 136) = *(unsigned __int64 *)(v_rip + 10964031);
    *(unsigned __int64 *)(v_stack_p8 + 144) = *(unsigned __int64 *)(v_rip + 10964020);
    *(unsigned __int64 *)(v_stack_p8 + 208) = *(unsigned __int64 *)(v_rip + 10964065);
    *(unsigned __int64 *)(v_stack_p8 + 216) = *(unsigned __int64 *)(v_rip + 10964054);
    *(unsigned __int64 *)(v_stack_p8 + 224) = *(unsigned __int64 *)(v_rip + 10964043);
    *(unsigned __int64 *)(v_stack_p8 + 248) = *(unsigned __int64 *)(v_rip + 10964048);
    *(unsigned __int64 *)(v_stack_p8 + 264) = *(unsigned __int64 *)(v_rip + 10964045);
    *(unsigned __int64 *)(v_stack_p8 + 272) = *(unsigned __int64 *)(v_rip + 10964034);
    *(unsigned __int64 *)(v_stack_p8 + 280) = *(unsigned __int64 *)(v_rip + 10964023);
    *(unsigned __int64 *)(v_stack_p8 + 288) = *(unsigned __int64 *)(v_rip + 10964012);
    *(unsigned __int64 *)(v_stack_p8 + 296) = *(unsigned __int64 *)(v_rip + 10964001);
    *(unsigned __int64 *)(v_stack_p8 + 304) = *(unsigned __int64 *)(v_rip + 10963990);
    *(unsigned __int64 *)(v_stack_p8 + 312) = *(unsigned __int64 *)(v_rip + 10963979);
    *(unsigned __int64 *)(v_stack_p8 + 320) = *(unsigned __int64 *)(v_rip + 10963968);
    *(unsigned __int64 *)(v_stack_p8 + 328) = *(unsigned __int64 *)(v_rip + 10963957);
    *(unsigned __int64 *)(v_stack_p8 + 336) = *(unsigned __int64 *)(v_rip + 10963946);
    *(unsigned __int64 *)(v_stack_p8 + 344) = *(unsigned __int64 *)(v_rip + 10963935);
    *(unsigned __int64 *)(v_stack_p8 + 352) = *(unsigned __int64 *)(v_rip + 10963924);
    *(unsigned __int64 *)(v_stack_p8 + 360) = *(unsigned __int64 *)(v_rip + 10963913);
    *(unsigned __int64 *)(v_stack_p8 + 368) = *(unsigned __int64 *)(v_rip + 10963902);
    *(unsigned __int64 *)(v_stack_p8 + 376) = *(unsigned __int64 *)(v_rip + 10963891);
    *(unsigned __int64 *)(v_stack_p8 + 384) = *(unsigned __int64 *)(v_rip + 10963880);
    result = HalpTimerUpdateApiConsumers(v_stack_p8, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpRestoreHvEnlightenment(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = v_rip + 10963749;
    *(uint32_t *)(v_stack_p8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA74D95)));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA74D8C)));
    *(uint32_t *)(v_stack_p8 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA74D96)));
    *(uint64_t *)(v_stack_p8 + 0x20) = *(uint64_t *)(v_rip + 0xA74D8B);
    *(uint64_t *)(v_stack_p8 + 0x30) = *(uint64_t *)(v_rip + 0xA74D8B);
    *(uint64_t *)(v_stack_p8 + 0x38) = *(uint64_t *)(v_rip + 0xA74D83);
    *(uint64_t *)(v_stack_p8 + 0x40) = *(uint64_t *)(v_rip + 0xA74D7B);
    *(uint64_t *)(v_stack_p8 + 0x48) = *(uint64_t *)(v_rip + 0xA74D73);
    *(uint64_t *)(v_stack_p8 + 0x50) = *(uint64_t *)(v_rip + 0xA74D6B);
    *(uint64_t *)(v_stack_p8 + 0x58) = *(uint64_t *)(v_rip + 0xA74D63);
    *(uint64_t *)(v_stack_p8 + 0x70) = *(uint64_t *)(v_rip + 0xA74D6B);
    *(uint64_t *)(v_stack_p8 + 0x98) = *(uint64_t *)(v_rip + 0xA74D83);
    *(uint64_t *)(v_stack_p8 + 0xA0) = *(uint64_t *)(v_rip + 0xA74D78);
    *(uint64_t *)(v_stack_p8 + 0xA8) = *(uint64_t *)(v_rip + 0xA74D6D);
    *(uint64_t *)(v_stack_p8 + 0xB0) = *(uint64_t *)(v_rip + 0xA74D62);
    *(uint64_t *)(v_stack_p8 + 0xB8) = *(uint64_t *)(v_rip + 0xA74D57);
    *(uint64_t *)(v_stack_p8 + 0xC0) = *(uint64_t *)(v_rip + 0xA74D4C);
    *(uint64_t *)(v_stack_p8 + 0x188) = *(uint64_t *)(v_rip + 0xA74E01);
    *(uint64_t *)(v_stack_p8 + 0x190) = *(uint64_t *)(v_rip + 0xA74DF6);
    *(uint64_t *)(v_stack_p8 + 0x100) = *(uint64_t *)(v_rip + 0xA74D53);
    *(uint64_t *)(v_stack_p8 + 0xE8) = *(uint64_t *)(v_rip + 0xA74D28);
    *(uint64_t *)(v_stack_p8 + 0xF0) = *(uint64_t *)(v_rip + 0xA74D1D);
    *(uint64_t *)(v_stack_p8 + 0x8) = *(uint64_t *)(v_rip + 0xA74C22);
    *(uint64_t *)(v_stack_p8 + 0x10) = *(uint64_t *)(v_rip + 0xA74C1A);
    *(uint64_t *)(v_stack_p8 + 0x60) = *(uint64_t *)(v_rip + 0xA74C5A);
    *(uint64_t *)(v_stack_p8 + 0x68) = *(uint64_t *)(v_rip + 0xA74C52);
    *(uint64_t *)(v_stack_p8 + 0x78) = *(uint64_t *)(v_rip + 0xA74C52);
    *(uint64_t *)(v_stack_p8 + 0x80) = *(uint64_t *)(v_rip + 0xA74C4A);
    *(uint64_t *)(v_stack_p8 + 0x88) = *(uint64_t *)(v_rip + 0xA74C3F);
    *(uint64_t *)(v_stack_p8 + 0x90) = *(uint64_t *)(v_rip + 0xA74C34);
    *(uint64_t *)(v_stack_p8 + 0xD0) = *(uint64_t *)(v_rip + 0xA74C61);
    *(uint64_t *)(v_stack_p8 + 0xD8) = *(uint64_t *)(v_rip + 0xA74C56);
    *(uint64_t *)(v_stack_p8 + 0xE0) = *(uint64_t *)(v_rip + 0xA74C4B);
    *(uint64_t *)(v_stack_p8 + 0xF8) = *(uint64_t *)(v_rip + 0xA74C50);
    *(uint64_t *)(v_stack_p8 + 0x108) = *(uint64_t *)(v_rip + 0xA74C4D);
    *(uint64_t *)(v_stack_p8 + 0x110) = *(uint64_t *)(v_rip + 0xA74C42);
    *(uint64_t *)(v_stack_p8 + 0x118) = *(uint64_t *)(v_rip + 0xA74C37);
    *(uint64_t *)(v_stack_p8 + 0x120) = *(uint64_t *)(v_rip + 0xA74C2C);
    *(uint64_t *)(v_stack_p8 + 0x128) = *(uint64_t *)(v_rip + 0xA74C21);
    *(uint64_t *)(v_stack_p8 + 0x130) = *(uint64_t *)(v_rip + 0xA74C16);
    *(uint64_t *)(v_stack_p8 + 0x138) = *(uint64_t *)(v_rip + 0xA74C0B);
    *(uint64_t *)(v_stack_p8 + 0x140) = *(uint64_t *)(v_rip + 0xA74C00);
    *(uint64_t *)(v_stack_p8 + 0x148) = *(uint64_t *)(v_rip + 0xA74BF5);
    *(uint64_t *)(v_stack_p8 + 0x150) = *(uint64_t *)(v_rip + 0xA74BEA);
    *(uint64_t *)(v_stack_p8 + 0x158) = *(uint64_t *)(v_rip + 0xA74BDF);
    *(uint64_t *)(v_stack_p8 + 0x160) = *(uint64_t *)(v_rip + 0xA74BD4);
    *(uint64_t *)(v_stack_p8 + 0x168) = *(uint64_t *)(v_rip + 0xA74BC9);
    *(uint64_t *)(v_stack_p8 + 0x170) = *(uint64_t *)(v_rip + 0xA74BBE);
    *(uint64_t *)(v_stack_p8 + 0x178) = *(uint64_t *)(v_rip + 0xA74BB3);
    *(uint64_t *)(v_stack_p8 + 0x180) = *(uint64_t *)(v_rip + 0xA74BA8);
    result = HalpTimerUpdateApiConsumers(v_stack_p8, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054D130&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054D130[BB_0054D130]
  bb_0054D4C9[BB_0054D4C9]
```
