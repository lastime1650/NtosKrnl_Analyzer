# SshpCacheInitializeLibraryCache

- RVA: `0x00AD0D30`–`0x00AD0D75` (길이 `69` bytes)
- VA: `0x0000000140AD0D30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `19`개 명령, `69/69` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AD0D61` → [RtlInitializeGenericTableAvl](../../text/46/RtlInitializeGenericTableAvl_function_00466100.md) (function, `0x00466100`)

### Direct callers
- [SleepstudyHelperCreateLibraryEx](../../text/4B/SleepstudyHelperCreateLibraryEx_function_004BAE50.md) at `0x004BAF0B`

### Static image references
- `0x00AD0D4C` → RVA `0x00A78840` (`SshpCacheDatabaseFree`; read)
- `0x00AD0D53` → RVA `0x00A7AF60` (`SshpCacheDatabaseAllocate`; read)
- `0x00AD0D5A` → RVA `0x009725D0` (`SshpCacheDatabaseCompare`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AD0D61` → [RtlInitializeGenericTableAvl](../../text/46/RtlInitializeGenericTableAvl_function_00466100.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD0D30  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AD0D35  57                              push rdi
00AD0D36  48 83 EC 30                     sub rsp, 0x30
00AD0D3A  8B FA                           mov edi, edx
00AD0D3C  48 8B D9                        mov rbx, rcx
00AD0D3F  85 D2                           test edx, edx
00AD0D41  74 23                           je 0x140ad0d66
00AD0D43  48 83 C1 30                     add rcx, 0x30
00AD0D47  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AD0D4C  4C 8D 0D ED 7A FA FF            lea r9, [rip - 0x58513]
00AD0D53  4C 8D 05 06 A2 FA FF            lea r8, [rip - 0x55dfa]
00AD0D5A  48 8D 15 6F 18 EA FF            lea rdx, [rip - 0x15e791]
00AD0D61  E8 9A 53 99 FF                  call 0x140466100
00AD0D66  89 7B 2C                        mov dword ptr [rbx + 0x2c], edi
00AD0D69  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AD0D6E  48 83 C4 30                     add rsp, 0x30
00AD0D72  5F                              pop rdi
00AD0D73  C3                              ret
00AD0D74  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpCacheInitializeLibraryCache(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if (a2 != 0) {
        a1 = (a1) + (48);
        v_stack_m18 = a1;
        a4 = v_rip - 361747;
        a3 = v_rip - 351738;
        a2 = v_rip - 1435537;
        result = RtlInitializeGenericTableAvl(a1, a2, a3, a4);
    }
    *(unsigned int *)(a1 + 44) = (unsigned int)((unsigned int)(a2));
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SshpCacheInitializeLibraryCache(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if (Arg2 != 0) {
        Arg1 = (Arg1) + (48);
        v_stack_m18 = Arg1;
        a4 = v_rip - 361747;
        a3 = v_rip - 351738;
        Arg2 = v_rip - 1435537;
        result = RtlInitializeGenericTableAvl(Arg1, Arg2, a3, a4);
    }
    *(uint32_t *)(arg1 + 0x2C) = (uint32_t)((uint32_t)(Arg2));
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD0D30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AD0D30[BB_00AD0D30]
  bb_00AD0D43[BB_00AD0D43]
  bb_00AD0D66[BB_00AD0D66]
  bb_00AD0D74[BB_00AD0D74]
  bb_00AD0D30 -->|branch| bb_00AD0D66
  bb_00AD0D30 -->|fallthrough| bb_00AD0D43
  bb_00AD0D43 -->|flow| bb_00AD0D66
```
