# MiReuseStandbyPage

- RVA: `0x0044CA90`–`0x0044CB04` (길이 `116` bytes)
- VA: `0x000000014044CA90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A689C`
- 디코드: `34`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0044CAA6` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x0044CAB2` → [MiRestoreTransitionPte](../33/MiRestoreTransitionPte_function_0033DD90.md) (function, `0x0033DD90`)
- `0x0044CAD5` → [MiClearPfnReuseFields](../37/MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x0044CAE8` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)

### Direct callers
- [MiTradePage](../28/MiTradePage_function_0028D160.md) at `0x0028D88E`
- [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) at `0x00365A65`
- [MiSwapNumaStandbyPage](../38/MiSwapNumaStandbyPage_function_00385144.md) at `0x00385659`
- [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) at `0x00404A03`
- [MiHandleSpecialPurposeMemoryCachedFault](MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044C87E`

### Static image references
- `0x0044CADA` → RVA `0x00010880` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044CA90  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0044CA95  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0044CA99  57                              push rdi
0044CA9A  48 83 EC 20                     sub rsp, 0x20
0044CA9E  BA 04 00 00 00                  mov edx, 4
0044CAA3  48 8B F9                        mov rdi, rcx
0044CAA6  E8 E5 AA E3 FF                  call 0x140287590
0044CAAB  33 D2                           xor edx, edx
0044CAAD  48 8B CF                        mov rcx, rdi
0044CAB0  8B D8                           mov ebx, eax
0044CAB2  E8 D9 12 EF FF                  call 0x14033dd90
0044CAB7  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
0044CABA  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0044CABE  C1 EA 10                        shr edx, 0x10
0044CAC1  80 E2 FD                        and dl, 0xfd
0044CAC4  80 CA 05                        or dl, 5
0044CAC7  88 54 24 3A                     mov byte ptr [rsp + 0x3a], dl
0044CACB  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
0044CACF  89 4F 20                        mov dword ptr [rdi + 0x20], ecx
0044CAD2  48 8B CF                        mov rcx, rdi
0044CAD5  E8 16 8F F2 FF                  call 0x1403759f0
0044CADA  48 8B 05 9F 3D BC FF            mov rax, qword ptr [rip - 0x43c261]
0044CAE1  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0044CAE5  48 89 01                        mov qword ptr [rcx], rax
0044CAE8  E8 AF DE E3 FF                  call 0x14028a99c
0044CAED  33 C0                           xor eax, eax
0044CAEF  F6 C3 03                        test bl, 3
0044CAF2  48 89 07                        mov qword ptr [rdi], rax
0044CAF5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0044CAFA  0F 94 C0                        sete al
0044CAFD  48 83 C4 20                     add rsp, 0x20
0044CB01  5F                              pop rdi
0044CB02  C3                              ret
0044CB03  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReuseStandbyPage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p12;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (32);
    result = MiUnlinkPageFromListEx(a1, 4, a3, a4);
    a2 = 0;
    result = MiRestoreTransitionPte(a1, a2, a3, a4);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    a2 = (unsigned __int8)((a2) & (253));
    a2 = (unsigned __int8)((a2) | (5));
    v_stack_p12 = (unsigned __int8)(a2);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p10));
    result = MiClearPfnReuseFields(a1, a2, a3, a4);
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(v_rip - 4440673);
    result = MiSetOriginalPtePfnFromFreeList(a1 + 16, a2, a3, a4);
    result = 0;
    *(unsigned __int64 *)(a1) = 0;
    result = ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (3)) == 0) ? 1 : 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReuseStandbyPage(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint8_t v_stack_p12;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (32);
    result = MiUnlinkPageFromListEx(Arg1, 4, a3, a4);
    Arg2 = 0;
    result = MiRestoreTransitionPte(Arg1, Arg2, a3, a4);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    Arg2 = (uint8_t)((Arg2) & (253));
    Arg2 = (uint8_t)((Arg2) | (5));
    v_stack_p12 = (uint8_t)(Arg2);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p10));
    result = MiClearPfnReuseFields(Arg1, Arg2, a3, a4);
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(v_rip - 0x43C261);
    result = MiSetOriginalPtePfnFromFreeList(Arg1 + 16, Arg2, a3, a4);
    result = 0;
    *(uint64_t *)(arg1) = 0;
    result = ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (3)) == 0) ? 1 : 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044CA90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044CA90[BB_0044CA90]
  bb_0044CB03[BB_0044CB03]
```
