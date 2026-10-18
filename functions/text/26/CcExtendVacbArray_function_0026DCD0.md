# CcExtendVacbArray

- RVA: `0x0026DCD0`–`0x0026E1B2` (길이 `1,250` bytes)
- VA: `0x000000014026DCD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000656B4`
- 디코드: `338`개 명령, `1,250/1,250` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0026DDCA` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (function, `0x00B82010`)
- `0x0026DDE7` → [CcAcquireBcbLockAndVacbLock](CcAcquireBcbLockAndVacbLock_function_0026FC58.md) (function, `0x0026FC58`)
- `0x0026DE02` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0026DE15` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026DE47` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x0026DE5F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0026DE7D` → [CcFreeUnusedVacbLevels](../27/CcFreeUnusedVacbLevels_function_00273B1C.md) (function, `0x00273B1C`)
- `0x0026DFA9` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x0026DFC0` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x0026DFDA` → [ExAllocateFromNPagedLookasideList](../38/ExAllocateFromNPagedLookasideList_function_0038E6C0.md) (function, `0x0038E6C0`)
- `0x0026DFE8` → [CcFreeUnusedVacbLevels](../27/CcFreeUnusedVacbLevels_function_00273B1C.md) (function, `0x00273B1C`)
- `0x0026DFF8` → [CcAcquireBcbLockAndVacbLock](CcAcquireBcbLockAndVacbLock_function_0026FC58.md) (function, `0x0026FC58`)
- `0x0026E014` → [VacbLevelReference](VacbLevelReference_function_0026DCA0.md) (function, `0x0026DCA0`)
- `0x0026E035` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x0026E07F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026E098` → [VacbLevelReference](VacbLevelReference_function_0026DCA0.md) (function, `0x0026DCA0`)
- `0x0026E0C4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0026E160` → [CcCalculateVacbLevelLockCount](CcCalculateVacbLevelLockCount_function_0026CFC8.md) (function, `0x0026CFC8`)
- `0x0026E180` → [CcAllocateVacbLevel](../48/CcAllocateVacbLevel_function_004885C4.md) (function, `0x004885C4`)
- `0x0026E1A8` → [ExFreeToNPagedLookasideList](../38/ExFreeToNPagedLookasideList_function_0038D9D0.md) (function, `0x0038D9D0`)

### Direct callers
- [CcSetFileSizesEx](CcSetFileSizesEx_function_0026D070.md) at `0x0026D2C3`

### Static image references
- `0x0026DFAE` → RVA `0x00E0A894` (`.data`; read)
- `0x0026DFD3` → RVA `0x00E11A80` (`.data`; read)
- `0x0026E14E` → RVA `0x00E0A894` (`.data`; write)
- `0x0026E189` → RVA `0x00E11B80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0026DDCA` → [ExAllocatePoolWithTag](../../poolcode/B8/ExAllocatePoolWithTag_function_00B82010.md) (`.text` → `POOLCODE`)
  - `0x0026DE5F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0026E12E` → [sub_006D9DD0](../6D/Unknown_function_006D9DD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0026DCD0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0026DCD5  55                              push rbp
0026DCD6  56                              push rsi
0026DCD7  57                              push rdi
0026DCD8  41 54                           push r12
0026DCDA  41 55                           push r13
0026DCDC  41 56                           push r14
0026DCDE  41 57                           push r15
0026DCE0  48 8B EC                        mov rbp, rsp
0026DCE3  48 83 EC 50                     sub rsp, 0x50
0026DCE7  45 33 E4                        xor r12d, r12d
0026DCEA  48 8B C2                        mov rax, rdx
0026DCED  44 21 65 FC                     and dword ptr [rbp - 4], r12d
0026DCF1  48 8B DA                        mov rbx, rdx
0026DCF4  48 C1 E8 20                     shr rax, 0x20
0026DCF8  48 8B F9                        mov rdi, rcx
0026DCFB  85 C0                           test eax, eax
0026DCFD  0F 88 EA 01 00 00               js 0x14026deed
0026DD03  41 BA 00 02 00 00               mov r10d, 0x200
0026DD09  45 8D 6C 24 01                  lea r13d, [r12 + 1]
0026DD0E  44 85 91 98 00 00 00            test dword ptr [rcx + 0x98], r10d
0026DD15  0F 85 D9 01 00 00               jne 0x14026def4
0026DD1B  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
0026DD20  48 8D 45 E0                     lea rax, [rbp - 0x20]
0026DD24  83 65 F8 00                     and dword ptr [rbp - 8], 0
0026DD28  4C 8B 71 20                     mov r14, qword ptr [rcx + 0x20]
0026DD2C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0026DD30  48 8D 45 E0                     lea rax, [rbp - 0x20]
0026DD34  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0026DD38  49 3B DE                        cmp rbx, r14
0026DD3B  0F 8E 38 01 00 00               jle 0x14026de79
0026DD41  41 83 CB FF                     or r11d, 0xffffffff
0026DD45  41 B9 00 00 00 02               mov r9d, 0x2000000
0026DD4B  4D 3B F1                        cmp r14, r9
0026DD4E  0F 8D 20 01 00 00               jge 0x14026de74
0026DD54  49 3B D9                        cmp rbx, r9
0026DD57  4C 8B F3                        mov r14, rbx
0026DD5A  BA 00 00 10 00                  mov edx, 0x100000
0026DD5F  41 B8 20 00 00 00               mov r8d, 0x20
0026DD65  4D 0F 4D F1                     cmovge r14, r9
0026DD69  49 8B C6                        mov rax, r14
0026DD6C  48 C1 E8 20                     shr rax, 0x20
0026DD70  85 C0                           test eax, eax
0026DD72  75 0E                           jne 0x14026dd82
0026DD74  44 3B F2                        cmp r14d, edx
0026DD77  0F 87 20 01 00 00               ja 0x14026de9d
0026DD7D  41 8B C8                        mov ecx, r8d
0026DD80  EB 03                           jmp 0x14026dd85
0026DD82  41 8B CB                        mov ecx, r11d
0026DD85  83 7F 24 00                     cmp dword ptr [rdi + 0x24], 0
0026DD89  89 4D 48                        mov dword ptr [rbp + 0x48], ecx
0026DD8C  75 10                           jne 0x14026dd9e
0026DD8E  8B 77 20                        mov esi, dword ptr [rdi + 0x20]
0026DD91  3B F2                           cmp esi, edx
0026DD93  0F 87 12 01 00 00               ja 0x14026deab
0026DD99  41 8B F0                        mov esi, r8d
0026DD9C  EB 03                           jmp 0x14026dda1
0026DD9E  41 8B F3                        mov esi, r11d
0026DDA1  3B CE                           cmp ecx, esi
0026DDA3  0F 86 C7 00 00 00               jbe 0x14026de70
0026DDA9  45 85 E4                        test r12d, r12d
0026DDAC  0F 85 4B 03 00 00               jne 0x14026e0fd
0026DDB2  8D 41 08                        lea eax, [rcx + 8]
0026DDB5  49 3B D9                        cmp rbx, r9
0026DDB8  41 B8 43 63 56 70               mov r8d, 0x70566343
0026DDBE  0F 4C C1                        cmovl eax, ecx
0026DDC1  41 8B CA                        mov ecx, r10d
0026DDC4  8B D0                           mov edx, eax
0026DDC6  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0026DDCA  E8 41 42 91 00                  call 0x140b82010
0026DDCF  4C 8B E8                        mov r13, rax
0026DDD2  48 85 C0                        test rax, rax
0026DDD5  75 0A                           jne 0x14026dde1
0026DDD7  B8 9A 00 00 C0                  mov eax, 0xc000009a
0026DDDC  E9 A3 00 00 00                  jmp 0x14026de84
0026DDE1  48 8B D7                        mov rdx, rdi
0026DDE4  41 8B CC                        mov ecx, r12d
0026DDE7  E8 6C 1E 00 00                  call 0x14026fc58
0026DDEC  4C 8B 7F 58                     mov r15, qword ptr [rdi + 0x58]
0026DDF0  4D 85 FF                        test r15, r15
0026DDF3  0F 84 0B 01 00 00               je 0x14026df04
0026DDF9  44 8B C6                        mov r8d, esi
0026DDFC  49 8B D7                        mov rdx, r15
0026DDFF  49 8B CD                        mov rcx, r13
0026DE02  E8 39 8A 45 00                  call 0x1406c6840
0026DE07  44 8B 45 48                     mov r8d, dword ptr [rbp + 0x48]
0026DE0B  33 D2                           xor edx, edx
0026DE0D  8B CE                           mov ecx, esi
0026DE0F  44 2B C6                        sub r8d, esi
0026DE12  49 03 CD                        add rcx, r13
0026DE15  E8 26 8E 45 00                  call 0x1406c6c40
0026DE1A  48 81 FB 00 00 00 02            cmp rbx, 0x2000000
0026DE21  7C 0D                           jl 0x14026de30
0026DE23  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0026DE27  83 C1 F8                        add ecx, -8
0026DE2A  33 C0                           xor eax, eax
0026DE2C  4A 89 04 29                     mov qword ptr [rcx + r13], rax
0026DE30  45 85 E4                        test r12d, r12d
0026DE33  0F 85 D2 00 00 00               jne 0x14026df0b
0026DE39  48 8B D7                        mov rdx, rdi
0026DE3C  4C 89 6F 58                     mov qword ptr [rdi + 0x58], r13
0026DE40  41 8B CC                        mov ecx, r12d
0026DE43  4C 89 77 20                     mov qword ptr [rdi + 0x20], r14
0026DE47  E8 A4 1F 07 00                  call 0x1402dfdf0
0026DE4C  48 8D 47 38                     lea rax, [rdi + 0x38]
0026DE50  4C 3B F8                        cmp r15, rax
0026DE53  74 0F                           je 0x14026de64
0026DE55  4D 85 FF                        test r15, r15
0026DE58  74 0A                           je 0x14026de64
0026DE5A  33 D2                           xor edx, edx
0026DE5C  49 8B CF                        mov rcx, r15
0026DE5F  E8 0C 4A 91 00                  call 0x140b82870
0026DE64  41 BD 01 00 00 00               mov r13d, 1
0026DE6A  41 B9 00 00 00 02               mov r9d, 0x2000000
0026DE70  4C 89 77 20                     mov qword ptr [rdi + 0x20], r14
0026DE74  49 3B DE                        cmp rbx, r14
0026DE77  7F 3D                           jg 0x14026deb6
0026DE79  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0026DE7D  E8 9A 5C 00 00                  call 0x140273b1c
0026DE82  33 C0                           xor eax, eax
0026DE84  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0026DE8C  48 83 C4 50                     add rsp, 0x50
0026DE90  41 5F                           pop r15
0026DE92  41 5E                           pop r14
0026DE94  41 5D                           pop r13
0026DE96  41 5C                           pop r12
0026DE98  5F                              pop rdi
0026DE99  5E                              pop rsi
0026DE9A  5D                              pop rbp
0026DE9B  C3                              ret
0026DE9C  CC                              int3
0026DE9D  41 8B CE                        mov ecx, r14d
0026DEA0  C1 E9 12                        shr ecx, 0x12
0026DEA3  C1 E1 03                        shl ecx, 3
0026DEA6  E9 DA FE FF FF                  jmp 0x14026dd85
0026DEAB  C1 EE 12                        shr esi, 0x12
0026DEAE  C1 E6 03                        shl esi, 3
0026DEB1  E9 EB FE FF FF                  jmp 0x14026dda1
0026DEB6  41 8B F5                        mov esi, r13d
0026DEB9  B9 19 00 00 00                  mov ecx, 0x19
0026DEBE  4D 3B F1                        cmp r14, r9
0026DEC1  7E 11                           jle 0x14026ded4
0026DEC3  83 C1 07                        add ecx, 7
0026DEC6  49 8B C5                        mov rax, r13
0026DEC9  48 D3 E0                        shl rax, cl
0026DECC  41 03 F5                        add esi, r13d
0026DECF  4C 3B F0                        cmp r14, rax
0026DED2  7F EF                           jg 0x14026dec3
0026DED4  48 8D 43 FF                     lea rax, [rbx - 1]
0026DED8  44 8B FE                        mov r15d, esi
0026DEDB  48 D3 F8                        sar rax, cl
0026DEDE  48 85 C0                        test rax, rax
0026DEE1  0F 85 4C 02 00 00               jne 0x14026e133
0026DEE7  48 89 5F 20                     mov qword ptr [rdi + 0x20], rbx
0026DEEB  EB 8C                           jmp 0x14026de79
0026DEED  B8 40 00 00 C0                  mov eax, 0xc0000040
0026DEF2  EB 90                           jmp 0x14026de84
0026DEF4  48 81 FB 00 00 20 00            cmp rbx, 0x200000
0026DEFB  45 0F 4F E5                     cmovg r12d, r13d
0026DEFF  E9 17 FE FF FF                  jmp 0x14026dd1b
0026DF04  33 F6                           xor esi, esi
0026DF06  E9 FC FE FF FF                  jmp 0x14026de07
0026DF0B  44 8B 45 48                     mov r8d, dword ptr [rbp + 0x48]
0026DF0F  33 C0                           xor eax, eax
0026DF11  48 81 7F 20 00 00 20 00         cmp qword ptr [rdi + 0x20], 0x200000
0026DF19  41 BB 00 00 08 00               mov r11d, 0x80000
0026DF1F  4B 8D 0C 28                     lea rcx, [r8 + r13]
0026DF23  0F 8F E1 01 00 00               jg 0x14026e10a
0026DF29  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0026DF2D  4C 8D 4F 10                     lea r9, [rdi + 0x10]
0026DF31  4D 8B C1                        mov r8, r9
0026DF34  49 3B D1                        cmp rdx, r9
0026DF37  0F 85 A2 01 00 00               jne 0x14026e0df
0026DF3D  49 3B C6                        cmp rax, r14
0026DF40  0F 8D F3 FE FF FF               jge 0x14026de39
0026DF46  49 8B 10                        mov rdx, qword ptr [r8]
0026DF49  4C 39 42 08                     cmp qword ptr [rdx + 8], r8
0026DF4D  75 24                           jne 0x14026df73
0026DF4F  48 89 11                        mov qword ptr [rcx], rdx
0026DF52  49 03 C3                        add rax, r11
0026DF55  4C 89 41 08                     mov qword ptr [rcx + 8], r8
0026DF59  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0026DF5D  49 89 08                        mov qword ptr [r8], rcx
0026DF60  48 83 C1 10                     add rcx, 0x10
0026DF64  EB D7                           jmp 0x14026df3d
0026DF66  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0026DF6A  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0026DF6E  48 39 11                        cmp qword ptr [rcx], rdx
0026DF71  74 07                           je 0x14026df7a
0026DF73  B9 03 00 00 00                  mov ecx, 3
0026DF78  CD 29                           int 0x29
0026DF7A  48 89 48 08                     mov qword ptr [rax + 8], rcx
0026DF7E  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0026DF82  48 89 10                        mov qword ptr [rax], rdx
0026DF85  48 89 01                        mov qword ptr [rcx], rax
0026DF88  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0026DF8C  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0026DF8F  41 03 C5                        add eax, r13d
0026DF92  89 45 F8                        mov dword ptr [rbp - 8], eax
0026DF95  EB 37                           jmp 0x14026dfce
0026DF97  44 3B FE                        cmp r15d, esi
0026DF9A  0F 86 47 FF FF FF               jbe 0x14026dee7
0026DFA0  41 BE 04 00 00 00               mov r14d, 4
0026DFA6  41 8B CE                        mov ecx, r14d
0026DFA9  E8 D2 5D 00 00                  call 0x140273d80
0026DFAE  44 3B 3D DF C8 B9 00            cmp r15d, dword ptr [rip + 0xb9c8df]
0026DFB5  0F 83 8F 01 00 00               jae 0x14026e14a
0026DFBB  8A D0                           mov dl, al
0026DFBD  49 8B CE                        mov rcx, r14
0026DFC0  E8 7B 45 00 00                  call 0x140272540
0026DFC5  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0026DFC8  45 8B F7                        mov r14d, r15d
0026DFCB  44 2B F6                        sub r14d, esi
0026DFCE  44 3B F0                        cmp r14d, eax
0026DFD1  76 1F                           jbe 0x14026dff2
0026DFD3  48 8D 0D A6 3A BA 00            lea rcx, [rip + 0xba3aa6]
0026DFDA  E8 E1 06 12 00                  call 0x14038e6c0
0026DFDF  48 85 C0                        test rax, rax
0026DFE2  75 82                           jne 0x14026df66
0026DFE4  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0026DFE8  E8 2F 5B 00 00                  call 0x140273b1c
0026DFED  E9 E5 FD FF FF                  jmp 0x14026ddd7
0026DFF2  48 8B D7                        mov rdx, rdi
0026DFF5  41 8B CC                        mov ecx, r12d
0026DFF8  E8 5B 1C 00 00                  call 0x14026fc58
0026DFFD  41 3B F5                        cmp esi, r13d
0026E000  0F 84 53 01 00 00               je 0x14026e159
0026E006  4C 8B 77 58                     mov r14, qword ptr [rdi + 0x58]
0026E00A  44 8D 46 FF                     lea r8d, [rsi - 1]
0026E00E  49 8B D6                        mov rdx, r14
0026E011  48 8B CF                        mov rcx, rdi
0026E014  E8 87 FC FF FF                  call 0x14026dca0
0026E019  8B 08                           mov ecx, dword ptr [rax]
0026E01B  8B 40 04                        mov eax, dword ptr [rax + 4]
0026E01E  0B C1                           or eax, ecx
0026E020  75 1D                           jne 0x14026e03f
0026E022  41 3B F5                        cmp esi, r13d
0026E025  0F 84 3F 01 00 00               je 0x14026e16a
0026E02B  48 8B D7                        mov rdx, rdi
0026E02E  48 89 5F 20                     mov qword ptr [rdi + 0x20], rbx
0026E032  41 8B CC                        mov ecx, r12d
0026E035  E8 B6 1D 07 00                  call 0x1402dfdf0
0026E03A  E9 A8 FE FF FF                  jmp 0x14026dee7
0026E03F  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
0026E043  48 8D 45 E0                     lea rax, [rbp - 0x20]
0026E047  41 03 F5                        add esi, r13d
0026E04A  4C 3B F0                        cmp r14, rax
0026E04D  74 5C                           je 0x14026e0ab
0026E04F  49 8B 0E                        mov rcx, qword ptr [r14]
0026E052  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
0026E056  0F 85 17 FF FF FF               jne 0x14026df73
0026E05C  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0026E060  4C 39 30                        cmp qword ptr [rax], r14
0026E063  0F 85 0A FF FF FF               jne 0x14026df73
0026E069  48 89 08                        mov qword ptr [rax], rcx
0026E06C  33 D2                           xor edx, edx
0026E06E  48 89 41 08                     mov qword ptr [rcx + 8], rax
0026E072  41 B8 00 04 00 00               mov r8d, 0x400
0026E078  FF 4D F8                        dec dword ptr [rbp - 8]
0026E07B  49 8D 4E 08                     lea rcx, [r14 + 8]
0026E07F  E8 BC 8B 45 00                  call 0x1406c6c40
0026E084  49 83 26 00                     and qword ptr [r14], 0
0026E088  44 8B C6                        mov r8d, esi
0026E08B  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
0026E08F  49 8B D6                        mov rdx, r14
0026E092  48 8B CF                        mov rcx, rdi
0026E095  49 89 06                        mov qword ptr [r14], rax
0026E098  E8 03 FC FF FF                  call 0x14026dca0
0026E09D  44 01 28                        add dword ptr [rax], r13d
0026E0A0  4C 89 77 58                     mov qword ptr [rdi + 0x58], r14
0026E0A4  44 3B FE                        cmp r15d, esi
0026E0A7  77 96                           ja 0x14026e03f
0026E0A9  EB 80                           jmp 0x14026e02b
0026E0AB  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0026E0B1  45 33 C9                        xor r9d, r9d
0026E0B4  BA 32 16 00 00                  mov edx, 0x1632
0026E0B9  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0026E0C0  41 8D 49 34                     lea ecx, [r9 + 0x34]
0026E0C4  E8 97 F5 28 00                  call 0x1404fd660
0026E0C9  CC                              int3
0026E0CA  4C 89 01                        mov qword ptr [rcx], r8
0026E0CD  49 03 C3                        add rax, r11
0026E0D0  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0026E0D4  49 89 48 08                     mov qword ptr [r8 + 8], rcx
0026E0D8  48 89 0A                        mov qword ptr [rdx], rcx
0026E0DB  48 83 C1 10                     add rcx, 0x10
0026E0DF  48 3B 42 F8                     cmp rax, qword ptr [rdx - 8]
0026E0E3  7F 0F                           jg 0x14026e0f4
0026E0E5  4C 8B 02                        mov r8, qword ptr [rdx]
0026E0E8  49 39 50 08                     cmp qword ptr [r8 + 8], rdx
0026E0EC  0F 85 81 FE FF FF               jne 0x14026df73
0026E0F2  EB D6                           jmp 0x14026e0ca
0026E0F4  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
0026E0F8  E9 34 FE FF FF                  jmp 0x14026df31
0026E0FD  8D 41 0F                        lea eax, [rcx + 0xf]
0026E100  83 E0 F0                        and eax, 0xfffffff0
0026E103  03 C8                           add ecx, eax
0026E105  E9 A8 FC FF FF                  jmp 0x14026ddb2
0026E10A  4D 85 FF                        test r15, r15
0026E10D  0F 84 16 FE FF FF               je 0x14026df29
0026E113  8B D6                           mov edx, esi
0026E115  49 2B D0                        sub rdx, r8
0026E118  44 8B CE                        mov r9d, esi
0026E11B  49 2B D5                        sub rdx, r13
0026E11E  4D 2B C1                        sub r8, r9
0026E121  48 03 D1                        add rdx, rcx
0026E124  49 03 D7                        add rdx, r15
0026E127  4D 2B C7                        sub r8, r15
0026E12A  4F 8D 14 28                     lea r10, [r8 + r13]
0026E12E  E9 9D BC 46 00                  jmp 0x1406d9dd0
0026E133  83 C1 07                        add ecx, 7
0026E136  48 8D 43 FF                     lea rax, [rbx - 1]
0026E13A  48 D3 F8                        sar rax, cl
0026E13D  45 03 FD                        add r15d, r13d
0026E140  48 85 C0                        test rax, rax
0026E143  75 EE                           jne 0x14026e133
0026E145  E9 4D FE FF FF                  jmp 0x14026df97
0026E14A  41 8D 57 01                     lea edx, [r15 + 1]
0026E14E  89 15 40 C7 B9 00               mov dword ptr [rip + 0xb9c740], edx
0026E154  E9 62 FE FF FF                  jmp 0x14026dfbb
0026E159  48 8B 57 58                     mov rdx, qword ptr [rdi + 0x58]
0026E15D  48 8B CF                        mov rcx, rdi
0026E160  E8 63 EE FF FF                  call 0x14026cfc8
0026E165  E9 9C FE FF FF                  jmp 0x14026e006
0026E16A  F7 87 98 00 00 00 00 02 00 00   test dword ptr [rdi + 0x98], 0x200
0026E174  0F 84 B1 FE FF FF               je 0x14026e02b
0026E17A  33 D2                           xor edx, edx
0026E17C  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0026E180  E8 3F A4 21 00                  call 0x1404885c4
0026E185  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
0026E189  48 8D 0D F0 39 BA 00            lea rcx, [rip + 0xba39f0]
0026E190  4D 8B 86 00 04 00 00            mov r8, qword ptr [r14 + 0x400]
0026E197  49 8B D6                        mov rdx, r14
0026E19A  49 8B 86 F8 07 00 00            mov rax, qword ptr [r14 + 0x7f8]
0026E1A1  49 89 40 08                     mov qword ptr [r8 + 8], rax
0026E1A5  4C 89 00                        mov qword ptr [rax], r8
0026E1A8  E8 23 F8 11 00                  call 0x14038d9d0
0026E1AD  E9 79 FE FF FF                  jmp 0x14026e02b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcExtendVacbArray(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (80);
    v_r12 = 0;
    result = (a2) >> (32);
    if (sign_flag) goto loc_0026DEED;
    if (((*(unsigned int *)(a1 + 152)) & (512)) != 0) goto loc_0026DEF4;
loc_0026DD1B:
    v_stack_m50 = v_stack_m58;
    v_stack_m58 = v_stack_m58;
    if (a2 <= (*(unsigned __int64 *)(a1 + 32))) goto loc_0026DE79;
    v_r11 = (unsigned int)((v_r11) | (0xFFFFFFFFULL));
    if ((*(unsigned __int64 *)(a1 + 32)) >= ((unsigned int)(0x2000000ULL))) goto loc_0026DE74;
    if (a2 >= ((unsigned int)(0x2000000ULL))) { a2 = (unsigned int)(0x2000000ULL); }
    result = (a2) >> (32);
    if ((unsigned int)(result) != 0) goto loc_0026DD82;
    if (((unsigned int)(a2)) > ((unsigned int)((unsigned int)(0x100000ULL)))) goto loc_0026DE9D;
    goto loc_0026DD85;
loc_0026DD82:
loc_0026DD85:
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)(v_r11)));
    if ((*(unsigned int *)(a1 + 36)) != 0) goto loc_0026DD9E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) > ((unsigned int)((unsigned int)(0x100000ULL)))) goto loc_0026DEAB;
    goto loc_0026DDA1;
loc_0026DD9E:
loc_0026DDA1:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r11)))) <= ((unsigned int)((unsigned int)((unsigned int)(v_r11))))) goto loc_0026DE70;
    if (0 != 0) goto loc_0026E0FD;
loc_0026DDB2:
    result = (unsigned int)((unsigned int)(v_r11)) + 8;
    if (a2 < ((unsigned int)(0x2000000ULL))) { result = (unsigned int)((unsigned int)((unsigned int)(v_r11))); }
    v_stack_p18 = result;
    result = ExAllocatePoolWithTag(512, (unsigned int)((unsigned int)(result)), (unsigned int)(0x70566343ULL), (unsigned int)(0x2000000ULL));
    if (result != 0) goto loc_0026DDE1;
loc_0026DDD7:
    goto loc_0026DE84;
loc_0026DDE1:
    result = CcAcquireBcbLockAndVacbLock(0, a1, (unsigned int)(0x70566343ULL), (unsigned int)(0x2000000ULL));
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_0026DF04;
    result = memcpy(result, *(unsigned __int64 *)(a1 + 88), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11)))), (unsigned int)(0x2000000ULL));
loc_0026DE07:
    a2 = 0;
    a3 = (unsigned int)(((unsigned int)(v_stack_p10)) - ((unsigned int)((unsigned int)((unsigned int)(v_r11)))));
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11))))) + (result);
    result = memset(a1, a2, a3, (unsigned int)(0x2000000ULL));
    if (0 >= 0x2000000ULL) {
        a1 = v_stack_p18;
        a1 = (unsigned int)((a1) + (-8));
        result = 0;
        *(unsigned __int64 *)(a1 + result * 1) = 0;
    }
    if (0 != 0) goto loc_0026DF0B;
loc_0026DE39:
    *(unsigned __int64 *)(a1 + 88) = 0;
    *(unsigned __int64 *)(a1 + 32) = 0;
    result = CcReleaseBcbLockAndVacbLock(0, a1, a3, (unsigned int)(0x2000000ULL));
    if ((*(unsigned __int64 *)(a1 + 88)) == (a1 + 56)) goto loc_0026DE64;
    result = a1 + 56;
    if (*(unsigned __int64 *)(a1 + 88) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 88);
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(0x2000000ULL));
    }
loc_0026DE70:
    *(unsigned __int64 *)(a1 + 32) = 0;
loc_0026DE74:
    if (0 > 0) goto loc_0026DEB6;
loc_0026DE79:
    result = CcFreeUnusedVacbLevels(v_stack_m58, a2, a3, (unsigned int)(0x2000000ULL));
    result = 0;
loc_0026DE84:
    v_rsp = (v_rsp) + (80);
    return result;
loc_0026DE9D:
    a1 = (unsigned int)((0) >> (18));
    a1 = (unsigned int)((a1) << (3));
    goto loc_0026DD85;
loc_0026DEAB:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) >> (18));
    v_rsi = (unsigned int)((v_rsi) << (3));
    goto loc_0026DDA1;
loc_0026DEB6:
    if (0 <= ((unsigned int)(0x2000000ULL))) goto loc_0026DED4;
loc_0026DEC3:
    a1 = (unsigned int)((25) + (7));
    result = (1) << ((unsigned __int8)(a1));
    v_rsi = (unsigned int)((1) + (1));
    if (0 > result) goto loc_0026DEC3;
loc_0026DED4:
    result = (v_stack_p8 - 1) >> ((unsigned __int8)(a1));
    if (result != 0) goto loc_0026E133;
loc_0026DEE7:
    *(unsigned __int64 *)(a1 + 32) = v_stack_p8;
    goto loc_0026DE79;
loc_0026DEED:
    goto loc_0026DE84;
loc_0026DEF4:
    if (v_stack_p8 > 0x200000ULL) { v_r12 = 1; }
    goto loc_0026DD1B;
loc_0026DF04:
    v_rsi = 0;
    goto loc_0026DE07;
loc_0026DF0B:
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 32)) > 0x200000ULL) goto loc_0026E10A;
loc_0026DF29:
loc_0026DF31:
    if ((*(unsigned __int64 *)(a1 + 24)) != (a1 + 16)) goto loc_0026E0DF;
loc_0026DF3D:
    if (0 >= 0) goto loc_0026DE39;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8)) != (a1 + 16)) goto loc_0026DF73;
    *(unsigned __int64 *)((unsigned int)(v_stack_p10) + 1 * 1) = *(unsigned __int64 *)(a1 + 16);
    result = (result) + ((unsigned int)(0x80000ULL));
    *(unsigned __int64 *)((unsigned int)(v_stack_p10) + 1 * 1 + 8) = a1 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) = (unsigned int)(v_stack_p10) + 1 * 1;
    *(unsigned __int64 *)(a1 + 16) = (unsigned int)(v_stack_p10) + 1 * 1;
    a1 = ((unsigned int)(v_stack_p10) + 1 * 1) + (16);
    goto loc_0026DF3D;
loc_0026DF66:
    if ((*(unsigned __int64 *)(v_stack_m50)) != v_stack_m58) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result + 8) = a1;
    *(unsigned __int64 *)(result) = v_stack_m58;
    *(unsigned __int64 *)(a1) = result;
    v_stack_m50 = result;
    result = (unsigned int)(((unsigned int)(v_stack_m40)) + (1));
    v_stack_m40 = (unsigned int)(result);
    goto loc_0026DFCE;
loc_0026DF97:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) <= 0) goto loc_0026DEE7;
    result = KeAcquireQueuedSpinLock(4, v_stack_m58, a1 + 16, a1 + 16);
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) >= (*(unsigned int *)(v_rip + 12175583))) goto loc_0026E14A;
loc_0026DFBB:
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)(result), a1 + 16, a1 + 16);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))) - (0));
loc_0026DFCE:
    if (((unsigned int)(v_r14)) <= ((unsigned int)((unsigned int)(v_stack_m40)))) goto loc_0026DFF2;
    result = ExAllocateFromNPagedLookasideList(v_rip + 12204710, (unsigned __int8)(result), a1 + 16, a1 + 16);
    if (result != 0) goto loc_0026DF66;
    result = CcFreeUnusedVacbLevels(v_stack_m58, (unsigned __int8)(result), a1 + 16, a1 + 16);
    goto loc_0026DDD7;
loc_0026DFF2:
    result = CcAcquireBcbLockAndVacbLock((unsigned int)((unsigned int)(v_r12)), a1, a1 + 16, a1 + 16);
    if (0 == 1) goto loc_0026E159;
loc_0026E006:
    result = VacbLevelReference(a1, *(unsigned __int64 *)(a1 + 88), v_rsi - 1, a1 + 16);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) | ((unsigned int)((unsigned int)(*(unsigned int *)(result)))));
    if (condition_is_not_equal) goto loc_0026E03F;
    if (0 == 1) goto loc_0026E16A;
loc_0026E02B:
    *(unsigned __int64 *)(a1 + 32) = v_stack_p8;
    result = CcReleaseBcbLockAndVacbLock((unsigned int)((unsigned int)(v_r12)), a1, v_rsi - 1, a1 + 16);
    goto loc_0026DEE7;
loc_0026E03F:
    v_rsi = (unsigned int)((v_rsi) + (1));
    if (v_stack_m58 == v_stack_m58) goto loc_0026E0AB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 8)) != v_stack_m58) goto loc_0026DF73;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + 8))) != v_stack_m58) goto loc_0026DF73;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + 8)) = *(unsigned __int64 *)(v_stack_m58);
    a2 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58) + 8) = *(unsigned __int64 *)(v_stack_m58 + 8);
    result = memset(v_stack_m58 + 8, a2, (unsigned int)(0x400ULL), a1 + 16);
    *(unsigned __int64 *)(v_stack_m58) = *(unsigned __int64 *)(a1 + 88);
    result = VacbLevelReference(a1, v_stack_m58, (unsigned int)((unsigned int)(v_rsi)), a1 + 16);
    *(unsigned __int64 *)(a1 + 88) = v_stack_m58;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) > ((unsigned int)(v_rsi))) goto loc_0026E03F;
    goto loc_0026E02B;
loc_0026E0AB:
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x1632ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_0026E0CA:
    *(unsigned __int64 *)(a4 + 52) = 0xFFFFFFFFC0000420ULL;
    result = (result) + ((unsigned int)(0x80000ULL));
    *(unsigned __int64 *)(a4 + 52 + 8) = (unsigned int)(0x1632ULL);
    *(unsigned __int64 *)(0xFFFFFFFFC0000420ULL + 8) = a4 + 52;
    *(unsigned __int64 *)((unsigned int)(0x1632ULL)) = a4 + 52;
    a1 = (a4 + 52) + (16);
loc_0026E0DF:
    if (result > (*(unsigned __int64 *)((unsigned int)(0x1632ULL) - 8))) goto loc_0026E0F4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x1632ULL)) + 8)) != ((unsigned int)(0x1632ULL))) goto loc_0026DF73;
    goto loc_0026E0CA;
loc_0026E0F4:
    goto loc_0026DF31;
loc_0026E0FD:
    result = (unsigned int)((a1 + 15) & (0xFFFFFFF0ULL));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    goto loc_0026DDB2;
loc_0026E10A:
    if ((unsigned int)((unsigned int)(v_rsi)) == 0) goto loc_0026DF29;
    a2 = ((unsigned int)((unsigned int)(v_rsi))) - (*(unsigned __int64 *)((unsigned int)(0x1632ULL)));
    a2 = (a2) - (1);
    a3 = (*(unsigned __int64 *)((unsigned int)(0x1632ULL))) - ((unsigned int)((unsigned int)(v_rsi)));
    a2 = (a2) + (a1);
    a2 = (a2) + ((unsigned int)((unsigned int)(v_rsi)));
    a3 = (a3) - ((unsigned int)((unsigned int)(v_rsi)));
loc_0026E133:
    a1 = (unsigned int)((a1) + (7));
    result = (v_stack_p8 - 1) >> ((unsigned __int8)(a1));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + (1));
    if (result != 0) goto loc_0026E133;
    goto loc_0026DF97;
loc_0026E14A:
    *(unsigned int *)(v_rip + 12175168) = (unsigned int)(v_r15 + 1);
    goto loc_0026DFBB;
loc_0026E159:
    result = CcCalculateVacbLevelLockCount(a1, *(unsigned __int64 *)(a1 + 88), a3, (unsigned int)((unsigned int)(v_rsi)));
    goto loc_0026E006;
loc_0026E16A:
    if (((*(unsigned int *)(a1 + 152)) & (512)) == 0) goto loc_0026E02B;
    a2 = 0;
    result = CcAllocateVacbLevel(v_stack_m58, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    *(unsigned __int64 *)(a1 + 88) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + 1024) + 8) = *(unsigned __int64 *)(v_stack_m58 + 2040);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m58 + 2040)) = *(unsigned __int64 *)(v_stack_m58 + 1024);
    result = ExFreeToNPagedLookasideList(v_rip + 12204528, v_stack_m58, *(unsigned __int64 *)(v_stack_m58 + 1024), (unsigned int)((unsigned int)(v_rsi)));
    goto loc_0026E02B;
}
```

## 5. (Beta) C Style

```c
int64_t CcExtendVacbArray(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (80);
    local_r12 = 0;
    result = (Arg2) >> (32);
    if (sign_flag) goto loc_0026DEED;
    if (((*(uint32_t *)(arg1 + 0x98)) & (512)) != 0) goto loc_0026DEF4;
loc_0026DD1B:
    v_stack_m50 = v_stack_m58;
    v_stack_m58 = v_stack_m58;
    if (Arg2 <= (*(uint64_t *)(arg1 + 0x20))) goto loc_0026DE79;
    local_r11 = (uint32_t)((local_r11) | (0xFFFFFFFFULL));
    if ((*(uint64_t *)(arg1 + 0x20)) >= ((uint32_t)(0x2000000ULL))) goto loc_0026DE74;
    if (Arg2 >= ((uint32_t)(0x2000000ULL))) { Arg2 = (uint32_t)(0x2000000ULL); }
    result = (Arg2) >> (32);
    if ((uint32_t)(result) != 0) goto loc_0026DD82;
    if (((uint32_t)(Arg2)) > ((uint32_t)((uint32_t)(0x100000ULL)))) goto loc_0026DE9D;
    goto loc_0026DD85;
loc_0026DD82:
loc_0026DD85:
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)(local_r11)));
    if ((*(uint32_t *)(arg1 + 0x24)) != 0) goto loc_0026DD9E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) > ((uint32_t)((uint32_t)(0x100000ULL)))) goto loc_0026DEAB;
    goto loc_0026DDA1;
loc_0026DD9E:
loc_0026DDA1:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r11)))) <= ((uint32_t)((uint32_t)((uint32_t)(local_r11))))) goto loc_0026DE70;
    if (0 != 0) goto loc_0026E0FD;
loc_0026DDB2:
    result = (uint32_t)((uint32_t)(local_r11)) + 8;
    if (Arg2 < ((uint32_t)(0x2000000ULL))) { result = (uint32_t)((uint32_t)((uint32_t)(local_r11))); }
    v_stack_p18 = result;
    result = ExAllocatePoolWithTag(512, (uint32_t)((uint32_t)(result)), (uint32_t)(0x70566343ULL), (uint32_t)(0x2000000ULL));
    if (result != 0) goto loc_0026DDE1;
loc_0026DDD7:
    goto loc_0026DE84;
loc_0026DDE1:
    result = CcAcquireBcbLockAndVacbLock(0, Arg1, (uint32_t)(0x70566343ULL), (uint32_t)(0x2000000ULL));
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_0026DF04;
    result = memcpy(result, *(uint64_t *)(arg1 + 0x58), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11)))), (uint32_t)(0x2000000ULL));
loc_0026DE07:
    Arg2 = 0;
    a3 = (uint32_t)(((uint32_t)(v_stack_p10)) - ((uint32_t)((uint32_t)((uint32_t)(local_r11)))));
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11))))) + (result);
    result = memset(Arg1, Arg2, a3, (uint32_t)(0x2000000ULL));
    if (0 >= 0x2000000ULL) {
        Arg1 = v_stack_p18;
        Arg1 = (uint32_t)((Arg1) + (-8));
        result = 0;
        *(uint64_t *)(arg1 + result * 1) = 0;
    }
    if (0 != 0) goto loc_0026DF0B;
loc_0026DE39:
    *(uint64_t *)(arg1 + 0x58) = 0;
    *(uint64_t *)(arg1 + 0x20) = 0;
    result = CcReleaseBcbLockAndVacbLock(0, Arg1, a3, (uint32_t)(0x2000000ULL));
    if ((*(uint64_t *)(arg1 + 0x58)) == (Arg1 + 56)) goto loc_0026DE64;
    result = Arg1 + 56;
    if (*(uint64_t *)(arg1 + 0x58) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x58);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, (uint32_t)(0x2000000ULL));
    }
loc_0026DE70:
    *(uint64_t *)(arg1 + 0x20) = 0;
loc_0026DE74:
    if (0 > 0) goto loc_0026DEB6;
loc_0026DE79:
    result = CcFreeUnusedVacbLevels(v_stack_m58, Arg2, a3, (uint32_t)(0x2000000ULL));
    result = 0;
loc_0026DE84:
    local_rsp = (local_rsp) + (80);
    return result;
loc_0026DE9D:
    Arg1 = (uint32_t)((0) >> (18));
    Arg1 = (uint32_t)((Arg1) << (3));
    goto loc_0026DD85;
loc_0026DEAB:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) >> (18));
    local_rsi = (uint32_t)((local_rsi) << (3));
    goto loc_0026DDA1;
loc_0026DEB6:
    if (0 <= ((uint32_t)(0x2000000ULL))) goto loc_0026DED4;
loc_0026DEC3:
    Arg1 = (uint32_t)((25) + (7));
    result = (1) << ((uint8_t)(Arg1));
    local_rsi = (uint32_t)((1) + (1));
    if (0 > result) goto loc_0026DEC3;
loc_0026DED4:
    result = (v_stack_p8 - 1) >> ((uint8_t)(Arg1));
    if (result != 0) goto loc_0026E133;
loc_0026DEE7:
    *(uint64_t *)(arg1 + 0x20) = v_stack_p8;
    goto loc_0026DE79;
loc_0026DEED:
    goto loc_0026DE84;
loc_0026DEF4:
    if (v_stack_p8 > 0x200000ULL) { local_r12 = 1; }
    goto loc_0026DD1B;
loc_0026DF04:
    local_rsi = 0;
    goto loc_0026DE07;
loc_0026DF0B:
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x20)) > 0x200000ULL) goto loc_0026E10A;
loc_0026DF29:
loc_0026DF31:
    if ((*(uint64_t *)(arg1 + 0x18)) != (Arg1 + 16)) goto loc_0026E0DF;
loc_0026DF3D:
    if (0 >= 0) goto loc_0026DE39;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8)) != (Arg1 + 16)) goto loc_0026DF73;
    *(uint64_t *)((uint32_t)(v_stack_p10) + 0x1 * 1) = *(uint64_t *)(arg1 + 0x10);
    result = (result) + ((uint32_t)(0x80000ULL));
    *(void **)((uint32_t)(v_stack_p10) + 0x1 * 1 + 0x8) = Arg1 + 16;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) = (uint32_t)(v_stack_p10) + 1 * 1;
    *(uint64_t *)(arg1 + 0x10) = (uint32_t)(v_stack_p10) + 1 * 1;
    Arg1 = ((uint32_t)(v_stack_p10) + 1 * 1) + (16);
    goto loc_0026DF3D;
loc_0026DF66:
    if ((*(uint64_t *)(v_stack_m50)) != v_stack_m58) {
        Arg1 = 3;
    }
    *(void **)(result + 0x8) = Arg1;
    *(uint64_t *)(result) = v_stack_m58;
    *(uint64_t *)(arg1) = result;
    v_stack_m50 = result;
    result = (uint32_t)(((uint32_t)(v_stack_m40)) + (1));
    v_stack_m40 = (uint32_t)(result);
    goto loc_0026DFCE;
loc_0026DF97:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) <= 0) goto loc_0026DEE7;
    result = KeAcquireQueuedSpinLock(4, v_stack_m58, Arg1 + 16, Arg1 + 16);
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) >= (*(uint32_t *)(v_rip + 0xB9C8DF))) goto loc_0026E14A;
loc_0026DFBB:
    result = KeReleaseQueuedSpinLock(4, (uint8_t)(result), Arg1 + 16, Arg1 + 16);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))) - (0));
loc_0026DFCE:
    if (((uint32_t)(local_r14)) <= ((uint32_t)((uint32_t)(v_stack_m40)))) goto loc_0026DFF2;
    result = ExAllocateFromNPagedLookasideList(v_rip + 12204710, (uint8_t)(result), Arg1 + 16, Arg1 + 16);
    if (result != 0) goto loc_0026DF66;
    result = CcFreeUnusedVacbLevels(v_stack_m58, (uint8_t)(result), Arg1 + 16, Arg1 + 16);
    goto loc_0026DDD7;
loc_0026DFF2:
    result = CcAcquireBcbLockAndVacbLock((uint32_t)((uint32_t)(local_r12)), Arg1, Arg1 + 16, Arg1 + 16);
    if (0 == 1) goto loc_0026E159;
loc_0026E006:
    result = VacbLevelReference(Arg1, *(uint64_t *)(arg1 + 0x58), local_rsi - 1, Arg1 + 16);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) | ((uint32_t)((uint32_t)(*(uint32_t *)(result)))));
    if (condition_is_not_equal) goto loc_0026E03F;
    if (0 == 1) goto loc_0026E16A;
loc_0026E02B:
    *(uint64_t *)(arg1 + 0x20) = v_stack_p8;
    result = CcReleaseBcbLockAndVacbLock((uint32_t)((uint32_t)(local_r12)), Arg1, local_rsi - 1, Arg1 + 16);
    goto loc_0026DEE7;
loc_0026E03F:
    local_rsi = (uint32_t)((local_rsi) + (1));
    if (v_stack_m58 == v_stack_m58) goto loc_0026E0AB;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x8)) != v_stack_m58) goto loc_0026DF73;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m58 + 0x8))) != v_stack_m58) goto loc_0026DF73;
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + 0x8)) = *(uint64_t *)(v_stack_m58);
    Arg2 = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m58) + 0x8) = *(uint64_t *)(v_stack_m58 + 0x8);
    result = memset(v_stack_m58 + 8, Arg2, (uint32_t)(0x400ULL), Arg1 + 16);
    *(uint64_t *)(v_stack_m58) = *(uint64_t *)(arg1 + 0x58);
    result = VacbLevelReference(Arg1, v_stack_m58, (uint32_t)((uint32_t)(local_rsi)), Arg1 + 16);
    *(uint64_t *)(arg1 + 0x58) = v_stack_m58;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) > ((uint32_t)(local_rsi))) goto loc_0026E03F;
    goto loc_0026E02B;
loc_0026E0AB:
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (uint32_t)(0x1632ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_0026E0CA:
    *(uint64_t *)(a4 + 0x34) = 0xFFFFFFFFC0000420ULL;
    result = (result) + ((uint32_t)(0x80000ULL));
    *(uint64_t *)(a4 + 0x34 + 0x8) = (uint32_t)(0x1632ULL);
    *(uint64_t *)(0xFFFFFFFFC0000420ULL + 0x8) = a4 + 52;
    *(uint64_t *)((uint32_t)(0x1632ULL)) = a4 + 52;
    Arg1 = (a4 + 52) + (16);
loc_0026E0DF:
    if (result > (*(uint64_t *)((uint32_t)(0x1632ULL) - 0x8))) goto loc_0026E0F4;
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(0x1632ULL)) + 0x8)) != ((uint32_t)(0x1632ULL))) goto loc_0026DF73;
    goto loc_0026E0CA;
loc_0026E0F4:
    goto loc_0026DF31;
loc_0026E0FD:
    result = (uint32_t)((Arg1 + 15) & (0xFFFFFFF0ULL));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    goto loc_0026DDB2;
loc_0026E10A:
    if ((uint32_t)((uint32_t)(local_rsi)) == 0) goto loc_0026DF29;
    Arg2 = ((uint32_t)((uint32_t)(local_rsi))) - (*(uint64_t *)((uint32_t)(0x1632ULL)));
    Arg2 = (Arg2) - (1);
    a3 = (*(uint64_t *)((uint32_t)(0x1632ULL))) - ((uint32_t)((uint32_t)(local_rsi)));
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) + ((uint32_t)((uint32_t)(local_rsi)));
    a3 = (a3) - ((uint32_t)((uint32_t)(local_rsi)));
loc_0026E133:
    Arg1 = (uint32_t)((Arg1) + (7));
    result = (v_stack_p8 - 1) >> ((uint8_t)(Arg1));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + (1));
    if (result != 0) goto loc_0026E133;
    goto loc_0026DF97;
loc_0026E14A:
    *(uint32_t *)(v_rip + 0xB9C740) = (uint32_t)(local_r15 + 1);
    goto loc_0026DFBB;
loc_0026E159:
    result = CcCalculateVacbLevelLockCount(Arg1, *(uint64_t *)(arg1 + 0x58), a3, (uint32_t)((uint32_t)(local_rsi)));
    goto loc_0026E006;
loc_0026E16A:
    if (((*(uint32_t *)(arg1 + 0x98)) & (512)) == 0) goto loc_0026E02B;
    Arg2 = 0;
    result = CcAllocateVacbLevel(v_stack_m58, Arg2, a3, (uint32_t)((uint32_t)(local_rsi)));
    *(uint64_t *)(arg1 + 0x58) = result;
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + 0x400) + 0x8) = *(uint64_t *)(v_stack_m58 + 0x7F8);
    *(uint64_t *)(*(uint64_t *)(v_stack_m58 + 0x7F8)) = *(uint64_t *)(v_stack_m58 + 0x400);
    result = ExFreeToNPagedLookasideList(v_rip + 12204528, v_stack_m58, *(uint64_t *)(v_stack_m58 + 0x400), (uint32_t)((uint32_t)(local_rsi)));
    goto loc_0026E02B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x98` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026DCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
