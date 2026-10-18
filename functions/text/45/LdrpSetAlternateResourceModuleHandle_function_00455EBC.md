# LdrpSetAlternateResourceModuleHandle

- RVA: `0x00455EBC`–`0x004562EA` (길이 `1,070` bytes)
- VA: `0x0000000140455EBC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7BFC`
- 디코드: `255`개 명령, `1,070/1,070` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00455F1D` → [LdrpInitMuiCrits](LdrpInitMuiCrits_function_00455B80.md) (function, `0x00455B80`)
- `0x00455F36` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00455F9B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004560F8` → [MmUnmapViewInSessionSpace](../../page/A5/MmUnmapViewInSessionSpace_function_00A5FE60.md) (function, `0x00A5FE60`)
- `0x00456105` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00456156` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0045617C` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0045618A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004562BA` → [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) (function, `0x00396850`)

### Direct callers
- [LdrpGetRcConfig](LdrpGetRcConfig_function_0045555C.md) at `0x00455687`
- [LdrLoadAlternateResourceModuleEx](LdrLoadAlternateResourceModuleEx_function_004557CC.md) at `0x0045590F`
- [sub_00B42D56](../../page/B4/Unknown_function_00B42D56.md) at `0x00B42FE7`

### Static image references
- `0x00455F2F` → RVA `0x00F05C60` (`.data`; read)
- `0x00455F4B` → RVA `0x00F05C54` (`.data`; read)
- `0x00455F5B` → RVA `0x00F05C58` (`.data`; read)
- `0x00455FAC` → RVA `0x00F05C58` (`.data`; write)
- `0x00455FB3` → RVA `0x00F05C50` (`.data`; write)
- `0x00456136` → RVA `0x00F05C50` (`.data`; read)
- `0x0045629E` → RVA `0x00F05C54` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00455F9B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004560F8` → [MmUnmapViewInSessionSpace](../../page/A5/MmUnmapViewInSessionSpace_function_00A5FE60.md) (`.text` → `PAGE`)
  - `0x00456156` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0045618A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00455EBC  48 8B C4                        mov rax, rsp
00455EBF  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00455EC3  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00455EC7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00455ECB  48 89 48 08                     mov qword ptr [rax + 8], rcx
00455ECF  57                              push rdi
00455ED0  41 54                           push r12
00455ED2  41 55                           push r13
00455ED4  41 56                           push r14
00455ED6  41 57                           push r15
00455ED8  48 83 EC 40                     sub rsp, 0x40
00455EDC  4D 8B F8                        mov r15, r8
00455EDF  4C 8B E2                        mov r12, rdx
00455EE2  48 8B F1                        mov rsi, rcx
00455EE5  33 FF                           xor edi, edi
00455EE7  48 85 C9                        test rcx, rcx
00455EEA  0F 84 EC 03 00 00               je 0x1404562dc
00455EF0  44 8B B4 24 98 00 00 00         mov r14d, dword ptr [rsp + 0x98]
00455EF8  41 F7 C6 CC FF FF FF            test r14d, 0xffffffcc
00455EFF  0F 85 D7 03 00 00               jne 0x1404562dc
00455F05  41 8B C6                        mov eax, r14d
00455F08  83 E0 03                        and eax, 3
00455F0B  3C 03                           cmp al, 3
00455F0D  0F 84 C9 03 00 00               je 0x1404562dc
00455F13  41 F6 C6 01                     test r14b, 1
00455F17  0F 85 C3 03 00 00               jne 0x1404562e0
00455F1D  E8 5E FC FF FF                  call 0x140455b80
00455F22  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00455F27  45 33 C9                        xor r9d, r9d
00455F2A  45 33 C0                        xor r8d, r8d
00455F2D  33 D2                           xor edx, edx
00455F2F  48 8D 0D 2A FD AA 00            lea rcx, [rip + 0xaafd2a]
00455F36  E8 75 87 DB FF                  call 0x14020e6b0
00455F3B  90                              nop
00455F3C  8B DF                           mov ebx, edi
00455F3E  44 0F B7 AC 24 90 00 00 00      movzx r13d, word ptr [rsp + 0x90]
00455F47  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00455F4B  8B 05 03 FD AA 00               mov eax, dword ptr [rip + 0xaafd03]
00455F51  3B D8                           cmp ebx, eax
00455F53  73 1C                           jae 0x140455f71
00455F55  8B C3                           mov eax, ebx
00455F57  48 C1 E0 06                     shl rax, 6
00455F5B  48 8B 0D F6 FC AA 00            mov rcx, qword ptr [rip + 0xaafcf6]
00455F62  48 39 74 08 08                  cmp qword ptr [rax + rcx + 8], rsi
00455F67  0F 84 46 01 00 00               je 0x1404560b3
00455F6D  FF C3                           inc ebx
00455F6F  EB D6                           jmp 0x140455f47
00455F71  41 F6 C6 10                     test r14b, 0x10
00455F75  0F 85 2A 03 00 00               jne 0x1404562a5
00455F7B  48 8B 35 D6 FC AA 00            mov rsi, qword ptr [rip + 0xaafcd6]
00455F82  48 85 F6                        test rsi, rsi
00455F85  0F 85 AB 01 00 00               jne 0x140456136
00455F8B  BA 00 08 00 00                  mov edx, 0x800
00455F90  B9 00 01 00 00                  mov ecx, 0x100
00455F95  41 B8 72 74 50 69               mov r8d, 0x69507472
00455F9B  E8 50 C1 72 00                  call 0x140b820f0
00455FA0  48 8B F0                        mov rsi, rax
00455FA3  48 85 C0                        test rax, rax
00455FA6  0F 84 F9 02 00 00               je 0x1404562a5
00455FAC  48 89 05 A5 FC AA 00            mov qword ptr [rip + 0xaafca5], rax
00455FB3  C7 05 93 FC AA 00 20 00 00 00   mov dword ptr [rip + 0xaafc93], 0x20
00455FBD  8B D7                           mov edx, edi
00455FBF  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00455FC3  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
00455FC8  8B 05 86 FC AA 00               mov eax, dword ptr [rip + 0xaafc86]
00455FCE  3B D0                           cmp edx, eax
00455FD0  73 19                           jae 0x140455feb
00455FD2  8B CA                           mov ecx, edx
00455FD4  48 C1 E1 06                     shl rcx, 6
00455FD8  4C 39 54 31 08                  cmp qword ptr [rcx + rsi + 8], r10
00455FDD  0F 84 C7 01 00 00               je 0x1404561aa
00455FE3  FF C2                           inc edx
00455FE5  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00455FE9  EB DD                           jmp 0x140455fc8
00455FEB  49 8B D2                        mov rdx, r10
00455FEE  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
00455FF2  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00455FF7  48 8B CF                        mov rcx, rdi
00455FFA  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00455FFF  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00456004  0F 84 3F 02 00 00               je 0x140456249
0045600A  B8 4D 5A 00 00                  mov eax, 0x5a4d
0045600F  66 39 02                        cmp word ptr [rdx], ax
00456012  75 4A                           jne 0x14045605e
00456014  8B 4A 3C                        mov ecx, dword ptr [rdx + 0x3c]
00456017  48 03 CA                        add rcx, rdx
0045601A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0045601F  48 3B CA                        cmp rcx, rdx
00456022  72 3A                           jb 0x14045605e
00456024  49 B8 FF FF FE FF FF 7F 00 00   movabs r8, 0x7ffffffeffff
0045602E  49 3B D0                        cmp rdx, r8
00456031  77 11                           ja 0x140456044
00456033  48 8D 81 07 01 00 00            lea rax, [rcx + 0x107]
0045603A  48 3B C1                        cmp rax, rcx
0045603D  72 1F                           jb 0x14045605e
0045603F  49 3B C0                        cmp rax, r8
00456042  77 1A                           ja 0x14045605e
00456044  81 39 50 45 00 00               cmp dword ptr [rcx], 0x4550
0045604A  75 12                           jne 0x14045605e
0045604C  8B D7                           mov edx, edi
0045604E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00456053  85 D2                           test edx, edx
00456055  48 0F 49 C1                     cmovns rax, rcx
00456059  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0045605E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00456063  48 85 C0                        test rax, rax
00456066  0F 84 39 02 00 00               je 0x1404562a5
0045606C  44 8B 48 58                     mov r9d, dword ptr [rax + 0x58]
00456070  44 8B 05 DD FB AA 00            mov r8d, dword ptr [rip + 0xaafbdd]
00456077  41 8B C8                        mov ecx, r8d
0045607A  48 C1 E1 06                     shl rcx, 6
0045607E  48 8B 15 D3 FB AA 00            mov rdx, qword ptr [rip + 0xaafbd3]
00456085  4C 89 54 11 08                  mov qword ptr [rcx + rdx + 8], r10
0045608A  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00456092  48 89 44 11 10                  mov qword ptr [rcx + rdx + 0x10], rax
00456097  41 F6 C6 01                     test r14b, 1
0045609B  0F 84 D6 01 00 00               je 0x140456277
004560A1  4D 85 E4                        test r12, r12
004560A4  0F 84 A9 01 00 00               je 0x140456253
004560AA  49 8B 04 24                     mov rax, qword ptr [r12]
004560AE  E9 A3 01 00 00                  jmp 0x140456256
004560B3  41 F6 C6 02                     test r14b, 2
004560B7  74 0B                           je 0x1404560c4
004560B9  48 39 7C 08 10                  cmp qword ptr [rax + rcx + 0x10], rdi
004560BE  0F 85 E1 01 00 00               jne 0x1404562a5
004560C4  41 F6 C6 01                     test r14b, 1
004560C8  0F 84 9F FE FF FF               je 0x140455f6d
004560CE  48 39 7C 08 20                  cmp qword ptr [rax + rcx + 0x20], rdi
004560D3  0F 84 94 FE FF FF               je 0x140455f6d
004560D9  66 45 85 ED                     test r13w, r13w
004560DD  0F 84 8A FE FF FF               je 0x140455f6d
004560E3  66 44 39 2C 08                  cmp word ptr [rax + rcx], r13w
004560E8  0F 85 7F FE FF FF               jne 0x140455f6d
004560EE  49 8B 0C 24                     mov rcx, qword ptr [r12]
004560F2  48 83 F9 FF                     cmp rcx, -1
004560F6  74 12                           je 0x14045610a
004560F8  E8 63 9D 60 00                  call 0x140a5fe60
004560FD  4D 85 FF                        test r15, r15
00456100  74 08                           je 0x14045610a
00456102  49 8B 0F                        mov rcx, qword ptr [r15]
00456105  E8 A6 71 25 00                  call 0x1406ad2b0
0045610A  8B CB                           mov ecx, ebx
0045610C  48 C1 E1 06                     shl rcx, 6
00456110  48 8B 15 41 FB AA 00            mov rdx, qword ptr [rip + 0xaafb41]
00456117  48 8B 44 11 20                  mov rax, qword ptr [rcx + rdx + 0x20]
0045611C  49 89 04 24                     mov qword ptr [r12], rax
00456120  4D 85 FF                        test r15, r15
00456123  0F 84 7C 01 00 00               je 0x1404562a5
00456129  48 8B 44 11 28                  mov rax, qword ptr [rcx + rdx + 0x28]
0045612E  49 89 07                        mov qword ptr [r15], rax
00456131  E9 6F 01 00 00                  jmp 0x1404562a5
00456136  8B 0D 14 FB AA 00               mov ecx, dword ptr [rip + 0xaafb14]
0045613C  3B C1                           cmp eax, ecx
0045613E  0F 82 79 FE FF FF               jb 0x140455fbd
00456144  8D 51 20                        lea edx, [rcx + 0x20]
00456147  48 C1 E2 06                     shl rdx, 6
0045614B  B9 00 01 00 00                  mov ecx, 0x100
00456150  41 B8 72 74 50 69               mov r8d, 0x69507472
00456156  E8 95 BF 72 00                  call 0x140b820f0
0045615B  48 8B F0                        mov rsi, rax
0045615E  48 85 C0                        test rax, rax
00456161  0F 84 3E 01 00 00               je 0x1404562a5
00456167  44 8B 05 E2 FA AA 00            mov r8d, dword ptr [rip + 0xaafae2]
0045616E  49 C1 E0 06                     shl r8, 6
00456172  48 8B 15 DF FA AA 00            mov rdx, qword ptr [rip + 0xaafadf]
00456179  48 8B C8                        mov rcx, rax
0045617C  E8 BF 06 27 00                  call 0x1406c6840
00456181  33 D2                           xor edx, edx
00456183  48 8B 0D CE FA AA 00            mov rcx, qword ptr [rip + 0xaaface]
0045618A  E8 E1 C6 72 00                  call 0x140b82870
0045618F  48 89 35 C2 FA AA 00            mov qword ptr [rip + 0xaafac2], rsi
00456196  8B 05 B4 FA AA 00               mov eax, dword ptr [rip + 0xaafab4]
0045619C  83 C0 20                        add eax, 0x20
0045619F  89 05 AB FA AA 00               mov dword ptr [rip + 0xaafaab], eax
004561A5  E9 13 FE FF FF                  jmp 0x140455fbd
004561AA  41 F6 C6 02                     test r14b, 2
004561AE  74 24                           je 0x1404561d4
004561B0  48 39 7C 31 10                  cmp qword ptr [rcx + rsi + 0x10], rdi
004561B5  75 1D                           jne 0x1404561d4
004561B7  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004561BF  48 89 44 31 10                  mov qword ptr [rcx + rsi + 0x10], rax
004561C4  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
004561CB  89 44 31 38                     mov dword ptr [rcx + rsi + 0x38], eax
004561CF  E9 D1 00 00 00                  jmp 0x1404562a5
004561D4  41 F6 C6 01                     test r14b, 1
004561D8  0F 84 05 FE FF FF               je 0x140455fe3
004561DE  48 39 7C 31 20                  cmp qword ptr [rcx + rsi + 0x20], rdi
004561E3  0F 85 FA FD FF FF               jne 0x140455fe3
004561E9  0F B7 04 31                     movzx eax, word ptr [rcx + rsi]
004561ED  66 41 3B C5                     cmp ax, r13w
004561F1  74 09                           je 0x1404561fc
004561F3  66 85 C0                        test ax, ax
004561F6  0F 85 E7 FD FF FF               jne 0x140455fe3
004561FC  49 8B 04 24                     mov rax, qword ptr [r12]
00456200  48 89 44 31 20                  mov qword ptr [rcx + rsi + 0x20], rax
00456205  4D 85 FF                        test r15, r15
00456208  74 03                           je 0x14045620d
0045620A  49 8B 3F                        mov rdi, qword ptr [r15]
0045620D  8B C2                           mov eax, edx
0045620F  48 C1 E0 06                     shl rax, 6
00456213  48 89 7C 30 28                  mov qword ptr [rax + rsi + 0x28], rdi
00456218  8B C2                           mov eax, edx
0045621A  48 C1 E0 06                     shl rax, 6
0045621E  66 44 89 2C 30                  mov word ptr [rax + rsi], r13w
00456223  8B CA                           mov ecx, edx
00456225  48 C1 E1 06                     shl rcx, 6
00456229  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00456230  89 44 31 38                     mov dword ptr [rcx + rsi + 0x38], eax
00456234  8B CA                           mov ecx, edx
00456236  48 C1 E1 06                     shl rcx, 6
0045623A  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00456242  48 89 44 31 30                  mov qword ptr [rcx + rsi + 0x30], rax
00456247  EB 5C                           jmp 0x1404562a5
00456249  BA 0D 00 00 C0                  mov edx, 0xc000000d
0045624E  E9 FB FD FF FF                  jmp 0x14045604e
00456253  48 8B C7                        mov rax, rdi
00456256  48 89 44 11 20                  mov qword ptr [rcx + rdx + 0x20], rax
0045625B  4D 85 FF                        test r15, r15
0045625E  74 03                           je 0x140456263
00456260  49 8B 3F                        mov rdi, qword ptr [r15]
00456263  48 89 7C 11 28                  mov qword ptr [rcx + rdx + 0x28], rdi
00456268  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00456270  48 89 44 11 30                  mov qword ptr [rcx + rdx + 0x30], rax
00456275  EB 0F                           jmp 0x140456286
00456277  48 89 7C 11 20                  mov qword ptr [rcx + rdx + 0x20], rdi
0045627C  48 89 7C 11 28                  mov qword ptr [rcx + rdx + 0x28], rdi
00456281  48 89 7C 11 30                  mov qword ptr [rcx + rdx + 0x30], rdi
00456286  66 44 89 2C 11                  mov word ptr [rcx + rdx], r13w
0045628B  44 89 4C 11 18                  mov dword ptr [rcx + rdx + 0x18], r9d
00456290  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00456297  89 44 11 38                     mov dword ptr [rcx + rdx + 0x38], eax
0045629B  41 FF C0                        inc r8d
0045629E  44 89 05 AF F9 AA 00            mov dword ptr [rip + 0xaaf9af], r8d
004562A5  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
004562AA  BA 01 00 00 00                  mov edx, 1
004562AF  44 8D 42 03                     lea r8d, [rdx + 3]
004562B3  48 8D 0D A6 F9 AA 00            lea rcx, [rip + 0xaaf9a6]
004562BA  E8 91 05 F4 FF                  call 0x140396850
004562BF  B0 01                           mov al, 1
004562C1  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
004562C6  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
004562CA  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
004562CE  49 8B E3                        mov rsp, r11
004562D1  41 5F                           pop r15
004562D3  41 5E                           pop r14
004562D5  41 5D                           pop r13
004562D7  41 5C                           pop r12
004562D9  5F                              pop rdi
004562DA  C3                              ret
004562DB  CC                              int3
004562DC  32 C0                           xor al, al
004562DE  EB E1                           jmp 0x1404562c1
004562E0  4D 85 E4                        test r12, r12
004562E3  74 F7                           je 0x1404562dc
004562E5  E9 33 FC FF FF                  jmp 0x140455f1d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrpSetAlternateResourceModuleHandle(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int16 a5, unsigned int a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (64);
    v_rdi = 0;
    if (a1 == 0) goto loc_004562DC;
    if ((((unsigned int)((unsigned int)(a6))) & (0xFFFFFFCCULL)) != 0) goto loc_004562DC;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_004562DC;
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) != 0) goto loc_004562E0;
loc_00455F1D:
    result = LdrpInitMuiCrits(a1, a2, a3, a4);
    v_stack_m48 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 11205930, a2, a3, a4);
loc_00455F47:
    v_stack_m38 = 0;
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11205891))))) goto loc_00455F71;
    result = (0) << (6);
    if ((*(unsigned __int64 *)(result + *(unsigned __int64 *)(v_rip + 11205878) * 1 + 8)) == a1) goto loc_004560B3;
loc_00455F6D:
    v_rbx = (unsigned int)((0) + 1);
    goto loc_00455F47;
loc_00455F71:
    if ((((unsigned __int8)((unsigned int)(a6))) & (16)) != 0) goto loc_004562A5;
    if (*(unsigned __int64 *)(v_rip + 11205846) != 0) goto loc_00456136;
    result = ExAllocatePool2(256, (unsigned int)(0x800ULL), (unsigned int)(0x69507472ULL), a4);
    if (result == 0) goto loc_004562A5;
    *(unsigned __int64 *)(v_rip + 11205797) = result;
    *(unsigned int *)(v_rip + 11205779) = 32;
loc_00455FBD:
    v_stack_m38 = 0;
loc_00455FC8:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11205766))))) goto loc_00455FEB;
    a1 = (0) << (6);
    if ((*(unsigned __int64 *)(a1 + result * 1 + 8)) == v_stack_p8) goto loc_004561AA;
loc_00455FE3:
    a2 = (unsigned int)((0) + 1);
    v_stack_m38 = (unsigned int)(a2);
    goto loc_00455FC8;
loc_00455FEB:
    a2 = (v_stack_p8) & (-4);
    v_stack_p8 = 0;
    v_stack_m30 = 0;
    v_stack_p8 = 0;
    if (condition_is_equal) goto loc_00456249;
    if ((*(unsigned __int16 *)(a2)) != ((unsigned __int16)((unsigned int)(0x5A4DULL)))) goto loc_0045605E;
    a1 = ((unsigned int)(*(unsigned int *)(a2 + 60))) + (a2);
    v_stack_m30 = a1;
    if (a1 < a2) goto loc_0045605E;
    if (a2 > ((unsigned int)(0x69507472ULL))) goto loc_00456044;
    if ((a1 + 263) < a1) goto loc_0045605E;
    if ((a1 + 263) > ((unsigned int)(0x69507472ULL))) goto loc_0045605E;
loc_00456044:
    if ((*(unsigned int *)(a1)) != 0x4550ULL) goto loc_0045605E;
loc_0045604E:
    result = v_stack_p8;
    if (!sign_flag) { result = a1; }
    v_stack_p8 = result;
loc_0045605E:
    if (v_stack_p8 == 0) goto loc_004562A5;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11205597))))) << (6);
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11205587) * 1 + 8) = v_stack_p8;
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11205587) * 1 + 16) = v_stack_p20;
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) == 0) goto loc_00456277;
    if (a2 == 0) goto loc_00456253;
    goto loc_00456256;
loc_004560B3:
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) == 0) goto loc_004560C4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + a1 * 1 + 16)) != 0) goto loc_004562A5;
loc_004560C4:
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) == 0) goto loc_00455F6D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + a1 * 1 + 32)) == 0) goto loc_00455F6D;
    if (a5 == 0) goto loc_00455F6D;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2) + a1 * 1)) != a5) goto loc_00455F6D;
    if ((*(unsigned __int64 *)(a2)) == -1) goto loc_0045610A;
    result = MmUnmapViewInSessionSpace(*(unsigned __int64 *)(a2), *(unsigned __int64 *)(v_rip + 11205587), (unsigned int)(*(unsigned int *)(v_rip + 11205597)), (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    if (0 != 0) {
        a1 = *(unsigned __int64 *)(a3);
        result = ZwClose(a1, *(unsigned __int64 *)(v_rip + 11205587), (unsigned int)(*(unsigned int *)(v_rip + 11205597)), (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    }
    a1 = ((unsigned int)((unsigned int)(v_rbx))) << (6);
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11205441) * 1 + 32);
    if (0 == 0) goto loc_004562A5;
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11205441) * 1 + 40);
    goto loc_004562A5;
loc_00456136:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 11205441) * 1 + 40))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11205396))))) goto loc_00455FBD;
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 11205396)) + 32) << (6);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x69507472ULL), (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    if (result == 0) goto loc_004562A5;
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 11205346))) << (6);
    result = memcpy(result, *(unsigned __int64 *)(v_rip + 11205343), a3, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 11205326), a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    *(unsigned __int64 *)(v_rip + 11205314) = result;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11205300))) + (32));
    *(unsigned int *)(v_rip + 11205291) = (unsigned int)(result);
    goto loc_00455FBD;
loc_004561AA:
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) == 0) goto loc_004561D4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1 + 16)) != 0) goto loc_004561D4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1 + 16) = v_stack_p20;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1 + 56) = (unsigned int)((unsigned int)(a7));
    goto loc_004562A5;
loc_004561D4:
    if ((((unsigned __int8)((unsigned int)(a6))) & (1)) == 0) goto loc_00455FE3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1 + 32)) != 0) goto loc_00455FE3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1))) == a5) goto loc_004561FC;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1)) != 0) goto loc_00455FE3;
loc_004561FC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11205326) + result * 1 + 32) = *(unsigned __int64 *)(a2);
    if (a3 != 0) {
        v_rdi = *(unsigned __int64 *)(a3);
    }
    result = (0) << (6);
    *(unsigned __int64 *)(result + result * 1 + 40) = v_rdi;
    result = (0) << (6);
    *(unsigned __int16 *)(result + result * 1) = a5;
    a1 = (0) << (6);
    *(unsigned int *)(a1 + result * 1 + 56) = (unsigned int)((unsigned int)(a7));
    a1 = (0) << (6);
    *(unsigned __int64 *)(a1 + result * 1 + 48) = a8;
    goto loc_004562A5;
loc_00456249:
    goto loc_0045604E;
loc_00456253:
loc_00456256:
    *(unsigned __int64 *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 32) = v_rdi;
    if (a3 != 0) {
        v_rdi = *(unsigned __int64 *)(a3);
    }
    *(unsigned __int64 *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 40) = v_rdi;
    *(unsigned __int64 *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 48) = a8;
    goto loc_00456286;
loc_00456277:
    *(unsigned __int64 *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 32) = v_rdi;
    *(unsigned __int64 *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 40) = v_rdi;
    *(unsigned __int64 *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 48) = v_rdi;
loc_00456286:
    *(unsigned __int16 *)(a1 + (unsigned int)(0xC000000DULL) * 1) = a5;
    *(unsigned int *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    *(unsigned int *)(a1 + (unsigned int)(0xC000000DULL) * 1 + 56) = (unsigned int)((unsigned int)(a7));
    a3 = (unsigned int)((a3) + 1);
    *(unsigned int *)(v_rip + 11205039) = (unsigned int)(a3);
loc_004562A5:
    result = KeReleaseMutantEx(v_rip + 11205030, 1, 1 + 3, v_stack_p8);
loc_004562C1:
    return 1;
loc_004562DC:
    result = 0;
    goto loc_004562C1;
loc_004562E0:
    if (0 == 0) goto loc_004562DC;
    goto loc_00455F1D;
}
```

## 5. (Beta) C Style

```c
int64_t LdrpSetAlternateResourceModuleHandle(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint16_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (64);
    local_rdi = 0;
    if (Arg1 == 0) goto loc_004562DC;
    if ((((uint32_t)((uint32_t)(Arg6))) & (0xFFFFFFCCULL)) != 0) goto loc_004562DC;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (3));
    if (((uint8_t)(result)) == 3) goto loc_004562DC;
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) != 0) goto loc_004562E0;
loc_00455F1D:
    result = LdrpInitMuiCrits(Arg1, Arg2, Arg3, Arg4);
    v_stack_m48 = 0;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 11205930, Arg2, Arg3, Arg4);
loc_00455F47:
    v_stack_m38 = 0;
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAAFD03))))) goto loc_00455F71;
    result = (0) << (6);
    if ((*(uint64_t *)(result + *(uint64_t *)(v_rip + 0xAAFCF6) * 1 + 0x8)) == Arg1) goto loc_004560B3;
loc_00455F6D:
    local_rbx = (uint32_t)((0) + 1);
    goto loc_00455F47;
loc_00455F71:
    if ((((uint8_t)((uint32_t)(Arg6))) & (16)) != 0) goto loc_004562A5;
    if (*(uint64_t *)(v_rip + 0xAAFCD6) != 0) goto loc_00456136;
    result = ExAllocatePool2(256, (uint32_t)(0x800ULL), (uint32_t)(0x69507472ULL), Arg4);
    if (result == 0) goto loc_004562A5;
    *(uint64_t *)(v_rip + 0xAAFCA5) = result;
    *(uint32_t *)(v_rip + 0xAAFC93) = 32;
loc_00455FBD:
    v_stack_m38 = 0;
loc_00455FC8:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAAFC86))))) goto loc_00455FEB;
    Arg1 = (0) << (6);
    if ((*(uint64_t *)(Arg1 + result * 1 + 0x8)) == v_stack_p8) goto loc_004561AA;
loc_00455FE3:
    Arg2 = (uint32_t)((0) + 1);
    v_stack_m38 = (uint32_t)(Arg2);
    goto loc_00455FC8;
loc_00455FEB:
    Arg2 = (v_stack_p8) & (-4);
    v_stack_p8 = 0;
    v_stack_m30 = 0;
    v_stack_p8 = 0;
    if (condition_is_equal) goto loc_00456249;
    if ((*(uint16_t *)(Arg2)) != ((uint16_t)((uint32_t)(0x5A4DULL)))) goto loc_0045605E;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg2 + 0x3C))) + (Arg2);
    v_stack_m30 = Arg1;
    if (Arg1 < Arg2) goto loc_0045605E;
    if (Arg2 > ((uint32_t)(0x69507472ULL))) goto loc_00456044;
    if ((Arg1 + 263) < Arg1) goto loc_0045605E;
    if ((Arg1 + 263) > ((uint32_t)(0x69507472ULL))) goto loc_0045605E;
loc_00456044:
    if ((*(uint32_t *)(Arg1)) != 0x4550ULL) goto loc_0045605E;
loc_0045604E:
    result = v_stack_p8;
    if (!sign_flag) { result = Arg1; }
    v_stack_p8 = result;
loc_0045605E:
    if (v_stack_p8 == 0) goto loc_004562A5;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAAFBDD))))) << (6);
    *(uint64_t *)(Arg1 + *(uint64_t *)(v_rip + 0xAAFBD3) * 1 + 0x8) = v_stack_p8;
    *(uint64_t *)(Arg1 + *(uint64_t *)(v_rip + 0xAAFBD3) * 1 + 0x10) = v_stack_p20;
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) == 0) goto loc_00456277;
    if (Arg2 == 0) goto loc_00456253;
    goto loc_00456256;
loc_004560B3:
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) == 0) goto loc_004560C4;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2) + Arg1 * 1 + 0x10)) != 0) goto loc_004562A5;
loc_004560C4:
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) == 0) goto loc_00455F6D;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2) + Arg1 * 1 + 0x20)) == 0) goto loc_00455F6D;
    if (Arg5 == 0) goto loc_00455F6D;
    if ((*(uint16_t *)(*(uint64_t *)(Arg2) + Arg1 * 1)) != Arg5) goto loc_00455F6D;
    if ((*(uint64_t *)(Arg2)) == -1) goto loc_0045610A;
    result = MmUnmapViewInSessionSpace(*(uint64_t *)(Arg2), *(uint64_t *)(v_rip + 0xAAFBD3), (uint32_t)(*(uint32_t *)(v_rip + 0xAAFBDD)), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    if (0 != 0) {
        Arg1 = *(uint64_t *)(Arg3);
        result = ZwClose(Arg1, *(uint64_t *)(v_rip + 0xAAFBD3), (uint32_t)(*(uint32_t *)(v_rip + 0xAAFBDD)), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    }
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) << (6);
    *(uint64_t *)(Arg2) = *(uint64_t *)(Arg1 + *(uint64_t *)(v_rip + 0xAAFB41) * 1 + 0x20);
    if (0 == 0) goto loc_004562A5;
    *(uint64_t *)(Arg3) = *(uint64_t *)(Arg1 + *(uint64_t *)(v_rip + 0xAAFB41) * 1 + 0x28);
    goto loc_004562A5;
loc_00456136:
    if (((uint32_t)(*(uint64_t *)(Arg1 + *(uint64_t *)(v_rip + 0xAAFB41) * 1 + 0x28))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAAFB14))))) goto loc_00455FBD;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xAAFB14)) + 32) << (6);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x69507472ULL), (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    if (result == 0) goto loc_004562A5;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xAAFAE2))) << (6);
    result = memcpy(result, *(uint64_t *)(v_rip + 0xAAFADF), Arg3, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0xAAFACE), Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    *(uint64_t *)(v_rip + 0xAAFAC2) = result;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAAFAB4))) + (32));
    *(uint32_t *)(v_rip + 0xAAFAAB) = (uint32_t)(result);
    goto loc_00455FBD;
loc_004561AA:
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) == 0) goto loc_004561D4;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1 + 0x10)) != 0) goto loc_004561D4;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1 + 0x10) = v_stack_p20;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1 + 0x38) = (uint32_t)((uint32_t)(Arg7));
    goto loc_004562A5;
loc_004561D4:
    if ((((uint8_t)((uint32_t)(Arg6))) & (1)) == 0) goto loc_00455FE3;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1 + 0x20)) != 0) goto loc_00455FE3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1))) == Arg5) goto loc_004561FC;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1)) != 0) goto loc_00455FE3;
loc_004561FC:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xAAFACE) + result * 1 + 0x20) = *(uint64_t *)(Arg2);
    if (Arg3 != 0) {
        local_rdi = *(uint64_t *)(Arg3);
    }
    result = (0) << (6);
    *(uint64_t *)(result + result * 1 + 0x28) = local_rdi;
    result = (0) << (6);
    *(uint16_t *)(result + result * 1) = Arg5;
    Arg1 = (0) << (6);
    *(uint32_t *)(Arg1 + result * 1 + 0x38) = (uint32_t)((uint32_t)(Arg7));
    Arg1 = (0) << (6);
    *(uint64_t *)(Arg1 + result * 1 + 0x30) = Arg8;
    goto loc_004562A5;
loc_00456249:
    goto loc_0045604E;
loc_00456253:
loc_00456256:
    *(uint64_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x20) = local_rdi;
    if (Arg3 != 0) {
        local_rdi = *(uint64_t *)(Arg3);
    }
    *(uint64_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x28) = local_rdi;
    *(uint64_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x30) = Arg8;
    goto loc_00456286;
loc_00456277:
    *(uint64_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x20) = local_rdi;
    *(uint64_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x28) = local_rdi;
    *(uint64_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x30) = local_rdi;
loc_00456286:
    *(uint16_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1) = Arg5;
    *(uint32_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    *(uint32_t *)(Arg1 + (uint32_t)(0xC000000DULL) * 1 + 0x38) = (uint32_t)((uint32_t)(Arg7));
    Arg3 = (uint32_t)((Arg3) + 1);
    *(uint32_t *)(v_rip + 0xAAF9AF) = (uint32_t)(Arg3);
loc_004562A5:
    result = KeReleaseMutantEx(v_rip + 11205030, 1, 1 + 3, v_stack_p8);
loc_004562C1:
    return 1;
loc_004562DC:
    result = 0;
    goto loc_004562C1;
loc_004562E0:
    if (0 == 0) goto loc_004562DC;
    goto loc_00455F1D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00455EBC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
