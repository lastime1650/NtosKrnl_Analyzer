# MiProtectPrivateMemory

- RVA: `0x002C45B0`–`0x002C5151` (길이 `2,977` bytes)
- VA: `0x00000001402C45B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EA64`
- 디코드: `670`개 명령, `2,977/2,977` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002C46AB` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C46DE` → [MiComputePageCommitment](MiComputePageCommitment_function_002C5C34.md) (function, `0x002C5C34`)
- `0x002C475B` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x002C478C` → [MiGetPageProtection](../32/MiGetPageProtection_function_0032BA10.md) (function, `0x0032BA10`)
- `0x002C480A` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x002C499D` → [MiRevertValidPte](MiRevertValidPte_function_002C5160.md) (function, `0x002C5160`)
- `0x002C49ED` → [MiSetProtectionOnTransitionPte](MiSetProtectionOnTransitionPte_function_002C586C.md) (function, `0x002C586C`)
- `0x002C4ACA` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C4ACF` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C4AED` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002C4AFD` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C4B52` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C4B57` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C4B84` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x002C4B9D` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002C4C03` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C4C0B` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C4C3E` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x002C4C81` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x002C4C8E` → [MiRotatedToFrameBuffer](MiRotatedToFrameBuffer_function_002C5FE4.md) (function, `0x002C5FE4`)
- `0x002C4CDA` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C4CDF` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C4D0A` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x002C4D27` → [MiMakeProtoPrivate](MiMakeProtoPrivate_function_002C64A4.md) (function, `0x002C64A4`)
- `0x002C4D47` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002C4D57` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C4D64` → [MiFaultInPagedPool](../4B/MiFaultInPagedPool_function_004B3BC0.md) (function, `0x004B3BC0`)
- `0x002C4D6C` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C4DAD` → [MiMakeVaRangeNoAccess](../4A/MiMakeVaRangeNoAccess_function_004A3CE0.md) (function, `0x004A3CE0`)
- `0x002C4E1E` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x002C4E31` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C4E66` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x002C4EE8` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002C4EED` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x002C4F1A` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x002C4F3B` → [MiMakeProtoLeafValid](../2A/MiMakeProtoLeafValid_function_002A6710.md) (function, `0x002A6710`)
- `0x002C4F68` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C4F8E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002C4F9D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002C4FC0` → [MI_GET_GRAPHICS_PROTECTION_FROM_VAD](../43/MI_GET_GRAPHICS_PROTECTION_FROM_VAD_function_00438CA0.md) (function, `0x00438CA0`)
- `0x002C5001` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x002C509D` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002C50AD` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (function, `0x00887630`)
- `0x002C50BD` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002C5120` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002C5135` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x002C5147` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)

### Direct callers
- [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) at `0x00881488`

### Static image references
- `0x002C467B` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002C4A22` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002C4BC2` → RVA `0x00E38840` (`.data`; read)
- `0x002C4F80` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002C50AD` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (`.text` → `PAGE`)
  - `0x002C5147` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C45B0  48 8B C4                        mov rax, rsp
002C45B3  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
002C45B7  48 89 48 08                     mov qword ptr [rax + 8], rcx
002C45BB  55                              push rbp
002C45BC  56                              push rsi
002C45BD  57                              push rdi
002C45BE  41 54                           push r12
002C45C0  41 55                           push r13
002C45C2  41 56                           push r14
002C45C4  41 57                           push r15
002C45C6  48 81 EC B0 00 00 00            sub rsp, 0xb0
002C45CD  4C 8B E2                        mov r12, rdx
002C45D0  45 8B F1                        mov r14d, r9d
002C45D3  45 33 C9                        xor r9d, r9d
002C45D6  49 C1 EC 09                     shr r12, 9
002C45DA  4C 89 48 A0                     mov qword ptr [rax - 0x60], r9
002C45DE  49 8B D8                        mov rbx, r8
002C45E1  66 44 89 48 18                  mov word ptr [rax + 0x18], r9w
002C45E6  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
002C45F0  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
002C45F5  48 8B FA                        mov rdi, rdx
002C45F8  4C 89 48 90                     mov qword ptr [rax - 0x70], r9
002C45FC  45 8B F9                        mov r15d, r9d
002C45FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002C4608  4D 23 E0                        and r12, r8
002C460B  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
002C4610  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
002C461A  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
002C4621  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
002C4629  4C 8D A8 00 04 00 00            lea r13, [rax + 0x400]
002C4630  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
002C4635  48 8B C2                        mov rax, rdx
002C4638  48 8B EB                        mov rbp, rbx
002C463B  4C 03 E0                        add r12, rax
002C463E  48 C1 ED 09                     shr rbp, 9
002C4642  49 23 E8                        and rbp, r8
002C4645  48 8B C2                        mov rax, rdx
002C4648  48 03 E8                        add rbp, rax
002C464B  44 89 4C 24 64                  mov dword ptr [rsp + 0x64], r9d
002C4650  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
002C4653  41 8D 71 03                     lea esi, [r9 + 3]
002C4657  8B D0                           mov edx, eax
002C4659  48 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbp
002C4661  25 00 00 A0 00                  and eax, 0xa00000
002C4666  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
002C466B  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
002C4670  41 BA 01 00 00 00               mov r10d, 1
002C4676  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
002C467B  4C 8D 05 7E B9 D3 FF            lea r8, [rip - 0x2c4682]
002C4682  3D 00 00 A0 00                  cmp eax, 0xa00000
002C4687  0F 84 C0 09 00 00               je 0x1402c504d
002C468D  4C 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], r10
002C4695  C1 EA 0C                        shr edx, 0xc
002C4698  49 8B CD                        mov rcx, r13
002C469B  83 E2 7F                        and edx, 0x7f
002C469E  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
002C46A3  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
002C46AB  E8 40 85 FB FF                  call 0x14027cbf0
002C46B0  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
002C46B8  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
002C46BD  33 D2                           xor edx, edx
002C46BF  88 84 24 18 01 00 00            mov byte ptr [rsp + 0x118], al
002C46C6  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
002C46CB  44 0F B6 C8                     movzx r9d, al
002C46CF  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002C46D4  48 8B CF                        mov rcx, rdi
002C46D7  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
002C46DB  48 8B D3                        mov rdx, rbx
002C46DE  E8 51 15 00 00                  call 0x1402c5c34
002C46E3  48 8B D5                        mov rdx, rbp
002C46E6  49 2B D4                        sub rdx, r12
002C46E9  48 C1 FA 03                     sar rdx, 3
002C46ED  48 FF C2                        inc rdx
002C46F0  48 3B C2                        cmp rax, rdx
002C46F3  0F B6 94 24 18 01 00 00         movzx edx, byte ptr [rsp + 0x118]
002C46FB  0F 85 2D 07 00 00               jne 0x1402c4e2e
002C4701  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
002C4706  49 8B FD                        mov rdi, r13
002C4709  48 85 DB                        test rbx, rbx
002C470C  0F 85 88 09 00 00               jne 0x1402c509a
002C4712  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
002C471C  49 8B DC                        mov rbx, r12
002C471F  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
002C4729  83 FE 01                        cmp esi, 1
002C472C  0F 86 E5 08 00 00               jbe 0x1402c5017
002C4732  4C 8B EB                        mov r13, rbx
002C4735  49 C1 ED 09                     shr r13, 9
002C4739  4D 23 E9                        and r13, r9
002C473C  49 8B C0                        mov rax, r8
002C473F  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
002C4747  4C 03 E8                        add r13, rax
002C474A  44 0F B6 C2                     movzx r8d, dl
002C474E  45 33 C9                        xor r9d, r9d
002C4751  8B 94 24 90 00 00 00            mov edx, dword ptr [rsp + 0x90]
002C4758  48 8B CB                        mov rcx, rbx
002C475B  E8 10 B8 FB FF                  call 0x14027ff70
002C4760  48 8B 03                        mov rax, qword ptr [rbx]
002C4763  48 8B CE                        mov rcx, rsi
002C4766  48 85 C0                        test rax, rax
002C4769  0F 84 38 08 00 00               je 0x1402c4fa7
002C476F  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
002C4777  48 8B D3                        mov rdx, rbx
002C477A  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
002C477F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002C4784  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
002C478C  E8 7F 72 06 00                  call 0x14032ba10
002C4791  4C 39 BC 24 88 00 00 00         cmp qword ptr [rsp + 0x88], r15
002C4799  0F 85 A2 05 00 00               jne 0x1402c4d41
002C479F  8B C0                           mov eax, eax
002C47A1  4C 8D 05 58 B8 D3 FF            lea r8, [rip - 0x2c47a8]
002C47A8  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
002C47B0  45 8B 84 80 30 46 01 00         mov r8d, dword ptr [r8 + rax*4 + 0x14630]
002C47B8  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
002C47BC  44 0B C0                        or r8d, eax
002C47BF  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
002C47C7  44 89 00                        mov dword ptr [rax], r8d
002C47CA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002C47D0  48 3B DD                        cmp rbx, rbp
002C47D3  0F 87 E4 02 00 00               ja 0x1402c4abd
002C47D9  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
002C47E0  0F 84 52 03 00 00               je 0x1402c4b38
002C47E6  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
002C47EB  0F 85 47 03 00 00               jne 0x1402c4b38
002C47F1  48 8B 3B                        mov rdi, qword ptr [rbx]
002C47F4  40 F6 C7 01                     test dil, 1
002C47F8  0F 84 CE 01 00 00               je 0x1402c49cc
002C47FE  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
002C4804  0F 85 8D 00 00 00               jne 0x1402c4897
002C480A  E8 81 E4 F7 FF                  call 0x140242c90
002C480F  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002C4814  45 33 C0                        xor r8d, r8d
002C4817  4C 8B F8                        mov r15, rax
002C481A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002C481F  44 89 40 10                     mov dword ptr [rax + 0x10], r8d
002C4823  C7 40 14 20 00 00 00            mov dword ptr [rax + 0x14], 0x20
002C482A  48 89 10                        mov qword ptr [rax], rdx
002C482D  8B 8A B8 00 00 00               mov ecx, dword ptr [rdx + 0xb8]
002C4833  C1 E9 08                        shr ecx, 8
002C4836  F6 C1 08                        test cl, 8
002C4839  0F 95 C0                        setne al
002C483C  41 88 47 18                     mov byte ptr [r15 + 0x18], al
002C4840  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
002C4846  A8 0F                           test al, 0xf
002C4848  75 20                           jne 0x1402c486a
002C484A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002C4853  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002C485A  48 81 C1 00 04 00 00            add rcx, 0x400
002C4861  48 3B D1                        cmp rdx, rcx
002C4864  0F 85 87 07 00 00               jne 0x1402c4ff1
002C486A  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
002C4870  41 8B C8                        mov ecx, r8d
002C4873  A8 0F                           test al, 0xf
002C4875  B8 01 00 00 00                  mov eax, 1
002C487A  0F 44 C8                        cmove ecx, eax
002C487D  41 83 67 10 DB                  and dword ptr [r15 + 0x10], 0xffffffdb
002C4882  41 89 4F 08                     mov dword ptr [r15 + 8], ecx
002C4886  66 45 89 47 19                  mov word ptr [r15 + 0x19], r8w
002C488B  45 89 47 1C                     mov dword ptr [r15 + 0x1c], r8d
002C488F  4D 89 47 20                     mov qword ptr [r15 + 0x20], r8
002C4893  4D 89 47 28                     mov qword ptr [r15 + 0x28], r8
002C4897  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002C48A1  48 C1 EF 0C                     shr rdi, 0xc
002C48A5  48 23 F8                        and rdi, rax
002C48A8  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002C48B2  48 8D 34 7F                     lea rsi, [rdi + rdi*2]
002C48B6  48 C1 E6 04                     shl rsi, 4
002C48BA  48 8B C0                        mov rax, rax
002C48BD  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
002C48C5  48 03 F0                        add rsi, rax
002C48C8  41 8B 40 30                     mov eax, dword ptr [r8 + 0x30]
002C48CC  24 70                           and al, 0x70
002C48CE  3C 40                           cmp al, 0x40
002C48D0  0F 84 B5 03 00 00               je 0x1402c4c8b
002C48D6  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002C48DA  48 85 C0                        test rax, rax
002C48DD  0F 88 F2 03 00 00               js 0x1402c4cd5
002C48E3  F7 84 24 10 01 00 00 01 01 00 00  test dword ptr [rsp + 0x110], 0x101
002C48EE  0F 85 98 04 00 00               jne 0x1402c4d8c
002C48F4  33 ED                           xor ebp, ebp
002C48F6  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
002C48FD  0F 82 1D 01 00 00               jb 0x1402c4a20
002C4903  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
002C4907  48 8B C1                        mov rax, rcx
002C490A  48 C1 E8 05                     shr rax, 5
002C490E  83 E0 1F                        and eax, 0x1f
002C4911  41 83 FE 18                     cmp r14d, 0x18
002C4915  0F 84 8C 03 00 00               je 0x1402c4ca7
002C491B  83 F8 18                        cmp eax, 0x18
002C491E  0F 84 EE 02 00 00               je 0x1402c4c12
002C4924  83 E0 18                        and eax, 0x18
002C4927  0F 85 13 05 00 00               jne 0x1402c4e40
002C492D  41 8B C6                        mov eax, r14d
002C4930  83 E0 18                        and eax, 0x18
002C4933  83 F8 18                        cmp eax, 0x18
002C4936  0F 84 A2 07 00 00               je 0x1402c50de
002C493C  83 F8 08                        cmp eax, 8
002C493F  75 04                           jne 0x1402c4945
002C4941  41 83 E6 F7                     and r14d, 0xfffffff7
002C4945  48 85 C9                        test rcx, rcx
002C4948  0F 84 B0 06 00 00               je 0x1402c4ffe
002C494E  41 8B D6                        mov edx, r14d
002C4951  48 C1 E2 05                     shl rdx, 5
002C4955  48 8B C2                        mov rax, rdx
002C4958  48 33 C1                        xor rax, rcx
002C495B  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
002C4961  48 33 C2                        xor rax, rdx
002C4964  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
002C4968  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002C4972  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
002C4977  48 8B AC 24 98 00 00 00         mov rbp, qword ptr [rsp + 0x98]
002C497F  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002C4984  4C 8B CF                        mov r9, rdi
002C4987  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
002C498F  45 8B C6                        mov r8d, r14d
002C4992  48 8B CE                        mov rcx, rsi
002C4995  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002C499A  48 8B D3                        mov rdx, rbx
002C499D  E8 BE 07 00 00                  call 0x1402c5160
002C49A2  83 7C 24 64 00                  cmp dword ptr [rsp + 0x64], 0
002C49A7  0F 85 C7 04 00 00               jne 0x1402c4e74
002C49AD  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
002C49B5  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C49BA  4D 8D 24 C4                     lea r12, [r12 + rax*8]
002C49BE  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002C49C3  48 8D 1C C3                     lea rbx, [rbx + rax*8]
002C49C7  E9 04 FE FF FF                  jmp 0x1402c47d0
002C49CC  48 0F BA E7 0A                  bt rdi, 0xa
002C49D1  0F 82 04 05 00 00               jb 0x1402c4edb
002C49D7  48 0F BA E7 0B                  bt rdi, 0xb
002C49DC  73 61                           jae 0x1402c4a3f
002C49DE  41 B9 01 00 00 00               mov r9d, 1
002C49E4  45 8B C6                        mov r8d, r14d
002C49E7  48 8B D3                        mov rdx, rbx
002C49EA  48 8B CE                        mov rcx, rsi
002C49ED  E8 7A 0E 00 00                  call 0x1402c586c
002C49F2  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
002C49FA  48 83 F9 01                     cmp rcx, 1
002C49FE  0F 85 97 04 00 00               jne 0x1402c4e9b
002C4A04  85 C0                           test eax, eax
002C4A06  0F 85 22 01 00 00               jne 0x1402c4b2e
002C4A0C  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C4A11  49 83 C4 08                     add r12, 8
002C4A15  48 83 C3 08                     add rbx, 8
002C4A19  E9 B2 FD FF FF                  jmp 0x1402c47d0
002C4A1E  66 90                           nop
002C4A20  FF C5                           inc ebp
002C4A22  85 2D 84 08 D0 00               test dword ptr [rip + 0xd00884], ebp
002C4A28  0F 84 52 05 00 00               je 0x1402c4f80
002C4A2E  F3 90                           pause
002C4A30  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002C4A34  48 85 C0                        test rax, rax
002C4A37  0F 89 B9 FE FF FF               jns 0x1402c48f6
002C4A3D  EB E1                           jmp 0x1402c4a20
002C4A3F  48 83 BC 24 80 00 00 00 01      cmp qword ptr [rsp + 0x80], 1
002C4A48  0F 85 B9 06 00 00               jne 0x1402c5107
002C4A4E  48 85 FF                        test rdi, rdi
002C4A51  0F 84 9C 03 00 00               je 0x1402c4df3
002C4A57  48 8B C7                        mov rax, rdi
002C4A5A  48 C1 E8 05                     shr rax, 5
002C4A5E  83 E0 1F                        and eax, 0x1f
002C4A61  41 83 FE 18                     cmp r14d, 0x18
002C4A65  0F 84 62 03 00 00               je 0x1402c4dcd
002C4A6B  83 F8 18                        cmp eax, 0x18
002C4A6E  0F 84 3E 02 00 00               je 0x1402c4cb2
002C4A74  83 E0 18                        and eax, 0x18
002C4A77  0F 85 51 05 00 00               jne 0x1402c4fce
002C4A7D  41 8B C6                        mov eax, r14d
002C4A80  83 E0 18                        and eax, 0x18
002C4A83  83 F8 18                        cmp eax, 0x18
002C4A86  0F 84 72 06 00 00               je 0x1402c50fe
002C4A8C  83 F8 08                        cmp eax, 8
002C4A8F  75 04                           jne 0x1402c4a95
002C4A91  41 83 E6 F7                     and r14d, 0xfffffff7
002C4A95  48 85 FF                        test rdi, rdi
002C4A98  0F 84 C5 03 00 00               je 0x1402c4e63
002C4A9E  41 8B CE                        mov ecx, r14d
002C4AA1  48 C1 E1 05                     shl rcx, 5
002C4AA5  48 8B C1                        mov rax, rcx
002C4AA8  48 33 C7                        xor rax, rdi
002C4AAB  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
002C4AB1  48 33 C1                        xor rax, rcx
002C4AB4  49 89 04 24                     mov qword ptr [r12], rax
002C4AB8  E9 4F FF FF FF                  jmp 0x1402c4a0c
002C4ABD  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002C4AC2  48 85 C0                        test rax, rax
002C4AC5  74 0D                           je 0x1402c4ad4
002C4AC7  48 8B C8                        mov rcx, rax
002C4ACA  E8 F1 D4 04 00                  call 0x140311fc0
002C4ACF  E8 9C F1 04 00                  call 0x140313c70
002C4AD4  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002C4AD9  48 85 C9                        test rcx, rcx
002C4ADC  0F 85 44 06 00 00               jne 0x1402c5126
002C4AE2  4D 85 ED                        test r13, r13
002C4AE5  74 0B                           je 0x1402c4af2
002C4AE7  49 8B D5                        mov rdx, r13
002C4AEA  48 8B CF                        mov rcx, rdi
002C4AED  E8 CE 23 F5 FF                  call 0x140216ec0
002C4AF2  0F B6 94 24 18 01 00 00         movzx edx, byte ptr [rsp + 0x118]
002C4AFA  48 8B CF                        mov rcx, rdi
002C4AFD  E8 8E 8B FB FF                  call 0x14027d690
002C4B02  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
002C4B07  48 85 D2                        test rdx, rdx
002C4B0A  0F 85 2F 06 00 00               jne 0x1402c513f
002C4B10  33 C0                           xor eax, eax
002C4B12  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
002C4B1A  48 81 C4 B0 00 00 00            add rsp, 0xb0
002C4B21  41 5F                           pop r15
002C4B23  41 5E                           pop r14
002C4B25  41 5D                           pop r13
002C4B27  41 5C                           pop r12
002C4B29  5F                              pop rdi
002C4B2A  5E                              pop rsi
002C4B2B  5D                              pop rbp
002C4B2C  C3                              ret
002C4B2D  CC                              int3
002C4B2E  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C4B33  E9 98 FC FF FF                  jmp 0x1402c47d0
002C4B38  C7 44 24 40 00 00 00 00         mov dword ptr [rsp + 0x40], 0
002C4B40  4D 85 ED                        test r13, r13
002C4B43  74 23                           je 0x1402c4b68
002C4B45  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002C4B4A  48 85 C0                        test rax, rax
002C4B4D  74 19                           je 0x1402c4b68
002C4B4F  48 8B C8                        mov rcx, rax
002C4B52  E8 69 D4 04 00                  call 0x140311fc0
002C4B57  E8 14 F1 04 00                  call 0x140313c70
002C4B5C  45 33 FF                        xor r15d, r15d
002C4B5F  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
002C4B68  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002C4B6D  48 85 C0                        test rax, rax
002C4B70  74 20                           je 0x1402c4b92
002C4B72  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002C4B77  48 8B C8                        mov rcx, rax
002C4B7A  48 2B D0                        sub rdx, rax
002C4B7D  48 C1 FA 03                     sar rdx, 3
002C4B81  48 FF C2                        inc rdx
002C4B84  E8 EB C7 21 00                  call 0x1404e1374
002C4B89  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
002C4B92  4D 85 ED                        test r13, r13
002C4B95  74 0B                           je 0x1402c4ba2
002C4B97  49 8B D5                        mov rdx, r13
002C4B9A  48 8B CF                        mov rcx, rdi
002C4B9D  E8 1E 23 F5 FF                  call 0x140216ec0
002C4BA2  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002C4BA8  24 0F                           and al, 0xf
002C4BAA  3C 05                           cmp al, 5
002C4BAC  0F 87 8C 00 00 00               ja 0x1402c4c3e
002C4BB2  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002C4BB8  24 0F                           and al, 0xf
002C4BBA  3C 01                           cmp al, 1
002C4BBC  0F 85 49 04 00 00               jne 0x1402c500b
002C4BC2  48 8D 05 77 3C B7 00            lea rax, [rip + 0xb73c77]
002C4BC9  48 8B 10                        mov rdx, qword ptr [rax]
002C4BCC  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002C4BD5  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002C4BDC  48 85 C9                        test rcx, rcx
002C4BDF  0F 84 BB 00 00 00               je 0x1402c4ca0
002C4BE5  8B 81 44 01 00 00               mov eax, dword ptr [rcx + 0x144]
002C4BEB  48 C1 E0 06                     shl rax, 6
002C4BEF  8B 0C 10                        mov ecx, dword ptr [rax + rdx]
002C4BF2  0F BA E1 1E                     bt ecx, 0x1e
002C4BF6  73 46                           jae 0x1402c4c3e
002C4BF8  0F B6 94 24 18 01 00 00         movzx edx, byte ptr [rsp + 0x118]
002C4C00  48 8B CF                        mov rcx, rdi
002C4C03  E8 88 8A FB FF                  call 0x14027d690
002C4C08  48 8B CF                        mov rcx, rdi
002C4C0B  E8 E0 7F FB FF                  call 0x14027cbf0
002C4C10  EB 35                           jmp 0x1402c4c47
002C4C12  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
002C4C1A  41 8B 50 30                     mov edx, dword ptr [r8 + 0x30]
002C4C1E  0F BA E2 15                     bt edx, 0x15
002C4C22  0F 83 56 01 00 00               jae 0x1402c4d7e
002C4C28  C1 EA 07                        shr edx, 7
002C4C2B  83 E2 1F                        and edx, 0x1f
002C4C2E  8B C2                           mov eax, edx
002C4C30  83 FA 18                        cmp edx, 0x18
002C4C33  0F 84 F4 FC FF FF               je 0x1402c492d
002C4C39  E9 E6 FC FF FF                  jmp 0x1402c4924
002C4C3E  E8 9D 27 FB FF                  call 0x1402773e0
002C4C43  85 C0                           test eax, eax
002C4C45  75 B1                           jne 0x1402c4bf8
002C4C47  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C4C51  4C 8B EB                        mov r13, rbx
002C4C54  49 C1 ED 09                     shr r13, 9
002C4C58  4C 23 E8                        and r13, rax
002C4C5B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002C4C65  48 8B C0                        mov rax, rax
002C4C68  44 0F B6 84 24 18 01 00 00      movzx r8d, byte ptr [rsp + 0x118]
002C4C71  4C 03 E8                        add r13, rax
002C4C74  8B 94 24 90 00 00 00            mov edx, dword ptr [rsp + 0x90]
002C4C7B  45 33 C9                        xor r9d, r9d
002C4C7E  48 8B CB                        mov rcx, rbx
002C4C81  E8 EA B2 FB FF                  call 0x14027ff70
002C4C86  E9 66 FB FF FF                  jmp 0x1402c47f1
002C4C8B  48 8B CB                        mov rcx, rbx
002C4C8E  E8 51 13 00 00                  call 0x1402c5fe4
002C4C93  85 C0                           test eax, eax
002C4C95  0F 85 E4 FC FF FF               jne 0x1402c497f
002C4C9B  E9 36 FC FF FF                  jmp 0x1402c48d6
002C4CA0  33 C0                           xor eax, eax
002C4CA2  E9 44 FF FF FF                  jmp 0x1402c4beb
002C4CA7  41 BE 18 00 00 00               mov r14d, 0x18
002C4CAD  E9 93 FC FF FF                  jmp 0x1402c4945
002C4CB2  8B 4E 30                        mov ecx, dword ptr [rsi + 0x30]
002C4CB5  0F BA E1 15                     bt ecx, 0x15
002C4CB9  0F 83 B3 02 00 00               jae 0x1402c4f72
002C4CBF  C1 E9 07                        shr ecx, 7
002C4CC2  83 E1 1F                        and ecx, 0x1f
002C4CC5  8B C1                           mov eax, ecx
002C4CC7  83 F9 18                        cmp ecx, 0x18
002C4CCA  0F 84 AD FD FF FF               je 0x1402c4a7d
002C4CD0  E9 9F FD FF FF                  jmp 0x1402c4a74
002C4CD5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
002C4CDA  E8 E1 D2 04 00                  call 0x140311fc0
002C4CDF  E8 8C EF 04 00                  call 0x140313c70
002C4CE4  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
002C4CE9  33 FF                           xor edi, edi
002C4CEB  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
002C4CF0  44 8B FF                        mov r15d, edi
002C4CF3  48 85 F6                        test rsi, rsi
002C4CF6  74 1C                           je 0x1402c4d14
002C4CF8  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002C4CFD  48 8B CE                        mov rcx, rsi
002C4D00  48 2B D6                        sub rdx, rsi
002C4D03  48 C1 FA 03                     sar rdx, 3
002C4D07  48 FF C2                        inc rdx
002C4D0A  E8 65 C6 21 00                  call 0x1404e1374
002C4D0F  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
002C4D14  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C4D19  4C 8B C3                        mov r8, rbx
002C4D1C  0F B6 94 24 18 01 00 00         movzx edx, byte ptr [rsp + 0x118]
002C4D24  48 8B CF                        mov rcx, rdi
002C4D27  E8 78 17 00 00                  call 0x1402c64a4
002C4D2C  85 C0                           test eax, eax
002C4D2E  0F 85 A4 00 00 00               jne 0x1402c4dd8
002C4D34  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
002C4D3C  E9 8F FA FF FF                  jmp 0x1402c47d0
002C4D41  49 8B D5                        mov rdx, r13
002C4D44  48 8B CF                        mov rcx, rdi
002C4D47  E8 74 21 F5 FF                  call 0x140216ec0
002C4D4C  0F B6 94 24 18 01 00 00         movzx edx, byte ptr [rsp + 0x118]
002C4D54  48 8B CF                        mov rcx, rdi
002C4D57  E8 34 89 FB FF                  call 0x14027d690
002C4D5C  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
002C4D64  E8 57 EE 1E 00                  call 0x1404b3bc0
002C4D69  48 8B CF                        mov rcx, rdi
002C4D6C  E8 7F 7E FB FF                  call 0x14027cbf0
002C4D71  0F B6 94 24 18 01 00 00         movzx edx, byte ptr [rsp + 0x118]
002C4D79  E9 CC F9 FF FF                  jmp 0x1402c474a
002C4D7E  49 8B 40 48                     mov rax, qword ptr [r8 + 0x48]
002C4D82  8B 50 20                        mov edx, dword ptr [rax + 0x20]
002C4D85  D1 EA                           shr edx, 1
002C4D87  E9 9F FE FF FF                  jmp 0x1402c4c2b
002C4D8C  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
002C4D94  4D 8B CF                        mov r9, r15
002C4D97  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
002C4D9F  4C 8B C5                        mov r8, rbp
002C4DA2  48 8B CE                        mov rcx, rsi
002C4DA5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002C4DAA  48 8B D3                        mov rdx, rbx
002C4DAD  E8 2E EF 1D 00                  call 0x1404a3ce0
002C4DB2  85 C0                           test eax, eax
002C4DB4  0F 85 E8 FB FF FF               jne 0x1402c49a2
002C4DBA  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002C4DBF  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C4DC4  83 48 14 01                     or dword ptr [rax + 0x14], 1
002C4DC8  E9 03 FA FF FF                  jmp 0x1402c47d0
002C4DCD  41 BE 18 00 00 00               mov r14d, 0x18
002C4DD3  E9 BD FC FF FF                  jmp 0x1402c4a95
002C4DD8  83 F8 01                        cmp eax, 1
002C4DDB  0F 85 79 01 00 00               jne 0x1402c4f5a
002C4DE1  48 FF 4C 24 78                  dec qword ptr [rsp + 0x78]
002C4DE6  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
002C4DEE  E9 DD F9 FF FF                  jmp 0x1402c47d0
002C4DF3  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C4DFD  49 8B D4                        mov rdx, r12
002C4E00  48 C1 EA 09                     shr rdx, 9
002C4E04  48 23 D0                        and rdx, rax
002C4E07  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002C4E11  48 8B C0                        mov rax, rax
002C4E14  45 33 C9                        xor r9d, r9d
002C4E17  48 03 D0                        add rdx, rax
002C4E1A  45 8D 41 01                     lea r8d, [r9 + 1]
002C4E1E  E8 0D E8 F7 FF                  call 0x140243630
002C4E23  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
002C4E26  C1 E8 07                        shr eax, 7
002C4E29  E9 30 FC FF FF                  jmp 0x1402c4a5e
002C4E2E  49 8B CD                        mov rcx, r13
002C4E31  E8 5A 88 FB FF                  call 0x14027d690
002C4E36  B8 2D 00 00 C0                  mov eax, 0xc000002d
002C4E3B  E9 D2 FC FF FF                  jmp 0x1402c4b12
002C4E40  83 F8 10                        cmp eax, 0x10
002C4E43  0F 84 F8 FA FF FF               je 0x1402c4941
002C4E49  83 F8 08                        cmp eax, 8
002C4E4C  0F 84 7F 02 00 00               je 0x1402c50d1
002C4E52  83 F8 18                        cmp eax, 0x18
002C4E55  0F 85 EA FA FF FF               jne 0x1402c4945
002C4E5B  44 0B F0                        or r14d, eax
002C4E5E  E9 E2 FA FF FF                  jmp 0x1402c4945
002C4E63  41 8B CE                        mov ecx, r14d
002C4E66  E8 95 2B 07 00                  call 0x140337a00
002C4E6B  49 89 04 24                     mov qword ptr [r12], rax
002C4E6F  E9 98 FB FF FF                  jmp 0x1402c4a0c
002C4E74  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002C4E79  48 85 C0                        test rax, rax
002C4E7C  48 0F 44 C3                     cmove rax, rbx
002C4E80  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002C4E85  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002C4E8A  48 FF C8                        dec rax
002C4E8D  48 8D 04 C3                     lea rax, [rbx + rax*8]
002C4E91  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
002C4E96  E9 12 FB FF FF                  jmp 0x1402c49ad
002C4E9B  83 7C 24 64 00                  cmp dword ptr [rsp + 0x64], 0
002C4EA0  0F 84 41 02 00 00               je 0x1402c50e7
002C4EA6  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002C4EAB  48 85 C0                        test rax, rax
002C4EAE  48 0F 44 C3                     cmove rax, rbx
002C4EB2  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002C4EB7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002C4EBC  48 8D 50 FF                     lea rdx, [rax - 1]
002C4EC0  48 8D 14 D3                     lea rdx, [rbx + rdx*8]
002C4EC4  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
002C4EC9  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C4ECE  4D 8D 24 CC                     lea r12, [r12 + rcx*8]
002C4ED2  48 8D 1C C3                     lea rbx, [rbx + rax*8]
002C4ED6  E9 F5 F8 FF FF                  jmp 0x1402c47d0
002C4EDB  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002C4EE0  48 85 C0                        test rax, rax
002C4EE3  74 19                           je 0x1402c4efe
002C4EE5  48 8B C8                        mov rcx, rax
002C4EE8  E8 D3 D0 04 00                  call 0x140311fc0
002C4EED  E8 7E ED 04 00                  call 0x140313c70
002C4EF2  45 33 FF                        xor r15d, r15d
002C4EF5  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
002C4EFE  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
002C4F03  48 85 FF                        test rdi, rdi
002C4F06  74 20                           je 0x1402c4f28
002C4F08  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002C4F0D  48 8B CF                        mov rcx, rdi
002C4F10  48 2B D7                        sub rdx, rdi
002C4F13  48 C1 FA 03                     sar rdx, 3
002C4F17  48 FF C2                        inc rdx
002C4F1A  E8 55 C4 21 00                  call 0x1404e1374
002C4F1F  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
002C4F28  44 0F B6 84 24 18 01 00 00      movzx r8d, byte ptr [rsp + 0x118]
002C4F31  BF 01 00 00 00                  mov edi, 1
002C4F36  8B D7                           mov edx, edi
002C4F38  48 8B CB                        mov rcx, rbx
002C4F3B  E8 D0 17 FE FF                  call 0x1402a6710
002C4F40  85 C0                           test eax, eax
002C4F42  79 08                           jns 0x1402c4f4c
002C4F44  49 83 C4 08                     add r12, 8
002C4F48  48 83 C3 08                     add rbx, 8
002C4F4C  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
002C4F50  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
002C4F55  E9 76 F8 FF FF                  jmp 0x1402c47d0
002C4F5A  45 33 ED                        xor r13d, r13d
002C4F5D  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
002C4F65  48 8B CF                        mov rcx, rdi
002C4F68  E8 83 7C FB FF                  call 0x14027cbf0
002C4F6D  E9 C2 FD FF FF                  jmp 0x1402c4d34
002C4F72  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
002C4F76  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
002C4F79  D1 E9                           shr ecx, 1
002C4F7B  E9 42 FD FF FF                  jmp 0x1402c4cc2
002C4F80  8B 05 32 1B D0 00               mov eax, dword ptr [rip + 0xd01b32]
002C4F86  A8 40                           test al, 0x40
002C4F88  0F 84 A0 FA FF FF               je 0x1402c4a2e
002C4F8E  E8 FD A4 04 00                  call 0x14030f490
002C4F93  84 C0                           test al, al
002C4F95  0F 84 93 FA FF FF               je 0x1402c4a2e
002C4F9B  8B CD                           mov ecx, ebp
002C4F9D  E8 BE A4 04 00                  call 0x14030f460
002C4FA2  E9 89 FA FF FF                  jmp 0x1402c4a30
002C4FA7  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
002C4FAA  4C 8D 05 4F B0 D3 FF            lea r8, [rip - 0x2c4fb1]
002C4FB1  48 C1 E8 07                     shr rax, 7
002C4FB5  83 E0 1F                        and eax, 0x1f
002C4FB8  45 8B 84 80 30 46 01 00         mov r8d, dword ptr [r8 + rax*4 + 0x14630]
002C4FC0  E8 DB 3C 17 00                  call 0x140438ca0
002C4FC5  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
002C4FC9  E9 EE F7 FF FF                  jmp 0x1402c47bc
002C4FCE  83 F8 10                        cmp eax, 0x10
002C4FD1  0F 84 BA FA FF FF               je 0x1402c4a91
002C4FD7  83 F8 08                        cmp eax, 8
002C4FDA  0F 84 11 01 00 00               je 0x1402c50f1
002C4FE0  83 F8 18                        cmp eax, 0x18
002C4FE3  0F 85 AC FA FF FF               jne 0x1402c4a95
002C4FE9  44 0B F0                        or r14d, eax
002C4FEC  E9 A4 FA FF FF                  jmp 0x1402c4a95
002C4FF1  41 83 4F 10 09                  or dword ptr [r15 + 0x10], 9
002C4FF6  41 8B C8                        mov ecx, r8d
002C4FF9  E9 7F F8 FF FF                  jmp 0x1402c487d
002C4FFE  41 8B CE                        mov ecx, r14d
002C5001  E8 FA 29 07 00                  call 0x140337a00
002C5006  E9 59 F9 FF FF                  jmp 0x1402c4964
002C500B  48 8D 87 C0 00 00 00            lea rax, [rdi + 0xc0]
002C5012  E9 B2 FB FF FF                  jmp 0x1402c4bc9
002C5017  B9 02 00 00 00                  mov ecx, 2
002C501C  2B CE                           sub ecx, esi
002C501E  66 90                           nop
002C5020  48 C1 EB 09                     shr rbx, 9
002C5024  49 23 D9                        and rbx, r9
002C5027  49 8B C0                        mov rax, r8
002C502A  48 C1 ED 09                     shr rbp, 9
002C502E  48 03 D8                        add rbx, rax
002C5031  49 23 E9                        and rbp, r9
002C5034  49 8B C0                        mov rax, r8
002C5037  48 03 E8                        add rbp, rax
002C503A  48 83 E9 01                     sub rcx, 1
002C503E  75 E0                           jne 0x1402c5020
002C5040  48 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbp
002C5048  E9 E5 F6 FF FF                  jmp 0x1402c4732
002C504D  48 8B C2                        mov rax, rdx
002C5050  48 C1 E8 13                     shr rax, 0x13
002C5054  23 C6                           and eax, esi
002C5056  49 8B 8C C0 78 45 01 00         mov rcx, qword ptr [r8 + rax*8 + 0x14578]
002C505E  41 8B B4 80 10 3F 01 00         mov esi, dword ptr [r8 + rax*4 + 0x13f10]
002C5066  B8 10 00 00 00                  mov eax, 0x10
002C506B  48 3B C8                        cmp rcx, rax
002C506E  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
002C5076  41 8B C9                        mov ecx, r9d
002C5079  49 0F 45 C2                     cmovne rax, r10
002C507D  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002C5082  8B C2                           mov eax, edx
002C5084  25 00 00 20 04                  and eax, 0x4200000
002C5089  3D 00 00 20 04                  cmp eax, 0x4200000
002C508E  0F 94 C1                        sete cl
002C5091  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
002C5095  E9 FB F5 FF FF                  jmp 0x1402c4695
002C509A  49 8B CD                        mov rcx, r13
002C509D  E8 EE 85 FB FF                  call 0x14027d690
002C50A2  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002C50AA  48 8B D3                        mov rdx, rbx
002C50AD  E8 7E 25 5C 00                  call 0x140887630
002C50B2  85 C0                           test eax, eax
002C50B4  0F 88 58 FA FF FF               js 0x1402c4b12
002C50BA  49 8B CD                        mov rcx, r13
002C50BD  E8 2E 7B FB FF                  call 0x14027cbf0
002C50C2  0F B6 D0                        movzx edx, al
002C50C5  88 84 24 18 01 00 00            mov byte ptr [rsp + 0x118], al
002C50CC  E9 41 F6 FF FF                  jmp 0x1402c4712
002C50D1  41 83 E6 EF                     and r14d, 0xffffffef
002C50D5  41 83 CE 08                     or r14d, 8
002C50D9  E9 67 F8 FF FF                  jmp 0x1402c4945
002C50DE  41 83 E6 E7                     and r14d, 0xffffffe7
002C50E2  E9 5E F8 FF FF                  jmp 0x1402c4945
002C50E7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002C50EC  E9 D8 FD FF FF                  jmp 0x1402c4ec9
002C50F1  41 83 E6 EF                     and r14d, 0xffffffef
002C50F5  41 83 CE 08                     or r14d, 8
002C50F9  E9 97 F9 FF FF                  jmp 0x1402c4a95
002C50FE  41 83 E6 E7                     and r14d, 0xffffffe7
002C5102  E9 8E F9 FF FF                  jmp 0x1402c4a95
002C5107  4C 8B CF                        mov r9, rdi
002C510A  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002C5113  4D 8B C4                        mov r8, r12
002C5116  BA 00 40 04 00                  mov edx, 0x44000
002C511B  B9 1A 00 00 00                  mov ecx, 0x1a
002C5120  E8 3B 85 23 00                  call 0x1404fd660
002C5125  CC                              int3
002C5126  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002C512B  48 2B D1                        sub rdx, rcx
002C512E  48 C1 FA 03                     sar rdx, 3
002C5132  48 FF C2                        inc rdx
002C5135  E8 3A C2 21 00                  call 0x1404e1374
002C513A  E9 A3 F9 FF FF                  jmp 0x1402c4ae2
002C513F  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002C5147  E8 0C 0C 72 00                  call 0x1409e5d58
002C514C  E9 BF F9 FF FF                  jmp 0x1402c4b10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProtectPrivateMemory(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned __int8 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int8 v_stack_p118;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pF0;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    a4 = 0;
    v_r12 = (a2) >> (9);
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    *(unsigned __int16 *)(v_rsp + 24) = 0;
    v_stack_m88 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_r12 = (v_r12) & (a3);
    v_stack_mA0 = 0;
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    v_r12 = (v_r12) + (a2);
    v_rbp = (a3) >> (9);
    v_rbp = (v_rbp) & (a3);
    v_rbp = (v_rbp) + (a2);
    v_stack_m84 = 0;
    v_stack_m50 = v_rbp;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (0xA00000ULL));
    v_stack_m98 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 1;
    if (((unsigned int)(result)) == 0xA00000ULL) goto loc_002C504D;
    v_stack_m68 = 1;
loc_002C4695:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) >> (12));
    a2 = (unsigned int)((a2) & (127));
    v_stack_mA8 = 0;
    v_stack_m58 = a2;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, v_rip - 2901634, a4);
    a2 = 0;
    v_stack_p30 = (unsigned __int8)(result);
    v_stack_mB8 = 0;
    v_stack_mC0 = v_stack_m70;
    v_stack_mC8 = 0;
    result = MiComputePageCommitment(0, a3, v_stack_p8, (unsigned __int8)(result));
    a2 = (v_rbp) - (v_r12);
    a2 = (a2) >> (3);
    a2 = (a2) + 1;
    if (result != a2) goto loc_002C4E2E;
    if (v_stack_m70 != 0) goto loc_002C509A;
loc_002C4712:
    if (((unsigned int)(a4 + 3)) <= 1) goto loc_002C5017;
loc_002C4732:
    v_r13 = (v_r12) >> (9);
    v_r13 = (v_r13) & ((unsigned __int8)(result));
    v_r13 = (v_r13) + (v_stack_p8);
loc_002C474A:
    a4 = 0;
    result = MiMakeSystemAddressValid(v_r12, (unsigned int)(v_stack_m58), a6, a4);
    if (*(unsigned __int64 *)(v_r12) == 0) goto loc_002C4FA7;
    v_stack_mC8 = v_stack_p18;
    result = MiGetPageProtection(v_stack_p8, v_r12, v_stack_m60, v_stack_m88);
    if (v_stack_m60 != 0) goto loc_002C4D41;
    v_stack_mA8 = 1;
loc_002C47BC:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2901928 + (unsigned int)((unsigned int)(result)) * 4 + 83504))) | ((unsigned int)((unsigned int)(v_stack_m88))));
    *(unsigned int *)(a7) = (unsigned int)(a3);
loc_002C47D0:
    if (v_r12 > v_rbp) goto loc_002C4ABD;
    if (((v_r12) & (0xFFFULL)) == 0) goto loc_002C4B38;
    if (v_stack_mA8 != 0) goto loc_002C4B38;
loc_002C47F1:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r12))) & (1)) == 0) goto loc_002C49CC;
    if (v_stack_mA0 != 0) goto loc_002C4897;
    result = MiGetProcessorFlushList(v_stack_p8, v_r12, a3, v_stack_m88);
    a3 = 0;
    v_stack_mA0 = result;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned int *)(result + 20) = 32;
    *(unsigned __int64 *)(result) = v_stack_m90;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90 + 184))) >> (8));
    result = ((((unsigned __int8)(a1)) & (8)) != 0) ? 1 : 0;
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + 184)))) & (15)) != 0) goto loc_002C486A;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_stack_m90 != a1) goto loc_002C4FF1;
loc_002C486A:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + 184)))) & (15)) == 0) { a1 = 1; }
loc_002C487D:
    *(unsigned int *)(result + 8) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 25) = 0;
    *(unsigned int *)(result + 28) = 0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
loc_002C4897:
    v_rdi = (*(unsigned __int64 *)(v_r12)) >> (12);
    v_rdi = (v_rdi) & (1);
    v_rsi = (v_rdi + v_rdi * 2) << (4);
    v_rsi = (v_rsi) + (1);
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 48))) & (112));
    if (((unsigned __int8)(result)) == 64) goto loc_002C4C8B;
loc_002C48D6:
    if (sign_flag) goto loc_002C4CD5;
    if (((a5) & (257)) != 0) goto loc_002C4D8C;
    v_rbp = 0;
loc_002C48F6:
    if (condition_is_below) goto loc_002C4A20;
    result = (*(unsigned __int64 *)(v_rsi + 16)) >> (5);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)((unsigned int)(a4))) == 24) goto loc_002C4CA7;
    if (((unsigned int)(result)) == 24) goto loc_002C4C12;
loc_002C4924:
    result = (unsigned int)((result) & (24));
    if (condition_is_not_equal) goto loc_002C4E40;
loc_002C492D:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (24));
    if (((unsigned int)(result)) == 24) goto loc_002C50DE;
    v_r14 = (unsigned int)(a4);
    if (((unsigned int)(result)) == 8) {
        v_r14 = (unsigned int)(((unsigned int)(a4)) & (0xFFFFFFF7ULL));
    }
    if (*(unsigned __int64 *)(v_rsi + 16) == 0) goto loc_002C4FFE;
    a2 = ((unsigned int)((unsigned int)(v_r14))) << (5);
    result = (a2) ^ (*(unsigned __int64 *)(v_rsi + 16));
    result = (result) & (-993);
    result = (result) ^ (a2);
loc_002C4964:
    *(unsigned __int64 *)(v_rsi + 16) = result;
loc_002C497F:
    v_stack_mC8 = v_stack_mA0;
    result = MiRevertValidPte(v_stack_p8, v_r12, (unsigned int)((unsigned int)(v_r14)), v_rdi);
loc_002C49A2:
    if (v_stack_m84 != 0) goto loc_002C4E74;
loc_002C49AD:
    goto loc_002C47D0;
loc_002C49CC:
    if (v_stack_m84 < 0) goto loc_002C4EDB;
    if (v_stack_m84 >= 0) goto loc_002C4A3F;
    result = MiSetProtectionOnTransitionPte(v_stack_p8, v_r12 + v_stack_m78 * 8, (unsigned int)((unsigned int)(v_r14)), 1);
    if (v_stack_m68 != 1) goto loc_002C4E9B;
    if ((unsigned int)(result) != 0) goto loc_002C4B2E;
loc_002C4A0C:
    v_r12 = (v_r12 + v_stack_m68 * 8) + (8);
    v_rbx = (v_r12 + v_stack_m78 * 8) + (8);
    goto loc_002C47D0;
loc_002C4A20:
    v_rbp = (unsigned int)((v_stack_m50) + 1);
    if (((*(unsigned int *)(v_rip + 13633668)) & ((unsigned int)(v_rbp))) == 0) goto loc_002C4F80;
loc_002C4A2E:
loc_002C4A30:
    if (!sign_flag) goto loc_002C48F6;
    goto loc_002C4A20;
loc_002C4A3F:
    if (v_stack_m68 != 1) goto loc_002C5107;
    if (v_stack_m90 == 0) goto loc_002C4DF3;
    result = (v_stack_m90) >> (5);
loc_002C4A5E:
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(v_r14)) == 24) goto loc_002C4DCD;
    if (((unsigned int)(result)) == 24) goto loc_002C4CB2;
loc_002C4A74:
    result = (unsigned int)((result) & (24));
    if (condition_is_not_equal) goto loc_002C4FCE;
loc_002C4A7D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (24));
    if (((unsigned int)(result)) == 24) goto loc_002C50FE;
    if (((unsigned int)(result)) == 8) {
        v_r14 = (unsigned int)((v_r14) & (0xFFFFFFF7ULL));
    }
    if (v_stack_m90 == 0) goto loc_002C4E63;
    a1 = ((unsigned int)((unsigned int)(v_r14))) << (5);
    result = (a1) ^ (v_stack_m90);
    result = (result) & (-993);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_r12) = result;
    goto loc_002C4A0C;
loc_002C4ABD:
    result = v_stack_mA0;
    if (v_stack_mA0 != 0) {
        a1 = v_stack_mA0;
        result = MiFlushTbList(a1, v_r12 + v_stack_m78 * 8, (unsigned int)((unsigned int)(v_r14)), 1);
        result = MiReleaseProcessorFlushList(a1, v_r12 + v_stack_m78 * 8, (unsigned int)((unsigned int)(v_r14)), 1);
    }
    if (v_stack_m98 != 0) goto loc_002C5126;
loc_002C4AE2:
    if (v_r13 != 0) {
        a2 = v_r13;
        a1 = v_stack_m90;
        result = MiUnlockPageTable(a1, a2, (unsigned int)((unsigned int)(v_r14)), 1);
    }
    result = MiUnlockWorkingSetShared(v_stack_m90, a6, (unsigned int)((unsigned int)(v_r14)), 1);
    if (v_stack_m70 != 0) goto loc_002C513F;
loc_002C4B10:
    result = 0;
loc_002C4B12:
    v_rsp = (v_rsp) + (176);
    return result;
loc_002C4B2E:
    goto loc_002C47D0;
loc_002C4B38:
    v_stack_p40 = 0;
    if (v_r13 == 0) goto loc_002C4B68;
    result = v_stack_p48;
    v_r15 = result;
    if (v_stack_p48 != 0) {
        a1 = v_stack_p48;
        result = MiFlushTbList(a1, v_stack_m70, (unsigned int)((unsigned int)(v_r14)), 1);
        result = MiReleaseProcessorFlushList(a1, v_stack_m70, (unsigned int)((unsigned int)(v_r14)), 1);
        v_r15 = 0;
        v_stack_p48 = 0;
    }
    result = v_stack_p50;
    if (v_stack_p50 != 0) {
        a2 = v_stack_p68;
        a1 = v_stack_p50;
        a2 = (a2) - (v_stack_p50);
        a2 = (a2) >> (3);
        a2 = (a2) + 1;
        result = MiFlushGraphicsPtes(a1, a2, (unsigned int)((unsigned int)(v_r14)), 1);
        v_stack_p50 = 0;
    }
    if (v_r13 != 0) {
        a2 = v_r13;
        a1 = v_stack_p58;
        result = MiUnlockPageTable(a1, a2, (unsigned int)((unsigned int)(v_r14)), 1);
    }
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 184))) & (15));
    if (((unsigned __int8)(result)) > 5) goto loc_002C4C3E;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_002C500B;
loc_002C4BC9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_002C4CA0;
loc_002C4BEB:
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324))) << (6);
    if (condition_is_above_or_equal) goto loc_002C4C3E;
loc_002C4BF8:
    result = MiUnlockWorkingSetShared(v_stack_p58, a6, (unsigned int)((unsigned int)(v_r14)), 1);
    result = MiLockWorkingSetShared(v_stack_p58, a6, (unsigned int)((unsigned int)(v_r14)), 1);
    goto loc_002C4C47;
loc_002C4C12:
    if (condition_is_above_or_equal) goto loc_002C4D7E;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pF0 + 48))) >> (7));
loc_002C4C2B:
    a2 = (unsigned int)((a2) & (31));
    if (((unsigned int)(a2)) == 24) goto loc_002C492D;
    goto loc_002C4924;
loc_002C4C3E:
    result = KeShouldYieldProcessor(v_stack_p58, a2, v_stack_pF0, 1);
    if ((unsigned int)(result) != 0) goto loc_002C4BF8;
loc_002C4C47:
    v_r13 = (v_stack_p20) >> (9);
    v_r13 = (v_r13) & (result);
    v_r13 = (v_r13) + (result);
    a4 = 0;
    result = MiMakeSystemAddressValid(v_stack_p20, (unsigned int)(v_stack_p90), a6, a4);
    goto loc_002C47F1;
loc_002C4C8B:
    result = MiRotatedToFrameBuffer(v_stack_p20, (unsigned int)(v_stack_p90), a6, a4);
    if ((unsigned int)(result) != 0) goto loc_002C497F;
    goto loc_002C48D6;
loc_002C4CA0:
    result = 0;
    goto loc_002C4BEB;
loc_002C4CA7:
    goto loc_002C4945;
loc_002C4CB2:
    if (condition_is_above_or_equal) goto loc_002C4F72;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 48))) >> (7));
loc_002C4CC2:
    a1 = (unsigned int)((a1) & (31));
    if (((unsigned int)(a1)) == 24) goto loc_002C4A7D;
    goto loc_002C4A74;
loc_002C4CD5:
    result = MiFlushTbList(v_stack_p48, (unsigned int)(v_stack_p90), a6, a4);
    result = MiReleaseProcessorFlushList(v_stack_p48, (unsigned int)(v_stack_p90), a6, a4);
    v_rdi = 0;
    v_stack_p48 = 0;
    if (v_stack_p50 != 0) {
        a2 = v_stack_p68;
        a1 = v_stack_p50;
        a2 = (a2) - (v_stack_p50);
        a2 = (a2) >> (3);
        a2 = (a2) + 1;
        result = MiFlushGraphicsPtes(a1, a2, a6, a4);
        v_stack_p50 = 0;
    }
    result = MiMakeProtoPrivate(v_stack_p58, a6, v_stack_p20, a4);
    if ((unsigned int)(result) != 0) goto loc_002C4DD8;
loc_002C4D34:
    goto loc_002C47D0;
loc_002C4D41:
    result = MiUnlockPageTable(v_stack_p58, v_r13, v_stack_p20, a4);
    result = MiUnlockWorkingSetShared(v_stack_p58, a6, v_stack_p20, a4);
    result = MiFaultInPagedPool(v_stack_p88, a6, v_stack_p20, a4);
    result = MiLockWorkingSetShared(v_stack_p58, a6, v_stack_p20, a4);
    goto loc_002C474A;
loc_002C4D7E:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 72) + 32))) >> (1));
    goto loc_002C4C2B;
loc_002C4D8C:
    v_stack_p20 = a8;
    result = MiMakeVaRangeNoAccess(v_stack_pF0, v_stack_p20, v_rbp, 0);
    if ((unsigned int)(result) != 0) goto loc_002C49A2;
    goto loc_002C47D0;
loc_002C4DCD:
    goto loc_002C4A95;
loc_002C4DD8:
    if (((unsigned int)(v_stack_p48)) != 1) goto loc_002C4F5A;
    goto loc_002C47D0;
loc_002C4DF3:
    a2 = (v_r12) >> (9);
    a2 = (a2) & (v_stack_p48);
    a4 = 0;
    a2 = (a2) + (v_stack_p48);
    result = MiIncreaseUsedPtes(v_stack_pF0, a2, a4 + 1, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pF0 + 48))) >> (7));
    goto loc_002C4A5E;
loc_002C4E2E:
    result = MiUnlockWorkingSetShared(v_r13, a2, a4 + 1, a4);
    goto loc_002C4B12;
loc_002C4E40:
    if (((unsigned int)((unsigned int)(0xC000002DULL))) == 16) goto loc_002C4941;
    if (((unsigned int)((unsigned int)(0xC000002DULL))) == 8) goto loc_002C50D1;
    if (((unsigned int)((unsigned int)(0xC000002DULL))) != 24) goto loc_002C4945;
    v_r14 = (unsigned int)((24) | ((unsigned int)((unsigned int)(0xC000002DULL))));
    goto loc_002C4945;
loc_002C4E63:
    result = MiMakeDemandZeroPte((unsigned int)((unsigned int)(v_r14)), a2, a4 + 1, a4);
    *(unsigned __int64 *)(v_r12) = result;
    goto loc_002C4A0C;
loc_002C4E74:
    result = v_stack_p50;
    if (v_stack_p50 == 0) { result = v_stack_p20; }
    v_stack_p50 = result;
    result = (v_stack_p70) - 1;
    v_stack_p68 = v_stack_p20 + result * 8;
    goto loc_002C49AD;
loc_002C4E9B:
    if (v_stack_p64 == 0) goto loc_002C50E7;
    result = v_stack_p50;
    if (v_stack_p50 == 0) { result = v_stack_p20; }
    v_stack_p50 = result;
    v_stack_p68 = v_stack_p20 + v_stack_p70 - 1 * 8;
loc_002C4EC9:
    goto loc_002C47D0;
loc_002C4EDB:
    result = v_stack_p48;
    v_r15 = 0;
    if (v_stack_p48 != 0) {
        a1 = v_stack_p48;
        result = MiFlushTbList(a1, v_stack_p20 + v_stack_p70 - 1 * 8, a4 + 1, a4);
        result = MiReleaseProcessorFlushList(a1, v_stack_p20 + v_stack_p70 - 1 * 8, a4 + 1, a4);
        v_r15 = 0;
        v_stack_p48 = 0;
    }
    if (v_stack_p50 != 0) {
        a2 = v_stack_p68;
        a1 = v_stack_p50;
        a2 = (a2) - (v_stack_p50);
        a2 = (a2) >> (3);
        a2 = (a2) + 1;
        result = MiFlushGraphicsPtes(a1, a2, a4 + 1, a4);
        v_stack_p50 = 0;
    }
    result = MiMakeProtoLeafValid(v_stack_p20 + v_stack_p70 * 8, 1, a6, a4);
    v_rbx = v_stack_p20 + v_stack_p70 * 8;
    v_r12 = v_r12 + (unsigned int)((unsigned int)(v_r14)) * 8;
    if (sign_flag) {
        v_r12 = (v_r12 + (unsigned int)((unsigned int)(v_r14)) * 8) + (8);
        v_rbx = (v_stack_p20 + v_stack_p70 * 8) + (8);
    }
    v_stack_p40 = 1;
    goto loc_002C47D0;
loc_002C4F5A:
    v_r13 = 0;
    v_stack_p40 = 1;
    result = MiLockWorkingSetShared(v_stack_p58, 1, a6, a4);
    goto loc_002C4D34;
loc_002C4F72:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pF0 + 72) + 32))) >> (1));
    goto loc_002C4CC2;
loc_002C4F80:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13638450)))) & (64)) == 0) goto loc_002C4A2E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, 1, a6, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002C4A2E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), 1, a6, a4);
    goto loc_002C4A30;
loc_002C4FA7:
    result = ((unsigned int)(*(unsigned int *)(v_stack_pF0 + 48))) >> (7);
    result = (unsigned int)((result) & (31));
    result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD((unsigned int)((unsigned int)(v_rbp)), 1, (unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)), a4);
    v_stack_p60 = (unsigned int)(result);
    goto loc_002C47BC;
loc_002C4FCE:
    if (((unsigned int)(result)) == 16) goto loc_002C4A91;
    if (((unsigned int)(result)) == 8) goto loc_002C50F1;
    if (((unsigned int)(result)) != 24) goto loc_002C4A95;
    v_r14 = (unsigned int)((v_r14) | ((unsigned int)(result)));
    goto loc_002C4A95;
loc_002C4FF1:
    goto loc_002C487D;
loc_002C4FFE:
    result = MiMakeDemandZeroPte((unsigned int)((unsigned int)(v_r14)), 1, (unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)), a4);
    goto loc_002C4964;
loc_002C500B:
    goto loc_002C4BC9;
loc_002C5017:
    a1 = (unsigned int)((2) - ((unsigned int)(v_stack_pF0)));
loc_002C5020:
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & (0);
    v_rbp = (v_rbp) >> (9);
    v_rbx = (v_rbx) + ((unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)));
    v_rbp = (v_rbp) & (0);
    v_rbp = (v_rbp) + ((unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)));
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_002C5020;
    v_stack_p98 = v_rbp;
    goto loc_002C4732;
loc_002C504D:
    result = (1) >> (19);
    result = (unsigned int)((result) & ((unsigned int)(v_stack_pF0)));
    v_stack_p80 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)) + result * 8 + 83320);
    result = 16;
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)) + result * 8 + 83320)) != 16) { result = 1; }
    v_stack_p70 = result;
    result = (unsigned int)((1) & (0x4200000ULL));
    a1 = (((unsigned int)(result)) == 0x4200000ULL) ? 1 : 0;
    v_stack_p64 = (unsigned int)(a1);
    goto loc_002C4695;
loc_002C509A:
    result = MiUnlockWorkingSetShared(0, 1, (unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)), a4);
    result = MiChargeFullProcessCommitment(v_stack_pA0, v_rbx, (unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)), a4);
    if (sign_flag) goto loc_002C4B12;
    result = MiLockWorkingSetShared(0, v_rbx, (unsigned int)(*(unsigned int *)(v_rip - 2903985 + result * 4 + 83504)), a4);
    v_stack_p118 = (unsigned __int8)(result);
    goto loc_002C4712;
loc_002C50D1:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFEFULL));
    v_r14 = (unsigned int)((v_r14) | (8));
    goto loc_002C4945;
loc_002C50DE:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFE7ULL));
    goto loc_002C4945;
loc_002C50E7:
    goto loc_002C4EC9;
loc_002C50F1:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFEFULL));
    v_r14 = (unsigned int)((v_r14) | (8));
    goto loc_002C4A95;
loc_002C50FE:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFE7ULL));
    goto loc_002C4A95;
loc_002C5107:
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x44000ULL), v_r12, v_stack_p58);
loc_002C5126:
    a2 = (v_stack_p68) - (26);
    a2 = (a2) >> (3);
    a2 = (a2) + 1;
    result = MiFlushGraphicsPtes(26, a2, v_r12, v_stack_p58);
    goto loc_002C4AE2;
loc_002C513F:
    result = MiReturnFullProcessCommitment(v_stack_pA0, a2, v_r12, v_stack_p58);
    goto loc_002C4B10;
}
```

## 5. (Beta) C Style

```c
int64_t MiProtectPrivateMemory(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, void *Arg7, int64_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint8_t v_stack_p118;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint32_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pF0;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    Arg4 = 0;
    local_r12 = (Arg2) >> (9);
    *(uint64_t *)(local_rsp - 0x60) = 0;
    *(uint16_t *)(local_rsp + 0x18) = 0;
    v_stack_m88 = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    local_r12 = (local_r12) & (Arg3);
    v_stack_mA0 = 0;
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    local_r12 = (local_r12) + (Arg2);
    local_rbp = (Arg3) >> (9);
    local_rbp = (local_rbp) & (Arg3);
    local_rbp = (local_rbp) + (Arg2);
    v_stack_m84 = 0;
    v_stack_m50 = local_rbp;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (0xA00000ULL));
    v_stack_m98 = 0;
    v_stack_m80 = 0;
    v_stack_m78 = 1;
    if (((uint32_t)(result)) == 0xA00000ULL) goto loc_002C504D;
    v_stack_m68 = 1;
loc_002C4695:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) >> (12));
    Arg2 = (uint32_t)((Arg2) & (127));
    v_stack_mA8 = 0;
    v_stack_m58 = Arg2;
    result = MiLockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, v_rip - 2901634, Arg4);
    Arg2 = 0;
    v_stack_p30 = (uint8_t)(result);
    v_stack_mB8 = 0;
    v_stack_mC0 = v_stack_m70;
    v_stack_mC8 = 0;
    result = MiComputePageCommitment(0, Arg3, v_stack_p8, (uint8_t)(result));
    Arg2 = (local_rbp) - (local_r12);
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) + 1;
    if (result != Arg2) goto loc_002C4E2E;
    if (v_stack_m70 != 0) goto loc_002C509A;
loc_002C4712:
    if (((uint32_t)(Arg4 + 3)) <= 1) goto loc_002C5017;
loc_002C4732:
    local_r13 = (local_r12) >> (9);
    local_r13 = (local_r13) & ((uint8_t)(result));
    local_r13 = (local_r13) + (v_stack_p8);
loc_002C474A:
    Arg4 = 0;
    result = MiMakeSystemAddressValid(local_r12, (uint32_t)(v_stack_m58), Arg6, Arg4);
    if (*(uint64_t *)(local_r12) == 0) goto loc_002C4FA7;
    v_stack_mC8 = v_stack_p18;
    result = MiGetPageProtection(v_stack_p8, local_r12, v_stack_m60, v_stack_m88);
    if (v_stack_m60 != 0) goto loc_002C4D41;
    v_stack_mA8 = 1;
loc_002C47BC:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x2C47A8 + (uint32_t)((uint32_t)(result)) * 4 + 0x14630))) | ((uint32_t)((uint32_t)(v_stack_m88))));
    *(uint32_t *)(arg7) = (uint32_t)(Arg3);
loc_002C47D0:
    if (local_r12 > local_rbp) goto loc_002C4ABD;
    if (((local_r12) & (0xFFFULL)) == 0) goto loc_002C4B38;
    if (v_stack_mA8 != 0) goto loc_002C4B38;
loc_002C47F1:
    if ((((uint8_t)(*(uint64_t *)(local_r12))) & (1)) == 0) goto loc_002C49CC;
    if (v_stack_mA0 != 0) goto loc_002C4897;
    result = MiGetProcessorFlushList(v_stack_p8, local_r12, Arg3, v_stack_m88);
    Arg3 = 0;
    v_stack_mA0 = result;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0x14) = 32;
    *(uint64_t *)(result) = v_stack_m90;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90 + 0xB8))) >> (8));
    result = ((((uint8_t)(Arg1)) & (8)) != 0) ? 1 : 0;
    *(uint8_t *)(result + 0x18) = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0xB8)))) & (15)) != 0) goto loc_002C486A;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (v_stack_m90 != Arg1) goto loc_002C4FF1;
loc_002C486A:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_002C487D:
    *(uint32_t *)(result + 0x8) = (uint32_t)(Arg1);
    *(uint16_t *)(result + 0x19) = 0;
    *(uint32_t *)(result + 0x1C) = 0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
loc_002C4897:
    local_rdi = (*(uint64_t *)(local_r12)) >> (12);
    local_rdi = (local_rdi) & (1);
    local_rsi = (local_rdi + local_rdi * 2) << (4);
    local_rsi = (local_rsi) + (1);
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x30))) & (112));
    if (((uint8_t)(result)) == 64) goto loc_002C4C8B;
loc_002C48D6:
    if (sign_flag) goto loc_002C4CD5;
    if (((Arg5) & (257)) != 0) goto loc_002C4D8C;
    local_rbp = 0;
loc_002C48F6:
    if (condition_is_below) goto loc_002C4A20;
    result = (*(uint64_t *)(local_rsi + 0x10)) >> (5);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)((uint32_t)(Arg4))) == 24) goto loc_002C4CA7;
    if (((uint32_t)(result)) == 24) goto loc_002C4C12;
loc_002C4924:
    result = (uint32_t)((result) & (24));
    if (condition_is_not_equal) goto loc_002C4E40;
loc_002C492D:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (24));
    if (((uint32_t)(result)) == 24) goto loc_002C50DE;
    local_r14 = (uint32_t)(Arg4);
    if (((uint32_t)(result)) == 8) {
        local_r14 = (uint32_t)(((uint32_t)(Arg4)) & (0xFFFFFFF7ULL));
    }
    if (*(uint64_t *)(local_rsi + 0x10) == 0) goto loc_002C4FFE;
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) << (5);
    result = (Arg2) ^ (*(uint64_t *)(local_rsi + 0x10));
    result = (result) & (-993);
    result = (result) ^ (Arg2);
loc_002C4964:
    *(uint64_t *)(local_rsi + 0x10) = result;
loc_002C497F:
    v_stack_mC8 = v_stack_mA0;
    result = MiRevertValidPte(v_stack_p8, local_r12, (uint32_t)((uint32_t)(local_r14)), local_rdi);
loc_002C49A2:
    if (v_stack_m84 != 0) goto loc_002C4E74;
loc_002C49AD:
    goto loc_002C47D0;
loc_002C49CC:
    if (v_stack_m84 < 0) goto loc_002C4EDB;
    if (v_stack_m84 >= 0) goto loc_002C4A3F;
    result = MiSetProtectionOnTransitionPte(v_stack_p8, local_r12 + v_stack_m78 * 8, (uint32_t)((uint32_t)(local_r14)), 1);
    if (v_stack_m68 != 1) goto loc_002C4E9B;
    if ((uint32_t)(result) != 0) goto loc_002C4B2E;
loc_002C4A0C:
    local_r12 = (local_r12 + v_stack_m68 * 8) + (8);
    local_rbx = (local_r12 + v_stack_m78 * 8) + (8);
    goto loc_002C47D0;
loc_002C4A20:
    local_rbp = (uint32_t)((v_stack_m50) + 1);
    if (((*(uint32_t *)(v_rip + 0xD00884)) & ((uint32_t)(local_rbp))) == 0) goto loc_002C4F80;
loc_002C4A2E:
loc_002C4A30:
    if (!sign_flag) goto loc_002C48F6;
    goto loc_002C4A20;
loc_002C4A3F:
    if (v_stack_m68 != 1) goto loc_002C5107;
    if (v_stack_m90 == 0) goto loc_002C4DF3;
    result = (v_stack_m90) >> (5);
loc_002C4A5E:
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(local_r14)) == 24) goto loc_002C4DCD;
    if (((uint32_t)(result)) == 24) goto loc_002C4CB2;
loc_002C4A74:
    result = (uint32_t)((result) & (24));
    if (condition_is_not_equal) goto loc_002C4FCE;
loc_002C4A7D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (24));
    if (((uint32_t)(result)) == 24) goto loc_002C50FE;
    if (((uint32_t)(result)) == 8) {
        local_r14 = (uint32_t)((local_r14) & (0xFFFFFFF7ULL));
    }
    if (v_stack_m90 == 0) goto loc_002C4E63;
    Arg1 = ((uint32_t)((uint32_t)(local_r14))) << (5);
    result = (Arg1) ^ (v_stack_m90);
    result = (result) & (-993);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_r12) = result;
    goto loc_002C4A0C;
loc_002C4ABD:
    result = v_stack_mA0;
    if (v_stack_mA0 != 0) {
        Arg1 = v_stack_mA0;
        result = MiFlushTbList(Arg1, local_r12 + v_stack_m78 * 8, (uint32_t)((uint32_t)(local_r14)), 1);
        result = MiReleaseProcessorFlushList(Arg1, local_r12 + v_stack_m78 * 8, (uint32_t)((uint32_t)(local_r14)), 1);
    }
    if (v_stack_m98 != 0) goto loc_002C5126;
loc_002C4AE2:
    if (local_r13 != 0) {
        Arg2 = local_r13;
        Arg1 = v_stack_m90;
        result = MiUnlockPageTable(Arg1, Arg2, (uint32_t)((uint32_t)(local_r14)), 1);
    }
    result = MiUnlockWorkingSetShared(v_stack_m90, Arg6, (uint32_t)((uint32_t)(local_r14)), 1);
    if (v_stack_m70 != 0) goto loc_002C513F;
loc_002C4B10:
    result = 0;
loc_002C4B12:
    local_rsp = (local_rsp) + (176);
    return result;
loc_002C4B2E:
    goto loc_002C47D0;
loc_002C4B38:
    v_stack_p40 = 0;
    if (local_r13 == 0) goto loc_002C4B68;
    result = v_stack_p48;
    local_r15 = result;
    if (v_stack_p48 != 0) {
        Arg1 = v_stack_p48;
        result = MiFlushTbList(Arg1, v_stack_m70, (uint32_t)((uint32_t)(local_r14)), 1);
        result = MiReleaseProcessorFlushList(Arg1, v_stack_m70, (uint32_t)((uint32_t)(local_r14)), 1);
        local_r15 = 0;
        v_stack_p48 = 0;
    }
    result = v_stack_p50;
    if (v_stack_p50 != 0) {
        Arg2 = v_stack_p68;
        Arg1 = v_stack_p50;
        Arg2 = (Arg2) - (v_stack_p50);
        Arg2 = (Arg2) >> (3);
        Arg2 = (Arg2) + 1;
        result = MiFlushGraphicsPtes(Arg1, Arg2, (uint32_t)((uint32_t)(local_r14)), 1);
        v_stack_p50 = 0;
    }
    if (local_r13 != 0) {
        Arg2 = local_r13;
        Arg1 = v_stack_p58;
        result = MiUnlockPageTable(Arg1, Arg2, (uint32_t)((uint32_t)(local_r14)), 1);
    }
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xB8))) & (15));
    if (((uint8_t)(result)) > 5) goto loc_002C4C3E;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_002C500B;
loc_002C4BC9:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_002C4CA0;
loc_002C4BEB:
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144))) << (6);
    if (condition_is_above_or_equal) goto loc_002C4C3E;
loc_002C4BF8:
    result = MiUnlockWorkingSetShared(v_stack_p58, Arg6, (uint32_t)((uint32_t)(local_r14)), 1);
    result = MiLockWorkingSetShared(v_stack_p58, Arg6, (uint32_t)((uint32_t)(local_r14)), 1);
    goto loc_002C4C47;
loc_002C4C12:
    if (condition_is_above_or_equal) goto loc_002C4D7E;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pF0 + 0x30))) >> (7));
loc_002C4C2B:
    Arg2 = (uint32_t)((Arg2) & (31));
    if (((uint32_t)(Arg2)) == 24) goto loc_002C492D;
    goto loc_002C4924;
loc_002C4C3E:
    result = KeShouldYieldProcessor(v_stack_p58, Arg2, v_stack_pF0, 1);
    if ((uint32_t)(result) != 0) goto loc_002C4BF8;
loc_002C4C47:
    local_r13 = (v_stack_p20) >> (9);
    local_r13 = (local_r13) & (result);
    local_r13 = (local_r13) + (result);
    Arg4 = 0;
    result = MiMakeSystemAddressValid(v_stack_p20, (uint32_t)(v_stack_p90), Arg6, Arg4);
    goto loc_002C47F1;
loc_002C4C8B:
    result = MiRotatedToFrameBuffer(v_stack_p20, (uint32_t)(v_stack_p90), Arg6, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002C497F;
    goto loc_002C48D6;
loc_002C4CA0:
    result = 0;
    goto loc_002C4BEB;
loc_002C4CA7:
    goto loc_002C4945;
loc_002C4CB2:
    if (condition_is_above_or_equal) goto loc_002C4F72;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x30))) >> (7));
loc_002C4CC2:
    Arg1 = (uint32_t)((Arg1) & (31));
    if (((uint32_t)(Arg1)) == 24) goto loc_002C4A7D;
    goto loc_002C4A74;
loc_002C4CD5:
    result = MiFlushTbList(v_stack_p48, (uint32_t)(v_stack_p90), Arg6, Arg4);
    result = MiReleaseProcessorFlushList(v_stack_p48, (uint32_t)(v_stack_p90), Arg6, Arg4);
    local_rdi = 0;
    v_stack_p48 = 0;
    if (v_stack_p50 != 0) {
        Arg2 = v_stack_p68;
        Arg1 = v_stack_p50;
        Arg2 = (Arg2) - (v_stack_p50);
        Arg2 = (Arg2) >> (3);
        Arg2 = (Arg2) + 1;
        result = MiFlushGraphicsPtes(Arg1, Arg2, Arg6, Arg4);
        v_stack_p50 = 0;
    }
    result = MiMakeProtoPrivate(v_stack_p58, Arg6, v_stack_p20, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002C4DD8;
loc_002C4D34:
    goto loc_002C47D0;
loc_002C4D41:
    result = MiUnlockPageTable(v_stack_p58, local_r13, v_stack_p20, Arg4);
    result = MiUnlockWorkingSetShared(v_stack_p58, Arg6, v_stack_p20, Arg4);
    result = MiFaultInPagedPool(v_stack_p88, Arg6, v_stack_p20, Arg4);
    result = MiLockWorkingSetShared(v_stack_p58, Arg6, v_stack_p20, Arg4);
    goto loc_002C474A;
loc_002C4D7E:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x48) + 0x20))) >> (1));
    goto loc_002C4C2B;
loc_002C4D8C:
    v_stack_p20 = Arg8;
    result = MiMakeVaRangeNoAccess(v_stack_pF0, v_stack_p20, local_rbp, 0);
    if ((uint32_t)(result) != 0) goto loc_002C49A2;
    goto loc_002C47D0;
loc_002C4DCD:
    goto loc_002C4A95;
loc_002C4DD8:
    if (((uint32_t)(v_stack_p48)) != 1) goto loc_002C4F5A;
    goto loc_002C47D0;
loc_002C4DF3:
    Arg2 = (local_r12) >> (9);
    Arg2 = (Arg2) & (v_stack_p48);
    Arg4 = 0;
    Arg2 = (Arg2) + (v_stack_p48);
    result = MiIncreaseUsedPtes(v_stack_pF0, Arg2, Arg4 + 1, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pF0 + 0x30))) >> (7));
    goto loc_002C4A5E;
loc_002C4E2E:
    result = MiUnlockWorkingSetShared(local_r13, Arg2, Arg4 + 1, Arg4);
    goto loc_002C4B12;
loc_002C4E40:
    if (((uint32_t)((uint32_t)(0xC000002DULL))) == 16) goto loc_002C4941;
    if (((uint32_t)((uint32_t)(0xC000002DULL))) == 8) goto loc_002C50D1;
    if (((uint32_t)((uint32_t)(0xC000002DULL))) != 24) goto loc_002C4945;
    local_r14 = (uint32_t)((24) | ((uint32_t)((uint32_t)(0xC000002DULL))));
    goto loc_002C4945;
loc_002C4E63:
    result = MiMakeDemandZeroPte((uint32_t)((uint32_t)(local_r14)), Arg2, Arg4 + 1, Arg4);
    *(uint64_t *)(local_r12) = result;
    goto loc_002C4A0C;
loc_002C4E74:
    result = v_stack_p50;
    if (v_stack_p50 == 0) { result = v_stack_p20; }
    v_stack_p50 = result;
    result = (v_stack_p70) - 1;
    v_stack_p68 = v_stack_p20 + result * 8;
    goto loc_002C49AD;
loc_002C4E9B:
    if (v_stack_p64 == 0) goto loc_002C50E7;
    result = v_stack_p50;
    if (v_stack_p50 == 0) { result = v_stack_p20; }
    v_stack_p50 = result;
    v_stack_p68 = v_stack_p20 + v_stack_p70 - 1 * 8;
loc_002C4EC9:
    goto loc_002C47D0;
loc_002C4EDB:
    result = v_stack_p48;
    local_r15 = 0;
    if (v_stack_p48 != 0) {
        Arg1 = v_stack_p48;
        result = MiFlushTbList(Arg1, v_stack_p20 + v_stack_p70 - 1 * 8, Arg4 + 1, Arg4);
        result = MiReleaseProcessorFlushList(Arg1, v_stack_p20 + v_stack_p70 - 1 * 8, Arg4 + 1, Arg4);
        local_r15 = 0;
        v_stack_p48 = 0;
    }
    if (v_stack_p50 != 0) {
        Arg2 = v_stack_p68;
        Arg1 = v_stack_p50;
        Arg2 = (Arg2) - (v_stack_p50);
        Arg2 = (Arg2) >> (3);
        Arg2 = (Arg2) + 1;
        result = MiFlushGraphicsPtes(Arg1, Arg2, Arg4 + 1, Arg4);
        v_stack_p50 = 0;
    }
    result = MiMakeProtoLeafValid(v_stack_p20 + v_stack_p70 * 8, 1, Arg6, Arg4);
    local_rbx = v_stack_p20 + v_stack_p70 * 8;
    local_r12 = local_r12 + (uint32_t)((uint32_t)(local_r14)) * 8;
    if (sign_flag) {
        local_r12 = (local_r12 + (uint32_t)((uint32_t)(local_r14)) * 8) + (8);
        local_rbx = (v_stack_p20 + v_stack_p70 * 8) + (8);
    }
    v_stack_p40 = 1;
    goto loc_002C47D0;
loc_002C4F5A:
    local_r13 = 0;
    v_stack_p40 = 1;
    result = MiLockWorkingSetShared(v_stack_p58, 1, Arg6, Arg4);
    goto loc_002C4D34;
loc_002C4F72:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pF0 + 0x48) + 0x20))) >> (1));
    goto loc_002C4CC2;
loc_002C4F80:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD01B32)))) & (64)) == 0) goto loc_002C4A2E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, 1, Arg6, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002C4A2E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), 1, Arg6, Arg4);
    goto loc_002C4A30;
loc_002C4FA7:
    result = ((uint32_t)(*(uint32_t *)(v_stack_pF0 + 0x30))) >> (7);
    result = (uint32_t)((result) & (31));
    result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD((uint32_t)((uint32_t)(local_rbp)), 1, (uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)), Arg4);
    v_stack_p60 = (uint32_t)(result);
    goto loc_002C47BC;
loc_002C4FCE:
    if (((uint32_t)(result)) == 16) goto loc_002C4A91;
    if (((uint32_t)(result)) == 8) goto loc_002C50F1;
    if (((uint32_t)(result)) != 24) goto loc_002C4A95;
    local_r14 = (uint32_t)((local_r14) | ((uint32_t)(result)));
    goto loc_002C4A95;
loc_002C4FF1:
    goto loc_002C487D;
loc_002C4FFE:
    result = MiMakeDemandZeroPte((uint32_t)((uint32_t)(local_r14)), 1, (uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)), Arg4);
    goto loc_002C4964;
loc_002C500B:
    goto loc_002C4BC9;
loc_002C5017:
    Arg1 = (uint32_t)((2) - ((uint32_t)(v_stack_pF0)));
loc_002C5020:
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & (0);
    local_rbp = (local_rbp) >> (9);
    local_rbx = (local_rbx) + ((uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)));
    local_rbp = (local_rbp) & (0);
    local_rbp = (local_rbp) + ((uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)));
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_002C5020;
    v_stack_p98 = local_rbp;
    goto loc_002C4732;
loc_002C504D:
    result = (1) >> (19);
    result = (uint32_t)((result) & ((uint32_t)(v_stack_pF0)));
    v_stack_p80 = *(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)) + result * 8 + 0x14578);
    result = 16;
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)) + result * 8 + 0x14578)) != 16) { result = 1; }
    v_stack_p70 = result;
    result = (uint32_t)((1) & (0x4200000ULL));
    Arg1 = (((uint32_t)(result)) == 0x4200000ULL) ? 1 : 0;
    v_stack_p64 = (uint32_t)(Arg1);
    goto loc_002C4695;
loc_002C509A:
    result = MiUnlockWorkingSetShared(0, 1, (uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)), Arg4);
    result = MiChargeFullProcessCommitment(v_stack_pA0, local_rbx, (uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)), Arg4);
    if (sign_flag) goto loc_002C4B12;
    result = MiLockWorkingSetShared(0, local_rbx, (uint32_t)(*(uint32_t *)(v_rip - 0x2C4FB1 + result * 4 + 0x14630)), Arg4);
    v_stack_p118 = (uint8_t)(result);
    goto loc_002C4712;
loc_002C50D1:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFEFULL));
    local_r14 = (uint32_t)((local_r14) | (8));
    goto loc_002C4945;
loc_002C50DE:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFE7ULL));
    goto loc_002C4945;
loc_002C50E7:
    goto loc_002C4EC9;
loc_002C50F1:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFEFULL));
    local_r14 = (uint32_t)((local_r14) | (8));
    goto loc_002C4A95;
loc_002C50FE:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFE7ULL));
    goto loc_002C4A95;
loc_002C5107:
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x44000ULL), local_r12, v_stack_p58);
loc_002C5126:
    Arg2 = (v_stack_p68) - (26);
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) + 1;
    result = MiFlushGraphicsPtes(26, Arg2, local_r12, v_stack_p58);
    goto loc_002C4AE2;
loc_002C513F:
    result = MiReturnFullProcessCommitment(v_stack_pA0, Arg2, local_r12, v_stack_p58);
    goto loc_002C4B10;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x0 + rax*1` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C45B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
