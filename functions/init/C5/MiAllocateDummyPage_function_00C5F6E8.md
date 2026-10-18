# MiAllocateDummyPage

- RVA: `0x00C5F6E8`–`0x00C5F860` (길이 `376` bytes)
- VA: `0x0000000140C5F6E8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000717F8`
- 디코드: `99`개 명령, `376/376` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C5F713` → [MiAcquireNonPagedResources](../../text/28/MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x00C5F725` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x00C5F767` → [MiGetPage](../../text/28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x00C5F778` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5F79B` → [MiSetPfnTbFlushStamp](../../text/2B/MiSetPfnTbFlushStamp_function_002B7A70.md) (function, `0x002B7A70`)
- `0x00C5F7B1` → [MiLockPageInline](../../text/31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00C5F7BD` → [MiMakeDemandZeroPte](../../text/33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00C5F83D` → [MiSetPfnContainingFrame](../../text/36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x00C5F847` → [MiUnlockPage](../../text/31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiInitSystem](MiInitSystem_function_00C5E6C0.md) at `0x00C5E9F9`
- [MiInitializeDummyPages](../C6/MiInitializeDummyPages_function_00C605CC.md) at `0x00C6060A`

### Static image references
- `0x00C5F6FC` → RVA `0x00E38D00` (`.data`; read)
- `0x00C5F73B` → RVA `0x00E2DCC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00C5F713` → [MiAcquireNonPagedResources](../../text/28/MiAcquireNonPagedResources_function_00286C60.md) (`INIT` → `.text`)
  - `0x00C5F725` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (`INIT` → `.text`)
  - `0x00C5F767` → [MiGetPage](../../text/28/MiGetPage_function_002884C0.md) (`INIT` → `.text`)
  - `0x00C5F778` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5F79B` → [MiSetPfnTbFlushStamp](../../text/2B/MiSetPfnTbFlushStamp_function_002B7A70.md) (`INIT` → `.text`)
  - `0x00C5F7B1` → [MiLockPageInline](../../text/31/MiLockPageInline_function_0031A340.md) (`INIT` → `.text`)
  - `0x00C5F7BD` → [MiMakeDemandZeroPte](../../text/33/MiMakeDemandZeroPte_function_00337A00.md) (`INIT` → `.text`)
  - `0x00C5F83D` → [MiSetPfnContainingFrame](../../text/36/MiSetPfnContainingFrame_function_00363FC0.md) (`INIT` → `.text`)
  - `0x00C5F847` → [MiUnlockPage](../../text/31/MiUnlockPage_function_0031A3E0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5F6E8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C5F6ED  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C5F6F2  57                              push rdi
00C5F6F3  48 83 EC 30                     sub rsp, 0x30
00C5F6F7  BB 01 00 00 00                  mov ebx, 1
00C5F6FC  48 8D 0D FD 95 1D 00            lea rcx, [rip + 0x1d95fd]
00C5F703  0F 57 C0                        xorps xmm0, xmm0
00C5F706  44 8B CB                        mov r9d, ebx
00C5F709  8B D3                           mov edx, ebx
00C5F70B  45 33 C0                        xor r8d, r8d
00C5F70E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00C5F713  E8 48 75 62 FF                  call 0x140286c60
00C5F718  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00C5F71D  45 33 C0                        xor r8d, r8d
00C5F720  8D 53 02                        lea edx, [rbx + 2]
00C5F723  33 C9                           xor ecx, ecx
00C5F725  E8 E6 0C 6C FF                  call 0x140320410
00C5F72A  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
00C5F72F  8B C3                           mov eax, ebx
00C5F731  F0 41 0F C1 01                  lock xadd dword ptr [r9], eax
00C5F736  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
00C5F73B  4C 8D 15 7E E5 1C 00            lea r10, [rip + 0x1ce57e]
00C5F742  33 D2                           xor edx, edx
00C5F744  48 8D 0D B5 95 1D 00            lea rcx, [rip + 0x1d95b5]
00C5F74B  4D 8B C1                        mov r8, r9
00C5F74E  49 C1 E8 10                     shr r8, 0x10
00C5F752  41 83 E0 03                     and r8d, 3
00C5F756  43 F7 34 82                     div dword ptr [r10 + r8*4]
00C5F75A  44 8D 43 7F                     lea r8d, [rbx + 0x7f]
00C5F75E  41 33 D1                        xor edx, r9d
00C5F761  0F B6 D2                        movzx edx, dl
00C5F764  41 33 D1                        xor edx, r9d
00C5F767  E8 54 8D 62 FF                  call 0x1402884c0
00C5F76C  48 8B F0                        mov rsi, rax
00C5F76F  48 83 F8 FF                     cmp rax, -1
00C5F773  75 09                           jne 0x140c5f77e
00C5F775  8D 4B 01                        lea ecx, [rbx + 1]
00C5F778  E8 87 22 A1 FF                  call 0x140671a04
00C5F77D  CC                              int3
00C5F77E  48 8D 3C 40                     lea rdi, [rax + rax*2]
00C5F782  48 C1 E7 04                     shl rdi, 4
00C5F786  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00C5F790  48 03 F8                        add rdi, rax
00C5F793  45 33 C0                        xor r8d, r8d
00C5F796  48 8B CF                        mov rcx, rdi
00C5F799  33 D2                           xor edx, edx
00C5F79B  E8 D0 82 65 FF                  call 0x1402b7a70
00C5F7A0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00C5F7AA  48 8B CF                        mov rcx, rdi
00C5F7AD  48 89 47 08                     mov qword ptr [rdi + 8], rax
00C5F7B1  E8 8A AB 6B FF                  call 0x14031a340
00C5F7B6  B9 04 00 00 00                  mov ecx, 4
00C5F7BB  8A D8                           mov bl, al
00C5F7BD  E8 3E 82 6D FF                  call 0x140337a00
00C5F7C2  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00C5F7C6  33 D2                           xor edx, edx
00C5F7C8  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00C5F7CB  B8 02 00 00 00                  mov eax, 2
00C5F7D0  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00C5F7D4  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00C5F7D9  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00C5F7DD  89 4F 20                        mov dword ptr [rdi + 0x20], ecx
00C5F7E0  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00C5F7EA  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00C5F7ED  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C5F7F1  C1 E8 10                        shr eax, 0x10
00C5F7F4  0C 07                           or al, 7
00C5F7F6  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00C5F7FA  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00C5F7FE  89 47 20                        mov dword ptr [rdi + 0x20], eax
00C5F801  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00C5F804  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C5F808  C1 E8 10                        shr eax, 0x10
00C5F80B  0C 20                           or al, 0x20
00C5F80D  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00C5F811  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00C5F815  89 47 20                        mov dword ptr [rdi + 0x20], eax
00C5F818  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00C5F81B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C5F81F  C1 E8 10                        shr eax, 0x10
00C5F822  0C 08                           or al, 8
00C5F824  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00C5F828  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00C5F82C  89 47 20                        mov dword ptr [rdi + 0x20], eax
00C5F82F  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00C5F833  48 23 C1                        and rax, rcx
00C5F836  48 8B CF                        mov rcx, rdi
00C5F839  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00C5F83D  E8 7E 47 70 FF                  call 0x140363fc0
00C5F842  8A D3                           mov dl, bl
00C5F844  48 8B CF                        mov rcx, rdi
00C5F847  E8 94 AB 6B FF                  call 0x14031a3e0
00C5F84C  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00C5F851  48 8B C6                        mov rax, rsi
00C5F854  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00C5F859  48 83 C4 30                     add rsp, 0x30
00C5F85D  5F                              pop rdi
00C5F85E  C3                              ret
00C5F85F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateDummyPage(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pA;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a3 = 0;
    v_stack_m18 = v_xmm0;
    result = MiAcquireNonPagedResources(v_rip + 1938941, 1, a3, 1);
    a3 = 0;
    a1 = 0;
    result = MiInitializePageColorBase(a1, 1 + 2, a3, v_stack_m18);
    a2 = 0;
    a3 = (v_stack_m10) >> (16);
    a3 = (unsigned int)((a3) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_stack_m10)));
    a2 = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(v_stack_m10)));
    result = MiGetPage(v_rip + 1938869, a2, 1 + 127, v_stack_m10);
    if (result == -1) {
        a1 = 1 + 1;
        result = MxInstallMoreMemory(a1, a2, 1 + 127, v_stack_m10);
    }
    v_rdi = (result + result * 2) << (4);
    v_rdi = (v_rdi) + (result);
    a3 = 0;
    a2 = 0;
    result = MiSetPfnTbFlushStamp(v_rdi, a2, a3, v_stack_m10);
    *(unsigned __int64 *)(v_rdi + 8) = result;
    result = MiLockPageInline(v_rdi, a2, a3, v_stack_m10);
    result = MiMakeDemandZeroPte(4, a2, a3, v_stack_m10);
    *(unsigned __int64 *)(v_rdi + 16) = result;
    a2 = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    v_stack_p8 = 2;
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) | (7));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) | (32));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) | (8));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = (*(unsigned __int64 *)(v_rdi + 40)) & ((unsigned int)(v_stack_p8));
    *(unsigned __int64 *)(v_rdi + 40) = result;
    result = MiSetPfnContainingFrame(v_rdi, a2, a3, v_stack_m10);
    result = MiUnlockPage(v_rdi, (unsigned __int8)((unsigned __int8)(result)), a3, v_stack_m10);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateDummyPage(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;
    uint8_t v_stack_pA;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg3 = 0;
    v_stack_m18 = v_xmm0;
    result = MiAcquireNonPagedResources(v_rip + 1938941, 1, Arg3, 1);
    Arg3 = 0;
    Arg1 = 0;
    result = MiInitializePageColorBase(Arg1, 1 + 2, Arg3, v_stack_m18);
    Arg2 = 0;
    Arg3 = (v_stack_m10) >> (16);
    Arg3 = (uint32_t)((Arg3) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(v_stack_m10)));
    Arg2 = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(v_stack_m10)));
    result = MiGetPage(v_rip + 1938869, Arg2, 1 + 127, v_stack_m10);
    if (result == -1) {
        Arg1 = 1 + 1;
        result = MxInstallMoreMemory(Arg1, Arg2, 1 + 127, v_stack_m10);
    }
    local_rdi = (result + result * 2) << (4);
    local_rdi = (local_rdi) + (result);
    Arg3 = 0;
    Arg2 = 0;
    result = MiSetPfnTbFlushStamp(local_rdi, Arg2, Arg3, v_stack_m10);
    *(uint64_t *)(local_rdi + 0x8) = result;
    result = MiLockPageInline(local_rdi, Arg2, Arg3, v_stack_m10);
    result = MiMakeDemandZeroPte(4, Arg2, Arg3, v_stack_m10);
    *(uint64_t *)(local_rdi + 0x10) = result;
    Arg2 = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    v_stack_p8 = 2;
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) | (7));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) | (32));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) | (8));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = (*(uint64_t *)(local_rdi + 0x28)) & ((uint32_t)(v_stack_p8));
    *(uint64_t *)(local_rdi + 0x28) = result;
    result = MiSetPfnContainingFrame(local_rdi, Arg2, Arg3, v_stack_m10);
    result = MiUnlockPage(local_rdi, (uint8_t)((uint8_t)(result)), Arg3, v_stack_m10);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5F6E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C5F6E8[BB_00C5F6E8]
  bb_00C5F775[BB_00C5F775]
  bb_00C5F77E[BB_00C5F77E]
  bb_00C5F85F[BB_00C5F85F]
  bb_00C5F6E8 -->|branch| bb_00C5F77E
  bb_00C5F6E8 -->|fallthrough| bb_00C5F775
  bb_00C5F775 -->|flow| bb_00C5F77E
```
