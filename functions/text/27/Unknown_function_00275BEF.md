# sub_00275BEF

- RVA: `0x00275BEF`–`0x002760B0` (길이 `1,217` bytes)
- VA: `0x0000000140275BEF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065EA4`
- 디코드: `264`개 명령, `1,217/1,217` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00275CE2` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00275EC1` → [ExReleaseSpinLockRegardlessFromDpcLevel](../23/ExReleaseSpinLockRegardlessFromDpcLevel_function_0023A330.md) (function, `0x0023A330`)
- `0x00275EF1` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00275F57` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0027608E` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002760A6` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00275BEF` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00275DF9` → RVA `0x00E2CB40` (`.data`; read)
- `0x00276080` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **27**
  - `0x00275BFA` → [sub_002759BE + 0xF8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275C17` → [sub_002759BE + 0xF8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275C27` → [sub_002759BE + 0xF8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275C52` → [sub_002759BE + 0xF8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275C82` → [sub_002759BE + 0x9D](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275CC2` → [sub_002760C1 + 0x171](Unknown_function_002760C1.md) (`tail-transfer`)
  - `0x00275D16` → [sub_002760C1](Unknown_function_002760C1.md) (`tail-transfer`)
  - `0x00275E18` → [sub_002759BE + 0x1D8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275E35` → [sub_002759BE + 0x1D8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275E45` → [sub_002759BE + 0x1D8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275E6F` → [sub_002759BE + 0x1D8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275EFD` → [sub_002760C1 + 0x62](Unknown_function_002760C1.md) (`tail-transfer`)
  - `0x00275F22` → [sub_002759BE + 0x4D](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275F30` → [sub_002759BE + 0x213](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275F3C` → [sub_002759BE + 0x21B](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275F49` → [sub_002759BE + 0x21B](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275F5F` → [sub_002759BE + 0x21B](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00275F74` → [sub_002760C1 + 0x6C](Unknown_function_002760C1.md) (`tail-transfer`)
  - `0x00275F7C` → [sub_002762D6 + 0x52](Unknown_function_002762D6.md) (`tail-transfer`)
  - `0x00275F94` → [sub_002759BE + 0x162](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x0027601C` → [sub_002760C1 + 0x108](Unknown_function_002760C1.md) (`tail-transfer`)
  - `0x00276041` → [sub_002759BE + 0x1F8](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00276050` → [sub_002759BE + 0x213](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00276066` → [sub_002760C1 + 0x49](Unknown_function_002760C1.md) (`tail-transfer`)
  - `0x00276088` → [sub_002759BE + 0x73](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x00276093` → [sub_002759BE + 0x82](Unknown_function_002759BE.md) (`tail-transfer`)
  - `0x002760A0` → [sub_002759BE + 0x18C](Unknown_function_002759BE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00275BEF  48 F7 05 8E 0E D5 00 00 00 60 00  test qword ptr [rip + 0xd50e8e], 0x600000
00275BFA  0F 84 B6 FE FF FF               je 0x140275ab6
00275C00  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00275C09  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00275C10  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00275C17  0F 84 99 FE FF FF               je 0x140275ab6
00275C1D  4C 8B 81 08 05 00 00            mov r8, qword ptr [rcx + 0x508]
00275C24  4D 85 C0                        test r8, r8
00275C27  0F 84 89 FE FF FF               je 0x140275ab6
00275C2D  49 8B C5                        mov rax, r13
00275C30  48 C1 E8 03                     shr rax, 3
00275C34  25 FF 01 00 00                  and eax, 0x1ff
00275C39  49 8B 04 C0                     mov rax, qword ptr [r8 + rax*8]
00275C3D  A8 20                           test al, 0x20
00275C3F  74 04                           je 0x140275c45
00275C41  48 83 CA 20                     or rdx, 0x20
00275C45  48 8B CA                        mov rcx, rdx
00275C48  48 83 CA 42                     or rdx, 0x42
00275C4C  A8 42                           test al, 0x42
00275C4E  48 0F 44 D1                     cmove rdx, rcx
00275C52  E9 5F FE FF FF                  jmp 0x140275ab6
00275C57  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
00275C61  F0 48 21 02                     lock and qword ptr [rdx], rax
00275C65  4C 89 6E 10                     mov qword ptr [rsi + 0x10], r13
00275C69  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
00275C73  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
00275C7D  FF CF                           dec edi
00275C7F  48 FF CB                        dec rbx
00275C82  E9 D4 FD FF FF                  jmp 0x140275a5b
00275C87  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275C8D  A8 0F                           test al, 0xf
00275C8F  75 37                           jne 0x140275cc8
00275C91  49 8B C2                        mov rax, r10
00275C94  4C 3B E8                        cmp r13, rax
00275C97  72 2F                           jb 0x140275cc8
00275C99  49 8B C3                        mov rax, r11
00275C9C  4C 3B E8                        cmp r13, rax
00275C9F  77 27                           ja 0x140275cc8
00275CA1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00275CAA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00275CB1  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00275CB8  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00275CBF  48 85 C9                        test rcx, rcx
00275CC2  0F 85 6A 05 00 00               jne 0x140276232
00275CC8  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275CCE  A8 0F                           test al, 0xf
00275CD0  0F 85 C3 02 00 00               jne 0x140275f99
00275CD6  33 FF                           xor edi, edi
00275CD8  49 8B CD                        mov rcx, r13
00275CDB  89 BC 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edi
00275CE2  E8 B9 CB 00 00                  call 0x1402828a0
00275CE7  48 8B D8                        mov rbx, rax
00275CEA  48 BE FF FF FF FF FF FF FF DF   movabs rsi, 0xdfffffffffffffff
00275CF4  48 BD 20 00 00 00 00 00 00 10   movabs rbp, 0x1000000000000020
00275CFE  49 BC 00 00 00 00 00 00 00 20   movabs r12, 0x2000000000000000
00275D08  F6 C3 01                        test bl, 1
00275D0B  74 36                           je 0x140275d43
00275D0D  48 8B C3                        mov rax, rbx
00275D10  48 C1 E8 3C                     shr rax, 0x3c
00275D14  A8 01                           test al, 1
00275D16  0F 85 A5 03 00 00               jne 0x1402760c1
00275D1C  48 8B CB                        mov rcx, rbx
00275D1F  48 23 CE                        and rcx, rsi
00275D22  48 0B CD                        or rcx, rbp
00275D25  48 F7 05 58 0D D5 00 00 00 00 02  test qword ptr [rip + 0xd50d58], 0x2000000
00275D30  74 03                           je 0x140275d35
00275D32  0F AE E8                        lfence
00275D35  48 8B C3                        mov rax, rbx
00275D38  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
00275D3E  48 8B D8                        mov rbx, rax
00275D41  75 C5                           jne 0x140275d08
00275D43  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00275D4B  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00275D50  49 BC FF FF FF FF FF F6 FF FF   movabs r12, 0xfffff6ffffffffff
00275D5A  49 8D 76 38                     lea rsi, [r14 + 0x38]
00275D5E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00275D63  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00275D6A  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
00275D74  49 BB FF DF BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbedfff
00275D7E  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
00275D82  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00275D8C  48 8B C0                        mov rax, rax
00275D8F  48 3B D0                        cmp rdx, rax
00275D92  0F 84 33 01 00 00               je 0x140275ecb
00275D98  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275D9E  A8 0F                           test al, 0xf
00275DA0  0F 84 CE 00 00 00               je 0x140275e74
00275DA6  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275DAC  A8 0F                           test al, 0xf
00275DAE  0F 84 A3 FE FF FF               je 0x140275c57
00275DB4  49 8B C2                        mov rax, r10
00275DB7  48 3B D0                        cmp rdx, rax
00275DBA  0F 82 97 FE FF FF               jb 0x140275c57
00275DC0  49 8B C3                        mov rax, r11
00275DC3  48 3B D0                        cmp rdx, rax
00275DC6  0F 87 8B FE FF FF               ja 0x140275c57
00275DCC  49 8B C2                        mov rax, r10
00275DCF  48 2B D0                        sub rdx, rax
00275DD2  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275DD8  48 C1 FA 03                     sar rdx, 3
00275DDC  44 8D 04 12                     lea r8d, [rdx + rdx]
00275DE0  BA 02 00 00 00                  mov edx, 2
00275DE5  41 8B C8                        mov ecx, r8d
00275DE8  41 8B C0                        mov eax, r8d
00275DEB  83 E1 1F                        and ecx, 0x1f
00275DEE  D3 E2                           shl edx, cl
00275DF0  F7 D2                           not edx
00275DF2  0F B3 CA                        btr edx, ecx
00275DF5  48 C1 E8 05                     shr rax, 5
00275DF9  48 8D 0D 40 6D BB 00            lea rcx, [rip + 0xbb6d40]
00275E00  F0 21 94 81 6C 26 00 00         lock and dword ptr [rcx + rax*4 + 0x266c], edx
00275E08  E9 58 FE FF FF                  jmp 0x140275c65
00275E0D  48 F7 05 70 0C D5 00 00 00 60 00  test qword ptr [rip + 0xd50c70], 0x600000
00275E18  0F 84 78 FD FF FF               je 0x140275b96
00275E1E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00275E27  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00275E2E  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00275E35  0F 84 5B FD FF FF               je 0x140275b96
00275E3B  48 8B 81 08 05 00 00            mov rax, qword ptr [rcx + 0x508]
00275E42  48 85 C0                        test rax, rax
00275E45  0F 84 4B FD FF FF               je 0x140275b96
00275E4B  49 C1 ED 03                     shr r13, 3
00275E4F  41 81 E5 FF 01 00 00            and r13d, 0x1ff
00275E56  4A 8B 04 E8                     mov rax, qword ptr [rax + r13*8]
00275E5A  A8 20                           test al, 0x20
00275E5C  74 04                           je 0x140275e62
00275E5E  49 83 C8 20                     or r8, 0x20
00275E62  49 8B C8                        mov rcx, r8
00275E65  49 83 C8 42                     or r8, 0x42
00275E69  A8 42                           test al, 0x42
00275E6B  4C 0F 44 C1                     cmove r8, rcx
00275E6F  E9 22 FD FF FF                  jmp 0x140275b96
00275E74  49 8B C2                        mov rax, r10
00275E77  48 3B D0                        cmp rdx, rax
00275E7A  0F 82 26 FF FF FF               jb 0x140275da6
00275E80  49 8B C3                        mov rax, r11
00275E83  48 3B D0                        cmp rdx, rax
00275E86  0F 87 1A FF FF FF               ja 0x140275da6
00275E8C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00275E95  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00275E9C  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00275EA3  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00275EAA  48 85 C9                        test rcx, rcx
00275EAD  0F 84 F3 FE FF FF               je 0x140275da6
00275EB3  48 C1 EA 03                     shr rdx, 3
00275EB7  81 E2 FF 01 00 00               and edx, 0x1ff
00275EBD  48 8D 0C 91                     lea rcx, [rcx + rdx*4]
00275EC1  E8 6A 44 FC FF                  call 0x14023a330
00275EC6  E9 9A FD FF FF                  jmp 0x140275c65
00275ECB  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00275ED4  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275EDA  24 0F                           and al, 0xf
00275EDC  0F 85 82 01 00 00               jne 0x140276064
00275EE2  B9 30 00 00 00                  mov ecx, 0x30
00275EE7  48 81 C2 40 9C 00 00            add rdx, 0x9c40
00275EEE  48 03 CA                        add rcx, rdx
00275EF1  E8 BA 12 FA FF                  call 0x1402171b0
00275EF6  E9 6A FD FF FF                  jmp 0x140275c65
00275EFB  3C 07                           cmp al, 7
00275EFD  0F 84 20 02 00 00               je 0x140276123
00275F03  3C 05                           cmp al, 5
00275F05  B9 03 00 00 00                  mov ecx, 3
00275F0A  41 0F 44 C9                     cmove ecx, r9d
00275F0E  8B C1                           mov eax, ecx
00275F10  48 8D 15 29 6C BB 00            lea rdx, [rip + 0xbb6c29]
00275F17  48 8D 92 80 32 00 00            lea rdx, [rdx + 0x3280]
00275F1E  48 8D 14 C2                     lea rdx, [rdx + rax*8]
00275F22  E9 E4 FA FF FF                  jmp 0x140275a0b
00275F27  8B 9C 24 B8 00 00 00            mov ebx, dword ptr [rsp + 0xb8]
00275F2E  85 DB                           test ebx, ebx
00275F30  0F 88 9B FC FF FF               js 0x140275bd1
00275F36  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00275F3A  A8 01                           test al, 1
00275F3C  0F 84 97 FC FF FF               je 0x140275bd9
00275F42  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00275F46  80 38 08                        cmp byte ptr [rax], 8
00275F49  0F 85 8A FC FF FF               jne 0x140275bd9
00275F4F  48 63 C7                        movsxd rax, edi
00275F52  49 8B 4C C6 18                  mov rcx, qword ptr [r14 + rax*8 + 0x18]
00275F57  E8 44 C9 00 00                  call 0x1402828a0
00275F5C  48 85 C0                        test rax, rax
00275F5F  0F 85 74 FC FF FF               jne 0x140275bd9
00275F65  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00275F69  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00275F6D  E9 D5 00 00 00                  jmp 0x140276047
00275F72  3C 07                           cmp al, 7
00275F74  0F 84 B3 01 00 00               je 0x14027612d
00275F7A  3C 05                           cmp al, 5
00275F7C  0F 84 A6 03 00 00               je 0x140276328
00275F82  B9 03 00 00 00                  mov ecx, 3
00275F87  8B D1                           mov edx, ecx
00275F89  48 81 C2 50 06 00 00            add rdx, 0x650
00275F90  49 8D 14 D1                     lea rdx, [r9 + rdx*8]
00275F94  E9 87 FB FF FF                  jmp 0x140275b20
00275F99  49 8B C2                        mov rax, r10
00275F9C  4C 3B E8                        cmp r13, rax
00275F9F  0F 82 31 FD FF FF               jb 0x140275cd6
00275FA5  49 8B C3                        mov rax, r11
00275FA8  4C 3B E8                        cmp r13, rax
00275FAB  0F 87 25 FD FF FF               ja 0x140275cd6
00275FB1  C7 84 24 B0 00 00 00 00 00 00 00  mov dword ptr [rsp + 0xb0], 0
00275FBC  49 8B C2                        mov rax, r10
00275FBF  49 8B CD                        mov rcx, r13
00275FC2  41 B8 01 00 00 00               mov r8d, 1
00275FC8  48 2B C8                        sub rcx, rax
00275FCB  41 BA 02 00 00 00               mov r10d, 2
00275FD1  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00275FD7  48 C1 F9 03                     sar rcx, 3
00275FDB  03 C9                           add ecx, ecx
00275FDD  8B F9                           mov edi, ecx
00275FDF  8B D9                           mov ebx, ecx
00275FE1  48 C1 EB 05                     shr rbx, 5
00275FE5  83 E7 1F                        and edi, 0x1f
00275FE8  48 81 C3 9B 09 00 00            add rbx, 0x99b
00275FEF  8B CF                           mov ecx, edi
00275FF1  41 8B 14 99                     mov edx, dword ptr [r9 + rbx*4]
00275FF5  49 8D 1C 99                     lea rbx, [r9 + rbx*4]
00275FF9  41 D3 E0                        shl r8d, cl
00275FFC  41 D3 E2                        shl r10d, cl
00275FFF  45 8B CA                        mov r9d, r10d
00276002  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00276007  41 F7 D1                        not r9d
0027600A  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
0027600F  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00276014  8B CF                           mov ecx, edi
00276016  8B C2                           mov eax, edx
00276018  D3 E8                           shr eax, cl
0027601A  A8 01                           test al, 1
0027601C  0F 85 A7 01 00 00               jne 0x1402761c9
00276022  41 8B C8                        mov ecx, r8d
00276025  8B C2                           mov eax, edx
00276027  0B CA                           or ecx, edx
00276029  41 23 C9                        and ecx, r9d
0027602C  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
00276030  8B D0                           mov edx, eax
00276032  0F 84 26 FD FF FF               je 0x140275d5e
00276038  EB DA                           jmp 0x140276014
0027603A  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0027603E  80 38 08                        cmp byte ptr [rax], 8
00276041  0F 85 6F FB FF FF               jne 0x140275bb6
00276047  C6 40 2C 01                     mov byte ptr [rax + 0x2c], 1
0027604B  BB 05 00 00 C0                  mov ebx, 0xc0000005
00276050  E9 7C FB FF FF                  jmp 0x140275bd1
00276055  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0027605A  FF C7                           inc edi
0027605C  48 FF C3                        inc rbx
0027605F  E9 05 FC FF FF                  jmp 0x140275c69
00276064  3C 07                           cmp al, 7
00276066  0F 84 9E 00 00 00               je 0x14027610a
0027606C  3C 05                           cmp al, 5
0027606E  B9 48 00 00 00                  mov ecx, 0x48
00276073  B8 00 00 00 00                  mov eax, 0
00276078  0F 44 C8                        cmove ecx, eax
0027607B  E9 67 FE FF FF                  jmp 0x140275ee7
00276080  8B 05 D2 7D C9 00               mov eax, dword ptr [rip + 0xc97dd2]
00276086  85 C0                           test eax, eax
00276088  0F 85 A3 F9 FF FF               jne 0x140275a31
0027608E  E8 BD F7 FF FF                  call 0x140275850
00276093  E9 A8 F9 FF FF                  jmp 0x140275a40
00276098  8B 05 BA 7D C9 00               mov eax, dword ptr [rip + 0xc97dba]
0027609E  85 C0                           test eax, eax
002760A0  0F 85 A4 FA FF FF               jne 0x140275b4a
002760A6  E8 A5 F7 FF FF                  call 0x140275850
002760AB  E9 BA FC FF FF                  jmp 0x140275d6a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00275BEF(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_pA0;
    unsigned int v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pB8;

    result = (v_r13) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { a2 = a2; }
}
```

## 5. (Beta) C Style

```c
int64_t sub_00275BEF(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_pA0;
    uint32_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pB8;

    result = (local_r13) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { Arg2 = Arg2; }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00275BEF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
