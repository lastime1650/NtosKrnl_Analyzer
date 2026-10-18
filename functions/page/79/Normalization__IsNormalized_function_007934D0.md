# Normalization__IsNormalized

- RVA: `0x007934D0`–`0x007939A6` (길이 `1,238` bytes)
- VA: `0x00000001407934D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFE50`
- 디코드: `347`개 명령, `1,238/1,238` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007935E3` → [CanComposeHangul](../../text/5E/CanComposeHangul_function_005ED6B4.md) (function, `0x005ED6B4`)
- `0x00793673` → [CanComposeHangul](../../text/5E/CanComposeHangul_function_005ED6B4.md) (function, `0x005ED6B4`)
- `0x00793720` → [Normalization__GetLastChar](Normalization__GetLastChar_function_0079321C.md) (function, `0x0079321C`)
- `0x00793795` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x007937E0` → [Normalization__CanCombineWithStartFirstPair](Normalization__CanCombineWithStartFirstPair_function_007930E4.md) (function, `0x007930E4`)
- `0x00793817` → [Normalization__CanCombineWithStartBase](Normalization__CanCombineWithStartBase_function_00793098.md) (function, `0x00793098`)
- `0x00793840` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x00793879` → [Normalization__CanCombineWithStartFirstPair](Normalization__CanCombineWithStartFirstPair_function_007930E4.md) (function, `0x007930E4`)
- `0x00793899` → [Normalization__CanCombineWithStartBase](Normalization__CanCombineWithStartBase_function_00793098.md) (function, `0x00793098`)
- `0x007938DE` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)
- `0x00793919` → [Normalization__GetLastChar](Normalization__GetLastChar_function_0079321C.md) (function, `0x0079321C`)
- `0x00793931` → [Normalization__CanCombinableCharactersCombine](Normalization__CanCombinableCharactersCombine_function_00792F2C.md) (function, `0x00792F2C`)

### Direct callers
- [RtlIsNormalizedString](RtlIsNormalizedString_function_007945B0.md) at `0x00794616`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007935E3` → [CanComposeHangul](../../text/5E/CanComposeHangul_function_005ED6B4.md) (`PAGE` → `.text`)
  - `0x00793673` → [CanComposeHangul](../../text/5E/CanComposeHangul_function_005ED6B4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007934D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007934D5  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
007934DA  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
007934DF  55                              push rbp
007934E0  56                              push rsi
007934E1  57                              push rdi
007934E2  41 54                           push r12
007934E4  41 55                           push r13
007934E6  41 56                           push r14
007934E8  41 57                           push r15
007934EA  48 8B EC                        mov rbp, rsp
007934ED  48 83 EC 50                     sub rsp, 0x50
007934F1  33 C0                           xor eax, eax
007934F3  45 8B F8                        mov r15d, r8d
007934F6  4C 8B E2                        mov r12, rdx
007934F9  48 8B F9                        mov rdi, rcx
007934FC  48 85 D2                        test rdx, rdx
007934FF  75 0A                           jne 0x14079350b
00793501  B8 0D 00 00 C0                  mov eax, 0xc000000d
00793506  E9 7B 04 00 00                  jmp 0x140793986
0079350B  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
0079350E  88 45 E0                        mov byte ptr [rbp - 0x20], al
00793511  88 45 48                        mov byte ptr [rbp + 0x48], al
00793514  48 8D 42 FE                     lea rax, [rdx - 2]
00793518  33 D2                           xor edx, edx
0079351A  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0079351E  21 55 E8                        and dword ptr [rbp - 0x18], edx
00793521  21 55 F0                        and dword ptr [rbp - 0x10], edx
00793524  40 32 F6                        xor sil, sil
00793527  89 55 EC                        mov dword ptr [rbp - 0x14], edx
0079352A  40 88 75 E2                     mov byte ptr [rbp - 0x1e], sil
0079352E  88 55 E1                        mov byte ptr [rbp - 0x1f], dl
00793531  45 85 FF                        test r15d, r15d
00793534  0F 8E 43 04 00 00               jle 0x14079397d
0079353A  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
0079353F  3B 5F 1C                        cmp ebx, dword ptr [rdi + 0x1c]
00793542  0F 8C 1B 04 00 00               jl 0x140793963
00793548  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0079354C  8B CB                           mov ecx, ebx
0079354E  48 C1 E9 07                     shr rcx, 7
00793552  8A 14 01                        mov dl, byte ptr [rcx + rax]
00793555  84 D2                           test dl, dl
00793557  0F 84 06 04 00 00               je 0x140793963
0079355D  80 FA FB                        cmp dl, 0xfb
00793560  75 0A                           jne 0x14079356c
00793562  80 7F 71 00                     cmp byte ptr [rdi + 0x71], 0
00793566  0F 85 F7 03 00 00               jne 0x140793963
0079356C  44 0F B6 C2                     movzx r8d, dl
00793570  41 8B C8                        mov ecx, r8d
00793573  84 D2                           test dl, dl
00793575  0F 84 D9 03 00 00               je 0x140793954
0079357B  81 E9 FB 00 00 00               sub ecx, 0xfb
00793581  0F 84 C7 03 00 00               je 0x14079394e
00793587  83 E9 01                        sub ecx, 1
0079358A  0F 84 0F 04 00 00               je 0x14079399f
00793590  83 E9 01                        sub ecx, 1
00793593  0F 84 E7 00 00 00               je 0x140793680
00793599  83 E9 01                        sub ecx, 1
0079359C  74 70                           je 0x14079360e
0079359E  83 F9 01                        cmp ecx, 1
007935A1  0F 85 E5 00 00 00               jne 0x14079368c
007935A7  81 FB 00 AC 00 00               cmp ebx, 0xac00
007935AD  7C 26                           jl 0x1407935d5
007935AF  81 FB A4 D7 00 00               cmp ebx, 0xd7a4
007935B5  0F 8C A0 00 00 00               jl 0x14079365b
007935BB  8D 83 50 28 FF FF               lea eax, [rbx - 0xd7b0]
007935C1  83 F8 16                        cmp eax, 0x16
007935C4  76 41                           jbe 0x140793607
007935C6  8D 83 35 28 FF FF               lea eax, [rbx - 0xd7cb]
007935CC  83 F8 30                        cmp eax, 0x30
007935CF  76 36                           jbe 0x140793607
007935D1  B2 FB                           mov dl, 0xfb
007935D3  EB 97                           jmp 0x14079356c
007935D5  41 83 FF 01                     cmp r15d, 1
007935D9  7E 15                           jle 0x1407935f0
007935DB  41 0F B7 54 24 02               movzx edx, word ptr [r12 + 2]
007935E1  8B CB                           mov ecx, ebx
007935E3  E8 CC A0 E5 FF                  call 0x1405ed6b4
007935E8  84 C0                           test al, al
007935EA  0F 85 90 00 00 00               jne 0x140793680
007935F0  8B 07                           mov eax, dword ptr [rdi]
007935F2  83 E8 0D                        sub eax, 0xd
007935F5  A9 FF FE FF FF                  test eax, 0xfffffeff
007935FA  75 0B                           jne 0x140793607
007935FC  8D 83 A1 EE FF FF               lea eax, [rbx - 0x115f]
00793602  83 F8 01                        cmp eax, 1
00793605  76 CA                           jbe 0x1407935d1
00793607  32 D2                           xor dl, dl
00793609  E9 5E FF FF FF                  jmp 0x14079356c
0079360E  41 83 FF 01                     cmp r15d, 1
00793612  0F 8E 87 03 00 00               jle 0x14079399f
00793618  49 83 C4 02                     add r12, 2
0079361C  41 FF CF                        dec r15d
0079361F  B8 00 24 00 00                  mov eax, 0x2400
00793624  44 89 7D 50                     mov dword ptr [rbp + 0x50], r15d
00793628  BA FF 03 00 00                  mov edx, 0x3ff
0079362D  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00793632  03 C1                           add eax, ecx
00793634  66 3B C2                        cmp ax, dx
00793637  0F 87 62 03 00 00               ja 0x14079399f
0079363D  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00793641  81 C3 09 28 FF FF               add ebx, 0xffff2809
00793647  C1 E3 0A                        shl ebx, 0xa
0079364A  03 D9                           add ebx, ecx
0079364C  48 63 CB                        movsxd rcx, ebx
0079364F  48 C1 F9 07                     sar rcx, 7
00793653  8A 14 01                        mov dl, byte ptr [rcx + rax]
00793656  E9 11 FF FF FF                  jmp 0x14079356c
0079365B  80 7F 70 01                     cmp byte ptr [rdi + 0x70], 1
0079365F  74 1F                           je 0x140793680
00793661  41 83 FF 01                     cmp r15d, 1
00793665  0F 8E E9 02 00 00               jle 0x140793954
0079366B  41 0F B7 54 24 02               movzx edx, word ptr [r12 + 2]
00793671  8B CB                           mov ecx, ebx
00793673  E8 3C A0 E5 FF                  call 0x1405ed6b4
00793678  84 C0                           test al, al
0079367A  0F 84 D4 02 00 00               je 0x140793954
00793680  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00793684  C6 00 00                        mov byte ptr [rax], 0
00793687  E9 F8 02 00 00                  jmp 0x140793984
0079368C  8B C3                           mov eax, ebx
0079368E  49 8B C8                        mov rcx, r8
00793691  83 E0 7F                        and eax, 0x7f
00793694  48 C1 E1 07                     shl rcx, 7
00793698  48 03 C8                        add rcx, rax
0079369B  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0079369F  0F B6 54 01 80                  movzx edx, byte ptr [rcx + rax - 0x80]
007936A4  84 D2                           test dl, dl
007936A6  0F 84 A8 02 00 00               je 0x140793954
007936AC  44 8A EA                        mov r13b, dl
007936AF  44 8A F2                        mov r14b, dl
007936B2  41 80 E5 C0                     and r13b, 0xc0
007936B6  41 80 E6 3F                     and r14b, 0x3f
007936BA  74 06                           je 0x1407936c2
007936BC  41 80 FE 3F                     cmp r14b, 0x3f
007936C0  75 34                           jne 0x1407936f6
007936C2  8B CA                           mov ecx, edx
007936C4  83 E9 40                        sub ecx, 0x40
007936C7  0F 84 71 02 00 00               je 0x14079393e
007936CD  83 E9 3F                        sub ecx, 0x3f
007936D0  0F 84 78 02 00 00               je 0x14079394e
007936D6  83 E9 01                        sub ecx, 1
007936D9  0F 84 5F 02 00 00               je 0x14079393e
007936DF  83 E9 3F                        sub ecx, 0x3f
007936E2  74 9C                           je 0x140793680
007936E4  83 E9 01                        sub ecx, 1
007936E7  0F 84 0C 02 00 00               je 0x1407938f9
007936ED  83 F9 3F                        cmp ecx, 0x3f
007936F0  0F 84 7D 02 00 00               je 0x140793973
007936F6  41 F6 C5 BF                     test r13b, 0xbf
007936FA  0F 84 F0 01 00 00               je 0x1407938f0
00793700  48 8D 45 48                     lea rax, [rbp + 0x48]
00793704  49 8B D4                        mov rdx, r12
00793707  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0079370C  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
00793710  48 8D 45 E0                     lea rax, [rbp - 0x20]
00793714  48 8B CF                        mov rcx, rdi
00793717  4C 8D 45 F8                     lea r8, [rbp - 8]
0079371B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00793720  E8 F7 FA FF FF                  call 0x14079321c
00793725  40 8A 75 E0                     mov sil, byte ptr [rbp - 0x20]
00793729  40 84 F6                        test sil, sil
0079372C  0F 84 81 01 00 00               je 0x1407938b3
00793732  40 80 FE 3F                     cmp sil, 0x3f
00793736  0F 84 77 01 00 00               je 0x1407938b3
0079373C  44 8A 7D 48                     mov r15b, byte ptr [rbp + 0x48]
00793740  41 F6 C7 BF                     test r15b, 0xbf
00793744  0F 84 D4 00 00 00               je 0x14079381e
0079374A  41 3A F6                        cmp sil, r14b
0079374D  0F 87 2D FF FF FF               ja 0x140793680
00793753  41 80 FD C0                     cmp r13b, 0xc0
00793757  0F 85 90 00 00 00               jne 0x1407937ed
0079375D  41 3A F6                        cmp sil, r14b
00793760  0F 84 87 00 00 00               je 0x1407937ed
00793766  8A 4D E1                        mov cl, byte ptr [rbp - 0x1f]
00793769  40 8A 75 E2                     mov sil, byte ptr [rbp - 0x1e]
0079376D  8A C1                           mov al, cl
0079376F  40 0A C6                        or al, sil
00793772  2C 40                           sub al, 0x40
00793774  A8 BF                           test al, 0xbf
00793776  74 10                           je 0x140793788
00793778  80 F9 40                        cmp cl, 0x40
0079377B  75 2A                           jne 0x1407937a7
0079377D  40 84 F6                        test sil, sil
00793780  74 06                           je 0x140793788
00793782  40 80 FE 3F                     cmp sil, 0x3f
00793786  75 1F                           jne 0x1407937a7
00793788  44 8B 7D EC                     mov r15d, dword ptr [rbp - 0x14]
0079378C  44 8B C3                        mov r8d, ebx
0079378F  41 8B D7                        mov edx, r15d
00793792  48 8B CF                        mov rcx, rdi
00793795  E8 92 F7 FF FF                  call 0x140792f2c
0079379A  85 C0                           test eax, eax
0079379C  0F 85 DE FE FF FF               jne 0x140793680
007937A2  8A 4D E1                        mov cl, byte ptr [rbp - 0x1f]
007937A5  EB 04                           jmp 0x1407937ab
007937A7  44 8B 7D EC                     mov r15d, dword ptr [rbp - 0x14]
007937AB  44 3A F6                        cmp r14b, sil
007937AE  73 3D                           jae 0x1407937ed
007937B0  F6 C1 BF                        test cl, 0xbf
007937B3  75 38                           jne 0x1407937ed
007937B5  8D 46 FF                        lea eax, [rsi - 1]
007937B8  3C 3D                           cmp al, 0x3d
007937BA  77 31                           ja 0x1407937ed
007937BC  40 3A 77 74                     cmp sil, byte ptr [rdi + 0x74]
007937C0  75 3C                           jne 0x1407937fe
007937C2  44 3A 77 72                     cmp r14b, byte ptr [rdi + 0x72]
007937C6  72 42                           jb 0x14079380a
007937C8  44 3A 77 73                     cmp r14b, byte ptr [rdi + 0x73]
007937CC  75 1F                           jne 0x1407937ed
007937CE  45 8B CF                        mov r9d, r15d
007937D1  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
007937D5  4C 8D 45 E8                     lea r8, [rbp - 0x18]
007937D9  48 8B CF                        mov rcx, rdi
007937DC  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007937E0  E8 FF F8 FF FF                  call 0x1407930e4
007937E5  85 C0                           test eax, eax
007937E7  0F 85 93 FE FF FF               jne 0x140793680
007937ED  44 8B 7D 50                     mov r15d, dword ptr [rbp + 0x50]
007937F1  44 88 75 E0                     mov byte ptr [rbp - 0x20], r14b
007937F5  44 88 6D 48                     mov byte ptr [rbp + 0x48], r13b
007937F9  E9 5E 01 00 00                  jmp 0x14079395c
007937FE  40 3A 77 76                     cmp sil, byte ptr [rdi + 0x76]
00793802  75 06                           jne 0x14079380a
00793804  44 3A 77 75                     cmp r14b, byte ptr [rdi + 0x75]
00793808  74 C4                           je 0x1407937ce
0079380A  44 8B CB                        mov r9d, ebx
0079380D  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00793811  45 8B C7                        mov r8d, r15d
00793814  48 8B CF                        mov rcx, rdi
00793817  E8 7C F8 FF FF                  call 0x140793098
0079381C  EB C7                           jmp 0x1407937e5
0079381E  83 65 E8 00                     and dword ptr [rbp - 0x18], 0
00793822  83 65 F0 00                     and dword ptr [rbp - 0x10], 0
00793826  8B 45 E4                        mov eax, dword ptr [rbp - 0x1c]
00793829  89 45 EC                        mov dword ptr [rbp - 0x14], eax
0079382C  41 80 FD C0                     cmp r13b, 0xc0
00793830  75 74                           jne 0x1407938a6
00793832  41 80 FF 40                     cmp r15b, 0x40
00793836  75 18                           jne 0x140793850
00793838  44 8B C3                        mov r8d, ebx
0079383B  8B D0                           mov edx, eax
0079383D  48 8B CF                        mov rcx, rdi
00793840  E8 E7 F6 FF FF                  call 0x140792f2c
00793845  85 C0                           test eax, eax
00793847  0F 85 33 FE FF FF               jne 0x140793680
0079384D  8B 45 EC                        mov eax, dword ptr [rbp - 0x14]
00793850  41 3A F6                        cmp sil, r14b
00793853  76 51                           jbe 0x1407938a6
00793855  40 3A 77 74                     cmp sil, byte ptr [rdi + 0x74]
00793859  75 25                           jne 0x140793880
0079385B  44 3A 77 72                     cmp r14b, byte ptr [rdi + 0x72]
0079385F  72 2B                           jb 0x14079388c
00793861  44 3A 77 73                     cmp r14b, byte ptr [rdi + 0x73]
00793865  75 3F                           jne 0x1407938a6
00793867  44 8B C8                        mov r9d, eax
0079386A  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0079386E  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00793872  48 8B CF                        mov rcx, rdi
00793875  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00793879  E8 66 F8 FF FF                  call 0x1407930e4
0079387E  EB 1E                           jmp 0x14079389e
00793880  40 3A 77 76                     cmp sil, byte ptr [rdi + 0x76]
00793884  75 06                           jne 0x14079388c
00793886  44 3A 77 75                     cmp r14b, byte ptr [rdi + 0x75]
0079388A  74 DB                           je 0x140793867
0079388C  44 8B CB                        mov r9d, ebx
0079388F  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00793893  44 8B C0                        mov r8d, eax
00793896  48 8B CF                        mov rcx, rdi
00793899  E8 FA F7 FF FF                  call 0x140793098
0079389E  85 C0                           test eax, eax
007938A0  0F 85 DA FD FF FF               jne 0x140793680
007938A6  40 88 75 E2                     mov byte ptr [rbp - 0x1e], sil
007938AA  44 88 7D E1                     mov byte ptr [rbp - 0x1f], r15b
007938AE  E9 3A FF FF FF                  jmp 0x1407937ed
007938B3  8A 4D 48                        mov cl, byte ptr [rbp + 0x48]
007938B6  8B 55 E4                        mov edx, dword ptr [rbp - 0x1c]
007938B9  89 55 EC                        mov dword ptr [rbp - 0x14], edx
007938BC  40 88 75 E2                     mov byte ptr [rbp - 0x1e], sil
007938C0  8D 41 C0                        lea eax, [rcx - 0x40]
007938C3  88 4D E1                        mov byte ptr [rbp - 0x1f], cl
007938C6  A8 BF                           test al, 0xbf
007938C8  0F 85 23 FF FF FF               jne 0x1407937f1
007938CE  41 80 FD C0                     cmp r13b, 0xc0
007938D2  0F 85 19 FF FF FF               jne 0x1407937f1
007938D8  44 8B C3                        mov r8d, ebx
007938DB  48 8B CF                        mov rcx, rdi
007938DE  E8 49 F6 FF FF                  call 0x140792f2c
007938E3  85 C0                           test eax, eax
007938E5  0F 85 95 FD FF FF               jne 0x140793680
007938EB  E9 01 FF FF FF                  jmp 0x1407937f1
007938F0  C7 45 E8 00 00 00 00            mov dword ptr [rbp - 0x18], 0
007938F7  EB 45                           jmp 0x14079393e
007938F9  48 8D 45 48                     lea rax, [rbp + 0x48]
007938FD  49 8B D4                        mov rdx, r12
00793900  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00793905  4C 8D 4D E4                     lea r9, [rbp - 0x1c]
00793909  48 8D 45 E0                     lea rax, [rbp - 0x20]
0079390D  48 8B CF                        mov rcx, rdi
00793910  4C 8D 45 F8                     lea r8, [rbp - 8]
00793914  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00793919  E8 FE F8 FF FF                  call 0x14079321c
0079391E  8A 45 48                        mov al, byte ptr [rbp + 0x48]
00793921  0A 45 E0                        or al, byte ptr [rbp - 0x20]
00793924  3C 80                           cmp al, 0x80
00793926  75 16                           jne 0x14079393e
00793928  8B 55 E4                        mov edx, dword ptr [rbp - 0x1c]
0079392B  44 8B C3                        mov r8d, ebx
0079392E  48 8B CF                        mov rcx, rdi
00793931  E8 F6 F5 FF FF                  call 0x140792f2c
00793936  85 C0                           test eax, eax
00793938  0F 85 42 FD FF FF               jne 0x140793680
0079393E  89 5D EC                        mov dword ptr [rbp - 0x14], ebx
00793941  44 88 75 E2                     mov byte ptr [rbp - 0x1e], r14b
00793945  44 88 6D E1                     mov byte ptr [rbp - 0x1f], r13b
00793949  E9 A3 FE FF FF                  jmp 0x1407937f1
0079394E  80 7F 71 00                     cmp byte ptr [rdi + 0x71], 0
00793952  74 4B                           je 0x14079399f
00793954  C6 45 48 00                     mov byte ptr [rbp + 0x48], 0
00793958  C6 45 E0 00                     mov byte ptr [rbp - 0x20], 0
0079395C  89 5D E4                        mov dword ptr [rbp - 0x1c], ebx
0079395F  4C 89 65 F8                     mov qword ptr [rbp - 8], r12
00793963  49 83 C4 02                     add r12, 2
00793967  41 FF CF                        dec r15d
0079396A  44 89 7D 50                     mov dword ptr [rbp + 0x50], r15d
0079396E  E9 BE FB FF FF                  jmp 0x140793531
00793973  85 DB                           test ebx, ebx
00793975  75 28                           jne 0x14079399f
00793977  41 83 FF 01                     cmp r15d, 1
0079397B  7F 22                           jg 0x14079399f
0079397D  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00793981  C6 00 01                        mov byte ptr [rax], 1
00793984  33 C0                           xor eax, eax
00793986  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0079398E  48 83 C4 50                     add rsp, 0x50
00793992  41 5F                           pop r15
00793994  41 5E                           pop r14
00793996  41 5D                           pop r13
00793998  41 5C                           pop r12
0079399A  5F                              pop rdi
0079399B  5E                              pop rsi
0079399C  5D                              pop rbp
0079399D  C3                              ret
0079399E  CC                              int3
0079399F  B8 17 07 00 C0                  mov eax, 0xc0000717
007939A4  EB E0                           jmp 0x140793986
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Normalization__IsNormalized(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_m56;
    unsigned __int8 v_stack_m57;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    result = 0;
    if (a2 != 0) goto loc_0079350B;
    goto loc_00793986;
loc_0079350B:
    v_stack_m54 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_stack_m58 = (unsigned __int8)((unsigned int)(0xC000000DULL));
    v_stack_p10 = (unsigned __int8)((unsigned int)(0xC000000DULL));
    a2 = 0;
    v_stack_m40 = a2 - 2;
    v_rsi = 0;
    v_stack_m4C = 0;
    v_stack_m56 = 0;
    v_stack_m57 = 0;
loc_00793531:
    if (condition_is_less_or_equal) goto loc_0079397D;
    if (((unsigned int)(*(unsigned __int16 *)(a2))) < (*(unsigned int *)(a1 + 28))) goto loc_00793963;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a2)))) >> (7);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1)) == 0) goto loc_00793963;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1))) != 251) goto loc_0079356C;
    if ((*(unsigned __int8 *)(a1 + 113)) != 0) goto loc_00793963;
loc_0079356C:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1)) == 0) goto loc_00793954;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1))))) - (251));
    if (condition_is_equal) goto loc_0079394E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0079399F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00793680;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0079360E;
    if (((unsigned int)(a1)) != 1) goto loc_0079368C;
    if (((unsigned int)(*(unsigned __int16 *)(a2))) < 0xAC00ULL) goto loc_007935D5;
    if (((unsigned int)(*(unsigned __int16 *)(a2))) < 0xD7A4ULL) goto loc_0079365B;
    if (((unsigned int)(*(unsigned __int16 *)(a2) - 55216)) <= 22) goto loc_00793607;
    if (((unsigned int)(*(unsigned __int16 *)(a2) - 55243)) <= 48) goto loc_00793607;
loc_007935D1:
    goto loc_0079356C;
loc_007935D5:
    if (((unsigned int)((unsigned int)(a3))) <= 1) goto loc_007935F0;
    result = CanComposeHangul((unsigned int)((unsigned int)(*(unsigned __int16 *)(a2))), *(unsigned __int16 *)(a2 + 2), (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00793680;
loc_007935F0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (13));
    if ((((unsigned int)(result)) & (0xFFFFFEFFULL)) != 0) goto loc_00793607;
    if (((unsigned int)(*(unsigned __int16 *)(a2) - 4447)) <= 1) goto loc_007935D1;
loc_00793607:
    a2 = 0;
    goto loc_0079356C;
loc_0079360E:
    if (((unsigned int)((unsigned int)(a3))) <= 1) goto loc_0079399F;
    v_r12 = (a2) + (2);
    v_r15 = (unsigned int)(((unsigned int)(a3)) - 1);
    v_stack_p18 = (unsigned int)(v_r15);
    result = (unsigned int)(((unsigned int)(0x2400ULL)) + ((unsigned int)(*(unsigned __int16 *)(v_r12))));
    if (((unsigned __int16)(result)) > ((unsigned __int16)((unsigned int)(0x3FFULL)))) goto loc_0079399F;
    v_rbx = (unsigned int)((*(unsigned __int16 *)(a2)) + (0xFFFF2809ULL));
    v_rbx = (unsigned int)((v_rbx) << (10));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(*(unsigned __int16 *)(v_r12))));
    a1 = ((int)((unsigned int)(v_rbx))) >> (7);
    goto loc_0079356C;
loc_0079365B:
    if ((*(unsigned __int8 *)(a1 + 112)) == 1) goto loc_00793680;
    if (((unsigned int)(v_r15)) <= 1) goto loc_00793954;
    result = CanComposeHangul((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int16 *)(v_r12 + 2), (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00793954;
loc_00793680:
    *(unsigned __int8 *)(v_stack_p20) = 0;
    goto loc_00793984;
loc_0079368C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (127));
    a1 = ((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 32) * 1))) << (7);
    a1 = (a1) + (result);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128)) == 0) goto loc_00793954;
    v_r13 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128))) & (192));
    v_r14 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128))) & (63));
    if (condition_is_equal) goto loc_007936C2;
    if (((unsigned __int8)(v_r14)) != 63) goto loc_007936F6;
loc_007936C2:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(a1 + 40) * 1 - 128)))) - (64));
    if (condition_is_equal) goto loc_0079393E;
    a1 = (unsigned int)((a1) - (63));
    if (condition_is_equal) goto loc_0079394E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0079393E;
    a1 = (unsigned int)((a1) - (63));
    if (condition_is_equal) goto loc_00793680;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_007938F9;
    if (((unsigned int)(a1)) == 63) goto loc_00793973;
loc_007936F6:
    if ((((unsigned __int8)(v_r13)) & (191)) == 0) goto loc_007938F0;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = v_stack_m58;
    result = Normalization__GetLastChar(a1, v_r12, v_stack_m40, v_stack_m54);
    if ((unsigned __int8)(v_stack_m58) == 0) goto loc_007938B3;
    if (((unsigned __int8)(v_stack_m58)) == 63) goto loc_007938B3;
    if ((((unsigned __int8)(v_stack_p10)) & (191)) == 0) goto loc_0079381E;
    if (((unsigned __int8)(v_stack_m58)) > ((unsigned __int8)(v_r14))) goto loc_00793680;
    if (((unsigned __int8)(v_r13)) != 192) goto loc_007937ED;
    if (((unsigned __int8)(v_stack_m58)) == ((unsigned __int8)(v_r14))) goto loc_007937ED;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m57)) | ((unsigned __int8)(v_stack_m56)));
    result = (unsigned __int8)((result) - (64));
    if ((((unsigned __int8)(result)) & (191)) == 0) goto loc_00793788;
    if (((unsigned __int8)(v_stack_m57)) != 64) goto loc_007937A7;
    if ((unsigned __int8)(v_stack_m56) == 0) goto loc_00793788;
    if (((unsigned __int8)(v_stack_m56)) != 63) goto loc_007937A7;
loc_00793788:
    result = Normalization__CanCombinableCharactersCombine(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C))), (unsigned int)((unsigned int)(v_rbx)), v_stack_m54);
    if ((unsigned int)(result) != 0) goto loc_00793680;
    goto loc_007937AB;
loc_007937A7:
loc_007937AB:
    if (((unsigned __int8)(v_r14)) >= ((unsigned __int8)(v_stack_m56))) goto loc_007937ED;
    if ((((unsigned __int8)(v_stack_m57)) & (191)) != 0) goto loc_007937ED;
    if (((unsigned __int8)(v_stack_m56 - 1)) > 61) goto loc_007937ED;
    if (((unsigned __int8)(v_stack_m56)) != (*(unsigned __int8 *)(a1 + 116))) goto loc_007937FE;
    if (((unsigned __int8)(v_r14)) < (*(unsigned __int8 *)(a1 + 114))) goto loc_0079380A;
    if (((unsigned __int8)(v_r14)) != (*(unsigned __int8 *)(a1 + 115))) goto loc_007937ED;
loc_007937CE:
    v_stack_m68 = (unsigned int)(v_rbx);
    result = Normalization__CanCombineWithStartFirstPair(a1, v_stack_m48, v_stack_m50, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C))));
loc_007937E5:
    if ((unsigned int)(result) != 0) goto loc_00793680;
loc_007937ED:
loc_007937F1:
    v_stack_m58 = (unsigned __int8)(v_r14);
    v_stack_p10 = (unsigned __int8)(v_r13);
    goto loc_0079395C;
loc_007937FE:
    if (((unsigned __int8)(v_stack_m56)) != (*(unsigned __int8 *)(a1 + 118))) goto loc_0079380A;
    if (((unsigned __int8)(v_r14)) == (*(unsigned __int8 *)(a1 + 117))) goto loc_007937CE;
loc_0079380A:
    result = Normalization__CanCombineWithStartBase(a1, v_stack_m50, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_rbx)));
    goto loc_007937E5;
loc_0079381E:
    v_stack_m4C = (unsigned int)((unsigned int)(v_stack_m54));
    if (((unsigned __int8)(v_r13)) != 192) goto loc_007938A6;
    if (((unsigned __int8)((unsigned int)(v_stack_p18))) != 64) goto loc_00793850;
    result = Normalization__CanCombinableCharactersCombine(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) != 0) goto loc_00793680;
loc_00793850:
    if (((unsigned __int8)(v_stack_m56)) <= ((unsigned __int8)(v_r14))) goto loc_007938A6;
    if (((unsigned __int8)(v_stack_m56)) != (*(unsigned __int8 *)(a1 + 116))) goto loc_00793880;
    if (((unsigned __int8)(v_r14)) < (*(unsigned __int8 *)(a1 + 114))) goto loc_0079388C;
    if (((unsigned __int8)(v_r14)) != (*(unsigned __int8 *)(a1 + 115))) goto loc_007938A6;
loc_00793867:
    v_stack_m68 = (unsigned int)(v_rbx);
    result = Normalization__CanCombineWithStartFirstPair(a1, v_stack_m48, v_stack_m50, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C))));
    goto loc_0079389E;
loc_00793880:
    if (((unsigned __int8)(v_stack_m56)) != (*(unsigned __int8 *)(a1 + 118))) goto loc_0079388C;
    if (((unsigned __int8)(v_r14)) == (*(unsigned __int8 *)(a1 + 117))) goto loc_00793867;
loc_0079388C:
    result = Normalization__CanCombineWithStartBase(a1, v_stack_m50, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_rbx)));
loc_0079389E:
    if ((unsigned int)(result) != 0) goto loc_00793680;
loc_007938A6:
    v_stack_m56 = (unsigned __int8)(v_stack_m56);
    v_stack_m57 = (unsigned __int8)((unsigned int)(v_stack_p18));
    goto loc_007937ED;
loc_007938B3:
    v_stack_m4C = (unsigned int)((unsigned int)(v_stack_m54));
    v_stack_m56 = (unsigned __int8)(v_stack_m56);
    v_stack_m57 = (unsigned __int8)(v_stack_p10);
    if ((((unsigned __int8)(v_stack_p10 - 64)) & (191)) != 0) goto loc_007937F1;
    if (((unsigned __int8)(v_r13)) != 192) goto loc_007937F1;
    result = Normalization__CanCombinableCharactersCombine(a1, (unsigned int)(v_stack_m54), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rbx)));
    if ((unsigned int)(result) != 0) goto loc_00793680;
    goto loc_007937F1;
loc_007938F0:
    v_stack_m50 = 0;
    goto loc_0079393E;
loc_007938F9:
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = v_stack_m58;
    result = Normalization__GetLastChar(a1, v_r12, v_stack_m40, v_stack_m54);
    result = (unsigned __int8)((v_stack_p10) | (v_stack_m58));
    if (((unsigned __int8)(result)) != 128) goto loc_0079393E;
    result = Normalization__CanCombinableCharactersCombine(a1, (unsigned int)(v_stack_m54), (unsigned int)((unsigned int)(v_rbx)), v_stack_m54);
    if ((unsigned int)(result) != 0) goto loc_00793680;
loc_0079393E:
    v_stack_m4C = (unsigned int)(v_rbx);
    v_stack_m56 = (unsigned __int8)(v_r14);
    v_stack_m57 = (unsigned __int8)(v_r13);
    goto loc_007937F1;
loc_0079394E:
    if ((*(unsigned __int8 *)(a1 + 113)) == 0) goto loc_0079399F;
loc_00793954:
    v_stack_p10 = 0;
    v_stack_m58 = 0;
loc_0079395C:
    v_stack_m54 = (unsigned int)(v_rbx);
    v_stack_m40 = v_r12;
loc_00793963:
    v_r12 = (v_r12) + (2);
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p18)) - 1);
    v_stack_p18 = (unsigned int)(v_r15);
    goto loc_00793531;
loc_00793973:
    if ((unsigned int)(v_rbx) != 0) goto loc_0079399F;
    if (((unsigned int)(v_r15)) > 1) goto loc_0079399F;
loc_0079397D:
    *(unsigned __int8 *)(v_stack_p20) = 1;
loc_00793984:
    result = 0;
loc_00793986:
    v_rsp = (v_rsp) + (80);
    return result;
loc_0079399F:
    goto loc_00793986;
}
```

## 5. (Beta) C Style

```c
int64_t Normalization__IsNormalized(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint8_t v_stack_m56;
    uint8_t v_stack_m57;
    uint8_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    result = 0;
    if (Arg2 != NULL) goto loc_0079350B;
    goto loc_00793986;
loc_0079350B:
    v_stack_m54 = (uint32_t)((uint32_t)(0xC000000DULL));
    v_stack_m58 = (uint8_t)((uint32_t)(0xC000000DULL));
    v_stack_p10 = (uint8_t)((uint32_t)(0xC000000DULL));
    Arg2 = 0;
    v_stack_m40 = Arg2 - 2;
    local_rsi = 0;
    v_stack_m4C = 0;
    v_stack_m56 = 0;
    v_stack_m57 = 0;
loc_00793531:
    if (condition_is_less_or_equal) goto loc_0079397D;
    if (((uint32_t)(*(uint16_t *)(arg2))) < (*(uint32_t *)(arg1 + 0x1C))) goto loc_00793963;
    Arg1 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg2)))) >> (7);
    if ((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1)) == 0) goto loc_00793963;
    if (((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1))) != 251) goto loc_0079356C;
    if ((*(uint8_t *)(arg1 + 0x71)) != 0) goto loc_00793963;
loc_0079356C:
    if ((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1)) == 0) goto loc_00793954;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1))))) - (251));
    if (condition_is_equal) goto loc_0079394E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0079399F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00793680;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0079360E;
    if (((uint32_t)(Arg1)) != 1) goto loc_0079368C;
    if (((uint32_t)(*(uint16_t *)(arg2))) < 0xAC00ULL) goto loc_007935D5;
    if (((uint32_t)(*(uint16_t *)(arg2))) < 0xD7A4ULL) goto loc_0079365B;
    if (((uint32_t)(*(uint16_t *)(arg2) - 55216)) <= 22) goto loc_00793607;
    if (((uint32_t)(*(uint16_t *)(arg2) - 55243)) <= 48) goto loc_00793607;
loc_007935D1:
    goto loc_0079356C;
loc_007935D5:
    if (((uint32_t)((uint32_t)(Arg3))) <= 1) goto loc_007935F0;
    result = CanComposeHangul((uint32_t)((uint32_t)(*(uint16_t *)(arg2))), *(uint16_t *)(arg2 + 0x2), (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1)), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00793680;
loc_007935F0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (13));
    if ((((uint32_t)(result)) & (0xFFFFFEFFULL)) != 0) goto loc_00793607;
    if (((uint32_t)(*(uint16_t *)(arg2) - 4447)) <= 1) goto loc_007935D1;
loc_00793607:
    Arg2 = 0;
    goto loc_0079356C;
loc_0079360E:
    if (((uint32_t)((uint32_t)(Arg3))) <= 1) goto loc_0079399F;
    local_r12 = (Arg2) + (2);
    local_r15 = (uint32_t)(((uint32_t)(Arg3)) - 1);
    v_stack_p18 = (uint32_t)(local_r15);
    result = (uint32_t)(((uint32_t)(0x2400ULL)) + ((uint32_t)(*(uint16_t *)(local_r12))));
    if (((uint16_t)(result)) > ((uint16_t)((uint32_t)(0x3FFULL)))) goto loc_0079399F;
    local_rbx = (uint32_t)((*(uint16_t *)(arg2)) + (0xFFFF2809ULL));
    local_rbx = (uint32_t)((local_rbx) << (10));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(*(uint16_t *)(local_r12))));
    Arg1 = ((int32_t)((uint32_t)(local_rbx))) >> (7);
    goto loc_0079356C;
loc_0079365B:
    if ((*(uint8_t *)(arg1 + 0x70)) == 1) goto loc_00793680;
    if (((uint32_t)(local_r15)) <= 1) goto loc_00793954;
    result = CanComposeHangul((uint32_t)((uint32_t)(local_rbx)), *(uint16_t *)(local_r12 + 0x2), (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00793954;
loc_00793680:
    *(uint8_t *)(v_stack_p20) = 0;
    goto loc_00793984;
loc_0079368C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (127));
    Arg1 = ((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x20) * 1))) << (7);
    Arg1 = (Arg1) + (result);
    if ((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80)) == 0) goto loc_00793954;
    local_r13 = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80))) & (192));
    local_r14 = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80))) & (63));
    if (condition_is_equal) goto loc_007936C2;
    if (((uint8_t)(local_r14)) != 63) goto loc_007936F6;
loc_007936C2:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + *(uint64_t *)(arg1 + 0x28) * 1 - 0x80)))) - (64));
    if (condition_is_equal) goto loc_0079393E;
    Arg1 = (uint32_t)((Arg1) - (63));
    if (condition_is_equal) goto loc_0079394E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0079393E;
    Arg1 = (uint32_t)((Arg1) - (63));
    if (condition_is_equal) goto loc_00793680;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_007938F9;
    if (((uint32_t)(Arg1)) == 63) goto loc_00793973;
loc_007936F6:
    if ((((uint8_t)(local_r13)) & (191)) == 0) goto loc_007938F0;
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = v_stack_m58;
    result = Normalization__GetLastChar(Arg1, local_r12, v_stack_m40, v_stack_m54);
    if ((uint8_t)(v_stack_m58) == 0) goto loc_007938B3;
    if (((uint8_t)(v_stack_m58)) == 63) goto loc_007938B3;
    if ((((uint8_t)(v_stack_p10)) & (191)) == 0) goto loc_0079381E;
    if (((uint8_t)(v_stack_m58)) > ((uint8_t)(local_r14))) goto loc_00793680;
    if (((uint8_t)(local_r13)) != 192) goto loc_007937ED;
    if (((uint8_t)(v_stack_m58)) == ((uint8_t)(local_r14))) goto loc_007937ED;
    result = (uint8_t)(((uint8_t)(v_stack_m57)) | ((uint8_t)(v_stack_m56)));
    result = (uint8_t)((result) - (64));
    if ((((uint8_t)(result)) & (191)) == 0) goto loc_00793788;
    if (((uint8_t)(v_stack_m57)) != 64) goto loc_007937A7;
    if ((uint8_t)(v_stack_m56) == 0) goto loc_00793788;
    if (((uint8_t)(v_stack_m56)) != 63) goto loc_007937A7;
loc_00793788:
    result = Normalization__CanCombinableCharactersCombine(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C))), (uint32_t)((uint32_t)(local_rbx)), v_stack_m54);
    if ((uint32_t)(result) != 0) goto loc_00793680;
    goto loc_007937AB;
loc_007937A7:
loc_007937AB:
    if (((uint8_t)(local_r14)) >= ((uint8_t)(v_stack_m56))) goto loc_007937ED;
    if ((((uint8_t)(v_stack_m57)) & (191)) != 0) goto loc_007937ED;
    if (((uint8_t)(v_stack_m56 - 1)) > 61) goto loc_007937ED;
    if (((uint8_t)(v_stack_m56)) != (*(uint8_t *)(arg1 + 0x74))) goto loc_007937FE;
    if (((uint8_t)(local_r14)) < (*(uint8_t *)(arg1 + 0x72))) goto loc_0079380A;
    if (((uint8_t)(local_r14)) != (*(uint8_t *)(arg1 + 0x73))) goto loc_007937ED;
loc_007937CE:
    v_stack_m68 = (uint32_t)(local_rbx);
    result = Normalization__CanCombineWithStartFirstPair(Arg1, v_stack_m48, v_stack_m50, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C))));
loc_007937E5:
    if ((uint32_t)(result) != 0) goto loc_00793680;
loc_007937ED:
loc_007937F1:
    v_stack_m58 = (uint8_t)(local_r14);
    v_stack_p10 = (uint8_t)(local_r13);
    goto loc_0079395C;
loc_007937FE:
    if (((uint8_t)(v_stack_m56)) != (*(uint8_t *)(arg1 + 0x76))) goto loc_0079380A;
    if (((uint8_t)(local_r14)) == (*(uint8_t *)(arg1 + 0x75))) goto loc_007937CE;
loc_0079380A:
    result = Normalization__CanCombineWithStartBase(Arg1, v_stack_m50, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(local_rbx)));
    goto loc_007937E5;
loc_0079381E:
    v_stack_m4C = (uint32_t)((uint32_t)(v_stack_m54));
    if (((uint8_t)(local_r13)) != 192) goto loc_007938A6;
    if (((uint8_t)((uint32_t)(v_stack_p18))) != 64) goto loc_00793850;
    result = Normalization__CanCombinableCharactersCombine(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) != 0) goto loc_00793680;
loc_00793850:
    if (((uint8_t)(v_stack_m56)) <= ((uint8_t)(local_r14))) goto loc_007938A6;
    if (((uint8_t)(v_stack_m56)) != (*(uint8_t *)(arg1 + 0x74))) goto loc_00793880;
    if (((uint8_t)(local_r14)) < (*(uint8_t *)(arg1 + 0x72))) goto loc_0079388C;
    if (((uint8_t)(local_r14)) != (*(uint8_t *)(arg1 + 0x73))) goto loc_007938A6;
loc_00793867:
    v_stack_m68 = (uint32_t)(local_rbx);
    result = Normalization__CanCombineWithStartFirstPair(Arg1, v_stack_m48, v_stack_m50, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C))));
    goto loc_0079389E;
loc_00793880:
    if (((uint8_t)(v_stack_m56)) != (*(uint8_t *)(arg1 + 0x76))) goto loc_0079388C;
    if (((uint8_t)(local_r14)) == (*(uint8_t *)(arg1 + 0x75))) goto loc_00793867;
loc_0079388C:
    result = Normalization__CanCombineWithStartBase(Arg1, v_stack_m50, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_rbx)));
loc_0079389E:
    if ((uint32_t)(result) != 0) goto loc_00793680;
loc_007938A6:
    v_stack_m56 = (uint8_t)(v_stack_m56);
    v_stack_m57 = (uint8_t)((uint32_t)(v_stack_p18));
    goto loc_007937ED;
loc_007938B3:
    v_stack_m4C = (uint32_t)((uint32_t)(v_stack_m54));
    v_stack_m56 = (uint8_t)(v_stack_m56);
    v_stack_m57 = (uint8_t)(v_stack_p10);
    if ((((uint8_t)(v_stack_p10 - 64)) & (191)) != 0) goto loc_007937F1;
    if (((uint8_t)(local_r13)) != 192) goto loc_007937F1;
    result = Normalization__CanCombinableCharactersCombine(Arg1, (uint32_t)(v_stack_m54), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rbx)));
    if ((uint32_t)(result) != 0) goto loc_00793680;
    goto loc_007937F1;
loc_007938F0:
    v_stack_m50 = 0;
    goto loc_0079393E;
loc_007938F9:
    v_stack_m60 = v_stack_p10;
    v_stack_m68 = v_stack_m58;
    result = Normalization__GetLastChar(Arg1, local_r12, v_stack_m40, v_stack_m54);
    result = (uint8_t)((v_stack_p10) | (v_stack_m58));
    if (((uint8_t)(result)) != 128) goto loc_0079393E;
    result = Normalization__CanCombinableCharactersCombine(Arg1, (uint32_t)(v_stack_m54), (uint32_t)((uint32_t)(local_rbx)), v_stack_m54);
    if ((uint32_t)(result) != 0) goto loc_00793680;
loc_0079393E:
    v_stack_m4C = (uint32_t)(local_rbx);
    v_stack_m56 = (uint8_t)(local_r14);
    v_stack_m57 = (uint8_t)(local_r13);
    goto loc_007937F1;
loc_0079394E:
    if ((*(uint8_t *)(arg1 + 0x71)) == 0) goto loc_0079399F;
loc_00793954:
    v_stack_p10 = 0;
    v_stack_m58 = 0;
loc_0079395C:
    v_stack_m54 = (uint32_t)(local_rbx);
    v_stack_m40 = local_r12;
loc_00793963:
    local_r12 = (local_r12) + (2);
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p18)) - 1);
    v_stack_p18 = (uint32_t)(local_r15);
    goto loc_00793531;
loc_00793973:
    if ((uint32_t)(local_rbx) != 0) goto loc_0079399F;
    if (((uint32_t)(local_r15)) > 1) goto loc_0079399F;
loc_0079397D:
    *(uint8_t *)(v_stack_p20) = 1;
loc_00793984:
    result = 0;
loc_00793986:
    local_rsp = (local_rsp) + (80);
    return result;
loc_0079399F:
    goto loc_00793986;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x71` | `8` | `R` |
| `Arg1` | `+ 0x72` | `8` | `R` |
| `Arg1` | `+ 0x73` | `8` | `R` |
| `Arg1` | `+ 0x74` | `8` | `R` |
| `Arg1` | `+ 0x75` | `8` | `R` |
| `Arg1` | `+ 0x76` | `8` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007934D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
