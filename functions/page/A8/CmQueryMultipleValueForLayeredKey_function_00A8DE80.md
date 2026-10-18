# CmQueryMultipleValueForLayeredKey

- RVA: `0x00A8DE80`–`0x00A8E355` (길이 `1,237` bytes)
- VA: `0x0000000140A8DE80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B89C8`
- 디코드: `283`개 명령, `1,237/1,237` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8DED8` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00A8DEE2` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00A8DF03` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00A8DF2A` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x00A8DF5D` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00A8DF80` → [CmpLockKcbStackShared](../94/CmpLockKcbStackShared_function_00948000.md) (function, `0x00948000`)
- `0x00A8DF97` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x00A8E020` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00A8E034` → [CmpIsValueTombstone](../84/CmpIsValueTombstone_function_00849900.md) (function, `0x00849900`)
- `0x00A8E0C0` → [CmpGetValueData](../85/CmpGetValueData_function_00856DB0.md) (function, `0x00856DB0`)
- `0x00A8E0E4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A8E14E` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A8E17B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A8E190` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00A8E1C2` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x00A8E1E6` → [CmpGetKeyNodeForKcb](../85/CmpGetKeyNodeForKcb_function_00856480.md) (function, `0x00856480`)
- `0x00A8E208` → [CmpFindNameInListWithStatus](../84/CmpFindNameInListWithStatus_function_00846B80.md) (function, `0x00846B80`)
- `0x00A8E221` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00A8E23A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A8E244` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A8E24E` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A8E29D` → [CmpGetEffectiveKcbSemantics](../84/CmpGetEffectiveKcbSemantics_function_00848E20.md) (function, `0x00848E20`)
- `0x00A8E2D9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A8E319` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A8E339` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00A8E34B` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)

### Direct callers
- [CmQueryMultipleValueKey](../84/CmQueryMultipleValueKey_function_00846EC0.md) at `0x008473DD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00A8DF5D` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00A8DF97` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x00A8E0E4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A8E2D9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A8E319` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00A8E27D` → [sub_00B46510](../B4/Unknown_function_00B46510.md) (`tail-transfer`)
  - `0x00A8E2F9` → [sub_00B46510 + 0x21](../B4/Unknown_function_00B46510.md) (`tail-transfer`)
  - `0x00A8E305` → [sub_00B46510 + 0x21](../B4/Unknown_function_00B46510.md) (`tail-transfer`)
  - `0x00A8E30E` → [sub_00B46510 + 0x37](../B4/Unknown_function_00B46510.md) (`tail-transfer`)
  - `0x00A8E333` → [sub_00B46510 + 0x5F](../B4/Unknown_function_00B46510.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A8DE80  4C 8B DC                        mov r11, rsp
00A8DE83  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
00A8DE87  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
00A8DE8B  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
00A8DE8F  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00A8DE93  53                              push rbx
00A8DE94  56                              push rsi
00A8DE95  57                              push rdi
00A8DE96  41 54                           push r12
00A8DE98  41 55                           push r13
00A8DE9A  41 56                           push r14
00A8DE9C  41 57                           push r15
00A8DE9E  48 81 EC C0 00 00 00            sub rsp, 0xc0
00A8DEA5  48 8B D1                        mov rdx, rcx
00A8DEA8  33 DB                           xor ebx, ebx
00A8DEAA  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00A8DEAF  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00A8DEB4  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00A8DEB9  0F 57 C0                        xorps xmm0, xmm0
00A8DEBC  41 0F 11 43 90                  movups xmmword ptr [r11 - 0x70], xmm0
00A8DEC1  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
00A8DEC6  83 C8 FF                        or eax, 0xffffffff
00A8DEC9  66 41 89 43 92                  mov word ptr [r11 - 0x6e], ax
00A8DECE  44 8A F3                        mov r14b, bl
00A8DED1  8B F3                           mov esi, ebx
00A8DED3  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A8DED8  E8 33 80 DC FF                  call 0x140855f10
00A8DEDD  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00A8DEE2  E8 29 80 DC FF                  call 0x140855f10
00A8DEE7  44 8B EB                        mov r13d, ebx
00A8DEEA  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
00A8DEF2  44 8B FB                        mov r15d, ebx
00A8DEF5  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00A8DEFA  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
00A8DEFE  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00A8DF03  E8 08 80 DC FF                  call 0x140855f10
00A8DF08  44 8B E3                        mov r12d, ebx
00A8DF0B  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00A8DF0F  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
00A8DF13  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00A8DF17  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00A8DF1F  48 8B D0                        mov rdx, rax
00A8DF22  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00A8DF2A  E8 61 A4 DB FF                  call 0x140848390
00A8DF2F  8B F8                           mov edi, eax
00A8DF31  85 C0                           test eax, eax
00A8DF33  79 43                           jns 0x140a8df78
00A8DF35  4D 85 FF                        test r15, r15
00A8DF38  0F 85 CC 03 00 00               jne 0x140a8e30a
00A8DF3E  48 85 F6                        test rsi, rsi
00A8DF41  0F 85 DC 03 00 00               jne 0x140a8e323
00A8DF47  45 84 F6                        test r14b, r14b
00A8DF4A  0F 85 F3 03 00 00               jne 0x140a8e343
00A8DF50  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00A8DF58  48 85 C9                        test rcx, rcx
00A8DF5B  74 05                           je 0x140a8df62
00A8DF5D  E8 1E 7E 9E FF                  call 0x140475d80
00A8DF62  8B C7                           mov eax, edi
00A8DF64  48 81 C4 C0 00 00 00            add rsp, 0xc0
00A8DF6B  41 5F                           pop r15
00A8DF6D  41 5E                           pop r14
00A8DF6F  41 5D                           pop r13
00A8DF71  41 5C                           pop r12
00A8DF73  5F                              pop rdi
00A8DF74  5E                              pop rsi
00A8DF75  5B                              pop rbx
00A8DF76  C3                              ret
00A8DF77  CC                              int3
00A8DF78  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00A8DF80  E8 7B A0 EB FF                  call 0x140948000
00A8DF85  41 B6 01                        mov r14b, 1
00A8DF88  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
00A8DF8D  33 D2                           xor edx, edx
00A8DF8F  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00A8DF97  E8 34 B8 13 00                  call 0x140bc97d0
00A8DF9C  8B F8                           mov edi, eax
00A8DF9E  85 C0                           test eax, eax
00A8DFA0  78 93                           js 0x140a8df35
00A8DFA2  8B C3                           mov eax, ebx
00A8DFA4  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A8DFA8  3B 84 24 10 01 00 00            cmp eax, dword ptr [rsp + 0x110]
00A8DFAF  0F 83 2E 03 00 00               jae 0x140a8e2e3
00A8DFB5  48 8D 04 40                     lea rax, [rax + rax*2]
00A8DFB9  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00A8DFC1  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A8DFC9  48 8B 3C C1                     mov rdi, qword ptr [rcx + rax*8]
00A8DFCD  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00A8DFD2  0F B7 0F                        movzx ecx, word ptr [rdi]
00A8DFD5  66 85 C9                        test cx, cx
00A8DFD8  0F 85 9B 02 00 00               jne 0x140a8e279
00A8DFDE  83 4C 24 48 FF                  or dword ptr [rsp + 0x48], 0xffffffff
00A8DFE3  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00A8DFEB  0F B7 70 42                     movzx esi, word ptr [rax + 0x42]
00A8DFEF  66 85 F6                        test si, si
00A8DFF2  0F 89 A9 01 00 00               jns 0x140a8e1a1
00A8DFF8  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
00A8DFFD  41 83 FE FF                     cmp r14d, -1
00A8E001  0F 84 60 02 00 00               je 0x140a8e267
00A8E007  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00A8E00B  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A8E010  41 8B D6                        mov edx, r14d
00A8E013  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00A8E01A  0F 84 70 01 00 00               je 0x140a8e190
00A8E020  E8 3B 6C DC FF                  call 0x140854c60
00A8E025  48 8B F0                        mov rsi, rax
00A8E028  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A8E02D  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00A8E031  48 8B D0                        mov rdx, rax
00A8E034  E8 C7 B8 DB FF                  call 0x140849900
00A8E039  84 C0                           test al, al
00A8E03B  0F 85 76 02 00 00               jne 0x140a8e2b7
00A8E041  8B 42 04                        mov eax, dword ptr [rdx + 4]
00A8E044  8D B8 00 00 00 80               lea edi, [rax - 0x80000000]
00A8E04A  3D 00 00 00 80                  cmp eax, 0x80000000
00A8E04F  0F 42 F8                        cmovb edi, eax
00A8E052  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00A8E056  41 83 C4 03                     add r12d, 3
00A8E05A  B8 FC FF FF FF                  mov eax, 0xfffffffc
00A8E05F  44 23 E0                        and r12d, eax
00A8E062  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
00A8E066  83 C2 03                        add edx, 3
00A8E069  23 D0                           and edx, eax
00A8E06B  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
00A8E06F  38 5C 24 41                     cmp byte ptr [rsp + 0x41], bl
00A8E073  0F 85 21 01 00 00               jne 0x140a8e19a
00A8E079  41 8D 04 3C                     lea eax, [r12 + rdi]
00A8E07D  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A8E085  41 3B 00                        cmp eax, dword ptr [r8]
00A8E088  0F 87 0C 01 00 00               ja 0x140a8e19a
00A8E08E  41 3B C4                        cmp eax, r12d
00A8E091  0F 82 03 01 00 00               jb 0x140a8e19a
00A8E097  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A8E09C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A8E0A1  48 8D 44 24 42                  lea rax, [rsp + 0x42]
00A8E0A6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A8E0AB  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00A8E0B0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A8E0B5  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00A8E0BA  4C 8B C6                        mov r8, rsi
00A8E0BD  41 8B D6                        mov edx, r14d
00A8E0C0  E8 EB 8C DC FF                  call 0x140856db0
00A8E0C5  84 C0                           test al, al
00A8E0C7  0F 84 F1 01 00 00               je 0x140a8e2be
00A8E0CD  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
00A8E0D1  44 8B C7                        mov r8d, edi
00A8E0D4  41 8B CC                        mov ecx, r12d
00A8E0D7  48 03 8C 24 18 01 00 00         add rcx, qword ptr [rsp + 0x118]
00A8E0DF  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00A8E0E4  E8 57 87 C3 FF                  call 0x1406c6840
00A8E0E9  EB 20                           jmp 0x140a8e10b
00A8E0EB  8B F8                           mov edi, eax
00A8E0ED  33 DB                           xor ebx, ebx
00A8E0EF  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00A8E0F4  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00A8E0F9  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
00A8E101  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00A8E106  E9 2A FE FF FF                  jmp 0x140a8df35
00A8E10B  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
00A8E10E  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00A8E116  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
00A8E11E  89 44 CA 10                     mov dword ptr [rdx + rcx*8 + 0x10], eax
00A8E122  89 7C CA 08                     mov dword ptr [rdx + rcx*8 + 8], edi
00A8E126  44 89 64 CA 0C                  mov dword ptr [rdx + rcx*8 + 0xc], r12d
00A8E12B  44 03 E7                        add r12d, edi
00A8E12E  38 5C 24 42                     cmp byte ptr [rsp + 0x42], bl
00A8E132  0F 85 9A 01 00 00               jne 0x140a8e2d2
00A8E138  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00A8E13C  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A8E141  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00A8E148  0F 85 F6 00 00 00               jne 0x140a8e244
00A8E14E  E8 ED 7D DC FF                  call 0x140855f40
00A8E153  4C 8B FB                        mov r15, rbx
00A8E156  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00A8E15B  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
00A8E15F  03 D7                           add edx, edi
00A8E161  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
00A8E165  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00A8E169  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00A8E16E  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00A8E175  0F 85 BF 00 00 00               jne 0x140a8e23a
00A8E17B  E8 C0 7D DC FF                  call 0x140855f40
00A8E180  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
00A8E184  FF C0                           inc eax
00A8E186  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00A8E18B  E9 14 FE FF FF                  jmp 0x140a8dfa4
00A8E190  E8 1B 6B DC FF                  call 0x140854cb0
00A8E195  E9 8B FE FF FF                  jmp 0x140a8e025
00A8E19A  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
00A8E19F  EB BE                           jmp 0x140a8e15f
00A8E1A1  4C 0F BF F6                     movsx r14, si
00A8E1A5  66 83 FE 02                     cmp si, 2
00A8E1A9  0F 8D A6 00 00 00               jge 0x140a8e255
00A8E1AF  4E 8B B4 F4 90 00 00 00         mov r14, qword ptr [rsp + r14*8 + 0x90]
00A8E1B7  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00A8E1BF  49 8B CE                        mov rcx, r14
00A8E1C2  E8 59 AC DB FF                  call 0x140848e20
00A8E1C7  83 F8 01                        cmp eax, 1
00A8E1CA  0F 84 28 FE FF FF               je 0x140a8dff8
00A8E1D0  41 83 7E 28 FF                  cmp dword ptr [r14 + 0x28], -1
00A8E1D5  0F 84 A7 00 00 00               je 0x140a8e282
00A8E1DB  45 33 C0                        xor r8d, r8d
00A8E1DE  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00A8E1E3  49 8B CE                        mov rcx, r14
00A8E1E6  E8 95 82 DC FF                  call 0x140856480
00A8E1EB  48 8D 50 24                     lea rdx, [rax + 0x24]
00A8E1EF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00A8E1F4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A8E1F9  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A8E1FE  45 33 C9                        xor r9d, r9d
00A8E201  4C 8B C7                        mov r8, rdi
00A8E204  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00A8E208  E8 73 89 DB FF                  call 0x140846b80
00A8E20D  8B F8                           mov edi, eax
00A8E20F  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00A8E213  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00A8E218  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00A8E21F  75 2D                           jne 0x140a8e24e
00A8E221  E8 1A 7D DC FF                  call 0x140855f40
00A8E226  85 FF                           test edi, edi
00A8E228  78 60                           js 0x140a8e28a
00A8E22A  4D 8B EE                        mov r13, r14
00A8E22D  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
00A8E235  E9 BE FD FF FF                  jmp 0x140a8dff8
00A8E23A  E8 E1 E9 DC FF                  call 0x14085cc20
00A8E23F  E9 3C FF FF FF                  jmp 0x140a8e180
00A8E244  E8 D7 E9 DC FF                  call 0x14085cc20
00A8E249  E9 05 FF FF FF                  jmp 0x140a8e153
00A8E24E  E8 CD E9 DC FF                  call 0x14085cc20
00A8E253  EB D1                           jmp 0x140a8e226
00A8E255  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00A8E25D  4E 8B 74 F0 F0                  mov r14, qword ptr [rax + r14*8 - 0x10]
00A8E262  E9 50 FF FF FF                  jmp 0x140a8e1b7
00A8E267  BF 34 00 00 C0                  mov edi, 0xc0000034
00A8E26C  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00A8E271  48 8B F3                        mov rsi, rbx
00A8E274  E9 BC FC FF FF                  jmp 0x140a8df35
00A8E279  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A8E27D  E9 8E 82 0B 00                  jmp 0x140b46510
00A8E282  66 FF CE                        dec si
00A8E285  E9 65 FD FF FF                  jmp 0x140a8dfef
00A8E28A  81 FF 34 00 00 C0               cmp edi, 0xc0000034
00A8E290  75 DA                           jne 0x140a8e26c
00A8E292  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00A8E29A  49 8B CE                        mov rcx, r14
00A8E29D  E8 7E AB DB FF                  call 0x140848e20
00A8E2A2  85 C0                           test eax, eax
00A8E2A4  0F 85 4E FD FF FF               jne 0x140a8dff8
00A8E2AA  66 FF CE                        dec si
00A8E2AD  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00A8E2B2  E9 38 FD FF FF                  jmp 0x140a8dfef
00A8E2B7  BF 34 00 00 C0                  mov edi, 0xc0000034
00A8E2BC  EB 0A                           jmp 0x140a8e2c8
00A8E2BE  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A8E2C3  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00A8E2C8  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00A8E2CD  E9 63 FC FF FF                  jmp 0x140a8df35
00A8E2D2  33 D2                           xor edx, edx
00A8E2D4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A8E2D9  E8 92 45 0F 00                  call 0x140b82870
00A8E2DE  E9 70 FE FF FF                  jmp 0x140a8e153
00A8E2E3  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00A8E2EB  44 89 20                        mov dword ptr [rax], r12d
00A8E2EE  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
00A8E2F6  48 85 C0                        test rax, rax
00A8E2F9  0F 84 32 82 0B 00               je 0x140b46531
00A8E2FF  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00A8E303  89 08                           mov dword ptr [rax], ecx
00A8E305  E9 27 82 0B 00                  jmp 0x140b46531
00A8E30A  38 5C 24 42                     cmp byte ptr [rsp + 0x42], bl
00A8E30E  0F 84 33 82 0B 00               je 0x140b46547
00A8E314  33 D2                           xor edx, edx
00A8E316  49 8B CF                        mov rcx, r15
00A8E319  E8 52 45 0F 00                  call 0x140b82870
00A8E31E  E9 1B FC FF FF                  jmp 0x140a8df3e
00A8E323  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00A8E327  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00A8E32C  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00A8E333  0F 84 36 82 0B 00               je 0x140b4656f
00A8E339  E8 E2 E8 DC FF                  call 0x14085cc20
00A8E33E  E9 04 FC FF FF                  jmp 0x140a8df47
00A8E343  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00A8E34B  E8 10 A1 DB FF                  call 0x140848460
00A8E350  E9 FB FB FF FF                  jmp 0x140a8df50
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmQueryMultipleValueForLayeredKey(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB6;
    unsigned __int8 v_stack_mB7;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned int v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int64 v_stack_p42;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (192);
    v_rbx = 0;
    v_stack_mA8 = 0;
    v_stack_m88 = 0;
    v_stack_m98 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    *(unsigned __int16 *)(v_rsp - 110) = (unsigned __int16)(result);
    result = HvpGetCellContextInitialize(v_stack_mA8, a1, a3, a4);
    result = HvpGetCellContextInitialize(v_stack_m88, a1, a3, a4);
    v_stack_m78 = 0;
    v_stack_mA0 = 0;
    v_stack_mB6 = 0;
    result = HvpGetCellContextInitialize(v_stack_m98, a1, a3, a4);
    v_stack_mB4 = 0;
    v_stack_mB7 = 0;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 8);
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m70, *(unsigned __int64 *)(a1 + 8), a3, a4);
    if (!sign_flag) goto loc_00A8DF78;
loc_00A8DF35:
    if (0 != 0) goto loc_00A8E30A;
loc_00A8DF3E:
    if (0 != 0) goto loc_00A8E323;
loc_00A8DF47:
    if (0 != 0) goto loc_00A8E343;
loc_00A8DF50:
    if (v_stack_m58 != 0) {
        result = CmSiFreeMemory(v_stack_m58, *(unsigned __int64 *)(a1 + 8), a3, a4);
    }
    v_rsp = (v_rsp) + (192);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A8DF78:
    result = CmpLockKcbStackShared(v_stack_p88, *(unsigned __int64 *)(a1 + 8), a3, a4);
    v_stack_p40 = 1;
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_p100, a2, a3, a4);
    if (sign_flag) goto loc_00A8DF35;
loc_00A8DFA4:
    v_stack_p68 = 0;
    if (0 >= v_stack_p110) goto loc_00A8E2E3;
    v_stack_pB0 = 0 + 0 * 2;
    v_stack_p78 = *(unsigned __int64 *)(v_stack_p108 + 0 + 0 * 2 * 8);
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p108 + 0 + 0 * 2 * 8))) != 0) goto loc_00A8E279;
loc_00A8DFEF:
    if (!sign_flag) goto loc_00A8E1A1;
loc_00A8DFF8:
    if (((unsigned int)((unsigned int)(v_stack_p48))) == -1) goto loc_00A8E267;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 32) + 140)) & (1)) == 0) goto loc_00A8E190;
    result = HvpGetCellFlat(*(unsigned __int64 *)(0 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), v_stack_p50, a4);
loc_00A8E025:
    v_stack_p78 = result;
    result = CmpIsValueTombstone(*(unsigned __int64 *)(0 + 32), result, v_stack_p50, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A8E2B7;
    v_rdi = (unsigned int)(*(unsigned int *)(result + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < 0x80000000ULL) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4))); }
    v_stack_p48 = (unsigned int)(v_rdi);
    v_r12 = (unsigned int)((0) + (3));
    v_r12 = (unsigned int)((v_r12) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    a2 = (unsigned int)(((unsigned int)(v_stack_p44)) + (3));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_stack_p44 = (unsigned int)(a2);
    if (v_stack_p41 != 0) goto loc_00A8E19A;
    if (((unsigned int)(v_r12 + v_rdi * 1)) > (*(unsigned int *)(a5))) goto loc_00A8E19A;
    if (((unsigned int)(v_r12 + v_rdi * 1)) < ((unsigned int)(v_r12))) goto loc_00A8E19A;
    v_stack_p30 = v_stack_p60;
    v_stack_p28 = v_stack_p42;
    v_stack_p20 = v_stack_p58;
    result = CmpGetValueData(*(unsigned __int64 *)(0 + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), result, v_stack_p48);
    if ((unsigned __int8)(result) == 0) goto loc_00A8E2BE;
    a1 = ((unsigned int)((unsigned int)(v_r12))) + (v_stack_p118);
    result = memcpy(a1, v_stack_p58, (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), v_stack_p48);
    goto loc_00A8E10B;
loc_00A8E10B:
    *(unsigned int *)(v_stack_p108 + v_stack_pB0 * 8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    *(unsigned int *)(v_stack_p108 + v_stack_pB0 * 8 + 8) = (unsigned int)((unsigned int)(v_stack_p48));
    *(unsigned int *)(v_stack_p108 + v_stack_pB0 * 8 + 12) = (unsigned int)(v_r12);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)((unsigned int)(v_stack_p48))));
    if (v_stack_p42 != 0) goto loc_00A8E2D2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 32) + 140)) & (1)) != 0) goto loc_00A8E244;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(0 + 32), v_stack_p60, (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), v_stack_p48);
loc_00A8E153:
    v_stack_p58 = 0;
loc_00A8E15F:
    a2 = (unsigned int)(((unsigned int)(v_stack_p44)) + ((unsigned int)((unsigned int)(v_stack_p48))));
    v_stack_p44 = (unsigned int)(a2);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(0 + 32) + 140)) & (1)) != 0) goto loc_00A8E23A;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(0 + 32), v_stack_p50, (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), v_stack_p48);
loc_00A8E180:
    result = (unsigned int)(((unsigned int)(v_stack_p68)) + 1);
    goto loc_00A8DFA4;
loc_00A8E190:
    result = HvpGetCellPaged(*(unsigned __int64 *)(0 + 32), v_stack_p50, (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), v_stack_p48);
    goto loc_00A8E025;
loc_00A8E19A:
    v_stack_p41 = 1;
    goto loc_00A8E15F;
loc_00A8E1A1:
    if (((unsigned __int16)(result)) >= 2) goto loc_00A8E255;
loc_00A8E1B7:
    result = CmpGetEffectiveKcbSemantics(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144), v_stack_p100, (unsigned int)((unsigned int)((unsigned int)(v_stack_p48))), v_stack_p48);
    if (((unsigned int)(result)) == 1) goto loc_00A8DFF8;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 40)) == -1) goto loc_00A8E282;
    a3 = 0;
    result = CmpGetKeyNodeForKcb(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144), v_stack_p70, a3, v_stack_p48);
    v_stack_p28 = v_stack_p48;
    v_stack_p20 = 0;
    a4 = 0;
    result = CmpFindNameInListWithStatus(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32), result + 36, (unsigned int)(v_stack_p48), a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32) + 140)) & (1)) != 0) goto loc_00A8E24E;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32), v_stack_p70, (unsigned int)(v_stack_p48), a4);
loc_00A8E226:
    if (sign_flag) goto loc_00A8E28A;
    v_stack_p80 = *(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144);
    goto loc_00A8DFF8;
loc_00A8E23A:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32), v_stack_p70, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8E180;
loc_00A8E244:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32), v_stack_p70, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8E153;
loc_00A8E24E:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32), v_stack_p70, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8E226;
loc_00A8E255:
    goto loc_00A8E1B7;
loc_00A8E267:
loc_00A8E26C:
    goto loc_00A8DF35;
loc_00A8E279:
loc_00A8E282:
    v_rsi = (unsigned __int16)((0) - 1);
    goto loc_00A8DFEF;
loc_00A8E28A:
    if (((unsigned int)((unsigned int)(0xC0000034ULL))) != 0xC0000034ULL) goto loc_00A8E26C;
    result = CmpGetEffectiveKcbSemantics(v_stack_p40, v_stack_p100, (unsigned int)(v_stack_p48), a4);
    if ((unsigned int)(result) != 0) goto loc_00A8DFF8;
    v_rsi = (unsigned __int16)((v_rsi) - 1);
    goto loc_00A8DFEF;
loc_00A8E2B7:
    goto loc_00A8E2C8;
loc_00A8E2BE:
loc_00A8E2C8:
    goto loc_00A8DF35;
loc_00A8E2D2:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, a2, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8E153;
loc_00A8E2E3:
    *(unsigned int *)(a5) = (unsigned int)(v_r12);
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(v_stack_p44));
loc_00A8E30A:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, a2, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8DF3E;
loc_00A8E323:
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (__int16)((unsigned __int16)(result)) * 8 + 144) + 32), v_stack_p50, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8DF47;
loc_00A8E343:
    result = CmpUnlockKcbStack(v_stack_p88, v_stack_p50, (unsigned int)(v_stack_p48), a4);
    goto loc_00A8DF50;
}
```

## 5. (Beta) C Style

```c
int64_t CmQueryMultipleValueForLayeredKey(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB6;
    uint8_t v_stack_mB7;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint32_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint64_t v_stack_p42;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (192);
    local_rbx = 0;
    v_stack_mA8 = 0;
    v_stack_m88 = 0;
    v_stack_m98 = 0;
    *(uint64_t *)(local_rsp - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    *(uint16_t *)(local_rsp - 0x6E) = (uint16_t)(result);
    result = HvpGetCellContextInitialize(v_stack_mA8, Arg1, Arg3, Arg4);
    result = HvpGetCellContextInitialize(v_stack_m88, Arg1, Arg3, Arg4);
    v_stack_m78 = 0;
    v_stack_mA0 = 0;
    v_stack_mB6 = 0;
    result = HvpGetCellContextInitialize(v_stack_m98, Arg1, Arg3, Arg4);
    v_stack_mB4 = 0;
    v_stack_mB7 = 0;
    v_stack_m50 = *(uint64_t *)(Arg1 + 0x8);
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m70, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    if (!sign_flag) goto loc_00A8DF78;
loc_00A8DF35:
    if (0 != 0) goto loc_00A8E30A;
loc_00A8DF3E:
    if (0 != 0) goto loc_00A8E323;
loc_00A8DF47:
    if (0 != 0) goto loc_00A8E343;
loc_00A8DF50:
    if (v_stack_m58 != 0) {
        result = CmSiFreeMemory(v_stack_m58, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (192);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A8DF78:
    result = CmpLockKcbStackShared(v_stack_p88, *(uint64_t *)(Arg1 + 0x8), Arg3, Arg4);
    v_stack_p40 = 1;
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_p100, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00A8DF35;
loc_00A8DFA4:
    v_stack_p68 = 0;
    if (0 >= v_stack_p110) goto loc_00A8E2E3;
    v_stack_pB0 = 0 + 0 * 2;
    v_stack_p78 = *(uint64_t *)(v_stack_p108 + 0x0 + 0x0 * 2 * 8);
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p108 + 0x0 + 0x0 * 2 * 8))) != 0) goto loc_00A8E279;
loc_00A8DFEF:
    if (!sign_flag) goto loc_00A8E1A1;
loc_00A8DFF8:
    if (((uint32_t)((uint32_t)(v_stack_p48))) == -1) goto loc_00A8E267;
    if (((*(uint8_t *)(*(uint64_t *)(0 + 0x20) + 0x8C)) & (1)) == 0) goto loc_00A8E190;
    result = HvpGetCellFlat(*(uint64_t *)(0 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), v_stack_p50, Arg4);
loc_00A8E025:
    v_stack_p78 = result;
    result = CmpIsValueTombstone(*(uint64_t *)(0 + 0x20), result, v_stack_p50, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A8E2B7;
    local_rdi = (uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < 0x80000000ULL) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))); }
    v_stack_p48 = (uint32_t)(local_rdi);
    local_r12 = (uint32_t)((0) + (3));
    local_r12 = (uint32_t)((local_r12) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p44)) + (3));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    v_stack_p44 = (uint32_t)(Arg2);
    if (v_stack_p41 != 0) goto loc_00A8E19A;
    if (((uint32_t)(local_r12 + local_rdi * 1)) > (*(uint32_t *)(arg5))) goto loc_00A8E19A;
    if (((uint32_t)(local_r12 + local_rdi * 1)) < ((uint32_t)(local_r12))) goto loc_00A8E19A;
    v_stack_p30 = v_stack_p60;
    v_stack_p28 = v_stack_p42;
    v_stack_p20 = v_stack_p58;
    result = CmpGetValueData(*(uint64_t *)(0 + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), result, v_stack_p48);
    if ((uint8_t)(result) == 0) goto loc_00A8E2BE;
    Arg1 = ((uint32_t)((uint32_t)(local_r12))) + (v_stack_p118);
    result = memcpy(Arg1, v_stack_p58, (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), v_stack_p48);
    goto loc_00A8E10B;
loc_00A8E10B:
    *(uint32_t *)(v_stack_p108 + v_stack_pB0 * 8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    *(uint32_t *)(v_stack_p108 + v_stack_pB0 * 8 + 0x8) = (uint32_t)((uint32_t)(v_stack_p48));
    *(uint32_t *)(v_stack_p108 + v_stack_pB0 * 8 + 0xC) = (uint32_t)(local_r12);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)((uint32_t)(v_stack_p48))));
    if (v_stack_p42 != 0) goto loc_00A8E2D2;
    if (((*(uint8_t *)(*(uint64_t *)(0 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A8E244;
    result = HvpReleaseCellPaged(*(uint64_t *)(0 + 0x20), v_stack_p60, (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), v_stack_p48);
loc_00A8E153:
    v_stack_p58 = 0;
loc_00A8E15F:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p44)) + ((uint32_t)((uint32_t)(v_stack_p48))));
    v_stack_p44 = (uint32_t)(Arg2);
    if (((*(uint8_t *)(*(uint64_t *)(0 + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A8E23A;
    result = HvpReleaseCellPaged(*(uint64_t *)(0 + 0x20), v_stack_p50, (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), v_stack_p48);
loc_00A8E180:
    result = (uint32_t)(((uint32_t)(v_stack_p68)) + 1);
    goto loc_00A8DFA4;
loc_00A8E190:
    result = HvpGetCellPaged(*(uint64_t *)(0 + 0x20), v_stack_p50, (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), v_stack_p48);
    goto loc_00A8E025;
loc_00A8E19A:
    v_stack_p41 = 1;
    goto loc_00A8E15F;
loc_00A8E1A1:
    if (((uint16_t)(result)) >= 2) goto loc_00A8E255;
loc_00A8E1B7:
    result = CmpGetEffectiveKcbSemantics(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90), v_stack_p100, (uint32_t)((uint32_t)((uint32_t)(v_stack_p48))), v_stack_p48);
    if (((uint32_t)(result)) == 1) goto loc_00A8DFF8;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x28)) == -1) goto loc_00A8E282;
    Arg3 = 0;
    result = CmpGetKeyNodeForKcb(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90), v_stack_p70, Arg3, v_stack_p48);
    v_stack_p28 = v_stack_p48;
    v_stack_p20 = 0;
    Arg4 = 0;
    result = CmpFindNameInListWithStatus(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20), result + 36, (uint32_t)(v_stack_p48), Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20) + 0x8C)) & (1)) != 0) goto loc_00A8E24E;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20), v_stack_p70, (uint32_t)(v_stack_p48), Arg4);
loc_00A8E226:
    if (sign_flag) goto loc_00A8E28A;
    v_stack_p80 = *(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90);
    goto loc_00A8DFF8;
loc_00A8E23A:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20), v_stack_p70, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8E180;
loc_00A8E244:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20), v_stack_p70, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8E153;
loc_00A8E24E:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20), v_stack_p70, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8E226;
loc_00A8E255:
    goto loc_00A8E1B7;
loc_00A8E267:
loc_00A8E26C:
    goto loc_00A8DF35;
loc_00A8E279:
loc_00A8E282:
    local_rsi = (uint16_t)((0) - 1);
    goto loc_00A8DFEF;
loc_00A8E28A:
    if (((uint32_t)((uint32_t)(0xC0000034ULL))) != 0xC0000034ULL) goto loc_00A8E26C;
    result = CmpGetEffectiveKcbSemantics(v_stack_p40, v_stack_p100, (uint32_t)(v_stack_p48), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A8DFF8;
    local_rsi = (uint16_t)((local_rsi) - 1);
    goto loc_00A8DFEF;
loc_00A8E2B7:
    goto loc_00A8E2C8;
loc_00A8E2BE:
loc_00A8E2C8:
    goto loc_00A8DF35;
loc_00A8E2D2:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, Arg2, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8E153;
loc_00A8E2E3:
    *(uint32_t *)(arg5) = (uint32_t)(local_r12);
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(v_stack_p44));
loc_00A8E30A:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, Arg2, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8DF3E;
loc_00A8E323:
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp + (int16_t)((uint16_t)(result)) * 8 + 0x90) + 0x20), v_stack_p50, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8DF47;
loc_00A8E343:
    result = CmpUnlockKcbStack(v_stack_p88, v_stack_p50, (uint32_t)(v_stack_p48), Arg4);
    goto loc_00A8DF50;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8DE80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
