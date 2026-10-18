# PiAllocateDeviceObjectList

- RVA: `0x00A078B4`–`0x00A0791B` (길이 `103` bytes)
- VA: `0x0000000140A078B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FD80`
- 디코드: `30`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A078E3` → [PnpAllocateCriticalMemory](PnpAllocateCriticalMemory_function_00A07924.md) (function, `0x00A07924`)
- `0x00A07914` → [PiClearDeviceObjectList](PiClearDeviceObjectList_function_00A09AD0.md) (function, `0x00A09AD0`)

### Direct callers
- [PipGrowDeviceObjectList](PipGrowDeviceObjectList_function_00A04620.md) at `0x00A04648`
- [IopAllocateRelationList](IopAllocateRelationList_function_00A0784C.md) at `0x00A0788C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A078B4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A078B9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A078BE  57                              push rdi
00A078BF  48 83 EC 20                     sub rsp, 0x20
00A078C3  8D 04 52                        lea eax, [rdx + rdx*2]
00A078C6  8B FA                           mov edi, edx
00A078C8  8D 04 C5 F8 FF FF FF            lea eax, [rax*8 - 8]
00A078CF  BA 00 01 00 00                  mov edx, 0x100
00A078D4  4C 63 C0                        movsxd r8, eax
00A078D7  41 B9 50 6E 70 54               mov r9d, 0x54706e50
00A078DD  49 83 C0 18                     add r8, 0x18
00A078E1  8B F1                           mov esi, ecx
00A078E3  E8 3C 00 00 00                  call 0x140a07924
00A078E8  48 8B D8                        mov rbx, rax
00A078EB  48 85 C0                        test rax, rax
00A078EE  75 14                           jne 0x140a07904
00A078F0  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00A078F5  48 8B C3                        mov rax, rbx
00A078F8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A078FD  48 83 C4 20                     add rsp, 0x20
00A07901  5F                              pop rdi
00A07902  C3                              ret
00A07903  CC                              int3
00A07904  83 20 00                        and dword ptr [rax], 0
00A07907  48 8B CB                        mov rcx, rbx
00A0790A  83 60 08 00                     and dword ptr [rax + 8], 0
00A0790E  89 70 0C                        mov dword ptr [rax + 0xc], esi
00A07911  89 78 04                        mov dword ptr [rax + 4], edi
00A07914  E8 B7 21 00 00                  call 0x140a09ad0
00A07919  EB D5                           jmp 0x140a078f0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiAllocateDeviceObjectList(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a3 = ((int)((unsigned int)(a2 + a2 * 2 * 8 - 8))) + (24);
    result = PnpAllocateCriticalMemory(a1, 256, a3, (unsigned int)(0x54706E50ULL));
    if (result != 0) goto loc_00A07904;
loc_00A078F0:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A07904:
    *(unsigned int *)(result + 12) = (unsigned int)(v_stack_p10);
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)((unsigned int)(a2)));
    result = PiClearDeviceObjectList(v_stack_p8, 256, a3, (unsigned int)(0x54706E50ULL));
    goto loc_00A078F0;
}
```

## 5. (Beta) C Style

```c
int64_t PiAllocateDeviceObjectList(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    a3 = ((int32_t)((uint32_t)(Arg2 + Arg2 * 2 * 8 - 8))) + (24);
    result = PnpAllocateCriticalMemory(Arg1, 256, a3, (uint32_t)(0x54706E50ULL));
    if (result != 0) goto loc_00A07904;
loc_00A078F0:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A07904:
    *(uint32_t *)(result + 0xC) = (uint32_t)(v_stack_p10);
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)((uint32_t)(Arg2)));
    result = PiClearDeviceObjectList(v_stack_p8, 256, a3, (uint32_t)(0x54706E50ULL));
    goto loc_00A078F0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rdx*2` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A078B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A078B4[BB_00A078B4]
  bb_00A078F0[BB_00A078F0]
  bb_00A07903[BB_00A07903]
  bb_00A07904[BB_00A07904]
  bb_00A078B4 -->|branch| bb_00A07904
  bb_00A078B4 -->|fallthrough| bb_00A078F0
  bb_00A07903 -->|flow| bb_00A07904
  bb_00A07904 -->|branch| bb_00A078F0
```
