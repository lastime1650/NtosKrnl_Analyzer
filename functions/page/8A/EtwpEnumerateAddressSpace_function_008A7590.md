# EtwpEnumerateAddressSpace

- RVA: `0x008A7590`–`0x008A7E9F` (길이 `2,319` bytes)
- VA: `0x00000001408A7590`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F250`
- 디코드: `464`개 명령, `2,319/2,319` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008A7722` → [MmEnumerateAddressSpaceAndReferenceImages](../97/MmEnumerateAddressSpaceAndReferenceImages_function_0097DD50.md) (function, `0x0097DD50`)
- `0x008A77CF` → [KeAreInterruptsEnabled](../../text/2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x008A7812` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008A7837` → [ObQueryNameStringMode](ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x008A7865` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x008A7975` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008A7A95` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x008A7AB2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008A7BA7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008A7C14` → [EtwpTraceImageUnload](../../text/44/EtwpTraceImageUnload_function_0044C048.md) (function, `0x0044C048`)
- `0x008A7C2A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A7C43` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008A7D3F` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x008A7D66` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008A7DCA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008A7E21` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)

### Direct callers
- [EtwTraceProcess](EtwTraceProcess_function_008A4004.md) at `0x008A41AA`
- [EtwpProcessEnumCallback](EtwpProcessEnumCallback_function_008A5F40.md) at `0x008A601A`
- [EtwpProcessEnumCallback](EtwpProcessEnumCallback_function_008A5F40.md) at `0x008A6172`

### Static image references
- `0x008A75AA` → RVA `0x00E0A740` (`.data`; read)
- `0x008A77F2` → RVA `0x00E65BF0` (`.data`; read)
- `0x008A7A4B` → RVA `0x000105E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x008A77CF` → [KeAreInterruptsEnabled](../../text/2F/KeAreInterruptsEnabled_function_002F8060.md) (`PAGE` → `.text`)
  - `0x008A7812` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008A7865` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x008A7975` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008A7A95` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (`PAGE` → `.text`)
  - `0x008A7AB2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008A7BA7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008A7C14` → [EtwpTraceImageUnload](../../text/44/EtwpTraceImageUnload_function_0044C048.md) (`PAGE` → `.text`)
  - `0x008A7C2A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A7C43` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008A7D3F` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (`PAGE` → `.text`)
  - `0x008A7D66` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008A7DCA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008A7E21` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A7590  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008A7595  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
008A759A  57                              push rdi
008A759B  41 54                           push r12
008A759D  41 55                           push r13
008A759F  41 56                           push r14
008A75A1  41 57                           push r15
008A75A3  48 81 EC C0 01 00 00            sub rsp, 0x1c0
008A75AA  48 8B 05 8F 31 56 00            mov rax, qword ptr [rip + 0x56318f]
008A75B1  48 33 C4                        xor rax, rsp
008A75B4  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
008A75BC  4C 8B EA                        mov r13, rdx
008A75BF  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
008A75C7  4C 8B C9                        mov r9, rcx
008A75CA  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
008A75D2  48 89 8C 24 00 01 00 00         mov qword ptr [rsp + 0x100], rcx
008A75DA  48 89 94 24 08 01 00 00         mov qword ptr [rsp + 0x108], rdx
008A75E2  33 F6                           xor esi, esi
008A75E4  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
008A75E8  0F 57 C0                        xorps xmm0, xmm0
008A75EB  0F 11 84 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm0
008A75F3  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
008A75FB  4D 85 C0                        test r8, r8
008A75FE  0F 84 55 08 00 00               je 0x1408a7e59
008A7604  41 8B 00                        mov eax, dword ptr [r8]
008A7607  A8 04                           test al, 4
008A7609  0F 84 4A 08 00 00               je 0x1408a7e59
008A760F  BF 01 00 00 00                  mov edi, 1
008A7614  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
008A7618  4D 85 C0                        test r8, r8
008A761B  0F 84 43 08 00 00               je 0x1408a7e64
008A7621  41 F7 40 04 00 80 00 00         test dword ptr [r8 + 4], 0x8000
008A7629  0F 84 35 08 00 00               je 0x1408a7e64
008A762F  B0 01                           mov al, 1
008A7631  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
008A7635  84 C0                           test al, al
008A7637  74 0B                           je 0x1408a7644
008A7639  83 CF 04                        or edi, 4
008A763C  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
008A7640  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
008A7644  4D 85 ED                        test r13, r13
008A7647  74 19                           je 0x1408a7662
008A7649  4D 85 C0                        test r8, r8
008A764C  74 14                           je 0x1408a7662
008A764E  41 F7 00 00 80 00 00            test dword ptr [r8], 0x8000
008A7655  74 0B                           je 0x1408a7662
008A7657  83 CF 02                        or edi, 2
008A765A  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
008A765E  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
008A7662  85 FF                           test edi, edi
008A7664  0F 84 4A 07 00 00               je 0x1408a7db4
008A766A  4D 85 ED                        test r13, r13
008A766D  0F 84 E3 06 00 00               je 0x1408a7d56
008A7673  48 8B 52 20                     mov rdx, qword ptr [rdx + 0x20]
008A7677  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
008A767F  48 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdx
008A7687  41 0F B6 4D 40                  movzx ecx, byte ptr [r13 + 0x40]
008A768C  4D 8B 7D 10                     mov r15, qword ptr [r13 + 0x10]
008A7690  0F B6 C1                        movzx eax, cl
008A7693  F6 D8                           neg al
008A7695  66 1B D2                        sbb dx, dx
008A7698  66 81 C2 04 14                  add dx, 0x1404
008A769D  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
008A76A1  66 89 54 24 5C                  mov word ptr [rsp + 0x5c], dx
008A76A6  0F B6 C1                        movzx eax, cl
008A76A9  F6 D8                           neg al
008A76AB  66 45 1B E4                     sbb r12w, r12w
008A76AF  66 41 81 C4 28 04               add r12w, 0x428
008A76B5  F6 D9                           neg cl
008A76B7  66 1B C9                        sbb cx, cx
008A76BA  66 81 C1 81 02                  add cx, 0x281
008A76BF  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
008A76C3  66 89 4C 24 64                  mov word ptr [rsp + 0x64], cx
008A76C8  66 44 89 64 24 60               mov word ptr [rsp + 0x60], r12w
008A76CE  44 89 64 24 70                  mov dword ptr [rsp + 0x70], r12d
008A76D3  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
008A76DB  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
008A76E3  4D 85 FF                        test r15, r15
008A76E6  0F 84 86 07 00 00               je 0x1408a7e72
008A76EC  8B C6                           mov eax, esi
008A76EE  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
008A76F6  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
008A76FD  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
008A7705  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
008A770C  48 89 B4 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rsi
008A7714  66 89 74 24 50                  mov word ptr [rsp + 0x50], si
008A7719  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
008A771D  8B D7                           mov edx, edi
008A771F  49 8B C9                        mov rcx, r9
008A7722  E8 29 66 0D 00                  call 0x14097dd50
008A7727  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
008A772F  48 85 C0                        test rax, rax
008A7732  0F 84 F7 04 00 00               je 0x1408a7c2f
008A7738  48 8B D8                        mov rbx, rax
008A773B  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
008A7743  48 8B 03                        mov rax, qword ptr [rbx]
008A7746  48 85 C0                        test rax, rax
008A7749  0F 84 D1 04 00 00               je 0x1408a7c20
008A774F  48 8B C8                        mov rcx, rax
008A7752  83 E1 03                        and ecx, 3
008A7755  48 83 E0 FC                     and rax, 0xfffffffffffffffc
008A7759  48 89 03                        mov qword ptr [rbx], rax
008A775C  44 8B F6                        mov r14d, esi
008A775F  89 B4 24 94 00 00 00            mov dword ptr [rsp + 0x94], esi
008A7766  48 85 C9                        test rcx, rcx
008A7769  0F 85 4C 05 00 00               jne 0x1408a7cbb
008A776F  40 F6 C7 02                     test dil, 2
008A7773  0F 85 ED 04 00 00               jne 0x1408a7c66
008A7779  89 B4 24 90 00 00 00            mov dword ptr [rsp + 0x90], esi
008A7780  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008A7784  4C 8B E0                        mov r12, rax
008A7787  49 C1 EC 06                     shr r12, 6
008A778B  41 83 E4 0F                     and r12d, 0xf
008A778F  44 89 A4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r12d
008A7797  4C 8B E8                        mov r13, rax
008A779A  49 C1 ED 0A                     shr r13, 0xa
008A779E  41 83 E5 07                     and r13d, 7
008A77A2  44 89 AC 24 BC 00 00 00         mov dword ptr [rsp + 0xbc], r13d
008A77AA  48 25 3F E0 FF FF               and rax, 0xffffffffffffe03f
008A77B0  48 89 43 08                     mov qword ptr [rbx + 8], rax
008A77B4  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
008A77BC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008A77C5  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
008A77CD  75 13                           jne 0x1408a77e2
008A77CF  E8 8C 08 A5 FF                  call 0x1402f8060
008A77D4  84 C0                           test al, al
008A77D6  74 0A                           je 0x1408a77e2
008A77D8  44 0F 20 C0                     mov rax, cr8
008A77DC  3C 01                           cmp al, 1
008A77DE  8B C6                           mov eax, esi
008A77E0  72 05                           jb 0x1408a77e7
008A77E2  B8 01 00 00 00                  mov eax, 1
008A77E7  85 C0                           test eax, eax
008A77E9  0F 85 7C 06 00 00               jne 0x1408a7e6b
008A77EF  48 8B 0B                        mov rcx, qword ptr [rbx]
008A77F2  48 8B 05 F7 E3 5B 00            mov rax, qword ptr [rip + 0x5be3f7]
008A77F9  48 85 C0                        test rax, rax
008A77FC  74 23                           je 0x1408a7821
008A77FE  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
008A7802  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
008A780A  4D 8B C7                        mov r8, r15
008A780D  BA 00 04 00 00                  mov edx, 0x400
008A7812  E8 B9 32 E1 FF                  call 0x1406baad0
008A7817  8B F8                           mov edi, eax
008A7819  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
008A781D  85 C0                           test eax, eax
008A781F  79 21                           jns 0x1408a7842
008A7821  48 8B 0B                        mov rcx, qword ptr [rbx]
008A7824  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
008A7829  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
008A782E  41 B8 00 20 00 00               mov r8d, 0x2000
008A7834  49 8B D7                        mov rdx, r15
008A7837  E8 94 06 00 00                  call 0x1408a7ed0
008A783C  8B F8                           mov edi, eax
008A783E  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
008A7842  89 B4 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], esi
008A7849  44 8B 73 28                     mov r14d, dword ptr [rbx + 0x28]
008A784D  44 89 B4 24 88 00 00 00         mov dword ptr [rsp + 0x88], r14d
008A7855  4C 8B 7B 10                     mov r15, qword ptr [rbx + 0x10]
008A7859  4C 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r15
008A7861  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008A7865  E8 F6 C2 B9 FF                  call 0x140443b60
008A786A  48 85 C0                        test rax, rax
008A786D  74 22                           je 0x1408a7891
008A786F  44 8B 70 58                     mov r14d, dword ptr [rax + 0x58]
008A7873  44 89 B4 24 88 00 00 00         mov dword ptr [rsp + 0x88], r14d
008A787B  8B 70 08                        mov esi, dword ptr [rax + 8]
008A787E  89 B4 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], esi
008A7885  4C 8B 78 30                     mov r15, qword ptr [rax + 0x30]
008A7889  4C 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r15
008A7891  33 C0                           xor eax, eax
008A7893  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
008A789B  E9 B6 00 00 00                  jmp 0x1408a7956
008A78A0  33 C0                           xor eax, eax
008A78A2  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
008A78AA  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
008A78B2  8B 7C 24 7C                     mov edi, dword ptr [rsp + 0x7c]
008A78B6  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
008A78BE  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
008A78C6  0F B7 4C 24 5C                  movzx ecx, word ptr [rsp + 0x5c]
008A78CB  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
008A78CF  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
008A78D7  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
008A78DC  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
008A78E0  0F B7 4C 24 64                  movzx ecx, word ptr [rsp + 0x64]
008A78E5  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
008A78E9  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
008A78ED  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
008A78F1  8B 8C 24 80 00 00 00            mov ecx, dword ptr [rsp + 0x80]
008A78F8  48 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rcx
008A7900  8B 8C 24 84 00 00 00            mov ecx, dword ptr [rsp + 0x84]
008A7907  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
008A790F  44 8B A4 24 B8 00 00 00         mov r12d, dword ptr [rsp + 0xb8]
008A7917  44 8B AC 24 BC 00 00 00         mov r13d, dword ptr [rsp + 0xbc]
008A791F  44 8B B4 24 88 00 00 00         mov r14d, dword ptr [rsp + 0x88]
008A7927  8B B4 24 8C 00 00 00            mov esi, dword ptr [rsp + 0x8c]
008A792E  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
008A7936  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
008A793E  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
008A7946  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
008A794E  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
008A7956  85 FF                           test edi, edi
008A7958  0F 88 70 02 00 00               js 0x1408a7bce
008A795E  48 85 D2                        test rdx, rdx
008A7961  0F 84 76 02 00 00               je 0x1408a7bdd
008A7967  33 D2                           xor edx, edx
008A7969  44 8D 42 40                     lea r8d, [rdx + 0x40]
008A796D  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
008A7975  E8 C6 F2 E1 FF                  call 0x1406c6c40
008A797A  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
008A7982  4D 85 FF                        test r15, r15
008A7985  0F 84 4B 02 00 00               je 0x1408a7bd6
008A798B  41 0F B7 17                     movzx edx, word ptr [r15]
008A798F  66 85 D2                        test dx, dx
008A7992  0F 84 3E 02 00 00               je 0x1408a7bd6
008A7998  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
008A799C  33 F6                           xor esi, esi
008A799E  48 85 C9                        test rcx, rcx
008A79A1  0F 84 F3 00 00 00               je 0x1408a7a9a
008A79A7  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
008A79AF  8B 80 D0 01 00 00               mov eax, dword ptr [rax + 0x1d0]
008A79B5  89 84 24 30 01 00 00            mov dword ptr [rsp + 0x130], eax
008A79BC  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008A79C0  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
008A79C8  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
008A79CC  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
008A79D4  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
008A79D7  89 84 24 34 01 00 00            mov dword ptr [rsp + 0x134], eax
008A79DE  89 B4 24 38 01 00 00            mov dword ptr [rsp + 0x138], esi
008A79E5  44 88 A4 24 3C 01 00 00         mov byte ptr [rsp + 0x13c], r12b
008A79ED  44 88 AC 24 3D 01 00 00         mov byte ptr [rsp + 0x13d], r13b
008A79F5  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
008A79F9  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
008A7A01  66 89 B4 24 3E 01 00 00         mov word ptr [rsp + 0x13e], si
008A7A09  48 89 B4 24 48 01 00 00         mov qword ptr [rsp + 0x148], rsi
008A7A11  48 89 B4 24 50 01 00 00         mov qword ptr [rsp + 0x150], rsi
008A7A19  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
008A7A21  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
008A7A29  48 C7 84 24 88 01 00 00 38 00 00 00  mov qword ptr [rsp + 0x188], 0x38
008A7A35  48 89 8C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rcx
008A7A3D  89 94 24 98 01 00 00            mov dword ptr [rsp + 0x198], edx
008A7A44  89 B4 24 9C 01 00 00            mov dword ptr [rsp + 0x19c], esi
008A7A4B  48 8D 05 8E 8B 76 FF            lea rax, [rip - 0x897472]
008A7A52  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
008A7A5A  48 C7 84 24 A8 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x1a8], 2
008A7A66  C7 44 24 28 03 18 50 00         mov dword ptr [rsp + 0x28], 0x501803
008A7A6E  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
008A7A72  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
008A7A77  44 8D 4E 03                     lea r9d, [rsi + 3]
008A7A7B  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008A7A83  44 8B 00                        mov r8d, dword ptr [rax]
008A7A86  48 8B 90 50 05 00 00            mov rdx, qword ptr [rax + 0x550]
008A7A8D  48 8D 8C 24 80 01 00 00         lea rcx, [rsp + 0x180]
008A7A95  E8 66 51 9B FF                  call 0x14025cc00
008A7A9A  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
008A7AA2  48 85 C9                        test rcx, rcx
008A7AA5  74 10                           je 0x1408a7ab7
008A7AA7  48 8B 05 42 E1 5B 00            mov rax, qword ptr [rip + 0x5be142]
008A7AAE  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
008A7AB2  E8 19 30 E1 FF                  call 0x1406baad0
008A7AB7  4C 8B 0B                        mov r9, qword ptr [rbx]
008A7ABA  8B BC 24 90 00 00 00            mov edi, dword ptr [rsp + 0x90]
008A7AC1  85 FF                           test edi, edi
008A7AC3  0F 84 0B 03 00 00               je 0x1408a7dd4
008A7AC9  0F 10 13                        movups xmm2, xmmword ptr [rbx]
008A7ACC  0F 10 5B 10                     movups xmm3, xmmword ptr [rbx + 0x10]
008A7AD0  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
008A7AD4  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
008A7ADC  0F 57 C9                        xorps xmm1, xmm1
008A7ADF  0F 11 0B                        movups xmmword ptr [rbx], xmm1
008A7AE2  0F 11 4B 10                     movups xmmword ptr [rbx + 0x10], xmm1
008A7AE6  0F 11 4B 20                     movups xmmword ptr [rbx + 0x20], xmm1
008A7AEA  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
008A7AF2  8B 80 D0 01 00 00               mov eax, dword ptr [rax + 0x1d0]
008A7AF8  89 43 28                        mov dword ptr [rbx + 0x28], eax
008A7AFB  66 48 0F 7E D0                  movq rax, xmm2
008A7B00  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
008A7B04  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
008A7B08  66 0F 73 DA 08                  psrldq xmm2, 8
008A7B0D  66 48 0F D6 13                  movq qword ptr [rbx], xmm2
008A7B12  66 0F 73 DB 08                  psrldq xmm3, 8
008A7B17  66 48 0F D6 5B 18               movq qword ptr [rbx + 0x18], xmm3
008A7B1D  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008A7B25  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
008A7B29  44 8B 84 24 C8 00 00 00         mov r8d, dword ptr [rsp + 0xc8]
008A7B31  49 C1 E0 30                     shl r8, 0x30
008A7B35  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
008A7B3C  48 C1 E0 35                     shl rax, 0x35
008A7B40  49 8B D0                        mov rdx, r8
008A7B43  48 33 53 10                     xor rdx, qword ptr [rbx + 0x10]
008A7B47  48 B9 FF FF FF FF FF FF 40 FF   movabs rcx, 0xff40ffffffffffff
008A7B51  48 23 D1                        and rdx, rcx
008A7B54  48 B9 00 00 00 00 00 00 20 00   movabs rcx, 0x20000000000000
008A7B5E  48 23 C1                        and rax, rcx
008A7B61  48 33 D0                        xor rdx, rax
008A7B64  48 B8 FF FF FF FF FF FF 5F FF   movabs rax, 0xff5fffffffffffff
008A7B6E  4C 23 C0                        and r8, rax
008A7B71  49 33 D0                        xor rdx, r8
008A7B74  48 B8 00 00 00 00 00 00 40 00   movabs rax, 0x40000000000000
008A7B7E  48 0B D0                        or rdx, rax
008A7B81  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
008A7B85  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008A7B89  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
008A7B8E  C7 44 24 6C 00 80 00 00         mov dword ptr [rsp + 0x6c], 0x8000
008A7B96  41 BE 03 00 00 00               mov r14d, 3
008A7B9C  C7 44 24 54 2C 00 00 00         mov dword ptr [rsp + 0x54], 0x2c
008A7BA4  49 8B C9                        mov rcx, r9
008A7BA7  E8 A4 17 A5 FF                  call 0x1402f9350
008A7BAC  4C 8B AC 24 B0 00 00 00         mov r13, qword ptr [rsp + 0xb0]
008A7BB4  85 FF                           test edi, edi
008A7BB6  0F 85 EF 01 00 00               jne 0x1408a7dab
008A7BBC  48 83 C3 30                     add rbx, 0x30
008A7BC0  8B 7C 24 58                     mov edi, dword ptr [rsp + 0x58]
008A7BC4  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
008A7BC9  E9 6D FB FF FF                  jmp 0x1408a773b
008A7BCE  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
008A7BD6  33 F6                           xor esi, esi
008A7BD8  E9 BD FE FF FF                  jmp 0x1408a7a9a
008A7BDD  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008A7BE1  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
008A7BE6  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
008A7BEB  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
008A7BF0  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
008A7BF4  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
008A7BF9  4C 8B 4B 18                     mov r9, qword ptr [rbx + 0x18]
008A7BFD  4C 8B 43 08                     mov r8, qword ptr [rbx + 8]
008A7C01  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
008A7C09  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
008A7C11  49 8B CF                        mov rcx, r15
008A7C14  E8 2F 44 BA FF                  call 0x14044c048
008A7C19  33 F6                           xor esi, esi
008A7C1B  E9 7A FE FF FF                  jmp 0x1408a7a9a
008A7C20  33 D2                           xor edx, edx
008A7C22  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
008A7C2A  E8 41 AC 2D 00                  call 0x140b82870
008A7C2F  4D 85 ED                        test r13, r13
008A7C32  0F 84 84 01 00 00               je 0x1408a7dbc
008A7C38  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
008A7C40  48 33 CC                        xor rcx, rsp
008A7C43  E8 F8 49 E0 FF                  call 0x1406ac640
008A7C48  4C 8D 9C 24 C0 01 00 00         lea r11, [rsp + 0x1c0]
008A7C50  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
008A7C54  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
008A7C58  49 8B E3                        mov rsp, r11
008A7C5B  41 5F                           pop r15
008A7C5D  41 5E                           pop r14
008A7C5F  41 5D                           pop r13
008A7C61  41 5C                           pop r12
008A7C63  5F                              pop rdi
008A7C64  C3                              ret
008A7C65  CC                              int3
008A7C66  C7 84 24 90 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x90], 1
008A7C71  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
008A7C75  48 8B C1                        mov rax, rcx
008A7C78  48 D1 E8                        shr rax, 1
008A7C7B  83 E0 1F                        and eax, 0x1f
008A7C7E  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
008A7C86  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
008A7C8D  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
008A7C91  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
008A7C99  48 8B C1                        mov rax, rcx
008A7C9C  48 83 E0 C0                     and rax, 0xffffffffffffffc0
008A7CA0  48 89 43 08                     mov qword ptr [rbx + 8], rax
008A7CA4  83 E1 01                        and ecx, 1
008A7CA7  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
008A7CAF  89 8C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ecx
008A7CB6  E9 C5 FA FF FF                  jmp 0x1408a7780
008A7CBB  48 83 F9 02                     cmp rcx, 2
008A7CBF  0F 84 66 01 00 00               je 0x1408a7e2b
008A7CC5  66 44 89 64 24 50               mov word ptr [rsp + 0x50], r12w
008A7CCB  C7 44 24 6C 00 80 00 00         mov dword ptr [rsp + 0x6c], 0x8000
008A7CD3  B9 2C 00 00 00                  mov ecx, 0x2c
008A7CD8  44 8D 71 D7                     lea r14d, [rcx - 0x29]
008A7CDC  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
008A7CE0  4D 85 ED                        test r13, r13
008A7CE3  0F 84 F8 00 00 00               je 0x1408a7de1
008A7CE9  B8 02 18 60 00                  mov eax, 0x601802
008A7CEE  45 85 F6                        test r14d, r14d
008A7CF1  74 08                           je 0x1408a7cfb
008A7CF3  41 8B C6                        mov eax, r14d
008A7CF6  0D 00 18 60 00                  or eax, 0x601800
008A7CFB  48 89 9C 24 60 01 00 00         mov qword ptr [rsp + 0x160], rbx
008A7D03  89 8C 24 68 01 00 00            mov dword ptr [rsp + 0x168], ecx
008A7D0A  89 B4 24 6C 01 00 00            mov dword ptr [rsp + 0x16c], esi
008A7D11  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008A7D15  0F B7 44 24 50                  movzx eax, word ptr [rsp + 0x50]
008A7D1A  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
008A7D1F  41 B9 01 00 00 00               mov r9d, 1
008A7D25  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008A7D2D  44 8B 00                        mov r8d, dword ptr [rax]
008A7D30  48 8B 90 50 05 00 00            mov rdx, qword ptr [rax + 0x550]
008A7D37  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
008A7D3F  E8 BC 4E 9B FF                  call 0x14025cc00
008A7D44  48 83 C3 30                     add rbx, 0x30
008A7D48  8B 7C 24 58                     mov edi, dword ptr [rsp + 0x58]
008A7D4C  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
008A7D51  E9 E5 F9 FF FF                  jmp 0x1408a773b
008A7D56  BA 00 20 00 00                  mov edx, 0x2000
008A7D5B  B9 40 00 00 00                  mov ecx, 0x40
008A7D60  41 B8 50 65 72 66               mov r8d, 0x66726550
008A7D66  E8 85 A3 2D 00                  call 0x140b820f0
008A7D6B  4C 8B F8                        mov r15, rax
008A7D6E  41 BC 26 04 00 00               mov r12d, 0x426
008A7D74  B8 63 02 00 00                  mov eax, 0x263
008A7D79  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008A7D7D  66 89 44 24 64                  mov word ptr [rsp + 0x64], ax
008A7D82  48 8B C6                        mov rax, rsi
008A7D85  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008A7D8D  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
008A7D95  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
008A7D99  66 89 44 24 5C                  mov word ptr [rsp + 0x5c], ax
008A7D9E  4C 8B 8C 24 A0 00 00 00         mov r9, qword ptr [rsp + 0xa0]
008A7DA6  E9 1D F9 FF FF                  jmp 0x1408a76c8
008A7DAB  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
008A7DAF  E9 2C FF FF FF                  jmp 0x1408a7ce0
008A7DB4  4C 8B FE                        mov r15, rsi
008A7DB7  E9 73 FE FF FF                  jmp 0x1408a7c2f
008A7DBC  4D 85 FF                        test r15, r15
008A7DBF  0F 84 73 FE FF FF               je 0x1408a7c38
008A7DC5  33 D2                           xor edx, edx
008A7DC7  49 8B CF                        mov rcx, r15
008A7DCA  E8 A1 AA 2D 00                  call 0x140b82870
008A7DCF  E9 64 FE FF FF                  jmp 0x1408a7c38
008A7DD4  44 8B B4 24 94 00 00 00         mov r14d, dword ptr [rsp + 0x94]
008A7DDC  E9 C3 FD FF FF                  jmp 0x1408a7ba4
008A7DE1  B8 02 19 60 00                  mov eax, 0x601902
008A7DE6  45 85 F6                        test r14d, r14d
008A7DE9  0F 85 A3 00 00 00               jne 0x1408a7e92
008A7DEF  48 89 9C 24 70 01 00 00         mov qword ptr [rsp + 0x170], rbx
008A7DF7  89 8C 24 78 01 00 00            mov dword ptr [rsp + 0x178], ecx
008A7DFE  89 B4 24 7C 01 00 00            mov dword ptr [rsp + 0x17c], esi
008A7E05  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008A7E09  44 0F B7 4C 24 50               movzx r9d, word ptr [rsp + 0x50]
008A7E0F  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
008A7E14  BA 01 00 00 00                  mov edx, 1
008A7E19  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
008A7E21  E8 2A D5 98 FF                  call 0x140235350
008A7E26  E9 91 FD FF FF                  jmp 0x1408a7bbc
008A7E2B  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008A7E2F  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
008A7E34  C7 44 24 6C 00 80 00 20         mov dword ptr [rsp + 0x6c], 0x20008000
008A7E3C  4D 85 ED                        test r13, r13
008A7E3F  75 47                           jne 0x1408a7e88
008A7E41  C7 44 24 54 18 00 00 00         mov dword ptr [rsp + 0x54], 0x18
008A7E49  C7 43 14 00 80 00 00            mov dword ptr [rbx + 0x14], 0x8000
008A7E50  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
008A7E54  E9 87 FE FF FF                  jmp 0x1408a7ce0
008A7E59  8B FE                           mov edi, esi
008A7E5B  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
008A7E5F  E9 B4 F7 FF FF                  jmp 0x1408a7618
008A7E64  33 C0                           xor eax, eax
008A7E66  E9 C6 F7 FF FF                  jmp 0x1408a7631
008A7E6B  CD 2C                           int 0x2c
008A7E6D  E9 7D F9 FF FF                  jmp 0x1408a77ef
008A7E72  83 E7 FE                        and edi, 0xfffffffe
008A7E75  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
008A7E79  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
008A7E7D  0F 84 AC FD FF FF               je 0x1408a7c2f
008A7E83  E9 64 F8 FF FF                  jmp 0x1408a76ec
008A7E88  B9 20 00 00 00                  mov ecx, 0x20
008A7E8D  E9 4A FE FF FF                  jmp 0x1408a7cdc
008A7E92  41 8B C6                        mov eax, r14d
008A7E95  0D 00 19 60 00                  or eax, 0x601900
008A7E9A  E9 50 FF FF FF                  jmp 0x1408a7def
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEnumerateAddressSpace(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m13C;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned int v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int16 v_stack_m184;
    unsigned __int16 v_stack_m188;
    unsigned __int16 v_stack_m18C;
    unsigned int v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int16 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int16 v_stack_mAA;
    unsigned __int8 v_stack_mAB;
    unsigned __int8 v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 5648783)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m138 = a2;
    v_stack_m148 = a1;
    v_stack_mE8 = a1;
    v_stack_mE0 = a2;
    v_rsi = 0;
    v_stack_m194 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m128 = 0;
    if (a3 == 0) goto loc_008A7E59;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (4)) == 0) goto loc_008A7E59;
    v_stack_m190 = 1;
loc_008A7618:
    if (a3 == 0) goto loc_008A7E64;
    if (((*(unsigned int *)(a3 + 4)) & (0x8000ULL)) == 0) goto loc_008A7E64;
loc_008A7631:
    v_stack_m180 = 1;
    v_rdi = 1;
    if (1 != 0) {
        v_rdi = (unsigned int)((1) | (4));
        v_stack_m190 = (unsigned int)(v_rdi);
        v_stack_m180 = (unsigned int)(v_rdi);
    }
    if (a2 == 0) goto loc_008A7662;
    if (a3 == 0) goto loc_008A7662;
    if (((*(unsigned int *)(a3)) & (0x8000ULL)) != 0) {
        v_rdi = (unsigned int)((v_rdi) | (2));
        v_stack_m190 = (unsigned int)(v_rdi);
        v_stack_m180 = (unsigned int)(v_rdi);
    }
    if ((unsigned int)(v_rdi) == 0) goto loc_008A7DB4;
    if (a2 == 0) goto loc_008A7D56;
    v_stack_m140 = *(unsigned __int64 *)(a2 + 32);
    v_stack_m108 = *(unsigned __int64 *)(a2 + 32);
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(a2 + 64))));
    a2 = (unsigned __int16)((*(unsigned __int64 *)(a2 + 32)) + (0x1404ULL));
    v_stack_m174 = (unsigned int)(a2);
    v_stack_m18C = (unsigned __int16)(a2);
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(a2 + 64))));
    v_r12 = (unsigned __int16)((v_r12) + (0x428ULL));
    a1 = (unsigned __int8)(-(*(unsigned __int8 *)(a2 + 64)));
    a1 = (unsigned __int16)((a1) + (641));
    v_stack_m170 = (unsigned int)(a1);
    v_stack_m184 = (unsigned __int16)(a1);
loc_008A76C8:
    v_stack_m188 = (unsigned __int16)(v_r12);
    v_stack_m178 = (unsigned int)(v_r12);
    v_stack_m110 = *(unsigned __int64 *)(a2 + 16);
    v_stack_m150 = *(unsigned __int64 *)(a2 + 16);
    if (*(unsigned __int64 *)(a2 + 16) == 0) goto loc_008A7E72;
loc_008A76EC:
    v_stack_m120 = 0;
    v_stack_m168 = 0;
    v_stack_m118 = 0;
    v_stack_m164 = 0;
    v_stack_mF8 = 0;
    v_stack_m198 = 0;
    v_stack_m17C = 0;
    result = MmEnumerateAddressSpaceAndReferenceImages(a1, (unsigned int)((unsigned int)(v_rdi)), a3, a1);
    v_stack_mD8 = result;
    if (result == 0) goto loc_008A7C2F;
loc_008A773B:
    v_stack_mF0 = result;
    if (*(unsigned __int64 *)(result) == 0) goto loc_008A7C20;
    a1 = (unsigned int)((*(unsigned __int64 *)(result)) & (3));
    result = (*(unsigned __int64 *)(result)) & (-4);
    *(unsigned __int64 *)(result) = result;
    v_stack_m154 = 0;
    if (a1 != 0) goto loc_008A7CBB;
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_008A7C66;
    v_stack_m158 = 0;
loc_008A7780:
    v_r12 = (*(unsigned __int64 *)(result + 8)) >> (6);
    v_r12 = (unsigned int)((v_r12) & (15));
    v_stack_m130 = (unsigned int)(v_r12);
    v_r13 = (*(unsigned __int64 *)(result + 8)) >> (10);
    v_r13 = (unsigned int)((v_r13) & (7));
    v_stack_m12C = (unsigned int)(v_r13);
    result = (*(unsigned __int64 *)(result + 8)) & (0xFFFFFFFFFFFFE03FULL);
    *(unsigned __int64 *)(result + 8) = result;
    v_stack_m128 = 0;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_008A77E2;
    result = KeAreInterruptsEnabled(a1, (unsigned int)((unsigned int)(v_rdi)), a3, a1);
    if ((unsigned __int8)(result) == 0) goto loc_008A77E2;
    result = 0;
    if (((unsigned __int8)(v_cr8)) >= 1) {
        result = 1;
    }
    if ((unsigned int)(result) != 0) goto loc_008A7E6B;
loc_008A77EF:
    if (*(unsigned __int64 *)(v_rip + 6022135) == 0) goto loc_008A7821;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result), (unsigned int)(0x400ULL), *(unsigned __int64 *)(a2 + 16), v_stack_m128);
    v_stack_m16C = (unsigned int)(result);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (sign_flag) {
        a1 = *(unsigned __int64 *)(result);
        v_stack_m1C8 = 0;
        a4 = v_stack_m194;
        a3 = 0x2000ULL;
        a2 = *(unsigned __int64 *)(a2 + 16);
        result = ObQueryNameStringMode(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
        v_stack_m16C = (unsigned int)(result);
    }
    v_stack_m15C = 0;
    v_stack_m160 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    v_stack_m100 = *(unsigned __int64 *)(result + 16);
    result = RtlImageNtHeader(*(unsigned __int64 *)(result + 8), a2, a3, a4);
    v_r14 = (unsigned int)(*(unsigned int *)(result + 40));
    v_r15 = *(unsigned __int64 *)(result + 16);
    if (result != 0) {
        v_r14 = *(unsigned int *)(result + 88);
        v_stack_m160 = (unsigned int)(v_r14);
        v_rsi = *(unsigned int *)(result + 8);
        v_stack_m15C = (unsigned int)(v_rsi);
        v_r15 = *(unsigned __int64 *)(result + 48);
        v_stack_m100 = v_r15;
    }
    result = 0;
    goto loc_008A7956;
loc_008A7956:
    if (sign_flag) goto loc_008A7BCE;
    if (v_stack_m138 == 0) goto loc_008A7BDD;
    a2 = 0;
    result = memset(v_stack_mC8, a2, a2 + 64, a4);
    if (v_stack_m150 == 0) goto loc_008A7BD6;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m150)) == 0) goto loc_008A7BD6;
    v_rsi = 0;
    if (*(unsigned __int64 *)(v_stack_m150 + 8) != 0) {
        result = v_stack_m148;
        result = *(unsigned int *)(result + 464);
        v_stack_mB8 = (unsigned int)(result);
        result = *(unsigned __int64 *)(result + 8);
        v_stack_mC8 = result;
        result = *(unsigned __int64 *)(result + 24);
        v_stack_mC0 = result;
        result = *(unsigned int *)(result + 40);
        v_stack_mB4 = (unsigned int)(result);
        v_stack_mB0 = 0;
        v_stack_mAC = (unsigned __int8)(v_r12);
        v_stack_mAB = (unsigned __int8)(v_r13);
        result = *(unsigned __int64 *)(result + 16);
        v_stack_mA8 = result;
        v_stack_mAA = 0;
        v_stack_mA0 = 0;
        v_stack_m98 = 0;
        result = v_stack_mC8;
        v_stack_m68 = result;
        v_stack_m60 = 56;
        v_stack_m58 = *(unsigned __int64 *)(v_stack_m150 + 8);
        v_stack_m50 = (unsigned int)(*(unsigned __int16 *)(v_stack_m150));
        v_stack_m4C = 0;
        result = v_rip - 9008242;
        v_stack_m48 = result;
        v_stack_m40 = 2;
        v_stack_m1C0 = 0x501803ULL;
        result = v_stack_m174;
        v_stack_m1C8 = (unsigned __int16)(result);
        a4 = v_rsi + 3;
        result = v_stack_m140;
        a3 = *(unsigned int *)(result);
        a2 = *(unsigned __int64 *)(result + 1360);
        a1 = v_stack_m68;
        result = EtwpLogKernelEvent(a1, a2, a3, a4);
    }
    if (v_stack_m128 != 0) {
        result = *(unsigned __int64 *)(v_rip + 6021442);
        result = *(unsigned __int64 *)(result + 32);
        result = guard_dispatch_icall(v_stack_m128, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(v_stack_m158)) == 0) goto loc_008A7DD4;
    v_stack_m48 = v_xmm0;
    *(unsigned __int64 *)(result) = v_xmm1;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm1;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m148 + 464)));
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m148 + 464)) + 24);
    *(unsigned __int64 *)(result) = v_xmm2;
    *(unsigned __int64 *)(result + 24) = v_xmm3;
    *(unsigned __int64 *)(result + 32) = v_stack_mF8;
    a3 = ((unsigned int)(v_stack_m120)) << (48);
    result = ((unsigned int)(v_stack_m118)) << (53);
    a2 = (a3) ^ (*(unsigned __int64 *)(result + 16));
    a2 = (a2) & (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m148 + 464)) + 24));
    result = (result) & (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_stack_m148 + 464)) + 24));
    a2 = (a2) ^ (result);
    a3 = (a3) & (result);
    a2 = (a2) ^ (a3);
    a2 = (a2) | (result);
    *(unsigned __int64 *)(result + 16) = a2;
    v_stack_m198 = (unsigned __int16)((unsigned int)(v_stack_m178));
    v_stack_m17C = 0x8000ULL;
    v_stack_m194 = 44;
loc_008A7BA4:
    result = ObfDereferenceObject(*(unsigned __int64 *)(result), a2, a3, *(unsigned __int64 *)(result));
    if ((unsigned int)((unsigned int)(v_stack_m158)) != 0) goto loc_008A7DAB;
loc_008A7BBC:
    v_rbx = (result) + (48);
    goto loc_008A773B;
loc_008A7BCE:
loc_008A7BD6:
    v_rsi = 0;
    goto loc_008A7A9A;
loc_008A7BDD:
    v_stack_m1A0 = (unsigned int)(result);
    v_stack_m1A8 = v_stack_m150;
    v_stack_m1B0 = (unsigned int)(v_stack_m138);
    v_stack_m1B8 = (unsigned int)((unsigned int)(v_stack_m178));
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 3;
    result = EtwpTraceImageUnload(v_stack_m150, v_stack_m148, *(unsigned __int64 *)(v_rbx + 8), *(unsigned __int64 *)(v_rbx + 24));
    v_rsi = 0;
    goto loc_008A7A9A;
loc_008A7C20:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mD8, a2, *(unsigned __int64 *)(v_rbx + 8), *(unsigned __int64 *)(v_rbx + 24));
loc_008A7C2F:
    if (v_stack_m138 == 0) goto loc_008A7DBC;
loc_008A7C38:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rbx + 8), *(unsigned __int64 *)(v_rbx + 24));
    return result;
loc_008A7C66:
    v_stack_m130 = 1;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) >> (1);
    result = (unsigned int)((result) & (31));
    v_stack_mF8 = result;
    v_stack_m140 = (unsigned int)(result);
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 32);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) & (-64);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8) = result;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 64) + 8)) & (1));
    v_stack_mF0 = a1;
    v_stack_m13C = (unsigned int)(a1);
    goto loc_008A7780;
loc_008A7CBB:
    if (a1 == 2) goto loc_008A7E2B;
    v_stack_m170 = (unsigned __int16)((unsigned int)(v_stack_m178));
    v_stack_m154 = 0x8000ULL;
loc_008A7CDC:
    v_stack_m16C = 44;
loc_008A7CE0:
    if (v_stack_m138 == 0) goto loc_008A7DE1;
    result = (unsigned int)(0x601802ULL);
    if ((unsigned int)(44 - 41) != 0) {
        result = (unsigned int)(44 - 41);
        result = (unsigned int)((result) | (0x601800ULL));
    }
    v_stack_m60 = *(unsigned __int64 *)(v_stack_m28 + 64);
    v_stack_m58 = 44;
    v_stack_m54 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_m198 = (unsigned int)(result);
    v_stack_m1A0 = (unsigned __int16)(v_stack_m170);
    result = EtwpLogKernelEvent(v_stack_m60, *(unsigned __int64 *)(v_stack_m118 + 1360), (unsigned int)(*(unsigned int *)(v_stack_m118)), 1);
    v_rbx = (*(unsigned __int64 *)(v_stack_m28 + 64)) + (48);
    goto loc_008A773B;
loc_008A7D56:
    result = ExAllocatePool2(64, (unsigned int)(0x2000ULL), (unsigned int)(0x66726550ULL), 1);
    v_stack_m148 = 611;
    v_stack_m15C = 611;
    v_stack_m118 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m14C = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_m164 = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_008A76C8;
loc_008A7DAB:
    goto loc_008A7CE0;
loc_008A7DB4:
    goto loc_008A7C2F;
loc_008A7DBC:
    if (*(unsigned __int64 *)(v_stack_m28 + 72) == 0) goto loc_008A7C38;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)(0x66726550ULL), v_stack_m120);
    goto loc_008A7C38;
loc_008A7DD4:
    goto loc_008A7BA4;
loc_008A7DE1:
    if ((unsigned int)((unsigned int)(v_stack_m12C)) != 0) goto loc_008A7E92;
loc_008A7DEF:
    v_stack_m50 = v_rbx;
    v_stack_m48 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_m44 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_stack_m1A0 = (unsigned int)((unsigned int)(0x601902ULL));
    result = EtwTraceKernelEvent(v_stack_m50, 1, (unsigned int)(v_stack_m154), v_stack_m170);
    goto loc_008A7BBC;
loc_008A7E2B:
    v_stack_m170 = (unsigned __int16)((unsigned int)(v_stack_m148));
    v_stack_m154 = 0x20008000ULL;
    if (v_stack_m138 != 0) goto loc_008A7E88;
    v_stack_m16C = 24;
    *(unsigned int *)(v_rbx + 20) = 0x8000ULL;
    goto loc_008A7CE0;
loc_008A7E59:
    v_stack_m168 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_008A7618;
loc_008A7E64:
    result = 0;
    goto loc_008A7631;
loc_008A7E6B:
    goto loc_008A77EF;
loc_008A7E72:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)))) & (0xFFFFFFFEULL));
    v_stack_m168 = (unsigned int)(v_rdi);
    v_stack_m158 = (unsigned int)(v_rdi);
    if (condition_is_equal) goto loc_008A7C2F;
    goto loc_008A76EC;
loc_008A7E88:
    goto loc_008A7CDC;
loc_008A7E92:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m12C)))) | (0x601900ULL));
    goto loc_008A7DEF;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEnumerateAddressSpace(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m13C;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint32_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint16_t v_stack_m184;
    uint16_t v_stack_m188;
    uint16_t v_stack_m18C;
    uint32_t v_stack_m190;
    uint32_t v_stack_m194;
    uint16_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint16_t v_stack_mAA;
    uint8_t v_stack_mAB;
    uint8_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0x56318F)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m138 = Arg2;
    v_stack_m148 = Arg1;
    v_stack_mE8 = Arg1;
    v_stack_mE0 = Arg2;
    local_rsi = 0;
    v_stack_m194 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m128 = 0;
    if (Arg3 == 0) goto loc_008A7E59;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3)))) & (4)) == 0) goto loc_008A7E59;
    v_stack_m190 = 1;
loc_008A7618:
    if (Arg3 == 0) goto loc_008A7E64;
    if (((*(uint32_t *)(Arg3 + 0x4)) & (0x8000ULL)) == 0) goto loc_008A7E64;
loc_008A7631:
    v_stack_m180 = 1;
    local_rdi = 1;
    if (1 != 0) {
        local_rdi = (uint32_t)((1) | (4));
        v_stack_m190 = (uint32_t)(local_rdi);
        v_stack_m180 = (uint32_t)(local_rdi);
    }
    if (Arg2 == NULL) goto loc_008A7662;
    if (Arg3 == 0) goto loc_008A7662;
    if (((*(uint32_t *)(Arg3)) & (0x8000ULL)) != 0) {
        local_rdi = (uint32_t)((local_rdi) | (2));
        v_stack_m190 = (uint32_t)(local_rdi);
        v_stack_m180 = (uint32_t)(local_rdi);
    }
    if ((uint32_t)(local_rdi) == 0) goto loc_008A7DB4;
    if (Arg2 == NULL) goto loc_008A7D56;
    v_stack_m140 = *(uint64_t *)(arg2 + 0x20);
    v_stack_m108 = *(uint64_t *)(arg2 + 0x20);
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(arg2 + 0x40))));
    Arg2 = (uint16_t)((*(uint64_t *)(arg2 + 0x20)) + (0x1404ULL));
    v_stack_m174 = (uint32_t)(Arg2);
    v_stack_m18C = (uint16_t)(Arg2);
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(arg2 + 0x40))));
    local_r12 = (uint16_t)((local_r12) + (0x428ULL));
    Arg1 = (uint8_t)(-(*(uint8_t *)(arg2 + 0x40)));
    Arg1 = (uint16_t)((Arg1) + (641));
    v_stack_m170 = (uint32_t)(Arg1);
    v_stack_m184 = (uint16_t)(Arg1);
loc_008A76C8:
    v_stack_m188 = (uint16_t)(local_r12);
    v_stack_m178 = (uint32_t)(local_r12);
    v_stack_m110 = *(uint64_t *)(arg2 + 0x10);
    v_stack_m150 = *(uint64_t *)(arg2 + 0x10);
    if (*(uint64_t *)(arg2 + 0x10) == 0) goto loc_008A7E72;
loc_008A76EC:
    v_stack_m120 = 0;
    v_stack_m168 = 0;
    v_stack_m118 = 0;
    v_stack_m164 = 0;
    v_stack_mF8 = 0;
    v_stack_m198 = 0;
    v_stack_m17C = 0;
    result = MmEnumerateAddressSpaceAndReferenceImages(Arg1, (uint32_t)((uint32_t)(local_rdi)), Arg3, Arg1);
    v_stack_mD8 = result;
    if (result == 0) goto loc_008A7C2F;
loc_008A773B:
    v_stack_mF0 = result;
    if (*(uint64_t *)(result) == 0) goto loc_008A7C20;
    Arg1 = (uint32_t)((*(uint64_t *)(result)) & (3));
    result = (*(uint64_t *)(result)) & (-4);
    *(uint64_t *)(result) = result;
    v_stack_m154 = 0;
    if (Arg1 != 0) goto loc_008A7CBB;
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_008A7C66;
    v_stack_m158 = 0;
loc_008A7780:
    local_r12 = (*(uint64_t *)(result + 0x8)) >> (6);
    local_r12 = (uint32_t)((local_r12) & (15));
    v_stack_m130 = (uint32_t)(local_r12);
    local_r13 = (*(uint64_t *)(result + 0x8)) >> (10);
    local_r13 = (uint32_t)((local_r13) & (7));
    v_stack_m12C = (uint32_t)(local_r13);
    result = (*(uint64_t *)(result + 0x8)) & (0xFFFFFFFFFFFFE03FULL);
    *(uint64_t *)(result + 0x8) = result;
    v_stack_m128 = 0;
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_008A77E2;
    result = KeAreInterruptsEnabled(Arg1, (uint32_t)((uint32_t)(local_rdi)), Arg3, Arg1);
    if ((uint8_t)(result) == 0) goto loc_008A77E2;
    result = 0;
    if (((uint8_t)(v_cr8)) >= 1) {
        result = 1;
    }
    if ((uint32_t)(result) != 0) goto loc_008A7E6B;
loc_008A77EF:
    if (*(uint64_t *)(v_rip + 0x5BE3F7) == 0) goto loc_008A7821;
    result = guard_dispatch_icall(*(uint64_t *)(result), (uint32_t)(0x400ULL), *(uint64_t *)(arg2 + 0x10), v_stack_m128);
    v_stack_m16C = (uint32_t)(result);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (sign_flag) {
        Arg1 = *(uint64_t *)(result);
        v_stack_m1C8 = 0;
        a4 = v_stack_m194;
        Arg3 = 0x2000ULL;
        Arg2 = *(uint64_t *)(arg2 + 0x10);
        result = ObQueryNameStringMode(Arg1, Arg2, Arg3, a4);
        local_rdi = (uint32_t)(result);
        v_stack_m16C = (uint32_t)(result);
    }
    v_stack_m15C = 0;
    v_stack_m160 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    v_stack_m100 = *(uint64_t *)(result + 0x10);
    result = RtlImageNtHeader(*(uint64_t *)(result + 0x8), Arg2, Arg3, a4);
    local_r14 = (uint32_t)(*(uint32_t *)(result + 0x28));
    local_r15 = *(uint64_t *)(result + 0x10);
    if (result != 0) {
        local_r14 = *(uint32_t *)(result + 0x58);
        v_stack_m160 = (uint32_t)(local_r14);
        local_rsi = *(uint32_t *)(result + 0x8);
        v_stack_m15C = (uint32_t)(local_rsi);
        local_r15 = *(uint64_t *)(result + 0x30);
        v_stack_m100 = local_r15;
    }
    result = 0;
    goto loc_008A7956;
loc_008A7956:
    if (sign_flag) goto loc_008A7BCE;
    if (v_stack_m138 == 0) goto loc_008A7BDD;
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, Arg2 + 64, a4);
    if (v_stack_m150 == 0) goto loc_008A7BD6;
    if ((uint16_t)(*(uint16_t *)(v_stack_m150)) == 0) goto loc_008A7BD6;
    local_rsi = 0;
    if (*(uint64_t *)(v_stack_m150 + 0x8) != 0) {
        result = v_stack_m148;
        result = *(uint32_t *)(result + 0x1D0);
        v_stack_mB8 = (uint32_t)(result);
        result = *(uint64_t *)(result + 0x8);
        v_stack_mC8 = result;
        result = *(uint64_t *)(result + 0x18);
        v_stack_mC0 = result;
        result = *(uint32_t *)(result + 0x28);
        v_stack_mB4 = (uint32_t)(result);
        v_stack_mB0 = 0;
        v_stack_mAC = (uint8_t)(local_r12);
        v_stack_mAB = (uint8_t)(local_r13);
        result = *(uint64_t *)(result + 0x10);
        v_stack_mA8 = result;
        v_stack_mAA = 0;
        v_stack_mA0 = 0;
        v_stack_m98 = 0;
        result = v_stack_mC8;
        v_stack_m68 = result;
        v_stack_m60 = 56;
        v_stack_m58 = *(uint64_t *)(v_stack_m150 + 0x8);
        v_stack_m50 = (uint32_t)(*(uint16_t *)(v_stack_m150));
        v_stack_m4C = 0;
        result = v_rip - 9008242;
        v_stack_m48 = result;
        v_stack_m40 = 2;
        v_stack_m1C0 = 0x501803ULL;
        result = v_stack_m174;
        v_stack_m1C8 = (uint16_t)(result);
        a4 = local_rsi + 3;
        result = v_stack_m140;
        Arg3 = *(uint32_t *)(result);
        Arg2 = *(uint64_t *)(result + 0x550);
        Arg1 = v_stack_m68;
        result = EtwpLogKernelEvent(Arg1, Arg2, Arg3, a4);
    }
    if (v_stack_m128 != 0) {
        result = *(uint64_t *)(v_rip + 0x5BE142);
        result = *(uint64_t *)(result + 0x20);
        result = guard_dispatch_icall(v_stack_m128, Arg2, Arg3, a4);
    }
    if ((uint32_t)((uint32_t)(v_stack_m158)) == 0) goto loc_008A7DD4;
    v_stack_m48 = v_xmm0;
    *(uint64_t *)(result) = v_xmm1;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm1;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x1D0)));
    *(uint64_t *)(result + 0x8) = *(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x1D0)) + 0x18);
    *(uint64_t *)(result) = v_xmm2;
    *(uint64_t *)(result + 0x18) = v_xmm3;
    *(uint64_t *)(result + 0x20) = v_stack_mF8;
    Arg3 = ((uint32_t)(v_stack_m120)) << (48);
    result = ((uint32_t)(v_stack_m118)) << (53);
    Arg2 = (Arg3) ^ (*(uint64_t *)(result + 0x10));
    Arg2 = (Arg2) & (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x1D0)) + 0x18));
    result = (result) & (*(uint64_t *)((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x1D0)) + 0x18));
    Arg2 = (Arg2) ^ (result);
    Arg3 = (Arg3) & (result);
    Arg2 = (Arg2) ^ (Arg3);
    Arg2 = (Arg2) | (result);
    *(void **)(result + 0x10) = Arg2;
    v_stack_m198 = (uint16_t)((uint32_t)(v_stack_m178));
    v_stack_m17C = 0x8000ULL;
    v_stack_m194 = 44;
loc_008A7BA4:
    result = ObfDereferenceObject(*(uint64_t *)(result), Arg2, Arg3, *(uint64_t *)(result));
    if ((uint32_t)((uint32_t)(v_stack_m158)) != 0) goto loc_008A7DAB;
loc_008A7BBC:
    local_rbx = (result) + (48);
    goto loc_008A773B;
loc_008A7BCE:
loc_008A7BD6:
    local_rsi = 0;
    goto loc_008A7A9A;
loc_008A7BDD:
    v_stack_m1A0 = (uint32_t)(result);
    v_stack_m1A8 = v_stack_m150;
    v_stack_m1B0 = (uint32_t)(v_stack_m138);
    v_stack_m1B8 = (uint32_t)((uint32_t)(v_stack_m178));
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 3;
    result = EtwpTraceImageUnload(v_stack_m150, v_stack_m148, *(uint64_t *)(local_rbx + 0x8), *(uint64_t *)(local_rbx + 0x18));
    local_rsi = 0;
    goto loc_008A7A9A;
loc_008A7C20:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mD8, Arg2, *(uint64_t *)(local_rbx + 0x8), *(uint64_t *)(local_rbx + 0x18));
loc_008A7C2F:
    if (v_stack_m138 == 0) goto loc_008A7DBC;
loc_008A7C38:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(local_rbx + 0x8), *(uint64_t *)(local_rbx + 0x18));
    return result;
loc_008A7C66:
    v_stack_m130 = 1;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) >> (1);
    result = (uint32_t)((result) & (31));
    v_stack_mF8 = result;
    v_stack_m140 = (uint32_t)(result);
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x20);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) & (-64);
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8) = result;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x40) + 0x8)) & (1));
    v_stack_mF0 = Arg1;
    v_stack_m13C = (uint32_t)(Arg1);
    goto loc_008A7780;
loc_008A7CBB:
    if (Arg1 == 2) goto loc_008A7E2B;
    v_stack_m170 = (uint16_t)((uint32_t)(v_stack_m178));
    v_stack_m154 = 0x8000ULL;
loc_008A7CDC:
    v_stack_m16C = 44;
loc_008A7CE0:
    if (v_stack_m138 == 0) goto loc_008A7DE1;
    result = (uint32_t)(0x601802ULL);
    if ((uint32_t)(44 - 41) != 0) {
        result = (uint32_t)(44 - 41);
        result = (uint32_t)((result) | (0x601800ULL));
    }
    v_stack_m60 = *(uint64_t *)(v_stack_m28 + 0x40);
    v_stack_m58 = 44;
    v_stack_m54 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_m198 = (uint32_t)(result);
    v_stack_m1A0 = (uint16_t)(v_stack_m170);
    result = EtwpLogKernelEvent(v_stack_m60, *(uint64_t *)(v_stack_m118 + 0x550), (uint32_t)(*(uint32_t *)(v_stack_m118)), 1);
    local_rbx = (*(uint64_t *)(v_stack_m28 + 0x40)) + (48);
    goto loc_008A773B;
loc_008A7D56:
    result = ExAllocatePool2(64, (uint32_t)(0x2000ULL), (uint32_t)(0x66726550ULL), 1);
    v_stack_m148 = 611;
    v_stack_m15C = 611;
    v_stack_m118 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_mE0 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m14C = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_m164 = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_008A76C8;
loc_008A7DAB:
    goto loc_008A7CE0;
loc_008A7DB4:
    goto loc_008A7C2F;
loc_008A7DBC:
    if (*(uint64_t *)(v_stack_m28 + 0x48) == 0) goto loc_008A7C38;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)(0x66726550ULL), v_stack_m120);
    goto loc_008A7C38;
loc_008A7DD4:
    goto loc_008A7BA4;
loc_008A7DE1:
    if ((uint32_t)((uint32_t)(v_stack_m12C)) != 0) goto loc_008A7E92;
loc_008A7DEF:
    v_stack_m50 = local_rbx;
    v_stack_m48 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_m44 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    v_stack_m1A0 = (uint32_t)((uint32_t)(0x601902ULL));
    result = EtwTraceKernelEvent(v_stack_m50, 1, (uint32_t)(v_stack_m154), v_stack_m170);
    goto loc_008A7BBC;
loc_008A7E2B:
    v_stack_m170 = (uint16_t)((uint32_t)(v_stack_m148));
    v_stack_m154 = 0x20008000ULL;
    if (v_stack_m138 != 0) goto loc_008A7E88;
    v_stack_m16C = 24;
    *(uint32_t *)(local_rbx + 0x14) = 0x8000ULL;
    goto loc_008A7CE0;
loc_008A7E59:
    v_stack_m168 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_008A7618;
loc_008A7E64:
    result = 0;
    goto loc_008A7631;
loc_008A7E6B:
    goto loc_008A77EF;
loc_008A7E72:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) & (0xFFFFFFFEULL));
    v_stack_m168 = (uint32_t)(local_rdi);
    v_stack_m158 = (uint32_t)(local_rdi);
    if (condition_is_equal) goto loc_008A7C2F;
    goto loc_008A76EC;
loc_008A7E88:
    goto loc_008A7CDC;
loc_008A7E92:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m12C)))) | (0x601900ULL));
    goto loc_008A7DEF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A7590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
