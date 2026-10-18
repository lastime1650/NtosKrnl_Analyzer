# sub_00B19FF6

- RVA: `0x00B19FF6`–`0x00B1A403` (길이 `1,037` bytes)
- VA: `0x0000000140B19FF6`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F71C`
- 디코드: `258`개 명령, `1,037/1,037` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B1A03E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00B1A048` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B1A052` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00B1A10B` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00B1A17B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B1A1D1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00B1A1DF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B1A1ED` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00B1A205` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B1A21E` → [IoCheckEaBufferValidity](../A2/IoCheckEaBufferValidity_function_00A2B9F0.md) (function, `0x00A2B9F0`)
- `0x00B1A234` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B1A344` → [FsRtlAllocateExtraCreateParameterList](../9D/FsRtlAllocateExtraCreateParameterList_function_009D6200.md) (function, `0x009D6200`)
- `0x00B1A37A` → [FsRtlInsertExtraCreateParameter](../8A/FsRtlInsertExtraCreateParameter_function_008A1F30.md) (function, `0x008A1F30`)
- `0x00B1A397` → [FsRtlpPrepareExtraCreateParametersForCreate](../8A/FsRtlpPrepareExtraCreateParametersForCreate_function_008AC120.md) (function, `0x008AC120`)
- `0x00B1A3B9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B1A3DC` → [IopCloseFile](../86/IopCloseFile_function_008640C0.md) (function, `0x008640C0`)
- `0x00B1A3EA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B1A3F4` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B1A02F` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x00B1A25D` → RVA `0x00013E70` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00B1A03E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00B1A048` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B1A052` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00B1A10B` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00B1A17B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B1A1D1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00B1A1DF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B1A1ED` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00B1A205` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B1A234` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B1A3B9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00B1A3EA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B1A3F4` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **15**
  - `0x00B1A05C` → [IopCreateFile + 0x5DF](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A0B1` → [IopCreateFile + 0x11B](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A11D` → [IopCreateFile + 0x11B](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A164` → [IopCreateFile + 0x65B](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A1D7` → [IopCreateFile + 0xD8D](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A1E5` → [IopCreateFile + 0xD8D](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A1F3` → [IopCreateFile + 0xD8D](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A23D` → [IopCreateFile + 0x5B3](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A249` → [IopCreateFile + 0x25B](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A352` → [IopCreateFile + 0xC22](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A3A8` → [IopCreateFile + 0xC22](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A3BF` → [IopCreateFile + 0x67C](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A3CB` → [IopCreateFile + 0x67C](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A3E2` → [IopCreateFile + 0x67C](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)
  - `0x00B1A3FE` → [IopCreateFile + 0x5DF](../8A/IopCreateFile_function_008AB298.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B19FF6  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00B19FFF  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
00B1A006  01 71 1C                        add dword ptr [rcx + 0x1c], esi
00B1A009  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B1A00D  66 39 01                        cmp word ptr [rcx], ax
00B1A010  72 3D                           jb 0x140b1a04f
00B1A012  01 71 20                        add dword ptr [rcx + 0x20], esi
00B1A015  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
00B1A01C  01 71 1C                        add dword ptr [rcx + 0x1c], esi
00B1A01F  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B1A023  66 39 01                        cmp word ptr [rcx], ax
00B1A026  72 27                           jb 0x140b1a04f
00B1A028  01 71 20                        add dword ptr [rcx + 0x20], esi
00B1A02B  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
00B1A02F  48 8D 05 1A 88 06 00            lea rax, [rip + 0x6881a]
00B1A036  48 8B CB                        mov rcx, rbx
00B1A039  48 3B D0                        cmp rdx, rax
00B1A03C  75 07                           jne 0x140b1a045
00B1A03E  E8 0D 88 06 00                  call 0x140b82850
00B1A043  EB 12                           jmp 0x140b1a057
00B1A045  48 8B C2                        mov rax, rdx
00B1A048  E8 83 0A BA FF                  call 0x1406baad0
00B1A04D  EB 08                           jmp 0x140b1a057
00B1A04F  48 8B D3                        mov rdx, rbx
00B1A052  E8 59 05 BA FF                  call 0x1406ba5b0
00B1A057  B8 22 00 00 C0                  mov eax, 0xc0000022
00B1A05C  E9 16 18 D9 FF                  jmp 0x1408ab877
00B1A061  39 B4 24 28 01 00 00            cmp dword ptr [rsp + 0x128], esi
00B1A068  0F 85 A7 00 00 00               jne 0x140b1a115
00B1A06E  48 39 BC 24 30 01 00 00         cmp qword ptr [rsp + 0x130], rdi
00B1A076  74 3F                           je 0x140b1a0b7
00B1A078  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
00B1A080  F7 01 FC FF FF FF               test dword ptr [rcx], 0xfffffffc
00B1A086  75 2F                           jne 0x140b1a0b7
00B1A088  39 71 04                        cmp dword ptr [rcx + 4], esi
00B1A08B  77 2A                           ja 0x140b1a0b7
00B1A08D  39 71 08                        cmp dword ptr [rcx + 8], esi
00B1A090  77 25                           ja 0x140b1a0b7
00B1A092  F6 84 24 00 01 00 00 04         test byte ptr [rsp + 0x100], 4
00B1A09A  75 1B                           jne 0x140b1a0b7
00B1A09C  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
00B1A0A3  FF C8                           dec eax
00B1A0A5  83 F8 02                        cmp eax, 2
00B1A0A8  77 0D                           ja 0x140b1a0b7
00B1A0AA  41 F7 C5 CD FF FF FF            test r13d, 0xffffffcd
00B1A0B1  0F 84 FC 12 D9 FF               je 0x1408ab3b3
00B1A0B7  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00B1A0C0  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
00B1A0C7  01 71 1C                        add dword ptr [rcx + 0x1c], esi
00B1A0CA  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B1A0CE  66 39 01                        cmp word ptr [rcx], ax
00B1A0D1  0F 82 1A 03 00 00               jb 0x140b1a3f1
00B1A0D7  01 71 20                        add dword ptr [rcx + 0x20], esi
00B1A0DA  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
00B1A0E1  01 71 1C                        add dword ptr [rcx + 0x1c], esi
00B1A0E4  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B1A0E8  66 39 01                        cmp word ptr [rcx], ax
00B1A0EB  0F 82 00 03 00 00               jb 0x140b1a3f1
00B1A0F1  01 71 20                        add dword ptr [rcx + 0x20], esi
00B1A0F4  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
00B1A0F8  48 8D 05 51 87 06 00            lea rax, [rip + 0x68751]
00B1A0FF  48 8B CB                        mov rcx, rbx
00B1A102  48 3B D0                        cmp rdx, rax
00B1A105  0F 85 DC 02 00 00               jne 0x140b1a3e7
00B1A10B  E8 40 87 06 00                  call 0x140b82850
00B1A110  E9 E4 02 00 00                  jmp 0x140b1a3f9
00B1A115  83 BC 24 28 01 00 00 02         cmp dword ptr [rsp + 0x128], 2
00B1A11D  0F 85 90 12 D9 FF               jne 0x1408ab3b3
00B1A123  48 39 BC 24 30 01 00 00         cmp qword ptr [rsp + 0x130], rdi
00B1A12B  74 8A                           je 0x140b1a0b7
00B1A12D  F7 84 24 00 01 00 00 FD FF FF FF  test dword ptr [rsp + 0x100], 0xfffffffd
00B1A138  0F 95 C1                        setne cl
00B1A13B  F6 84 24 00 01 00 00 04         test byte ptr [rsp + 0x100], 4
00B1A143  0F 94 C0                        sete al
00B1A146  84 C8                           test al, cl
00B1A148  0F 84 69 FF FF FF               je 0x140b1a0b7
00B1A14E  83 BC 24 08 01 00 00 02         cmp dword ptr [rsp + 0x108], 2
00B1A156  0F 85 5B FF FF FF               jne 0x140b1a0b7
00B1A15C  E9 49 FF FF FF                  jmp 0x140b1a0aa
00B1A161  45 85 F6                        test r14d, r14d
00B1A164  0F 84 89 17 D9 FF               je 0x1408ab8f3
00B1A16A  45 8B E6                        mov r12d, r14d
00B1A16D  41 B8 49 6F 45 61               mov r8d, 0x61456f49
00B1A173  41 8B D6                        mov edx, r14d
00B1A176  B9 42 00 00 00                  mov ecx, 0x42
00B1A17B  E8 70 7F 06 00                  call 0x140b820f0
00B1A180  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
00B1A184  48 85 C0                        test rax, rax
00B1A187  75 6F                           jne 0x140b1a1f8
00B1A189  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00B1A192  48 8B 8A 80 08 00 00            mov rcx, qword ptr [rdx + 0x880]
00B1A199  01 71 1C                        add dword ptr [rcx + 0x1c], esi
00B1A19C  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B1A1A0  66 39 01                        cmp word ptr [rcx], ax
00B1A1A3  72 45                           jb 0x140b1a1ea
00B1A1A5  01 71 20                        add dword ptr [rcx + 0x20], esi
00B1A1A8  48 8B 8A 88 08 00 00            mov rcx, qword ptr [rdx + 0x888]
00B1A1AF  01 71 1C                        add dword ptr [rcx + 0x1c], esi
00B1A1B2  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B1A1B6  66 39 01                        cmp word ptr [rcx], ax
00B1A1B9  72 2F                           jb 0x140b1a1ea
00B1A1BB  01 71 20                        add dword ptr [rcx + 0x20], esi
00B1A1BE  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
00B1A1C2  48 8D 05 87 86 06 00            lea rax, [rip + 0x68687]
00B1A1C9  48 8B CB                        mov rcx, rbx
00B1A1CC  48 3B D0                        cmp rdx, rax
00B1A1CF  75 0B                           jne 0x140b1a1dc
00B1A1D1  E8 7A 86 06 00                  call 0x140b82850
00B1A1D6  90                              nop
00B1A1D7  E9 49 1E D9 FF                  jmp 0x1408ac025
00B1A1DC  48 8B C2                        mov rax, rdx
00B1A1DF  E8 EC 08 BA FF                  call 0x1406baad0
00B1A1E4  90                              nop
00B1A1E5  E9 3B 1E D9 FF                  jmp 0x1408ac025
00B1A1EA  48 8B D3                        mov rdx, rbx
00B1A1ED  E8 BE 03 BA FF                  call 0x1406ba5b0
00B1A1F2  90                              nop
00B1A1F3  E9 2D 1E D9 FF                  jmp 0x1408ac025
00B1A1F8  44 89 73 50                     mov dword ptr [rbx + 0x50], r14d
00B1A1FC  4D 8B C4                        mov r8, r12
00B1A1FF  49 8B D7                        mov rdx, r15
00B1A202  48 8B C8                        mov rcx, rax
00B1A205  E8 36 C6 BA FF                  call 0x1406c6840
00B1A20A  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
00B1A212  4D 8D 44 24 08                  lea r8, [r12 + 8]
00B1A217  41 8B D6                        mov edx, r14d
00B1A21A  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
00B1A21E  E8 CD 17 F1 FF                  call 0x140a2b9f0
00B1A223  44 8B F0                        mov r14d, eax
00B1A226  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B1A22A  85 C0                           test eax, eax
00B1A22C  79 14                           jns 0x140b1a242
00B1A22E  33 D2                           xor edx, edx
00B1A230  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
00B1A234  E8 37 86 06 00                  call 0x140b82870
00B1A239  45 89 34 24                     mov dword ptr [r12], r14d
00B1A23D  E9 09 16 D9 FF                  jmp 0x1408ab84b
00B1A242  8B 94 24 38 01 00 00            mov edx, dword ptr [rsp + 0x138]
00B1A249  E9 A5 12 D9 FF                  jmp 0x1408ab4f3
00B1A24E  48 C7 00 45 63 70 48            mov qword ptr [rax], 0x48706345
00B1A255  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
00B1A259  48 89 78 08                     mov qword ptr [rax + 8], rdi
00B1A25D  0F 10 05 0C 9C 4F FF            movups xmm0, xmmword ptr [rip - 0xb063f4]
00B1A264  F3 0F 7F 40 18                  movdqu xmmword ptr [rax + 0x18], xmm0
00B1A269  48 89 78 28                     mov qword ptr [rax + 0x28], rdi
00B1A26D  C7 40 30 02 00 00 00            mov dword ptr [rax + 0x30], 2
00B1A274  44 89 78 34                     mov dword ptr [rax + 0x34], r15d
00B1A278  48 89 78 38                     mov qword ptr [rax + 0x38], rdi
00B1A27C  48 89 78 40                     mov qword ptr [rax + 0x40], rdi
00B1A280  4C 8D 70 48                     lea r14, [rax + 0x48]
00B1A284  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00B1A289  0F 10 00                        movups xmm0, xmmword ptr [rax]
00B1A28C  F3 41 0F 7F 06                  movdqu xmmword ptr [r14], xmm0
00B1A291  0F 10 40 10                     movups xmm0, xmmword ptr [rax + 0x10]
00B1A295  F3 41 0F 7F 46 10               movdqu xmmword ptr [r14 + 0x10], xmm0
00B1A29B  41 39 3E                        cmp dword ptr [r14], edi
00B1A29E  75 41                           jne 0x140b1a2e1
00B1A2A0  66 41 39 7E 04                  cmp word ptr [r14 + 4], di
00B1A2A5  75 3A                           jne 0x140b1a2e1
00B1A2A7  66 41 39 7E 06                  cmp word ptr [r14 + 6], di
00B1A2AC  75 33                           jne 0x140b1a2e1
00B1A2AE  41 38 7E 08                     cmp byte ptr [r14 + 8], dil
00B1A2B2  75 2D                           jne 0x140b1a2e1
00B1A2B4  41 38 7E 09                     cmp byte ptr [r14 + 9], dil
00B1A2B8  75 27                           jne 0x140b1a2e1
00B1A2BA  41 38 7E 0A                     cmp byte ptr [r14 + 0xa], dil
00B1A2BE  75 21                           jne 0x140b1a2e1
00B1A2C0  41 38 7E 0B                     cmp byte ptr [r14 + 0xb], dil
00B1A2C4  75 1B                           jne 0x140b1a2e1
00B1A2C6  41 38 7E 0C                     cmp byte ptr [r14 + 0xc], dil
00B1A2CA  75 15                           jne 0x140b1a2e1
00B1A2CC  41 38 7E 0D                     cmp byte ptr [r14 + 0xd], dil
00B1A2D0  75 0F                           jne 0x140b1a2e1
00B1A2D2  41 38 7E 0E                     cmp byte ptr [r14 + 0xe], dil
00B1A2D6  75 09                           jne 0x140b1a2e1
00B1A2D8  41 38 7E 0F                     cmp byte ptr [r14 + 0xf], dil
00B1A2DC  40 8A C7                        mov al, dil
00B1A2DF  74 03                           je 0x140b1a2e4
00B1A2E1  40 8A C6                        mov al, sil
00B1A2E4  41 88 46 20                     mov byte ptr [r14 + 0x20], al
00B1A2E8  41 39 7E 10                     cmp dword ptr [r14 + 0x10], edi
00B1A2EC  75 41                           jne 0x140b1a32f
00B1A2EE  66 41 39 7E 14                  cmp word ptr [r14 + 0x14], di
00B1A2F3  75 3A                           jne 0x140b1a32f
00B1A2F5  66 41 39 7E 16                  cmp word ptr [r14 + 0x16], di
00B1A2FA  75 33                           jne 0x140b1a32f
00B1A2FC  41 38 7E 18                     cmp byte ptr [r14 + 0x18], dil
00B1A300  75 2D                           jne 0x140b1a32f
00B1A302  41 38 7E 19                     cmp byte ptr [r14 + 0x19], dil
00B1A306  75 27                           jne 0x140b1a32f
00B1A308  41 38 7E 1A                     cmp byte ptr [r14 + 0x1a], dil
00B1A30C  75 21                           jne 0x140b1a32f
00B1A30E  41 38 7E 1B                     cmp byte ptr [r14 + 0x1b], dil
00B1A312  75 1B                           jne 0x140b1a32f
00B1A314  41 38 7E 1C                     cmp byte ptr [r14 + 0x1c], dil
00B1A318  75 15                           jne 0x140b1a32f
00B1A31A  41 38 7E 1D                     cmp byte ptr [r14 + 0x1d], dil
00B1A31E  75 0F                           jne 0x140b1a32f
00B1A320  41 38 7E 1E                     cmp byte ptr [r14 + 0x1e], dil
00B1A324  75 09                           jne 0x140b1a32f
00B1A326  41 38 7E 1F                     cmp byte ptr [r14 + 0x1f], dil
00B1A32A  40 8A C7                        mov al, dil
00B1A32D  74 03                           je 0x140b1a332
00B1A32F  40 8A C6                        mov al, sil
00B1A332  41 88 46 21                     mov byte ptr [r14 + 0x21], al
00B1A336  48 39 7C 24 68                  cmp qword ptr [rsp + 0x68], rdi
00B1A33B  75 30                           jne 0x140b1a36d
00B1A33D  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00B1A342  33 C9                           xor ecx, ecx
00B1A344  E8 B7 BE EB FF                  call 0x1409d6200
00B1A349  44 8B F8                        mov r15d, eax
00B1A34C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B1A350  85 C0                           test eax, eax
00B1A352  0F 88 62 1B D9 FF               js 0x1408abeba
00B1A358  44 8B EE                        mov r13d, esi
00B1A35B  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
00B1A35F  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00B1A364  48 89 83 A8 00 00 00            mov qword ptr [rbx + 0xa8], rax
00B1A36B  EB 05                           jmp 0x140b1a372
00B1A36D  44 8B 6C 24 5C                  mov r13d, dword ptr [rsp + 0x5c]
00B1A372  49 8B D6                        mov rdx, r14
00B1A375  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00B1A37A  E8 B1 7B D8 FF                  call 0x1408a1f30
00B1A37F  44 8B F8                        mov r15d, eax
00B1A382  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B1A386  85 C0                           test eax, eax
00B1A388  78 19                           js 0x140b1a3a3
00B1A38A  4C 8B F7                        mov r14, rdi
00B1A38D  45 85 ED                        test r13d, r13d
00B1A390  74 11                           je 0x140b1a3a3
00B1A392  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00B1A397  E8 84 1D D9 FF                  call 0x1408ac120
00B1A39C  44 8B F8                        mov r15d, eax
00B1A39F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B1A3A3  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
00B1A3A8  E9 0D 1B D9 FF                  jmp 0x1408abeba
00B1A3AD  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00B1A3B1  48 89 78 08                     mov qword ptr [rax + 8], rdi
00B1A3B5  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00B1A3B9  E8 92 EF 7D FF                  call 0x1402f9350
00B1A3BE  90                              nop
00B1A3BF  E9 50 15 D9 FF                  jmp 0x1408ab914
00B1A3C4  F7 41 50 00 00 04 00            test dword ptr [rcx + 0x50], 0x40000
00B1A3CB  0F 85 43 15 D9 FF               jne 0x1408ab914
00B1A3D1  4C 8B CE                        mov r9, rsi
00B1A3D4  4C 8B C6                        mov r8, rsi
00B1A3D7  48 8B D1                        mov rdx, rcx
00B1A3DA  33 C9                           xor ecx, ecx
00B1A3DC  E8 DF 9C D4 FF                  call 0x1408640c0
00B1A3E1  90                              nop
00B1A3E2  E9 2D 15 D9 FF                  jmp 0x1408ab914
00B1A3E7  48 8B C2                        mov rax, rdx
00B1A3EA  E8 E1 06 BA FF                  call 0x1406baad0
00B1A3EF  EB 08                           jmp 0x140b1a3f9
00B1A3F1  48 8B D3                        mov rdx, rbx
00B1A3F4  E8 B7 01 BA FF                  call 0x1406ba5b0
00B1A3F9  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B1A3FE  E9 74 14 D9 FF                  jmp 0x1408ab877
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B19FF6(void)
{
    __int64 result;
    unsigned __int8 v_stack_p100;
    unsigned int v_stack_p108;
    unsigned int v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned int v_stack_p138;
    unsigned int v_stack_p40;
    unsigned int v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_pE8;

    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2176) + 16)))) goto loc_00B1A04F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 16)))) goto loc_00B1A04F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56)) != (v_rip + 428058)) goto loc_00B1A045;
    result = ExFreePool(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), a3, a4);
    goto loc_00B1A057;
loc_00B1A045:
    result = guard_dispatch_icall(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2184) + 56), a3, a4);
    goto loc_00B1A057;
loc_00B1A04F:
    result = ExpInterlockedPushEntrySList(v_rbx, v_rbx, a3, a4);
loc_00B1A057:
}
```

## 5. (Beta) C Style

```c
void sub_00B19FF6(void)
{
    int64_t result;
    uint8_t v_stack_p100;
    uint32_t v_stack_p108;
    uint32_t v_stack_p128;
    uint64_t v_stack_p130;
    uint32_t v_stack_p138;
    uint32_t v_stack_p40;
    uint32_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_pE8;

    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x880) + 0x10)))) goto loc_00B1A04F;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x10)))) goto loc_00B1A04F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38)) != (v_rip + 428058)) goto loc_00B1A045;
    result = ExFreePool(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), a3, a4);
    goto loc_00B1A057;
loc_00B1A045:
    result = guard_dispatch_icall(local_rbx, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x888) + 0x38), a3, a4);
    goto loc_00B1A057;
loc_00B1A04F:
    result = ExpInterlockedPushEntrySList(local_rbx, local_rbx, a3, a4);
loc_00B1A057:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B19FF6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
