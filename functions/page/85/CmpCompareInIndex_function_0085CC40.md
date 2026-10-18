# CmpCompareInIndex

- RVA: `0x0085CC40`–`0x0085D35F` (길이 `1,823` bytes)
- VA: `0x000000014085CC40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AF7C`
- 디코드: `453`개 명령, `1,823/1,823` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085CD5B` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0085CD8C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0085CE12` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085CEE6` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085CF34` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085D020` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085D063` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085D06D` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085D0DB` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085D0F3` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085D11F` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085D137` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085D146` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D156` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D166` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D176` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D1A4` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x0085D1D1` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x0085D328` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D335` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D345` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085D352` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- [CmpAddToLeaf](CmpAddToLeaf_function_0085BC2C.md) at `0x0085BD4D`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085DE29`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085DE5B`
- [CmpFindSubKeyInRoot](CmpFindSubKeyInRoot_function_0085D890.md) at `0x0085E02C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0085CD5B` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0085CD8C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0085CC40  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0085CC45  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0085CC4A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0085CC4F  55                              push rbp
0085CC50  56                              push rsi
0085CC51  57                              push rdi
0085CC52  41 54                           push r12
0085CC54  41 55                           push r13
0085CC56  41 56                           push r14
0085CC58  41 57                           push r15
0085CC5A  48 83 EC 40                     sub rsp, 0x40
0085CC5E  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
0085CC66  48 8B DA                        mov rbx, rdx
0085CC69  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0085CC71  BA 6C 66 00 00                  mov edx, 0x666c
0085CC76  48 8B E9                        mov rbp, rcx
0085CC79  45 8B E1                        mov r12d, r9d
0085CC7C  B9 FF FD 00 00                  mov ecx, 0xfdff
0085CC81  45 33 F6                        xor r14d, r14d
0085CC84  44 0F B7 16                     movzx r10d, word ptr [rsi]
0085CC88  49 8B F8                        mov rdi, r8
0085CC8B  41 0F B7 C2                     movzx eax, r10w
0085CC8F  41 C7 07 FF FF FF FF            mov dword ptr [r15], 0xffffffff
0085CC96  66 2B C2                        sub ax, dx
0085CC99  66 85 C1                        test cx, ax
0085CC9C  0F 85 62 02 00 00               jne 0x14085cf04
0085CCA2  4C 8D 6E 04                     lea r13, [rsi + 4]
0085CCA6  41 8B C4                        mov eax, r12d
0085CCA9  4F 8D 6C E5 00                  lea r13, [r13 + r12*8]
0085CCAE  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
0085CCB3  66 44 3B D2                     cmp r10w, dx
0085CCB7  0F 85 23 01 00 00               jne 0x14085cde0
0085CCBD  41 BF 04 00 00 00               mov r15d, 4
0085CCC3  41 8B C6                        mov eax, r14d
0085CCC6  41 3B C7                        cmp eax, r15d
0085CCC9  73 10                           jae 0x14085ccdb
0085CCCB  8B C8                           mov ecx, eax
0085CCCD  46 38 74 29 04                  cmp byte ptr [rcx + r13 + 4], r14b
0085CCD2  74 04                           je 0x14085ccd8
0085CCD4  FF C0                           inc eax
0085CCD6  EB EE                           jmp 0x14085ccc6
0085CCD8  44 8B F8                        mov r15d, eax
0085CCDB  48 85 FF                        test rdi, rdi
0085CCDE  0F 85 23 04 00 00               jne 0x14085d107
0085CCE4  0F B7 03                        movzx eax, word ptr [rbx]
0085CCE7  D1 E8                           shr eax, 1
0085CCE9  41 3B C7                        cmp eax, r15d
0085CCEC  4A 8D 14 E5 00 00 00 00         lea rdx, [r12*8]
0085CCF4  45 8B D6                        mov r10d, r14d
0085CCF7  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
0085CCFF  44 0F 42 F8                     cmovb r15d, eax
0085CD03  45 3B D7                        cmp r10d, r15d
0085CD06  0F 83 D1 00 00 00               jae 0x14085cddd
0085CD0C  41 8B CA                        mov ecx, r10d
0085CD0F  48 85 FF                        test rdi, rdi
0085CD12  0F 85 CD 03 00 00               jne 0x14085d0e5
0085CD18  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0085CD1C  44 0F B7 04 48                  movzx r8d, word ptr [rax + rcx*2]
0085CD21  48 8D 04 0A                     lea rax, [rdx + rcx]
0085CD25  44 0F B6 4C 30 08               movzx r9d, byte ptr [rax + rsi + 8]
0085CD2B  66 41 83 F8 61                  cmp r8w, 0x61
0085CD30  73 4F                           jae 0x14085cd81
0085CD32  45 0F B7 D8                     movzx r11d, r8w
0085CD36  41 83 F9 61                     cmp r9d, 0x61
0085CD3A  73 15                           jae 0x14085cd51
0085CD3C  41 8B C1                        mov eax, r9d
0085CD3F  44 2B D8                        sub r11d, eax
0085CD42  75 6E                           jne 0x14085cdb2
0085CD44  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
0085CD4C  41 FF C2                        inc r10d
0085CD4F  EB B2                           jmp 0x14085cd03
0085CD51  41 83 F9 7A                     cmp r9d, 0x7a
0085CD55  0F 86 FF 02 00 00               jbe 0x14085d05a
0085CD5B  E8 90 14 AA FF                  call 0x1402fe1f0
0085CD60  4C 8B 80 B0 04 00 00            mov r8, qword ptr [rax + 0x4b0]
0085CD67  4D 85 C0                        test r8, r8
0085CD6A  74 0F                           je 0x14085cd7b
0085CD6C  B8 C0 00 00 00                  mov eax, 0xc0
0085CD71  66 44 3B C8                     cmp r9w, ax
0085CD75  0F 83 0E 03 00 00               jae 0x14085d089
0085CD7B  41 0F B7 C1                     movzx eax, r9w
0085CD7F  EB BE                           jmp 0x14085cd3f
0085CD81  66 41 83 F8 7A                  cmp r8w, 0x7a
0085CD86  0F 86 C1 02 00 00               jbe 0x14085d04d
0085CD8C  E8 5F 14 AA FF                  call 0x1402fe1f0
0085CD91  4C 8B 98 B0 04 00 00            mov r11, qword ptr [rax + 0x4b0]
0085CD98  4D 85 DB                        test r11, r11
0085CD9B  74 0F                           je 0x14085cdac
0085CD9D  B8 C0 00 00 00                  mov eax, 0xc0
0085CDA2  66 44 3B C0                     cmp r8w, ax
0085CDA6  0F 83 00 03 00 00               jae 0x14085d0ac
0085CDAC  45 0F B7 D8                     movzx r11d, r8w
0085CDB0  EB 84                           jmp 0x14085cd36
0085CDB2  45 85 DB                        test r11d, r11d
0085CDB5  B8 01 00 00 00                  mov eax, 1
0085CDBA  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085CDC0  41 0F 4E C6                     cmovle eax, r14d
0085CDC4  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0085CDCC  48 83 C4 40                     add rsp, 0x40
0085CDD0  41 5F                           pop r15
0085CDD2  41 5E                           pop r14
0085CDD4  41 5D                           pop r13
0085CDD6  41 5C                           pop r12
0085CDD8  5F                              pop rdi
0085CDD9  5E                              pop rsi
0085CDDA  5D                              pop rbp
0085CDDB  C3                              ret
0085CDDC  CC                              int3
0085CDDD  49 8B C4                        mov rax, r12
0085CDE0  F6 85 8C 00 00 00 01            test byte ptr [rbp + 0x8c], 1
0085CDE7  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
0085CDEF  8B 54 C6 04                     mov edx, dword ptr [rsi + rax*8 + 4]
0085CDF3  48 8B CD                        mov rcx, rbp
0085CDF6  C7 84 24 90 00 00 00 FF FF FF FF  mov dword ptr [rsp + 0x90], 0xffffffff
0085CE01  C7 84 24 94 00 00 00 00 00 00 00  mov dword ptr [rsp + 0x94], 0
0085CE0C  0F 84 51 02 00 00               je 0x14085d063
0085CE12  E8 49 7E FF FF                  call 0x140854c60
0085CE17  48 8B C8                        mov rcx, rax
0085CE1A  48 85 C0                        test rax, rax
0085CE1D  0F 84 DA 02 00 00               je 0x14085d0fd
0085CE23  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085CE27  4C 8D 78 4C                     lea r15, [rax + 0x4c]
0085CE2B  0F 84 52 03 00 00               je 0x14085d183
0085CE31  48 85 FF                        test rdi, rdi
0085CE34  0F 85 D6 02 00 00               jne 0x14085d110
0085CE3A  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0085CE3E  41 BD E0 FF 00 00               mov r13d, 0xffe0
0085CE44  0F B7 1B                        movzx ebx, word ptr [rbx]
0085CE47  0F B7 69 48                     movzx ebp, word ptr [rcx + 0x48]
0085CE4B  66 D1 EB                        shr bx, 1
0085CE4E  45 8D 65 1F                     lea r12d, [r13 + 0x1f]
0085CE52  66 85 DB                        test bx, bx
0085CE55  74 62                           je 0x14085ceb9
0085CE57  66 85 ED                        test bp, bp
0085CE5A  74 5D                           je 0x14085ceb9
0085CE5C  0F B7 38                        movzx edi, word ptr [rax]
0085CE5F  48 83 C0 02                     add rax, 2
0085CE63  41 0F B6 37                     movzx esi, byte ptr [r15]
0085CE67  49 FF C7                        inc r15
0085CE6A  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0085CE72  66 3B FE                        cmp di, si
0085CE75  74 38                           je 0x14085ceaf
0085CE77  66 83 FF 61                     cmp di, 0x61
0085CE7B  72 0E                           jb 0x14085ce8b
0085CE7D  66 83 FF 7A                     cmp di, 0x7a
0085CE81  0F 87 BC 02 00 00               ja 0x14085d143
0085CE87  66 41 03 FD                     add di, r13w
0085CE8B  83 FE 61                        cmp esi, 0x61
0085CE8E  72 0D                           jb 0x14085ce9d
0085CE90  83 FE 7A                        cmp esi, 0x7a
0085CE93  0F 87 CA 02 00 00               ja 0x14085d163
0085CE99  66 41 03 F5                     add si, r13w
0085CE9D  0F B7 C6                        movzx eax, si
0085CEA0  0F B7 FF                        movzx edi, di
0085CEA3  2B F8                           sub edi, eax
0085CEA5  75 1A                           jne 0x14085cec1
0085CEA7  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0085CEAF  66 41 03 DC                     add bx, r12w
0085CEB3  66 41 03 EC                     add bp, r12w
0085CEB7  EB 99                           jmp 0x14085ce52
0085CEB9  0F B7 C5                        movzx eax, bp
0085CEBC  0F B7 FB                        movzx edi, bx
0085CEBF  2B F8                           sub edi, eax
0085CEC1  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
0085CEC9  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
0085CECE  F6 85 8C 00 00 00 01            test byte ptr [rbp + 0x8c], 1
0085CED5  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
0085CEDD  48 8B CD                        mov rcx, rbp
0085CEE0  0F 85 F5 01 00 00               jne 0x14085d0db
0085CEE6  E8 55 90 FF FF                  call 0x140855f40
0085CEEB  85 FF                           test edi, edi
0085CEED  0F 84 44 01 00 00               je 0x14085d037
0085CEF3  0F 88 36 01 00 00               js 0x14085d02f
0085CEF9  41 BE 01 00 00 00               mov r14d, 1
0085CEFF  E9 41 01 00 00                  jmp 0x14085d045
0085CF04  F6 85 8C 00 00 00 01            test byte ptr [rbp + 0x8c], 1
0085CF0B  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
0085CF13  42 8B 54 A6 04                  mov edx, dword ptr [rsi + r12*4 + 4]
0085CF18  48 8B CD                        mov rcx, rbp
0085CF1B  C7 84 24 90 00 00 00 FF FF FF FF  mov dword ptr [rsp + 0x90], 0xffffffff
0085CF26  44 89 B4 24 94 00 00 00         mov dword ptr [rsp + 0x94], r14d
0085CF2E  0F 84 39 01 00 00               je 0x14085d06d
0085CF34  E8 27 7D FF FF                  call 0x140854c60
0085CF39  48 8B C8                        mov rcx, rax
0085CF3C  48 85 C0                        test rax, rax
0085CF3F  0F 84 B8 01 00 00               je 0x14085d0fd
0085CF45  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085CF49  4C 8D 40 4C                     lea r8, [rax + 0x4c]
0085CF4D  0F 84 5B 02 00 00               je 0x14085d1ae
0085CF53  48 85 FF                        test rdi, rdi
0085CF56  0F 85 CF 01 00 00               jne 0x14085d12b
0085CF5C  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0085CF60  41 BD E0 FF 00 00               mov r13d, 0xffe0
0085CF66  0F B7 1B                        movzx ebx, word ptr [rbx]
0085CF69  44 0F B7 79 48                  movzx r15d, word ptr [rcx + 0x48]
0085CF6E  66 D1 EB                        shr bx, 1
0085CF71  45 8D 65 1F                     lea r12d, [r13 + 0x1f]
0085CF75  66 85 DB                        test bx, bx
0085CF78  74 6D                           je 0x14085cfe7
0085CF7A  66 45 85 FF                     test r15w, r15w
0085CF7E  74 67                           je 0x14085cfe7
0085CF80  0F B7 38                        movzx edi, word ptr [rax]
0085CF83  48 83 C0 02                     add rax, 2
0085CF87  41 0F B6 28                     movzx ebp, byte ptr [r8]
0085CF8B  49 FF C0                        inc r8
0085CF8E  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0085CF96  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0085CF9B  66 3B FD                        cmp di, bp
0085CF9E  74 3D                           je 0x14085cfdd
0085CFA0  66 83 FF 61                     cmp di, 0x61
0085CFA4  72 0E                           jb 0x14085cfb4
0085CFA6  66 83 FF 7A                     cmp di, 0x7a
0085CFAA  0F 87 A3 01 00 00               ja 0x14085d153
0085CFB0  66 41 03 FD                     add di, r13w
0085CFB4  83 FD 61                        cmp ebp, 0x61
0085CFB7  72 0D                           jb 0x14085cfc6
0085CFB9  83 FD 7A                        cmp ebp, 0x7a
0085CFBC  0F 87 B1 01 00 00               ja 0x14085d173
0085CFC2  66 41 03 ED                     add bp, r13w
0085CFC6  0F B7 C5                        movzx eax, bp
0085CFC9  0F B7 FF                        movzx edi, di
0085CFCC  2B F8                           sub edi, eax
0085CFCE  75 20                           jne 0x14085cff0
0085CFD0  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0085CFD5  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0085CFDD  66 41 03 DC                     add bx, r12w
0085CFE1  66 45 03 FC                     add r15w, r12w
0085CFE5  EB 8E                           jmp 0x14085cf75
0085CFE7  41 0F B7 C7                     movzx eax, r15w
0085CFEB  0F B7 FB                        movzx edi, bx
0085CFEE  2B F8                           sub edi, eax
0085CFF0  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
0085CFF8  44 8B A4 24 98 00 00 00         mov r12d, dword ptr [rsp + 0x98]
0085D000  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0085D008  F6 85 8C 00 00 00 01            test byte ptr [rbp + 0x8c], 1
0085D00F  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
0085D017  48 8B CD                        mov rcx, rbp
0085D01A  0F 85 D3 00 00 00               jne 0x14085d0f3
0085D020  E8 1B 8F FF FF                  call 0x140855f40
0085D025  85 FF                           test edi, edi
0085D027  74 4E                           je 0x14085d077
0085D029  0F 89 CA FE FF FF               jns 0x14085cef9
0085D02F  41 BE FF FF FF FF               mov r14d, 0xffffffff
0085D035  EB 0E                           jmp 0x14085d045
0085D037  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
0085D03F  41 8B 45 00                     mov eax, dword ptr [r13]
0085D043  89 01                           mov dword ptr [rcx], eax
0085D045  41 8B C6                        mov eax, r14d
0085D048  E9 77 FD FF FF                  jmp 0x14085cdc4
0085D04D  45 0F B7 D8                     movzx r11d, r8w
0085D051  41 83 EB 20                     sub r11d, 0x20
0085D055  E9 DC FC FF FF                  jmp 0x14085cd36
0085D05A  41 8D 41 E0                     lea eax, [r9 - 0x20]
0085D05E  E9 DC FC FF FF                  jmp 0x14085cd3f
0085D063  E8 48 7C FF FF                  call 0x140854cb0
0085D068  E9 AA FD FF FF                  jmp 0x14085ce17
0085D06D  E8 3E 7C FF FF                  call 0x140854cb0
0085D072  E9 C2 FE FF FF                  jmp 0x14085cf39
0085D077  41 8B C4                        mov eax, r12d
0085D07A  8B 4C 86 04                     mov ecx, dword ptr [rsi + rax*4 + 4]
0085D07E  41 8B C6                        mov eax, r14d
0085D081  41 89 0F                        mov dword ptr [r15], ecx
0085D084  E9 3B FD FF FF                  jmp 0x14085cdc4
0085D089  41 0F B7 00                     movzx eax, word ptr [r8]
0085D08D  41 8B C9                        mov ecx, r9d
0085D090  C1 E9 04                        shr ecx, 4
0085D093  41 8B D1                        mov edx, r9d
0085D096  03 C8                           add ecx, eax
0085D098  83 E2 0F                        and edx, 0xf
0085D09B  41 0F B7 0C 48                  movzx ecx, word ptr [r8 + rcx*2]
0085D0A0  03 CA                           add ecx, edx
0085D0A2  66 45 03 0C 48                  add r9w, word ptr [r8 + rcx*2]
0085D0A7  E9 CF FC FF FF                  jmp 0x14085cd7b
0085D0AC  41 0F B7 D0                     movzx edx, r8w
0085D0B0  41 0F B7 C0                     movzx eax, r8w
0085D0B4  48 C1 E8 08                     shr rax, 8
0085D0B8  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
0085D0BD  8B C2                           mov eax, edx
0085D0BF  C1 E8 04                        shr eax, 4
0085D0C2  83 E2 0F                        and edx, 0xf
0085D0C5  83 E0 0F                        and eax, 0xf
0085D0C8  03 C8                           add ecx, eax
0085D0CA  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
0085D0CF  03 CA                           add ecx, edx
0085D0D1  66 45 03 04 4B                  add r8w, word ptr [r11 + rcx*2]
0085D0D6  E9 D1 FC FF FF                  jmp 0x14085cdac
0085D0DB  E8 40 FB FF FF                  call 0x14085cc20
0085D0E0  E9 06 FE FF FF                  jmp 0x14085ceeb
0085D0E5  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0085D0E9  44 0F B6 04 08                  movzx r8d, byte ptr [rax + rcx]
0085D0EE  E9 2E FC FF FF                  jmp 0x14085cd21
0085D0F3  E8 28 FB FF FF                  call 0x14085cc20
0085D0F8  E9 28 FF FF FF                  jmp 0x14085d025
0085D0FD  B8 02 00 00 00                  mov eax, 2
0085D102  E9 BD FC FF FF                  jmp 0x14085cdc4
0085D107  41 0F B7 00                     movzx eax, word ptr [r8]
0085D10B  E9 D9 FB FF FF                  jmp 0x14085cce9
0085D110  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085D115  4D 8B C7                        mov r8, r15
0085D118  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0085D11C  0F B7 17                        movzx edx, word ptr [rdi]
0085D11F  E8 EC A4 FE FF                  call 0x140847610
0085D124  8B F8                           mov edi, eax
0085D126  E9 A3 FD FF FF                  jmp 0x14085cece
0085D12B  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085D130  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0085D134  0F B7 17                        movzx edx, word ptr [rdi]
0085D137  E8 D4 A4 FE FF                  call 0x140847610
0085D13C  8B F8                           mov edi, eax
0085D13E  E9 C5 FE FF FF                  jmp 0x14085d008
0085D143  0F B7 CF                        movzx ecx, di
0085D146  E8 A5 1F 00 00                  call 0x14085f0f0
0085D14B  0F B7 F8                        movzx edi, ax
0085D14E  E9 38 FD FF FF                  jmp 0x14085ce8b
0085D153  0F B7 CF                        movzx ecx, di
0085D156  E8 95 1F 00 00                  call 0x14085f0f0
0085D15B  0F B7 F8                        movzx edi, ax
0085D15E  E9 51 FE FF FF                  jmp 0x14085cfb4
0085D163  0F B7 CE                        movzx ecx, si
0085D166  E8 85 1F 00 00                  call 0x14085f0f0
0085D16B  0F B7 F0                        movzx esi, ax
0085D16E  E9 2A FD FF FF                  jmp 0x14085ce9d
0085D173  0F B7 CD                        movzx ecx, bp
0085D176  E8 75 1F 00 00                  call 0x14085f0f0
0085D17B  0F B7 E8                        movzx ebp, ax
0085D17E  E9 43 FE FF FF                  jmp 0x14085cfc6
0085D183  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
0085D187  48 85 FF                        test rdi, rdi
0085D18A  75 57                           jne 0x14085d1e3
0085D18C  0F B7 13                        movzx edx, word ptr [rbx]
0085D18F  44 8B CE                        mov r9d, esi
0085D192  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0085D196  4D 8B C7                        mov r8, r15
0085D199  49 D1 E9                        shr r9, 1
0085D19C  48 D1 EA                        shr rdx, 1
0085D19F  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0085D1A4  E8 37 56 11 00                  call 0x1409727e0
0085D1A9  E9 76 FF FF FF                  jmp 0x14085d124
0085D1AE  44 0F B7 79 48                  movzx r15d, word ptr [rcx + 0x48]
0085D1B3  48 85 FF                        test rdi, rdi
0085D1B6  0F 85 C0 00 00 00               jne 0x14085d27c
0085D1BC  0F B7 13                        movzx edx, word ptr [rbx]
0085D1BF  45 8B CF                        mov r9d, r15d
0085D1C2  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0085D1C6  49 D1 E9                        shr r9, 1
0085D1C9  48 D1 EA                        shr rdx, 1
0085D1CC  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0085D1D1  E8 0A 56 11 00                  call 0x1409727e0
0085D1D6  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0085D1DE  E9 59 FF FF FF                  jmp 0x14085d13c
0085D1E3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0085D1E7  41 BD E0 FF 00 00               mov r13d, 0xffe0
0085D1ED  0F B7 07                        movzx eax, word ptr [rdi]
0085D1F0  66 D1 EE                        shr si, 1
0085D1F3  45 8D 65 1F                     lea r12d, [r13 + 0x1f]
0085D1F7  66 89 84 24 A0 00 00 00         mov word ptr [rsp + 0xa0], ax
0085D1FF  66 85 F6                        test si, si
0085D202  74 64                           je 0x14085d268
0085D204  66 85 C0                        test ax, ax
0085D207  74 5F                           je 0x14085d268
0085D209  41 0F B7 1F                     movzx ebx, word ptr [r15]
0085D20D  49 83 C7 02                     add r15, 2
0085D211  0F B6 39                        movzx edi, byte ptr [rcx]
0085D214  48 FF C1                        inc rcx
0085D217  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0085D21C  66 3B DF                        cmp bx, di
0085D21F  74 3D                           je 0x14085d25e
0085D221  66 83 FB 61                     cmp bx, 0x61
0085D225  72 0E                           jb 0x14085d235
0085D227  66 83 FB 7A                     cmp bx, 0x7a
0085D22B  0F 87 01 01 00 00               ja 0x14085d332
0085D231  66 41 03 DD                     add bx, r13w
0085D235  83 FF 61                        cmp edi, 0x61
0085D238  72 0D                           jb 0x14085d247
0085D23A  83 FF 7A                        cmp edi, 0x7a
0085D23D  0F 87 0C 01 00 00               ja 0x14085d34f
0085D243  66 41 03 FD                     add di, r13w
0085D247  0F B7 C7                        movzx eax, di
0085D24A  0F B7 FB                        movzx edi, bx
0085D24D  2B F8                           sub edi, eax
0085D24F  75 1F                           jne 0x14085d270
0085D251  0F B7 84 24 A0 00 00 00         movzx eax, word ptr [rsp + 0xa0]
0085D259  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0085D25E  66 41 03 F4                     add si, r12w
0085D262  66 41 03 C4                     add ax, r12w
0085D266  EB 8F                           jmp 0x14085d1f7
0085D268  0F B7 C0                        movzx eax, ax
0085D26B  0F B7 FE                        movzx edi, si
0085D26E  2B F8                           sub edi, eax
0085D270  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
0085D275  F7 DF                           neg edi
0085D277  E9 52 FC FF FF                  jmp 0x14085cece
0085D27C  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0085D280  41 BD E0 FF 00 00               mov r13d, 0xffe0
0085D286  0F B7 07                        movzx eax, word ptr [rdi]
0085D289  66 41 D1 EF                     shr r15w, 1
0085D28D  45 8D 65 1F                     lea r12d, [r13 + 0x1f]
0085D291  66 89 84 24 A0 00 00 00         mov word ptr [rsp + 0xa0], ax
0085D299  66 45 85 FF                     test r15w, r15w
0085D29D  74 66                           je 0x14085d305
0085D29F  66 85 C0                        test ax, ax
0085D2A2  74 61                           je 0x14085d305
0085D2A4  41 0F B7 18                     movzx ebx, word ptr [r8]
0085D2A8  49 83 C0 02                     add r8, 2
0085D2AC  0F B6 39                        movzx edi, byte ptr [rcx]
0085D2AF  48 FF C1                        inc rcx
0085D2B2  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0085D2B7  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0085D2BC  66 3B DF                        cmp bx, di
0085D2BF  74 3A                           je 0x14085d2fb
0085D2C1  66 83 FB 61                     cmp bx, 0x61
0085D2C5  72 0A                           jb 0x14085d2d1
0085D2C7  66 83 FB 7A                     cmp bx, 0x7a
0085D2CB  77 58                           ja 0x14085d325
0085D2CD  66 41 03 DD                     add bx, r13w
0085D2D1  83 FF 61                        cmp edi, 0x61
0085D2D4  72 09                           jb 0x14085d2df
0085D2D6  83 FF 7A                        cmp edi, 0x7a
0085D2D9  77 67                           ja 0x14085d342
0085D2DB  66 41 03 FD                     add di, r13w
0085D2DF  0F B7 C7                        movzx eax, di
0085D2E2  0F B7 FB                        movzx edi, bx
0085D2E5  2B F8                           sub edi, eax
0085D2E7  75 25                           jne 0x14085d30e
0085D2E9  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0085D2EE  0F B7 84 24 A0 00 00 00         movzx eax, word ptr [rsp + 0xa0]
0085D2F6  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0085D2FB  66 45 03 FC                     add r15w, r12w
0085D2FF  66 41 03 C4                     add ax, r12w
0085D303  EB 8C                           jmp 0x14085d291
0085D305  0F B7 C0                        movzx eax, ax
0085D308  41 0F B7 FF                     movzx edi, r15w
0085D30C  2B F8                           sub edi, eax
0085D30E  44 8B A4 24 98 00 00 00         mov r12d, dword ptr [rsp + 0x98]
0085D316  F7 DF                           neg edi
0085D318  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
0085D320  E9 E3 FC FF FF                  jmp 0x14085d008
0085D325  0F B7 CB                        movzx ecx, bx
0085D328  E8 C3 1D 00 00                  call 0x14085f0f0
0085D32D  0F B7 D8                        movzx ebx, ax
0085D330  EB 9F                           jmp 0x14085d2d1
0085D332  0F B7 CB                        movzx ecx, bx
0085D335  E8 B6 1D 00 00                  call 0x14085f0f0
0085D33A  0F B7 D8                        movzx ebx, ax
0085D33D  E9 F3 FE FF FF                  jmp 0x14085d235
0085D342  0F B7 CF                        movzx ecx, di
0085D345  E8 A6 1D 00 00                  call 0x14085f0f0
0085D34A  0F B7 F8                        movzx edi, ax
0085D34D  EB 90                           jmp 0x14085d2df
0085D34F  0F B7 CF                        movzx ecx, di
0085D352  E8 99 1D 00 00                  call 0x14085f0f0
0085D357  0F B7 F8                        movzx edi, ax
0085D35A  E9 E8 FE FF FF                  jmp 0x14085d247
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCompareInIndex(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int16 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_p94;
    unsigned int v_stack_p98;
    unsigned __int64 v_stack_pA0;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    v_r14 = 0;
    *(unsigned int *)(a6) = 0xFFFFFFFFULL;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a5))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_0085CF04;
    v_stack_m48 = a5 + 4 + (unsigned int)(a4) * 8;
    if (((unsigned __int16)(*(unsigned __int16 *)(a5))) != ((unsigned __int16)((unsigned int)(0x666CULL)))) goto loc_0085CDE0;
loc_0085CCC6:
    if (0 >= 4) goto loc_0085CCDB;
    if ((*(unsigned __int8 *)(0 + a5 + 4 + (unsigned int)(a4) * 8 * 1 + 4)) == 0) goto loc_0085CCD8;
    result = (unsigned int)((0) + 1);
    goto loc_0085CCC6;
loc_0085CCD8:
loc_0085CCDB:
    if (a3 != 0) goto loc_0085D107;
    result = (unsigned int)((*(unsigned __int16 *)(a2)) >> (1));
loc_0085CCE9:
    v_stack_p28 = (unsigned int)(a4) * 8;
    v_r15 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) { v_r15 = (unsigned int)(result); }
loc_0085CD03:
    if (0 >= ((unsigned int)(v_r15))) goto loc_0085CDDD;
    if (a3 != 0) goto loc_0085D0E5;
loc_0085CD21:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + 0 * 2))) >= 97) goto loc_0085CD81;
loc_0085CD36:
    if (((unsigned int)(*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8))) >= 97) goto loc_0085CD51;
loc_0085CD3F:
    v_r11 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + 0 * 2))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8))))));
    if (condition_is_not_equal) goto loc_0085CDB2;
    v_r10 = (unsigned int)((0) + 1);
    goto loc_0085CD03;
loc_0085CD51:
    if (((unsigned int)(*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8))) <= 122) goto loc_0085D05A;
    result = PsGetCurrentServerSiloGlobals(0, a5, *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + 0 * 2), *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
    if (*(unsigned __int64 *)(result + 1200) == 0) goto loc_0085CD7B;
    if (((unsigned __int16)(*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8))) >= 192) goto loc_0085D089;
loc_0085CD7B:
    goto loc_0085CD3F;
loc_0085CD81:
    if (((unsigned __int16)(*(unsigned __int64 *)(result + 1200))) <= 122) goto loc_0085D04D;
    result = PsGetCurrentServerSiloGlobals(0, a5, *(unsigned __int64 *)(result + 1200), *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
    if (*(unsigned __int64 *)(result + 1200) == 0) goto loc_0085CDAC;
    if (((unsigned __int16)(*(unsigned __int64 *)(result + 1200))) >= 192) goto loc_0085D0AC;
loc_0085CDAC:
    goto loc_0085CD36;
loc_0085CDB2:
    result = 1;
    if (condition_is_less_or_equal) { result = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
loc_0085CDC4:
    v_rsp = (v_rsp) + (64);
    return result;
loc_0085CDDD:
loc_0085CDE0:
    v_stack_p90 = 0xFFFFFFFFULL;
    v_stack_p94 = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0085D063;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(a5 + (unsigned int)(a4) * 8 + 4)), v_stack_p90, *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
loc_0085CE17:
    if (result == 0) goto loc_0085D0FD;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_0085D183;
    if (a3 != 0) goto loc_0085D110;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p10)) >> (1));
loc_0085CE52:
    if ((unsigned __int16)(v_rbx) == 0) goto loc_0085CEB9;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_0085CEB9;
    result = (*(unsigned __int64 *)(v_stack_p10 + 8)) + (2);
    v_r15 = (result + 76) + 1;
    v_stack_pA0 = result;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_0085CEAF;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8)))) < 97) goto loc_0085CE8B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8)))) > 122) goto loc_0085D143;
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085CE8B:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_0085CE9D;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_0085D163;
    v_rsi = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085CE9D:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_rsi))));
    if (condition_is_not_equal) goto loc_0085CEC1;
loc_0085CEAF:
    v_rbx = (unsigned __int16)((v_rbx) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    v_rbp = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    goto loc_0085CE52;
loc_0085CEB9:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rbp))));
loc_0085CEC1:
loc_0085CECE:
    if (((*(unsigned __int8 *)(v_stack_p80 + 140)) & (1)) != 0) goto loc_0085D0DB;
    result = HvpReleaseCellPaged(v_stack_p80, v_stack_p90, v_stack_p90, *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
loc_0085CEEB:
    if ((unsigned int)(v_rdi) == 0) goto loc_0085D037;
    if (sign_flag) goto loc_0085D02F;
loc_0085CEF9:
    goto loc_0085D045;
loc_0085CF04:
    v_stack_p90 = 0xFFFFFFFFULL;
    v_stack_p94 = 1;
    if (((*(unsigned __int8 *)(v_stack_p80 + 140)) & (1)) == 0) goto loc_0085D06D;
    result = HvpGetCellFlat(v_stack_p80, (unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)(0xFFE0ULL) + 31 * 4 + 4)), v_stack_p90, *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
loc_0085CF39:
    if (result == 0) goto loc_0085D0FD;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_0085D1AE;
    if (v_rdi != 0) goto loc_0085D12B;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(v_rbx)) >> (1));
loc_0085CF75:
    if ((unsigned __int16)(v_rbx) == 0) goto loc_0085CFE7;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_0085CFE7;
    result = (*(unsigned __int64 *)(v_rbx + 8)) + (2);
    a3 = (result + 76) + 1;
    v_stack_pA0 = result;
    v_stack_p30 = a3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_0085CFDD;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 8)))) < 97) goto loc_0085CFB4;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 8)))) > 122) goto loc_0085D153;
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085CFB4:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_0085CFC6;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_0085D173;
    v_rbp = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085CFC6:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_rbp))));
    if (condition_is_not_equal) goto loc_0085CFF0;
loc_0085CFDD:
    v_rbx = (unsigned __int16)((v_rbx) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    goto loc_0085CF75;
loc_0085CFE7:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_r15))));
loc_0085CFF0:
loc_0085D008:
    if (((*(unsigned __int8 *)(v_stack_p80 + 140)) & (1)) != 0) goto loc_0085D0F3;
    result = HvpReleaseCellPaged(v_stack_p80, v_stack_p90, v_stack_p30, *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
loc_0085D025:
    if ((unsigned int)(v_rdi) == 0) goto loc_0085D077;
    if (!sign_flag) goto loc_0085CEF9;
loc_0085D02F:
    goto loc_0085D045;
loc_0085D037:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0xFFE0ULL))));
loc_0085D045:
    goto loc_0085CDC4;
loc_0085D04D:
    v_r11 = (unsigned int)(((unsigned __int16)(v_stack_p30)) - (32));
    goto loc_0085CD36;
loc_0085D05A:
    goto loc_0085CD3F;
loc_0085D063:
    result = HvpGetCellPaged(a6, v_stack_p90, v_stack_p30, *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
    goto loc_0085CE17;
loc_0085D06D:
    result = HvpGetCellPaged(a6, v_stack_p90, v_stack_p30, *(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8));
    goto loc_0085CF39;
loc_0085D077:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + (unsigned int)((unsigned int)((unsigned int)(v_stack_p98))) * 4 + 4)));
    goto loc_0085CDC4;
loc_0085D089:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8)))) >> (4));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(v_stack_p30))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8)))) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p30 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)((*(unsigned __int8 *)((unsigned int)(a4) * 8 + 0 * 1 + a5 * 1 + 8)) + (*(unsigned __int16 *)(v_stack_p30 + a1 * 2)));
    goto loc_0085CD7B;
loc_0085D0AC:
    result = ((unsigned __int16)(v_stack_p30)) >> (8);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int16)(v_stack_p30)))) >> (4));
    a2 = (unsigned int)(((unsigned __int16)(v_stack_p30)) & (15));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r11 + a1 * 2)) + ((unsigned int)(a2)));
    a3 = (unsigned __int16)((v_stack_p30) + (*(unsigned __int16 *)(v_r11 + a1 * 2)));
    goto loc_0085CDAC;
loc_0085D0DB:
    result = HvpReleaseCellFlat(a1, a2, a3, a4);
    goto loc_0085CEEB;
loc_0085D0E5:
    goto loc_0085CD21;
loc_0085D0F3:
    result = HvpReleaseCellFlat(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 8) + a1 * 1), a4);
    goto loc_0085D025;
loc_0085D0FD:
    goto loc_0085CDC4;
loc_0085D107:
    goto loc_0085CCE9;
loc_0085D110:
    result = CmpCompareTwoCompressedNames(*(unsigned __int64 *)(v_rdi + 8), *(unsigned __int16 *)(v_rdi), a6, *(unsigned __int16 *)(a1 + 72));
loc_0085D124:
    goto loc_0085CECE;
loc_0085D12B:
    result = CmpCompareTwoCompressedNames(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), a6, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 72));
loc_0085D13C:
    goto loc_0085D008;
loc_0085D143:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)((unsigned int)(result))), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), a6, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 72));
    goto loc_0085CE8B;
loc_0085D153:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), a6, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 72));
    goto loc_0085CFB4;
loc_0085D163:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rsi), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), a6, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 72));
    goto loc_0085CE9D;
loc_0085D173:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_stack_p80), *(unsigned __int16 *)((unsigned int)((unsigned int)(result))), a6, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 72));
    goto loc_0085CFC6;
loc_0085D183:
    if ((unsigned __int16)(result) != 0) goto loc_0085D1E3;
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned __int16)(v_stack_p80) + 72)))) >> (1);
    a2 = (*(unsigned __int16 *)(v_rbx)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 8), a2, a6, a4);
    goto loc_0085D124;
loc_0085D1AE:
    if ((unsigned __int16)(result) != 0) goto loc_0085D27C;
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 8) + 72)))) >> (1);
    a2 = (*(unsigned __int16 *)(v_rbx)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_rbx + 8), a2, a6, a4);
    goto loc_0085D13C;
loc_0085D1E3:
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)((unsigned __int16)(v_stack_p80) + 72)) >> (1));
loc_0085D1F7:
    v_stack_pA0 = (unsigned __int16)(*(unsigned __int16 *)((unsigned __int16)(result)));
    if ((unsigned __int16)(v_rsi) == 0) goto loc_0085D268;
    if ((unsigned __int16)(*(unsigned __int16 *)((unsigned __int16)(result))) == 0) goto loc_0085D268;
    v_r15 = (a6) + (2);
    a1 = (*(unsigned __int64 *)((unsigned __int16)(result) + 8)) + 1;
    v_stack_p38 = a1;
    if (((unsigned __int16)(*(unsigned __int16 *)(a6))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned __int16)(result) + 8))))) goto loc_0085D25E;
    if (((unsigned __int16)(*(unsigned __int16 *)(a6))) < 97) goto loc_0085D235;
    if (((unsigned __int16)(*(unsigned __int16 *)(a6))) > 122) goto loc_0085D332;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(a6)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085D235:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned __int16)(result) + 8)))) < 97) goto loc_0085D247;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned __int16)(result) + 8)))) > 122) goto loc_0085D34F;
    v_rdi = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned __int16)(result) + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085D247:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rdi))));
    if (condition_is_not_equal) goto loc_0085D270;
loc_0085D25E:
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    result = (unsigned __int16)((a5) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    goto loc_0085D1F7;
loc_0085D268:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rsi)) - ((unsigned int)((unsigned __int16)(result))));
loc_0085D270:
    v_rdi = (unsigned int)(-(v_rdi));
    goto loc_0085CECE;
loc_0085D27C:
    v_r15 = (unsigned __int16)((v_r15) >> (1));
loc_0085D291:
    v_stack_pA0 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
    if ((unsigned __int16)(v_r15) == 0) goto loc_0085D305;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)) == 0) goto loc_0085D305;
    a3 = (a6) + (2);
    a1 = (*(unsigned __int64 *)(v_rdi + 8)) + 1;
    v_stack_p30 = a3;
    v_stack_p38 = a1;
    if (((unsigned __int16)(*(unsigned __int16 *)(a6))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 8))))) goto loc_0085D2FB;
    if (((unsigned __int16)(*(unsigned __int16 *)(a6))) < 97) goto loc_0085D2D1;
    if (((unsigned __int16)(*(unsigned __int16 *)(a6))) > 122) goto loc_0085D325;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(a6)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085D2D1:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 8)))) < 97) goto loc_0085D2DF;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 8)))) > 122) goto loc_0085D342;
    v_rdi = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0085D2DF:
    v_rdi = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rdi))));
    if (condition_is_not_equal) goto loc_0085D30E;
loc_0085D2FB:
    v_r15 = (unsigned __int16)((v_r15) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    result = (unsigned __int16)((a5) + ((unsigned __int16)((unsigned int)(0xFFE0ULL) + 31)));
    goto loc_0085D291;
loc_0085D305:
    v_rdi = (unsigned int)(((unsigned __int16)(v_r15)) - ((unsigned int)((unsigned __int16)(result))));
loc_0085D30E:
    v_rdi = (unsigned int)(-(v_rdi));
    goto loc_0085D008;
loc_0085D325:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rbx), a2, v_stack_p30, a4);
    goto loc_0085D2D1;
loc_0085D332:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), a2, v_stack_p30, a4);
    goto loc_0085D235;
loc_0085D342:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rdi), a2, v_stack_p30, a4);
    goto loc_0085D2DF;
loc_0085D34F:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), a2, v_stack_p30, a4);
    goto loc_0085D247;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCompareInIndex(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p90;
    uint32_t v_stack_p94;
    uint32_t v_stack_p98;
    uint64_t v_stack_pA0;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    local_r14 = 0;
    *(uint32_t *)(arg6) = 0xFFFFFFFFULL;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg5))) - ((uint16_t)((uint32_t)(0x666CULL))));
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) != 0) goto loc_0085CF04;
    v_stack_m48 = Arg5 + 4 + (uint32_t)(Arg4) * 8;
    if (((uint16_t)(*(uint16_t *)(arg5))) != ((uint16_t)((uint32_t)(0x666CULL)))) goto loc_0085CDE0;
loc_0085CCC6:
    if (0 >= 4) goto loc_0085CCDB;
    if ((*(uint8_t *)(0 + arg5 + 0x4 + (uint32_t)(Arg4) * 8 * 1 + 0x4)) == 0) goto loc_0085CCD8;
    result = (uint32_t)((0) + 1);
    goto loc_0085CCC6;
loc_0085CCD8:
loc_0085CCDB:
    if (Arg3 != NULL) goto loc_0085D107;
    result = (uint32_t)((*(uint16_t *)(arg2)) >> (1));
loc_0085CCE9:
    v_stack_p28 = (uint32_t)(Arg4) * 8;
    local_r15 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) { local_r15 = (uint32_t)(result); }
loc_0085CD03:
    if (0 >= ((uint32_t)(local_r15))) goto loc_0085CDDD;
    if (Arg3 != NULL) goto loc_0085D0E5;
loc_0085CD21:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x8) + 0x0 * 2))) >= 97) goto loc_0085CD81;
loc_0085CD36:
    if (((uint32_t)(*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8))) >= 97) goto loc_0085CD51;
loc_0085CD3F:
    local_r11 = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x8) + 0x0 * 2))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8))))));
    if (condition_is_not_equal) goto loc_0085CDB2;
    local_r10 = (uint32_t)((0) + 1);
    goto loc_0085CD03;
loc_0085CD51:
    if (((uint32_t)(*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8))) <= 122) goto loc_0085D05A;
    result = PsGetCurrentServerSiloGlobals(0, Arg5, *(uint16_t *)(*(uint64_t *)(arg2 + 0x8) + 0x0 * 2), *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
    if (*(uint64_t *)(result + 0x4B0) == 0) goto loc_0085CD7B;
    if (((uint16_t)(*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8))) >= 192) goto loc_0085D089;
loc_0085CD7B:
    goto loc_0085CD3F;
loc_0085CD81:
    if (((uint16_t)(*(uint64_t *)(result + 0x4B0))) <= 122) goto loc_0085D04D;
    result = PsGetCurrentServerSiloGlobals(0, Arg5, *(uint64_t *)(result + 0x4B0), *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
    if (*(uint64_t *)(result + 0x4B0) == 0) goto loc_0085CDAC;
    if (((uint16_t)(*(uint64_t *)(result + 0x4B0))) >= 192) goto loc_0085D0AC;
loc_0085CDAC:
    goto loc_0085CD36;
loc_0085CDB2:
    result = 1;
    if (condition_is_less_or_equal) { result = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
loc_0085CDC4:
    local_rsp = (local_rsp) + (64);
    return result;
loc_0085CDDD:
loc_0085CDE0:
    v_stack_p90 = 0xFFFFFFFFULL;
    v_stack_p94 = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0085D063;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(arg5 + (uint32_t)(Arg4) * 8 + 0x4)), v_stack_p90, *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
loc_0085CE17:
    if (result == 0) goto loc_0085D0FD;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_0085D183;
    if (Arg3 != NULL) goto loc_0085D110;
    local_rbx = (uint16_t)((*(uint16_t *)(v_stack_p10)) >> (1));
loc_0085CE52:
    if ((uint16_t)(local_rbx) == 0) goto loc_0085CEB9;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_0085CEB9;
    result = (*(uint64_t *)(v_stack_p10 + 0x8)) + (2);
    local_r15 = (result + 76) + 1;
    v_stack_pA0 = result;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_0085CEAF;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8)))) < 97) goto loc_0085CE8B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8)))) > 122) goto loc_0085D143;
    local_rdi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085CE8B:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_0085CE9D;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_0085D163;
    local_rsi = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085CE9D:
    local_rdi = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_rsi))));
    if (condition_is_not_equal) goto loc_0085CEC1;
loc_0085CEAF:
    local_rbx = (uint16_t)((local_rbx) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    local_rbp = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    goto loc_0085CE52;
loc_0085CEB9:
    local_rdi = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rbp))));
loc_0085CEC1:
loc_0085CECE:
    if (((*(uint8_t *)(v_stack_p80 + 0x8C)) & (1)) != 0) goto loc_0085D0DB;
    result = HvpReleaseCellPaged(v_stack_p80, v_stack_p90, v_stack_p90, *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
loc_0085CEEB:
    if ((uint32_t)(local_rdi) == 0) goto loc_0085D037;
    if (sign_flag) goto loc_0085D02F;
loc_0085CEF9:
    goto loc_0085D045;
loc_0085CF04:
    v_stack_p90 = 0xFFFFFFFFULL;
    v_stack_p94 = 1;
    if (((*(uint8_t *)(v_stack_p80 + 0x8C)) & (1)) == 0) goto loc_0085D06D;
    result = HvpGetCellFlat(v_stack_p80, (uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)(0xFFE0ULL) + 0x1F * 4 + 0x4)), v_stack_p90, *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
loc_0085CF39:
    if (result == 0) goto loc_0085D0FD;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_0085D1AE;
    if (local_rdi != 0) goto loc_0085D12B;
    local_rbx = (uint16_t)((*(uint16_t *)(local_rbx)) >> (1));
loc_0085CF75:
    if ((uint16_t)(local_rbx) == 0) goto loc_0085CFE7;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_0085CFE7;
    result = (*(uint64_t *)(local_rbx + 0x8)) + (2);
    Arg3 = (result + 76) + 1;
    v_stack_pA0 = result;
    v_stack_p30 = Arg3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_0085CFDD;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x8)))) < 97) goto loc_0085CFB4;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x8)))) > 122) goto loc_0085D153;
    local_rdi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbx + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085CFB4:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_0085CFC6;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_0085D173;
    local_rbp = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085CFC6:
    local_rdi = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_rbp))));
    if (condition_is_not_equal) goto loc_0085CFF0;
loc_0085CFDD:
    local_rbx = (uint16_t)((local_rbx) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    local_r15 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    goto loc_0085CF75;
loc_0085CFE7:
    local_rdi = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_r15))));
loc_0085CFF0:
loc_0085D008:
    if (((*(uint8_t *)(v_stack_p80 + 0x8C)) & (1)) != 0) goto loc_0085D0F3;
    result = HvpReleaseCellPaged(v_stack_p80, v_stack_p90, v_stack_p30, *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
loc_0085D025:
    if ((uint32_t)(local_rdi) == 0) goto loc_0085D077;
    if (!sign_flag) goto loc_0085CEF9;
loc_0085D02F:
    goto loc_0085D045;
loc_0085D037:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xFFE0ULL))));
loc_0085D045:
    goto loc_0085CDC4;
loc_0085D04D:
    local_r11 = (uint32_t)(((uint16_t)(v_stack_p30)) - (32));
    goto loc_0085CD36;
loc_0085D05A:
    goto loc_0085CD3F;
loc_0085D063:
    result = HvpGetCellPaged(Arg6, v_stack_p90, v_stack_p30, *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
    goto loc_0085CE17;
loc_0085D06D:
    result = HvpGetCellPaged(Arg6, v_stack_p90, v_stack_p30, *(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8));
    goto loc_0085CF39;
loc_0085D077:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + (uint32_t)((uint32_t)((uint32_t)(v_stack_p98))) * 4 + 0x4)));
    goto loc_0085CDC4;
loc_0085D089:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8)))) >> (4));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(v_stack_p30))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8)))) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p30 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)((*(uint8_t *)((uint32_t)(Arg4) * 8 + 0x0 * 1 + arg5 * 1 + 0x8)) + (*(uint16_t *)(v_stack_p30 + arg1 * 2)));
    goto loc_0085CD7B;
loc_0085D0AC:
    result = ((uint16_t)(v_stack_p30)) >> (8);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint16_t)(v_stack_p30)))) >> (4));
    Arg2 = (uint32_t)(((uint16_t)(v_stack_p30)) & (15));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(local_r11 + arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg3 = (uint16_t)((v_stack_p30) + (*(uint16_t *)(local_r11 + arg1 * 2)));
    goto loc_0085CDAC;
loc_0085D0DB:
    result = HvpReleaseCellFlat(Arg1, Arg2, Arg3, Arg4);
    goto loc_0085CEEB;
loc_0085D0E5:
    goto loc_0085CD21;
loc_0085D0F3:
    result = HvpReleaseCellFlat(Arg1, Arg2, *(uint8_t *)(*(uint64_t *)(local_rdi + 0x8) + arg1 * 1), Arg4);
    goto loc_0085D025;
loc_0085D0FD:
    goto loc_0085CDC4;
loc_0085D107:
    goto loc_0085CCE9;
loc_0085D110:
    result = CmpCompareTwoCompressedNames(*(uint64_t *)(local_rdi + 0x8), *(uint16_t *)(local_rdi), Arg6, *(uint16_t *)(arg1 + 0x48));
loc_0085D124:
    goto loc_0085CECE;
loc_0085D12B:
    result = CmpCompareTwoCompressedNames(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8), *(uint16_t *)((uint32_t)((uint32_t)(result))), Arg6, *(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x48));
loc_0085D13C:
    goto loc_0085D008;
loc_0085D143:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)((uint32_t)(result))), *(uint16_t *)((uint32_t)((uint32_t)(result))), Arg6, *(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x48));
    goto loc_0085CE8B;
loc_0085D153:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), *(uint16_t *)((uint32_t)((uint32_t)(result))), Arg6, *(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x48));
    goto loc_0085CFB4;
loc_0085D163:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rsi), *(uint16_t *)((uint32_t)((uint32_t)(result))), Arg6, *(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x48));
    goto loc_0085CE9D;
loc_0085D173:
    result = RtlUpcaseUnicodeChar((uint16_t)(v_stack_p80), *(uint16_t *)((uint32_t)((uint32_t)(result))), Arg6, *(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x48));
    goto loc_0085CFC6;
loc_0085D183:
    if ((uint16_t)(result) != 0) goto loc_0085D1E3;
    Arg4 = ((uint32_t)((uint32_t)(*(uint16_t *)((uint16_t)(v_stack_p80) + 0x48)))) >> (1);
    Arg2 = (*(uint16_t *)(local_rbx)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x8), Arg2, Arg6, Arg4);
    goto loc_0085D124;
loc_0085D1AE:
    if ((uint16_t)(result) != 0) goto loc_0085D27C;
    Arg4 = ((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x48)))) >> (1);
    Arg2 = (*(uint16_t *)(local_rbx)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_rbx + 0x8), Arg2, Arg6, Arg4);
    goto loc_0085D13C;
loc_0085D1E3:
    local_rsi = (uint16_t)((*(uint16_t *)((uint16_t)(v_stack_p80) + 0x48)) >> (1));
loc_0085D1F7:
    v_stack_pA0 = (uint16_t)(*(uint16_t *)((uint16_t)(result)));
    if ((uint16_t)(local_rsi) == 0) goto loc_0085D268;
    if ((uint16_t)(*(uint16_t *)((uint16_t)(result))) == 0) goto loc_0085D268;
    local_r15 = (Arg6) + (2);
    Arg1 = (*(uint64_t *)((uint16_t)(result) + 0x8)) + 1;
    v_stack_p38 = Arg1;
    if (((uint16_t)(*(uint16_t *)(arg6))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)((uint16_t)(result) + 0x8))))) goto loc_0085D25E;
    if (((uint16_t)(*(uint16_t *)(arg6))) < 97) goto loc_0085D235;
    if (((uint16_t)(*(uint16_t *)(arg6))) > 122) goto loc_0085D332;
    local_rbx = (uint16_t)((*(uint16_t *)(arg6)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085D235:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)((uint16_t)(result) + 0x8)))) < 97) goto loc_0085D247;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)((uint16_t)(result) + 0x8)))) > 122) goto loc_0085D34F;
    local_rdi = (uint16_t)((*(uint8_t *)(*(uint64_t *)((uint16_t)(result) + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085D247:
    local_rdi = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rdi))));
    if (condition_is_not_equal) goto loc_0085D270;
loc_0085D25E:
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    result = (uint16_t)((Arg5) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    goto loc_0085D1F7;
loc_0085D268:
    local_rdi = (uint32_t)(((uint16_t)(local_rsi)) - ((uint32_t)((uint16_t)(result))));
loc_0085D270:
    local_rdi = (uint32_t)(-(local_rdi));
    goto loc_0085CECE;
loc_0085D27C:
    local_r15 = (uint16_t)((local_r15) >> (1));
loc_0085D291:
    v_stack_pA0 = (uint16_t)(*(uint16_t *)(local_rdi));
    if ((uint16_t)(local_r15) == 0) goto loc_0085D305;
    if ((uint16_t)(*(uint16_t *)(local_rdi)) == 0) goto loc_0085D305;
    Arg3 = (Arg6) + (2);
    Arg1 = (*(uint64_t *)(local_rdi + 0x8)) + 1;
    v_stack_p30 = Arg3;
    v_stack_p38 = Arg1;
    if (((uint16_t)(*(uint16_t *)(arg6))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(local_rdi + 0x8))))) goto loc_0085D2FB;
    if (((uint16_t)(*(uint16_t *)(arg6))) < 97) goto loc_0085D2D1;
    if (((uint16_t)(*(uint16_t *)(arg6))) > 122) goto loc_0085D325;
    local_rbx = (uint16_t)((*(uint16_t *)(arg6)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085D2D1:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rdi + 0x8)))) < 97) goto loc_0085D2DF;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_rdi + 0x8)))) > 122) goto loc_0085D342;
    local_rdi = (uint16_t)((*(uint8_t *)(*(uint64_t *)(local_rdi + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0085D2DF:
    local_rdi = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rdi))));
    if (condition_is_not_equal) goto loc_0085D30E;
loc_0085D2FB:
    local_r15 = (uint16_t)((local_r15) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    result = (uint16_t)((Arg5) + ((uint16_t)((uint32_t)(0xFFE0ULL) + 31)));
    goto loc_0085D291;
loc_0085D305:
    local_rdi = (uint32_t)(((uint16_t)(local_r15)) - ((uint32_t)((uint16_t)(result))));
loc_0085D30E:
    local_rdi = (uint32_t)(-(local_rdi));
    goto loc_0085D008;
loc_0085D325:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rbx), Arg2, v_stack_p30, Arg4);
    goto loc_0085D2D1;
loc_0085D332:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), Arg2, v_stack_p30, Arg4);
    goto loc_0085D235;
loc_0085D342:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rdi), Arg2, v_stack_p30, Arg4);
    goto loc_0085D2DF;
loc_0085D34F:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), Arg2, v_stack_p30, Arg4);
    goto loc_0085D247;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg5` | `+ 0x0` | `16` | `R` |
| `Arg5` | `+ 0x0 + r12*8` | `64` | `R` |
| `Arg5` | `+ 0x4` | `64` | `R` |
| `Arg5` | `+ 0x4 + r12*4` | `32` | `R` |
| `Arg5` | `+ 0x4 + rax*4` | `32` | `R` |
| `Arg5` | `+ 0x4 + rax*8` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085CC40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
