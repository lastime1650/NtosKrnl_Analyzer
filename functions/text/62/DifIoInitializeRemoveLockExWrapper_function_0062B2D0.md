# DifIoInitializeRemoveLockExWrapper

- RVA: `0x0062B2D0`–`0x0062B461` (길이 `401` bytes)
- VA: `0x000000014062B2D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3AF8`
- 디코드: `111`개 명령, `401/401` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062B308` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062B330` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062B378` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062B39F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062B3B8` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062B3D4` → [IoInitializeRemoveLockEx](../4C/IoInitializeRemoveLockEx_function_004C8F10.md) (function, `0x004C8F10`)
- `0x0062B3FD` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062B424` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062B43D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062B344` → RVA `0x00F048B8` (`.data`; read)
- `0x0062B365` → RVA `0x00F04980` (`.data`; read)
- `0x0062B371` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062B2D0  48 8B C4                        mov rax, rsp
0062B2D3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062B2D7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062B2DB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062B2DF  57                              push rdi
0062B2E0  41 54                           push r12
0062B2E2  41 55                           push r13
0062B2E4  41 56                           push r14
0062B2E6  41 57                           push r15
0062B2E8  48 83 EC 50                     sub rsp, 0x50
0062B2EC  0F 57 C0                        xorps xmm0, xmm0
0062B2EF  4C 8B E9                        mov r13, rcx
0062B2F2  B9 4A 01 00 00                  mov ecx, 0x14a
0062B2F7  45 8B F1                        mov r14d, r9d
0062B2FA  0F 11 40 B8                     movups xmmword ptr [rax - 0x48], xmm0
0062B2FE  45 8B F8                        mov r15d, r8d
0062B301  44 8B E2                        mov r12d, edx
0062B304  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062B308  E8 27 A7 E6 FF                  call 0x140495a34
0062B30D  48 8B F0                        mov rsi, rax
0062B310  48 85 C0                        test rax, rax
0062B313  0F 84 A4 00 00 00               je 0x14062b3bd
0062B319  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062B31C  A8 18                           test al, 0x18
0062B31E  74 0C                           je 0x14062b32c
0062B320  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0062B325  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0062B32A  EB 0E                           jmp 0x14062b33a
0062B32C  A8 04                           test al, 4
0062B32E  74 0A                           je 0x14062b33a
0062B330  E8 D3 88 EA FF                  call 0x1404d3c08
0062B335  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0062B33A  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
0062B341  40 32 ED                        xor bpl, bpl
0062B344  40 38 2D 6D 95 8D 00            cmp byte ptr [rip + 0x8d956d], bpl
0062B34B  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
0062B350  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
0062B355  44 89 7C 24 40                  mov dword ptr [rsp + 0x40], r15d
0062B35A  44 89 74 24 3C                  mov dword ptr [rsp + 0x3c], r14d
0062B35F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0062B363  75 0C                           jne 0x14062b371
0062B365  F7 05 11 96 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9611], 0x800
0062B36F  74 13                           je 0x14062b384
0062B371  48 8D 0D 08 8B 8D 00            lea rcx, [rip + 0x8d8b08]
0062B378  E8 A3 B2 BE FF                  call 0x140216620
0062B37D  40 8A E8                        mov bpl, al
0062B380  84 C0                           test al, al
0062B382  74 39                           je 0x14062b3bd
0062B384  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062B388  48 8B 1F                        mov rbx, qword ptr [rdi]
0062B38B  EB 1A                           jmp 0x14062b3a7
0062B38D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062B391  48 85 C0                        test rax, rax
0062B394  74 0E                           je 0x14062b3a4
0062B396  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062B39A  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0062B39F  E8 2C F7 08 00                  call 0x1406baad0
0062B3A4  48 8B 1B                        mov rbx, qword ptr [rbx]
0062B3A7  48 3B DF                        cmp rbx, rdi
0062B3AA  75 E1                           jne 0x14062b38d
0062B3AC  40 84 ED                        test bpl, bpl
0062B3AF  74 0C                           je 0x14062b3bd
0062B3B1  48 8D 0D C8 8A 8D 00            lea rcx, [rip + 0x8d8ac8]
0062B3B8  E8 C3 EA D1 FF                  call 0x140349e80
0062B3BD  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
0062B3C4  45 8B CE                        mov r9d, r14d
0062B3C7  45 8B C7                        mov r8d, r15d
0062B3CA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0062B3CE  41 8B D4                        mov edx, r12d
0062B3D1  49 8B CD                        mov rcx, r13
0062B3D4  E8 37 DB E9 FF                  call 0x1404c8f10
0062B3D9  48 85 F6                        test rsi, rsi
0062B3DC  74 64                           je 0x14062b442
0062B3DE  40 32 FF                        xor dil, dil
0062B3E1  40 38 3D D0 94 8D 00            cmp byte ptr [rip + 0x8d94d0], dil
0062B3E8  75 0C                           jne 0x14062b3f6
0062B3EA  F7 05 8C 95 8D 00 00 08 00 00   test dword ptr [rip + 0x8d958c], 0x800
0062B3F4  74 13                           je 0x14062b409
0062B3F6  48 8D 0D 83 8A 8D 00            lea rcx, [rip + 0x8d8a83]
0062B3FD  E8 1E B2 BE FF                  call 0x140216620
0062B402  40 8A F8                        mov dil, al
0062B405  84 C0                           test al, al
0062B407  74 39                           je 0x14062b442
0062B409  48 83 C6 30                     add rsi, 0x30
0062B40D  48 8B 1E                        mov rbx, qword ptr [rsi]
0062B410  EB 1A                           jmp 0x14062b42c
0062B412  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062B416  48 85 C0                        test rax, rax
0062B419  74 0E                           je 0x14062b429
0062B41B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062B41F  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0062B424  E8 A7 F6 08 00                  call 0x1406baad0
0062B429  48 8B 1B                        mov rbx, qword ptr [rbx]
0062B42C  48 3B DE                        cmp rbx, rsi
0062B42F  75 E1                           jne 0x14062b412
0062B431  40 84 FF                        test dil, dil
0062B434  74 0C                           je 0x14062b442
0062B436  48 8D 0D 43 8A 8D 00            lea rcx, [rip + 0x8d8a43]
0062B43D  E8 3E EA D1 FF                  call 0x140349e80
0062B442  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062B447  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0062B44B  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
0062B44F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062B453  49 8B E3                        mov rsp, r11
0062B456  41 5F                           pop r15
0062B458  41 5E                           pop r14
0062B45A  41 5D                           pop r13
0062B45C  41 5C                           pop r12
0062B45E  5F                              pop rdi
0062B45F  C3                              ret
0062B460  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoInitializeRemoveLockExWrapper(__int64 a1, int a2, int a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    result = DifGetAPIThunkContextById(330, a2, a3, a4);
    if (result == 0) goto loc_0062B3BD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062B32C;
    v_stack_m48 = v_stack_p0;
    goto loc_0062B33A;
loc_0062B32C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m48 = result;
    }
    v_rbp = 0;
    v_stack_m30 = a1;
    v_stack_m34 = (unsigned int)((unsigned int)(a2));
    v_stack_m38 = (unsigned int)((unsigned int)(a3));
    v_stack_m3C = (unsigned int)((unsigned int)(a4));
    v_stack_m40 = (unsigned int)((unsigned int)(a5));
    if ((*(unsigned __int8 *)(v_rip + 9278829)) != 0) goto loc_0062B371;
    if (((*(unsigned int *)(v_rip + 9278993)) & (0x800ULL)) == 0) goto loc_0062B384;
loc_0062B371:
    result = ExAcquireRundownProtection(v_rip + 9276168, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062B3BD;
loc_0062B384:
    goto loc_0062B3A7;
loc_0062B38D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062B3A7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062B38D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9276104;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    result = IoInitializeRemoveLockEx(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (result == 0) goto loc_0062B442;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9278672)) != 0) goto loc_0062B3F6;
    if (((*(unsigned int *)(v_rip + 9278860)) & (0x800ULL)) == 0) goto loc_0062B409;
loc_0062B3F6:
    result = ExAcquireRundownProtection(v_rip + 9276035, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0062B442;
loc_0062B409:
    v_rsi = (result) + (48);
    goto loc_0062B42C;
loc_0062B412:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0062B42C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062B412;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9275971;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoInitializeRemoveLockExWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;
    uint64_t v_stack_p0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    result = DifGetAPIThunkContextById(330, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062B3BD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062B32C;
    v_stack_m48 = v_stack_p0;
    goto loc_0062B33A;
loc_0062B32C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m48 = result;
    }
    local_rbp = 0;
    v_stack_m30 = Arg1;
    v_stack_m34 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m38 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m3C = (uint32_t)((uint32_t)(Arg4));
    v_stack_m40 = (uint32_t)((uint32_t)(Arg5));
    if ((*(uint8_t *)(v_rip + 0x8D956D)) != 0) goto loc_0062B371;
    if (((*(uint32_t *)(v_rip + 0x8D9611)) & (0x800ULL)) == 0) goto loc_0062B384;
loc_0062B371:
    result = ExAcquireRundownProtection(v_rip + 9276168, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062B3BD;
loc_0062B384:
    goto loc_0062B3A7;
loc_0062B38D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062B3A7:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062B38D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9276104;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    result = IoInitializeRemoveLockEx(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (result == 0) goto loc_0062B442;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D94D0)) != 0) goto loc_0062B3F6;
    if (((*(uint32_t *)(v_rip + 0x8D958C)) & (0x800ULL)) == 0) goto loc_0062B409;
loc_0062B3F6:
    result = ExAcquireRundownProtection(v_rip + 9276035, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0062B442;
loc_0062B409:
    local_rsi = (result) + (48);
    goto loc_0062B42C;
loc_0062B412:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0062B42C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062B412;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9275971;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062B2D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062B2D0[BB_0062B2D0]
  bb_0062B319[BB_0062B319]
  bb_0062B320[BB_0062B320]
  bb_0062B32C[BB_0062B32C]
  bb_0062B330[BB_0062B330]
  bb_0062B33A[BB_0062B33A]
  bb_0062B365[BB_0062B365]
  bb_0062B371[BB_0062B371]
  bb_0062B384[BB_0062B384]
  bb_0062B38D[BB_0062B38D]
  bb_0062B396[BB_0062B396]
  bb_0062B3A4[BB_0062B3A4]
  bb_0062B3A7[BB_0062B3A7]
  bb_0062B3AC[BB_0062B3AC]
  bb_0062B3B1[BB_0062B3B1]
  bb_0062B3BD[BB_0062B3BD]
  bb_0062B3DE[BB_0062B3DE]
  bb_0062B3EA[BB_0062B3EA]
  bb_0062B3F6[BB_0062B3F6]
  bb_0062B409[BB_0062B409]
  bb_0062B412[BB_0062B412]
  bb_0062B41B[BB_0062B41B]
  bb_0062B429[BB_0062B429]
  bb_0062B42C[BB_0062B42C]
  bb_0062B431[BB_0062B431]
  bb_0062B436[BB_0062B436]
  bb_0062B442[BB_0062B442]
  bb_0062B460[BB_0062B460]
  bb_0062B2D0 -->|branch| bb_0062B3BD
  bb_0062B2D0 -->|fallthrough| bb_0062B319
  bb_0062B319 -->|branch| bb_0062B32C
  bb_0062B319 -->|fallthrough| bb_0062B320
  bb_0062B320 -->|branch| bb_0062B33A
  bb_0062B32C -->|branch| bb_0062B33A
  bb_0062B32C -->|fallthrough| bb_0062B330
  bb_0062B330 -->|flow| bb_0062B33A
  bb_0062B33A -->|branch| bb_0062B371
  bb_0062B33A -->|fallthrough| bb_0062B365
  bb_0062B365 -->|branch| bb_0062B384
  bb_0062B365 -->|fallthrough| bb_0062B371
  bb_0062B371 -->|branch| bb_0062B3BD
  bb_0062B371 -->|fallthrough| bb_0062B384
  bb_0062B384 -->|branch| bb_0062B3A7
  bb_0062B38D -->|branch| bb_0062B3A4
  bb_0062B38D -->|fallthrough| bb_0062B396
  bb_0062B396 -->|flow| bb_0062B3A4
  bb_0062B3A4 -->|flow| bb_0062B3A7
  bb_0062B3A7 -->|branch| bb_0062B38D
  bb_0062B3A7 -->|fallthrough| bb_0062B3AC
  bb_0062B3AC -->|branch| bb_0062B3BD
  bb_0062B3AC -->|fallthrough| bb_0062B3B1
  bb_0062B3B1 -->|flow| bb_0062B3BD
  bb_0062B3BD -->|branch| bb_0062B442
  bb_0062B3BD -->|fallthrough| bb_0062B3DE
  bb_0062B3DE -->|branch| bb_0062B3F6
  bb_0062B3DE -->|fallthrough| bb_0062B3EA
  bb_0062B3EA -->|branch| bb_0062B409
  bb_0062B3EA -->|fallthrough| bb_0062B3F6
  bb_0062B3F6 -->|branch| bb_0062B442
  bb_0062B3F6 -->|fallthrough| bb_0062B409
  bb_0062B409 -->|branch| bb_0062B42C
  bb_0062B412 -->|branch| bb_0062B429
  bb_0062B412 -->|fallthrough| bb_0062B41B
  bb_0062B41B -->|flow| bb_0062B429
  bb_0062B429 -->|flow| bb_0062B42C
  bb_0062B42C -->|branch| bb_0062B412
  bb_0062B42C -->|fallthrough| bb_0062B431
  bb_0062B431 -->|branch| bb_0062B442
  bb_0062B431 -->|fallthrough| bb_0062B436
  bb_0062B436 -->|flow| bb_0062B442
```
