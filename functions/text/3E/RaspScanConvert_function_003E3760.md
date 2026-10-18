# RaspScanConvert

- RVA: `0x003E3760`–`0x003E3BB4` (길이 `1,108` bytes)
- VA: `0x00000001403E3760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094CB0`
- 디코드: `312`개 명령, `1,108/1,108` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003E37BE` → [RaspCreateSegmentList](RaspCreateSegmentList_function_003E3ED8.md) (function, `0x003E3ED8`)
- `0x003E37D9` → [BgpFmRoundUp](BgpFmRoundUp_function_003E4218.md) (function, `0x003E4218`)
- `0x003E37E6` → [BgpFmRoundUp](BgpFmRoundUp_function_003E4218.md) (function, `0x003E4218`)
- `0x003E3887` → [RaspAllocateMemory](RaspAllocateMemory_function_003E42F8.md) (function, `0x003E42F8`)
- `0x003E38AF` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003E38D9` → [RaspAllocateMemory](RaspAllocateMemory_function_003E42F8.md) (function, `0x003E42F8`)
- `0x003E391F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003E395D` → [RaspTestIntersection](RaspTestIntersection_function_003E3BBC.md) (function, `0x003E3BBC`)
- `0x003E3A08` → [RaspFreeMemory](RaspFreeMemory_function_003E28E4.md) (function, `0x003E28E4`)
- `0x003E3A1F` → [RaspDestroySegmentList](RaspDestroySegmentList_function_003E4238.md) (function, `0x003E4238`)
- `0x003E3B20` → [BgpGxInitializeRectangle](../69/BgpGxInitializeRectangle_function_0069F1E4.md) (function, `0x0069F1E4`)
- `0x003E3B48` → [BgpGxInitializeRectangle](../69/BgpGxInitializeRectangle_function_0069F1E4.md) (function, `0x0069F1E4`)

### Direct callers
- [RaspRasterize](../6A/RaspRasterize_function_006A2AA4.md) at `0x006A2B48`

### Static image references
- `0x003E38BF` → RVA `0x010286D0` (`INITDATA`; read)
- `0x003E3B2F` → RVA `0x01028870` (`INITDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E3760  4C 8B DC                        mov r11, rsp
003E3763  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
003E3767  45 89 4B 20                     mov dword ptr [r11 + 0x20], r9d
003E376B  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
003E376F  55                              push rbp
003E3770  56                              push rsi
003E3771  57                              push rdi
003E3772  41 54                           push r12
003E3774  41 55                           push r13
003E3776  41 56                           push r14
003E3778  41 57                           push r15
003E377A  48 8B EC                        mov rbp, rsp
003E377D  48 83 EC 60                     sub rsp, 0x60
003E3781  4C 8B 65 78                     mov r12, qword ptr [rbp + 0x78]
003E3785  48 8D 45 40                     lea rax, [rbp + 0x40]
003E3789  44 8B 75 60                     mov r14d, dword ptr [rbp + 0x60]
003E378D  4C 8D 4D F8                     lea r9, [rbp - 8]
003E3791  44 0F B7 41 18                  movzx r8d, word ptr [rcx + 0x18]
003E3796  45 33 ED                        xor r13d, r13d
003E3799  4D 89 63 90                     mov qword ptr [r11 - 0x70], r12
003E379D  4C 8B FA                        mov r15, rdx
003E37A0  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
003E37A4  48 8B F1                        mov rsi, rcx
003E37A7  44 89 6D 40                     mov dword ptr [rbp + 0x40], r13d
003E37AB  41 8B FD                        mov edi, r13d
003E37AE  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
003E37B2  41 83 E6 01                     and r14d, 1
003E37B6  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
003E37BA  4C 89 6D F8                     mov qword ptr [rbp - 8], r13
003E37BE  E8 15 07 00 00                  call 0x1403e3ed8
003E37C3  8B D8                           mov ebx, eax
003E37C5  85 C0                           test eax, eax
003E37C7  0F 88 40 02 00 00               js 0x1403e3a0d
003E37CD  44 0F B7 4E 18                  movzx r9d, word ptr [rsi + 0x18]
003E37D2  8B 4E 0E                        mov ecx, dword ptr [rsi + 0xe]
003E37D5  41 83 E9 02                     sub r9d, 2
003E37D9  E8 3A 0A 00 00                  call 0x1403e4218
003E37DE  8B 4E 06                        mov ecx, dword ptr [rsi + 6]
003E37E1  8B D8                           mov ebx, eax
003E37E3  89 45 58                        mov dword ptr [rbp + 0x58], eax
003E37E6  E8 2D 0A 00 00                  call 0x1403e4218
003E37EB  44 8B DB                        mov r11d, ebx
003E37EE  45 8D 41 01                     lea r8d, [r9 + 1]
003E37F2  44 2B D8                        sub r11d, eax
003E37F5  BB 00 00 00 FC                  mov ebx, 0xfc000000
003E37FA  41 FF C3                        inc r11d
003E37FD  41 83 FB 01                     cmp r11d, 1
003E3801  0F 84 DC 02 00 00               je 0x1403e3ae3
003E3807  8B 75 58                        mov esi, dword ptr [rbp + 0x58]
003E380A  41 8B C0                        mov eax, r8d
003E380D  48 6B D0 11                     imul rdx, rax, 0x11
003E3811  41 8B C1                        mov eax, r9d
003E3814  48 6B C8 11                     imul rcx, rax, 0x11
003E3818  46 8B 44 3A 08                  mov r8d, dword ptr [rdx + r15 + 8]
003E381D  46 8B 54 39 08                  mov r10d, dword ptr [rcx + r15 + 8]
003E3822  45 2B C2                        sub r8d, r10d
003E3825  46 8B 0C 39                     mov r9d, dword ptr [rcx + r15]
003E3829  45 2B C1                        sub r8d, r9d
003E382C  46 03 04 3A                     add r8d, dword ptr [rdx + r15]
003E3830  41 8B C0                        mov eax, r8d
003E3833  C1 F8 06                        sar eax, 6
003E3836  8B C8                           mov ecx, eax
003E3838  0B CB                           or ecx, ebx
003E383A  45 85 C0                        test r8d, r8d
003E383D  0F 49 C8                        cmovns ecx, eax
003E3840  41 F6 C0 20                     test r8b, 0x20
003E3844  42 8D 04 9D 00 00 00 00         lea eax, [r11*4]
003E384C  89 45 D8                        mov dword ptr [rbp - 0x28], eax
003E384F  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
003E3852  44 8D 69 01                     lea r13d, [rcx + 1]
003E3856  44 0F 44 E9                     cmove r13d, ecx
003E385A  43 8D 0C 0A                     lea ecx, [r10 + r9]
003E385E  41 C1 E5 02                     shl r13d, 2
003E3862  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
003E3865  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
003E3869  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
003E386D  45 84 F6                        test r14b, r14b
003E3870  0F 85 B9 02 00 00               jne 0x1403e3b2f
003E3876  41 8B DD                        mov ebx, r13d
003E3879  49 8B D4                        mov rdx, r12
003E387C  0F AF D8                        imul ebx, eax
003E387F  C1 EB 03                        shr ebx, 3
003E3882  83 C3 48                        add ebx, 0x48
003E3885  8B CB                           mov ecx, ebx
003E3887  E8 6C 0A 00 00                  call 0x1403e42f8
003E388C  4C 8B C0                        mov r8, rax
003E388F  48 85 C0                        test rax, rax
003E3892  0F 85 7C 02 00 00               jne 0x1403e3b14
003E3898  BB 17 00 00 C0                  mov ebx, 0xc0000017
003E389D  85 DB                           test ebx, ebx
003E389F  0F 88 FE 02 00 00               js 0x1403e3ba3
003E38A5  44 8B 47 0C                     mov r8d, dword ptr [rdi + 0xc]
003E38A9  33 D2                           xor edx, edx
003E38AB  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
003E38AF  E8 8C 33 2E 00                  call 0x1406c6c40
003E38B4  48 83 7D F8 00                  cmp qword ptr [rbp - 8], 0
003E38B9  0F 84 10 02 00 00               je 0x1403e3acf
003E38BF  48 8D 05 0A 4E C4 00            lea rax, [rip + 0xc44e0a]
003E38C6  45 84 F6                        test r14b, r14b
003E38C9  0F 85 8D 02 00 00               jne 0x1403e3b5c
003E38CF  49 63 CD                        movsxd rcx, r13d
003E38D2  49 8B D4                        mov rdx, r12
003E38D5  48 C1 E1 02                     shl rcx, 2
003E38D9  E8 1A 0A 00 00                  call 0x1403e42f8
003E38DE  48 8B F0                        mov rsi, rax
003E38E1  48 85 C0                        test rax, rax
003E38E4  0F 84 B4 02 00 00               je 0x1403e3b9e
003E38EA  83 65 60 00                     and dword ptr [rbp + 0x60], 0
003E38EE  45 33 F6                        xor r14d, r14d
003E38F1  44 89 75 D4                     mov dword ptr [rbp - 0x2c], r14d
003E38F5  4D 63 FD                        movsxd r15, r13d
003E38F8  44 39 75 D8                     cmp dword ptr [rbp - 0x28], r14d
003E38FC  0F 8E E2 00 00 00               jle 0x1403e39e4
003E3902  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
003E3905  4A 8D 0C BD 00 00 00 00         lea rcx, [r15*4]
003E390D  44 8B 65 60                     mov r12d, dword ptr [rbp + 0x60]
003E3911  C1 E0 06                        shl eax, 6
003E3914  89 45 E0                        mov dword ptr [rbp - 0x20], eax
003E3917  4C 8B C1                        mov r8, rcx
003E391A  33 D2                           xor edx, edx
003E391C  48 8B CE                        mov rcx, rsi
003E391F  E8 1C 33 2E 00                  call 0x1406c6c40
003E3924  8B 4D 40                        mov ecx, dword ptr [rbp + 0x40]
003E3927  41 8B DE                        mov ebx, r14d
003E392A  83 E3 03                        and ebx, 3
003E392D  41 8B C6                        mov eax, r14d
003E3930  F7 DB                           neg ebx
003E3932  C1 E8 02                        shr eax, 2
003E3935  C1 E3 04                        shl ebx, 4
003E3938  C1 E0 06                        shl eax, 6
003E393B  2B D8                           sub ebx, eax
003E393D  03 5D E0                        add ebx, dword ptr [rbp - 0x20]
003E3940  85 C9                           test ecx, ecx
003E3942  74 44                           je 0x1403e3988
003E3944  4C 8B 75 F8                     mov r14, qword ptr [rbp - 8]
003E3948  44 8B E1                        mov r12d, ecx
003E394B  49 83 C6 18                     add r14, 0x18
003E394F  4C 8D 4D 50                     lea r9, [rbp + 0x50]
003E3953  8B D3                           mov edx, ebx
003E3955  4C 8D 45 D0                     lea r8, [rbp - 0x30]
003E3959  49 8D 4E E8                     lea rcx, [r14 - 0x18]
003E395D  E8 5A 02 00 00                  call 0x1403e3bbc
003E3962  44 8B 55 D0                     mov r10d, dword ptr [rbp - 0x30]
003E3966  41 81 FA FF FF FF 7F            cmp r10d, 0x7fffffff
003E396D  0F 85 CC 00 00 00               jne 0x1403e3a3f
003E3973  4D 63 FD                        movsxd r15, r13d
003E3976  49 83 C6 19                     add r14, 0x19
003E397A  49 83 EC 01                     sub r12, 1
003E397E  75 CF                           jne 0x1403e394f
003E3980  44 8B 75 D4                     mov r14d, dword ptr [rbp - 0x2c]
003E3984  44 8B 65 60                     mov r12d, dword ptr [rbp + 0x60]
003E3988  41 8B CC                        mov ecx, r12d
003E398B  41 8B C4                        mov eax, r12d
003E398E  83 E1 07                        and ecx, 7
003E3991  48 C1 E8 03                     shr rax, 3
003E3995  48 03 47 18                     add rax, qword ptr [rdi + 0x18]
003E3999  BA 80 00 00 00                  mov edx, 0x80
003E399E  D3 FA                           sar edx, cl
003E39A0  33 C9                           xor ecx, ecx
003E39A2  4D 85 FF                        test r15, r15
003E39A5  7E 19                           jle 0x1403e39c0
003E39A7  83 3C 8E 00                     cmp dword ptr [rsi + rcx*4], 0
003E39AB  74 02                           je 0x1403e39af
003E39AD  08 10                           or byte ptr [rax], dl
003E39AF  D0 EA                           shr dl, 1
003E39B1  75 05                           jne 0x1403e39b8
003E39B3  B2 80                           mov dl, 0x80
003E39B5  48 FF C0                        inc rax
003E39B8  48 FF C1                        inc rcx
003E39BB  49 3B CF                        cmp rcx, r15
003E39BE  7C E7                           jl 0x1403e39a7
003E39C0  45 03 E5                        add r12d, r13d
003E39C3  4A 8D 0C BD 00 00 00 00         lea rcx, [r15*4]
003E39CB  41 FF C6                        inc r14d
003E39CE  44 89 65 60                     mov dword ptr [rbp + 0x60], r12d
003E39D2  44 89 75 D4                     mov dword ptr [rbp - 0x2c], r14d
003E39D6  44 3B 75 D8                     cmp r14d, dword ptr [rbp - 0x28]
003E39DA  0F 8C 37 FF FF FF               jl 0x1403e3917
003E39E0  4C 8B 65 78                     mov r12, qword ptr [rbp + 0x78]
003E39E4  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
003E39E8  33 DB                           xor ebx, ebx
003E39EA  8B 4D 58                        mov ecx, dword ptr [rbp + 0x58]
003E39ED  48 89 38                        mov qword ptr [rax], rdi
003E39F0  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
003E39F4  89 08                           mov dword ptr [rax], ecx
003E39F6  48 8D 05 D3 4C C4 00            lea rax, [rip + 0xc44cd3]
003E39FD  48 3B F0                        cmp rsi, rax
003E3A00  74 0B                           je 0x1403e3a0d
003E3A02  48 8B CE                        mov rcx, rsi
003E3A05  49 8B D4                        mov rdx, r12
003E3A08  E8 D7 EE FF FF                  call 0x1403e28e4
003E3A0D  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
003E3A11  48 85 C0                        test rax, rax
003E3A14  74 0E                           je 0x1403e3a24
003E3A16  8B 55 40                        mov edx, dword ptr [rbp + 0x40]
003E3A19  4D 8B C4                        mov r8, r12
003E3A1C  48 8B C8                        mov rcx, rax
003E3A1F  E8 14 08 00 00                  call 0x1403e4238
003E3A24  8B C3                           mov eax, ebx
003E3A26  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
003E3A2E  48 83 C4 60                     add rsp, 0x60
003E3A32  41 5F                           pop r15
003E3A34  41 5E                           pop r14
003E3A36  41 5D                           pop r13
003E3A38  41 5C                           pop r12
003E3A3A  5F                              pop rdi
003E3A3B  5E                              pop rsi
003E3A3C  5D                              pop rbp
003E3A3D  C3                              ret
003E3A3E  CC                              int3
003E3A3F  49 8B 46 F8                     mov rax, qword ptr [r14 - 8]
003E3A43  49 8B 4E E8                     mov rcx, qword ptr [r14 - 0x18]
003E3A47  44 8B 48 04                     mov r9d, dword ptr [rax + 4]
003E3A4B  41 8B D1                        mov edx, r9d
003E3A4E  2B 51 0C                        sub edx, dword ptr [rcx + 0xc]
003E3A51  2B 51 04                        sub edx, dword ptr [rcx + 4]
003E3A54  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
003E3A58  41 03 D0                        add edx, r8d
003E3A5B  0F 84 09 01 00 00               je 0x1403e3b6a
003E3A61  85 D2                           test edx, edx
003E3A63  7E 5E                           jle 0x1403e3ac3
003E3A65  41 B8 01 00 00 00               mov r8d, 1
003E3A6B  45 33 C9                        xor r9d, r9d
003E3A6E  4D 63 FD                        movsxd r15, r13d
003E3A71  33 C9                           xor ecx, ecx
003E3A73  45 85 ED                        test r13d, r13d
003E3A76  0F 8E FA FE FF FF               jle 0x1403e3976
003E3A7C  44 8B 5D F0                     mov r11d, dword ptr [rbp - 0x10]
003E3A80  41 8B C1                        mov eax, r9d
003E3A83  41 8B D1                        mov edx, r9d
003E3A86  C1 E0 04                        shl eax, 4
003E3A89  83 E2 03                        and edx, 3
003E3A8C  83 E0 C0                        and eax, 0xffffffc0
003E3A8F  C1 E2 04                        shl edx, 4
003E3A92  41 03 C3                        add eax, r11d
003E3A95  03 D0                           add edx, eax
003E3A97  41 80 3E 01                     cmp byte ptr [r14], 1
003E3A9B  74 0D                           je 0x1403e3aaa
003E3A9D  81 7D 50 FF FF FF 7F            cmp dword ptr [rbp + 0x50], 0x7fffffff
003E3AA4  0F 85 E3 00 00 00               jne 0x1403e3b8d
003E3AAA  41 3B D2                        cmp edx, r10d
003E3AAD  7F 04                           jg 0x1403e3ab3
003E3AAF  44 01 04 8E                     add dword ptr [rsi + rcx*4], r8d
003E3AB3  41 FF C1                        inc r9d
003E3AB6  48 FF C1                        inc rcx
003E3AB9  49 3B CF                        cmp rcx, r15
003E3ABC  7C C2                           jl 0x1403e3a80
003E3ABE  E9 B3 FE FF FF                  jmp 0x1403e3976
003E3AC3  0F 89 BC 00 00 00               jns 0x1403e3b85
003E3AC9  41 83 C8 FF                     or r8d, 0xffffffff
003E3ACD  EB 9C                           jmp 0x1403e3a6b
003E3ACF  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
003E3AD3  48 89 38                        mov qword ptr [rax], rdi
003E3AD6  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
003E3ADA  89 30                           mov dword ptr [rax], esi
003E3ADC  33 C0                           xor eax, eax
003E3ADE  E9 43 FF FF FF                  jmp 0x1403e3a26
003E3AE3  41 8B C0                        mov eax, r8d
003E3AE6  48 6B C8 11                     imul rcx, rax, 0x11
003E3AEA  42 8B 54 39 04                  mov edx, dword ptr [rcx + r15 + 4]
003E3AEF  8B C2                           mov eax, edx
003E3AF1  C1 F8 06                        sar eax, 6
003E3AF4  8B C8                           mov ecx, eax
003E3AF6  0B CB                           or ecx, ebx
003E3AF8  85 D2                           test edx, edx
003E3AFA  0F 49 C8                        cmovns ecx, eax
003E3AFD  F6 C2 20                        test dl, 0x20
003E3B00  44 8D 59 01                     lea r11d, [rcx + 1]
003E3B04  44 0F 44 D9                     cmove r11d, ecx
003E3B08  41 8B F3                        mov esi, r11d
003E3B0B  44 89 5D 58                     mov dword ptr [rbp + 0x58], r11d
003E3B0F  E9 F6 FC FF FF                  jmp 0x1403e380a
003E3B14  44 8B CB                        mov r9d, ebx
003E3B17  48 8D 4D E0                     lea rcx, [rbp - 0x20]
003E3B1B  BA 01 00 00 00                  mov edx, 1
003E3B20  E8 BF B6 2B 00                  call 0x14069f1e4
003E3B25  8B D8                           mov ebx, eax
003E3B27  49 8B F8                        mov rdi, r8
003E3B2A  E9 6E FD FF FF                  jmp 0x1403e389d
003E3B2F  48 8D 3D 3A 4D C4 00            lea rdi, [rip + 0xc44d3a]
003E3B36  41 B9 44 0C 00 00               mov r9d, 0xc44
003E3B3C  4C 8B C7                        mov r8, rdi
003E3B3F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
003E3B43  BA 01 00 00 00                  mov edx, 1
003E3B48  E8 97 B6 2B 00                  call 0x14069f1e4
003E3B4D  8B D8                           mov ebx, eax
003E3B4F  85 C0                           test eax, eax
003E3B51  0F 88 B6 FE FF FF               js 0x1403e3a0d
003E3B57  E9 49 FD FF FF                  jmp 0x1403e38a5
003E3B5C  41 83 FD 68                     cmp r13d, 0x68
003E3B60  7F 3C                           jg 0x1403e3b9e
003E3B62  48 8B F0                        mov rsi, rax
003E3B65  E9 80 FD FF FF                  jmp 0x1403e38ea
003E3B6A  41 80 3E 01                     cmp byte ptr [r14], 1
003E3B6E  74 15                           je 0x1403e3b85
003E3B70  49 8B 46 F0                     mov rax, qword ptr [r14 - 0x10]
003E3B74  41 8B D1                        mov edx, r9d
003E3B77  2B 50 0C                        sub edx, dword ptr [rax + 0xc]
003E3B7A  2B 50 04                        sub edx, dword ptr [rax + 4]
003E3B7D  41 03 D0                        add edx, r8d
003E3B80  E9 DC FE FF FF                  jmp 0x1403e3a61
003E3B85  45 33 C0                        xor r8d, r8d
003E3B88  E9 DE FE FF FF                  jmp 0x1403e3a6b
003E3B8D  41 3B D2                        cmp edx, r10d
003E3B90  0F 8C 1D FF FF FF               jl 0x1403e3ab3
003E3B96  3B 55 50                        cmp edx, dword ptr [rbp + 0x50]
003E3B99  E9 0F FF FF FF                  jmp 0x1403e3aad
003E3B9E  BB 9A 00 00 C0                  mov ebx, 0xc000009a
003E3BA3  48 85 FF                        test rdi, rdi
003E3BA6  0F 84 61 FE FF FF               je 0x1403e3a0d
003E3BAC  48 8B CF                        mov rcx, rdi
003E3BAF  E9 51 FE FF FF                  jmp 0x1403e3a05
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RaspScanConvert(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (96);
    v_r13 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = a8;
    *(unsigned __int64 *)(v_rsp - 120) = v_stack_p8;
    v_stack_p8 = 0;
    v_stack_m68 = 0;
    v_r14 = (unsigned int)(((unsigned int)(a5)) & (1));
    v_stack_p18 = 0;
    v_stack_m40 = 0;
    result = RaspCreateSegmentList(a1, a2, *(unsigned __int16 *)(a1 + 24), v_stack_m40);
    if (sign_flag) goto loc_003E3A0D;
    a4 = (unsigned int)((*(unsigned __int16 *)(a1 + 24)) - (2));
    result = BgpFmRoundUp((unsigned int)(*(unsigned int *)(a1 + 14)), a2, *(unsigned __int16 *)(a1 + 24), a4);
    v_stack_p20 = (unsigned int)(result);
    result = BgpFmRoundUp((unsigned int)(*(unsigned int *)(a1 + 6)), a2, *(unsigned __int16 *)(a1 + 24), a4);
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - ((unsigned int)(result)));
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) == 1) goto loc_003E3AE3;
loc_003E380A:
    a2 = (a2) * ((unsigned int)((unsigned int)(a4 + 1)));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 6))) * ((unsigned int)(a4));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + a2 * 1 + 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + a2 * 1 + 8)))));
    a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + a2 * 1)))));
    a3 = (unsigned int)((a3) + (*(unsigned int *)(a2 + a2 * 1)));
    result = (unsigned int)(((unsigned int)(a3)) >> (6));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | ((unsigned int)((unsigned int)(0xFC000000ULL))));
    if (!sign_flag) { a1 = (unsigned int)(result); }
    v_stack_m60 = (unsigned int)(v_r11 * 4);
    v_stack_m54 = (unsigned int)(v_r11 * 4);
    v_r13 = a1 + 1;
    if ((((unsigned __int8)(a3)) & (32)) == 0) { v_r13 = (unsigned int)(a1); }
    v_r13 = (unsigned int)((v_r13) << (2));
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + a2 * 1 + 8)) + (unsigned int)(*(unsigned int *)(a1 + a2 * 1)) * 1);
    v_stack_m58 = (unsigned int)(v_r13);
    v_stack_m50 = (unsigned int)(v_r13);
    if ((unsigned __int8)(v_r14) != 0) goto loc_003E3B2F;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) * ((unsigned int)(v_r11 * 4)));
    v_rbx = (unsigned int)((v_rbx) >> (3));
    v_rbx = (unsigned int)((v_rbx) + (72));
    result = RaspAllocateMemory((unsigned int)((unsigned int)(v_rbx)), a8, a3, (unsigned int)(*(unsigned int *)(a1 + a2 * 1)));
    if (result != 0) goto loc_003E3B14;
loc_003E389D:
    if (sign_flag) goto loc_003E3BA3;
loc_003E38A5:
    a2 = 0;
    result = memset(*(unsigned __int64 *)(0 + 24), a2, (unsigned int)(*(unsigned int *)(0 + 12)), (unsigned int)(*(unsigned int *)(a1 + a2 * 1)));
    if (v_stack_m40 == 0) goto loc_003E3ACF;
    if ((unsigned __int8)(v_r14) != 0) goto loc_003E3B5C;
    a1 = ((int)((unsigned int)(v_r13))) << (2);
    result = RaspAllocateMemory(a1, a8, (unsigned int)(*(unsigned int *)(0 + 12)), (unsigned int)(*(unsigned int *)(a1 + a2 * 1)));
    if (result == 0) goto loc_003E3B9E;
loc_003E38EA:
    v_r14 = 0;
    v_stack_m64 = 0;
    if (v_stack_m60 <= 0) goto loc_003E39E4;
    result = (unsigned int)(((unsigned int)(v_stack_p20)) << (6));
    v_stack_m58 = (unsigned int)(result);
loc_003E3917:
    a2 = 0;
    result = memset(result, a2, (int)((unsigned int)(v_r13)) * 4, (unsigned int)(*(unsigned int *)(a1 + a2 * 1)));
    v_rbx = (unsigned int)((0) & (3));
    v_rbx = (unsigned int)(-(v_rbx));
    result = (unsigned int)((0) >> (2));
    v_rbx = (unsigned int)((v_rbx) << (4));
    result = (unsigned int)((result) << (6));
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) + (v_stack_m58));
    if ((unsigned int)((unsigned int)(v_stack_p8)) == 0) goto loc_003E3988;
    v_r14 = (v_stack_m40) + (24);
loc_003E394F:
    result = RaspTestIntersection(v_r14 - 24, (unsigned int)((unsigned int)(v_rbx)), v_stack_m68, v_stack_p18);
    if (((unsigned int)((unsigned int)(v_stack_m68))) != 0x7FFFFFFFULL) goto loc_003E3A3F;
loc_003E3976:
    v_r14 = (v_r14) + (25);
    v_r12 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) - (1);
    if (condition_is_not_equal) goto loc_003E394F;
loc_003E3988:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (7));
    result = ((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (3);
    result = (result) + (*(unsigned __int64 *)(0 + 24));
    a2 = (unsigned int)((128) >> ((unsigned __int8)(a1)));
    a1 = 0;
    if (condition_is_less_or_equal) goto loc_003E39C0;
loc_003E39A7:
    if ((*(unsigned int *)(result + a1 * 4)) != 0) {
    }
    a2 = (unsigned __int8)((a2) >> (1));
    if (!(condition_is_not_equal)) {
        a2 = 128;
        result = (result) + 1;
    }
    a1 = (a1) + 1;
    if (a1 < ((int)((unsigned int)(v_r13)))) goto loc_003E39A7;
loc_003E39C0:
    v_r12 = (unsigned int)(((unsigned int)(a5)) + ((unsigned int)(v_r13)));
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m64)) + 1);
    v_stack_p28 = (unsigned int)(v_r12);
    v_stack_m64 = (unsigned int)(v_r14);
    if (((unsigned int)(v_r14)) < v_stack_m60) goto loc_003E3917;
loc_003E39E4:
    v_rbx = 0;
    *(unsigned __int64 *)(a6) = 0;
    *(unsigned int *)(a7) = (unsigned int)((unsigned int)(v_stack_p20));
    if (result == (v_rip + 12864723)) goto loc_003E3A0D;
loc_003E3A05:
    result = RaspFreeMemory(result, a8, v_stack_m68, v_stack_p18);
loc_003E3A0D:
    result = v_stack_m40;
    if (v_stack_m40 != 0) {
        a2 = v_stack_p8;
        a3 = a8;
        a1 = v_stack_m40;
        result = RaspDestroySegmentList(a1, a2, a3, v_stack_p18);
    }
loc_003E3A26:
    v_rsp = (v_rsp) + (96);
    return 0;
loc_003E3A3F:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14 - 8) + 4))))) - (*(unsigned int *)(*(unsigned __int64 *)(v_r14 - 24) + 12)));
    a2 = (unsigned int)((a2) - (*(unsigned int *)(*(unsigned __int64 *)(v_r14 - 24) + 4)));
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14 - 8) + 12)))));
    if (condition_is_equal) goto loc_003E3B6A;
loc_003E3A61:
    if (condition_is_less_or_equal) goto loc_003E3AC3;
loc_003E3A6B:
    a4 = 0;
    a1 = 0;
    if (condition_is_less_or_equal) goto loc_003E3976;
loc_003E3A80:
    result = (unsigned int)((0) << (4));
    a2 = (unsigned int)((0) & (3));
    result = (unsigned int)((result) & (0xFFFFFFC0ULL));
    a2 = (unsigned int)((a2) << (4));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(v_stack_m48))));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    if ((*(unsigned __int8 *)(v_r14)) == 1) goto loc_003E3AAA;
    if (v_stack_p18 != 0x7FFFFFFFULL) goto loc_003E3B8D;
loc_003E3AAA:
loc_003E3AAD:
    if (((unsigned int)(a2)) <= ((unsigned int)((unsigned int)(v_stack_m68)))) {
    }
    a4 = (unsigned int)((a4) + 1);
    a1 = (a1) + 1;
    if (a1 < ((int)((unsigned int)(v_r13)))) goto loc_003E3A80;
    goto loc_003E3976;
loc_003E3AC3:
    if (!sign_flag) goto loc_003E3B85;
    a3 = (unsigned int)((1) | (0xFFFFFFFFULL));
    goto loc_003E3A6B;
loc_003E3ACF:
    *(unsigned __int64 *)(a6) = 0;
    *(unsigned int *)(a7) = (unsigned int)(result);
    result = 0;
    goto loc_003E3A26;
loc_003E3AE3:
    a1 = (a1) * ((unsigned int)(a3));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + (int)((unsigned int)(v_r13)) * 1 + 4))))) >> (6));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | ((unsigned int)(v_stack_p10)));
    if (!sign_flag) { a1 = (unsigned int)(result); }
    v_r11 = a1 + 1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + (int)((unsigned int)(v_r13)) * 1 + 4)))) & (32)) == 0) { v_r11 = (unsigned int)(a1); }
    v_stack_p20 = (unsigned int)(v_r11);
    goto loc_003E380A;
loc_003E3B14:
    result = BgpGxInitializeRectangle(v_stack_m58, 1, a3, (unsigned int)((unsigned int)(v_stack_p10)));
    goto loc_003E389D;
loc_003E3B2F:
    result = BgpGxInitializeRectangle(v_stack_m58, 1, v_rip + 12864826, (unsigned int)(0xC44ULL));
    if (sign_flag) goto loc_003E3A0D;
    goto loc_003E38A5;
loc_003E3B5C:
    if (((unsigned int)(v_r13)) > 104) goto loc_003E3B9E;
    goto loc_003E38EA;
loc_003E3B6A:
    if ((*(unsigned __int8 *)(v_r14)) == 1) goto loc_003E3B85;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC44ULL)))) - (*(unsigned int *)(*(unsigned __int64 *)(v_r14 - 16) + 12)));
    a2 = (unsigned int)((a2) - (*(unsigned int *)(*(unsigned __int64 *)(v_r14 - 16) + 4)));
    a2 = (unsigned int)((a2) + ((unsigned int)(v_rip + 12864826)));
    goto loc_003E3A61;
loc_003E3B85:
    a3 = 0;
    goto loc_003E3A6B;
loc_003E3B8D:
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(v_stack_m68)))) goto loc_003E3AB3;
    goto loc_003E3AAD;
loc_003E3B9E:
loc_003E3BA3:
    if (v_rip + 12864826 == 0) goto loc_003E3A0D;
    goto loc_003E3A05;
}
```

## 5. (Beta) C Style

```c
int64_t RaspScanConvert(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6, void *Arg7, int64_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (96);
    local_r13 = 0;
    *(uint64_t *)(local_rsp - 0x70) = Arg8;
    *(uint64_t *)(local_rsp - 0x78) = v_stack_p8;
    v_stack_p8 = 0;
    v_stack_m68 = 0;
    local_r14 = (uint32_t)(((uint32_t)(Arg5)) & (1));
    v_stack_p18 = 0;
    v_stack_m40 = 0;
    result = RaspCreateSegmentList(Arg1, Arg2, *(uint16_t *)(arg1 + 0x18), v_stack_m40);
    if (sign_flag) goto loc_003E3A0D;
    Arg4 = (uint32_t)((*(uint16_t *)(arg1 + 0x18)) - (2));
    result = BgpFmRoundUp((uint32_t)(*(uint32_t *)(arg1 + 0xE)), Arg2, *(uint16_t *)(arg1 + 0x18), Arg4);
    v_stack_p20 = (uint32_t)(result);
    result = BgpFmRoundUp((uint32_t)(*(uint32_t *)(arg1 + 0x6)), Arg2, *(uint16_t *)(arg1 + 0x18), Arg4);
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - ((uint32_t)(result)));
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) == 1) goto loc_003E3AE3;
loc_003E380A:
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(Arg4 + 1)));
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x6))) * ((uint32_t)(Arg4));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + Arg2 * 1 + 0x8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1 + 0x8)))));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1)))));
    Arg3 = (uint32_t)((Arg3) + (*(uint32_t *)(Arg2 + Arg2 * 1)));
    result = (uint32_t)(((uint32_t)(Arg3)) >> (6));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | ((uint32_t)((uint32_t)(0xFC000000ULL))));
    if (!sign_flag) { Arg1 = (uint32_t)(result); }
    v_stack_m60 = (uint32_t)(local_r11 * 4);
    v_stack_m54 = (uint32_t)(local_r11 * 4);
    local_r13 = Arg1 + 1;
    if ((((uint8_t)(Arg3)) & (32)) == 0) { local_r13 = (uint32_t)(Arg1); }
    local_r13 = (uint32_t)((local_r13) << (2));
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1 + 0x8)) + (uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1)) * 1);
    v_stack_m58 = (uint32_t)(local_r13);
    v_stack_m50 = (uint32_t)(local_r13);
    if ((uint8_t)(local_r14) != 0) goto loc_003E3B2F;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) * ((uint32_t)(local_r11 * 4)));
    local_rbx = (uint32_t)((local_rbx) >> (3));
    local_rbx = (uint32_t)((local_rbx) + (72));
    result = RaspAllocateMemory((uint32_t)((uint32_t)(local_rbx)), Arg8, Arg3, (uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1)));
    if (result != 0) goto loc_003E3B14;
loc_003E389D:
    if (sign_flag) goto loc_003E3BA3;
loc_003E38A5:
    Arg2 = 0;
    result = memset(*(uint64_t *)(0 + 0x18), Arg2, (uint32_t)(*(uint32_t *)(0 + 0xC)), (uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1)));
    if (v_stack_m40 == 0) goto loc_003E3ACF;
    if ((uint8_t)(local_r14) != 0) goto loc_003E3B5C;
    Arg1 = ((int32_t)((uint32_t)(local_r13))) << (2);
    result = RaspAllocateMemory(Arg1, Arg8, (uint32_t)(*(uint32_t *)(0 + 0xC)), (uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1)));
    if (result == 0) goto loc_003E3B9E;
loc_003E38EA:
    local_r14 = 0;
    v_stack_m64 = 0;
    if (v_stack_m60 <= 0) goto loc_003E39E4;
    result = (uint32_t)(((uint32_t)(v_stack_p20)) << (6));
    v_stack_m58 = (uint32_t)(result);
loc_003E3917:
    Arg2 = 0;
    result = memset(result, Arg2, (int32_t)((uint32_t)(local_r13)) * 4, (uint32_t)(*(uint32_t *)(arg1 + Arg2 * 1)));
    local_rbx = (uint32_t)((0) & (3));
    local_rbx = (uint32_t)(-(local_rbx));
    result = (uint32_t)((0) >> (2));
    local_rbx = (uint32_t)((local_rbx) << (4));
    result = (uint32_t)((result) << (6));
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) + (v_stack_m58));
    if ((uint32_t)((uint32_t)(v_stack_p8)) == 0) goto loc_003E3988;
    local_r14 = (v_stack_m40) + (24);
loc_003E394F:
    result = RaspTestIntersection(local_r14 - 24, (uint32_t)((uint32_t)(local_rbx)), v_stack_m68, v_stack_p18);
    if (((uint32_t)((uint32_t)(v_stack_m68))) != 0x7FFFFFFFULL) goto loc_003E3A3F;
loc_003E3976:
    local_r14 = (local_r14) + (25);
    local_r12 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) - (1);
    if (condition_is_not_equal) goto loc_003E394F;
loc_003E3988:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (7));
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (3);
    result = (result) + (*(uint64_t *)(0 + 0x18));
    Arg2 = (uint32_t)((128) >> ((uint8_t)(Arg1)));
    Arg1 = 0;
    if (condition_is_less_or_equal) goto loc_003E39C0;
loc_003E39A7:
    if ((*(uint32_t *)(result + arg1 * 4)) != 0) {
    }
    Arg2 = (uint8_t)((Arg2) >> (1));
    if (!(condition_is_not_equal)) {
        Arg2 = 128;
        result = (result) + 1;
    }
    Arg1 = (Arg1) + 1;
    if (Arg1 < ((int32_t)((uint32_t)(local_r13)))) goto loc_003E39A7;
loc_003E39C0:
    local_r12 = (uint32_t)(((uint32_t)(Arg5)) + ((uint32_t)(local_r13)));
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m64)) + 1);
    v_stack_p28 = (uint32_t)(local_r12);
    v_stack_m64 = (uint32_t)(local_r14);
    if (((uint32_t)(local_r14)) < v_stack_m60) goto loc_003E3917;
loc_003E39E4:
    local_rbx = 0;
    *(uint64_t *)(arg6) = 0;
    *(uint32_t *)(arg7) = (uint32_t)((uint32_t)(v_stack_p20));
    if (result == (v_rip + 12864723)) goto loc_003E3A0D;
loc_003E3A05:
    result = RaspFreeMemory(result, Arg8, v_stack_m68, v_stack_p18);
loc_003E3A0D:
    result = v_stack_m40;
    if (v_stack_m40 != 0) {
        Arg2 = v_stack_p8;
        Arg3 = Arg8;
        Arg1 = v_stack_m40;
        result = RaspDestroySegmentList(Arg1, Arg2, Arg3, v_stack_p18);
    }
loc_003E3A26:
    local_rsp = (local_rsp) + (96);
    return 0;
loc_003E3A3F:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14 - 0x8) + 0x4))))) - (*(uint32_t *)(*(uint64_t *)(local_r14 - 0x18) + 0xC)));
    Arg2 = (uint32_t)((Arg2) - (*(uint32_t *)(*(uint64_t *)(local_r14 - 0x18) + 0x4)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14 - 0x8) + 0xC)))));
    if (condition_is_equal) goto loc_003E3B6A;
loc_003E3A61:
    if (condition_is_less_or_equal) goto loc_003E3AC3;
loc_003E3A6B:
    Arg4 = 0;
    Arg1 = 0;
    if (condition_is_less_or_equal) goto loc_003E3976;
loc_003E3A80:
    result = (uint32_t)((0) << (4));
    Arg2 = (uint32_t)((0) & (3));
    result = (uint32_t)((result) & (0xFFFFFFC0ULL));
    Arg2 = (uint32_t)((Arg2) << (4));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(v_stack_m48))));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    if ((*(uint8_t *)(local_r14)) == 1) goto loc_003E3AAA;
    if (v_stack_p18 != 0x7FFFFFFFULL) goto loc_003E3B8D;
loc_003E3AAA:
loc_003E3AAD:
    if (((uint32_t)(Arg2)) <= ((uint32_t)((uint32_t)(v_stack_m68)))) {
    }
    Arg4 = (uint32_t)((Arg4) + 1);
    Arg1 = (Arg1) + 1;
    if (Arg1 < ((int32_t)((uint32_t)(local_r13)))) goto loc_003E3A80;
    goto loc_003E3976;
loc_003E3AC3:
    if (!sign_flag) goto loc_003E3B85;
    Arg3 = (uint32_t)((1) | (0xFFFFFFFFULL));
    goto loc_003E3A6B;
loc_003E3ACF:
    *(uint64_t *)(arg6) = 0;
    *(uint32_t *)(arg7) = (uint32_t)(result);
    result = 0;
    goto loc_003E3A26;
loc_003E3AE3:
    Arg1 = (Arg1) * ((uint32_t)(Arg3));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + (int32_t)((uint32_t)(local_r13)) * 1 + 0x4))))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | ((uint32_t)(v_stack_p10)));
    if (!sign_flag) { Arg1 = (uint32_t)(result); }
    local_r11 = Arg1 + 1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + (int32_t)((uint32_t)(local_r13)) * 1 + 0x4)))) & (32)) == 0) { local_r11 = (uint32_t)(Arg1); }
    v_stack_p20 = (uint32_t)(local_r11);
    goto loc_003E380A;
loc_003E3B14:
    result = BgpGxInitializeRectangle(v_stack_m58, 1, Arg3, (uint32_t)((uint32_t)(v_stack_p10)));
    goto loc_003E389D;
loc_003E3B2F:
    result = BgpGxInitializeRectangle(v_stack_m58, 1, v_rip + 12864826, (uint32_t)(0xC44ULL));
    if (sign_flag) goto loc_003E3A0D;
    goto loc_003E38A5;
loc_003E3B5C:
    if (((uint32_t)(local_r13)) > 104) goto loc_003E3B9E;
    goto loc_003E38EA;
loc_003E3B6A:
    if ((*(uint8_t *)(local_r14)) == 1) goto loc_003E3B85;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC44ULL)))) - (*(uint32_t *)(*(uint64_t *)(local_r14 - 0x10) + 0xC)));
    Arg2 = (uint32_t)((Arg2) - (*(uint32_t *)(*(uint64_t *)(local_r14 - 0x10) + 0x4)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(v_rip + 12864826)));
    goto loc_003E3A61;
loc_003E3B85:
    Arg3 = 0;
    goto loc_003E3A6B;
loc_003E3B8D:
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(v_stack_m68)))) goto loc_003E3AB3;
    goto loc_003E3AAD;
loc_003E3B9E:
loc_003E3BA3:
    if (v_rip + 12864826 == 0) goto loc_003E3A0D;
    goto loc_003E3A05;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x6` | `32` | `R` |
| `Arg1` | `+ 0xE` | `32` | `R` |
| `Arg1` | `+ 0x18` | `16` | `R` |
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E3760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
