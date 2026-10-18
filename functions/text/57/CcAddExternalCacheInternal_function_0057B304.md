# CcAddExternalCacheInternal

- RVA: `0x0057B304`–`0x0057B392` (길이 `142` bytes)
- VA: `0x000000014057B304`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5770`
- 디코드: `38`개 명령, `142/142` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0057B31B` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0057B362` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0057B38C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcRegisterExternalCache](CcRegisterExternalCache_function_0057BFC0.md) at `0x0057C056`

### Static image references
- `0x0057B314` → RVA `0x00F8F5D0` (`.data`; read)
- `0x0057B337` → RVA `0x00F8F500` (`.data`; read)
- `0x0057B352` → RVA `0x00F8F500` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057B304  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0057B309  57                              push rdi
0057B30A  48 83 EC 30                     sub rsp, 0x30
0057B30E  48 8B D9                        mov rbx, rcx
0057B311  48 8B FA                        mov rdi, rdx
0057B314  48 8D 0D B5 42 A1 00            lea rcx, [rip + 0xa142b5]
0057B31B  E8 50 D1 C8 FF                  call 0x140208470
0057B320  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0057B324  48 83 C3 20                     add rbx, 0x20
0057B328  44 8A C0                        mov r8b, al
0057B32B  48 39 39                        cmp qword ptr [rcx], rdi
0057B32E  74 07                           je 0x14057b337
0057B330  B9 03 00 00 00                  mov ecx, 3
0057B335  CD 29                           int 0x29
0057B337  8B 05 C3 41 A1 00               mov eax, dword ptr [rip + 0xa141c3]
0057B33D  48 89 3B                        mov qword ptr [rbx], rdi
0057B340  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
0057B344  48 89 19                        mov qword ptr [rcx], rbx
0057B347  8D 50 01                        lea edx, [rax + 1]
0057B34A  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
0057B34E  3B D0                           cmp edx, eax
0057B350  76 21                           jbe 0x14057b373
0057B352  89 15 A8 41 A1 00               mov dword ptr [rip + 0xa141a8], edx
0057B358  48 8D 0D 71 42 A1 00            lea rcx, [rip + 0xa14271]
0057B35F  41 8A D0                        mov dl, r8b
0057B362  E8 39 78 E1 FF                  call 0x140392ba0
0057B367  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0057B36C  48 83 C4 30                     add rsp, 0x30
0057B370  5F                              pop rdi
0057B371  C3                              ret
0057B372  CC                              int3
0057B373  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0057B379  45 33 C9                        xor r9d, r9d
0057B37C  BA 27 1E 00 00                  mov edx, 0x1e27
0057B381  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0057B388  41 8D 49 34                     lea ecx, [r9 + 0x34]
0057B38C  E8 CF 22 F8 FF                  call 0x1404fd660
0057B391  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcAddExternalCacheInternal(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10568373, a2, a3, a4);
    v_rbx = (a1) + (32);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) != a2) {
        a1 = 3;
    }
    *(unsigned __int64 *)(v_rbx) = a2;
    *(unsigned __int64 *)(v_rbx + 8) = a1;
    *(unsigned __int64 *)(a1) = v_rbx;
    *(unsigned __int64 *)(a2 + 8) = v_rbx;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10568131)) + 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10568131))))) goto loc_0057B373;
    *(unsigned int *)(v_rip + 10568104) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10568131)) + 1);
    result = KeReleaseSpinLock(v_rip + 10568305, (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)(result), a4);
    v_rsp = (v_rsp) + (48);
    return result;
loc_0057B373:
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x1E27ULL), 0xFFFFFFFFC0000420ULL, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcAddExternalCacheInternal(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 10568373, Arg2, Arg3, Arg4);
    local_rbx = (Arg1) + (32);
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) != Arg2) {
        Arg1 = 3;
    }
    *(void **)(local_rbx) = Arg2;
    *(void **)(local_rbx + 0x8) = Arg1;
    *(uint64_t *)(arg1) = local_rbx;
    *(uint64_t *)(arg2 + 0x8) = local_rbx;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA141C3)) + 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA141C3))))) goto loc_0057B373;
    *(uint32_t *)(v_rip + 0xA141A8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA141C3)) + 1);
    result = KeReleaseSpinLock(v_rip + 10568305, (uint8_t)((uint8_t)(result)), (uint8_t)(result), Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
loc_0057B373:
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0x1E27ULL), 0xFFFFFFFFC0000420ULL, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057B304&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057B304[BB_0057B304]
  bb_0057B330[BB_0057B330]
  bb_0057B337[BB_0057B337]
  bb_0057B352[BB_0057B352]
  bb_0057B372[BB_0057B372]
  bb_0057B373[BB_0057B373]
  bb_0057B304 -->|branch| bb_0057B337
  bb_0057B304 -->|fallthrough| bb_0057B330
  bb_0057B330 -->|flow| bb_0057B337
  bb_0057B337 -->|branch| bb_0057B373
  bb_0057B337 -->|fallthrough| bb_0057B352
  bb_0057B372 -->|flow| bb_0057B373
```
