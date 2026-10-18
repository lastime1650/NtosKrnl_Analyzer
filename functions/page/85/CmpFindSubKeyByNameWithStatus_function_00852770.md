# CmpFindSubKeyByNameWithStatus

- RVA: `0x00852770`–`0x00852B96` (길이 `1,062` bytes)
- VA: `0x0000000140852770`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069EA4`
- 디코드: `263`개 명령, `1,062/1,062` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00852804` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008528C3` → [CmpFindSubKeyInLeafWithStatus](CmpFindSubKeyInLeafWithStatus_function_00853A70.md) (function, `0x00853A70`)
- `0x008528F5` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085290F` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00852940` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00852A1D` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00852A53` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00852A66` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00852A8E` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00852AA7` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00852AC6` → [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) (function, `0x0085D890`)
- `0x00852AE4` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00852B06` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00852B24` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00852B2E` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00852B38` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00852B49` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00852B57` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00852B7F` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00852B8C` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- [CmpMarkCurrentValueDirty](../7D/CmpMarkCurrentValueDirty_function_007DBD1C.md) at `0x007DBD70`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E945C`
- [CmRenameKey](../7E/CmRenameKey_function_007E8F48.md) at `0x007E982F`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1AFF`
- [CmpFindControlSet](../7F/CmpFindControlSet_function_007F1A34.md) at `0x007F1DD1`
- [CmpWalkUnicodeStringPath](../7F/CmpWalkUnicodeStringPath_function_007F3704.md) at `0x007F377C`
- [CmpFindPathByNameEx](../84/CmpFindPathByNameEx_function_0084BAAC.md) at `0x0084BBFA`
- [CmpCopySyncTree2](CmpCopySyncTree2_function_0085BF78.md) at `0x0085C4A7`
- [CmpFindSubKeyByName](../A4/CmpFindSubKeyByName_function_00A49D58.md) at `0x00A49D66`
- [CmpSyncSubKeysAfterDelete](../AC/CmpSyncSubKeysAfterDelete_function_00AC5980.md) at `0x00AC5A47`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00852770  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00852775  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0085277A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0085277F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00852784  55                              push rbp
00852785  53                              push rbx
00852786  56                              push rsi
00852787  57                              push rdi
00852788  41 54                           push r12
0085278A  41 55                           push r13
0085278C  41 56                           push r14
0085278E  41 57                           push r15
00852790  48 8B EC                        mov rbp, rsp
00852793  48 83 EC 78                     sub rsp, 0x78
00852797  45 33 ED                        xor r13d, r13d
0085279A  C7 45 C8 FF FF FF FF            mov dword ptr [rbp - 0x38], 0xffffffff
008527A1  44 89 6D CC                     mov dword ptr [rbp - 0x34], r13d
008527A5  45 8B F5                        mov r14d, r13d
008527A8  44 89 6D B8                     mov dword ptr [rbp - 0x48], r13d
008527AC  4D 8B E0                        mov r12, r8
008527AF  44 89 6D C0                     mov dword ptr [rbp - 0x40], r13d
008527B3  4C 8B F9                        mov r15, rcx
008527B6  44 89 6D BC                     mov dword ptr [rbp - 0x44], r13d
008527BA  BB 34 00 00 C0                  mov ebx, 0xc0000034
008527BF  41 C7 01 FF FF FF FF            mov dword ptr [r9], 0xffffffff
008527C6  BE 00 00 00 80                  mov esi, 0x80000000
008527CB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
008527D0  45 3B B7 D8 00 00 00            cmp r14d, dword ptr [r15 + 0xd8]
008527D7  0F 83 B6 02 00 00               jae 0x140852a93
008527DD  41 8B C6                        mov eax, r14d
008527E0  83 7C 82 14 00                  cmp dword ptr [rdx + rax*4 + 0x14], 0
008527E5  0F 84 18 01 00 00               je 0x140852903
008527EB  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
008527F3  4C 8D 45 C8                     lea r8, [rbp - 0x38]
008527F7  8B 54 82 1C                     mov edx, dword ptr [rdx + rax*4 + 0x1c]
008527FB  49 8B CF                        mov rcx, r15
008527FE  0F 84 0B 01 00 00               je 0x14085290f
00852804  E8 57 24 00 00                  call 0x140854c60
00852809  48 8B F8                        mov rdi, rax
0085280C  48 85 C0                        test rax, rax
0085280F  0F 84 02 03 00 00               je 0x140852b17
00852815  B8 72 69 00 00                  mov eax, 0x6972
0085281A  66 39 07                        cmp word ptr [rdi], ax
0085281D  0F 84 8E 02 00 00               je 0x140852ab1
00852823  B8 6C 68 00 00                  mov eax, 0x686c
00852828  66 39 07                        cmp word ptr [rdi], ax
0085282B  75 78                           jne 0x1408528a5
0085282D  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00852832  41 8B F5                        mov esi, r13d
00852835  66 0F 7E C0                     movd eax, xmm0
00852839  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0085283D  66 83 F8 02                     cmp ax, 2
00852841  72 34                           jb 0x140852877
00852843  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
00852847  44 0F B7 F0                     movzx r14d, ax
0085284B  49 D1 EE                        shr r14, 1
0085284E  0F B7 03                        movzx eax, word ptr [rbx]
00852851  66 83 F8 61                     cmp ax, 0x61
00852855  72 0E                           jb 0x140852865
00852857  66 83 F8 7A                     cmp ax, 0x7a
0085285B  0F 87 C0 02 00 00               ja 0x140852b21
00852861  66 83 E8 20                     sub ax, 0x20
00852865  6B F6 25                        imul esi, esi, 0x25
00852868  48 83 C3 02                     add rbx, 2
0085286C  0F B7 C0                        movzx eax, ax
0085286F  03 F0                           add esi, eax
00852871  49 83 EE 01                     sub r14, 1
00852875  75 D7                           jne 0x14085284e
00852877  C7 45 B8 FF FF FF FF            mov dword ptr [rbp - 0x48], 0xffffffff
0085287E  41 0F B7 DD                     movzx ebx, r13w
00852882  66 3B 5F 02                     cmp bx, word ptr [rdi + 2]
00852886  73 12                           jae 0x14085289a
00852888  0F B7 C3                        movzx eax, bx
0085288B  3B 74 C7 08                     cmp esi, dword ptr [rdi + rax*8 + 8]
0085288F  0F 84 84 00 00 00               je 0x140852919
00852895  66 FF C3                        inc bx
00852898  EB E8                           jmp 0x140852882
0085289A  44 8B 75 BC                     mov r14d, dword ptr [rbp - 0x44]
0085289E  BB 34 00 00 C0                  mov ebx, 0xc0000034
008528A3  EB 3B                           jmp 0x1408528e0
008528A5  48 8D 45 C0                     lea rax, [rbp - 0x40]
008528A9  45 33 C9                        xor r9d, r9d
008528AC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008528B1  4D 8B C4                        mov r8, r12
008528B4  48 8D 45 B8                     lea rax, [rbp - 0x48]
008528B8  48 8B D7                        mov rdx, rdi
008528BB  49 8B CF                        mov rcx, r15
008528BE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008528C3  E8 A8 11 00 00                  call 0x140853a70
008528C8  8B D8                           mov ebx, eax
008528CA  03 C6                           add eax, esi
008528CC  85 C6                           test esi, eax
008528CE  0F 84 6D 01 00 00               je 0x140852a41
008528D4  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
008528D7  83 F9 FF                        cmp ecx, -1
008528DA  0F 85 90 01 00 00               jne 0x140852a70
008528E0  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
008528E8  48 8D 55 C8                     lea rdx, [rbp - 0x38]
008528EC  49 8B CF                        mov rcx, r15
008528EF  0F 85 B2 01 00 00               jne 0x140852aa7
008528F5  E8 46 36 00 00                  call 0x140855f40
008528FA  BE 00 00 00 80                  mov esi, 0x80000000
008528FF  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
00852903  41 FF C6                        inc r14d
00852906  44 89 75 BC                     mov dword ptr [rbp - 0x44], r14d
0085290A  E9 C1 FE FF FF                  jmp 0x1408527d0
0085290F  E8 9C 23 00 00                  call 0x140854cb0
00852914  E9 F0 FE FF FF                  jmp 0x140852809
00852919  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
00852921  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00852925  8B 54 C7 04                     mov edx, dword ptr [rdi + rax*8 + 4]
00852929  49 8B CF                        mov rcx, r15
0085292C  C7 45 D0 FF FF FF FF            mov dword ptr [rbp - 0x30], 0xffffffff
00852933  C7 45 D4 00 00 00 00            mov dword ptr [rbp - 0x2c], 0
0085293A  0F 84 26 01 00 00               je 0x140852a66
00852940  E8 1B 23 00 00                  call 0x140854c60
00852945  48 8B C8                        mov rcx, rax
00852948  48 85 C0                        test rax, rax
0085294B  0F 84 EE 01 00 00               je 0x140852b3f
00852951  F6 40 02 20                     test byte ptr [rax + 2], 0x20
00852955  4C 8D 40 4C                     lea r8, [rax + 0x4c]
00852959  0F 84 06 02 00 00               je 0x140852b65
0085295F  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00852964  45 0F B7 24 24                  movzx r12d, word ptr [r12]
00852969  44 0F B7 69 48                  movzx r13d, word ptr [rcx + 0x48]
0085296E  66 41 D1 EC                     shr r12w, 1
00852972  66 45 85 E4                     test r12w, r12w
00852976  74 7A                           je 0x1408529f2
00852978  66 45 85 ED                     test r13w, r13w
0085297C  74 74                           je 0x1408529f2
0085297E  44 0F B7 30                     movzx r14d, word ptr [rax]
00852982  48 83 C0 02                     add rax, 2
00852986  45 0F B6 38                     movzx r15d, byte ptr [r8]
0085298A  49 FF C0                        inc r8
0085298D  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00852991  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00852995  66 45 3B F7                     cmp r14w, r15w
00852999  74 48                           je 0x1408529e3
0085299B  66 41 83 FE 61                  cmp r14w, 0x61
008529A0  0F 82 B6 00 00 00               jb 0x140852a5c
008529A6  66 41 83 FE 7A                  cmp r14w, 0x7a
008529AB  0F 87 9E 00 00 00               ja 0x140852a4f
008529B1  B8 E0 FF 00 00                  mov eax, 0xffe0
008529B6  66 44 03 F0                     add r14w, ax
008529BA  41 83 FF 61                     cmp r15d, 0x61
008529BE  72 0E                           jb 0x1408529ce
008529C0  41 83 FF 7A                     cmp r15d, 0x7a
008529C4  0F 87 89 01 00 00               ja 0x140852b53
008529CA  66 44 03 F8                     add r15w, ax
008529CE  41 0F B7 C7                     movzx eax, r15w
008529D2  45 0F B7 F6                     movzx r14d, r14w
008529D6  44 2B F0                        sub r14d, eax
008529D9  75 22                           jne 0x1408529fd
008529DB  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
008529DF  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
008529E3  B9 FF FF 00 00                  mov ecx, 0xffff
008529E8  66 44 03 E1                     add r12w, cx
008529EC  66 44 03 E9                     add r13w, cx
008529F0  EB 80                           jmp 0x140852972
008529F2  41 0F B7 C5                     movzx eax, r13w
008529F6  45 0F B7 F4                     movzx r14d, r12w
008529FA  44 2B F0                        sub r14d, eax
008529FD  4C 8B 7D 48                     mov r15, qword ptr [rbp + 0x48]
00852A01  45 33 ED                        xor r13d, r13d
00852A04  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
00852A08  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
00852A10  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00852A14  49 8B CF                        mov rcx, r15
00852A17  0F 85 11 01 00 00               jne 0x140852b2e
00852A1D  E8 1E 35 00 00                  call 0x140855f40
00852A22  45 85 F6                        test r14d, r14d
00852A25  0F 85 6A FE FF FF               jne 0x140852895
00852A2B  44 8B 75 BC                     mov r14d, dword ptr [rbp - 0x44]
00852A2F  0F B7 C3                        movzx eax, bx
00852A32  41 8B DD                        mov ebx, r13d
00852A35  8B 4C C7 04                     mov ecx, dword ptr [rdi + rax*8 + 4]
00852A39  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
00852A3C  E9 96 FE FF FF                  jmp 0x1408528d7
00852A41  81 FB 34 00 00 C0               cmp ebx, 0xc0000034
00852A47  0F 84 87 FE FF FF               je 0x1408528d4
00852A4D  EB 2A                           jmp 0x140852a79
00852A4F  41 0F B7 CE                     movzx ecx, r14w
00852A53  E8 98 C6 00 00                  call 0x14085f0f0
00852A58  44 0F B7 F0                     movzx r14d, ax
00852A5C  B8 E0 FF 00 00                  mov eax, 0xffe0
00852A61  E9 54 FF FF FF                  jmp 0x1408529ba
00852A66  E8 45 22 00 00                  call 0x140854cb0
00852A6B  E9 D5 FE FF FF                  jmp 0x140852945
00852A70  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00852A74  41 8B DD                        mov ebx, r13d
00852A77  89 08                           mov dword ptr [rax], ecx
00852A79  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
00852A81  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00852A85  49 8B CF                        mov rcx, r15
00852A88  0F 85 BB 00 00 00               jne 0x140852b49
00852A8E  E8 AD 34 00 00                  call 0x140855f40
00852A93  8B C3                           mov eax, ebx
00852A95  48 83 C4 78                     add rsp, 0x78
00852A99  41 5F                           pop r15
00852A9B  41 5E                           pop r14
00852A9D  41 5D                           pop r13
00852A9F  41 5C                           pop r12
00852AA1  5F                              pop rdi
00852AA2  5E                              pop rsi
00852AA3  5B                              pop rbx
00852AA4  5D                              pop rbp
00852AA5  C3                              ret
00852AA6  CC                              int3
00852AA7  E8 74 A1 00 00                  call 0x14085cc20
00852AAC  E9 49 FE FF FF                  jmp 0x1408528fa
00852AB1  48 8D 45 B8                     lea rax, [rbp - 0x48]
00852AB5  45 33 C9                        xor r9d, r9d
00852AB8  4D 8B C4                        mov r8, r12
00852ABB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00852AC0  48 8B D7                        mov rdx, rdi
00852AC3  49 8B CF                        mov rcx, r15
00852AC6  E8 C5 AD 00 00                  call 0x14085d890
00852ACB  85 C0                           test eax, eax
00852ACD  78 70                           js 0x140852b3f
00852ACF  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
00852AD7  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00852ADB  49 8B CF                        mov rcx, r15
00852ADE  0F 85 A8 00 00 00               jne 0x140852b8c
00852AE4  E8 57 34 00 00                  call 0x140855f40
00852AE9  8B 55 B8                        mov edx, dword ptr [rbp - 0x48]
00852AEC  83 FA FF                        cmp edx, -1
00852AEF  0F 84 0A FE FF FF               je 0x1408528ff
00852AF5  41 F6 87 8C 00 00 00 01         test byte ptr [r15 + 0x8c], 1
00852AFD  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00852B01  49 8B CF                        mov rcx, r15
00852B04  74 32                           je 0x140852b38
00852B06  E8 55 21 00 00                  call 0x140854c60
00852B0B  48 8B F8                        mov rdi, rax
00852B0E  48 85 C0                        test rax, rax
00852B11  0F 85 0C FD FF FF               jne 0x140852823
00852B17  B8 9A 00 00 C0                  mov eax, 0xc000009a
00852B1C  E9 74 FF FF FF                  jmp 0x140852a95
00852B21  0F B7 C8                        movzx ecx, ax
00852B24  E8 C7 C5 00 00                  call 0x14085f0f0
00852B29  E9 37 FD FF FF                  jmp 0x140852865
00852B2E  E8 ED A0 00 00                  call 0x14085cc20
00852B33  E9 EA FE FF FF                  jmp 0x140852a22
00852B38  E8 73 21 00 00                  call 0x140854cb0
00852B3D  EB CC                           jmp 0x140852b0b
00852B3F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00852B44  E9 30 FF FF FF                  jmp 0x140852a79
00852B49  E8 D2 A0 00 00                  call 0x14085cc20
00852B4E  E9 40 FF FF FF                  jmp 0x140852a93
00852B53  41 0F B7 CF                     movzx ecx, r15w
00852B57  E8 94 C5 00 00                  call 0x14085f0f0
00852B5C  44 0F B7 F8                     movzx r15d, ax
00852B60  E9 69 FE FF FF                  jmp 0x1408529ce
00852B65  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
00852B6A  41 0F B7 14 24                  movzx edx, word ptr [r12]
00852B6F  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
00852B74  49 D1 E9                        shr r9, 1
00852B77  48 D1 EA                        shr rdx, 1
00852B7A  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00852B7F  E8 5C FC 11 00                  call 0x1409727e0
00852B84  44 8B F0                        mov r14d, eax
00852B87  E9 7C FE FF FF                  jmp 0x140852a08
00852B8C  E8 8F A0 00 00                  call 0x14085cc20
00852B91  E9 53 FF FF FF                  jmp 0x140852ae9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFindSubKeyByNameWithStatus(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    v_r13 = 0;
    v_stack_m78 = 0xFFFFFFFFULL;
    v_stack_m74 = 0;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m84 = 0;
    *(unsigned int *)(a4) = 0xFFFFFFFFULL;
loc_008527D0:
    if (0 >= (*(unsigned int *)(a1 + 216))) goto loc_00852A93;
    if ((*(unsigned int *)(a2 + 0 * 4 + 20)) == 0) goto loc_00852903;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085290F;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(a2 + 0 * 4 + 28)), v_stack_m78, a4);
loc_00852809:
    if (result == 0) goto loc_00852B17;
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)((unsigned int)(0x6972ULL)))) goto loc_00852AB1;
loc_00852823:
    if ((*(unsigned __int16 *)(result)) != ((unsigned __int16)((unsigned int)(0x686CULL)))) goto loc_008528A5;
    v_stack_m60 = v_xmm0;
    if (((unsigned __int16)((unsigned int)(0x686CULL))) < 2) goto loc_00852877;
    v_r14 = ((unsigned __int16)((unsigned int)(0x686CULL))) >> (1);
loc_0085284E:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58))) < 97) goto loc_00852865;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58))) > 122) goto loc_00852B21;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m58)) - (32));
loc_00852865:
    v_rsi = (unsigned int)((0) * (0));
    v_rbx = (v_stack_m58) + (2);
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)((unsigned __int16)(result))));
    v_r14 = (v_r14) - (1);
    if (condition_is_not_equal) goto loc_0085284E;
loc_00852877:
    v_stack_m88 = 0xFFFFFFFFULL;
loc_00852882:
    if (0 >= (*(unsigned __int16 *)(result + 2))) goto loc_0085289A;
    if (((unsigned int)(v_rsi)) == (*(unsigned int *)(result + 0 * 8 + 8))) goto loc_00852919;
loc_00852895:
    v_rbx = (unsigned __int16)((0) + 1);
    goto loc_00852882;
loc_0085289A:
    goto loc_008528E0;
loc_008528A5:
    a4 = 0;
    v_stack_m90 = v_stack_m80;
    v_stack_m98 = v_stack_m88;
    result = CmpFindSubKeyInLeafWithStatus(a1, result, a3, a4);
    result = (unsigned int)((result) + ((unsigned int)(v_rsi)));
    if ((((unsigned int)(v_rsi)) & ((unsigned int)(result))) == 0) goto loc_00852A41;
loc_008528D4:
loc_008528D7:
    if (((unsigned int)((unsigned int)(v_stack_m88))) != -1) goto loc_00852A70;
loc_008528E0:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_00852AA7;
    result = HvpReleaseCellPaged(a1, v_stack_m78, a3, a4);
loc_008528FA:
loc_008528FF:
loc_00852903:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m84)) + 1);
    v_stack_m84 = (unsigned int)(v_r14);
    goto loc_008527D0;
loc_0085290F:
    result = HvpGetCellPaged(a1, v_stack_p10, a3, a4);
    goto loc_00852809;
loc_00852919:
    v_stack_m70 = 0xFFFFFFFFULL;
    v_stack_m6C = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00852A66;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(result + result * 8 + 4)), v_stack_m70, a4);
loc_00852945:
    if (result == 0) goto loc_00852B3F;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_00852B65;
    v_r12 = (unsigned __int16)((*(unsigned __int16 *)(a3)) >> (1));
loc_00852972:
    if ((unsigned __int16)(v_r12) == 0) goto loc_008529F2;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_008529F2;
    result = (*(unsigned __int64 *)(a3 + 8)) + (2);
    a3 = (result + 76) + 1;
    v_stack_m68 = result;
    v_stack_m60 = a3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_008529E3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8)))) < 97) goto loc_00852A5C;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8)))) > 122) goto loc_00852A4F;
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a3 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_008529BA:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_008529CE;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_00852B53;
    v_r15 = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_008529CE:
    v_r14 = (unsigned int)(((unsigned __int16)(v_r14)) - ((unsigned int)((unsigned __int16)(v_r15))));
    if (condition_is_not_equal) goto loc_008529FD;
loc_008529E3:
    v_r12 = (unsigned __int16)((v_r12) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r13 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00852972;
loc_008529F2:
    v_r14 = (unsigned int)(((unsigned __int16)(v_r12)) - ((unsigned int)((unsigned __int16)(v_r13))));
loc_008529FD:
    v_r13 = 0;
loc_00852A08:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00852B2E;
    result = HvpReleaseCellPaged(v_stack_p8, v_stack_m70, v_stack_m60, a4);
loc_00852A22:
    if ((unsigned int)(v_r14) != 0) goto loc_00852895;
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned __int16)((unsigned int)((unsigned int)(result))) * 8 + 4)));
    goto loc_008528D7;
loc_00852A41:
    if (0 == 0xC0000034ULL) goto loc_008528D4;
    goto loc_00852A79;
loc_00852A4F:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)(v_stack_m84)), v_stack_m70, v_stack_m60, a4);
loc_00852A5C:
    goto loc_008529BA;
loc_00852A66:
    result = HvpGetCellPaged((unsigned __int16)((unsigned int)(v_stack_m84)), v_stack_m70, v_stack_m60, a4);
    goto loc_00852945;
loc_00852A70:
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned __int16)((unsigned int)(v_stack_m84)));
loc_00852A79:
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00852B49;
    result = HvpReleaseCellPaged(v_stack_p8, v_stack_m78, v_stack_m60, a4);
loc_00852A93:
loc_00852A95:
    v_rsp = (v_rsp) + (120);
    return 0;
loc_00852AA7:
    result = HvpReleaseCellFlat(v_stack_p8, v_stack_m78, v_stack_m60, a4);
    goto loc_008528FA;
loc_00852AB1:
    a4 = 0;
    v_stack_p20 = v_stack_m88;
    result = CmpFindSubKeyInRoot(v_stack_p8, result, v_stack_p18, a4);
    if (sign_flag) goto loc_00852B3F;
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) != 0) goto loc_00852B8C;
    result = HvpReleaseCellPaged(v_stack_p8, v_stack_m78, v_stack_p18, a4);
loc_00852AE9:
    if (((unsigned int)((unsigned int)(v_stack_m88))) == -1) goto loc_008528FF;
    if (((*(unsigned __int8 *)(v_stack_p8 + 140)) & (1)) == 0) goto loc_00852B38;
    result = HvpGetCellFlat(v_stack_p8, (unsigned int)(v_stack_m88), v_stack_m78, a4);
loc_00852B0B:
    if (result != 0) goto loc_00852823;
loc_00852B17:
    goto loc_00852A95;
loc_00852B21:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)(0xC000009AULL)), (unsigned int)(v_stack_m88), v_stack_m78, a4);
    goto loc_00852865;
loc_00852B2E:
    result = HvpReleaseCellFlat((unsigned __int16)((unsigned int)(0xC000009AULL)), (unsigned int)(v_stack_m88), v_stack_m78, a4);
    goto loc_00852A22;
loc_00852B38:
    result = HvpGetCellPaged((unsigned __int16)((unsigned int)(0xC000009AULL)), (unsigned int)(v_stack_m88), v_stack_m78, a4);
    goto loc_00852B0B;
loc_00852B3F:
    goto loc_00852A79;
loc_00852B49:
    result = HvpReleaseCellFlat((unsigned __int16)((unsigned int)(0xC000009AULL)), (unsigned int)(v_stack_m88), v_stack_m78, a4);
    goto loc_00852A93;
loc_00852B53:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_stack_p8), (unsigned int)(v_stack_m88), v_stack_m78, a4);
    goto loc_008529CE;
loc_00852B65:
    a4 = (*(unsigned __int16 *)((unsigned __int16)(v_stack_p8) + 72)) >> (1);
    a2 = (*(unsigned __int16 *)(v_stack_p18)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_stack_p18 + 8), a2, v_stack_m78, a4);
    goto loc_00852A08;
loc_00852B8C:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_stack_p18 + 8), a2, v_stack_m78, a4);
    goto loc_00852AE9;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFindSubKeyByNameWithStatus(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    local_r13 = 0;
    v_stack_m78 = 0xFFFFFFFFULL;
    v_stack_m74 = 0;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m84 = 0;
    *(uint32_t *)(arg4) = 0xFFFFFFFFULL;
loc_008527D0:
    if (0 >= (*(uint32_t *)(Arg1 + 0xD8))) goto loc_00852A93;
    if ((*(uint32_t *)(Arg2 + 0x0 * 4 + 0x14)) == 0) goto loc_00852903;
    if (((*(uint8_t *)(Arg1 + 0x8C)) & (1)) == 0) goto loc_0085290F;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(Arg2 + 0x0 * 4 + 0x1C)), v_stack_m78, Arg4);
loc_00852809:
    if (result == 0) goto loc_00852B17;
    if ((*(uint16_t *)(result)) == ((uint16_t)((uint32_t)(0x6972ULL)))) goto loc_00852AB1;
loc_00852823:
    if ((*(uint16_t *)(result)) != ((uint16_t)((uint32_t)(0x686CULL)))) goto loc_008528A5;
    v_stack_m60 = v_xmm0;
    if (((uint16_t)((uint32_t)(0x686CULL))) < 2) goto loc_00852877;
    local_r14 = ((uint16_t)((uint32_t)(0x686CULL))) >> (1);
loc_0085284E:
    if (((uint16_t)(*(uint16_t *)(v_stack_m58))) < 97) goto loc_00852865;
    if (((uint16_t)(*(uint16_t *)(v_stack_m58))) > 122) goto loc_00852B21;
    result = (uint16_t)((*(uint16_t *)(v_stack_m58)) - (32));
loc_00852865:
    local_rsi = (uint32_t)((0) * (0));
    local_rbx = (v_stack_m58) + (2);
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)((uint16_t)(result))));
    local_r14 = (local_r14) - (1);
    if (condition_is_not_equal) goto loc_0085284E;
loc_00852877:
    v_stack_m88 = 0xFFFFFFFFULL;
loc_00852882:
    if (0 >= (*(uint16_t *)(result + 0x2))) goto loc_0085289A;
    if (((uint32_t)(local_rsi)) == (*(uint32_t *)(result + 0x0 * 8 + 0x8))) goto loc_00852919;
loc_00852895:
    local_rbx = (uint16_t)((0) + 1);
    goto loc_00852882;
loc_0085289A:
    goto loc_008528E0;
loc_008528A5:
    Arg4 = 0;
    v_stack_m90 = v_stack_m80;
    v_stack_m98 = v_stack_m88;
    result = CmpFindSubKeyInLeafWithStatus(Arg1, result, Arg3, Arg4);
    result = (uint32_t)((result) + ((uint32_t)(local_rsi)));
    if ((((uint32_t)(local_rsi)) & ((uint32_t)(result))) == 0) goto loc_00852A41;
loc_008528D4:
loc_008528D7:
    if (((uint32_t)((uint32_t)(v_stack_m88))) != -1) goto loc_00852A70;
loc_008528E0:
    if (((*(uint8_t *)(Arg1 + 0x8C)) & (1)) != 0) goto loc_00852AA7;
    result = HvpReleaseCellPaged(Arg1, v_stack_m78, Arg3, Arg4);
loc_008528FA:
loc_008528FF:
loc_00852903:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m84)) + 1);
    v_stack_m84 = (uint32_t)(local_r14);
    goto loc_008527D0;
loc_0085290F:
    result = HvpGetCellPaged(Arg1, v_stack_p10, Arg3, Arg4);
    goto loc_00852809;
loc_00852919:
    v_stack_m70 = 0xFFFFFFFFULL;
    v_stack_m6C = 0;
    if (((*(uint8_t *)(Arg1 + 0x8C)) & (1)) == 0) goto loc_00852A66;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(result + result * 8 + 0x4)), v_stack_m70, Arg4);
loc_00852945:
    if (result == 0) goto loc_00852B3F;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_00852B65;
    local_r12 = (uint16_t)((*(uint16_t *)(Arg3)) >> (1));
loc_00852972:
    if ((uint16_t)(local_r12) == 0) goto loc_008529F2;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_008529F2;
    result = (*(uint64_t *)(Arg3 + 0x8)) + (2);
    Arg3 = (result + 76) + 1;
    v_stack_m68 = result;
    v_stack_m60 = Arg3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_008529E3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8)))) < 97) goto loc_00852A5C;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8)))) > 122) goto loc_00852A4F;
    local_r14 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(Arg3 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_008529BA:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_008529CE;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_00852B53;
    local_r15 = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_008529CE:
    local_r14 = (uint32_t)(((uint16_t)(local_r14)) - ((uint32_t)((uint16_t)(local_r15))));
    if (condition_is_not_equal) goto loc_008529FD;
loc_008529E3:
    local_r12 = (uint16_t)((local_r12) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r13 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00852972;
loc_008529F2:
    local_r14 = (uint32_t)(((uint16_t)(local_r12)) - ((uint32_t)((uint16_t)(local_r13))));
loc_008529FD:
    local_r13 = 0;
loc_00852A08:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00852B2E;
    result = HvpReleaseCellPaged(v_stack_p8, v_stack_m70, v_stack_m60, Arg4);
loc_00852A22:
    if ((uint32_t)(local_r14) != 0) goto loc_00852895;
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(result + (uint16_t)((uint32_t)((uint32_t)(result))) * 8 + 0x4)));
    goto loc_008528D7;
loc_00852A41:
    if (0 == 0xC0000034ULL) goto loc_008528D4;
    goto loc_00852A79;
loc_00852A4F:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)(v_stack_m84)), v_stack_m70, v_stack_m60, Arg4);
loc_00852A5C:
    goto loc_008529BA;
loc_00852A66:
    result = HvpGetCellPaged((uint16_t)((uint32_t)(v_stack_m84)), v_stack_m70, v_stack_m60, Arg4);
    goto loc_00852945;
loc_00852A70:
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint16_t)((uint32_t)(v_stack_m84)));
loc_00852A79:
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00852B49;
    result = HvpReleaseCellPaged(v_stack_p8, v_stack_m78, v_stack_m60, Arg4);
loc_00852A93:
loc_00852A95:
    local_rsp = (local_rsp) + (120);
    return 0;
loc_00852AA7:
    result = HvpReleaseCellFlat(v_stack_p8, v_stack_m78, v_stack_m60, Arg4);
    goto loc_008528FA;
loc_00852AB1:
    Arg4 = 0;
    v_stack_p20 = v_stack_m88;
    result = CmpFindSubKeyInRoot(v_stack_p8, result, v_stack_p18, Arg4);
    if (sign_flag) goto loc_00852B3F;
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) != 0) goto loc_00852B8C;
    result = HvpReleaseCellPaged(v_stack_p8, v_stack_m78, v_stack_p18, Arg4);
loc_00852AE9:
    if (((uint32_t)((uint32_t)(v_stack_m88))) == -1) goto loc_008528FF;
    if (((*(uint8_t *)(v_stack_p8 + 0x8C)) & (1)) == 0) goto loc_00852B38;
    result = HvpGetCellFlat(v_stack_p8, (uint32_t)(v_stack_m88), v_stack_m78, Arg4);
loc_00852B0B:
    if (result != 0) goto loc_00852823;
loc_00852B17:
    goto loc_00852A95;
loc_00852B21:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)(0xC000009AULL)), (uint32_t)(v_stack_m88), v_stack_m78, Arg4);
    goto loc_00852865;
loc_00852B2E:
    result = HvpReleaseCellFlat((uint16_t)((uint32_t)(0xC000009AULL)), (uint32_t)(v_stack_m88), v_stack_m78, Arg4);
    goto loc_00852A22;
loc_00852B38:
    result = HvpGetCellPaged((uint16_t)((uint32_t)(0xC000009AULL)), (uint32_t)(v_stack_m88), v_stack_m78, Arg4);
    goto loc_00852B0B;
loc_00852B3F:
    goto loc_00852A79;
loc_00852B49:
    result = HvpReleaseCellFlat((uint16_t)((uint32_t)(0xC000009AULL)), (uint32_t)(v_stack_m88), v_stack_m78, Arg4);
    goto loc_00852A93;
loc_00852B53:
    result = RtlUpcaseUnicodeChar((uint16_t)(v_stack_p8), (uint32_t)(v_stack_m88), v_stack_m78, Arg4);
    goto loc_008529CE;
loc_00852B65:
    Arg4 = (*(uint16_t *)((uint16_t)(v_stack_p8) + 0x48)) >> (1);
    Arg2 = (*(uint16_t *)(v_stack_p18)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(v_stack_p18 + 0x8), Arg2, v_stack_m78, Arg4);
    goto loc_00852A08;
loc_00852B8C:
    result = HvpReleaseCellFlat(*(uint64_t *)(v_stack_p18 + 0x8), Arg2, v_stack_m78, Arg4);
    goto loc_00852AE9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00852770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
