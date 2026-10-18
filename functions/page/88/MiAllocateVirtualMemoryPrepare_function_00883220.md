# MiAllocateVirtualMemoryPrepare

- RVA: `0x00883220`–`0x00883B39` (길이 `2,329` bytes)
- VA: `0x0000000140883220`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007C7F4`
- 디코드: `506`개 명령, `2,329/2,329` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00883442` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00883594` → [MiValidateZeroBits](MiValidateZeroBits_function_00884440.md) (function, `0x00884440`)
- `0x008839D6` → [DefaultAddProfileSource](../../text/4E/DefaultAddProfileSource_function_004E1110.md) (function, `0x004E1110`)
- `0x00883A13` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x00883B2F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [MmAllocateUserStack](MmAllocateUserStack_function_00882B30.md) at `0x00882C08`
- [NtAllocateVirtualMemory](NtAllocateVirtualMemory_function_00882D20.md) at `0x00882EAE`
- [MiAllocateVirtualMemoryCommon](MiAllocateVirtualMemoryCommon_function_00883000.md) at `0x008830BA`

### Static image references
- `0x0088340E` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00883779` → RVA `0x00FC5000` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008839D6` → [DefaultAddProfileSource](../../text/4E/DefaultAddProfileSource_function_004E1110.md) (`PAGE` → `.text`)
  - `0x00883A13` → [MiMakeProtectionMask](../../text/32/MiMakeProtectionMask_function_00329480.md) (`PAGE` → `.text`)
  - `0x00883B2F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00883A35` → [sub_00B18DFE](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883A3E` → [sub_00B18DFE](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883AA8` → [sub_00B18DFE + 0x4B](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883ABA` → [sub_00B18DFE + 0x2E](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883AD7` → [sub_00B18DFE + 0x6B](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883AE5` → [sub_00B18DFE + 0x6B](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883AF6` → [sub_00B18DFE + 0x7D](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)
  - `0x00883B03` → [sub_00B18DFE + 0x8D](../B1/Unknown_function_00B18DFE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00883220  4C 8B DC                        mov r11, rsp
00883223  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
00883227  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
0088322B  53                              push rbx
0088322C  55                              push rbp
0088322D  56                              push rsi
0088322E  57                              push rdi
0088322F  41 54                           push r12
00883231  41 55                           push r13
00883233  41 56                           push r14
00883235  41 57                           push r15
00883237  48 83 EC 58                     sub rsp, 0x58
0088323B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00883244  33 ED                           xor ebp, ebp
00883246  48 8B B4 24 F8 00 00 00         mov rsi, qword ptr [rsp + 0xf8]
0088324E  4C 8B FA                        mov r15, rdx
00883251  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00883256  49 89 6B 08                     mov qword ptr [r11 + 8], rbp
0088325A  4C 8B B0 B8 00 00 00            mov r14, qword ptr [rax + 0xb8]
00883261  4C 89 76 60                     mov qword ptr [rsi + 0x60], r14
00883265  48 83 F9 FF                     cmp rcx, -1
00883269  0F 85 9F 01 00 00               jne 0x14088340e
0088326F  4D 8B 63 08                     mov r12, qword ptr [r11 + 8]
00883273  8B 94 24 C8 00 00 00            mov edx, dword ptr [rsp + 0xc8]
0088327A  8B CA                           mov ecx, edx
0088327C  8B BC 24 C0 00 00 00            mov edi, dword ptr [rsp + 0xc0]
00883283  81 E1 00 F8 07 00               and ecx, 0x7f800
00883289  81 E2 FF 07 F8 FF               and edx, 0xfff807ff
0088328F  4C 89 76 58                     mov qword ptr [rsi + 0x58], r14
00883293  4C 89 4E 20                     mov qword ptr [rsi + 0x20], r9
00883297  89 8C 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ecx
0088329E  89 94 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edx
008832A5  F7 C7 FF 8F 03 9E               test edi, 0x9e038fff
008832AB  0F 85 3B 01 00 00               jne 0x1408833ec
008832B1  F7 C7 00 30 08 01               test edi, 0x1083000
008832B7  0F 84 2F 01 00 00               je 0x1408833ec
008832BD  41 BA 00 00 20 00               mov r10d, 0x200000
008832C3  F7 C7 00 40 EC 61               test edi, 0x61ec4000
008832C9  0F 85 BB 01 00 00               jne 0x14088348a
008832CF  85 C9                           test ecx, ecx
008832D1  0F 85 FF 06 00 00               jne 0x1408839d6
008832D7  0F BA E7 0C                     bt edi, 0xc
008832DB  73 09                           jae 0x1408832e6
008832DD  4D 85 FF                        test r15, r15
008832E0  75 04                           jne 0x1408832e6
008832E2  0F BA EF 0D                     bts edi, 0xd
008832E6  4C 8B AC 24 D0 00 00 00         mov r13, qword ptr [rsp + 0xd0]
008832EE  49 39 6D 18                     cmp qword ptr [r13 + 0x18], rbp
008832F2  0F 85 65 07 00 00               jne 0x140883a5d
008832F8  49 8B 4D 38                     mov rcx, qword ptr [r13 + 0x38]
008832FC  48 F7 C1 A0 FF FF FF            test rcx, -0x60
00883303  0F 85 E3 00 00 00               jne 0x1408833ec
00883309  8B C2                           mov eax, edx
0088330B  25 F0 00 00 00                  and eax, 0xf0
00883310  74 04                           je 0x140883316
00883312  83 4E 3C 08                     or dword ptr [rsi + 0x3c], 8
00883316  0F BA E2 1E                     bt edx, 0x1e
0088331A  0F 82 3C 03 00 00               jb 0x14088365c
00883320  8B D9                           mov ebx, ecx
00883322  F6 C1 40                        test cl, 0x40
00883325  0F 85 91 06 00 00               jne 0x1408839bc
0088332B  8B C7                           mov eax, edi
0088332D  41 B8 00 00 01 00               mov r8d, 0x10000
00883333  25 00 00 40 20                  and eax, 0x20400000
00883338  4C 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r8
00883340  3D 00 00 00 20                  cmp eax, 0x20000000
00883345  0F 84 3F 07 00 00               je 0x140883a8a
0088334B  83 E3 1A                        and ebx, 0x1a
0088334E  89 9C 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], ebx
00883355  0F 85 3F 07 00 00               jne 0x140883a9a
0088335B  F6 C1 04                        test cl, 4
0088335E  0F 85 88 00 00 00               jne 0x1408833ec
00883364  8B C7                           mov eax, edi
00883366  25 00 00 40 20                  and eax, 0x20400000
0088336B  3D 00 00 40 00                  cmp eax, 0x400000
00883370  0F 84 CD 05 00 00               je 0x140883943
00883376  0F BA E7 0D                     bt edi, 0xd
0088337A  0F 82 FC 00 00 00               jb 0x14088347c
00883380  49 83 7D 00 00                  cmp qword ptr [r13], 0
00883385  75 65                           jne 0x1408833ec
00883387  49 83 7D 08 00                  cmp qword ptr [r13 + 8], 0
0088338C  75 5E                           jne 0x1408833ec
0088338E  49 83 7D 10 00                  cmp qword ptr [r13 + 0x10], 0
00883393  75 57                           jne 0x1408833ec
00883395  48 83 BC 24 B0 00 00 00 00      cmp qword ptr [rsp + 0xb0], 0
0088339E  49 BB FF FF FE FF FF 7F 00 00   movabs r11, 0x7ffffffeffff
008833A8  0F 85 DE 01 00 00               jne 0x14088358c
008833AE  0F BA E7 12                     bt edi, 0x12
008833B2  0F 82 6E 02 00 00               jb 0x140883626
008833B8  0F BA E7 0E                     bt edi, 0xe
008833BC  0F 82 3A 02 00 00               jb 0x1408835fc
008833C2  0F BA E7 0D                     bt edi, 0xd
008833C6  0F 82 99 00 00 00               jb 0x140883465
008833CC  41 BA 00 10 00 00               mov r10d, 0x1000
008833D2  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
008833D6  48 85 C9                        test rcx, rcx
008833D9  0F 85 EA 04 00 00               jne 0x1408838c9
008833DF  4D 89 55 10                     mov qword ptr [r13 + 0x10], r10
008833E3  4D 85 C9                        test r9, r9
008833E6  0F 85 2F 01 00 00               jne 0x14088351b
008833EC  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008833F1  4D 85 E4                        test r12, r12
008833F4  0F 85 2D 07 00 00               jne 0x140883b27
008833FA  8B C3                           mov eax, ebx
008833FC  48 83 C4 58                     add rsp, 0x58
00883400  41 5F                           pop r15
00883402  41 5E                           pop r14
00883404  41 5D                           pop r13
00883406  41 5C                           pop r12
00883408  5F                              pop rdi
00883409  5E                              pop rsi
0088340A  5D                              pop rbp
0088340B  5B                              pop rbx
0088340C  C3                              ret
0088340D  CC                              int3
0088340E  4C 8B 05 83 36 74 00            mov r8, qword ptr [rip + 0x743683]
00883415  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0088341D  44 0F B6 8C 24 D8 00 00 00      movzx r9d, byte ptr [rsp + 0xd8]
00883426  BA 08 00 00 00                  mov edx, 8
0088342B  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
00883430  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
00883435  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0088343A  C7 44 24 20 4D 6D 56 6D         mov dword ptr [rsp + 0x20], 0x6d566d4d
00883442  E8 09 62 FE FF                  call 0x140869650
00883447  4C 8B A4 24 A0 00 00 00         mov r12, qword ptr [rsp + 0xa0]
0088344F  8B D8                           mov ebx, eax
00883451  85 C0                           test eax, eax
00883453  78 9C                           js 0x1408833f1
00883455  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
0088345D  4D 8B F4                        mov r14, r12
00883460  E9 0E FE FF FF                  jmp 0x140883273
00883465  0F BA E7 1E                     bt edi, 0x1e
00883469  0F 82 EF 03 00 00               jb 0x14088385e
0088346F  4C 8B 94 24 A8 00 00 00         mov r10, qword ptr [rsp + 0xa8]
00883477  E9 56 FF FF FF                  jmp 0x1408833d2
0088347C  4D 85 FF                        test r15, r15
0088347F  0F 84 10 FF FF FF               je 0x140883395
00883485  E9 F6 FE FF FF                  jmp 0x140883380
0088348A  0F BA E7 13                     bt edi, 0x13
0088348E  73 0D                           jae 0x14088349d
00883490  81 FF 00 00 08 00               cmp edi, 0x80000
00883496  74 18                           je 0x1408834b0
00883498  E9 4F FF FF FF                  jmp 0x1408833ec
0088349D  0F BA E7 18                     bt edi, 0x18
008834A1  0F 82 8B 04 00 00               jb 0x140883932
008834A7  41 85 FA                        test r10d, edi
008834AA  0F 85 6C 03 00 00               jne 0x14088381c
008834B0  8B C7                           mov eax, edi
008834B2  25 00 00 40 20                  and eax, 0x20400000
008834B7  3D 00 00 40 20                  cmp eax, 0x20400000
008834BC  0F 84 28 05 00 00               je 0x1408839ea
008834C2  3D 00 00 00 20                  cmp eax, 0x20000000
008834C7  0F 84 DE 04 00 00               je 0x1408839ab
008834CD  0F BA E7 17                     bt edi, 0x17
008834D1  0F 82 7E 04 00 00               jb 0x140883955
008834D7  3D 00 00 40 00                  cmp eax, 0x400000
008834DC  0F 84 19 05 00 00               je 0x1408839fb
008834E2  0F BA E7 1E                     bt edi, 0x1e
008834E6  0F 82 62 05 00 00               jb 0x140883a4e
008834EC  0F BA E7 12                     bt edi, 0x12
008834F0  0F 82 18 04 00 00               jb 0x14088390e
008834F6  0F BA E7 0E                     bt edi, 0xe
008834FA  0F 83 CF FD FF FF               jae 0x1408832cf
00883500  0F BA E7 0D                     bt edi, 0xd
00883504  0F 83 E2 FE FF FF               jae 0x1408833ec
0088350A  F7 C7 FF 8F 9F DF               test edi, 0xdf9f8fff
00883510  0F 85 D6 FE FF FF               jne 0x1408833ec
00883516  E9 B4 FD FF FF                  jmp 0x1408832cf
0088351B  0F BA E7 0D                     bt edi, 0xd
0088351F  73 24                           jae 0x140883545
00883521  8B C7                           mov eax, edi
00883523  25 00 00 40 20                  and eax, 0x20400000
00883528  3D 00 00 40 20                  cmp eax, 0x20400000
0088352D  0F 84 8C 05 00 00               je 0x140883abf
00883533  8B C7                           mov eax, edi
00883535  25 00 00 40 20                  and eax, 0x20400000
0088353A  3D 00 00 00 20                  cmp eax, 0x20000000
0088353F  0F 84 7A 05 00 00               je 0x140883abf
00883545  4F 8D 04 0F                     lea r8, [r15 + r9]
00883549  49 8D 40 FF                     lea rax, [r8 - 1]
0088354D  49 3B C7                        cmp rax, r15
00883550  0F 82 96 FE FF FF               jb 0x1408833ec
00883556  49 3B C3                        cmp rax, r11
00883559  0F 87 8D FE FF FF               ja 0x1408833ec
0088355F  0F BA E7 0D                     bt edi, 0xd
00883563  0F 83 10 01 00 00               jae 0x140883679
00883569  0F BA E7 1E                     bt edi, 0x1e
0088356D  0F 83 33 01 00 00               jae 0x1408836a6
00883573  41 F7 C7 FF 0F 00 00            test r15d, 0xfff
0088357A  0F 85 6C FE FF FF               jne 0x1408833ec
00883580  41 F7 C1 FF 0F 00 00            test r9d, 0xfff
00883587  E9 F8 03 00 00                  jmp 0x140883984
0088358C  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00883594  E8 A7 0E 00 00                  call 0x140884440
00883599  8B D8                           mov ebx, eax
0088359B  85 C0                           test eax, eax
0088359D  0F 88 4E FE FF FF               js 0x1408833f1
008835A3  49 BB FF FF FE FF FF 7F 00 00   movabs r11, 0x7ffffffeffff
008835AD  0F BA E7 0D                     bt edi, 0xd
008835B1  73 2E                           jae 0x1408835e1
008835B3  4D 85 FF                        test r15, r15
008835B6  75 29                           jne 0x1408835e1
008835B8  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008835C0  49 8B D3                        mov rdx, r11
008835C3  48 85 C9                        test rcx, rcx
008835C6  0F 85 E7 02 00 00               jne 0x1408838b3
008835CC  49 8B 86 68 03 00 00            mov rax, qword ptr [r14 + 0x368]
008835D3  48 FF C8                        dec rax
008835D6  48 3B D0                        cmp rdx, rax
008835D9  48 0F 46 C2                     cmovbe rax, rdx
008835DD  49 89 45 08                     mov qword ptr [r13 + 8], rax
008835E1  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
008835E9  8B 94 24 C8 00 00 00            mov edx, dword ptr [rsp + 0xc8]
008835F0  8B 9C 24 F8 00 00 00            mov ebx, dword ptr [rsp + 0xf8]
008835F7  E9 B2 FD FF FF                  jmp 0x1408833ae
008835FC  49 83 7D 00 00                  cmp qword ptr [r13], 0
00883601  0F 85 E5 FD FF FF               jne 0x1408833ec
00883607  49 83 7D 08 00                  cmp qword ptr [r13 + 8], 0
0088360C  0F 85 DA FD FF FF               jne 0x1408833ec
00883612  49 83 7D 10 00                  cmp qword ptr [r13 + 0x10], 0
00883617  0F 85 CF FD FF FF               jne 0x1408833ec
0088361D  81 4E 40 00 00 00 04            or dword ptr [rsi + 0x40], 0x4000000
00883624  EB 11                           jmp 0x140883637
00883626  81 4E 40 00 00 00 08            or dword ptr [rsi + 0x40], 0x8000000
0088362D  0F BA E7 0E                     bt edi, 0xe
00883631  0F 83 8B FD FF FF               jae 0x1408833c2
00883637  85 DB                           test ebx, ebx
00883639  0F 85 30 FE FF FF               jne 0x14088346f
0088363F  8B C7                           mov eax, edi
00883641  25 00 00 40 20                  and eax, 0x20400000
00883646  3D 00 00 00 20                  cmp eax, 0x20000000
0088364B  0F 84 1E FE FF FF               je 0x14088346f
00883651  41 BA 00 10 00 00               mov r10d, 0x1000
00883657  E9 76 FD FF FF                  jmp 0x1408833d2
0088365C  85 C0                           test eax, eax
0088365E  0F 84 88 FD FF FF               je 0x1408833ec
00883664  0F BA F2 1E                     btr edx, 0x1e
00883668  BD 02 00 00 00                  mov ebp, 2
0088366D  89 94 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edx
00883674  E9 A7 FC FF FF                  jmp 0x140883320
00883679  81 FF 00 00 00 01               cmp edi, 0x1000000
0088367F  0F 84 08 02 00 00               je 0x14088388d
00883685  81 FF 00 00 08 00               cmp edi, 0x80000
0088368B  0F 84 FC 01 00 00               je 0x14088388d
00883691  49 FF C8                        dec r8
00883694  49 8D 42 FF                     lea rax, [r10 - 1]
00883698  48 F7 D0                        not rax
0088369B  4D 03 C2                        add r8, r10
0088369E  4C 23 F8                        and r15, rax
008836A1  4C 23 C0                        and r8, rax
008836A4  EB 42                           jmp 0x1408836e8
008836A6  0F BA E7 0E                     bt edi, 0xe
008836AA  0F 82 C7 02 00 00               jb 0x140883977
008836B0  49 F7 DA                        neg r10
008836B3  8B C7                           mov eax, edi
008836B5  4D 23 FA                        and r15, r10
008836B8  25 00 00 40 20                  and eax, 0x20400000
008836BD  3D 00 00 40 20                  cmp eax, 0x20400000
008836C2  0F 84 05 03 00 00               je 0x1408839cd
008836C8  8B C7                           mov eax, edi
008836CA  25 00 00 40 20                  and eax, 0x20400000
008836CF  3D 00 00 00 20                  cmp eax, 0x20000000
008836D4  0F 84 F3 02 00 00               je 0x1408839cd
008836DA  49 81 C0 FF 0F 00 00            add r8, 0xfff
008836E1  49 81 E0 00 F0 FF FF            and r8, 0xfffffffffffff000
008836E8  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
008836ED  4D 2B C7                        sub r8, r15
008836F0  4D 85 D2                        test r10, r10
008836F3  74 04                           je 0x1408836f9
008836F5  4D 89 7D 00                     mov qword ptr [r13], r15
008836F9  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
008836FD  4D 8B 4D 00                     mov r9, qword ptr [r13]
00883701  48 FF C8                        dec rax
00883704  49 85 C1                        test r9, rax
00883707  0F 85 DF FC FF FF               jne 0x1408833ec
0088370D  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00883711  48 85 C9                        test rcx, rcx
00883714  0F 85 75 02 00 00               jne 0x14088398f
0088371A  0F BA E7 0D                     bt edi, 0xd
0088371E  0F 83 18 01 00 00               jae 0x14088383c
00883724  4D 85 D2                        test r10, r10
00883727  0F 85 0F 01 00 00               jne 0x14088383c
0088372D  0F BA E7 0E                     bt edi, 0xe
00883731  0F 82 05 01 00 00               jb 0x14088383c
00883737  49 8B 8E 68 03 00 00            mov rcx, qword ptr [r14 + 0x368]
0088373E  48 FF C9                        dec rcx
00883741  49 3B CB                        cmp rcx, r11
00883744  49 0F 43 CB                     cmovae rcx, r11
00883748  49 89 4D 08                     mov qword ptr [r13 + 8], rcx
0088374C  85 DB                           test ebx, ebx
0088374E  0F 85 96 03 00 00               jne 0x140883aea
00883754  4C 3B C9                        cmp r9, rcx
00883757  0F 83 8F FC FF FF               jae 0x1408833ec
0088375D  48 8B C1                        mov rax, rcx
00883760  49 2B C1                        sub rax, r9
00883763  48 FF C0                        inc rax
00883766  49 3B C0                        cmp rax, r8
00883769  0F 82 7D FC FF FF               jb 0x1408833ec
0088376F  40 F6 C7 7F                     test dil, 0x7f
00883773  0F 85 73 FC FF FF               jne 0x1408833ec
00883779  0F B7 05 80 18 74 00            movzx eax, word ptr [rip + 0x741880]
00883780  45 8B 5D 20                     mov r11d, dword ptr [r13 + 0x20]
00883784  44 3B D8                        cmp r11d, eax
00883787  0F 87 5F FC FF FF               ja 0x1408833ec
0088378D  45 0F B6 55 31                  movzx r10d, byte ptr [r13 + 0x31]
00883792  45 84 D2                        test r10b, r10b
00883795  0F 85 6D 03 00 00               jne 0x140883b08
0088379B  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
0088379F  81 E7 FF BF FB FF               and edi, 0xfffbbfff
008837A5  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
008837A9  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
008837B0  89 46 30                        mov dword ptr [rsi + 0x30], eax
008837B3  0F B6 84 24 D8 00 00 00         movzx eax, byte ptr [rsp + 0xd8]
008837BB  88 46 39                        mov byte ptr [rsi + 0x39], al
008837BE  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
008837C5  09 46 40                        or dword ptr [rsi + 0x40], eax
008837C8  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
008837CF  89 46 44                        mov dword ptr [rsi + 0x44], eax
008837D2  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008837DA  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
008837DE  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
008837E2  48 89 46 68                     mov qword ptr [rsi + 0x68], rax
008837E6  49 8B 45 38                     mov rax, qword ptr [r13 + 0x38]
008837EA  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
008837EE  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
008837F6  4C 89 0E                        mov qword ptr [rsi], r9
008837F9  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
008837FD  4C 89 46 18                     mov qword ptr [rsi + 0x18], r8
00883801  4C 89 20                        mov qword ptr [rax], r12
00883804  33 C0                           xor eax, eax
00883806  89 7E 28                        mov dword ptr [rsi + 0x28], edi
00883809  89 56 2C                        mov dword ptr [rsi + 0x2c], edx
0088380C  44 89 5E 34                     mov dword ptr [rsi + 0x34], r11d
00883810  44 88 56 38                     mov byte ptr [rsi + 0x38], r10b
00883814  89 6E 78                        mov dword ptr [rsi + 0x78], ebp
00883817  E9 E0 FB FF FF                  jmp 0x1408833fc
0088381C  F7 84 24 E0 00 00 00 00 00 04 90  test dword ptr [rsp + 0xe0], 0x90040000
00883827  0F 85 BF FB FF FF               jne 0x1408833ec
0088382D  0F BA E7 0D                     bt edi, 0xd
00883831  0F 82 79 FC FF FF               jb 0x1408834b0
00883837  E9 B0 FB FF FF                  jmp 0x1408833ec
0088383C  4B 8D 0C 01                     lea rcx, [r9 + r8]
00883840  49 3B C9                        cmp rcx, r9
00883843  0F 82 A3 FB FF FF               jb 0x1408833ec
00883849  48 FF C9                        dec rcx
0088384C  49 89 4D 08                     mov qword ptr [r13 + 8], rcx
00883850  49 3B CB                        cmp rcx, r11
00883853  0F 86 FB FE FF FF               jbe 0x140883754
00883859  E9 8E FB FF FF                  jmp 0x1408833ec
0088385E  8B C7                           mov eax, edi
00883860  25 00 00 40 20                  and eax, 0x20400000
00883865  3D 00 00 40 20                  cmp eax, 0x20400000
0088386A  0F 84 7C FB FF FF               je 0x1408833ec
00883870  8B C7                           mov eax, edi
00883872  25 00 00 40 20                  and eax, 0x20400000
00883877  3D 00 00 00 20                  cmp eax, 0x20000000
0088387C  0F 84 6A FB FF FF               je 0x1408833ec
00883882  41 BA 00 10 00 00               mov r10d, 0x1000
00883888  E9 45 FB FF FF                  jmp 0x1408833d2
0088388D  49 FF CF                        dec r15
00883890  49 8D 42 FF                     lea rax, [r10 - 1]
00883894  48 F7 D0                        not rax
00883897  4D 03 FA                        add r15, r10
0088389A  4C 23 F8                        and r15, rax
0088389D  4C 23 C0                        and r8, rax
008838A0  4D 3B F8                        cmp r15, r8
008838A3  0F 82 3F FE FF FF               jb 0x1408836e8
008838A9  BB 18 00 00 C0                  mov ebx, 0xc0000018
008838AE  E9 3E FB FF FF                  jmp 0x1408833f1
008838B3  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
008838BA  48 D3 EA                        shr rdx, cl
008838BD  49 3B D3                        cmp rdx, r11
008838C0  49 0F 47 D3                     cmova rdx, r11
008838C4  E9 03 FD FF FF                  jmp 0x1408835cc
008838C9  49 3B CA                        cmp rcx, r10
008838CC  0F 82 1A FB FF FF               jb 0x1408833ec
008838D2  48 8D 41 FF                     lea rax, [rcx - 1]
008838D6  48 85 C1                        test rcx, rax
008838D9  0F 85 0D FB FF FF               jne 0x1408833ec
008838DF  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
008838E9  48 3B C8                        cmp rcx, rax
008838EC  0F 83 FA FA FF FF               jae 0x1408833ec
008838F2  0F BA E7 1E                     bt edi, 0x1e
008838F6  0F 83 E7 FA FF FF               jae 0x1408833e3
008838FC  48 81 F9 00 10 00 00            cmp rcx, 0x1000
00883903  0F 84 DA FA FF FF               je 0x1408833e3
00883909  E9 DE FA FF FF                  jmp 0x1408833ec
0088390E  0F BA E7 0D                     bt edi, 0xd
00883912  0F 83 D4 FA FF FF               jae 0x1408833ec
00883918  F7 C7 FF DF EB BF               test edi, 0xbfebdfff
0088391E  0F 85 C8 FA FF FF               jne 0x1408833ec
00883924  83 FA 01                        cmp edx, 1
00883927  0F 85 BF FA FF FF               jne 0x1408833ec
0088392D  E9 9D F9 FF FF                  jmp 0x1408832cf
00883932  81 FF 00 00 00 01               cmp edi, 0x1000000
00883938  0F 84 72 FB FF FF               je 0x1408834b0
0088393E  E9 A9 FA FF FF                  jmp 0x1408833ec
00883943  48 F7 C1 E0 FF FF FF            test rcx, -0x20
0088394A  0F 85 9C FA FF FF               jne 0x1408833ec
00883950  E9 21 FA FF FF                  jmp 0x140883376
00883955  F7 C7 00 00 40 40               test edi, 0x40400000
0088395B  0F 85 8B FA FF FF               jne 0x1408833ec
00883961  F7 C2 F9 F9 FF FF               test edx, 0xfffff9f9
00883967  0F 84 7F FB FF FF               je 0x1408834ec
0088396D  BB 45 00 00 C0                  mov ebx, 0xc0000045
00883972  E9 7A FA FF FF                  jmp 0x1408833f1
00883977  49 8B CF                        mov rcx, r15
0088397A  49 8D 42 FF                     lea rax, [r10 - 1]
0088397E  49 0B C9                        or rcx, r9
00883981  48 85 C8                        test rax, rcx
00883984  0F 84 5E FD FF FF               je 0x1408836e8
0088398A  E9 5D FA FF FF                  jmp 0x1408833ec
0088398F  49 3B CB                        cmp rcx, r11
00883992  0F 87 54 FA FF FF               ja 0x1408833ec
00883998  8D 41 01                        lea eax, [rcx + 1]
0088399B  A9 FF 0F 00 00                  test eax, 0xfff
008839A0  0F 84 AE FD FF FF               je 0x140883754
008839A6  E9 41 FA FF FF                  jmp 0x1408833ec
008839AB  F7 C7 00 00 C0 40               test edi, 0x40c00000
008839B1  0F 84 16 FB FF FF               je 0x1408834cd
008839B7  E9 30 FA FF FF                  jmp 0x1408833ec
008839BC  F6 C2 F0                        test dl, 0xf0
008839BF  0F 84 27 FA FF FF               je 0x1408833ec
008839C5  83 CD 08                        or ebp, 8
008839C8  E9 5E F9 FF FF                  jmp 0x14088332b
008839CD  4F 8D 04 0F                     lea r8, [r15 + r9]
008839D1  E9 12 FD FF FF                  jmp 0x1408836e8
008839D6  E8 35 D7 C5 FF                  call 0x1404e1110
008839DB  8B D8                           mov ebx, eax
008839DD  85 C0                           test eax, eax
008839DF  0F 89 F2 F8 FF FF               jns 0x1408832d7
008839E5  E9 07 FA FF FF                  jmp 0x1408833f1
008839EA  F7 C7 00 00 80 40               test edi, 0x40800000
008839F0  0F 84 D7 FA FF FF               je 0x1408834cd
008839F6  E9 F1 F9 FF FF                  jmp 0x1408833ec
008839FB  0F BA E7 0D                     bt edi, 0xd
008839FF  0F 83 E7 F9 FF FF               jae 0x1408833ec
00883A05  F7 C7 FF 9F 8F FF               test edi, 0xff8f9fff
00883A0B  0F 85 DB F9 FF FF               jne 0x1408833ec
00883A11  8B CA                           mov ecx, edx
00883A13  E8 68 5A AA FF                  call 0x140329480
00883A18  83 F8 FF                        cmp eax, -1
00883A1B  0F 84 4C FF FF FF               je 0x14088396d
00883A21  8B C8                           mov ecx, eax
00883A23  83 E1 F8                        and ecx, 0xfffffff8
00883A26  83 F9 10                        cmp ecx, 0x10
00883A29  0F 84 3E FF FF FF               je 0x14088396d
00883A2F  83 E0 07                        and eax, 7
00883A32  83 F8 04                        cmp eax, 4
00883A35  0F 84 C3 53 29 00               je 0x140b18dfe
00883A3B  83 F8 01                        cmp eax, 1
00883A3E  0F 84 BA 53 29 00               je 0x140b18dfe
00883A44  BB 45 00 00 C0                  mov ebx, 0xc0000045
00883A49  E9 A3 F9 FF FF                  jmp 0x1408833f1
00883A4E  0F BA E7 14                     bt edi, 0x14
00883A52  0F 83 94 FA FF FF               jae 0x1408834ec
00883A58  E9 8F F9 FF FF                  jmp 0x1408833ec
00883A5D  8B C7                           mov eax, edi
00883A5F  25 00 00 40 20                  and eax, 0x20400000
00883A64  3D 00 00 00 20                  cmp eax, 0x20000000
00883A69  0F 84 89 F8 FF FF               je 0x1408832f8
00883A6F  3D 00 00 40 20                  cmp eax, 0x20400000
00883A74  0F 85 72 F9 FF FF               jne 0x1408833ec
00883A7A  41 F6 45 38 02                  test byte ptr [r13 + 0x38], 2
00883A7F  0F 84 67 F9 FF FF               je 0x1408833ec
00883A85  E9 6E F8 FF FF                  jmp 0x1408832f8
00883A8A  4D 8B C2                        mov r8, r10
00883A8D  4C 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r10
00883A95  E9 B1 F8 FF FF                  jmp 0x14088334b
00883A9A  8D 43 FF                        lea eax, [rbx - 1]
00883A9D  85 C3                           test ebx, eax
00883A9F  0F 85 47 F9 FF FF               jne 0x1408833ec
00883AA5  F6 C3 02                        test bl, 2
00883AA8  0F 84 9B 53 29 00               je 0x140b18e49
00883AAE  8B C7                           mov eax, edi
00883AB0  25 00 00 40 20                  and eax, 0x20400000
00883AB5  3D 00 00 40 20                  cmp eax, 0x20400000
00883ABA  E9 6D 53 29 00                  jmp 0x140b18e2c
00883ABF  8B C7                           mov eax, edi
00883AC1  25 00 00 40 20                  and eax, 0x20400000
00883AC6  3D 00 00 40 20                  cmp eax, 0x20400000
00883ACB  0F 95 C1                        setne cl
00883ACE  0F BA E7 0C                     bt edi, 0xc
00883AD2  0F 93 C0                        setae al
00883AD5  84 C8                           test al, cl
00883AD7  0F 84 8C 53 29 00               je 0x140b18e69
00883ADD  85 DB                           test ebx, ebx
00883ADF  0F 84 07 F9 FF FF               je 0x1408833ec
00883AE5  E9 7F 53 29 00                  jmp 0x140b18e69
00883AEA  F6 C3 02                        test bl, 2
00883AED  0F 85 61 FC FF FF               jne 0x140883754
00883AF3  F6 C3 08                        test bl, 8
00883AF6  0F 84 7F 53 29 00               je 0x140b18e7b
00883AFC  48 C7 C0 00 00 E0 FF            mov rax, 0xffffffffffe00000
00883B03  E9 83 53 29 00                  jmp 0x140b18e8b
00883B08  85 DB                           test ebx, ebx
00883B0A  0F 85 8B FC FF FF               jne 0x14088379b
00883B10  8B C7                           mov eax, edi
00883B12  25 00 00 40 20                  and eax, 0x20400000
00883B17  3D 00 00 00 20                  cmp eax, 0x20000000
00883B1C  0F 85 CA F8 FF FF               jne 0x1408833ec
00883B22  E9 74 FC FF FF                  jmp 0x14088379b
00883B27  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
00883B2C  49 8B CC                        mov rcx, r12
00883B2F  E8 AC 3D A7 FF                  call 0x1402f78e0
00883B34  E9 C1 F8 FF FF                  jmp 0x1408833fa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateVirtualMemoryPrepare(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, unsigned __int8 a8, unsigned int a9, unsigned int a10, __int64 a11, unsigned int a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p60;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned int v_stack_pC8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (88);
    v_rbp = 0;
    v_stack_m58 = a2;
    *(unsigned __int64 *)(v_rsp + 8) = 0;
    *(unsigned __int64 *)(a12 + 96) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if (a1 != -1) goto loc_0088340E;
loc_00883273:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (0x7F800ULL));
    a2 = (unsigned int)(((unsigned int)(a6)) & (0xFFF807FFULL));
    *(unsigned __int64 *)(a12 + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    *(unsigned __int64 *)(a12 + 32) = a4;
    v_stack_p8 = (unsigned int)(a1);
    v_stack_p30 = (unsigned int)(a2);
    if ((((unsigned int)((unsigned int)(a5))) & (0x9E038FFFULL)) != 0) goto loc_008833EC;
    if ((((unsigned int)((unsigned int)(a5))) & (0x1083000ULL)) == 0) goto loc_008833EC;
    if ((((unsigned int)((unsigned int)(a5))) & (0x61EC4000ULL)) != 0) goto loc_0088348A;
loc_008832CF:
    if ((unsigned int)(a1) != 0) goto loc_008839D6;
loc_008832D7:
    if (condition_is_above_or_equal) goto loc_008832E6;
    if (a2 == 0) {
    }
    if ((*(unsigned __int64 *)(a7 + 24)) != 0) goto loc_00883A5D;
loc_008832F8:
    if (((*(unsigned __int64 *)(a7 + 56)) & (-96)) != 0) goto loc_008833EC;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (240));
    if (!(condition_is_equal)) {
    }
    if (condition_is_below) goto loc_0088365C;
loc_00883320:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a7 + 56))) & (64)) != 0) goto loc_008839BC;
loc_0088332B:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    v_stack_p10 = (unsigned int)(0x10000ULL);
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_00883A8A;
loc_0088334B:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a7 + 56)))) & (26));
    v_stack_p60 = (unsigned int)(v_rbx);
    if (condition_is_not_equal) goto loc_00883A9A;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a7 + 56))) & (4)) != 0) goto loc_008833EC;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x400000ULL) goto loc_00883943;
loc_00883376:
    if (((unsigned int)(result)) < 0x400000ULL) goto loc_0088347C;
loc_00883380:
    if ((*(unsigned __int64 *)(a7)) != 0) goto loc_008833EC;
    if ((*(unsigned __int64 *)(a7 + 8)) != 0) goto loc_008833EC;
    if ((*(unsigned __int64 *)(a7 + 16)) != 0) goto loc_008833EC;
loc_00883395:
    if (v_stack_p18 != 0) goto loc_0088358C;
loc_008833AE:
    if (v_stack_p18 < 0) goto loc_00883626;
    if (v_stack_p18 < 0) goto loc_008835FC;
loc_008833C2:
    if (v_stack_p18 < 0) goto loc_00883465;
loc_008833D2:
    if (*(unsigned __int64 *)(a7 + 16) != 0) goto loc_008838C9;
    *(unsigned __int64 *)(a7 + 16) = (unsigned int)(0x1000ULL);
loc_008833E3:
    if (a4 != 0) goto loc_0088351B;
loc_008833EC:
loc_008833F1:
    if (*(unsigned __int64 *)(v_rsp + 8) != 0) goto loc_00883B27;
loc_008833FA:
loc_008833FC:
    v_rsp = (v_rsp) + (88);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_0088340E:
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_pA0;
    v_stack_p20 = 0x6D566D4DULL;
    result = ObpReferenceObjectByHandleWithTag(*(unsigned __int64 *)(a7 + 16), 8, *(unsigned __int64 *)(v_rip + 7616131), a8);
    if (sign_flag) goto loc_008833F1;
    goto loc_00883273;
loc_00883465:
    if (condition_is_below) goto loc_0088385E;
loc_0088346F:
    goto loc_008833D2;
loc_0088347C:
    if (a2 == 0) goto loc_00883395;
    goto loc_00883380;
loc_0088348A:
    if (condition_is_above_or_equal) goto loc_0088349D;
    if (((unsigned int)((unsigned int)(a5))) == 0x80000ULL) goto loc_008834B0;
    goto loc_008833EC;
loc_0088349D:
    if (((unsigned int)((unsigned int)(a5))) < 0x80000ULL) goto loc_00883932;
    if ((((unsigned int)(v_stack_pA8)) & ((unsigned int)((unsigned int)(a5)))) != 0) goto loc_0088381C;
loc_008834B0:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20400000ULL) goto loc_008839EA;
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_008839AB;
loc_008834CD:
    if (((unsigned int)(result)) < 0x20000000ULL) goto loc_00883955;
    if (((unsigned int)(result)) == 0x400000ULL) goto loc_008839FB;
    if (((unsigned int)(result)) < 0x400000ULL) goto loc_00883A4E;
loc_008834EC:
    if (((unsigned int)(result)) < 0x400000ULL) goto loc_0088390E;
    if (((unsigned int)(result)) >= 0x400000ULL) goto loc_008832CF;
    if (((unsigned int)(result)) >= 0x400000ULL) goto loc_008833EC;
    if ((((unsigned int)((unsigned int)(a5))) & (0xDF9F8FFFULL)) != 0) goto loc_008833EC;
    goto loc_008832CF;
loc_0088351B:
    if (condition_is_above_or_equal) goto loc_00883545;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20400000ULL) goto loc_00883ABF;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_00883ABF;
loc_00883545:
    if ((a2 + v_stack_pB8 * 1 - 1) < a2) goto loc_008833EC;
    if ((a2 + v_stack_pB8 * 1 - 1) > v_rsp) goto loc_008833EC;
    if ((a2 + v_stack_pB8 * 1 - 1) >= v_rsp) goto loc_00883679;
    if ((a2 + v_stack_pB8 * 1 - 1) >= v_rsp) goto loc_008836A6;
    if ((((unsigned int)(a2)) & (0xFFFULL)) != 0) goto loc_008833EC;
    goto loc_00883984;
loc_0088358C:
    result = MiValidateZeroBits(v_stack_pB0, 8, a2 + v_stack_pB8 * 1, v_stack_pB8);
    if (sign_flag) goto loc_008833F1;
    if (condition_is_above_or_equal) goto loc_008835E1;
    if (a2 != 0) goto loc_008835E1;
    if (v_stack_pB0 != 0) goto loc_008838B3;
loc_008835CC:
    result = (*(unsigned __int64 *)(v_stack_pA0 + 872)) - 1;
    if (v_rsp <= result) { result = v_rsp; }
    *(unsigned __int64 *)(a7 + 8) = result;
loc_008835E1:
    goto loc_008833AE;
loc_008835FC:
    if ((*(unsigned __int64 *)(a7)) != 0) goto loc_008833EC;
    if ((*(unsigned __int64 *)(a7 + 8)) != 0) goto loc_008833EC;
    if ((*(unsigned __int64 *)(a7 + 16)) != 0) goto loc_008833EC;
    goto loc_00883637;
loc_00883626:
    if ((*(unsigned __int64 *)(a7 + 16)) >= 0) goto loc_008833C2;
loc_00883637:
    if ((unsigned int)((unsigned int)(a12)) != 0) goto loc_0088346F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_0088346F;
    goto loc_008833D2;
loc_0088365C:
    if ((unsigned int)(result) == 0) goto loc_008833EC;
    v_stack_pC8 = (unsigned int)((unsigned int)(a6));
    goto loc_00883320;
loc_00883679:
    if (((unsigned int)((unsigned int)(a5))) == 0x1000000ULL) goto loc_0088388D;
    if (((unsigned int)((unsigned int)(a5))) == 0x80000ULL) goto loc_0088388D;
    a3 = (a2 + v_stack_pB8 * 1) - 1;
    result = ~((unsigned int)(0x1000ULL) - 1);
    a3 = (a3) + ((unsigned int)(0x1000ULL));
    v_r15 = (a2) & (result);
    a3 = (a3) & (result);
    goto loc_008836E8;
loc_008836A6:
    if (condition_is_below) goto loc_00883977;
    v_r10 = -((unsigned int)(0x1000ULL));
    v_r15 = (v_r15) & (v_r10);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20400000ULL) goto loc_008839CD;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_008839CD;
    a3 = (a3) + (0xFFFULL);
    a3 = (a3) & (0xFFFFFFFFFFFFF000ULL);
loc_008836E8:
    a3 = (a3) - (v_r15);
    if (v_stack_p40 != 0) {
        *(unsigned __int64 *)(a7) = v_r15;
    }
    result = (*(unsigned __int64 *)(a7 + 16)) - 1;
    if (((*(unsigned __int64 *)(a7)) & (result)) != 0) goto loc_008833EC;
    if (*(unsigned __int64 *)(a7 + 8) != 0) goto loc_0088398F;
    if (condition_is_above_or_equal) goto loc_0088383C;
    if (v_stack_p40 != 0) goto loc_0088383C;
    if (condition_is_below) goto loc_0088383C;
    a1 = (*(unsigned __int64 *)(v_stack_pA0 + 872)) - 1;
    if (a1 >= v_rsp) { a1 = v_rsp; }
    *(unsigned __int64 *)(a7 + 8) = a1;
    if ((unsigned int)((unsigned int)(a12)) != 0) goto loc_00883AEA;
loc_00883754:
    if ((*(unsigned __int64 *)(a7)) >= a1) goto loc_008833EC;
    result = (a1) - (*(unsigned __int64 *)(a7));
    result = (result) + 1;
    if (result < a3) goto loc_008833EC;
    if ((((unsigned __int8)((unsigned int)(a5))) & (127)) != 0) goto loc_008833EC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 32)))) > ((unsigned int)(*(unsigned __int16 *)(v_rip + 7608448)))) goto loc_008833EC;
    if ((unsigned __int8)(*(unsigned __int8 *)(a7 + 49)) != 0) goto loc_00883B08;
loc_0088379B:
    v_rdi = (unsigned int)(((unsigned int)(a5)) & (0xFFFBBFFFULL));
    *(unsigned __int64 *)(a12 + 16) = *(unsigned __int64 *)(a7 + 16);
    *(unsigned int *)(a12 + 48) = (unsigned int)((unsigned int)(v_stack_pA0));
    *(unsigned __int8 *)(a12 + 57) = a8;
    *(unsigned int *)(a12 + 68) = (unsigned int)((unsigned int)(a10));
    *(unsigned __int64 *)(a12 + 72) = a11;
    *(unsigned __int64 *)(a12 + 104) = *(unsigned __int64 *)(a7 + 40);
    *(unsigned __int64 *)(a12 + 112) = *(unsigned __int64 *)(a7 + 56);
    *(unsigned __int64 *)(a12) = *(unsigned __int64 *)(a7);
    *(unsigned __int64 *)(a12 + 8) = a1;
    *(unsigned __int64 *)(a12 + 24) = a3;
    *(unsigned __int64 *)(a13) = v_stack_pA0;
    result = 0;
    *(unsigned int *)(a12 + 40) = (unsigned int)(v_rdi);
    *(unsigned int *)(a12 + 44) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(a12 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(a7 + 32)));
    *(unsigned __int8 *)(a12 + 56) = (unsigned __int8)(*(unsigned __int8 *)(a7 + 49));
    *(unsigned int *)(a12 + 120) = 2;
    goto loc_008833FC;
loc_0088381C:
    if (((a9) & (0x90040000ULL)) != 0) goto loc_008833EC;
    if (condition_is_below) goto loc_008834B0;
    goto loc_008833EC;
loc_0088383C:
    if ((*(unsigned __int64 *)(a7) + a3 * 1) < (*(unsigned __int64 *)(a7))) goto loc_008833EC;
    a1 = (*(unsigned __int64 *)(a7) + a3 * 1) - 1;
    *(unsigned __int64 *)(a7 + 8) = a1;
    if (a1 <= ((unsigned int)(*(unsigned int *)(a7 + 32)))) goto loc_00883754;
    goto loc_008833EC;
loc_0088385E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20400000ULL) goto loc_008833EC;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_008833EC;
    goto loc_008833D2;
loc_0088388D:
    v_r15 = (v_r15) - 1;
    result = ~((unsigned int)(0x1000ULL) - 1);
    v_r15 = (v_r15) + ((unsigned int)(0x1000ULL));
    v_r15 = (v_r15) & (result);
    a3 = (a3) & (result);
    if (v_r15 < a3) goto loc_008836E8;
    goto loc_008833F1;
loc_008838B3:
    a2 = (-1) >> ((unsigned __int8)(a1));
    if (a2 > ((unsigned int)(*(unsigned int *)(a7 + 32)))) { a2 = (unsigned int)(*(unsigned int *)(a7 + 32)); }
    goto loc_008835CC;
loc_008838C9:
    if (a1 < ((unsigned int)(0x1000ULL))) goto loc_008833EC;
    if (((a1) & (a1 - 1)) != 0) goto loc_008833EC;
    if (a1 >= (a1 - 1)) goto loc_008833EC;
    if (a1 >= (a1 - 1)) goto loc_008833E3;
    if (a1 == 0x1000ULL) goto loc_008833E3;
    goto loc_008833EC;
loc_0088390E:
    if (a1 >= 0x1000ULL) goto loc_008833EC;
    if ((((unsigned int)(v_rdi)) & (0xBFEBDFFFULL)) != 0) goto loc_008833EC;
    if (((unsigned int)(a2)) != 1) goto loc_008833EC;
    goto loc_008832CF;
loc_00883932:
    if (((unsigned int)(v_rdi)) == 0x1000000ULL) goto loc_008834B0;
    goto loc_008833EC;
loc_00883943:
    if (((a1) & (-32)) != 0) goto loc_008833EC;
    goto loc_00883376;
loc_00883955:
    if ((((unsigned int)(v_rdi)) & (0x40400000ULL)) != 0) goto loc_008833EC;
    if ((((unsigned int)(a2)) & (0xFFFFF9F9ULL)) == 0) goto loc_008834EC;
loc_0088396D:
    goto loc_008833F1;
loc_00883977:
    a1 = (v_r15) | (*(unsigned __int64 *)(a7));
loc_00883984:
    if ((((unsigned int)(0x1000ULL) - 1) & (a1)) == 0) goto loc_008836E8;
    goto loc_008833EC;
loc_0088398F:
    if (a1 > ((unsigned int)(*(unsigned int *)(a7 + 32)))) goto loc_008833EC;
    if ((((unsigned int)(a1 + 1)) & (0xFFFULL)) == 0) goto loc_00883754;
    goto loc_008833EC;
loc_008839AB:
    if ((((unsigned int)(v_rdi)) & (0x40C00000ULL)) == 0) goto loc_008834CD;
    goto loc_008833EC;
loc_008839BC:
    if ((((unsigned __int8)(a2)) & (240)) == 0) goto loc_008833EC;
    v_rbp = (unsigned int)((2) | (8));
    goto loc_0088332B;
loc_008839CD:
    goto loc_008836E8;
loc_008839D6:
    result = DefaultAddProfileSource(a1, a2, v_r15 + *(unsigned __int64 *)(a7) * 1, *(unsigned __int64 *)(a7));
    if (!sign_flag) goto loc_008832D7;
    goto loc_008833F1;
loc_008839EA:
    if ((((unsigned int)(v_rdi)) & (0x40800000ULL)) == 0) goto loc_008834CD;
    goto loc_008833EC;
loc_008839FB:
    if (condition_is_above_or_equal) goto loc_008833EC;
    if ((((unsigned int)(v_rdi)) & (0xFF8F9FFFULL)) != 0) goto loc_008833EC;
    result = MiMakeProtectionMask((unsigned int)((unsigned int)(a2)), a2, v_r15 + *(unsigned __int64 *)(a7) * 1, *(unsigned __int64 *)(a7));
    if (((unsigned int)(result)) == -1) goto loc_0088396D;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a1)) == 16) goto loc_0088396D;
    result = (unsigned int)((result) & (7));
    goto loc_008833F1;
loc_00883A4E:
    if (((unsigned int)(result)) >= 1) goto loc_008834EC;
    goto loc_008833EC;
loc_00883A5D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x20400000ULL));
    if (((unsigned int)(result)) == 0x20000000ULL) goto loc_008832F8;
    if (((unsigned int)(result)) != 0x20400000ULL) goto loc_008833EC;
    if (((*(unsigned __int8 *)(a7 + 56)) & (2)) == 0) goto loc_008833EC;
    goto loc_008832F8;
loc_00883A8A:
    v_stack_pA8 = (unsigned int)(0x1000ULL);
    goto loc_0088334B;
loc_00883A9A:
    if ((((unsigned int)((unsigned int)(0xC0000045ULL))) & ((unsigned int)((unsigned int)(0xC0000045ULL) - 1))) != 0) goto loc_008833EC;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x20400000ULL));
loc_00883ABF:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x20400000ULL));
    a1 = (((unsigned int)(result)) != 0x20400000ULL) ? 1 : 0;
    result = (((unsigned int)(result)) >= 0x20400000ULL) ? 1 : 0;
    if ((unsigned int)((unsigned int)(0xC0000045ULL)) == 0) goto loc_008833EC;
loc_00883AEA:
    if ((((unsigned __int8)((unsigned int)(0xC0000045ULL))) & (2)) != 0) goto loc_00883754;
loc_00883B08:
    if ((unsigned int)((unsigned int)(0xC0000045ULL)) != 0) goto loc_0088379B;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x20400000ULL));
    if (((unsigned int)(result)) != 0x20000000ULL) goto loc_008833EC;
    goto loc_0088379B;
loc_00883B27:
    result = ObfDereferenceObjectWithTag(v_stack_pA0, (unsigned int)(0x6D566D4DULL), (unsigned int)(0x1000ULL), *(unsigned __int64 *)(a7));
    goto loc_008833FA;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateVirtualMemoryPrepare(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, void *Arg7, uint8_t Arg8, uint32_t Arg9, uint32_t Arg10, int64_t Arg11, void *Arg12, void *Arg13)
{
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p60;
    uint32_t v_stack_p8;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint32_t v_stack_pC8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (88);
    local_rbp = 0;
    v_stack_m58 = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = 0;
    *(uint64_t *)(arg12 + 0x60) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if (Arg1 != -1) goto loc_0088340E;
loc_00883273:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (0x7F800ULL));
    Arg2 = (uint32_t)(((uint32_t)(Arg6)) & (0xFFF807FFULL));
    *(uint64_t *)(arg12 + 0x58) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    *(uint64_t *)(arg12 + 0x20) = Arg4;
    v_stack_p8 = (uint32_t)(Arg1);
    v_stack_p30 = (uint32_t)(Arg2);
    if ((((uint32_t)((uint32_t)(Arg5))) & (0x9E038FFFULL)) != 0) goto loc_008833EC;
    if ((((uint32_t)((uint32_t)(Arg5))) & (0x1083000ULL)) == 0) goto loc_008833EC;
    if ((((uint32_t)((uint32_t)(Arg5))) & (0x61EC4000ULL)) != 0) goto loc_0088348A;
loc_008832CF:
    if ((uint32_t)(Arg1) != 0) goto loc_008839D6;
loc_008832D7:
    if (condition_is_above_or_equal) goto loc_008832E6;
    if (Arg2 == 0) {
    }
    if ((*(uint64_t *)(arg7 + 0x18)) != 0) goto loc_00883A5D;
loc_008832F8:
    if (((*(uint64_t *)(arg7 + 0x38)) & (-96)) != 0) goto loc_008833EC;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (240));
    if (!(condition_is_equal)) {
    }
    if (condition_is_below) goto loc_0088365C;
loc_00883320:
    if ((((uint8_t)(*(uint64_t *)(arg7 + 0x38))) & (64)) != 0) goto loc_008839BC;
loc_0088332B:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    v_stack_p10 = (uint32_t)(0x10000ULL);
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_00883A8A;
loc_0088334B:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg7 + 0x38)))) & (26));
    v_stack_p60 = (uint32_t)(local_rbx);
    if (condition_is_not_equal) goto loc_00883A9A;
    if ((((uint8_t)(*(uint64_t *)(arg7 + 0x38))) & (4)) != 0) goto loc_008833EC;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x400000ULL) goto loc_00883943;
loc_00883376:
    if (((uint32_t)(result)) < 0x400000ULL) goto loc_0088347C;
loc_00883380:
    if ((*(uint64_t *)(arg7)) != 0) goto loc_008833EC;
    if ((*(uint64_t *)(arg7 + 0x8)) != 0) goto loc_008833EC;
    if ((*(uint64_t *)(arg7 + 0x10)) != 0) goto loc_008833EC;
loc_00883395:
    if (v_stack_p18 != 0) goto loc_0088358C;
loc_008833AE:
    if (v_stack_p18 < 0) goto loc_00883626;
    if (v_stack_p18 < 0) goto loc_008835FC;
loc_008833C2:
    if (v_stack_p18 < 0) goto loc_00883465;
loc_008833D2:
    if (*(uint64_t *)(arg7 + 0x10) != 0) goto loc_008838C9;
    *(uint64_t *)(arg7 + 0x10) = (uint32_t)(0x1000ULL);
loc_008833E3:
    if (Arg4 != 0) goto loc_0088351B;
loc_008833EC:
loc_008833F1:
    if (*(uint64_t *)(local_rsp + 0x8) != 0) goto loc_00883B27;
loc_008833FA:
loc_008833FC:
    local_rsp = (local_rsp) + (88);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_0088340E:
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_pA0;
    v_stack_p20 = 0x6D566D4DULL;
    result = ObpReferenceObjectByHandleWithTag(*(uint64_t *)(arg7 + 0x10), 8, *(uint64_t *)(v_rip + 0x743683), Arg8);
    if (sign_flag) goto loc_008833F1;
    goto loc_00883273;
loc_00883465:
    if (condition_is_below) goto loc_0088385E;
loc_0088346F:
    goto loc_008833D2;
loc_0088347C:
    if (Arg2 == 0) goto loc_00883395;
    goto loc_00883380;
loc_0088348A:
    if (condition_is_above_or_equal) goto loc_0088349D;
    if (((uint32_t)((uint32_t)(Arg5))) == 0x80000ULL) goto loc_008834B0;
    goto loc_008833EC;
loc_0088349D:
    if (((uint32_t)((uint32_t)(Arg5))) < 0x80000ULL) goto loc_00883932;
    if ((((uint32_t)(v_stack_pA8)) & ((uint32_t)((uint32_t)(Arg5)))) != 0) goto loc_0088381C;
loc_008834B0:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20400000ULL) goto loc_008839EA;
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_008839AB;
loc_008834CD:
    if (((uint32_t)(result)) < 0x20000000ULL) goto loc_00883955;
    if (((uint32_t)(result)) == 0x400000ULL) goto loc_008839FB;
    if (((uint32_t)(result)) < 0x400000ULL) goto loc_00883A4E;
loc_008834EC:
    if (((uint32_t)(result)) < 0x400000ULL) goto loc_0088390E;
    if (((uint32_t)(result)) >= 0x400000ULL) goto loc_008832CF;
    if (((uint32_t)(result)) >= 0x400000ULL) goto loc_008833EC;
    if ((((uint32_t)((uint32_t)(Arg5))) & (0xDF9F8FFFULL)) != 0) goto loc_008833EC;
    goto loc_008832CF;
loc_0088351B:
    if (condition_is_above_or_equal) goto loc_00883545;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20400000ULL) goto loc_00883ABF;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_00883ABF;
loc_00883545:
    if ((Arg2 + v_stack_pB8 * 1 - 1) < Arg2) goto loc_008833EC;
    if ((Arg2 + v_stack_pB8 * 1 - 1) > local_rsp) goto loc_008833EC;
    if ((Arg2 + v_stack_pB8 * 1 - 1) >= local_rsp) goto loc_00883679;
    if ((Arg2 + v_stack_pB8 * 1 - 1) >= local_rsp) goto loc_008836A6;
    if ((((uint32_t)(Arg2)) & (0xFFFULL)) != 0) goto loc_008833EC;
    goto loc_00883984;
loc_0088358C:
    result = MiValidateZeroBits(v_stack_pB0, 8, Arg2 + v_stack_pB8 * 1, v_stack_pB8);
    if (sign_flag) goto loc_008833F1;
    if (condition_is_above_or_equal) goto loc_008835E1;
    if (Arg2 != 0) goto loc_008835E1;
    if (v_stack_pB0 != 0) goto loc_008838B3;
loc_008835CC:
    result = (*(uint64_t *)(v_stack_pA0 + 0x368)) - 1;
    if (local_rsp <= result) { result = local_rsp; }
    *(uint64_t *)(arg7 + 0x8) = result;
loc_008835E1:
    goto loc_008833AE;
loc_008835FC:
    if ((*(uint64_t *)(arg7)) != 0) goto loc_008833EC;
    if ((*(uint64_t *)(arg7 + 0x8)) != 0) goto loc_008833EC;
    if ((*(uint64_t *)(arg7 + 0x10)) != 0) goto loc_008833EC;
    goto loc_00883637;
loc_00883626:
    if ((*(uint64_t *)(arg7 + 0x10)) >= 0) goto loc_008833C2;
loc_00883637:
    if ((uint32_t)((uint32_t)(Arg12)) != 0) goto loc_0088346F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_0088346F;
    goto loc_008833D2;
loc_0088365C:
    if ((uint32_t)(result) == 0) goto loc_008833EC;
    v_stack_pC8 = (uint32_t)((uint32_t)(Arg6));
    goto loc_00883320;
loc_00883679:
    if (((uint32_t)((uint32_t)(Arg5))) == 0x1000000ULL) goto loc_0088388D;
    if (((uint32_t)((uint32_t)(Arg5))) == 0x80000ULL) goto loc_0088388D;
    Arg3 = (Arg2 + v_stack_pB8 * 1) - 1;
    result = ~((uint32_t)(0x1000ULL) - 1);
    Arg3 = (Arg3) + ((uint32_t)(0x1000ULL));
    local_r15 = (Arg2) & (result);
    Arg3 = (Arg3) & (result);
    goto loc_008836E8;
loc_008836A6:
    if (condition_is_below) goto loc_00883977;
    local_r10 = -((uint32_t)(0x1000ULL));
    local_r15 = (local_r15) & (local_r10);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20400000ULL) goto loc_008839CD;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_008839CD;
    Arg3 = (Arg3) + (0xFFFULL);
    Arg3 = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
loc_008836E8:
    Arg3 = (Arg3) - (local_r15);
    if (v_stack_p40 != 0) {
        *(uint64_t *)(arg7) = local_r15;
    }
    result = (*(uint64_t *)(arg7 + 0x10)) - 1;
    if (((*(uint64_t *)(arg7)) & (result)) != 0) goto loc_008833EC;
    if (*(uint64_t *)(arg7 + 0x8) != 0) goto loc_0088398F;
    if (condition_is_above_or_equal) goto loc_0088383C;
    if (v_stack_p40 != 0) goto loc_0088383C;
    if (condition_is_below) goto loc_0088383C;
    Arg1 = (*(uint64_t *)(v_stack_pA0 + 0x368)) - 1;
    if (Arg1 >= local_rsp) { Arg1 = local_rsp; }
    *(uint64_t *)(arg7 + 0x8) = Arg1;
    if ((uint32_t)((uint32_t)(Arg12)) != 0) goto loc_00883AEA;
loc_00883754:
    if ((*(uint64_t *)(arg7)) >= Arg1) goto loc_008833EC;
    result = (Arg1) - (*(uint64_t *)(arg7));
    result = (result) + 1;
    if (result < Arg3) goto loc_008833EC;
    if ((((uint8_t)((uint32_t)(Arg5))) & (127)) != 0) goto loc_008833EC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x20)))) > ((uint32_t)(*(uint16_t *)(v_rip + 0x741880)))) goto loc_008833EC;
    if ((uint8_t)(*(uint8_t *)(arg7 + 0x31)) != 0) goto loc_00883B08;
loc_0088379B:
    local_rdi = (uint32_t)(((uint32_t)(Arg5)) & (0xFFFBBFFFULL));
    *(uint64_t *)(arg12 + 0x10) = *(uint64_t *)(arg7 + 0x10);
    *(uint32_t *)(arg12 + 0x30) = (uint32_t)((uint32_t)(v_stack_pA0));
    *(uint8_t *)(arg12 + 0x39) = Arg8;
    *(uint32_t *)(arg12 + 0x44) = (uint32_t)((uint32_t)(Arg10));
    *(uint64_t *)(arg12 + 0x48) = Arg11;
    *(uint64_t *)(arg12 + 0x68) = *(uint64_t *)(arg7 + 0x28);
    *(uint64_t *)(arg12 + 0x70) = *(uint64_t *)(arg7 + 0x38);
    *(uint64_t *)(arg12) = *(uint64_t *)(arg7);
    *(uint64_t *)(arg12 + 0x8) = Arg1;
    *(uint64_t *)(arg12 + 0x18) = Arg3;
    *(uint64_t *)(arg13) = v_stack_pA0;
    result = 0;
    *(uint32_t *)(arg12 + 0x28) = (uint32_t)(local_rdi);
    *(uint32_t *)(arg12 + 0x2C) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(arg12 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x20)));
    *(uint8_t *)(arg12 + 0x38) = (uint8_t)(*(uint8_t *)(arg7 + 0x31));
    *(uint32_t *)(arg12 + 0x78) = 2;
    goto loc_008833FC;
loc_0088381C:
    if (((Arg9) & (0x90040000ULL)) != 0) goto loc_008833EC;
    if (condition_is_below) goto loc_008834B0;
    goto loc_008833EC;
loc_0088383C:
    if ((*(uint64_t *)(arg7) + Arg3 * 1) < (*(uint64_t *)(arg7))) goto loc_008833EC;
    Arg1 = (*(uint64_t *)(arg7) + Arg3 * 1) - 1;
    *(uint64_t *)(arg7 + 0x8) = Arg1;
    if (Arg1 <= ((uint32_t)(*(uint32_t *)(arg7 + 0x20)))) goto loc_00883754;
    goto loc_008833EC;
loc_0088385E:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20400000ULL) goto loc_008833EC;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_008833EC;
    goto loc_008833D2;
loc_0088388D:
    local_r15 = (local_r15) - 1;
    result = ~((uint32_t)(0x1000ULL) - 1);
    local_r15 = (local_r15) + ((uint32_t)(0x1000ULL));
    local_r15 = (local_r15) & (result);
    Arg3 = (Arg3) & (result);
    if (local_r15 < Arg3) goto loc_008836E8;
    goto loc_008833F1;
loc_008838B3:
    Arg2 = (-1) >> ((uint8_t)(Arg1));
    if (Arg2 > ((uint32_t)(*(uint32_t *)(arg7 + 0x20)))) { Arg2 = (uint32_t)(*(uint32_t *)(arg7 + 0x20)); }
    goto loc_008835CC;
loc_008838C9:
    if (Arg1 < ((uint32_t)(0x1000ULL))) goto loc_008833EC;
    if (((Arg1) & (Arg1 - 1)) != 0) goto loc_008833EC;
    if (Arg1 >= (Arg1 - 1)) goto loc_008833EC;
    if (Arg1 >= (Arg1 - 1)) goto loc_008833E3;
    if (Arg1 == 0x1000ULL) goto loc_008833E3;
    goto loc_008833EC;
loc_0088390E:
    if (Arg1 >= 0x1000ULL) goto loc_008833EC;
    if ((((uint32_t)(local_rdi)) & (0xBFEBDFFFULL)) != 0) goto loc_008833EC;
    if (((uint32_t)(Arg2)) != 1) goto loc_008833EC;
    goto loc_008832CF;
loc_00883932:
    if (((uint32_t)(local_rdi)) == 0x1000000ULL) goto loc_008834B0;
    goto loc_008833EC;
loc_00883943:
    if (((Arg1) & (-32)) != 0) goto loc_008833EC;
    goto loc_00883376;
loc_00883955:
    if ((((uint32_t)(local_rdi)) & (0x40400000ULL)) != 0) goto loc_008833EC;
    if ((((uint32_t)(Arg2)) & (0xFFFFF9F9ULL)) == 0) goto loc_008834EC;
loc_0088396D:
    goto loc_008833F1;
loc_00883977:
    Arg1 = (local_r15) | (*(uint64_t *)(arg7));
loc_00883984:
    if ((((uint32_t)(0x1000ULL) - 1) & (Arg1)) == 0) goto loc_008836E8;
    goto loc_008833EC;
loc_0088398F:
    if (Arg1 > ((uint32_t)(*(uint32_t *)(arg7 + 0x20)))) goto loc_008833EC;
    if ((((uint32_t)(Arg1 + 1)) & (0xFFFULL)) == 0) goto loc_00883754;
    goto loc_008833EC;
loc_008839AB:
    if ((((uint32_t)(local_rdi)) & (0x40C00000ULL)) == 0) goto loc_008834CD;
    goto loc_008833EC;
loc_008839BC:
    if ((((uint8_t)(Arg2)) & (240)) == 0) goto loc_008833EC;
    local_rbp = (uint32_t)((2) | (8));
    goto loc_0088332B;
loc_008839CD:
    goto loc_008836E8;
loc_008839D6:
    result = DefaultAddProfileSource(Arg1, Arg2, local_r15 + *(uint64_t *)(arg7) * 1, *(uint64_t *)(arg7));
    if (!sign_flag) goto loc_008832D7;
    goto loc_008833F1;
loc_008839EA:
    if ((((uint32_t)(local_rdi)) & (0x40800000ULL)) == 0) goto loc_008834CD;
    goto loc_008833EC;
loc_008839FB:
    if (condition_is_above_or_equal) goto loc_008833EC;
    if ((((uint32_t)(local_rdi)) & (0xFF8F9FFFULL)) != 0) goto loc_008833EC;
    result = MiMakeProtectionMask((uint32_t)((uint32_t)(Arg2)), Arg2, local_r15 + *(uint64_t *)(arg7) * 1, *(uint64_t *)(arg7));
    if (((uint32_t)(result)) == -1) goto loc_0088396D;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg1)) == 16) goto loc_0088396D;
    result = (uint32_t)((result) & (7));
    goto loc_008833F1;
loc_00883A4E:
    if (((uint32_t)(result)) >= 1) goto loc_008834EC;
    goto loc_008833EC;
loc_00883A5D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x20400000ULL));
    if (((uint32_t)(result)) == 0x20000000ULL) goto loc_008832F8;
    if (((uint32_t)(result)) != 0x20400000ULL) goto loc_008833EC;
    if (((*(uint8_t *)(arg7 + 0x38)) & (2)) == 0) goto loc_008833EC;
    goto loc_008832F8;
loc_00883A8A:
    v_stack_pA8 = (uint32_t)(0x1000ULL);
    goto loc_0088334B;
loc_00883A9A:
    if ((((uint32_t)((uint32_t)(0xC0000045ULL))) & ((uint32_t)((uint32_t)(0xC0000045ULL) - 1))) != 0) goto loc_008833EC;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x20400000ULL));
loc_00883ABF:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x20400000ULL));
    Arg1 = (((uint32_t)(result)) != 0x20400000ULL) ? 1 : 0;
    result = (((uint32_t)(result)) >= 0x20400000ULL) ? 1 : 0;
    if ((uint32_t)((uint32_t)(0xC0000045ULL)) == 0) goto loc_008833EC;
loc_00883AEA:
    if ((((uint8_t)((uint32_t)(0xC0000045ULL))) & (2)) != 0) goto loc_00883754;
loc_00883B08:
    if ((uint32_t)((uint32_t)(0xC0000045ULL)) != 0) goto loc_0088379B;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x20400000ULL));
    if (((uint32_t)(result)) != 0x20000000ULL) goto loc_008833EC;
    goto loc_0088379B;
loc_00883B27:
    result = ObfDereferenceObjectWithTag(v_stack_pA0, (uint32_t)(0x6D566D4DULL), (uint32_t)(0x1000ULL), *(uint64_t *)(arg7));
    goto loc_008833FA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x8` | `64` | `R` |
| `Arg7` | `+ 0x8` | `64` | `W` |
| `Arg7` | `+ 0x10` | `64` | `R` |
| `Arg7` | `+ 0x10` | `64` | `W` |
| `Arg7` | `+ 0x18` | `64` | `R` |
| `Arg7` | `+ 0x20` | `32` | `R` |
| `Arg7` | `+ 0x28` | `64` | `R` |
| `Arg7` | `+ 0x31` | `8` | `R` |
| `Arg7` | `+ 0x38` | `8` | `R` |
| `Arg7` | `+ 0x38` | `64` | `R` |
| `Arg12` | `+ 0x0` | `64` | `W` |
| `Arg12` | `+ 0x8` | `64` | `W` |
| `Arg12` | `+ 0x10` | `64` | `W` |
| `Arg12` | `+ 0x18` | `64` | `W` |
| `Arg12` | `+ 0x20` | `64` | `W` |
| `Arg12` | `+ 0x28` | `32` | `W` |
| `Arg12` | `+ 0x2C` | `32` | `W` |
| `Arg12` | `+ 0x30` | `32` | `W` |
| `Arg12` | `+ 0x34` | `32` | `W` |
| `Arg12` | `+ 0x38` | `8` | `W` |
| `Arg12` | `+ 0x39` | `8` | `W` |
| `Arg12` | `+ 0x3C` | `32` | `R/W` |
| `Arg12` | `+ 0x40` | `32` | `R/W` |
| `Arg12` | `+ 0x44` | `32` | `W` |
| `Arg12` | `+ 0x48` | `64` | `W` |
| `Arg12` | `+ 0x58` | `64` | `W` |
| `Arg12` | `+ 0x60` | `64` | `W` |
| `Arg12` | `+ 0x68` | `64` | `W` |
| `Arg12` | `+ 0x70` | `64` | `W` |
| `Arg12` | `+ 0x78` | `32` | `W` |

추가 오프셋 1개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00883220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
